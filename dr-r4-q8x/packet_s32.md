# VALIDATION PACKET — scene s32
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 32 — INT. VICTOR'S OFFICE — NIGHT

*The photo on Victor's screen: a grainy service-corridor frame —
two identical women, one rigid on a gurney, one alive and
smoothing her dress.*

VICTOR
(to the empty room, delighted)
A person.

*He leans back, the smile genuine and terrible.*

VICTOR (CONT'D)
My brother's courtship coach is a PERSON. The lab committed fraud,
the companionship is a lie, and the trust clause —

*He opens a calendar. Damien's birthday gala circled in red.*

VICTOR (CONT'D)
— detonates on a stage, in front of everyone who matters.
Announcement the same night: Damien's engagement. To Sophia —
she owes me the estate, she'll say yes to anything, and a
blackmailed bride still counts as a bride under Section 14.
He'll be married, ruined, and mine by midnight.

*He picks up the phone.*

VICTOR (CONT'D)
Get me the gala's technical director. I need a screen.

---

**END OF ACT 2**


========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 32,
  "scene_heading": "SCENE 32 — INT. VICTOR'S OFFICE — NIGHT",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "END OF ACT 2 button. Victor alone in his office reads Vega's service-corridor photo and articulates the entire trap out loud to nobody: expose the 'fraud' at Damien's birthday gala, then satisfy the trust clause with a blackmailed bride — Sophia, who owes him the estate. Everything S33 executes is spoken here first, in an empty room, delighted.",
  "zones": [
    "victor's office"
  ],
  "events": [
    {
      "event_id": "s32.e01",
      "source_evidence": [
        "The photo on Victor's screen: a grainy service-corridor frame —",
        "two identical women, one rigid on a gurney, one alive and",
        "smoothing her dress."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the payload on screen — we see the evidence that ends Act 2",
      "participants": [
        "VICTOR"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "MAYA",
            "A.V.A."
          ],
          "seen_by": [
            "VICTOR"
          ],
          "channel": "screen photo",
          "from_zone": "service corridor (s31)"
        }
      ],
      "location": {
        "zone": "victor's office"
      },
      "timeline": [
        {
          "beat": "the grainy service-corridor frame on Victor's screen",
          "type": "insert"
        },
        {
          "beat": "two identical women — one rigid on a gurney, one alive and smoothing her dress",
          "type": "reveal"
        }
      ],
      "visual_requirements": [
        "the photo must read at a glance — corridor, gurney, the double",
        "grainy long-lens quality — evidence, not a portrait"
      ],
      "audio_requirements": [
        "screen glow hum in an empty office"
      ],
      "continuity_constraints": [
        "the frame matches what Vega shot in S30 and described in S31 — same corridor image"
      ],
      "ambiguities": [
        "frame reads as Vega's S30 long-lens shot — inferred from her 'both of them in one frame', not labeled in the text"
      ],
      "must_appear": [
        "VICTOR"
      ],
      "tableau": false,
      "shot_sequence": [
        "s32.sh01",
        "s32.snd01"
      ]
    },
    {
      "event_id": "s32.e02",
      "source_evidence": [
        "(to the empty room, delighted)",
        "A person.",
        "He leans back, the smile genuine and terrible."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the verdict lands as pleasure — 'a person' is the whole fraud in two words",
      "participants": [
        "VICTOR"
      ],
      "remote_participants": [],
      "location": {
        "zone": "victor's office"
      },
      "timeline": [
        {
          "beat": "'A person.' — delighted, to an empty room",
          "type": "dialogue"
        },
        {
          "beat": "he leans back — the smile genuine and terrible",
          "type": "held_reaction"
        }
      ],
      "visual_requirements": [
        "he is alone — the performance has no audience, which is the point",
        "the smile held past the line — genuine and terrible at once"
      ],
      "audio_requirements": [
        "his voice into an empty office room tone"
      ],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "VICTOR"
      ],
      "tableau": false,
      "shot_sequence": [
        "s32.sh02"
      ]
    },
    {
      "event_id": "s32.e03",
      "source_evidence": [
        "My brother's courtship coach is a PERSON. The lab committed fraud, the companionship is a lie, and the trust clause —"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "Victor reasons it into a weapon — fraud, lie, clause — the sentence cut off by the calendar",
      "participants": [
        "VICTOR"
      ],
      "remote_participants": [],
      "location": {
        "zone": "victor's office"
      },
      "timeline": [
        {
          "beat": "the realization spoken — coach is a PERSON, lab fraud, companionship a lie, the trust clause—",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the sentence breaks off — the calendar interrupts him mid-clause"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the cut-off sentence resumes after the calendar insert in e05 — same breath, split by the insert"
      ],
      "ambiguities": [],
      "must_appear": [
        "VICTOR"
      ],
      "tableau": false,
      "shot_sequence": [
        "s32.sh03"
      ]
    },
    {
      "event_id": "s32.e04",
      "source_evidence": [
        "He opens a calendar. Damien's birthday gala circled in red."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the stage is chosen — the red circle picks the date the clause detonates",
      "participants": [
        "VICTOR"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "VICTOR"
      ],
      "document_evidence": [
        {
          "author": "VICTOR",
          "artifact": "calendar — Damien's birthday gala circled in red",
          "channel": "document"
        }
      ],
      "location": {
        "zone": "victor's office"
      },
      "timeline": [
        {
          "beat": "he opens a calendar",
          "type": "action"
        },
        {
          "beat": "Damien's birthday gala circled in red — the target date",
          "type": "reveal"
        }
      ],
      "visual_requirements": [
        "the red circle must read as a decision, not a reminder",
        "insert grammar — hands may enter frame, no face required"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "this date is the S33 gala — the same event the trap is built around"
      ],
      "ambiguities": [],
      "must_appear": [],
      "tableau": false,
      "shot_sequence": [
        "s32.sh04"
      ]
    },
    {
      "event_id": "s32.e05",
      "source_evidence": [
        "— detonates on a stage, in front of everyone who matters.",
        "Announcement the same night: Damien's engagement. To Sophia — she owes me the estate, she'll say yes to anything, and a blackmailed bride still counts as a bride under Section 14.",
        "He'll be married, ruined, and mine by midnight."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the whole trap spoken — detonation venue, the engagement mechanism, Section 14, 'mine by midnight'",
      "participants": [
        "VICTOR"
      ],
      "remote_participants": [],
      "location": {
        "zone": "victor's office"
      },
      "timeline": [
        {
          "beat": "— detonates on a stage, in front of everyone who matters",
          "type": "dialogue"
        },
        {
          "beat": "the engagement scheme — Sophia owes him the estate, a blackmailed bride counts under Section 14",
          "type": "dialogue"
        },
        {
          "beat": "'married, ruined, and mine by midnight' — the deadline stated",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "held on him — the plan is a performance for an audience of zero"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "resumes the sentence e03 cut off — same monologue, the calendar was a held beat inside it",
        "Sophia's leverage ('owes me the estate') is the fact S33's 'in white' appearance cashes"
      ],
      "ambiguities": [],
      "must_appear": [
        "VICTOR"
      ],
      "tableau": false,
      "shot_sequence": [
        "s32.sh05"
      ]
    },
    {
      "event_id": "s32.e06",
      "source_evidence": [
        "He picks up the phone.",
        "Get me the gala's technical director. I need a screen."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the order that builds the gallows — the screen we watch him use in S33 is requisitioned here",
      "participants": [
        "VICTOR"
      ],
      "remote_participants": [],
      "location": {
        "zone": "victor's office"
      },
      "timeline": [
        {
          "beat": "he picks up the phone",
          "type": "action"
        },
        {
          "beat": "'Get me the gala's technical director. I need a screen.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the requisition reads casual — a logistics call that ends an empire"
      ],
      "audio_requirements": [
        "phone pickup"
      ],
      "continuity_constraints": [
        "the requested screen is 'a screen the size of a bus' in S33"
      ],
      "ambiguities": [
        "the technical director is an uncredited remote party — no cast entry; not declared remote_participants"
      ],
      "must_appear": [
        "VICTOR"
      ],
      "tableau": false,
      "shot_sequence": [
        "s32.sh06",
        "s32.snd01"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s32.sh01",
      "size": "INS",
      "zone": "victor's office",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "depicts": [
        {
          "actors": [
            "MAYA",
            "A.V.A."
          ],
          "channel": "screen photo"
        }
      ],
      "implements": [
        "s32.e01"
      ],
      "covers_beats": {
        "s32.e01": [
          0,
          1
        ]
      },
      "purpose": "the photo on his screen — corridor, gurney, the double; Victor's silhouette/shoulder at the frame edge",
      "audio_note": "screen glow hum in an empty office"
    },
    {
      "shot_id": "s32.sh02",
      "size": "M/CU",
      "zone": "victor's office",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "implements": [
        "s32.e02"
      ],
      "covers_beats": {
        "s32.e02": [
          0,
          1
        ]
      },
      "purpose": "'A person.' to the empty room — then the lean-back, the smile held past the line",
      "audio_note": "his voice into an empty office room tone",
      "dialogue_lines": [
        {
          "event_id": "s32.e02",
          "speaker": "VICTOR",
          "line": "A person.",
          "line_kind": "on_camera",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s32.sh03",
      "size": "M",
      "zone": "victor's office",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "implements": [
        "s32.e03"
      ],
      "covers_beats": {
        "s32.e03": [
          0
        ]
      },
      "purpose": "the realization reasoned into a weapon — the clause sentence breaking off",
      "audio_note": "empty-office room tone",
      "dialogue_lines": [
        {
          "event_id": "s32.e03",
          "speaker": "VICTOR",
          "line": "My brother's courtship coach is a PERSON. The lab committed fraud, the companionship is a lie, and the trust clause —",
          "line_kind": "on_camera",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s32.sh04",
      "size": "INS",
      "zone": "victor's office",
      "type": "visual",
      "participants": [],
      "implements": [
        "s32.e04"
      ],
      "covers_beats": {
        "s32.e04": [
          0,
          1
        ]
      },
      "purpose": "calendar insert — Damien's birthday gala circled in red; the target date becomes a decision",
      "audio_note": "empty-office room tone"
    },
    {
      "shot_id": "s32.sh05",
      "size": "M/CU",
      "zone": "victor's office",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "implements": [
        "s32.e05"
      ],
      "covers_beats": {
        "s32.e05": [
          0,
          1,
          2
        ]
      },
      "purpose": "the plan completed aloud — detonation venue, the engagement mechanism, 'mine by midnight'",
      "audio_note": "empty-office room tone",
      "dialogue_lines": [
        {
          "event_id": "s32.e05",
          "speaker": "VICTOR",
          "line": "— detonates on a stage, in front of everyone who matters.",
          "line_kind": "on_camera",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s32.e05",
          "speaker": "VICTOR",
          "line": "Announcement the same night: Damien's engagement. To Sophia — she owes me the estate, she'll say yes to anything, and a blackmailed bride still counts as a bride under Section 14.",
          "line_kind": "on_camera",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s32.e05",
          "speaker": "VICTOR",
          "line": "He'll be married, ruined, and mine by midnight.",
          "line_kind": "on_camera",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s32.sh06",
      "size": "M",
      "zone": "victor's office",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "implements": [
        "s32.e06"
      ],
      "covers_beats": {
        "s32.e06": [
          0,
          1
        ]
      },
      "purpose": "he picks up the phone and requisitions the screen — the act-3 gallows ordered as logistics",
      "audio_note": "phone pickup, empty-office room tone",
      "dialogue_lines": [
        {
          "event_id": "s32.e06",
          "speaker": "VICTOR",
          "line": "Get me the gala's technical director. I need a screen.",
          "line_kind": "on_camera",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s32.snd01",
      "type": "sound",
      "implements": [
        "s32.e01",
        "s32.e06"
      ],
      "purpose": "empty-office card — a man alone narrating his plan to nobody",
      "audio_note": "empty-office room tone, screen glow hum, phone pickup and dial tone — no score underneath",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "The photo on Victor's screen: a grainy service-corridor frame — two identical women, one rigid on a gurney, one alive and smoothing her dress.",
      "disposition": "covered_by",
      "by": [
        "s32.e01"
      ]
    },
    {
      "span": "A person.",
      "disposition": "covered_by",
      "by": [
        "s32.e02"
      ]
    },
    {
      "span": "He leans back, the smile genuine and terrible.",
      "disposition": "covered_by",
      "by": [
        "s32.e02"
      ]
    },
    {
      "span": "My brother's courtship coach is a PERSON. The lab committed fraud, the companionship is a lie, and the trust clause —",
      "disposition": "covered_by",
      "by": [
        "s32.e03"
      ]
    },
    {
      "span": "He opens a calendar. Damien's birthday gala circled in red.",
      "disposition": "covered_by",
      "by": [
        "s32.e04"
      ]
    },
    {
      "span": "— detonates on a stage, in front of everyone who matters. Announcement the same night: Damien's engagement.",
      "disposition": "covered_by",
      "by": [
        "s32.e05"
      ]
    },
    {
      "span": "He picks up the phone.",
      "disposition": "covered_by",
      "by": [
        "s32.e06"
      ]
    },
    {
      "span": "Get me the gala's technical director. I need a screen.",
      "disposition": "covered_by",
      "by": [
        "s32.e06"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['VICTOR'] | -  | The photo on Victor's screen: a grainy service-corridor frame — two identical wo
i02 blk=['VICTOR', 'DAMIEN'] | VICTOR A person. My brother's courtship coach is a PERSON. The lab  | VICTOR faces DAMIEN and speaks. He leans back, the smile genuine and terrible.
i03 blk=['VICTOR'] | VICTOR — detonates on a stage, in front of everyone who matters. An | He opens a calendar. Damien's birthday gala circled in red.
i04 blk=['VICTOR'] | VICTOR Get me the gala's technical director. I need a screen. | He picks up the phone.
i05 blk=['DAMIEN'] | -  | END OF ACT 2.