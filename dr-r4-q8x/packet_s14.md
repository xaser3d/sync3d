# VALIDATION PACKET — scene s14
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 14 — INT. THE MERIDIAN ROOM — RESTAURANT — NIGHT (DATE ONE)

*SOPHIA VANE across the table — beautiful, practiced, checking her
phone under her napkin. DAMIEN wears an earpiece disguised as a
studs earring. At VOLT LAB, MAYA sits in a rig of monitors —
audio feed, a vitals readout she keeps pretending not to watch.*

MAYA (V.O., in his ear)
Opening line. Not the compliment protocol. The fire question.

DAMIEN
What would you save from a fire?

SOPHIA
(blinking)
My Birkins. Obviously. You'd save your—? Actually, don't answer,
I already respect it.

MAYA (V.O.)
Ask about the Meridian. Her yacht. Specifically the depreciation
curve.

DAMIEN
The Meridian — beautiful boat. How's she holding her value?

*Sophia's smile freezes. Under the table, her phone is suddenly
very interesting.*

SOPHIA
She's... an asset. Who talks depreciation at dinner?

MAYA (V.O.)
(deadpan)
Someone whose broker told her a secret.

DAMIEN
Someone whose broker told me a secret.

*Sophia goes pale. The yacht is three payments behind — Victor
assured her it was a secret.*

SOPHIA
Excuse me. Powder room.

*She leaves and doesn't come back. At the lab, Maya leans back,
satisfied. J-7, watching the feed:*

J-7
Candidate one: eliminated. Shall I log it as a technical success
or a personal victory?

MAYA
Technical. She was on Victor's payroll.

J-7
Mm. And the payroll was on a yacht.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 14,
  "scene_heading": "INT. THE MERIDIAN ROOM — RESTAURANT — NIGHT (DATE ONE)",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "Date one of Victor's shortlist. Maya runs the evening from a Volt Lab rig — audio feed, an earpiece disguised as jewelry, and a vitals readout she keeps pretending not to watch. She kills candidate one with the fire question she taught Damien in S11 plus one loaded fact: Sophia's yacht is three payments behind and on Victor's payroll. The date ends with 'powder room' and the lab debrief logs it as a technical success.",
  "zones": [
    "meridian room restaurant",
    "volt lab"
  ],
  "events": [
    {
      "event_id": "s14.e01",
      "source_evidence": [
        "SOPHIA VANE across the table — beautiful, practiced, checking her",
        "phone under her napkin. DAMIEN wears an earpiece disguised as a",
        "studs earring. At VOLT LAB, MAYA sits in a rig of monitors —",
        "audio feed, a vitals readout she keeps pretending not to watch."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "two rooms, one wire — the date and its control room established in a single paragraph; the vitals readout is the scene's real tell",
      "participants": [
        "SOPHIA",
        "DAMIEN",
        "MAYA"
      ],
      "remote_participants": [],
      "location": {
        "zones": [
          "meridian room restaurant",
          "volt lab"
        ],
        "primary": "meridian room restaurant"
      },
      "timeline": [
        {
          "beat": "the table — Sophia beautiful and practiced, phone under the napkin; the earpiece disguised as a studs earring",
          "type": "atmosphere"
        },
        {
          "beat": "at the lab — Maya in the rig of monitors, audio feed, the vitals readout she pretends not to watch",
          "type": "action"
        }
      ],
      "visual_requirements": [
        "Sophia's practiced phone-check reads as disinterest already performed, not boredom developing",
        "the vitals readout must be legible as HIS vitals — her pretending not to watch is the characterization"
      ],
      "audio_requirements": [
        "restaurant murmur against lab rig hum — the two room tones of the operation"
      ],
      "continuity_constraints": [
        "the earpiece is disguised as a studs earring — the prop must read jewelry in the restaurant wide"
      ],
      "ambiguities": [],
      "must_appear": [
        "SOPHIA",
        "DAMIEN",
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s14.sh01",
        "s14.sh02"
      ]
    },
    {
      "event_id": "s14.e02",
      "source_evidence": [
        "Opening line. Not the compliment protocol. The fire question.",
        "What would you save from a fire?",
        "My Birkins. Obviously. You'd save your—? Actually, don't answer,",
        "I already respect it."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the planted question deployed — Maya's S11 lesson arrives via wire, and Sophia's Birkins answer grades itself",
      "participants": [
        "DAMIEN",
        "SOPHIA"
      ],
      "remote_participants": [
        {
          "actor": "MAYA",
          "channel": "earpiece",
          "direction": "out"
        }
      ],
      "location": {
        "zone": "meridian room restaurant"
      },
      "timeline": [
        {
          "beat": "Maya in his ear — 'Not the compliment protocol. The fire question.'",
          "type": "dialogue_remote"
        },
        {
          "beat": "'What would you save from a fire?'",
          "type": "dialogue"
        },
        {
          "beat": "'My Birkins. Obviously.' — self-grading answer",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Damien delivers the question like it was his — the coaching seam must stay invisible to Sophia"
      ],
      "audio_requirements": [
        "Maya's voice close in the earpiece — a private channel under the restaurant murmur"
      ],
      "continuity_constraints": [
        "the fire question is the S11 counter-lesson made ammunition — delivery should carry the memory of that scene"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "SOPHIA"
      ],
      "tableau": true,
      "shot_sequence": [
        "s14.sh03",
        "s14.snd01"
      ]
    },
    {
      "event_id": "s14.e03",
      "source_evidence": [
        "Ask about the Meridian. Her yacht. Specifically the depreciation",
        "curve.",
        "The Meridian — beautiful boat. How's she holding her value?",
        "Sophia's smile freezes. Under the table, her phone is suddenly",
        "very interesting."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the strike set — the yacht named and the depreciation question that turns small talk into an audit",
      "participants": [
        "DAMIEN",
        "SOPHIA"
      ],
      "remote_participants": [
        {
          "actor": "MAYA",
          "channel": "earpiece",
          "direction": "out"
        }
      ],
      "location": {
        "zone": "meridian room restaurant"
      },
      "timeline": [
        {
          "beat": "Maya feeds the line — 'Ask about the Meridian. Her yacht. Specifically the depreciation curve.'",
          "type": "dialogue_remote"
        },
        {
          "beat": "'The Meridian — beautiful boat. How's she holding her value?'",
          "type": "dialogue"
        },
        {
          "beat": "the smile freezes — the phone under the table suddenly very interesting",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "the freeze is the tell — her phone becomes a refuge, not a habit"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the Meridian was planted as 'yachts, yacht litigation' in S13 — this is the gun firing"
      ],
      "ambiguities": [],
      "must_appear": [
        "SOPHIA",
        "DAMIEN"
      ],
      "tableau": true,
      "shot_sequence": [
        "s14.sh04"
      ]
    },
    {
      "event_id": "s14.e04",
      "source_evidence": [
        "She's... an asset. Who talks depreciation at dinner?",
        "Someone whose broker told her a secret.",
        "Someone whose broker told me a secret.",
        "Sophia goes pale. The yacht is three payments behind — Victor",
        "assured her it was a secret.",
        "Excuse me. Powder room.",
        "She leaves and doesn't come back."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the kill — the deadpan line fed and repeated, the secret exposed, candidate one eliminated by 'powder room'",
      "participants": [
        "DAMIEN",
        "SOPHIA"
      ],
      "remote_participants": [
        {
          "actor": "MAYA",
          "channel": "earpiece",
          "direction": "out"
        }
      ],
      "location": {
        "zone": "meridian room restaurant"
      },
      "timeline": [
        {
          "beat": "'She's... an asset. Who talks depreciation at dinner?'",
          "type": "dialogue"
        },
        {
          "beat": "Maya deadpan in his ear — 'Someone whose broker told her a secret.'",
          "type": "dialogue_remote"
        },
        {
          "beat": "'Someone whose broker told me a secret.' — delivered as his own",
          "type": "dialogue"
        },
        {
          "beat": "she goes pale — three payments behind, and Victor had assured her it was a secret",
          "type": "reveal"
        },
        {
          "beat": "'Excuse me. Powder room.'",
          "type": "dialogue"
        },
        {
          "beat": "she leaves and doesn't come back",
          "type": "action"
        }
      ],
      "visual_requirements": [
        "the pale-going is the reveal rendered on her face — the narrator's 'three payments behind' is played, not spoken",
        "the exit must read permanent — 'powder room' as a door she never comes back through"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "Victor's assurance = the payroll link Maya names in e05 — the secret's leak path is Victor himself"
      ],
      "ambiguities": [],
      "must_appear": [
        "SOPHIA",
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s14.sh05"
      ]
    },
    {
      "event_id": "s14.e05",
      "source_evidence": [
        "At the lab, Maya leans back,",
        "satisfied. J-7, watching the feed:",
        "Candidate one: eliminated. Shall I log it as a technical success",
        "or a personal victory?",
        "Technical. She was on Victor's payroll.",
        "Mm. And the payroll was on a yacht."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the debrief — satisfaction logged as arithmetic, and the Victor link confirmed: the payroll was on a yacht",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "DAMIEN"
          ],
          "seen_by": [
            "MAYA",
            "J-7"
          ],
          "channel": "date feed",
          "from_zone": "meridian room restaurant"
        }
      ],
      "location": {
        "zone": "volt lab"
      },
      "timeline": [
        {
          "beat": "Maya leans back, satisfied — J-7 watching the feed",
          "type": "reaction"
        },
        {
          "beat": "'Candidate one: eliminated. Shall I log it as a technical success or a personal victory?'",
          "type": "dialogue"
        },
        {
          "beat": "'Technical. She was on Victor's payroll.'",
          "type": "dialogue"
        },
        {
          "beat": "'Mm. And the payroll was on a yacht.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "her lean-back is earned satisfaction she would deny — the personal victory J-7 offers is the truth she files under 'technical'"
      ],
      "audio_requirements": [
        "lab rig hum and the feed settling — the room tone after a kill"
      ],
      "continuity_constraints": [
        "J-7 is the lab's institutional memory — his 'log it' framing matches his S23 register of gentle arithmetic"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "J-7"
      ],
      "tableau": true,
      "shot_sequence": [
        "s14.sh06",
        "s14.snd01"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s14.sh01",
      "size": "M two-shot",
      "zone": "meridian room restaurant",
      "type": "visual",
      "participants": [
        "SOPHIA",
        "DAMIEN"
      ],
      "implements": [
        "s14.e01"
      ],
      "covers_beats": {
        "s14.e01": [
          0
        ]
      },
      "purpose": "the table — practiced beauty, phone under the napkin, the earring that is an earpiece",
      "audio_note": "restaurant murmur, cutlery, low room tone"
    },
    {
      "shot_id": "s14.sh02",
      "size": "M",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s14.e01"
      ],
      "covers_beats": {
        "s14.e01": [
          1
        ]
      },
      "purpose": "the control room — Maya in the rig, audio feed, the vitals readout she pretends not to watch",
      "audio_note": "rig monitors hum, feed static tick"
    },
    {
      "shot_id": "s14.sh03",
      "size": "two-shot",
      "zone": "meridian room restaurant",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "SOPHIA"
      ],
      "implements": [
        "s14.e02"
      ],
      "covers_beats": {
        "s14.e02": [
          0,
          1,
          2
        ]
      },
      "purpose": "the fire question delivered as his own → 'My Birkins. Obviously.' — self-grading answer",
      "audio_note": "earpiece feed under the murmur",
      "dialogue_lines": [
        {
          "event_id": "s14.e02",
          "speaker": "MAYA",
          "line": "Opening line. Not the compliment protocol. The fire question.",
          "line_kind": "earpiece",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s14.e02",
          "speaker": "DAMIEN",
          "line": "What would you save from a fire?",
          "line_kind": "on_camera",
          "recipient": "SOPHIA",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s14.e02",
          "speaker": "SOPHIA",
          "line": "My Birkins. Obviously. You'd save your—? Actually, don't answer, I already respect it.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s14.sh04",
      "size": "CU→two-shot",
      "zone": "meridian room restaurant",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "SOPHIA"
      ],
      "implements": [
        "s14.e03"
      ],
      "covers_beats": {
        "s14.e03": [
          0,
          1,
          2
        ]
      },
      "purpose": "the Meridian named — depreciation question lands, the smile freezes and the phone becomes refuge",
      "audio_note": "earpiece feed, restaurant murmur continuing",
      "dialogue_lines": [
        {
          "event_id": "s14.e03",
          "speaker": "MAYA",
          "line": "Ask about the Meridian. Her yacht. Specifically the depreciation curve.",
          "line_kind": "earpiece",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s14.e03",
          "speaker": "DAMIEN",
          "line": "The Meridian — beautiful boat. How's she holding her value?",
          "line_kind": "on_camera",
          "recipient": "SOPHIA",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s14.sh05",
      "size": "CU SOPHIA→two-shot",
      "zone": "meridian room restaurant",
      "type": "visual",
      "participants": [
        "SOPHIA",
        "DAMIEN"
      ],
      "implements": [
        "s14.e04"
      ],
      "covers_beats": {
        "s14.e04": [
          0,
          1,
          2,
          3,
          4,
          5
        ]
      },
      "purpose": "the kill — deadpan fed and repeated, she goes pale on the three-payments-behind reveal, 'powder room' exit that doesn't come back",
      "audio_note": "earpiece deadpan, chair push, her exit footsteps",
      "dialogue_lines": [
        {
          "event_id": "s14.e04",
          "speaker": "SOPHIA",
          "line": "She's... an asset. Who talks depreciation at dinner?",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s14.e04",
          "speaker": "MAYA",
          "line": "Someone whose broker told her a secret.",
          "line_kind": "earpiece",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s14.e04",
          "speaker": "DAMIEN",
          "line": "Someone whose broker told me a secret.",
          "line_kind": "on_camera",
          "recipient": "SOPHIA",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s14.e04",
          "speaker": "SOPHIA",
          "line": "Excuse me. Powder room.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            4
          ]
        }
      ]
    },
    {
      "shot_id": "s14.sh06",
      "size": "M two-shot",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "depicts": [
        {
          "actors": [
            "DAMIEN"
          ],
          "channel": "date feed"
        }
      ],
      "implements": [
        "s14.e05"
      ],
      "covers_beats": {
        "s14.e05": [
          0,
          1,
          2,
          3
        ]
      },
      "purpose": "the debrief — lean-back satisfaction, 'technical success or personal victory', and the payroll-on-a-yacht button",
      "audio_note": "lab rig hum, feed settling",
      "dialogue_lines": [
        {
          "event_id": "s14.e05",
          "speaker": "J-7",
          "line": "Candidate one: eliminated. Shall I log it as a technical success or a personal victory?",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s14.e05",
          "speaker": "MAYA",
          "line": "Technical. She was on Victor's payroll.",
          "line_kind": "on_camera",
          "recipient": "J-7",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s14.e05",
          "speaker": "J-7",
          "line": "Mm. And the payroll was on a yacht.",
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
      "shot_id": "s14.snd01",
      "type": "sound",
      "implements": [
        "s14.e02",
        "s14.e05"
      ],
      "purpose": "sound card: earpiece intimacy against restaurant murmur at the table, lab rig hum at the console — the two room tones of the operation; no score",
      "audio_note": "Maya's voice close in the earpiece feed under restaurant murmur, lab rig hum",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "SOPHIA VANE across the table — beautiful, practiced, checking her phone under her napkin.",
      "disposition": "covered_by",
      "by": [
        "s14.e01"
      ]
    },
    {
      "span": "DAMIEN wears an earpiece disguised as a studs earring.",
      "disposition": "covered_by",
      "by": [
        "s14.e01"
      ]
    },
    {
      "span": "MAYA sits in a rig of monitors — audio feed, a vitals readout she keeps pretending not to watch.",
      "disposition": "covered_by",
      "by": [
        "s14.e01"
      ]
    },
    {
      "span": "Opening line. Not the compliment protocol. The fire question.",
      "disposition": "covered_by",
      "by": [
        "s14.e02"
      ]
    },
    {
      "span": "What would you save from a fire?",
      "disposition": "covered_by",
      "by": [
        "s14.e02"
      ]
    },
    {
      "span": "My Birkins. Obviously. You'd save your—? Actually, don't answer, I already respect it.",
      "disposition": "covered_by",
      "by": [
        "s14.e02"
      ]
    },
    {
      "span": "Ask about the Meridian. Her yacht. Specifically the depreciation curve.",
      "disposition": "covered_by",
      "by": [
        "s14.e03"
      ]
    },
    {
      "span": "The Meridian — beautiful boat. How's she holding her value?",
      "disposition": "covered_by",
      "by": [
        "s14.e03"
      ]
    },
    {
      "span": "Sophia's smile freezes. Under the table, her phone is suddenly very interesting.",
      "disposition": "covered_by",
      "by": [
        "s14.e03"
      ]
    },
    {
      "span": "She's... an asset. Who talks depreciation at dinner?",
      "disposition": "covered_by",
      "by": [
        "s14.e04"
      ]
    },
    {
      "span": "Someone whose broker told her a secret.",
      "disposition": "covered_by",
      "by": [
        "s14.e04"
      ]
    },
    {
      "span": "Someone whose broker told me a secret.",
      "disposition": "covered_by",
      "by": [
        "s14.e04"
      ]
    },
    {
      "span": "Sophia goes pale. The yacht is three payments behind — Victor assured her it was a secret.",
      "disposition": "covered_by",
      "by": [
        "s14.e04"
      ]
    },
    {
      "span": "Excuse me. Powder room.",
      "disposition": "covered_by",
      "by": [
        "s14.e04"
      ]
    },
    {
      "span": "She leaves and doesn't come back.",
      "disposition": "covered_by",
      "by": [
        "s14.e04"
      ]
    },
    {
      "span": "At the lab, Maya leans back, satisfied.",
      "disposition": "covered_by",
      "by": [
        "s14.e05"
      ]
    },
    {
      "span": "Candidate one: eliminated. Shall I log it as a technical success or a personal victory?",
      "disposition": "covered_by",
      "by": [
        "s14.e05"
      ]
    },
    {
      "span": "Technical. She was on Victor's payroll.",
      "disposition": "covered_by",
      "by": [
        "s14.e05"
      ]
    },
    {
      "span": "Mm. And the payroll was on a yacht.",
      "disposition": "covered_by",
      "by": [
        "s14.e05"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['SOPHIA', 'DAMIEN'] | -  | SOPHIA VANE across the table — beautiful, practiced, checking her phone under he
i02 blk=['MAYA', 'DAMIEN'] | MAYA Opening line. Not the compliment protocol. The fire question | MAYA faces DAMIEN and speaks.
i03 blk=['DAMIEN'] | DAMIEN What would you save from a fire? | DAMIEN faces MAYA and speaks.
i04 blk=['SOPHIA'] | SOPHIA My Birkins. Obviously. You'd save your—? Actually, don't ans | SOPHIA faces MAYA and speaks.
i05 blk=['MAYA'] | MAYA Ask about the Meridian. Her yacht. Specifically the deprecia | MAYA faces DAMIEN and speaks.
i06 blk=['SOPHIA', 'DAMIEN'] | DAMIEN The Meridian — beautiful boat. How's she holding her value? | DAMIEN faces MAYA and speaks.
i07 blk=['SOPHIA'] | SOPHIA She's... an asset. Who talks depreciation at dinner? | Sophia's smile freezes. Under the table, her phone is suddenly very interesting.
i08 blk=['MAYA'] | MAYA Someone whose broker told her a secret. | MAYA faces DAMIEN and speaks.
i09 blk=['DAMIEN'] | DAMIEN Someone whose broker told me a secret. | DAMIEN faces MAYA and speaks.
i10 blk=['SOPHIA'] | SOPHIA Excuse me. Powder room. | Sophia goes pale. The yacht is three payments behind — Victor assured her it was
i11 blk=['J-7', 'MAYA'] | J-7 Candidate one: eliminated. Shall I log it as a technical suc | She leaves and doesn't come back. At the lab, Maya leans back, satisfied. J-7, w
i12 blk=['MAYA'] | MAYA Technical. She was on Victor's payroll. | MAYA faces DAMIEN and speaks.
i13 blk=['J-7'] | J-7 Mm. And the payroll was on a yacht. | J-7 faces MAYA and speaks.