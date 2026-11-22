# VALIDATION PACKET — scene s02
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 2 — INT. PENHALIGON & SONS — TRUST OFFICE — DAY

*An office so old the wood has seniority. MR. PENHALIGON, 80, a lawyer
who predates the concept of urgency, opens a leather-bound document
with the tenderness of a man diffusing a bomb.*

PENHALIGON
Section fourteen of the Alistair Cross Family Trust. Your father's
handwriting, his insistence, his lawyers' headaches. Quoting:

*He adjusts his glasses.*

PENHALIGON (CONT'D)
"Voting control of Cross Holdings vests in the heir upon his
thirty-second birthday, provided he is married — and demonstrably so."

DAMIEN
"Demonstrably."

PENHALIGON
Your father anticipated you might attempt a technicality. There's a
second page. It's mostly adjectives.

*Damien reads the second page. Something passes across his face that
might, in a warmer man, have been a wince.*

DAMIEN
Fine. We'll procure a wife.

*The room goes very still. His corporate counsel — a woman named DALE
who has billed him for nine years — blinks.*

DAMIEN (CONT'D)
An expression.

DALE
It wasn't, sir.

DAMIEN
A wife, then. The process. How long does it take?

PENHALIGON
Statistically? Between eighteen months and never.

DAMIEN
We have eight weeks.

PENHALIGON
Then statistically — never.

DAMIEN
(to Dale)
Task force. Treat it like a hostile acquisition of my own personal
life.

DALE
Sir, with respect — you can't due-diligence a marriage.

DAMIEN
Watch me. Candidate criteria, background checks, compatibility scoring,
negotiation window, closing date.

PENHALIGON
(delighted, at last)
Your father wrote a second clause for this exact sentence.

DAMIEN
What does it say.

PENHALIGON
"No loopholes, Damien. I know how you think. Signed — Dad."

*Damien looks at the signature. For half a second — only half — the
boardroom face drops, and there's a boy who used to sit on this office's
floor while his father signed things.*

DAMIEN
Noted.

PENHALIGON
He also wrote, and I paraphrase — "I do this because I love you, and
because you'll hate it, and those are the same thing."

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 2,
  "scene_heading": "INT. PENHALIGON & SONS — TRUST OFFICE — DAY",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "The inciting document. Penhaligon reads the father's marriage clause aloud and Damien receives the news the only way he can — as a procurement problem. The scene's real payload is emotional and arrives disguised as paperwork: 'No loopholes, Damien. I know how you think. Signed — Dad.' The half-second where the boardroom face drops and a boy sits on this office's floor is the film's first crack in the armor.",
  "zones": [
    "trust office"
  ],
  "events": [
    {
      "event_id": "s02.e01",
      "source_evidence": [
        "An office so old the wood has seniority. MR. PENHALIGON, 80, a lawyer who predates the concept of urgency, opens a leather-bound document with the tenderness of a man diffusing a bomb.",
        "Section fourteen of the Alistair Cross Family Trust. Your father's handwriting, his insistence, his lawyers' headaches. Quoting:",
        "He adjusts his glasses.",
        "\"Voting control of Cross Holdings vests in the heir upon his thirty-second birthday, provided he is married — and demonstrably so.\""
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the bomb placed on the desk — the father's clause read aloud in the father's handwriting",
      "participants": [
        "PENHALIGON",
        "DAMIEN",
        "DALE"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "DALE"
      ],
      "document_evidence": [
        {
          "artifact": "Alistair Cross Family Trust — section fourteen, in the father's handwriting",
          "channel": "document"
        }
      ],
      "location": {
        "zone": "trust office"
      },
      "timeline": [
        {
          "beat": "the office — wood with seniority; the leather-bound document opened like a bomb defused",
          "type": "atmosphere"
        },
        {
          "beat": "'Section fourteen — your father's handwriting, his insistence. Quoting:'",
          "type": "dialogue"
        },
        {
          "beat": "he adjusts his glasses",
          "type": "action"
        },
        {
          "beat": "the clause read aloud — voting control vests at thirty-two, provided he is married, and demonstrably so",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the document is handled like ordnance — the tenderness is in the hands, not the face",
        "the clause page is a document insert — the handwriting must read as the father's"
      ],
      "audio_requirements": [
        "leather-bound document opening — page and old-wood quiet"
      ],
      "continuity_constraints": [
        "section fourteen and 'demonstrably so' are load-bearing — the whole film argues about what demonstrably means"
      ],
      "ambiguities": [],
      "must_appear": [
        "PENHALIGON",
        "DAMIEN"
      ],
      "tableau": true,
      "shot_sequence": [
        "s02.sh01",
        "s02.sh02",
        "s02.sh03",
        "s02.snd01"
      ]
    },
    {
      "event_id": "s02.e02",
      "source_evidence": [
        "\"Demonstrably.\"",
        "Your father anticipated you might attempt a technicality. There's a second page. It's mostly adjectives.",
        "Damien reads the second page. Something passes across his face that might, in a warmer man, have been a wince."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the loophole-hunter pre-empted — the father left a second page of adjectives for exactly this moment",
      "participants": [
        "DAMIEN",
        "PENHALIGON",
        "DALE"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "DALE"
      ],
      "document_evidence": [
        {
          "artifact": "the trust's second page — 'mostly adjectives'",
          "channel": "document"
        }
      ],
      "location": {
        "zone": "trust office"
      },
      "timeline": [
        {
          "beat": "'Demonstrably.' — the word tasted for loopholes",
          "type": "dialogue"
        },
        {
          "beat": "'Your father anticipated a technicality — there's a second page, mostly adjectives'",
          "type": "dialogue"
        },
        {
          "beat": "the second page read — something that in a warmer man would be a wince",
          "type": "held_reaction"
        }
      ],
      "visual_requirements": [
        "the wince is sub-perceptual — a data point for the audience, not a performance for the room"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the father is dead before the film starts — he exists only as handwriting, clauses and other people's quotes"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s02.sh04",
        "s02.sh05",
        "s02.sh06"
      ]
    },
    {
      "event_id": "s02.e03",
      "source_evidence": [
        "Fine. We'll procure a wife.",
        "The room goes very still. His corporate counsel — a woman named DALE who has billed him for nine years — blinks."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the decision that defines him — marriage processed as a procurement verb, and the room registering it",
      "participants": [
        "DAMIEN",
        "PENHALIGON",
        "DALE"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "location": {
        "zone": "trust office"
      },
      "timeline": [
        {
          "beat": "'Fine. We'll procure a wife.'",
          "type": "dialogue"
        },
        {
          "beat": "the room goes very still",
          "type": "held_reaction"
        },
        {
          "beat": "Dale — nine years of billing — blinks",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "'procure' lands without irony in his mouth — the stillness around him carries the judgment"
      ],
      "audio_requirements": [
        "the room's sudden still — clock and old wood going quiet"
      ],
      "continuity_constraints": [
        "Dale is introduced here — nine years of billing history is why her blink counts"
      ],
      "ambiguities": [],
      "must_appear": [
        "DALE"
      ],
      "tableau": false,
      "shot_sequence": [
        "s02.sh07",
        "s02.sh08",
        "s02.snd01"
      ]
    },
    {
      "event_id": "s02.e04",
      "source_evidence": [
        "An expression.",
        "It wasn't, sir."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the two-word audit — Damien annotates Dale's blink and Dale declines the annotation",
      "participants": [
        "DAMIEN",
        "DALE",
        "PENHALIGON"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "PENHALIGON"
      ],
      "location": {
        "zone": "trust office"
      },
      "timeline": [
        {
          "beat": "'An expression.'",
          "type": "dialogue"
        },
        {
          "beat": "'It wasn't, sir.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "played completely flat on both sides — the comedy is that both are technically correct"
      ],
      "audio_requirements": [],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "DALE"
      ],
      "tableau": true,
      "shot_sequence": [
        "s02.sh09"
      ]
    },
    {
      "event_id": "s02.e05",
      "source_evidence": [
        "A wife, then. The process. How long does it take?",
        "Statistically? Between eighteen months and never.",
        "We have eight weeks.",
        "Then statistically — never."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the deadline set — eighteen-months-to-never compressed into eight weeks",
      "participants": [
        "DAMIEN",
        "PENHALIGON",
        "DALE"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "DALE"
      ],
      "location": {
        "zone": "trust office"
      },
      "timeline": [
        {
          "beat": "'The process. How long does it take?'",
          "type": "dialogue"
        },
        {
          "beat": "'Between eighteen months and never.'",
          "type": "dialogue"
        },
        {
          "beat": "'We have eight weeks.'",
          "type": "dialogue"
        },
        {
          "beat": "'Then statistically — never.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Penhaligon enjoys delivering 'never' — the only urgency he has ever shown is comic timing"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "eight weeks is the film's clock — every later deadline hangs off this line"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "PENHALIGON"
      ],
      "tableau": false,
      "shot_sequence": [
        "s02.sh10",
        "s02.sh11",
        "s02.sh12"
      ]
    },
    {
      "event_id": "s02.e06",
      "source_evidence": [
        "Task force. Treat it like a hostile acquisition of my own personal life.",
        "Sir, with respect — you can't due-diligence a marriage.",
        "Watch me. Candidate criteria, background checks, compatibility scoring, negotiation window, closing date."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the rom-com premise stated as a term sheet — Dale's one honest objection batted away with 'Watch me'",
      "participants": [
        "DAMIEN",
        "DALE",
        "PENHALIGON"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "PENHALIGON"
      ],
      "location": {
        "zone": "trust office"
      },
      "timeline": [
        {
          "beat": "'Task force — a hostile acquisition of my own personal life.'",
          "type": "dialogue"
        },
        {
          "beat": "'you can't due-diligence a marriage.'",
          "type": "dialogue"
        },
        {
          "beat": "'Watch me.' — criteria, background checks, compatibility scoring, negotiation window, closing date",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Damien directs the order to Dale, not the room — the 'task force' is born as a headcount of one"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "'negotiation window, closing date' is the vocabulary A.V.A. later parodies — same cadence, warmer mouth"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "DALE"
      ],
      "tableau": true,
      "shot_sequence": [
        "s02.sh13"
      ]
    },
    {
      "event_id": "s02.e07",
      "source_evidence": [
        "Your father wrote a second clause for this exact sentence.",
        "What does it say.",
        "\"No loopholes, Damien. I know how you think. Signed — Dad.\""
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the dead father answers the living son — a clause written in advance for this exact sentence",
      "participants": [
        "PENHALIGON",
        "DAMIEN",
        "DALE"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "DALE"
      ],
      "document_evidence": [
        {
          "artifact": "the father's second clause — 'No loopholes, Damien. I know how you think. Signed — Dad.'",
          "channel": "document"
        }
      ],
      "location": {
        "zone": "trust office"
      },
      "timeline": [
        {
          "beat": "delighted, at last — 'your father wrote a second clause for this exact sentence'",
          "type": "dialogue"
        },
        {
          "beat": "'What does it say.'",
          "type": "dialogue"
        },
        {
          "beat": "'No loopholes, Damien. I know how you think. Signed — Dad.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Penhaligon's delight is the only smile the office has produced — it is directed at the joke, not at Damien"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "'Signed — Dad' is read off the page — the signature itself becomes the next event's insert"
      ],
      "ambiguities": [],
      "must_appear": [
        "PENHALIGON",
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s02.sh14",
        "s02.sh15",
        "s02.sh16"
      ]
    },
    {
      "event_id": "s02.e08",
      "source_evidence": [
        "Damien looks at the signature. For half a second — only half — the boardroom face drops, and there's a boy who used to sit on this office's floor while his father signed things.",
        "Noted.",
        "He also wrote, and I paraphrase — \"I do this because I love you, and because you'll hate it, and those are the same thing.\""
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the grief underneath the compliance — half a second of the boy on the floor, then 'Noted.' as the mask reseals; the father's love stated as a clause",
      "participants": [
        "DAMIEN",
        "PENHALIGON",
        "DALE"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "PENHALIGON",
        "DALE"
      ],
      "location": {
        "zone": "trust office"
      },
      "timeline": [
        {
          "beat": "the signature — half a second, only half, the boardroom face drops; the boy who sat on this floor",
          "type": "held_reaction"
        },
        {
          "beat": "'Noted.'",
          "type": "dialogue"
        },
        {
          "beat": "'I do this because I love you, and because you'll hate it, and those are the same thing.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the half-second drop is the scene — the camera must already be on him when it happens",
        "Penhaligon's last line lands over Damien's held face — the love arrives while the mask is still down"
      ],
      "audio_requirements": [
        "the held half-second over the signature — room tone only"
      ],
      "continuity_constraints": [
        "the boy-on-the-floor memory is narration rendered as a held face — do not cut to a flashback",
        "'those are the same thing' is the film's thesis spoken by a dead man — keep the exact wording"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s02.sh17",
        "s02.sh18",
        "s02.snd01"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s02.sh01",
      "size": "M",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "PENHALIGON",
        "DAMIEN"
      ],
      "implements": [
        "s02.e01"
      ],
      "covers_beats": {
        "s02.e01": [
          0
        ]
      },
      "purpose": "the office established — wood with seniority; Penhaligon opens the leather-bound document like a man defusing a bomb",
      "audio_note": "leather-bound document opening, old-wood quiet"
    },
    {
      "shot_id": "s02.sh02",
      "size": "CU",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "PENHALIGON"
      ],
      "implements": [
        "s02.e01"
      ],
      "covers_beats": {
        "s02.e01": [
          1,
          2
        ]
      },
      "purpose": "'Section fourteen' — the glasses adjusted, the page located, the quoting announced",
      "audio_note": "page turn, old-wood quiet",
      "dialogue_lines": [
        {
          "event_id": "s02.e01",
          "speaker": "PENHALIGON",
          "line": "Section fourteen of the Alistair Cross Family Trust. Your father's handwriting, his insistence, his lawyers' headaches. Quoting:",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "offscreen",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s02.sh03",
      "size": "INS",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "PENHALIGON"
      ],
      "depicts": [
        {
          "object": "trust document page — the father's handwriting, section fourteen",
          "channel": "in_frame"
        }
      ],
      "implements": [
        "s02.e01"
      ],
      "covers_beats": {
        "s02.e01": [
          3
        ]
      },
      "purpose": "the clause page — 'demonstrably so' read aloud over the father's handwriting",
      "audio_note": "paper under a level voice",
      "dialogue_lines": [
        {
          "event_id": "s02.e01",
          "speaker": "PENHALIGON",
          "line": "\"Voting control of Cross Holdings vests in the heir upon his thirty-second birthday, provided he is married — and demonstrably so.\"",
          "line_kind": "over_picture",
          "recipient": "DAMIEN",
          "recipient_presence": "offscreen",
          "beats": [
            3
          ]
        }
      ]
    },
    {
      "shot_id": "s02.sh04",
      "size": "CU",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s02.e02"
      ],
      "covers_beats": {
        "s02.e02": [
          0
        ]
      },
      "purpose": "'Demonstrably.' — the word repeated like a clause being test-loaded",
      "dialogue_lines": [
        {
          "event_id": "s02.e02",
          "speaker": "DAMIEN",
          "line": "\"Demonstrably.\"",
          "line_kind": "on_camera",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s02.sh05",
      "size": "M",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "PENHALIGON"
      ],
      "implements": [
        "s02.e02"
      ],
      "covers_beats": {
        "s02.e02": [
          1
        ]
      },
      "purpose": "the second page produced — 'mostly adjectives' delivered dry",
      "dialogue_lines": [
        {
          "event_id": "s02.e02",
          "speaker": "PENHALIGON",
          "line": "Your father anticipated you might attempt a technicality. There's a second page. It's mostly adjectives.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "offscreen",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s02.sh06",
      "size": "CU",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s02.e02"
      ],
      "covers_beats": {
        "s02.e02": [
          2
        ]
      },
      "purpose": "the second page read — the almost-wince passes and is gone",
      "audio_note": "page turn, held quiet"
    },
    {
      "shot_id": "s02.sh07",
      "size": "M",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s02.e03"
      ],
      "covers_beats": {
        "s02.e03": [
          0
        ]
      },
      "purpose": "'Fine. We'll procure a wife.' — the decision delivered like a line item",
      "dialogue_lines": [
        {
          "event_id": "s02.e03",
          "speaker": "DAMIEN",
          "line": "Fine. We'll procure a wife.",
          "line_kind": "on_camera",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s02.sh08",
      "size": "M",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "DALE",
        "PENHALIGON"
      ],
      "implements": [
        "s02.e03"
      ],
      "covers_beats": {
        "s02.e03": [
          1,
          2
        ]
      },
      "purpose": "the room goes very still — Dale's nine-year blink, Penhaligon holding the document",
      "audio_note": "the room's sudden still — clock and old wood"
    },
    {
      "shot_id": "s02.sh09",
      "size": "two-shot",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "DALE"
      ],
      "implements": [
        "s02.e04"
      ],
      "covers_beats": {
        "s02.e04": [
          0,
          1
        ]
      },
      "purpose": "'An expression.' / 'It wasn't, sir.' — the two-word audit, both sides flat",
      "dialogue_lines": [
        {
          "event_id": "s02.e04",
          "speaker": "DAMIEN",
          "line": "An expression.",
          "line_kind": "on_camera",
          "recipient": "DALE",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s02.e04",
          "speaker": "DALE",
          "line": "It wasn't, sir.",
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
      "shot_id": "s02.sh10",
      "size": "two-shot",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "PENHALIGON"
      ],
      "implements": [
        "s02.e05"
      ],
      "covers_beats": {
        "s02.e05": [
          0,
          1
        ]
      },
      "purpose": "'The process. How long does it take?' / 'Between eighteen months and never.'",
      "dialogue_lines": [
        {
          "event_id": "s02.e05",
          "speaker": "DAMIEN",
          "line": "A wife, then. The process. How long does it take?",
          "line_kind": "on_camera",
          "recipient": "PENHALIGON",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s02.e05",
          "speaker": "PENHALIGON",
          "line": "Statistically? Between eighteen months and never.",
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
      "shot_id": "s02.sh11",
      "size": "CU",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s02.e05"
      ],
      "covers_beats": {
        "s02.e05": [
          2
        ]
      },
      "purpose": "'We have eight weeks.' — the deadline dropped without inflection",
      "dialogue_lines": [
        {
          "event_id": "s02.e05",
          "speaker": "DAMIEN",
          "line": "We have eight weeks.",
          "line_kind": "on_camera",
          "recipient": "PENHALIGON",
          "recipient_presence": "offscreen",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s02.sh12",
      "size": "CU",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "PENHALIGON"
      ],
      "implements": [
        "s02.e05"
      ],
      "covers_beats": {
        "s02.e05": [
          3
        ]
      },
      "purpose": "'Then statistically — never.' — delivered with eighty years of patience",
      "dialogue_lines": [
        {
          "event_id": "s02.e05",
          "speaker": "PENHALIGON",
          "line": "Then statistically — never.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "offscreen",
          "beats": [
            3
          ]
        }
      ]
    },
    {
      "shot_id": "s02.sh13",
      "size": "two-shot",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "DALE"
      ],
      "implements": [
        "s02.e06"
      ],
      "covers_beats": {
        "s02.e06": [
          0,
          1,
          2
        ]
      },
      "purpose": "the task force order to Dale, her objection, and 'Watch me' — the acquisition checklist",
      "dialogue_lines": [
        {
          "event_id": "s02.e06",
          "speaker": "DAMIEN",
          "line": "Task force. Treat it like a hostile acquisition of my own personal life.",
          "line_kind": "on_camera",
          "recipient": "DALE",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s02.e06",
          "speaker": "DALE",
          "line": "Sir, with respect — you can't due-diligence a marriage.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s02.e06",
          "speaker": "DAMIEN",
          "line": "Watch me. Candidate criteria, background checks, compatibility scoring, negotiation window, closing date.",
          "line_kind": "on_camera",
          "recipient": "DALE",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s02.sh14",
      "size": "M",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "PENHALIGON"
      ],
      "implements": [
        "s02.e07"
      ],
      "covers_beats": {
        "s02.e07": [
          0
        ]
      },
      "purpose": "delighted at last — the second clause exists for this exact sentence",
      "dialogue_lines": [
        {
          "event_id": "s02.e07",
          "speaker": "PENHALIGON",
          "line": "Your father wrote a second clause for this exact sentence.",
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
      "shot_id": "s02.sh15",
      "size": "CU",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s02.e07"
      ],
      "covers_beats": {
        "s02.e07": [
          1
        ]
      },
      "purpose": "'What does it say.' — flat as a subpoena",
      "dialogue_lines": [
        {
          "event_id": "s02.e07",
          "speaker": "DAMIEN",
          "line": "What does it say.",
          "line_kind": "on_camera",
          "recipient": "PENHALIGON",
          "recipient_presence": "offscreen",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s02.sh16",
      "size": "CU",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "PENHALIGON"
      ],
      "depicts": [
        {
          "object": "the father's second clause — 'No loopholes, Damien' over his signature",
          "channel": "in_frame"
        }
      ],
      "implements": [
        "s02.e07"
      ],
      "covers_beats": {
        "s02.e07": [
          2
        ]
      },
      "purpose": "the clause read — 'No loopholes, Damien. I know how you think. Signed — Dad.'",
      "audio_note": "paper under an old voice",
      "dialogue_lines": [
        {
          "event_id": "s02.e07",
          "speaker": "PENHALIGON",
          "line": "\"No loopholes, Damien. I know how you think. Signed — Dad.\"",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "offscreen",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s02.sh17",
      "size": "CU held",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s02.e08"
      ],
      "covers_beats": {
        "s02.e08": [
          0,
          1
        ]
      },
      "purpose": "the signature — half a second of the boy on the floor, then 'Noted.' and the mask",
      "audio_note": "room tone only — the held half-second",
      "dialogue_lines": [
        {
          "event_id": "s02.e08",
          "speaker": "DAMIEN",
          "line": "Noted.",
          "line_kind": "on_camera",
          "recipient": "PENHALIGON",
          "recipient_presence": "offscreen",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s02.sh18",
      "size": "CU held",
      "zone": "trust office",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s02.e08"
      ],
      "covers_beats": {
        "s02.e08": [
          2
        ]
      },
      "purpose": "Penhaligon's paraphrase lands off-camera over Damien's held face — love stated as a clause",
      "audio_note": "room tone only",
      "dialogue_lines": [
        {
          "event_id": "s02.e08",
          "speaker": "PENHALIGON",
          "line": "He also wrote, and I paraphrase — \"I do this because I love you, and because you'll hate it, and those are the same thing.\"",
          "line_kind": "offscreen",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s02.snd01",
      "type": "sound",
      "implements": [
        "s02.e01",
        "s02.e03",
        "s02.e08"
      ],
      "purpose": "sound card: leather page turns, clock and old-wood still, room tone held over the signature",
      "audio_note": "leather-bound document opening and page turns; clock and old-wood still after 'procure a wife'; room tone only held over the signature",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "An office so old the wood has seniority. MR. PENHALIGON, 80, a lawyer who predates the concept of urgency, opens a leather-bound document with the tenderness of a man diffusing a bomb.",
      "disposition": "covered_by",
      "by": [
        "s02.e01"
      ]
    },
    {
      "span": "Section fourteen of the Alistair Cross Family Trust. Your father's handwriting, his insistence, his lawyers' headaches. Quoting:",
      "disposition": "covered_by",
      "by": [
        "s02.e01"
      ]
    },
    {
      "span": "He adjusts his glasses.",
      "disposition": "covered_by",
      "by": [
        "s02.e01"
      ]
    },
    {
      "span": "\"Voting control of Cross Holdings vests in the heir upon his thirty-second birthday, provided he is married — and demonstrably so.\"",
      "disposition": "covered_by",
      "by": [
        "s02.e01"
      ]
    },
    {
      "span": "\"Demonstrably.\"",
      "disposition": "covered_by",
      "by": [
        "s02.e02"
      ]
    },
    {
      "span": "Your father anticipated you might attempt a technicality. There's a second page. It's mostly adjectives.",
      "disposition": "covered_by",
      "by": [
        "s02.e02"
      ]
    },
    {
      "span": "Damien reads the second page. Something passes across his face that might, in a warmer man, have been a wince.",
      "disposition": "covered_by",
      "by": [
        "s02.e02"
      ]
    },
    {
      "span": "Fine. We'll procure a wife.",
      "disposition": "covered_by",
      "by": [
        "s02.e03"
      ]
    },
    {
      "span": "The room goes very still. His corporate counsel — a woman named DALE who has billed him for nine years — blinks.",
      "disposition": "covered_by",
      "by": [
        "s02.e03"
      ]
    },
    {
      "span": "An expression.",
      "disposition": "covered_by",
      "by": [
        "s02.e04"
      ]
    },
    {
      "span": "It wasn't, sir.",
      "disposition": "covered_by",
      "by": [
        "s02.e04"
      ]
    },
    {
      "span": "A wife, then. The process. How long does it take?",
      "disposition": "covered_by",
      "by": [
        "s02.e05"
      ]
    },
    {
      "span": "Statistically? Between eighteen months and never.",
      "disposition": "covered_by",
      "by": [
        "s02.e05"
      ]
    },
    {
      "span": "We have eight weeks.",
      "disposition": "covered_by",
      "by": [
        "s02.e05"
      ]
    },
    {
      "span": "Then statistically — never.",
      "disposition": "covered_by",
      "by": [
        "s02.e05"
      ]
    },
    {
      "span": "Task force. Treat it like a hostile acquisition of my own personal life.",
      "disposition": "covered_by",
      "by": [
        "s02.e06"
      ]
    },
    {
      "span": "Sir, with respect — you can't due-diligence a marriage.",
      "disposition": "covered_by",
      "by": [
        "s02.e06"
      ]
    },
    {
      "span": "Watch me. Candidate criteria, background checks, compatibility scoring, negotiation window, closing date.",
      "disposition": "covered_by",
      "by": [
        "s02.e06"
      ]
    },
    {
      "span": "Your father wrote a second clause for this exact sentence.",
      "disposition": "covered_by",
      "by": [
        "s02.e07"
      ]
    },
    {
      "span": "What does it say.",
      "disposition": "covered_by",
      "by": [
        "s02.e07"
      ]
    },
    {
      "span": "\"No loopholes, Damien. I know how you think. Signed — Dad.\"",
      "disposition": "covered_by",
      "by": [
        "s02.e07"
      ]
    },
    {
      "span": "Damien looks at the signature. For half a second — only half — the boardroom face drops, and there's a boy who used to sit on this office's floor while his father signed things.",
      "disposition": "covered_by",
      "by": [
        "s02.e08"
      ]
    },
    {
      "span": "Noted.",
      "disposition": "covered_by",
      "by": [
        "s02.e08"
      ]
    },
    {
      "span": "He also wrote, and I paraphrase — \"I do this because I love you, and because you'll hate it, and those are the same thing.\"",
      "disposition": "covered_by",
      "by": [
        "s02.e08"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['PENHALIGON'] | -  | An office so old the wood has seniority. MR. PENHALIGON, a lawyer who predates t
i02 blk=['PENHALIGON', 'DAMIEN'] | PENHALIGON Section fourteen of the Alistair Cross Family Trust. Your fa | PENHALIGON faces DAMIEN and speaks. He adjusts his glasses.
i03 blk=['DAMIEN'] | DAMIEN "Demonstrably." | DAMIEN faces PENHALIGON and speaks.
i04 blk=['PENHALIGON'] | PENHALIGON Your father anticipated you might attempt a technicality. Th | PENHALIGON faces DAMIEN and speaks.
i05 blk=['DAMIEN'] | -  | Damien reads the second page. Something passes across his face that might, in a 
i06 blk=['DALE', 'DAMIEN'] | DAMIEN Fine. We'll procure a wife. | DAMIEN faces PENHALIGON and speaks.
i07 blk=['DALE'] | -  | The room goes very still. His corporate counsel — a woman named DALE who has bil
i08 blk=['DAMIEN'] | DAMIEN An expression. | DAMIEN faces PENHALIGON and speaks.
i09 blk=['DALE'] | DALE It wasn't, sir. | DALE faces PENHALIGON and speaks.
i10 blk=['DAMIEN', 'PENHALIGON'] | DAMIEN A wife, then. The process. How long does it take? | DAMIEN faces PENHALIGON and speaks.
i11 blk=['PENHALIGON'] | PENHALIGON Statistically? Between eighteen months and never. | PENHALIGON faces DAMIEN and speaks.
i12 blk=['DAMIEN', 'PENHALIGON'] | DAMIEN We have eight weeks. | DAMIEN faces PENHALIGON and speaks.
i13 blk=['DAMIEN', 'PENHALIGON'] | PENHALIGON Then statistically — never. | PENHALIGON faces DAMIEN and speaks.
i14 blk=['DAMIEN'] | DAMIEN Task force. Treat it like a hostile acquisition of my own pe | DAMIEN faces PENHALIGON and speaks.
i15 blk=['DALE'] | DALE Sir, with respect — you can't due-diligence a marriage. | DALE faces PENHALIGON and speaks.
i16 blk=['DAMIEN'] | DAMIEN Watch me. Candidate criteria, background checks, compatibili | DAMIEN faces PENHALIGON and speaks.
i17 blk=['PENHALIGON', 'DAMIEN'] | PENHALIGON Your father wrote a second clause for this exact sentence. | PENHALIGON faces DAMIEN and speaks.
i18 blk=['DAMIEN'] | DAMIEN What does it say. | DAMIEN faces PENHALIGON and speaks.
i19 blk=['PENHALIGON'] | PENHALIGON "No loopholes, Damien. I know how you think. Signed — Dad." | PENHALIGON faces DAMIEN and speaks.
i20 blk=['DAMIEN'] | -  | Damien looks at the signature. For half a second — only half — the boardroom fac
i21 blk=['PENHALIGON', 'DAMIEN'] | DAMIEN Noted. | DAMIEN faces PENHALIGON and speaks.
i22 blk=['PENHALIGON'] | PENHALIGON He also wrote, and I paraphrase — "I do this because I love  | PENHALIGON faces DAMIEN and speaks.