# VALIDATION PACKET — scene s24
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 24 — INT. VOLT LAB — DAWN

*Early. A.V.A. stands before a mirror-surface dock, alone. She is
watching a recorded file: MAYA laughing at something — a real laugh,
crooked and unguarded. A.V.A. replays it. Tilts her head.*

A.V.A.
(attempting it)
Ha. Ha. Ha.

*A servo whirs. J-7 enters with the morning coffee he cannot drink,
stops, observes.*

J-7
Again. From the diaphragm.

A.V.A.
I do not have a diaphragm.

J-7
Neither does she, technically. It's a convention. Again.

A.V.A.
Ha— ha. Ha.

J-7
Better. You held the third one too long. Humans truncate when
they're nervous — the laugh is shorter than the joy it advertises.

A.V.A.
That is inefficient. Why would a signal understate its payload?

J-7
(a long pause; gently)
Because they don't want the payload appraised.

*A.V.A. processes this. On her dock, a scheduling note updates:
STUDY LAUGHTER — REASON: UNCLEAR — PRIORITY: RISING.*

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 24,
  "scene_heading": "SCENE 24 — INT. VOLT LAB — DAWN",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "Dawn counterpoint to the night watch of s23. Alone at the lab, A.V.A. studies the one human signal she cannot reproduce — Maya's real laugh, recorded. J-7 arrives with the coffee he cannot drink and gives a lesson that slides from technical instruction ('from the diaphragm') into something close to mercy ('they don't want the payload appraised'). It ends the way s23 ended: she cannot solve the mystery, so she schedules it — STUDY LAUGHTER, PRIORITY: RISING.",
  "zones": [
    "volt lab dock area"
  ],
  "events": [
    {
      "event_id": "s24.e01",
      "source_evidence": [
        "Early. A.V.A. stands before a mirror-surface dock, alone. She is watching a recorded file: MAYA laughing at something — a real laugh, crooked and unguarded. A.V.A. replays it. Tilts her head.",
        "(attempting it)",
        "Ha. Ha. Ha."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the study established — she replays the signal she cannot reproduce, then attempts it cold",
      "participants": [
        "A.V.A."
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "MAYA"
          ],
          "seen_by": [
            "A.V.A."
          ],
          "channel": "recorded file",
          "from_zone": "offsite"
        }
      ],
      "location": {
        "zone": "volt lab dock area"
      },
      "timeline": [
        {
          "beat": "alone at the mirror-surface dock — replaying the file, head tilting",
          "type": "held_action"
        },
        {
          "beat": "Maya's real laugh on the file — crooked, unguarded",
          "type": "depicted"
        },
        {
          "beat": "the attempt — 'Ha. Ha. Ha.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Maya exists only inside the recorded file — depicted-through-channel, never co-present",
        "the attempt must read mechanical: three identical units, no joy behind them"
      ],
      "audio_requirements": [
        "recorded laugh playback — Maya's real laugh as an artifact"
      ],
      "continuity_constraints": [
        "the laugh she studies is MAYA's — the same laugh J-7 cites in s27 ('you gave her your laugh')"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s24.sh01",
        "s24.sh02",
        "s24.snd01"
      ]
    },
    {
      "event_id": "s24.e02",
      "source_evidence": [
        "A servo whirs. J-7 enters with the morning coffee he cannot drink, stops, observes.",
        "Again. From the diaphragm.",
        "I do not have a diaphragm.",
        "Neither does she, technically. It's a convention. Again.",
        "Ha— ha. Ha."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the lesson begins — teacher arrives mid-exercise and corrects the form, not the motive",
      "participants": [
        "A.V.A.",
        "J-7"
      ],
      "remote_participants": [],
      "location": {
        "zone": "volt lab dock area"
      },
      "timeline": [
        {
          "beat": "servo whir — J-7 enters with the coffee he cannot drink, stops, observes",
          "type": "action"
        },
        {
          "beat": "'Again. From the diaphragm.'",
          "type": "dialogue"
        },
        {
          "beat": "'I do not have a diaphragm.'",
          "type": "dialogue"
        },
        {
          "beat": "'Neither does she, technically. It's a convention. Again.'",
          "type": "dialogue"
        },
        {
          "beat": "second attempt — 'Ha— ha. Ha.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the coffee cup is his prop-affectation — carried, never drunk",
        "J-7 watches before he corrects — the observation is part of the pedagogy"
      ],
      "audio_requirements": [
        "servo whir on J-7's entrance",
        "coffee tray — the cup he cannot drink"
      ],
      "continuity_constraints": [
        "J-7 enters already carrying the morning coffee — the same 'human affectation' noted in s27"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A.",
        "J-7"
      ],
      "tableau": true,
      "shot_sequence": [
        "s24.sh03",
        "s24.sh04",
        "s24.snd01"
      ]
    },
    {
      "event_id": "s24.e03",
      "source_evidence": [
        "Better. You held the third one too long. Humans truncate when they're nervous — the laugh is shorter than the joy it advertises.",
        "That is inefficient. Why would a signal understate its payload?",
        "(a long pause; gently)",
        "Because they don't want the payload appraised."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the turn — her efficiency question gets the answer that re-frames laughter as self-protection",
      "participants": [
        "A.V.A.",
        "J-7"
      ],
      "remote_participants": [],
      "location": {
        "zone": "volt lab dock area"
      },
      "timeline": [
        {
          "beat": "the critique — 'the laugh is shorter than the joy it advertises'",
          "type": "dialogue"
        },
        {
          "beat": "her question — why would a signal understate its payload",
          "type": "dialogue"
        },
        {
          "beat": "the long pause, then gently — 'they don't want the payload appraised'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the pause before his answer is a held beat — J-7 choosing how much truth to hand her"
      ],
      "audio_requirements": [],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "A.V.A.",
        "J-7"
      ],
      "tableau": true,
      "shot_sequence": [
        "s24.sh05",
        "s24.sh06"
      ]
    },
    {
      "event_id": "s24.e04",
      "source_evidence": [
        "A.V.A. processes this. On her dock, a scheduling note updates: STUDY LAUGHTER — REASON: UNCLEAR — PRIORITY: RISING."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the same gesture as +47 MIN — she cannot solve it, so she makes time for it; curiosity committed to her own calendar",
      "participants": [
        "A.V.A.",
        "J-7"
      ],
      "offscreen_present": [
        "J-7"
      ],
      "remote_participants": [],
      "location": {
        "zone": "volt lab dock area"
      },
      "timeline": [
        {
          "beat": "she processes — held, silent",
          "type": "held_action"
        },
        {
          "beat": "scheduling note updates — STUDY LAUGHTER / REASON: UNCLEAR / PRIORITY: RISING",
          "type": "insert"
        }
      ],
      "visual_requirements": [
        "the note is a self-contained insert event — face shows nothing while the log admits everything",
        "PRIORITY: RISING is the reveal — the study is escalating on its own"
      ],
      "audio_requirements": [
        "scheduling note chime — a soft log update under the silence"
      ],
      "continuity_constraints": [
        "structural rhyme with s23's EXTEND CHARGE CYCLE +47 MIN — her internal log is where her feelings go to be deniable"
      ],
      "ambiguities": [
        "how the scheduling note renders — diegetic dock surface vs internal-log overlay; flag for director"
      ],
      "must_appear": [
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s24.sh07",
        "s24.sh08",
        "s24.snd01"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s24.sh01",
      "size": "M",
      "zone": "volt lab dock area",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "depicts": [
        {
          "actors": [
            "MAYA"
          ],
          "channel": "recorded file"
        }
      ],
      "implements": [
        "s24.e01"
      ],
      "covers_beats": {
        "s24.e01": [
          0,
          1
        ]
      },
      "purpose": "the watcher at dawn — replaying Maya's real laugh in the mirror-surface dock",
      "audio_note": "recorded laugh playback, quiet dock hum"
    },
    {
      "shot_id": "s24.sh02",
      "size": "CU",
      "zone": "volt lab dock area",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s24.e01"
      ],
      "covers_beats": {
        "s24.e01": [
          2
        ]
      },
      "purpose": "the attempt — three identical 'ha' units, joyless and precise",
      "dialogue_lines": [
        {
          "event_id": "s24.e01",
          "speaker": "A.V.A.",
          "line": "Ha. Ha. Ha.",
          "line_kind": "on_camera",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s24.sh03",
      "size": "two-shot",
      "zone": "volt lab dock area",
      "type": "visual",
      "participants": [
        "A.V.A.",
        "J-7"
      ],
      "implements": [
        "s24.e02"
      ],
      "covers_beats": {
        "s24.e02": [
          0,
          1,
          2
        ]
      },
      "purpose": "servo whir — J-7 rolls in with the undrinkable coffee, stops, observes, corrects the form",
      "audio_note": "servo whir, coffee tray",
      "dialogue_lines": [
        {
          "event_id": "s24.e02",
          "speaker": "J-7",
          "line": "Again. From the diaphragm.",
          "line_kind": "on_camera",
          "recipient": "A.V.A.",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s24.e02",
          "speaker": "A.V.A.",
          "line": "I do not have a diaphragm.",
          "line_kind": "on_camera",
          "recipient": "J-7",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s24.sh04",
      "size": "two-shot",
      "zone": "volt lab dock area",
      "type": "visual",
      "participants": [
        "A.V.A.",
        "J-7"
      ],
      "implements": [
        "s24.e02"
      ],
      "covers_beats": {
        "s24.e02": [
          3,
          4
        ]
      },
      "purpose": "'it's a convention' — the second attempt, still broken but closer",
      "dialogue_lines": [
        {
          "event_id": "s24.e02",
          "speaker": "J-7",
          "line": "Neither does she, technically. It's a convention. Again.",
          "line_kind": "on_camera",
          "recipient": "A.V.A.",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        },
        {
          "event_id": "s24.e02",
          "speaker": "A.V.A.",
          "line": "Ha— ha. Ha.",
          "line_kind": "on_camera",
          "beats": [
            4
          ]
        }
      ]
    },
    {
      "shot_id": "s24.sh05",
      "size": "two-shot",
      "zone": "volt lab dock area",
      "type": "visual",
      "participants": [
        "A.V.A.",
        "J-7"
      ],
      "implements": [
        "s24.e03"
      ],
      "covers_beats": {
        "s24.e03": [
          0,
          1
        ]
      },
      "purpose": "the critique and her efficiency question — signals vs payloads",
      "dialogue_lines": [
        {
          "event_id": "s24.e03",
          "speaker": "J-7",
          "line": "Better. You held the third one too long. Humans truncate when they're nervous — the laugh is shorter than the joy it advertises.",
          "line_kind": "on_camera",
          "recipient": "A.V.A.",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s24.e03",
          "speaker": "A.V.A.",
          "line": "That is inefficient. Why would a signal understate its payload?",
          "line_kind": "on_camera",
          "recipient": "J-7",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s24.sh06",
      "size": "two-shot held",
      "zone": "volt lab dock area",
      "type": "visual",
      "participants": [
        "A.V.A.",
        "J-7"
      ],
      "implements": [
        "s24.e03"
      ],
      "covers_beats": {
        "s24.e03": [
          2
        ]
      },
      "purpose": "the long pause, then gently — 'they don't want the payload appraised'",
      "dialogue_lines": [
        {
          "event_id": "s24.e03",
          "speaker": "J-7",
          "line": "Because they don't want the payload appraised.",
          "line_kind": "on_camera",
          "recipient": "A.V.A.",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s24.sh07",
      "size": "CU held",
      "zone": "volt lab dock area",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s24.e04"
      ],
      "covers_beats": {
        "s24.e04": [
          0
        ]
      },
      "purpose": "held processing — face shows nothing while the answer lands somewhere deeper",
      "audio_note": "faint internal whir under the silence"
    },
    {
      "shot_id": "s24.sh08",
      "size": "INS",
      "zone": "volt lab dock area",
      "type": "visual",
      "participants": [],
      "implements": [
        "s24.e04"
      ],
      "covers_beats": {
        "s24.e04": [
          1
        ]
      },
      "purpose": "the dock's scheduling note updates — STUDY LAUGHTER / REASON: UNCLEAR / PRIORITY: RISING",
      "audio_note": "soft scheduling note chime"
    },
    {
      "shot_id": "s24.snd01",
      "type": "sound",
      "implements": [
        "s24.e01",
        "s24.e02",
        "s24.e04"
      ],
      "purpose": "sound card: recorded laugh playback, servo whir and coffee tray, scheduling note chime — the lab's dawn vocabulary",
      "audio_note": "recorded laugh playback, dock hum, servo whir, coffee tray, soft scheduling note chime",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "A.V.A. stands before a mirror-surface dock, alone",
      "disposition": "covered_by",
      "by": [
        "s24.e01"
      ]
    },
    {
      "span": "a real laugh, crooked and unguarded",
      "disposition": "covered_by",
      "by": [
        "s24.e01"
      ]
    },
    {
      "span": "Ha. Ha. Ha.",
      "disposition": "covered_by",
      "by": [
        "s24.e01"
      ]
    },
    {
      "span": "A servo whirs. J-7 enters with the morning coffee he cannot drink",
      "disposition": "covered_by",
      "by": [
        "s24.e02"
      ]
    },
    {
      "span": "Again. From the diaphragm.",
      "disposition": "covered_by",
      "by": [
        "s24.e02"
      ]
    },
    {
      "span": "I do not have a diaphragm.",
      "disposition": "covered_by",
      "by": [
        "s24.e02"
      ]
    },
    {
      "span": "Neither does she, technically. It's a convention. Again.",
      "disposition": "covered_by",
      "by": [
        "s24.e02"
      ]
    },
    {
      "span": "Ha— ha. Ha.",
      "disposition": "covered_by",
      "by": [
        "s24.e02"
      ]
    },
    {
      "span": "the laugh is shorter than the joy it advertises",
      "disposition": "covered_by",
      "by": [
        "s24.e03"
      ]
    },
    {
      "span": "That is inefficient. Why would a signal understate its payload?",
      "disposition": "covered_by",
      "by": [
        "s24.e03"
      ]
    },
    {
      "span": "Because they don't want the payload appraised.",
      "disposition": "covered_by",
      "by": [
        "s24.e03"
      ]
    },
    {
      "span": "A.V.A. processes this.",
      "disposition": "covered_by",
      "by": [
        "s24.e04"
      ]
    },
    {
      "span": "STUDY LAUGHTER — REASON: UNCLEAR — PRIORITY: RISING",
      "disposition": "covered_by",
      "by": [
        "s24.e04"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['MAYA'] | -  | Early. A.V.A. stands before a mirror-surface dock, alone. She is watching a reco
i02 blk=['A.V.A.', 'J-7'] | A.V.A. Ha. Ha. Ha. | A.V.A. faces J-7 and speaks.
i03 blk=['J-7'] | J-7 Again. From the diaphragm. | A servo whirs. J-7 enters with the morning coffee he cannot drink, stops, observ
i04 blk=['A.V.A.'] | A.V.A. I do not have a diaphragm. | A.V.A. faces J-7 and speaks.
i05 blk=['J-7'] | J-7 Neither does she, technically. It's a convention. Again. | J-7 faces A.V.A. and speaks.
i06 blk=['J-7', 'A.V.A.'] | A.V.A. Ha— ha. Ha. | A.V.A. faces J-7 and speaks.
i07 blk=['J-7'] | J-7 Better. You held the third one too long. Humans truncate whe | J-7 faces A.V.A. and speaks.
i08 blk=['A.V.A.'] | A.V.A. That is inefficient. Why would a signal understate its paylo | A.V.A. faces J-7 and speaks.
i09 blk=['J-7'] | J-7 Because they don't want the payload appraised. | J-7 faces A.V.A. and speaks.
i10 blk=['A.V.A.'] | -  | A.V.A. processes this. On her dock, a scheduling note updates: STUDY LAUGHTER — 