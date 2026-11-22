# VALIDATION PACKET — scene s25
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 25 — INT. PENTHOUSE — SALON — EVENING

*DAMIEN and MAYA-A.V.A. — a chess board between them she is
deliberately losing badly at ("warm mode" cannot calculate in
front of him, so Maya plays like a talented amateur).*

DAMIEN
You hung your queen.

MAYA-A.V.A.
I was told queens are expendable. Faulty module.

DAMIEN
You're getting worse at chess and better at—

*He reaches across the board to correct her knight — and brushes
her hand.*

*She flinches.*

*A small, fast, utterly human flinch — the hand retreating before
the face can be composed.*

*Silence. The chess piece rocks and stills.*

DAMIEN (CONT'D)
(slowly)
Robots don't flinch.

*Across the room — the service dock, where the real A.V.A. sits
in her charge-cycle, eyes open, on the staff feed. She says it to
no one:*

A.V.A.
...Correct.

*Maya recovers — glacial, perfect, machine-smooth:*

MAYA-A.V.A.
A startle reflex was added for social realism. Version 4.1.
Flagging it as oversensitive.

DAMIEN
(still watching her)
Dial it up.

*He goes back to the board. Maya stares at him — and for once the
mask slips just enough that if he looked up, everything would be
over. He doesn't look up. He moves his knight and says, to the
board:*

DAMIEN (CONT'D)
Don't ever roll it back.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 25,
  "scene_heading": "SCENE 25 — INT. PENTHOUSE — SALON — EVENING",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "The mask's narrowest escape. Maya-as-A.V.A. loses at chess on purpose because 'warm mode' cannot calculate in front of him — and then one brushed hand produces a flinch no machine would make. Damien names it ('Robots don't flinch'), the real A.V.A. confirms it across the room to no one, and Maya talks her way out with a version number. His closer — 'Don't ever roll it back' — is the scene's buried confession: he prefers whatever this is to what it was.",
  "zones": [
    "penthouse salon chess area",
    "penthouse salon service dock"
  ],
  "events": [
    {
      "event_id": "s25.e01",
      "source_evidence": [
        "DAMIEN and MAYA-A.V.A. — a chess board between them she is deliberately losing badly at",
        "so Maya plays like a talented amateur",
        "You hung your queen.",
        "I was told queens are expendable. Faulty module.",
        "You're getting worse at chess and better at—"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the cover performance established — she loses on purpose; his unfinished sentence ('better at—') is the scene aiming at its own reveal",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "remote_participants": [],
      "location": {
        "zone": "penthouse salon chess area"
      },
      "timeline": [
        {
          "beat": "the game — she hangs pieces on purpose, 'talented amateur' as disguise",
          "type": "held_action"
        },
        {
          "beat": "'You hung your queen.'",
          "type": "dialogue"
        },
        {
          "beat": "'queens are expendable. Faulty module.' — the joke that doubles as confession",
          "type": "dialogue"
        },
        {
          "beat": "'worse at chess and better at—' cut off",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the chess position must be legible as deliberate badness — a queen left hanging in the open",
        "ease between them is the baseline the flinch will break"
      ],
      "audio_requirements": [
        "chess pieces moved and set down — quiet game sounds"
      ],
      "continuity_constraints": [
        "screenplay registers the opponent as MAYA-A.V.A. — Maya performing A.V.A.; the real A.V.A. is across the room on her dock",
        "Damien's line truncates mid-word — the reach interrupts the sentence"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "MAYA"
      ],
      "tableau": true,
      "shot_sequence": [
        "s25.sh01"
      ]
    },
    {
      "event_id": "s25.e02",
      "source_evidence": [
        "He reaches across the board to correct her knight — and brushes her hand.",
        "She flinches.",
        "A small, fast, utterly human flinch — the hand retreating before the face can be composed.",
        "Silence. The chess piece rocks and stills.",
        "(slowly)",
        "Robots don't flinch."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "THE BREACH — one touch produces the reflex that outs her; the rocking piece is the room holding its breath",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "remote_participants": [],
      "location": {
        "zone": "penthouse salon chess area"
      },
      "timeline": [
        {
          "beat": "he reaches across to correct her knight — brushes her hand",
          "type": "action"
        },
        {
          "beat": "the flinch — hand retreats before the face can compose itself",
          "type": "reaction"
        },
        {
          "beat": "silence — the chess piece rocks and stills",
          "type": "held_image"
        },
        {
          "beat": "'Robots don't flinch.' said slowly",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the flinch is a hands-and-speed event: small, fast, human — the hand moves before the mask can",
        "the rocking piece reads as the room's pulse — one small object doing all the acting"
      ],
      "audio_requirements": [
        "the flinch silence — room tone drops out; chess piece rocking to still"
      ],
      "continuity_constraints": [
        "his reach corrects HER knight — physical proximity established by the game, not by approach"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s25.sh02",
        "s25.sh03",
        "s25.snd01"
      ]
    },
    {
      "event_id": "s25.e03",
      "source_evidence": [
        "Across the room — the service dock, where the real A.V.A. sits in her charge-cycle, eyes open, on the staff feed. She says it to no one:",
        "...Correct."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the hidden witness — the real machine is in the room the whole time, watching her own impersonation, and confirms the verdict aloud to no one",
      "participants": [
        "A.V.A."
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "DAMIEN",
            "MAYA"
          ],
          "seen_by": [
            "A.V.A."
          ],
          "channel": "staff feed",
          "from_zone": "penthouse salon chess area"
        }
      ],
      "location": {
        "zone": "penthouse salon service dock"
      },
      "timeline": [
        {
          "beat": "charge-cycle, eyes open — the staff feed is her window on the salon",
          "type": "held_action"
        },
        {
          "beat": "'...Correct.' — agreement nobody hears",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Damien and Maya exist for her only on the feed — depicted-through-channel, not co-present in her frame",
        "the dock must read as furniture-with-eyes — she is the room's other occupant, unacknowledged"
      ],
      "audio_requirements": [
        "charge-cycle hum — the dock's quiet machine presence across the room"
      ],
      "continuity_constraints": [
        "same watching posture as s23 — eyes open on the dock; her line is spoken to no one"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s25.sh04",
        "s25.snd01"
      ]
    },
    {
      "event_id": "s25.e04",
      "source_evidence": [
        "Maya recovers — glacial, perfect, machine-smooth:",
        "A startle reflex was added for social realism. Version 4.1. Flagging it as oversensitive.",
        "(still watching her)",
        "Dial it up."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the cover-up that almost works — she sells the flinch back to him as a feature; his 'dial it up' accepts the lie because he liked the truth",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "remote_participants": [],
      "location": {
        "zone": "penthouse salon chess area"
      },
      "timeline": [
        {
          "beat": "the recovery — glacial, perfect, machine-smooth",
          "type": "reaction"
        },
        {
          "beat": "the cover story — startle reflex, version 4.1, 'flagging it as oversensitive'",
          "type": "dialogue"
        },
        {
          "beat": "'Dial it up.' — still watching her",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "her recovery is over-corrected — too smooth, which is its own tell",
        "'still watching her' — his gaze stays a beat too long; he is testing, not convinced"
      ],
      "audio_requirements": [],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s25.sh05",
        "s25.sh06"
      ]
    },
    {
      "event_id": "s25.e05",
      "source_evidence": [
        "He goes back to the board. Maya stares at him — and for once the mask slips just enough that if he looked up, everything would be over. He doesn't look up. He moves his knight and says, to the board:",
        "Don't ever roll it back."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the buried confession — he tells the board, not her face, that he wants the flaw kept; her slipped mask is only safe because he chooses not to look",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "remote_participants": [],
      "location": {
        "zone": "penthouse salon chess area"
      },
      "timeline": [
        {
          "beat": "he goes back to the board — moves his knight, doesn't look up",
          "type": "action"
        },
        {
          "beat": "Maya stares — the mask slips; if he looked up it would be over",
          "type": "held_reaction"
        },
        {
          "beat": "'Don't ever roll it back.' — said to the board",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the line is addressed to the chessboard — the frame must show him NOT looking while her face is unguarded",
        "the mask-slip lives in one frame-safe expression: everything visible, nothing confirmed"
      ],
      "audio_requirements": [
        "knight move on the board — the line said to the game, not to her"
      ],
      "continuity_constraints": [
        "'roll it back' refers to the version-4.1 'startle reflex' she just invented — he is protecting the humanity he almost caught"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s25.sh07",
        "s25.snd01"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s25.sh01",
      "size": "two-shot",
      "zone": "penthouse salon chess area",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "implements": [
        "s25.e01"
      ],
      "covers_beats": {
        "s25.e01": [
          0,
          1,
          2,
          3
        ]
      },
      "purpose": "the easy game — she throws the queen, he starts a compliment he won't finish",
      "audio_note": "chess pieces moved on board, salon room tone",
      "dialogue_lines": [
        {
          "event_id": "s25.e01",
          "speaker": "DAMIEN",
          "line": "You hung your queen.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s25.e01",
          "speaker": "MAYA",
          "line": "I was told queens are expendable. Faulty module.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s25.e01",
          "speaker": "DAMIEN",
          "line": "You're getting worse at chess and better at—",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        }
      ]
    },
    {
      "shot_id": "s25.sh02",
      "size": "INS hands",
      "zone": "penthouse salon chess area",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "implements": [
        "s25.e02"
      ],
      "covers_beats": {
        "s25.e02": [
          0,
          1
        ]
      },
      "purpose": "reach — brush — flinch: the hand retreats before any face could be composed",
      "audio_note": "room tone drops out on the flinch"
    },
    {
      "shot_id": "s25.sh03",
      "size": "M held",
      "zone": "penthouse salon chess area",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "implements": [
        "s25.e02"
      ],
      "covers_beats": {
        "s25.e02": [
          2,
          3
        ]
      },
      "purpose": "the chess piece rocks and stills in silence; he says it slowly — the verdict",
      "audio_note": "chess piece rocking to stillness, held silence",
      "dialogue_lines": [
        {
          "event_id": "s25.e02",
          "speaker": "DAMIEN",
          "line": "Robots don't flinch.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        }
      ]
    },
    {
      "shot_id": "s25.sh04",
      "size": "M",
      "zone": "penthouse salon service dock",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "depicts": [
        {
          "actors": [
            "DAMIEN",
            "MAYA"
          ],
          "channel": "staff feed"
        }
      ],
      "implements": [
        "s25.e03"
      ],
      "covers_beats": {
        "s25.e03": [
          0,
          1
        ]
      },
      "purpose": "across the room — the real A.V.A. on charge-cycle, eyes open, agreeing with the verdict to no one",
      "audio_note": "charge-cycle hum",
      "dialogue_lines": [
        {
          "event_id": "s25.e03",
          "speaker": "A.V.A.",
          "line": "...Correct.",
          "line_kind": "on_camera",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s25.sh05",
      "size": "CU",
      "zone": "penthouse salon chess area",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s25.e04"
      ],
      "covers_beats": {
        "s25.e04": [
          0,
          1
        ]
      },
      "purpose": "the glacial recovery — she sells the flinch as a shipped feature",
      "dialogue_lines": [
        {
          "event_id": "s25.e04",
          "speaker": "MAYA",
          "line": "A startle reflex was added for social realism. Version 4.1. Flagging it as oversensitive.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s25.sh06",
      "size": "CU",
      "zone": "penthouse salon chess area",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s25.e04"
      ],
      "covers_beats": {
        "s25.e04": [
          2
        ]
      },
      "purpose": "still watching her — 'Dial it up.' he accepts the lie because he liked the truth",
      "dialogue_lines": [
        {
          "event_id": "s25.e04",
          "speaker": "DAMIEN",
          "line": "Dial it up.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s25.sh07",
      "size": "two-shot",
      "zone": "penthouse salon chess area",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "implements": [
        "s25.e05"
      ],
      "covers_beats": {
        "s25.e05": [
          0,
          1,
          2
        ]
      },
      "purpose": "he plays to the board while her mask slips — 'Don't ever roll it back.'",
      "audio_note": "knight move clicks on the board",
      "dialogue_lines": [
        {
          "event_id": "s25.e05",
          "speaker": "DAMIEN",
          "line": "Don't ever roll it back.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s25.snd01",
      "type": "sound",
      "implements": [
        "s25.e02",
        "s25.e03",
        "s25.e05"
      ],
      "purpose": "sound card: flinch silence with room tone dropped, chess piece rocking to stillness, charge-cycle hum across the room, knight click — the salon's held breath",
      "audio_note": "room tone drops on the flinch, chess piece rocking to stillness, distant charge-cycle hum at the dock, knight move click",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "a chess board between them she is deliberately losing badly at",
      "disposition": "covered_by",
      "by": [
        "s25.e01"
      ]
    },
    {
      "span": "You hung your queen.",
      "disposition": "covered_by",
      "by": [
        "s25.e01"
      ]
    },
    {
      "span": "I was told queens are expendable. Faulty module.",
      "disposition": "covered_by",
      "by": [
        "s25.e01"
      ]
    },
    {
      "span": "You're getting worse at chess and better at—",
      "disposition": "covered_by",
      "by": [
        "s25.e01"
      ]
    },
    {
      "span": "He reaches across the board to correct her knight — and brushes her hand.",
      "disposition": "covered_by",
      "by": [
        "s25.e02"
      ]
    },
    {
      "span": "She flinches.",
      "disposition": "covered_by",
      "by": [
        "s25.e02"
      ]
    },
    {
      "span": "A small, fast, utterly human flinch",
      "disposition": "covered_by",
      "by": [
        "s25.e02"
      ]
    },
    {
      "span": "Silence. The chess piece rocks and stills.",
      "disposition": "covered_by",
      "by": [
        "s25.e02"
      ]
    },
    {
      "span": "Robots don't flinch.",
      "disposition": "covered_by",
      "by": [
        "s25.e02"
      ]
    },
    {
      "span": "the real A.V.A. sits in her charge-cycle, eyes open, on the staff feed",
      "disposition": "covered_by",
      "by": [
        "s25.e03"
      ]
    },
    {
      "span": "...Correct.",
      "disposition": "covered_by",
      "by": [
        "s25.e03"
      ]
    },
    {
      "span": "Maya recovers — glacial, perfect, machine-smooth:",
      "disposition": "covered_by",
      "by": [
        "s25.e04"
      ]
    },
    {
      "span": "A startle reflex was added for social realism. Version 4.1.",
      "disposition": "covered_by",
      "by": [
        "s25.e04"
      ]
    },
    {
      "span": "Dial it up.",
      "disposition": "covered_by",
      "by": [
        "s25.e04"
      ]
    },
    {
      "span": "the mask slips just enough that if he looked up, everything would be over",
      "disposition": "covered_by",
      "by": [
        "s25.e05"
      ]
    },
    {
      "span": "He moves his knight and says, to the board:",
      "disposition": "covered_by",
      "by": [
        "s25.e05"
      ]
    },
    {
      "span": "Don't ever roll it back.",
      "disposition": "covered_by",
      "by": [
        "s25.e05"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['DAMIEN', 'MAYA'] | -  | DAMIEN and MAYA-A.V.A. — a chess board between them she is deliberately losing b
i02 blk=['DAMIEN', 'MAYA'] | DAMIEN You hung your queen. | DAMIEN faces MAYA and speaks.
i03 blk=['MAYA'] | MAYA I was told queens are expendable. Faulty module. | MAYA faces DAMIEN and speaks.
i04 blk=['DAMIEN'] | DAMIEN You're getting worse at chess and better at— | DAMIEN faces MAYA and speaks.
i05 blk=['MAYA'] | -  | He reaches across the board to correct her knight — and brushes her hand. She fl
i06 blk=['MAYA'] | -  | A small, fast, utterly human flinch — the hand retreating before the face can be
i07 blk=['MAYA', 'DAMIEN'] | DAMIEN Robots don't flinch. | DAMIEN faces MAYA and speaks.
i08 blk=['MAYA'] | -  | Across the room — the service dock, where the real A.V.A. sits in her charge-cyc
i09 blk=['A.V.A.', 'DAMIEN'] | A.V.A. ...Correct. | A.V.A. faces DAMIEN and speaks.
i10 blk=['MAYA'] | MAYA A startle reflex was added for social realism. Version 4.1.  | Maya recovers — glacial, perfect, machine-smooth.
i11 blk=['DAMIEN', 'MAYA'] | DAMIEN Dial it up. | DAMIEN faces MAYA and speaks.
i12 blk=['MAYA'] | -  | He goes back to the board. Maya stares at him — and for once the mask slips just
i13 blk=['DAMIEN'] | DAMIEN Don't ever roll it back. | DAMIEN faces MAYA and speaks.