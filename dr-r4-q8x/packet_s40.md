# VALIDATION PACKET — scene s40
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 40 — INT. CROSS TOWER — BOARDROOM — DAY

*The trustee review — six months later in spirit if not on
screen. PENHALIGON presides; DAMIEN sits at the foot of the
table — not the head, a choice that shocks the room.*

PENHALIGON
The six-month review concludes: the demonstration has been
maintained. Control vests unconditionally. Also — and this is
a personal note from the trustees — please stop reorganizing
the board meetings around your girlfriend's lab schedule.
It's sweet and it's irregular.

DAMIEN
Partner's lab schedule. And it's efficient — her commute is
fourteen minutes.

PENHALIGON
You see? Even now you optimize.

DAMIEN
I've learned to optimize smaller.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 40,
  "scene_heading": "INT. CROSS TOWER — BOARDROOM — DAY",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "The clause pays out — quietly. Six months on, the trustee review formally vests control, but the scene is really about the seating chart: Damien at the foot of his own table, and a board that now schedules around a partner's lab hours. The empire survived; the emperor's job description changed. 'I've learned to optimize smaller' is the thesis line of the whole third act.",
  "zones": [
    "cross tower boardroom"
  ],
  "events": [
    {
      "event_id": "s40.e01",
      "source_evidence": [
        "The trustee review — six months later in spirit if not on screen. PENHALIGON presides; DAMIEN sits at the foot of the table — not the head, a choice that shocks the room."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the seating chart is the verdict — before a word is read, the foot-of-table choice tells the room (and us) that control has already changed hands inwardly",
      "participants": [
        "PENHALIGON",
        "DAMIEN",
        "TRUSTEES"
      ],
      "remote_participants": [],
      "location": {
        "zone": "cross tower boardroom"
      },
      "timeline": [
        {
          "beat": "the trustee review convenes — six months later in spirit if not on screen",
          "type": "atmosphere"
        },
        {
          "beat": "Damien sits at the foot of the table, not the head — a choice that shocks the room",
          "type": "reveal"
        }
      ],
      "visual_requirements": [
        "the seat geography must read instantly — head empty, Damien at the foot by choice",
        "the trustees' shock is on their faces, not in dialogue — no one comments on it aloud"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "six months post-gala — this is the formal payout of the demonstration clause, not a new threat"
      ],
      "ambiguities": [],
      "must_appear": [
        "PENHALIGON",
        "DAMIEN",
        "TRUSTEES"
      ],
      "tableau": true,
      "shot_sequence": [
        "s40.sh01"
      ]
    },
    {
      "event_id": "s40.e02",
      "source_evidence": [
        "The six-month review concludes: the demonstration has been maintained. Control vests unconditionally.",
        "Also — and this is a personal note from the trustees — please stop reorganizing the board meetings around your girlfriend's lab schedule. It's sweet and it's irregular."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the ruling plus the rebuke — control vests unconditionally AND the board officially complains that he schedules around her lab hours; institutional language delivering a love letter",
      "participants": [
        "PENHALIGON",
        "DAMIEN",
        "TRUSTEES"
      ],
      "offscreen_present": [
        "TRUSTEES"
      ],
      "remote_participants": [],
      "location": {
        "zone": "cross tower boardroom"
      },
      "timeline": [
        {
          "beat": "the ruling — the demonstration maintained, control vests unconditionally",
          "type": "dialogue"
        },
        {
          "beat": "the personal note — 'please stop reorganizing the board meetings around your girlfriend's lab schedule'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Penhaligon delivers both clauses in the same register — the tenderness hides inside the legalese"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "'the demonstration has been maintained' — proof-language settled; nothing remains contested",
        "'girlfriend' is the trustees' word — Damien corrects it to 'partner' in e03"
      ],
      "ambiguities": [],
      "must_appear": [
        "PENHALIGON",
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s40.sh02"
      ]
    },
    {
      "event_id": "s40.e03",
      "source_evidence": [
        "Partner's lab schedule. And it's efficient — her commute is fourteen minutes.",
        "You see? Even now you optimize.",
        "I've learned to optimize smaller."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the correction and the thesis — 'girlfriend' becomes 'partner', the commute math betrays the old optimizer, and 'optimize smaller' lands the film's final definition of growth",
      "participants": [
        "PENHALIGON",
        "DAMIEN",
        "TRUSTEES"
      ],
      "offscreen_present": [
        "TRUSTEES"
      ],
      "remote_participants": [],
      "location": {
        "zone": "cross tower boardroom"
      },
      "timeline": [
        {
          "beat": "'Partner's lab schedule.' — plus the fourteen-minute commute defense",
          "type": "dialogue"
        },
        {
          "beat": "'You see? Even now you optimize.'",
          "type": "dialogue"
        },
        {
          "beat": "'I've learned to optimize smaller.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the exchange is dry on both sides — two men fluent in ledger, using it to say something warm"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "fourteen-minute commute implies the penthouse-to-lab geography — the same distance the film has been measuring since S23"
      ],
      "ambiguities": [],
      "must_appear": [
        "PENHALIGON",
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s40.sh03",
        "s40.sh04",
        "s40.sh05"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s40.sh01",
      "size": "W tableau",
      "zone": "cross tower boardroom",
      "type": "visual",
      "participants": [
        "PENHALIGON",
        "DAMIEN",
        "TRUSTEES"
      ],
      "implements": [
        "s40.e01"
      ],
      "covers_beats": {
        "s40.e01": [
          0,
          1
        ]
      },
      "purpose": "the review convened — Penhaligon presiding, Damien at the foot of the table, the room quietly shocked",
      "audio_note": "boardroom hush — papers, leather, HVAC"
    },
    {
      "shot_id": "s40.sh02",
      "size": "two-shot",
      "zone": "cross tower boardroom",
      "type": "visual",
      "participants": [
        "PENHALIGON",
        "DAMIEN"
      ],
      "implements": [
        "s40.e02"
      ],
      "covers_beats": {
        "s40.e02": [
          0,
          1
        ]
      },
      "purpose": "the ruling read in legalese, then the personal note — 'it's sweet and it's irregular'",
      "dialogue_lines": [
        {
          "event_id": "s40.e02",
          "speaker": "PENHALIGON",
          "line": "The six-month review concludes: the demonstration has been maintained. Control vests unconditionally.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s40.e02",
          "speaker": "PENHALIGON",
          "line": "Also — and this is a personal note from the trustees — please stop reorganizing the board meetings around your girlfriend's lab schedule. It's sweet and it's irregular.",
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
      "shot_id": "s40.sh03",
      "size": "M",
      "zone": "cross tower boardroom",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s40.e03"
      ],
      "covers_beats": {
        "s40.e03": [
          0
        ]
      },
      "purpose": "the correction — 'partner's lab schedule' — and the commute math he cannot help producing",
      "dialogue_lines": [
        {
          "event_id": "s40.e03",
          "speaker": "DAMIEN",
          "line": "Partner's lab schedule. And it's efficient — her commute is fourteen minutes.",
          "line_kind": "on_camera",
          "recipient": "PENHALIGON",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s40.sh04",
      "size": "M",
      "zone": "cross tower boardroom",
      "type": "visual",
      "participants": [
        "PENHALIGON"
      ],
      "implements": [
        "s40.e03"
      ],
      "covers_beats": {
        "s40.e03": [
          1
        ]
      },
      "purpose": "'You see? Even now you optimize.' — the trustee calls the tell",
      "dialogue_lines": [
        {
          "event_id": "s40.e03",
          "speaker": "PENHALIGON",
          "line": "You see? Even now you optimize.",
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
      "shot_id": "s40.sh05",
      "size": "CU",
      "zone": "cross tower boardroom",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s40.e03"
      ],
      "covers_beats": {
        "s40.e03": [
          2
        ]
      },
      "purpose": "'I've learned to optimize smaller.' — the act's thesis, held",
      "dialogue_lines": [
        {
          "event_id": "s40.e03",
          "speaker": "DAMIEN",
          "line": "I've learned to optimize smaller.",
          "line_kind": "on_camera",
          "recipient": "PENHALIGON",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        }
      ]
    }
  ],
  "coverage": [
    {
      "span": "The trustee review — six months later in spirit if not on screen. PENHALIGON presides; DAMIEN sits at the foot of the table — not the head, a choice that shocks the room.",
      "disposition": "covered_by",
      "by": [
        "s40.e01"
      ]
    },
    {
      "span": "The six-month review concludes: the demonstration has been maintained. Control vests unconditionally.",
      "disposition": "covered_by",
      "by": [
        "s40.e02"
      ]
    },
    {
      "span": "Partner's lab schedule. And it's efficient — her commute is fourteen minutes.",
      "disposition": "covered_by",
      "by": [
        "s40.e03"
      ]
    },
    {
      "span": "You see? Even now you optimize.",
      "disposition": "covered_by",
      "by": [
        "s40.e03"
      ]
    },
    {
      "span": "I've learned to optimize smaller.",
      "disposition": "covered_by",
      "by": [
        "s40.e03"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['PENHALIGON', 'DAMIEN'] | -  | The trustee review — six months later in spirit if not on screen. PENHALIGON pre
i02 blk=['PENHALIGON', 'DAMIEN'] | PENHALIGON The six-month review concludes: the demonstration has been m | PENHALIGON faces DAMIEN and speaks.
i03 blk=['DAMIEN'] | DAMIEN Partner's lab schedule. And it's efficient — her commute is  | DAMIEN faces PENHALIGON and speaks.
i04 blk=['PENHALIGON'] | PENHALIGON You see? Even now you optimize. | PENHALIGON faces DAMIEN and speaks.
i05 blk=['PENHALIGON', 'DAMIEN'] | DAMIEN I've learned to optimize smaller. | DAMIEN faces PENHALIGON and speaks.