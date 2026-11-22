# VALIDATION PACKET 01 — R4 baseline acceptance
Role: independent reviewer. Verify claims vs data; do NOT rewrite or improve.
For each verdict cite the exact line/file that proves it. List what you could NOT verify.


========== FILE: director_review_final.md ==========

# HALF CHARGED v1 — AI Director Run v3.2 / R4
## Final Directorial Coverage Report (analytic baseline)

Status: **analytic baseline, review-complete on the sampled edge cases.**
Nothing in this document is a command to change Studio, production, `studio_core.db`,
queues, or any of the existing 586 cards. Migration requires a separate explicit
authorization, a dry-run, an ID mapping, and a rollback plan.

---

## 1. Revision lineage

| Rev | What changed | Manifest |
|---|---|---|
| v3.2 | Full-script baseline: 44 isolated `sNN_*.events.json`, contract v3.2, validator + 40 negative tests, 468 visual plans | `baseline_manifest_v32.json` (52 files) |
| R1 | Six resolved FLAGs → `resolved-decision` records; S44 card 6 rebuilt as a real frame | `baseline_manifest_v32_r1.json` |
| R2 | S07.sh11 split a/b/c (order: pretense → exchange → warmth); S33 sh05→sh04, sh23→sh22; trustee arc recorded | `baseline_manifest_v32_r2.json` |
| R3 | S34 sh02→sh01, sh09→sh08; rustle audio preserved in snd01; presence/link fixes required by validator | `baseline_manifest_v32_r3.json` |
| **R4** | **S35 sh01→sh02 (held breath inside the walk). Final reviewed baseline.** | **`baseline_manifest_v32_r4.json` (58 files, SHA-256)** |

All manifests coexist; none was overwritten. Historical FLAGs remain in the
frozen reports; resolved items carry `resolved-decision` with `basis` and
`consequence` plus a `resolved_from` pointer inside the artifacts.

## 2. Totals (R4)

| Metric | Value |
|---|---|
| Scenes | 44 / 44 — every screenplay paragraph covered |
| Director events | 288 |
| Visual plans | **465** |
| Sound cards | 42 |
| Verbatim dialogue lines registered | 471 (0 `dialogue-source` FLAGs — every line found verbatim in the screenplay) |
| Validator | **0 FAIL** |
| Negative tests | 40 / 40, exit 0 |
| FLAG | 38 (33 ambiguity, 4 beat-duplicate, 1 tableau-group) |
| UNVERIFIED | 525 (see §6) |
| Studio comparison | 465 vs 586 → **−121, analytic only** |

## 3. Comparison methodology (465 vs 586)

- Read-only (`mode=ro`) count of Studio cards per `script_scene_number`; no card
  content altered, no import attempted.
- Dialogue parity was checked first: registered lines track Studio dialogue
  cards within ±0–4 per scene everywhere → **the delta is coverage, not lines.**
- Classification is by line-presence and event-function, **not** by frame review.
  A card with no line can still carry a needed silent beat.
- **−121 must not be read as "121 cards to delete."** It is the arithmetic
  balance of two opposite effects: ≈−150 probable over-coverage in early/mid
  dialogue scenes, offset by ≈+35 probable under-coverage in the act-3
  set-piece (S33–S36, S30).

## 4. Five-scene semantic review (both edges of the delta)

Verdicts used four categories: **Keep / Merge / Delete-candidate / Needs viewing.**

### S03 — office pitch (Studio 17 → model 11, Δ−6)
- Outcome: **11 plans kept, no change.** Event grouping of the sales dialogue
  confirmed; the box/card insert (sh03), the "sex toy" CU (sh05), and the
  empty-chair beat (sh09) all carry distinct information.
- Studio defect found: **ghost cast** — i14's `blocking` lists PHOTOGRAPHER in a
  frame whose action is the *empty* chair he fled.

### S07 — morning call (Studio 27 → model 13 after split, Δ−14)
- Outcome: phone-call ping-pong (15 cards) merges to 4 plans; three information
  turns preserved as their own plans (serial read, weather-report rules,
  "I'm her mother"). The quiet A.V.A. beat was the one place Studio's
  granularity was right → **sh11 split into sh11a/b/c** (pretense →
  "How is she?"/"Loud." → warmth + "Yes.").
- Studio defects found: **cross-space eyelines** — MAYA "faces JIM" across
  lab↔penthouse (i08–i23); **blocking/dialogue desync** — i25 blocks DAMIEN but
  carries A.V.A.'s line; **focus swap inside another's card** — i07.

### S33 — gala trap (Studio 11 → model 21 after merges, Δ+10)
- Outcome: silent events Studio hid inside `action_description` became plans:
  establishers, detonation, Maya watching her own face, phones/press-release
  insert, Sophia-as-hostage, trustee math, chair silhouette + room turn.
- Merges: sh05 (laughter → inside the toast frame), sh23 (room turn → inside
  the chair reveal). Kept as distinct: the **trustee arc** laugh → stillness →
  math (sh08/sh12/sh21) recorded as three screenplay-justified states.

### S34 — A.V.A.'s defense (Studio 9 → model 15 after merges, Δ+6)
- Outcome: state-changes each earn a plan (silence tableau, defense landing,
  reframe on trustees vs on Damien, mic set-down, kill shot, landing of the
  numbers, eruption vs firmware counter).
- Merges: sh02 (room's attention → inside the descent W), sh09 (rustle →
  inside the defense coverage; **sound kept in snd01**).
- R1 consistency verified: mic set-down has its own insert (sh13), statistics
  unamplified (sh14–15), standing mic carried into S35.

### S35 — Damien's confession (Studio 10 → model 16 after merge, Δ+6)
- Outcome: S34/S35 boundary clean — no re-coverage; mic is the same physical
  object ("left standing" → Damien claims it). Documents kept as a three-stage
  prop choreography (takes → refuses → sets down: empire surrendered by hand);
  eyeline exchange sh07/sh08 kept.
- Merge: sh01 (held breath → inside the walk W).

## 5. Studio defects observed during review (record only, no fix action)

| Scene | Defect |
|---|---|
| S03 i14 | PHOTOGRAPHER in blocking of the empty-chair frame (ghost cast) |
| S07 i08–i23 | MAYA "faces JIM" — cross-location eyeline (lab ↔ penthouse) |
| S07 i25 | blocking DAMIEN / dialogue A.V.A. desync |
| S07 i07 | Damien's warranty-card action inside MAYA's card (focus swap) |
| S34/S35 pattern | named room-state beats (silence, rustle, laughter, applause, set-down) carried inside `action_description` of unrelated dialogue cards — invisible to per-card coverage logic |

## 6. UNVERIFIED — explicit limitation, not a defect count

525 entries, two families, unchanged by design:
- **continuity** — cross-shot spatial/screen-direction/prop continuity is not
  machine-checked (the validator has no continuity rules by intent);
- **beat-order-intrashot** — order of beats inside a shared take is not checked
  unless `beat_order` is declared.

Both families stay visible. No attempt was made to reach zero. Individual
entries may hide real continuity problems; they require scene-level review,
not bulk clearance.

## 7. Open FLAGs — 38, prioritized

Resolved during R1–R4 (no longer open): S15 parallel montage, S33 silhouette,
S09 same-face reveal discipline, S34 microphone, S38 non-kiss, S44 sixth card,
S07 sh11 split, S33 sh05/sh23 merges + trustee arc, S34 sh02/sh09 merges,
S35 sh01 merge — all `resolved-decision` with basis + consequence.

### Priority 1 — narrative/reveal logic (director decision recommended)
- **s30.e15** — dance partner is MAYA; screenplay writes "A.V.A." in quotes (swap staging hinges on it)
- **s30.e14** — door insert: her POV frame vs neutral coverage
- **s30.e05** — which surface carries the 3% readout (screen vs body)
- **s30.e09** — 10s written vs ~6–7s playable; plus 2 beat-duplicates + 1 tableau-group FLAG on the same event (the dance coverage is the most FLAG-dense spot in the film)
- **s30.e11** — beat-duplicate (re-coverage of beat 1: deliberate or duplication?)
- **s43.e01** — MAYBE-tag: is the wedding real? coverage intentionally soft
- **s09.e06** — unnamed hospital director inside GUESTS (cast discipline)
- **s35.e01** — A.V.A.'s position after leaving the mic unspecified (modeled present-but-unspecified)
- **s34.e04** — Maya on the service level throughout the defense, no screenplay position

### Priority 2 — rendering/mix decisions (affects prompt building later)
- **s06.e09** — the dim: practical vs grade vs VFX
- **s12.e09** — whose hum swells (walls' charger vs her)
- **s16.e03** — Maya's V.O.: literal earpiece vs over-picture
- **s22.e07** — heartbeat: literal mix vs performance only
- **s22.e05** — beat-duplicate (b4 covered by sh05+sh06)
- **s23.e05** — internal log: diegetic overlay vs screen cut
- **s24.e04** — scheduling note: dock surface vs overlay
- **s28.e03** — Anna's file: insert vs verbal
- **s36.e03** — founder exists only as handwriting: legible page?
- **s39.e03** — CV insert: how much legible vs read aloud
- **s11.e03** — seventeen variations on the wall: legible text vs abstract

### Priority 3 — can stay open (stylistic/edge; safe to leave flagged)
- s03.e05 empty-chair rendering of the S1 flight aftermath
- s04.e06 crate sleeve already staged?
- s05.e01 "(into the phone)" parenthetical; s05.e02 couriers' unwritten exit; s05.e03 uncredited florist/manager extras
- s07.e06 "I'm her mother" — literal builder vs emotional claim (performance note)
- s10.e03 "It's a felony" — Jim's own legal read
- s20.e04 detective's "companion" hesitation — comic vs uneasy
- s21.e07 how long the final look holds
- s31.e01 transport gurney rigidity (consistent with S33 photo)
- s32.e01 frame reads as Vega's S30 long-lens shot (inferred); s32.e06 uncredited technical director (remote)
- s38.e01 "the glass is drunk this time" — emptied-glass reading
- s39.e01 delivery agent: courier glimpsed vs boxes only
- s41.e01 investors inside PRESS crowd (no dedicated extras group)

## 8. Conditions for any future migration

1. Separate explicit authorization — this baseline grants none.
2. Dry-run import producing a full diff report before any write.
3. Scene→event→shot ID mapping to Studio `script_scene_number`/`shot_index`.
4. Rollback plan with JSON backup of scenes+takes (existing
   `production/backup_*` pattern).
5. Studio defects in §5 would be fixed *by* migration, not carried into it.
6. The −121 delta is context, not a deletion list — merge/keep verdicts are
   per-scene and must survive contact with the actual frames.

## 9. What this baseline does NOT claim

- Not a full audit of all 44 scenes — five representative scenes were reviewed
  semantically; 39 passed structural validation only.
- Not a continuity guarantee — see §6.
- Not a correctness proof of every directorial choice — 0 FAIL means the
  implemented checks passed.
- Not an instruction to modify the existing 586 cards.


========== FILE: coverage_report.md ==========

# Coverage report — 44 scenes, director_run v3.2

Analytical only. No Studio/DB writes were made.

| Scene | Heading | Events | Visual | Snd | Lines | Cov.spans | omit/flag | FAIL | UNVER | FLAG | Studio cards | Δshots |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | INT. CROSS TOWER — BOARDROOM — DAY | 6 | 16 | 1 | 9 | 19 | 0 | 0 | 8 | 0 | 14 | 2 |
| 2 | INT. PENHALIGON & SONS — TRUST OFFICE — DAY | 8 | 18 | 1 | 19 | 24 | 0 | 0 | 14 | 0 | 22 | -4 |
| 3 | INT. CROSS TOWER — DAMIEN'S OFFICE — DAY | 5 | 11 | 1 | 15 | 20 | 0 | 0 | 12 | 1 | 17 | -6 |
| 4 | INT. VOLT ROBOTICS LAB — DAY | 6 | 21 | 1 | 17 | 26 | 0 | 0 | 14 | 1 | 23 | -2 |
| 5 | INT. CROSS PENTHOUSE — GRAND FOYER — DAY (DELIVE | 5 | 14 | 1 | 9 | 21 | 0 | 0 | 16 | 3 | 17 | -3 |
| 6 | INT. PENTHOUSE — KITCHEN — NIGHT | 13 | 14 | 1 | 23 | 30 | 0 | 0 | 22 | 1 | 25 | -11 |
| 7 | INT. PENTHOUSE — KITCHEN / INT. VOLT LAB — MORNI | 7 | 11 | 1 | 23 | 35 | 0 | 0 | 21 | 1 | 27 | -16 |
| 8 | INT. CROSS PENTHOUSE — DAY INTO EVENING (THE DEM | 9 | 19 | 1 | 14 | 31 | 0 | 0 | 20 | 0 | 18 | 1 |
| 9 | INT. PENTHOUSE — SERVICE CORRIDOR — CONTINUOUS | 8 | 16 | 1 | 20 | 30 | 0 | 0 | 19 | 2 | 24 | -8 |
| 10 | INT. PENTHOUSE — SERVICE DOCK — NIGHT | 4 | 6 | 1 | 11 | 17 | 0 | 0 | 11 | 1 | 12 | -6 |
| 11 | INT. CROSS PENTHOUSE — TRAINING SALON — EVENING | 6 | 11 | 1 | 19 | 23 | 0 | 0 | 13 | 1 | 22 | -11 |
| 12 | INT. PENTHOUSE — DAMIEN'S STUDY — NIGHT | 9 | 13 | 1 | 17 | 26 | 0 | 0 | 16 | 1 | 21 | -8 |
| 13 | INT. CROSS TOWER — DAMIEN'S OFFICE — DAY | 6 | 8 | 0 | 13 | 19 | 0 | 0 | 13 | 0 | 14 | -6 |
| 14 | INT. THE MERIDIAN ROOM — RESTAURANT — NIGHT (DAT | 5 | 6 | 1 | 12 | 19 | 0 | 0 | 9 | 0 | 13 | -7 |
| 15 | INT. PRIVATE DINING CLUB — NIGHT (DATE TWO) | 6 | 7 | 1 | 11 | 17 | 0 | 0 | 10 | 1 | 14 | -7 |
| 16 | INT. NEIGHBORHOOD BISTRO — NIGHT (DATE THREE) | 8 | 9 | 1 | 12 | 18 | 0 | 0 | 15 | 1 | 16 | -7 |
| 17 | INT. CROSS PENTHOUSE — DAMIEN'S OFFICE — NIGHT | 4 | 5 | 1 | 12 | 16 | 1 | 0 | 8 | 0 | 15 | -10 |
| 18 | INT. CROSS TOWER — STRATEGY MEETING — DAY | 4 | 8 | 1 | 8 | 12 | 0 | 0 | 7 | 0 | 9 | -1 |
| 19 | INT. CROSS TOWER — VIDEO CONFERENCE — DAY | 4 | 4 | 1 | 6 | 10 | 0 | 0 | 7 | 0 | 8 | -4 |
| 20 | EXT. CROSS TOWER — GARAGE — DAY | 4 | 8 | 1 | 8 | 12 | 0 | 0 | 8 | 1 | 10 | -2 |
| 21 | INT. PENTHOUSE — ROOFTOP TERRACE — NIGHT | 7 | 8 | 1 | 12 | 16 | 0 | 0 | 13 | 1 | 15 | -7 |
| 22 | INT. PENTHOUSE — CORRIDOR — NIGHT — CONTINUOUS | 8 | 7 | 1 | 9 | 12 | 0 | 0 | 15 | 2 | 11 | -4 |
| 23 | INT. VOLT LAB — NIGHT | 6 | 7 | 1 | 9 | 11 | 0 | 0 | 10 | 1 | 9 | -2 |
| 24 | SCENE 24 — INT. VOLT LAB — DAWN | 4 | 8 | 1 | 8 | 13 | 0 | 0 | 7 | 1 | 10 | -2 |
| 25 | SCENE 25 — INT. PENTHOUSE — SALON — EVENING | 5 | 7 | 1 | 8 | 17 | 0 | 0 | 11 | 0 | 13 | -6 |
| 26 | SCENE 26 — INT. VICTOR'S OFFICE — DAY | 4 | 4 | 1 | 5 | 10 | 0 | 0 | 7 | 0 | 6 | -2 |
| 27 | SCENE 27 — INT. VOLT LAB — MAYA'S OFFICE — NIGHT | 5 | 8 | 1 | 11 | 16 | 0 | 0 | 9 | 0 | 11 | -3 |
| 28 | SCENE 28 — INT. VOLT LAB — LATER | 4 | 4 | 1 | 7 | 9 | 0 | 0 | 8 | 1 | 8 | -4 |
| 29 | SCENE 29 — INT. HOTEL BAR — NIGHT | 4 | 9 | 1 | 10 | 16 | 0 | 0 | 10 | 0 | 12 | -3 |
| 30 | INT. GRAND HOTEL — CHARITY GALA — NIGHT (THE SET | 16 | 19 | 1 | 7 | 17 | 0 | 0 | 24 | 8 | 15 | 4 |
| 31 | SCENE 31 — INT. GRAND HOTEL — SERVICE CORRIDOR — | 7 | 7 | 1 | 6 | 8 | 0 | 0 | 6 | 1 | 8 | -1 |
| 32 | SCENE 32 — INT. VICTOR'S OFFICE — NIGHT | 6 | 6 | 1 | 6 | 8 | 0 | 0 | 11 | 2 | 5 | 1 |
| 33 | SCENE 33 — INT. GRAND BALLROOM — THE BIRTHDAY GA | 11 | 23 | 1 | 5 | 13 | 0 | 0 | 16 | 1 | 11 | 12 |
| 34 | SCENE 34 — INT. BALLROOM — CONTINUOUS | 9 | 17 | 1 | 10 | 12 | 0 | 0 | 14 | 2 | 9 | 8 |
| 35 | INT. BALLROOM — CONTINUOUS | 11 | 17 | 1 | 8 | 15 | 0 | 0 | 15 | 1 | 10 | 7 |
| 36 | INT. BALLROOM — LATER | 5 | 9 | 1 | 4 | 7 | 0 | 0 | 7 | 1 | 5 | 4 |
| 37 | INT. BALLROOM — BAR — NIGHT | 7 | 10 | 1 | 7 | 10 | 0 | 0 | 6 | 0 | 7 | 3 |
| 38 | INT. BALLROOM — TERRACE — NIGHT | 15 | 20 | 1 | 14 | 18 | 0 | 0 | 12 | 2 | 17 | 3 |
| 39 | INT. VOLT LAB — MORNING | 6 | 20 | 1 | 18 | 24 | 0 | 0 | 14 | 2 | 25 | -5 |
| 40 | INT. CROSS TOWER — BOARDROOM — DAY | 3 | 5 | 0 | 5 | 5 | 0 | 0 | 6 | 0 | 5 | 0 |
| 41 | INT. VOLT LAB — RELAUNCH EVENT — DAY | 4 | 4 | 1 | 3 | 6 | 0 | 0 | 8 | 1 | 5 | -1 |
| 42 | INT. CROSS PENTHOUSE — BREAKFAST — MORNING | 5 | 11 | 1 | 14 | 18 | 0 | 0 | 13 | 0 | 16 | -5 |
| 43 | EXT./INT. THE WEDDING — DAY (MAYBE-TAG) | 3 | 7 | 1 | 7 | 7 | 0 | 0 | 10 | 1 | 7 | 0 |
| 44 | EPILOGUE CARDS (ROLLING) | 6 | 6 | 1 | 0 | 7 | 0 | 0 | 9 | 1 | 5 | 1 |
| **Σ** | | 288 | 468 | 42 | 471 | 720 | | 0 | 524 | 44 | 586 | -118 |

## FLAG — director decisions required (from validator_report.md)

- FLAG        ambiguity              s03.e05    the 'empty chair across his desk where the photographer fled' — the S1 flight ha
- FLAG        ambiguity              s04.e06    a 'crate sleeve' implies the shipping crate is already staged in the lab — the w
- FLAG        ambiguity              s05.e01    '(into the phone) Put it with the others.' — the parenthetical says the line goe
- FLAG        ambiguity              s05.e02    the couriers' exit is unwritten — they vanish between the tablet signature and J
- FLAG        ambiguity              s05.e03    the florist and house manager are uncredited extras outside the project cast — m
- FLAG        ambiguity              s06.e09    rendering of the dim — practical light vs grade vs subtle VFX; flag for director
- FLAG        ambiguity              s07.e06    'I'm her mother' — literal builder claim vs emotional claim; performance should 
- FLAG        ambiguity              s09.e03    how literally identical Maya and A.V.A. read on camera — same-face design is ass
- FLAG        ambiguity              s09.e06    the hospital's director is an unnamed member of the table — modeled inside GUEST
- FLAG        ambiguity              s10.e03    'It's a felony' — Jim's guess at the legal exposure is his own read; whether any
- FLAG        ambiguity              s11.e03    whether the seventeen variations are legible text on the wall display or abstrac
- FLAG        ambiguity              s12.e09    whose hum is swelling — the walls' charger or the suggestion it is her; flag for
- FLAG        ambiguity              s15.e02    screenplay marks the abort line (V.O.) yet cuts to the lab for the lean-in — fla
- FLAG        ambiguity              s16.e03    how much of Maya's V.O. the audience hears as literal earpiece audio vs. over th
- FLAG        ambiguity              s20.e04    whether the detective's 'companion' hesitation should play comic or uneasy — fla
- FLAG        ambiguity              s21.e07    how long the final look holds before the scene releases — the screenplay gives n
- FLAG        beat-duplicate         s22.e05    beat 4 covered by ['s22.sh05', 's22.sh06'] — deliberate re-coverage or duplication?
- FLAG        ambiguity              s22.e07    how the heartbeat is rendered audible — literal mix element vs. performance only
- FLAG        ambiguity              s23.e05    how the internal log is rendered — diegetic overlay vs cut to a screen; flag for
- FLAG        ambiguity              s24.e04    how the scheduling note renders — diegetic dock surface vs internal-log overlay;
- FLAG        ambiguity              s28.e03    whether Anna's file is shown as its own insert or stays verbal — screenplay keep
- FLAG        tableau-group          s30.e09    tableau has no single shot containing all of ['A.V.A.', 'DAMIEN', 'JIM'] — confirm intended
- FLAG        beat-duplicate         s30.e09    beat 1 covered by ['s30.sh10', 's30.sh11'] — deliberate re-coverage or duplication?
- FLAG        beat-duplicate         s30.e09    beat 2 covered by ['s30.sh10', 's30.sh12'] — deliberate re-coverage or duplication?
- FLAG        beat-duplicate         s30.e11    beat 1 covered by ['s30.sh15', 's30.sh16'] — deliberate re-coverage or duplication?
- FLAG        ambiguity              s30.e05    which surface carries the 3% readout — screen vs her body; director pick, both a
- FLAG        ambiguity              s30.e09    10s written vs ~6-7s playable — flagged for director
- FLAG        ambiguity              s30.e14    whether the door insert is shown as her POV frame or as neutral coverage — POV k
- FLAG        ambiguity              s30.e15    partner in the pose is MAYA — interpreted: the screenplay writes "A.V.A." in quo
- FLAG        ambiguity              s31.e01    transport reads as gurney/cart — 'wheels' and the S33 screen photo confirm rigid
- FLAG        ambiguity              s32.e01    frame reads as Vega's S30 long-lens shot — inferred from her 'both of them in on
- FLAG        ambiguity              s32.e06    the technical director is an uncredited remote party — no cast entry; not declar
- FLAG        ambiguity              s33.e11    the screenplay withholds the occupant ('on its own') — coverage keeps A.V.A. a s
- FLAG        ambiguity              s34.e04    Maya is on the service level throughout the defense — the screenplay gives her n
- FLAG        ambiguity              s34.e07    the mic is set down before the final speech — she continues unamplified or recla
- FLAG        ambiguity              s35.e01    A.V.A.'s position after leaving the mic is unspecified — modeled present-but-uns
- FLAG        ambiguity              s36.e03    the founder exists only as handwriting — whether the page is shown as a legible 
- FLAG        ambiguity              s38.e01    'the glass is drunk this time' — read as the drink consumed (an emptied glass); 
- FLAG        ambiguity              s38.e15    whether the held two-shot closes the four feet into a kiss is a director call — 
- FLAG        ambiguity              s39.e01    the delivery agent is unspecified — whether a courier is glimpsed or the boxes s
- FLAG        ambiguity              s39.e03    how much of the CV is legible in the insert versus how much Maya reads aloud — d
- FLAG        ambiguity              s41.e01    'investors' has no dedicated extras group — modeled inside the PRESS/floor crowd
- FLAG        ambiguity              s43.e01    MAYBE-TAG — the heading leaves the wedding's reality deliberately soft; coverage
- FLAG        ambiguity              s44.e06    whether the third coffee is ever visualized as a shot or stays pure text — the s

========== FILE: baseline_manifest_v32_r4.json ==========

{
 "name": "HALF CHARGED \u2014 AI Director v3.2 R4 (S35 merge sh01->sh02; final reviewed baseline)",
 "parent": "baseline_manifest_v32_r3.json",
 "files": {
  "AUTHORING_GUIDE_v32.md": {
   "bytes": 6113,
   "sha256": "7c3b846b5853cf6343fef9e296bc02e4d2d9f02835866272f0cd744ff527daa9"
  },
  "README.md": {
   "bytes": 2675,
   "sha256": "4819f09630f6e4e84b7bdbd487d1f44102ee69024442c776da258a1d903ad129"
  },
  "_patch_decisions_r1.py": {
   "bytes": 6429,
   "sha256": "990c6c9be687c2cdeb9709bac630b6ce276d32d664359d1c1d711b2968bb81db"
  },
  "_patch_r2.py": {
   "bytes": 4566,
   "sha256": "de5b879736799ff2d34d386b3d613b07ec4fde4de0a70536430ea12d758b0bc6"
  },
  "_patch_r3.py": {
   "bytes": 2927,
   "sha256": "2a96717d5bdb9bf6038dd41729a385d89fa5f10de30b579c1d3896d164a02268"
  },
  "_patch_r4.py": {
   "bytes": 1535,
   "sha256": "f45b0588ff253475bbf7ce5626909ec8009278d7081a93ff3bbdef8eb81d76f1"
  },
  "_patch_v32.py": {
   "bytes": 14134,
   "sha256": "849e0883377b8439c3825bbf9233b7e8f9abf1c5a2de9e902b40aea3b99635f3"
  },
  "coverage_report.md": {
   "bytes": 10654,
   "sha256": "c2b862a8da57b907d725868710821d479dd84f13b996a845ae89bc73475b6b55"
  },
  "delta_analysis.md": {
   "bytes": 5072,
   "sha256": "608a953685ed6fcdc0c4f5c5f473aa7e5b516bf26b4c62178afb9f22459746ba"
  },
  "negtest_validator.py": {
   "bytes": 9724,
   "sha256": "d34d6a3d5c5bd7c73c0ae006aa08757b7fe8639f3b9be66f1232442a92d36be5"
  },
  "review_package_s03_s34.json": {
   "bytes": 73355,
   "sha256": "7bf325f919b157ccb962ce044361ccffc3883576b914a356212e5221102fb978"
  },
  "review_package_s07_s33.json": {
   "bytes": 98894,
   "sha256": "eb37be48dca537729166f26f9c29b9852990c0d909614cd4723ef40ed1a86dd3"
  },
  "s01_boardroom.events.json": {
   "bytes": 27485,
   "sha256": "17ee72c79bc2e26195ae085b2a3bd17c4b702eb30f632c49dc3d9c4619672567"
  },
  "s02_trust_office.events.json": {
   "bytes": 35493,
   "sha256": "b8ba99a90037c9cd61c80651725c474caedd78077d60c39c058b3e9c198dee5d"
  },
  "s03_damien_office.events.json": {
   "bytes": 27345,
   "sha256": "89a448d43222a1adb878d809e4f771fdf6be58f507c8fa3a2e83659e0797659e"
  },
  "s04_volt_lab.events.json": {
   "bytes": 37248,
   "sha256": "b9b688fe2eac41536fe8304c0c95a80f0a1e861537b685957353833ccf68452d"
  },
  "s05_delivery.events.json": {
   "bytes": 30025,
   "sha256": "fd43aafa7984550dae0bb3e7fd5a1d9cadd3ba7906acc433a75efd55a5d49ad7"
  },
  "s06_kitchen.events.json": {
   "bytes": 41167,
   "sha256": "943d2080bb18cd3709b256f2dfccc0830e18708fc749d1405969984c9a3f30c7"
  },
  "s07_morning.events.json": {
   "bytes": 37575,
   "sha256": "e8448420021db08bc1cddb9e5af27144c005cff2f9b32bb6eb285f0331685084"
  },
  "s08_demo.events.json": {
   "bytes": 37800,
   "sha256": "a117983121f68bc3302ddaf3088c971da252c0663b7fc4c7349a36168044507a"
  },
  "s09_service_corridor.events.json": {
   "bytes": 38907,
   "sha256": "18b935afeaf11490d4f9c49fcd7a22ea0f50441885aa0d0e47733df8aee8dddd"
  },
  "s10_service_dock.events.json": {
   "bytes": 19216,
   "sha256": "d6cd1d39cc4df1d0415695433faaab7b2b583efe822e64753193402e758e31f7"
  },
  "s11_training_salon.events.json": {
   "bytes": 27659,
   "sha256": "a0759c5bdc6f4fbaa36378f1c7a65e0f7d70a46e7418ed559d0f01b9ac331369"
  },
  "s12_study.events.json": {
   "bytes": 33218,
   "sha256": "f35bb2b630dccdf930cf5389c30ffde642ff825814a97b2e652a0faea08645a5"
  },
  "s13_office.events.json": {
   "bytes": 24077,
   "sha256": "e42de514a250dd8609b2c30b20b2e112ffa32490430f28e4ef40e10dff79f6b3"
  },
  "s14_date_one.events.json": {
   "bytes": 22268,
   "sha256": "c32533194ac11425a2fb1cb3916e163b08322adca9f7435e88d21ae078d1ba87"
  },
  "s15_date_two.events.json": {
   "bytes": 22647,
   "sha256": "3e823dc84089e8a67c829e39bb03881cb6016fdc3057863d20f1a41eba8e8460"
  },
  "s16_date_three.events.json": {
   "bytes": 29803,
   "sha256": "6d161d027f5d6fe37c0f4440759f48ec6f18090ccd6888246ab6e3386e0f97e1"
  },
  "s17_office_night.events.json": {
   "bytes": 18627,
   "sha256": "ba86fd46c25d281c42d7ec33801c25f3851a7eea6b2e58a04e7801a89be06ec2"
  },
  "s18_strategy.events.json": {
   "bytes": 17990,
   "sha256": "e179cdf2122976e1d4cfc83aca3d3096bb61d56787803d625577564307ffcb0f"
  },
  "s19_video_conf.events.json": {
   "bytes": 15753,
   "sha256": "50661bf7600d9f28498b4d8ddbf0691655493976faaf4366748c751a108ed6e4"
  },
  "s20_garage.events.json": {
   "bytes": 18178,
   "sha256": "9fa0b0669dd2ad2ec0834cd51858e1291d86c976e954f55fbf09f424cc973f78"
  },
  "s21_terrace.events.json": {
   "bytes": 25688,
   "sha256": "1e5251c8e830826863b1be5ebbf363baff569d9c81b1814cb5a1ebf66a1734bb"
  },
  "s22_proximity.events.json": {
   "bytes": 21247,
   "sha256": "082ef3ddf506ef87817f00f08ffc54cce493abb45da2d355a9d18f54d1c9611b"
  },
  "s23_plus47min.events.json": {
   "bytes": 19022,
   "sha256": "15813cc80491d35399360a15db295c779e68b60287145da67734ef7581d06f0b"
  },
  "s24_volt_dawn.events.json": {
   "bytes": 16924,
   "sha256": "a4048649c7c2a5bf4e2d971eece681775c12eb2642d70ce7c333b440ca922328"
  },
  "s25_salon.events.json": {
   "bytes": 19765,
   "sha256": "e7002880852b4a3dd5d9363e852154262171e1735909366eb446677ac36a0f69"
  },
  "s26_victor_office.events.json": {
   "bytes": 13838,
   "sha256": "f91e63fa0cde68b4a7d4a5d78da26f861e51a7cdec872a5012a6b0bbf1d0ee6c"
  },
  "s27_maya_office.events.json": {
   "bytes": 21547,
   "sha256": "20376a153a04ac570dffe5d3e2349b5ccc5860fa2bf2c1107c4b60534f64f918"
  },
  "s28_volt_later.events.json": {
   "bytes": 13738,
   "sha256": "afe4bdd3009e51a6cded1bb90f82f8c1e0a325b7b77fbe7664b9ab362d60e941"
  },
  "s29_hotel_bar.events.json": {
   "bytes": 20137,
   "sha256": "aa6da08ec231eab5ed8b85071e5ef419fcb3cd857f1b7e664f18dc8d23a68ee1"
  },
  "s30_gala.events.json": {
   "bytes": 38936,
   "sha256": "57dccc1271d2bc3c2c9f7033680065ea95040a1bf8aa8e9bc0ee3154d1b87428"
  },
  "s31_service_corridor.events.json": {
   "bytes": 17020,
   "sha256": "25649bd3024eb3f9e176df2b5d0be639de4eeaaa682c0126f297879c773ed8c3"
  },
  "s32_victor_night.events.json": {
   "bytes": 16247,
   "sha256": "4720fca0466da550a29d2d94ec39d14d3b92a75bea1eced327f5f5228bb89070"
  },
  "s33_birthday_gala.events.json": {
   "bytes": 37683,
   "sha256": "1b33c5e28304f6b30132a78122b2787be53d9973230b0679d5da906067586924"
  },
  "s34_ballroom.events.json": {
   "bytes": 31250,
   "sha256": "b448c529dadf8492010b8ab3383e142623c40cb06ac54349476a203d3243ad70"
  },
  "s35_ballroom.events.json": {
   "bytes": 35703,
   "sha256": "cca11aa29d0af77869dfb0c7af5cf8576ced1f78f2da5bb636581fdd41c21b65"
  },
  "s36_ballroom_later.events.json": {
   "bytes": 19271,
   "sha256": "5a294f647c2edc462bd63879dda5f625dfee6dcb569a2f04fd7862628f57f939"
  },
  "s37_ballroom_bar.events.json": {
   "bytes": 21526,
   "sha256": "fcb043e848e43b7ff4ad8132d1255d0b421e0a2f1fab612cbcea25c3f57a4d11"
  },
  "s38_terrace.events.json": {
   "bytes": 40546,
   "sha256": "081163ac7fa8d5b6916417e827bfb5f1d4aeb1c8d363a78e29c9ffd9dd021e9b"
  },
  "s39_volt_morning.events.json": {
   "bytes": 35134,
   "sha256": "39380db66b4fff867cf982eec1f57a4074d0a46241598ca2137c68ebf10ea5c3"
  },
  "s40_boardroom.events.json": {
   "bytes": 11152,
   "sha256": "37b7a9af7825c6aa7f5c3611f9f06d7af925aea4d4613ea3192edbdd27baf747"
  },
  "s41_relaunch.events.json": {
   "bytes": 12870,
   "sha256": "cac180e2206eeafa22f24a522c330e2611f713ea1d1850af4959912b3377d4ef"
  },
  "s42_breakfast.events.json": {
   "bytes": 26016,
   "sha256": "af22d3d3c925c33b8b83bb76f53afa51c90ef58ca5c0ddd0aa9053b6375f8047"
  },
  "s43_wedding.events.json": {
   "bytes": 17375,
   "sha256": "b67aa68e784c1e3475e004632fe97f737b0970650052d842426a767719fe03cc"
  },
  "s44_epilogue.events.json": {
   "bytes": 17005,
   "sha256": "6dc44b8648c92ab9f7785b69edffa6bb60af0deac322278f442ab6f91d9a7a38"
  },
  "validator.py": {
   "bytes": 33709,
   "sha256": "7338340cf960e6f469778d7d3660b2002162a881f7165718bf773312d0fbfa2b"
  },
  "validator_report.md": {
   "bytes": 75502,
   "sha256": "cef5c15be15ba57706e3951126ee402038cc3413db9ff2a41fb46dc175f93cca"
  }
 }
}