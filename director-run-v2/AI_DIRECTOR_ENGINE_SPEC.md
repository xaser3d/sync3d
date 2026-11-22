# AI Director Decomposition Engine — Technical Specification

Status: **proposed — awaiting approval**. Derived from `Script/rework/HALF_CHARGED_director_analysis.md` and `Script/rework/HALF_CHARGED_S30_audit.md`. Nothing in this document authorizes DB writes, card creation, or pipeline changes.

## 1. Core principle

The unit of decomposition is the **director's event**, not the dialogue line.

A director's event is: an image, an action, a state change, a reaction, a sound, a pause, a spatial relationship, or an information reveal — anything the audience must see or hear for the scene to function. Dialogue coverage is a *consequence* of event coverage, not its driver.

The 586-card baseline proves the failure mode of line-driven decomposition: ~64.7% of cards (379, reproducible via `image_prompt LIKE '%faces%speaks%'`) are the auto-paired "speaker + interlocutor" scheme, which fabricates co-presence (remote/V.O. speakers blocked in frame), drops principals from blocking (the frozen A.V.A. absent from her own statue shot), merges impossible geography (mezzanine + dance floor), and flattens time (ten seconds of dead air as one card).

## 2. Pipeline

```
Full screenplay (44 scenes: dialogue, action, direction, sound)
        │
        ▼
1. Director's understanding          — dramaturgy, arcs, motifs, space, causality
        │                              (global pass over whole script; inferences
        ▼                               labeled, never merged into facts)
2. Director's events                 — actions, reveals, reactions, pauses,
        │                              sound events, transitions (nested timelines)
        ▼
3. Shot sequences                    — wides, details, reactions, moves, edit links
        │
        ▼
4. Studio draft cards                — drafts → validation → director edit → approve
        │                              → materialize → existing pipeline
        ▼
   (existing readiness/queue/render guards — unchanged)
```

Three counts are always kept separate: **events** (dramaturgical units), **visual shots** (proposed coverage), **sound cards** (audio-state entries — not visual shots) and later **cards** (Studio artifacts). One event may produce several shots (S30 artifact: 16 events → 19 visual shots + 1 sound card); one shot may serve several events.

## 3. The event contract (minimal schema)

```json
{
  "event_id": "s30.e09",
  "scene_id": 30,
  "source_evidence": ["Ten seconds of dead air. Damien holds the frozen android in the middle of the dance floor."],
  "evidence_kind": "verbatim",          // verbatim | inferred | interpreted
  "dramatic_function": "held catastrophe — the room must feel the ten seconds",
  "participants": ["DAMIEN", "A.V.A."],  // physically present ONLY
  "remote_participants": [{"actor": "MAYA", "channel": "earpiece", "direction": "out"}],
  "location": {"set": "GRAND HOTEL — CHARITY GALA", "zone": "dance floor center"},
  "timeline": [
    {"beat": "quarter stumbles", "type": "sound"},
    {"beat": "silence", "type": "sound", "duration": "~10s"},
    {"beat": "300 guests turn", "type": "reaction"},
    {"beat": "Damien holds pose", "type": "held_action"},
    {"beat": "Jim materializes, white", "type": "reaction"}
  ],
  "visual_requirements": ["statue tableau readable in one wide", "crowd turn as separate frame"],
  "audio_requirements": ["quartet stumble → dead air", "no score underneath"],
  "continuity_constraints": ["axis: Damien frame-left, A.V.A. frame-right", "A.V.A. frozen mid-dip, eyes open"],
  "ambiguities": ["10s written vs ~6-7s playable — director decision"],
  "shot_sequence": [
    {"shot": "W", "purpose": "statue tableau", "events": ["s30.e08", "s30.e09"]},
    {"shot": "R", "purpose": "300 turning", "events": ["s30.e09"]},
    {"shot": "CU", "purpose": "Damien holds", "events": ["s30.e09"]}
  ]
}
```

### Field rules (v2)
- `source_evidence` — verbatim spans (strings, or `{text, lines:[a,b]}` when line ranges are available) **bound to this scene's section** of the screenplay; a span that exists only in another scene fails validation. `evidence_kind` applies per-assertion (`verbatim | inferred | interpreted`); a mixed event splits its assertions or carries per-item kinds.
- **Presence taxonomy — four distinct kinds, never interchangeable:**
  - `participants` — physically in the scene space.
  - `remote_participants` — live communication channel: `{actor, channel: earpiece|phone|vo|screen|wallscreen, direction}`.
  - `depicts_via_channel` — seen through an image/monitor/lens/feed: `{actors|object, seen_by, channel, from_zone}`. Depicted subjects are NOT participants.
  - `document_evidence` — presence through artifact: handwriting, photo, recording, prop — `{author|subject, artifact, channel:"document"}`. A handwritten note is document presence, not remote speech.
- `timeline` — ordered beats; each may carry `duration`. `shot_sequence` is **ordered**: it states the intended implementation order (instruction → reaction → action), not just a set of covering shots.
- `coverage` — per-scene registry: every meaningful screenplay paragraph gets a disposition — `covered_by:[event_ids]` | `embodied_in:[event_ids]` | `omitted:reason` | `flagged_for_director`. Nothing is silently uncovered.
- `ambiguities` — screenplay gaps and interpretation risks surfaced for human decision; never auto-resolved (e.g. brake-line authorship S20 — neutral coverage until director rules). Interpretive claims (e.g. "the partner in the pose is Maya") live here or under `evidence_kind:"interpreted"` — never as verbatim facts.

## 4. Validator (deterministic, no creative judgment)

Implemented in v1 (executable, `director_run/validator.py`): evidence substring, cast, remote-not-in-frame, principal presence (must_appear/tableau), beat coverage, sound surfacing, dialogue addressing, link existence.

**v2 upgrades — required before the 44-scene run:**

| Rule | v1 gap | v2 requirement |
|---|---|---|
| Evidence | span searched in the WHOLE screenplay — could pass with text from another scene | span must be a substring of **this scene's section** + bound to line range |
| Coverage | no completeness check — whole events could be missing silently | **coverage registry**: every meaningful paragraph gets a disposition (covered/embodied/omitted/flagged); uncovered paragraphs are violations |
| Links | one direction only (shot→event, event→shot-id exists) | **bidirectional**: `shot.implements ⊆ event.shot_sequence` AND vice versa — a shot can't claim an event the event doesn't list |
| Order/duration | covers_beats treated as set — [3,0,2] passes | beat order must follow `shot_sequence` order; beats with `duration` require duration-bearing shots or sound cards |
| Sound | any non-empty audio_note passed | each `audio_requirement` must match content in an implementing shot's audio_note or a sound card's purpose |
| Dialogue | only recipient presence checked | speaker membership (participants∪remote), **per-line uniqueness** — one line lives on exactly one shot |
| Geography | zone ∈ declared list only | shot.zone must agree with its events' `location.zone` (single-zone events); cross-zone only via declared depicts/channel |
| Participants | only must_appear checked | all declared `participants` must be covered across the event's shots (non-tableau actors may appear in different shots) |
| Cast | hardcoded list | cast read from the project's approved source (DB `virtual_actors`), not the validator's own table |
| Continuity | **specified but NOT implemented in v1** | axis/prop/costume constraints: flagged `continuity_constraints` must be carried — implementation target for v2; until then reported as unverified |

Validator output is a report — violations list, unassigned elements list, ambiguity list, **unverified list** (constraints it cannot yet check). It never silently repairs; unassigned means unassigned until a human or the director model assigns it. PASS means "passed the implemented checks", not "artistically correct".

## 5. Roles

- **SWE-2 High (director intelligence)** — reads the whole screenplay; produces the understanding layer, then per-scene event structures and shot sequences as schema-valid JSON. Runs outside Studio during qualification — output is files, not DB rows. Later automation path (separate decision): CLI `-p`/`--prompt-file` batch or `devin acp` bridge.
- **Regex/heuristic analyzer (`coverage_analyzer`)** — demoted to signaler. May flag suspicious spots (unmatched speakers, unmapped text spans) for review. **Forbidden:** auto-assigning interlocutors, fabricating presence, or acting as source of truth.
- **Validator** — structure/evidence/geography/continuity checks above.
- **Studio** — Coverage Review UI presents events+shots for edit/approve; existing materialize/readiness/queue/render guards unchanged downstream.

## 6. Qualification — four mandatory cases (from HALF CHARGED)

| Case | Must preserve |
|---|---|
| **S30 charity gala** | geography, the swap mechanics, battery 14→3%, the dancing couple, 300-guest reaction, quartet/dead-air sound dramaturgy |
| **S22 proximity event** | the gesture, the four-second duration, physical contact, the mutual non-registration as meaning |
| **S23 +47 MIN** | A.V.A.'s schedule change read as an *act of care*, not only a UI insert |
| **S6 kitchen 3:11 AM** | atmosphere, prop details, sound, action — without binding every frame to a line |

**Pass criterion** (not shot-count match): zero fabricated presences, zero lost principals, zero impossible geography, zero lost director's events.

## 7. Isolated first run (before any Studio connection)

1. SWE-2 High produces event+shot JSON for all 44 scenes → artifact files only.
2. Validator runs the rule set → violation/unassigned/ambiguity report.
3. Coverage report: which actions, atmospheric details, and sound events received no assignment.
4. Comparison vs the 586 cards — **analysis only**. No migration, no DB writes, no card edits.

## 8. Hard constraints

- Project 8, the production DB, existing cards, and the working pipeline remain untouched until a separate explicit approval.
- The engine proposes; only human approval materializes.
- Interpretations are labeled, ambiguities are escalated, unassigned elements are reported — never silently filled.
- Mass card generation is a later, separate decision after the spec and the isolated run are approved.
