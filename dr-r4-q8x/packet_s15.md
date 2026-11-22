# VALIDATION PACKET — scene s15
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 15 — INT. PRIVATE DINING CLUB — NIGHT (DATE TWO)

*OCTAVIA MARLOWE — cheekbones like case law. She and DAMIEN regard
each other across the table like two firms contemplating a merger.*

OCTAVIA
Your pre-date dossier says you read seven languages. The trust
clause says you need this done in six weeks. Propose terms.

DAMIEN
(blinking)
You're direct.

OCTAVIA
I'm expensive. Time is the fee.

*At the lab, MAYA leans into the mic:*

MAYA (V.O.)
Abort. Abort now. She's you with better cheekbones. You'd merge,
not marry — and she'd own the combined entity by Tuesday.

DAMIEN
(coughs into napkin)
Octavia — if this were a merger, who keeps the chair?

OCTAVIA
(without blinking)
Whichever of us loves less. That's always the chair, Damien.
That's why it would be you.

*Silence. Damien studies her — respect, recognition, and something
like sadness for them both.*

DAMIEN
You're not interested in me at all, are you.

OCTAVIA
I'm interested in not being a subsidiary. Your brother offered my
board a seat to sit at this table. I'd rather own a chair than
decorate one. No offense.

DAMIEN
(genuine, first time)
None taken.

MAYA (V.O., quietly)
She just did more for you than any of us. Say thank you and let
her keep the chair.

DAMIEN
Thank you, Octavia. Keep the chair.

*Octavia raises her wine glass an eighth of an inch. From her,
it's practically an embrace.*

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 15,
  "scene_heading": "INT. PRIVATE DINING CLUB — NIGHT (DATE TWO)",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "Date two. Octavia Marlowe opens with 'Propose terms' and conducts the dinner like a hostile merger — which is exactly what it is. Maya calls the abort from the lab, but Octavia's verdict ('whichever of us loves less') is the first time a candidate tells Damien the truth about himself and Victor in the same breath. She self-eliminates by refusing to be a subsidiary; Damien's first genuine 'none taken' of the film is the beginning of his honesty. Maya, quietly, recognizes it too.",
  "zones": [
    "private dining club",
    "volt lab"
  ],
  "events": [
    {
      "event_id": "s15.e01",
      "source_evidence": [
        "OCTAVIA MARLOWE — cheekbones like case law. She and DAMIEN regard",
        "each other across the table like two firms contemplating a merger.",
        "Your pre-date dossier says you read seven languages. The trust",
        "clause says you need this done in six weeks. Propose terms.",
        "You're direct.",
        "I'm expensive. Time is the fee."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the negotiation framed — she already knows the clause, the deadline, and his dossier; the date is a term sheet",
      "participants": [
        "OCTAVIA",
        "DAMIEN"
      ],
      "remote_participants": [],
      "location": {
        "zone": "private dining club"
      },
      "timeline": [
        {
          "beat": "cheekbones like case law — two firms contemplating a merger across the table",
          "type": "atmosphere"
        },
        {
          "beat": "'Your pre-date dossier says you read seven languages... Propose terms.'",
          "type": "dialogue"
        },
        {
          "beat": "'You're direct.' — blinking",
          "type": "dialogue"
        },
        {
          "beat": "'I'm expensive. Time is the fee.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the regard must play as mutual valuation — two entities pricing each other, not two people flirting"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "she cites the trust clause and six weeks — she has done the diligence; nothing about this dinner is a surprise to her"
      ],
      "ambiguities": [],
      "must_appear": [
        "OCTAVIA",
        "DAMIEN"
      ],
      "tableau": true,
      "shot_sequence": [
        "s15.sh01"
      ]
    },
    {
      "event_id": "s15.e02",
      "source_evidence": [
        "At the lab, MAYA leans into the mic:",
        "Abort. Abort now. She's you with better cheekbones. You'd merge,",
        "not marry — and she'd own the combined entity by Tuesday."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the abort call — Maya reads Octavia instantly and correctly: this is Damien with better cheekbones, a merger not a marriage",
      "participants": [
        "MAYA"
      ],
      "remote_participants": [
        {
          "actor": "DAMIEN",
          "channel": "earpiece feed",
          "direction": "out"
        }
      ],
      "location": {
        "zone": "volt lab"
      },
      "timeline": [
        {
          "beat": "Maya leans into the mic at the lab",
          "type": "action"
        },
        {
          "beat": "the abort warning — 'She's you with better cheekbones. You'd merge, not marry.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the lean into the mic is urgency, not routine — the first time she calls an abort"
      ],
      "audio_requirements": [
        "the live feed in his earpiece — her voice close and urgent"
      ],
      "continuity_constraints": [
        "the warning lands at the table as remote audio — registered there or here exactly once; the physical origin is this lab shot"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s15.sh02",
        "s15.snd01"
      ],
      "decisions": [
        {
          "topic": "abort line — V.O. vs lab coverage",
          "status": "resolved-decision",
          "decision": "parallel edit: Maya shown physically at the lab leaning into the mic; her voice reaches Damien as earpiece V.O. at the table",
          "basis": "screenplay_text",
          "consequence": "sh covering the lab lean-in keeps MAYA physical; the restaurant-side recipient stays remote-declared earpiece — do not play the line as disembodied narration over the table only",
          "resolved_from": "screenplay marks the abort line (V.O.) yet cuts to the lab for the lean-in"
        }
      ]
    },
    {
      "event_id": "s15.e03",
      "source_evidence": [
        "(coughs into napkin)",
        "Octavia — if this were a merger, who keeps the chair?"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the abort lands — the napkin cough covers the wire, and he tests her frame instead of aborting",
      "participants": [
        "DAMIEN",
        "OCTAVIA"
      ],
      "remote_participants": [],
      "location": {
        "zone": "private dining club"
      },
      "timeline": [
        {
          "beat": "the warning lands in his ear — he coughs into the napkin",
          "type": "reaction"
        },
        {
          "beat": "'Octavia — if this were a merger, who keeps the chair?'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the cough-into-napkin is the tell of a man receiving a line — half a beat of cover, no more"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "he ignores the abort — asking the merger question instead is him choosing curiosity over the wire"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "OCTAVIA"
      ],
      "tableau": true,
      "shot_sequence": [
        "s15.sh03"
      ]
    },
    {
      "event_id": "s15.e04",
      "source_evidence": [
        "Whichever of us loves less. That's always the chair, Damien.",
        "That's why it would be you.",
        "Silence. Damien studies her — respect, recognition, and something",
        "like sadness for them both."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the verdict — she names the game and his seat in it; the silence after is respect, recognition, and shared sadness",
      "participants": [
        "OCTAVIA",
        "DAMIEN"
      ],
      "remote_participants": [],
      "location": {
        "zone": "private dining club"
      },
      "timeline": [
        {
          "beat": "'Whichever of us loves less. That's always the chair, Damien. That's why it would be you.' — without blinking",
          "type": "dialogue"
        },
        {
          "beat": "silence — he studies her: respect, recognition, something like sadness for them both",
          "type": "held_reaction"
        }
      ],
      "visual_requirements": [
        "without blinking — the verdict arrives pre-calculated, the way everything about her arrives",
        "the study-silence is shared, not one-sided — sadness for them both must be legible on him"
      ],
      "audio_requirements": [],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "OCTAVIA",
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s15.sh04",
        "s15.sh05"
      ]
    },
    {
      "event_id": "s15.e05",
      "source_evidence": [
        "You're not interested in me at all, are you.",
        "I'm interested in not being a subsidiary. Your brother offered my",
        "board a seat to sit at this table. I'd rather own a chair than",
        "decorate one. No offense.",
        "(genuine, first time)",
        "None taken."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the real terms — she exposes Victor's board-seat offer and declines the whole structure; his first genuine beat of the film is 'None taken.'",
      "participants": [
        "DAMIEN",
        "OCTAVIA"
      ],
      "remote_participants": [],
      "location": {
        "zone": "private dining club"
      },
      "timeline": [
        {
          "beat": "'You're not interested in me at all, are you.' — statement, not question",
          "type": "dialogue"
        },
        {
          "beat": "'I'm interested in not being a subsidiary. Your brother offered my board a seat to sit at this table. I'd rather own a chair than decorate one. No offense.'",
          "type": "dialogue"
        },
        {
          "beat": "'None taken.' — genuine, first time",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "'none taken' must land differently from every line he's said all film — no rehearsed register available for genuine"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the board-seat offer is Victor's fingerprints — the same payroll logic Maya exposed on the yacht in S14"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "OCTAVIA"
      ],
      "tableau": true,
      "shot_sequence": [
        "s15.sh06"
      ]
    },
    {
      "event_id": "s15.e06",
      "source_evidence": [
        "She just did more for you than any of us. Say thank you and let",
        "her keep the chair.",
        "Thank you, Octavia. Keep the chair.",
        "Octavia raises her wine glass an eighth of an inch. From her,",
        "it's practically an embrace."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the release — Maya concedes the point on the wire, he says thank you in his own voice, and an eighth of an inch of wine glass is the closest thing to an embrace Octavia offers",
      "participants": [
        "DAMIEN",
        "OCTAVIA"
      ],
      "remote_participants": [
        {
          "actor": "MAYA",
          "channel": "earpiece",
          "direction": "out"
        }
      ],
      "location": {
        "zone": "private dining club"
      },
      "timeline": [
        {
          "beat": "Maya quietly on the wire — 'She just did more for you than any of us. Say thank you and let her keep the chair.'",
          "type": "dialogue_remote"
        },
        {
          "beat": "'Thank you, Octavia. Keep the chair.'",
          "type": "dialogue"
        },
        {
          "beat": "the wine glass raised an eighth of an inch — from her, practically an embrace",
          "type": "held_action"
        }
      ],
      "visual_requirements": [
        "the eighth of an inch must be measured — the smallest possible gesture played as a large one"
      ],
      "audio_requirements": [
        "Maya's voice quieter now on the earpiece — nearly private to the audience"
      ],
      "continuity_constraints": [
        "'thank you' is scripted by Maya but lands as his — the first wire line he would have said anyway"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "OCTAVIA"
      ],
      "tableau": true,
      "shot_sequence": [
        "s15.sh07",
        "s15.snd01"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s15.sh01",
      "size": "two-shot",
      "zone": "private dining club",
      "type": "visual",
      "participants": [
        "OCTAVIA",
        "DAMIEN"
      ],
      "implements": [
        "s15.e01"
      ],
      "covers_beats": {
        "s15.e01": [
          0,
          1,
          2,
          3
        ]
      },
      "purpose": "two firms contemplating a merger — 'Propose terms.' / 'You're direct.' / 'I'm expensive. Time is the fee.'",
      "audio_note": "dining club hush, crystal and low murmur",
      "dialogue_lines": [
        {
          "event_id": "s15.e01",
          "speaker": "OCTAVIA",
          "line": "Your pre-date dossier says you read seven languages. The trust clause says you need this done in six weeks. Propose terms.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s15.e01",
          "speaker": "DAMIEN",
          "line": "You're direct.",
          "line_kind": "on_camera",
          "recipient": "OCTAVIA",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s15.e01",
          "speaker": "OCTAVIA",
          "line": "I'm expensive. Time is the fee.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        }
      ]
    },
    {
      "shot_id": "s15.sh02",
      "size": "M",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s15.e02"
      ],
      "covers_beats": {
        "s15.e02": [
          0,
          1
        ]
      },
      "purpose": "the abort call — she leans into the mic at the lab and names the merger before it happens",
      "audio_note": "mic click, live feed, lab rig hum",
      "dialogue_lines": [
        {
          "event_id": "s15.e02",
          "speaker": "MAYA",
          "line": "Abort. Abort now. She's you with better cheekbones. You'd merge, not marry — and she'd own the combined entity by Tuesday.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "remote",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s15.sh03",
      "size": "two-shot",
      "zone": "private dining club",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "OCTAVIA"
      ],
      "implements": [
        "s15.e03"
      ],
      "covers_beats": {
        "s15.e03": [
          0,
          1
        ]
      },
      "purpose": "the abort lands — cough into the napkin, then the merger-chair question she has already answered in her head",
      "audio_note": "napkin, suppressed cough, club hush",
      "dialogue_lines": [
        {
          "event_id": "s15.e03",
          "speaker": "DAMIEN",
          "line": "Octavia — if this were a merger, who keeps the chair?",
          "line_kind": "on_camera",
          "recipient": "OCTAVIA",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s15.sh04",
      "size": "CU",
      "zone": "private dining club",
      "type": "visual",
      "participants": [
        "OCTAVIA"
      ],
      "implements": [
        "s15.e04"
      ],
      "covers_beats": {
        "s15.e04": [
          0
        ]
      },
      "purpose": "the verdict without blinking — 'whichever of us loves less... that's why it would be you'",
      "dialogue_lines": [
        {
          "event_id": "s15.e04",
          "speaker": "OCTAVIA",
          "line": "Whichever of us loves less. That's always the chair, Damien. That's why it would be you.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "offscreen",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s15.sh05",
      "size": "CU held",
      "zone": "private dining club",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s15.e04"
      ],
      "covers_beats": {
        "s15.e04": [
          1
        ]
      },
      "purpose": "the study — silence, respect, recognition, something like sadness for them both",
      "audio_note": "held silence, club room tone"
    },
    {
      "shot_id": "s15.sh06",
      "size": "two-shot",
      "zone": "private dining club",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "OCTAVIA"
      ],
      "implements": [
        "s15.e05"
      ],
      "covers_beats": {
        "s15.e05": [
          0,
          1,
          2
        ]
      },
      "purpose": "the real terms — the subsidiary refusal, the board-seat exposure, and 'None taken.' landing genuine",
      "dialogue_lines": [
        {
          "event_id": "s15.e05",
          "speaker": "DAMIEN",
          "line": "You're not interested in me at all, are you.",
          "line_kind": "on_camera",
          "recipient": "OCTAVIA",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s15.e05",
          "speaker": "OCTAVIA",
          "line": "I'm interested in not being a subsidiary. Your brother offered my board a seat to sit at this table. I'd rather own a chair than decorate one. No offense.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s15.e05",
          "speaker": "DAMIEN",
          "line": "None taken.",
          "line_kind": "on_camera",
          "recipient": "OCTAVIA",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s15.sh07",
      "size": "two-shot→INS",
      "zone": "private dining club",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "OCTAVIA"
      ],
      "implements": [
        "s15.e06"
      ],
      "covers_beats": {
        "s15.e06": [
          0,
          1,
          2
        ]
      },
      "purpose": "the quiet wire instruction → 'Thank you, Octavia. Keep the chair.' → the eighth-of-an-inch glass raise as insert",
      "audio_note": "earpiece quiet, the small glass raise",
      "dialogue_lines": [
        {
          "event_id": "s15.e06",
          "speaker": "MAYA",
          "line": "She just did more for you than any of us. Say thank you and let her keep the chair.",
          "line_kind": "earpiece",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s15.e06",
          "speaker": "DAMIEN",
          "line": "Thank you, Octavia. Keep the chair.",
          "line_kind": "on_camera",
          "recipient": "OCTAVIA",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s15.snd01",
      "type": "sound",
      "implements": [
        "s15.e02",
        "s15.e06"
      ],
      "purpose": "sound card: the earpiece feed — urgent on the abort call, quieter on the release; dining club hush underneath; no score",
      "audio_note": "earpiece feed with her voice close and urgent then quieter, dining club hush",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "OCTAVIA MARLOWE — cheekbones like case law.",
      "disposition": "covered_by",
      "by": [
        "s15.e01"
      ]
    },
    {
      "span": "two firms contemplating a merger.",
      "disposition": "covered_by",
      "by": [
        "s15.e01"
      ]
    },
    {
      "span": "The trust clause says you need this done in six weeks. Propose terms.",
      "disposition": "covered_by",
      "by": [
        "s15.e01"
      ]
    },
    {
      "span": "You're direct.",
      "disposition": "covered_by",
      "by": [
        "s15.e01"
      ]
    },
    {
      "span": "I'm expensive. Time is the fee.",
      "disposition": "covered_by",
      "by": [
        "s15.e01"
      ]
    },
    {
      "span": "At the lab, MAYA leans into the mic:",
      "disposition": "covered_by",
      "by": [
        "s15.e02"
      ]
    },
    {
      "span": "Abort. Abort now. She's you with better cheekbones.",
      "disposition": "covered_by",
      "by": [
        "s15.e02"
      ]
    },
    {
      "span": "she'd own the combined entity by Tuesday.",
      "disposition": "covered_by",
      "by": [
        "s15.e02"
      ]
    },
    {
      "span": "Octavia — if this were a merger, who keeps the chair?",
      "disposition": "covered_by",
      "by": [
        "s15.e03"
      ]
    },
    {
      "span": "Whichever of us loves less. That's always the chair, Damien. That's why it would be you.",
      "disposition": "covered_by",
      "by": [
        "s15.e04"
      ]
    },
    {
      "span": "Silence. Damien studies her — respect, recognition, and something like sadness for them both.",
      "disposition": "covered_by",
      "by": [
        "s15.e04"
      ]
    },
    {
      "span": "You're not interested in me at all, are you.",
      "disposition": "covered_by",
      "by": [
        "s15.e05"
      ]
    },
    {
      "span": "I'm interested in not being a subsidiary. Your brother offered my board a seat to sit at this table.",
      "disposition": "covered_by",
      "by": [
        "s15.e05"
      ]
    },
    {
      "span": "None taken.",
      "disposition": "covered_by",
      "by": [
        "s15.e05"
      ]
    },
    {
      "span": "She just did more for you than any of us. Say thank you and let her keep the chair.",
      "disposition": "covered_by",
      "by": [
        "s15.e06"
      ]
    },
    {
      "span": "Thank you, Octavia. Keep the chair.",
      "disposition": "covered_by",
      "by": [
        "s15.e06"
      ]
    },
    {
      "span": "Octavia raises her wine glass an eighth of an inch. From her, it's practically an embrace.",
      "disposition": "covered_by",
      "by": [
        "s15.e06"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['OCTAVIA', 'DAMIEN'] | -  | OCTAVIA MARLOWE — cheekbones like case law. She and DAMIEN regard each other acr
i02 blk=['OCTAVIA', 'DAMIEN'] | OCTAVIA Your pre-date dossier says you read seven languages. The tru | OCTAVIA faces DAMIEN and speaks.
i03 blk=['DAMIEN'] | DAMIEN You're direct. | DAMIEN faces OCTAVIA and speaks.
i04 blk=['OCTAVIA'] | OCTAVIA I'm expensive. Time is the fee. | OCTAVIA faces DAMIEN and speaks.
i05 blk=['MAYA'] | MAYA Abort. Abort now. She's you with better cheekbones. You'd me | At the lab, MAYA leans into the mic.
i06 blk=['OCTAVIA', 'DAMIEN'] | DAMIEN Octavia — if this were a merger, who keeps the chair? | DAMIEN faces OCTAVIA and speaks.
i07 blk=['OCTAVIA'] | OCTAVIA Whichever of us loves less. That's always the chair, Damien. | OCTAVIA faces DAMIEN and speaks.
i08 blk=['DAMIEN'] | -  | Silence. Damien studies her — respect, recognition, and something like sadness f
i09 blk=['DAMIEN'] | DAMIEN You're not interested in me at all, are you. | DAMIEN faces OCTAVIA and speaks.
i10 blk=['OCTAVIA'] | OCTAVIA I'm interested in not being a subsidiary. Your brother offer | OCTAVIA faces DAMIEN and speaks.
i11 blk=['DAMIEN'] | DAMIEN None taken. | DAMIEN faces OCTAVIA and speaks.
i12 blk=['MAYA', 'OCTAVIA'] | MAYA She just did more for you than any of us. Say thank you and  | MAYA faces OCTAVIA and speaks.
i13 blk=['DAMIEN', 'OCTAVIA'] | DAMIEN Thank you, Octavia. Keep the chair. | DAMIEN faces OCTAVIA and speaks.
i14 blk=['OCTAVIA'] | -  | Octavia raises her wine glass an eighth of an inch. From her, it's practically a