# VALIDATION PACKET — scene s37
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 37 — INT. BALLROOM — BAR — NIGHT

*The after-chaos: everyone talking, nobody eating. SOPHIA finds
MAYA at the back of the room — in her engineer hoodie under a
stolen waiter's jacket, watching Damien across the crowd.*

SOPHIA
He just gave away the empire rather than fake-marry me. Do you
know what that's worth in self-esteem?

MAYA
Congratulations — you were almost a trophy wife.

SOPHIA
I WAS a trophy wife. For four minutes. It's the best career I've
ever had.

*A beat. Sophia follows Maya's gaze to Damien.*

SOPHIA (CONT'D)
You're not going over there.

MAYA
I'm the fraud on the ten-meter screen. He lost his empire in
front of everyone because of my contract. There's a version of
this where I'm the apology, not the—

SOPHIA
Maya. He gave up the company rather than sign a fake marriage —
and the fake marriage wasn't to the robot. It was to a stranger.
He could have had the letter of the clause and kept the world.
He wanted the real thing.

*Maya says nothing. Her eyes do something complicated.*

SOPHIA (CONT'D)
Go. Before someone sensible talks you out of it. And Maya —
when this works out, I want a job. Being a trophy was the most
honest work I've done in years.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 37,
  "scene_heading": "INT. BALLROOM — BAR — NIGHT",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "After-chaos at the back of the ballroom. Sophia — just released from the staged engagement — finds Maya hiding in an engineer hoodie under a stolen waiter's jacket, watching Damien across the crowd. Over trophy-wife banter, Sophia dismantles Maya's apology narrative: the fake marriage was to a stranger, not the robot; he wanted the real thing. Sends her to him — and asks for a job.",
  "zones": [
    "ballroom bar",
    "ballroom floor"
  ],
  "events": [
    {
      "event_id": "s37.e01",
      "source_evidence": [
        "*The after-chaos: everyone talking, nobody eating. SOPHIA finds\nMAYA at the back of the room — in her engineer hoodie under a\nstolen waiter's jacket, watching Damien across the crowd.*"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "locate the two women inside the noise — Maya hiding in a borrowed uniform, already watching him",
      "participants": [
        "SOPHIA",
        "MAYA",
        "DAMIEN",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "location": {
        "zones": [
          "ballroom bar",
          "ballroom floor"
        ],
        "primary": "ballroom bar"
      },
      "timeline": [
        {
          "beat": "the after-chaos — everyone talking, nobody eating",
          "type": "atmosphere"
        },
        {
          "beat": "Sophia finds Maya at the back — engineer hoodie under a stolen waiter's jacket",
          "type": "action"
        },
        {
          "beat": "Maya's gaze held on Damien across the crowd",
          "type": "held_action"
        }
      ],
      "visual_requirements": [
        "Maya reads as staff-adjacent and wrong — the stolen jacket over the hoodie is the costume joke and the hiding place",
        "Damien stays deep in the crowd — present only as the far end of her sightline"
      ],
      "audio_requirements": [
        "after-chaos walla — everyone talking, nobody eating"
      ],
      "continuity_constraints": [
        "Maya has been Maya-as-herself in public since scene 30 — the hiding is social, not secret"
      ],
      "ambiguities": [],
      "must_appear": [
        "SOPHIA",
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s37.sh01",
        "s37.sh02",
        "s37.snd01"
      ]
    },
    {
      "event_id": "s37.e02",
      "source_evidence": [
        "SOPHIA\nHe just gave away the empire rather than fake-marry me. Do you\nknow what that's worth in self-esteem?",
        "MAYA\nCongratulations — you were almost a trophy wife.",
        "SOPHIA\nI WAS a trophy wife. For four minutes. It's the best career I've\never had."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the banter establishes the friendship's grammar — Sophia's self-esteem read, Maya's deadpan, the four-minute career",
      "participants": [
        "SOPHIA",
        "MAYA"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "location": {
        "zone": "ballroom bar"
      },
      "timeline": [
        {
          "beat": "'He just gave away the empire rather than fake-marry me' — the self-esteem question",
          "type": "dialogue"
        },
        {
          "beat": "'Congratulations — you were almost a trophy wife.'",
          "type": "dialogue"
        },
        {
          "beat": "'I WAS a trophy wife. For four minutes.' — the best career she's ever had",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the volley plays in one two-shot — the comedy is the rhythm, not the coverage"
      ],
      "audio_requirements": [
        "close dry dialogue under the walla"
      ],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "SOPHIA",
        "MAYA"
      ],
      "tableau": true,
      "shot_sequence": [
        "s37.sh03",
        "s37.snd01"
      ]
    },
    {
      "event_id": "s37.e03",
      "source_evidence": [
        "*A beat. Sophia follows Maya's gaze to Damien.*",
        "SOPHIA (CONT'D)\nYou're not going over there."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the read — Sophia catches the gaze's object and names what Maya is not doing",
      "participants": [
        "SOPHIA",
        "MAYA",
        "DAMIEN"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "location": {
        "zones": [
          "ballroom bar",
          "ballroom floor"
        ],
        "primary": "ballroom bar"
      },
      "timeline": [
        {
          "beat": "a beat — Sophia follows Maya's gaze to Damien",
          "type": "reaction"
        },
        {
          "beat": "Damien across the crowd — the object of the gaze",
          "type": "insert"
        },
        {
          "beat": "'You're not going over there.' — observation, not question",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the gaze chain is traceable: Maya's eyeline → Sophia's eyeline → Damien alone in the crowd",
        "Damien's insert keeps him unaware — he is looked at, not looking back"
      ],
      "audio_requirements": [
        "walla continuing — the room does not know what it's watching"
      ],
      "continuity_constraints": [
        "same sightline established in e01 — Damien has not moved"
      ],
      "ambiguities": [],
      "must_appear": [
        "SOPHIA",
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s37.sh04",
        "s37.sh05",
        "s37.sh06"
      ]
    },
    {
      "event_id": "s37.e04",
      "source_evidence": [
        "MAYA\nI'm the fraud on the ten-meter screen. He lost his empire in\nfront of everyone because of my contract. There's a version of\nthis where I'm the apology, not the—"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "Maya's confession — she has cast herself as the apology, and the sentence cuts off before the alternative",
      "participants": [
        "MAYA",
        "SOPHIA"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "SOPHIA"
      ],
      "location": {
        "zone": "ballroom bar"
      },
      "timeline": [
        {
          "beat": "'I'm the fraud on the ten-meter screen' — ending on the interrupted 'not the—'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "held on Maya — the apology logic spoken while her eyes stay on him"
      ],
      "audio_requirements": [
        "close dry"
      ],
      "continuity_constraints": [
        "'the fraud on the ten-meter screen' — the gala projection from scenes 33-34 is the public record she means"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s37.sh07"
      ]
    },
    {
      "event_id": "s37.e05",
      "source_evidence": [
        "SOPHIA\nMaya. He gave up the company rather than sign a fake marriage —\nand the fake marriage wasn't to the robot. It was to a stranger.\nHe could have had the letter of the clause and kept the world.\nHe wanted the real thing."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the counter-argument — Sophia separates the robot from the stranger and lands 'He wanted the real thing.'",
      "participants": [
        "SOPHIA",
        "MAYA"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "MAYA"
      ],
      "location": {
        "zone": "ballroom bar"
      },
      "timeline": [
        {
          "beat": "the full argument — stranger not robot, letter vs world, 'He wanted the real thing.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "held on Sophia — she is the only person in the room who can make this argument from inside the almost-marriage"
      ],
      "audio_requirements": [
        "close dry"
      ],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "SOPHIA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s37.sh08"
      ]
    },
    {
      "event_id": "s37.e06",
      "source_evidence": [
        "*Maya says nothing. Her eyes do something complicated.*"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the argument lands — no line, just the math moving behind her eyes",
      "participants": [
        "MAYA",
        "SOPHIA"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "SOPHIA"
      ],
      "location": {
        "zone": "ballroom bar"
      },
      "timeline": [
        {
          "beat": "Maya says nothing",
          "type": "held_reaction"
        },
        {
          "beat": "her eyes do something complicated",
          "type": "reveal"
        }
      ],
      "visual_requirements": [
        "one held close frame — the 'complicated' is the shot's whole job; no cutaway to Damien"
      ],
      "audio_requirements": [
        "the walla drops to a hum under her silence"
      ],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s37.sh09"
      ]
    },
    {
      "event_id": "s37.e07",
      "source_evidence": [
        "SOPHIA (CONT'D)\nGo. Before someone sensible talks you out of it. And Maya —\nwhen this works out, I want a job. Being a trophy was the most\nhonest work I've done in years."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the send-off plus the job ask — Sophia pushes Maya toward Damien and invoices the friendship in the same breath",
      "participants": [
        "SOPHIA",
        "MAYA"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "location": {
        "zone": "ballroom bar"
      },
      "timeline": [
        {
          "beat": "'Go. Before someone sensible talks you out of it' — then the job ask, 'the most honest work I've done in years'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "two-shot — the send-off lands on both faces; Maya's exit happens in scene 38's doorway, not here"
      ],
      "audio_requirements": [
        "close dry, the send-off"
      ],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "SOPHIA",
        "MAYA"
      ],
      "tableau": true,
      "shot_sequence": [
        "s37.sh10"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s37.sh01",
      "size": "W",
      "zone": "ballroom bar",
      "type": "visual",
      "participants": [
        "SOPHIA",
        "MAYA",
        "GUESTS"
      ],
      "implements": [
        "s37.e01"
      ],
      "covers_beats": {
        "s37.e01": [
          0,
          1
        ]
      },
      "purpose": "the after-chaos — everyone talking, nobody eating — Sophia finds Maya at the back in the stolen jacket",
      "audio_note": "after-chaos walla, everyone talking, nobody eating"
    },
    {
      "shot_id": "s37.sh02",
      "size": "M",
      "zone": "ballroom bar",
      "type": "visual",
      "participants": [
        "MAYA",
        "DAMIEN"
      ],
      "implements": [
        "s37.e01"
      ],
      "covers_beats": {
        "s37.e01": [
          2
        ]
      },
      "purpose": "her gaze held on Damien — he stays deep in the crowd, unaware",
      "audio_note": "walla"
    },
    {
      "shot_id": "s37.sh03",
      "size": "M two-shot",
      "zone": "ballroom bar",
      "type": "visual",
      "participants": [
        "SOPHIA",
        "MAYA"
      ],
      "implements": [
        "s37.e02"
      ],
      "covers_beats": {
        "s37.e02": [
          0,
          1,
          2
        ]
      },
      "purpose": "the trophy-wife volley — empire vs self-esteem, 'almost', 'I WAS', four minutes, best career",
      "audio_note": "close dry dialogue; walla under",
      "dialogue_lines": [
        {
          "event_id": "s37.e02",
          "speaker": "SOPHIA",
          "line": "He just gave away the empire rather than fake-marry me. Do you know what that's worth in self-esteem?",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s37.e02",
          "speaker": "MAYA",
          "line": "Congratulations — you were almost a trophy wife.",
          "line_kind": "on_camera",
          "recipient": "SOPHIA",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s37.e02",
          "speaker": "SOPHIA",
          "line": "I WAS a trophy wife. For four minutes. It's the best career I've ever had.",
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
      "shot_id": "s37.sh04",
      "size": "M",
      "zone": "ballroom bar",
      "type": "visual",
      "participants": [
        "SOPHIA",
        "MAYA"
      ],
      "implements": [
        "s37.e03"
      ],
      "covers_beats": {
        "s37.e03": [
          0
        ]
      },
      "purpose": "a beat — Sophia follows Maya's gaze to its object",
      "audio_note": "walla continuing"
    },
    {
      "shot_id": "s37.sh05",
      "size": "M/INS",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s37.e03"
      ],
      "covers_beats": {
        "s37.e03": [
          1
        ]
      },
      "purpose": "Damien alone across the crowd — the object of the gaze, looking at no one",
      "audio_note": "walla continuing"
    },
    {
      "shot_id": "s37.sh06",
      "size": "M",
      "zone": "ballroom bar",
      "type": "visual",
      "participants": [
        "SOPHIA"
      ],
      "implements": [
        "s37.e03"
      ],
      "covers_beats": {
        "s37.e03": [
          2
        ]
      },
      "purpose": "'You're not going over there.' — observation, not question",
      "audio_note": "close dry; walla under",
      "dialogue_lines": [
        {
          "event_id": "s37.e03",
          "speaker": "SOPHIA",
          "line": "You're not going over there.",
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
      "shot_id": "s37.sh07",
      "size": "M/CU",
      "zone": "ballroom bar",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s37.e04"
      ],
      "covers_beats": {
        "s37.e04": [
          0
        ]
      },
      "purpose": "'I'm the fraud on the ten-meter screen' — the apology logic, cut off at 'not the—'",
      "audio_note": "close, dry",
      "dialogue_lines": [
        {
          "event_id": "s37.e04",
          "speaker": "MAYA",
          "line": "I'm the fraud on the ten-meter screen. He lost his empire in front of everyone because of my contract. There's a version of this where I'm the apology, not the—",
          "line_kind": "on_camera",
          "recipient": "SOPHIA",
          "recipient_presence": "offscreen",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s37.sh08",
      "size": "M",
      "zone": "ballroom bar",
      "type": "visual",
      "participants": [
        "SOPHIA"
      ],
      "implements": [
        "s37.e05"
      ],
      "covers_beats": {
        "s37.e05": [
          0
        ]
      },
      "purpose": "the counter-argument — stranger not robot, letter vs world — 'He wanted the real thing.'",
      "audio_note": "close, dry",
      "dialogue_lines": [
        {
          "event_id": "s37.e05",
          "speaker": "SOPHIA",
          "line": "Maya. He gave up the company rather than sign a fake marriage — and the fake marriage wasn't to the robot. It was to a stranger. He could have had the letter of the clause and kept the world. He wanted the real thing.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "offscreen",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s37.sh09",
      "size": "CU",
      "zone": "ballroom bar",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s37.e06"
      ],
      "covers_beats": {
        "s37.e06": [
          0,
          1
        ]
      },
      "purpose": "Maya says nothing — her eyes do something complicated",
      "audio_note": "the walla drops to a hum under her silence"
    },
    {
      "shot_id": "s37.sh10",
      "size": "M two-shot",
      "zone": "ballroom bar",
      "type": "visual",
      "participants": [
        "SOPHIA",
        "MAYA"
      ],
      "implements": [
        "s37.e07"
      ],
      "covers_beats": {
        "s37.e07": [
          0
        ]
      },
      "purpose": "'Go.' — the send-off, and the job ask that makes it a friendship",
      "audio_note": "close dry, the send-off",
      "dialogue_lines": [
        {
          "event_id": "s37.e07",
          "speaker": "SOPHIA",
          "line": "Go. Before someone sensible talks you out of it. And Maya — when this works out, I want a job. Being a trophy was the most honest work I've done in years.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s37.snd01",
      "type": "sound",
      "implements": [
        "s37.e01",
        "s37.e02"
      ],
      "purpose": "sound-states card for the bar — the after-chaos walla the two women talk underneath",
      "audio_note": "after-chaos walla — everyone talking, nobody eating; glasses and untouched cutlery; close dry dialogue above it; no score",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "*The after-chaos: everyone talking, nobody eating. SOPHIA finds\nMAYA at the back of the room — in her engineer hoodie under a\nstolen waiter's jacket, watching Damien across the crowd.*",
      "disposition": "covered_by",
      "by": [
        "s37.e01"
      ]
    },
    {
      "span": "SOPHIA\nHe just gave away the empire rather than fake-marry me. Do you\nknow what that's worth in self-esteem?",
      "disposition": "covered_by",
      "by": [
        "s37.e02"
      ]
    },
    {
      "span": "MAYA\nCongratulations — you were almost a trophy wife.",
      "disposition": "covered_by",
      "by": [
        "s37.e02"
      ]
    },
    {
      "span": "SOPHIA\nI WAS a trophy wife. For four minutes. It's the best career I've\never had.",
      "disposition": "covered_by",
      "by": [
        "s37.e02"
      ]
    },
    {
      "span": "*A beat. Sophia follows Maya's gaze to Damien.*",
      "disposition": "covered_by",
      "by": [
        "s37.e03"
      ]
    },
    {
      "span": "SOPHIA (CONT'D)\nYou're not going over there.",
      "disposition": "covered_by",
      "by": [
        "s37.e03"
      ]
    },
    {
      "span": "MAYA\nI'm the fraud on the ten-meter screen. He lost his empire in\nfront of everyone because of my contract. There's a version of\nthis where I'm the apology, not the—",
      "disposition": "covered_by",
      "by": [
        "s37.e04"
      ]
    },
    {
      "span": "SOPHIA\nMaya. He gave up the company rather than sign a fake marriage —\nand the fake marriage wasn't to the robot. It was to a stranger.\nHe could have had the letter of the clause and kept the world.\nHe wanted the real thing.",
      "disposition": "covered_by",
      "by": [
        "s37.e05"
      ]
    },
    {
      "span": "*Maya says nothing. Her eyes do something complicated.*",
      "disposition": "covered_by",
      "by": [
        "s37.e06"
      ]
    },
    {
      "span": "SOPHIA (CONT'D)\nGo. Before someone sensible talks you out of it. And Maya —\nwhen this works out, I want a job. Being a trophy was the most\nhonest work I've done in years.",
      "disposition": "covered_by",
      "by": [
        "s37.e07"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['SOPHIA', 'MAYA'] | -  | The after-chaos: everyone talking, nobody eating. SOPHIA finds MAYA at the back 
i02 blk=['SOPHIA', 'MAYA'] | SOPHIA He just gave away the empire rather than fake-marry me. Do y | SOPHIA faces MAYA and speaks.
i03 blk=['MAYA'] | MAYA Congratulations — you were almost a trophy wife. | MAYA faces SOPHIA and speaks.
i04 blk=['SOPHIA'] | SOPHIA I WAS a trophy wife. For four minutes. It's the best career  | SOPHIA faces MAYA and speaks. A beat. Sophia follows Maya's gaze to Damien.
i05 blk=['MAYA'] | MAYA I'm the fraud on the ten-meter screen. He lost his empire in | MAYA faces SOPHIA and speaks.
i06 blk=['MAYA', 'SOPHIA'] | SOPHIA Maya. He gave up the company rather than sign a fake marriag | SOPHIA faces MAYA and speaks.
i07 blk=['SOPHIA'] | SOPHIA Go. Before someone sensible talks you out of it. And Maya —  | Maya says nothing. Her eyes do something complicated.