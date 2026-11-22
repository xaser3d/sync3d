"""Validator v2 for director-event JSON artifacts — AI Director Engine spec.

v2 upgrades over v1: scene-scoped evidence, coverage registry, bidirectional
links, beat order/duration, sound content matching, dialogue speaker +
per-line uniqueness, zone consistency, full participant coverage, cast from
the project DB, document_evidence presence kind, unverified list.

Read-only: loads screenplay + artifacts + cast from studio_core.db (project 8),
writes validator_report.md.
"""
from __future__ import annotations

import json
import re
import sqlite3
from pathlib import Path

RUN = Path(__file__).parent
SCREENPLAY = RUN.parent / "HALF_CHARGED_screenplay.md"
REPORT = RUN / "validator_report.md"
DB = RUN.parent.parent.parent / "studio_core.db"
PROJECT_ID = 8

EXTRAS = {"GUESTS", "QUARTET", "TRUSTEES", "BUYERS", "LAWYERS", "EXECUTIVES",
          "COURIERS", "PRESS", "WAITERS"}
ALIAS = {"SOPHIA VANE": "SOPHIA", "OCTAVIA MARLOWE": "OCTAVIA",
         "ANNA REYES": "ANNA", "MAYA-A.V.A.": "MAYA"}
STOP = {"a", "an", "the", "of", "to", "in", "on", "and", "or", "is", "it",
        "its", "as", "be", "by", "at", "no", "not", "his", "her", "under",
        "with", "into", "that", "this", "only", "own", "s", "for"}


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def tokens(s: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in STOP}


def load_cast() -> set[str]:
    try:
        conn = sqlite3.connect(DB)
        names = {r[0].upper() for r in conn.execute(
            "SELECT name FROM virtual_actors WHERE project_id=?", (PROJECT_ID,))}
        conn.close()
    except Exception:
        names = set()
    cast = names | EXTRAS | set(ALIAS)
    return cast


def scene_section(doc: str, scene_id: int) -> str:
    m = re.search(rf"^## SCENE {scene_id}\b.*$", doc, re.M)
    if not m:
        return ""
    nxt = re.search(r"^## SCENE ", doc[m.end():], re.M)
    return doc[m.end(): m.end() + nxt.start()] if nxt else doc[m.end():]


def paragraphs(section: str) -> list[str]:
    out = []
    for p in re.split(r"\n\s*\n", section):
        p = p.strip().strip("*").strip()
        if len(norm(p)) > 25 and not p.startswith("##"):
            out.append(p)
    return out


def canon(actor: str) -> str:
    return ALIAS.get(actor, actor)


def check_scene(doc: str, data: dict, cast: set[str]) -> list[tuple]:
    rep = []
    events = {e["event_id"]: e for e in data["events"]}
    shots = {s["shot_id"]: s for s in data["shots"]}
    zones = data.get("zones", [])
    section = scene_section(doc, data["scene_id"])
    nsec = norm(section)
    if not section:
        rep.append(("FAIL", "scene-scope", "—", f"scene {data['scene_id']} section not found"))
        return rep

    # --- per-event checks ---
    for eid, ev in events.items():
        # evidence scoped to THIS scene
        for item in ev.get("source_evidence", []):
            span = item["text"] if isinstance(item, dict) else item
            if norm(span) not in nsec:
                rep.append(("FAIL", "evidence-scoped", eid, f"span not in scene {data['scene_id']}: {span[:60]!r}"))
        # cast
        for a in ev.get("participants", []):
            if canon(a) not in cast:
                rep.append(("FAIL", "cast", eid, f"participant not in cast: {a}"))
        for r in ev.get("remote_participants", []):
            if canon(r["actor"]) not in cast:
                rep.append(("FAIL", "cast", eid, f"remote actor not in cast: {r['actor']}"))
            if not r.get("channel"):
                rep.append(("FAIL", "presence-kind", eid, "remote participant without channel"))
        for d in ev.get("depicts_via_channel", []):
            if not d.get("channel"):
                rep.append(("FAIL", "presence-kind", eid, "depicted subject without channel"))
            for a in d.get("actors", []) + d.get("seen_by", []):
                if canon(a) not in cast:
                    rep.append(("FAIL", "cast", eid, f"depicted actor not in cast: {a}"))
        for d in ev.get("document_evidence", []):
            who = d.get("author") or d.get("subject")
            if who and canon(who) not in cast:
                rep.append(("FAIL", "cast", eid, f"document author not in cast: {who}"))
            if d.get("channel") != "document":
                rep.append(("FAIL", "presence-kind", eid, "document_evidence without channel='document'"))
        # remote never co-present in participants
        remote = {r["actor"] for r in ev.get("remote_participants", [])}
        if remote & set(ev.get("participants", [])):
            rep.append(("FAIL", "remote-in-frame", eid, f"remote actor in participants: {remote & set(ev['participants'])}"))
        # all participants covered across implementing shots
        impl = [shots[s] for s in ev.get("shot_sequence", []) if s in shots and shots[s].get("type") != "sound"]
        covered = set().union(*(set(s.get("participants", [])) for s in impl)) if impl else set()
        miss = set(ev.get("participants", [])) - covered - set(ev.get("offscreen_present", []))
        if miss:
            rep.append(("FAIL", "participant-coverage", eid, f"declared participants never appear in shots: {sorted(miss)}"))
        # tableau single-frame
        req = set(ev.get("must_appear", []))
        if ev.get("tableau") and req and not any(req <= set(s.get("participants", [])) for s in impl):
            rep.append(("FAIL", "principal-presence", eid, f"tableau has no shot containing {sorted(req)}"))
        # remote actors not inside implementing shots' physical frame
        for s in impl:
            ov = remote & set(s.get("participants", []))
            if ov:
                rep.append(("FAIL", "remote-in-frame", eid, f"{s['shot_id']} puts remote {ov} in physical frame"))
        # beat coverage + order
        tl = ev.get("timeline", [])
        if tl:
            first_at = {}
            for pos, sid in enumerate(ev.get("shot_sequence", [])):
                sh = shots.get(sid)
                if not sh or sh.get("type") == "sound":
                    continue
                cb = sh.get("covers_beats", {})
                idxs = cb.get(eid, cb if isinstance(cb, list) else [])
                for i in idxs:
                    first_at.setdefault(i, pos)
            missing = set(range(len(tl))) - set(first_at)
            if missing:
                rep.append(("FAIL", "time-structure", eid, f"timeline beats {sorted(missing)} uncovered"))
            else:
                order = [first_at[i] for i in sorted(first_at)]
                if order != sorted(order):
                    rep.append(("FAIL", "beat-order", eid, f"beats appear out of order in shot_sequence: {order}"))
            # duration: any beat with duration needs a duration-bearing shot/sound card
            if any(b.get("duration") for b in tl):
                ok = any(shots[s].get("duration_note") or
                         (shots[s].get("type") == "sound" and shots[s].get("duration_note"))
                         for s in ev.get("shot_sequence", []) if s in shots)
                if not ok:
                    rep.append(("FAIL", "duration", eid, "duration-bearing beats but no shot declares duration_note"))
        # sound content: each audio_requirement must share content tokens with
        # audio text of implementing shots (incl. sound cards)
        reqs = ev.get("audio_requirements", [])
        if reqs:
            audio_text = " ".join(
                " ".join([shots[s].get("audio_note", ""), shots[s].get("purpose", "")])
                for s in ev.get("shot_sequence", []) if s in shots)
            atoks = tokens(audio_text)
            for rtext in reqs:
                if not (tokens(rtext) & atoks):
                    rep.append(("FAIL", "sound-content", eid, f"audio_requirement unsurfaced: {rtext[:60]!r}"))
        # zone agreement: shot.zone must be among the event's declared zones
        loc = ev.get("location", {})
        ezones = set(loc.get("zones") or ([loc["zone"]] if loc.get("zone") else []))
        if ezones:
            for s in impl:
                if len(s.get("implements", [])) == 1 and s.get("zone") not in ezones:
                    rep.append(("FAIL", "zone-agreement", eid, f"{s['shot_id']} zone {s.get('zone')!r} not in event zones {sorted(ezones)}"))

    # --- per-shot checks ---
    lines_seen = {}
    for sid, sh in shots.items():
        if sh.get("type") == "sound":
            if not sh.get("implements"):
                rep.append(("FAIL", "link", sid, "sound card implements no event"))
            continue
        if sh.get("zone") not in zones:
            rep.append(("FAIL", "geography", sid, f"zone {sh.get('zone')!r} not declared"))
        if not sh.get("implements"):
            rep.append(("FAIL", "link", sid, "shot implements no event"))
        for eid in sh.get("implements", []):
            ev = events.get(eid)
            if not ev:
                rep.append(("FAIL", "link", sid, f"implements unknown event {eid}"))
            elif sid not in ev.get("shot_sequence", []):
                rep.append(("FAIL", "link-bidirectional", sid, f"claims {eid} but event's shot_sequence lacks {sid}"))
        for d in sh.get("depicts", []):
            if not d.get("channel"):
                rep.append(("FAIL", "presence-kind", sid, "depicted subject without channel"))
        dlg = sh.get("dialogue")
        if dlg:
            parts = set(sh.get("participants", []))
            remote_ok = set()
            for eid in sh.get("implements", []):
                ev = events.get(eid, {})
                remote_ok |= {r["actor"] for r in ev.get("remote_participants", [])}
            if dlg.get("recipient_presence") == "physical" and dlg.get("recipient") not in parts:
                rep.append(("FAIL", "dialogue-addressing", sid, f"recipient {dlg.get('recipient')} not in frame"))
            if dlg.get("line_kind") in ("earpiece", "vo") and dlg.get("speaker") not in remote_ok:
                rep.append(("FAIL", "dialogue-addressing", sid, f"{dlg['line_kind']} speaker {dlg['speaker']} not remote-declared"))
            if dlg.get("speaker") not in parts | remote_ok:
                rep.append(("FAIL", "dialogue-speaker", sid, f"speaker {dlg.get('speaker')} neither in frame nor remote"))
            line = norm(dlg.get("line", ""))
            if line:
                if line in lines_seen:
                    rep.append(("FAIL", "dialogue-unique", sid, f"line also on {lines_seen[line]}: {line[:50]!r}"))
                else:
                    lines_seen[line] = sid

    for eid, ev in events.items():
        for sid in ev.get("shot_sequence", []):
            if sid not in shots:
                rep.append(("FAIL", "link", eid, f"references missing shot {sid}"))

    # --- coverage registry ---
    cov = data.get("coverage", [])
    for c in cov:
        if norm(c.get("span", "")) not in nsec:
            rep.append(("FAIL", "coverage-span", "—", f"coverage span not in scene: {c.get('span','')[:60]!r}"))
        if c.get("disposition") not in ("covered_by", "embodied_in", "omitted", "flagged_for_director"):
            rep.append(("FAIL", "coverage-disposition", "—", f"bad disposition {c.get('disposition')!r}"))
        if c.get("disposition") in ("covered_by", "embodied_in"):
            for eid in c.get("by", []):
                if eid not in events:
                    rep.append(("FAIL", "coverage-link", "—", f"coverage points at unknown event {eid}"))
    for p in paragraphs(section):
        np_ = norm(p)
        hit = any(norm(c.get("span", "")) in np_ or np_ in norm(c.get("span", "")) for c in cov)
        if not hit:
            rep.append(("FAIL", "coverage-completeness", "—", f"paragraph uncovered: {np_[:80]!r}"))

    # --- unverified (reported, not failed) ---
    for eid, ev in events.items():
        for cc in ev.get("continuity_constraints", []):
            rep.append(("UNVERIFIED", "continuity", eid, cc[:80]))
        for a in ev.get("ambiguities", []):
            rep.append(("FLAG", "ambiguity", eid, a[:80]))
    return rep


def main() -> int:
    doc = SCREENPLAY.read_text(encoding="utf-8")
    cast = load_cast()
    all_rep, totals = [], {"events": 0, "shots": 0, "violations": 0}
    for path in sorted(RUN.glob("*.events.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        rep = check_scene(doc, data, cast)
        totals["events"] += len(data["events"])
        totals["shots"] += len(data["shots"])
        totals["violations"] += sum(1 for r in rep if r[0] == "FAIL")
        all_rep.append((path.name, data["scene_heading"], rep))

    lines = ["# Validator Report v2 — director_run artifacts", "",
             "Spec §4 v2. FAIL=violation, UNVERIFIED=constraint the validator cannot yet check, FLAG=director decision.", ""]
    for name, heading, rep in all_rep:
        lines.append(f"## {name} — {heading}")
        for status, label, eid, grounds in rep:
            if status != "PASS":
                lines.append(f"{status:<11} {label:<22} {eid:<10} {grounds}")
        lines.append(f"**scene violations: {sum(1 for r in rep if r[0]=='FAIL')}**")
        lines.append("")
    lines.append(f"## Totals: {totals['events']} events, {totals['shots']} shots/cards, {totals['violations']} violations")
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {REPORT} — {totals['violations']} violations")
    return 0 if totals["violations"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
