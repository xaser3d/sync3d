# VALIDATION PACKET — scene s10
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 10 — INT. PENTHOUSE — SERVICE DOCK — NIGHT

*The dinner is over. MAYA wheels A.V.A. back into the service
dock — JIM holding the door, sweating.*

JIM
For the record: you are the understudy for a toaster.

MAYA
She's a four-hundred-series adaptive companion.

JIM
You're the understudy for an expensive toaster. And the
toaster's understudy just got a children's hospital funded.

MAYA
That was — look, the contract says the unit stays at
performance for sixty days or the lab eats the cost of the
whole deployment plus a penalty clause that would kill us
twice. I can't fix her battery curve in time. But her windows
are predictable — four hours on, six charging. I can cover
the gaps.

JIM
You want to keep pretending to be your own robot for two
months.

MAYA
Nine weeks. It's not pretending — it's live debugging. Every
social failure I make as her, I fix in her that night. It's
field data.

JIM
It's a felony wearing a nice dress.

MAYA
It's an NDA with consequences. Different thing.

JIM
(a long look; then, beaten)
You're going to need someone on the inside. Doors, schedules,
distractions when the toaster needs her nap.

MAYA
You'd help?

JIM
Lady, I drive a man who calls his own mother "the board."
This is the most human thing to happen in this building in
six years. I'm in.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 10,
  "scene_heading": "INT. PENTHOUSE — SERVICE DOCK — NIGHT",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "Post-party debrief at the service dock — the swap survived night one. Jim is recruited, the two-month arrangement is invented out loud, and the film's engine starts here: Maya will cover A.V.A.'s charge windows as 'field data' while the contract clock runs. The scene's warmth is that the building's most human thing in six years is two people conspiring to keep a machine alive.",
  "zones": [
    "service dock"
  ],
  "events": [
    {
      "event_id": "s10.e01",
      "source_evidence": [
        "The dinner is over. MAYA wheels A.V.A. back into the service dock — JIM holding the door, sweating."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "aftermath — the conspiracy's first successful night; the scene plays in back-of-house quiet where the debrief can happen",
      "participants": [
        "MAYA",
        "A.V.A.",
        "JIM"
      ],
      "remote_participants": [],
      "location": {
        "zone": "service dock"
      },
      "timeline": [
        {
          "beat": "Maya wheels A.V.A. back into the service dock — the dinner is over",
          "type": "action"
        },
        {
          "beat": "Jim holding the door, sweating",
          "type": "held_image"
        }
      ],
      "visual_requirements": [
        "the wheel-in rhymes with S9's haul-out — same cargo, now one conspirator richer",
        "Jim's sweat is the performance note: he has spent the evening as an accomplice"
      ],
      "audio_requirements": [
        "post-party hush — dock wheels on concrete, the penthouse settling after guests"
      ],
      "continuity_constraints": [
        "Maya still wears A.V.A.'s evening wrap over whatever came off in the corridor — the costume continuity of the swap"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "A.V.A.",
        "JIM"
      ],
      "tableau": true,
      "shot_sequence": [
        "s10.sh01",
        "s10.snd01"
      ]
    },
    {
      "event_id": "s10.e02",
      "source_evidence": [
        "For the record: you are the understudy for a toaster.",
        "She's a four-hundred-series adaptive companion.",
        "You're the understudy for an expensive toaster. And the toaster's understudy just got a children's hospital funded."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the absurdity named, then justified — Jim's toaster insult accidentally delivers the scene's thesis: the understudy already outperformed the star",
      "participants": [
        "JIM",
        "MAYA",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "service dock"
      },
      "timeline": [
        {
          "beat": "'For the record: you are the understudy for a toaster.'",
          "type": "dialogue"
        },
        {
          "beat": "'She's a four-hundred-series adaptive companion.'",
          "type": "dialogue"
        },
        {
          "beat": "'the toaster's understudy just got a children's hospital funded.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the docked android is the third party in the frame — the joke plays to her frozen audience of one"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the hospital line confirms e06's cardiac wing actually funded — the swap's first proof of concept"
      ],
      "ambiguities": [],
      "must_appear": [
        "JIM",
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s10.sh02"
      ]
    },
    {
      "event_id": "s10.e03",
      "source_evidence": [
        "That was — look, the contract says the unit stays at performance for sixty days or the lab eats the cost of the whole deployment plus a penalty clause that would kill us twice. I can't fix her battery curve in time. But her windows are predictable — four hours on, six charging. I can cover the gaps.",
        "You want to keep pretending to be your own robot for two months.",
        "Nine weeks. It's not pretending — it's live debugging. Every social failure I make as her, I fix in her that night. It's field data.",
        "It's a felony wearing a nice dress.",
        "It's an NDA with consequences. Different thing."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the series engine pitched — fraud reframed as field data; Maya sells the swap as methodology and Jim prices it correctly as a felony",
      "participants": [
        "MAYA",
        "JIM",
        "A.V.A."
      ],
      "offscreen_present": [
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "service dock"
      },
      "timeline": [
        {
          "beat": "the contract math — sixty days at performance or the lab dies; windows predictable, 'I can cover the gaps'",
          "type": "dialogue"
        },
        {
          "beat": "'You want to keep pretending to be your own robot for two months.'",
          "type": "dialogue"
        },
        {
          "beat": "'Nine weeks' — not pretending, live debugging; field data",
          "type": "dialogue"
        },
        {
          "beat": "'It's a felony wearing a nice dress.'",
          "type": "dialogue"
        },
        {
          "beat": "'It's an NDA with consequences. Different thing.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Maya's pitch is a founder's defense — numbers first, moral language second; she believes 'field data' while she says it",
        "Jim listens like a man pricing his own complicity — the felony/NDA exchange is the price negotiation"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the sixty-day performance clause + penalty is the contract Victor 'already thought of' in S7 — the trap's terms finally stated",
        "'four hours on, six charging' is now protocol — the cover schedule that structures the middle of the film"
      ],
      "ambiguities": [
        "'It's a felony' — Jim's guess at the legal exposure is his own read; whether any actual statute applies is unresolved in-text, flag for director"
      ],
      "must_appear": [
        "MAYA",
        "JIM"
      ],
      "tableau": false,
      "shot_sequence": [
        "s10.sh03",
        "s10.sh04"
      ]
    },
    {
      "event_id": "s10.e04",
      "source_evidence": [
        "(a long look; then, beaten)",
        "You're going to need someone on the inside. Doors, schedules, distractions when the toaster needs her nap.",
        "You'd help?",
        "Lady, I drive a man who calls his own mother \"the board.\" This is the most human thing to happen in this building in six years. I'm in."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the crew forms — Jim's surrender is the scene's warmth: he prices the job, offers himself, and names why in the same breath",
      "participants": [
        "JIM",
        "MAYA",
        "A.V.A."
      ],
      "offscreen_present": [
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "service dock"
      },
      "timeline": [
        {
          "beat": "the long look — beaten",
          "type": "held_reaction"
        },
        {
          "beat": "'You're going to need someone on the inside' — doors, schedules, nap distractions",
          "type": "dialogue"
        },
        {
          "beat": "'You'd help?'",
          "type": "dialogue"
        },
        {
          "beat": "'the most human thing to happen in this building in six years. I'm in.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the long look is the whole negotiation — Jim deciding who he is before he says it",
        "'I'm in' lands as relief, not tension — the scene ends on a conspiracy the audience roots for"
      ],
      "audio_requirements": [
        "the held quiet of the dock at night — the conspiracy's first silence"
      ],
      "continuity_constraints": [
        "Jim becomes the inside man — doors/schedules/distractions is the job description he executes through the cover months"
      ],
      "ambiguities": [],
      "must_appear": [
        "JIM",
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s10.sh05",
        "s10.sh06",
        "s10.snd01"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s10.sh01",
      "size": "M",
      "zone": "service dock",
      "type": "visual",
      "participants": [
        "MAYA",
        "A.V.A.",
        "JIM"
      ],
      "implements": [
        "s10.e01"
      ],
      "covers_beats": {
        "s10.e01": [
          0,
          1
        ]
      },
      "purpose": "the return — Maya wheels the frozen android back into the dock, Jim holding the door, sweating",
      "audio_note": "post-party hush, dock wheels on concrete"
    },
    {
      "shot_id": "s10.sh02",
      "size": "two-shot",
      "zone": "service dock",
      "type": "visual",
      "participants": [
        "JIM",
        "MAYA",
        "A.V.A."
      ],
      "implements": [
        "s10.e02"
      ],
      "covers_beats": {
        "s10.e02": [
          0,
          1,
          2
        ]
      },
      "purpose": "the toaster exchange — 'understudy for a toaster' → 'four-hundred-series adaptive companion' → 'the toaster's understudy just got a children's hospital funded'",
      "dialogue_lines": [
        {
          "event_id": "s10.e02",
          "speaker": "JIM",
          "line": "For the record: you are the understudy for a toaster.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s10.e02",
          "speaker": "MAYA",
          "line": "She's a four-hundred-series adaptive companion.",
          "line_kind": "on_camera",
          "recipient": "JIM",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s10.e02",
          "speaker": "JIM",
          "line": "You're the understudy for an expensive toaster. And the toaster's understudy just got a children's hospital funded.",
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
      "shot_id": "s10.sh03",
      "size": "M",
      "zone": "service dock",
      "type": "visual",
      "participants": [
        "MAYA",
        "JIM"
      ],
      "implements": [
        "s10.e03"
      ],
      "covers_beats": {
        "s10.e03": [
          0,
          1
        ]
      },
      "purpose": "the contract math — sixty days or the lab dies; 'You want to keep pretending to be your own robot for two months.'",
      "dialogue_lines": [
        {
          "event_id": "s10.e03",
          "speaker": "MAYA",
          "line": "That was — look, the contract says the unit stays at performance for sixty days or the lab eats the cost of the whole deployment plus a penalty clause that would kill us twice. I can't fix her battery curve in time. But her windows are predictable — four hours on, six charging. I can cover the gaps.",
          "line_kind": "on_camera",
          "recipient": "JIM",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s10.e03",
          "speaker": "JIM",
          "line": "You want to keep pretending to be your own robot for two months.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s10.sh04",
      "size": "two-shot",
      "zone": "service dock",
      "type": "visual",
      "participants": [
        "MAYA",
        "JIM"
      ],
      "implements": [
        "s10.e03"
      ],
      "covers_beats": {
        "s10.e03": [
          2,
          3,
          4
        ]
      },
      "purpose": "'Nine weeks... field data' → 'a felony wearing a nice dress' → 'an NDA with consequences. Different thing.'",
      "dialogue_lines": [
        {
          "event_id": "s10.e03",
          "speaker": "MAYA",
          "line": "Nine weeks. It's not pretending — it's live debugging. Every social failure I make as her, I fix in her that night. It's field data.",
          "line_kind": "on_camera",
          "recipient": "JIM",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s10.e03",
          "speaker": "JIM",
          "line": "It's a felony wearing a nice dress.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        },
        {
          "event_id": "s10.e03",
          "speaker": "MAYA",
          "line": "It's an NDA with consequences. Different thing.",
          "line_kind": "on_camera",
          "recipient": "JIM",
          "recipient_presence": "physical",
          "beats": [
            4
          ]
        }
      ]
    },
    {
      "shot_id": "s10.sh05",
      "size": "CU",
      "zone": "service dock",
      "type": "visual",
      "participants": [
        "JIM"
      ],
      "implements": [
        "s10.e04"
      ],
      "covers_beats": {
        "s10.e04": [
          0,
          1
        ]
      },
      "purpose": "the long look — beaten → 'You're going to need someone on the inside. Doors, schedules, distractions when the toaster needs her nap.'",
      "audio_note": "the held quiet of the dock at night",
      "dialogue_lines": [
        {
          "event_id": "s10.e04",
          "speaker": "JIM",
          "line": "You're going to need someone on the inside. Doors, schedules, distractions when the toaster needs her nap.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "offscreen",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s10.sh06",
      "size": "two-shot",
      "zone": "service dock",
      "type": "visual",
      "participants": [
        "JIM",
        "MAYA"
      ],
      "implements": [
        "s10.e04"
      ],
      "covers_beats": {
        "s10.e04": [
          2,
          3
        ]
      },
      "purpose": "'You'd help?' → 'the most human thing to happen in this building in six years. I'm in.'",
      "dialogue_lines": [
        {
          "event_id": "s10.e04",
          "speaker": "MAYA",
          "line": "You'd help?",
          "line_kind": "on_camera",
          "recipient": "JIM",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s10.e04",
          "speaker": "JIM",
          "line": "Lady, I drive a man who calls his own mother \"the board.\" This is the most human thing to happen in this building in six years. I'm in.",
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
      "shot_id": "s10.snd01",
      "type": "sound",
      "implements": [
        "s10.e01",
        "s10.e04"
      ],
      "purpose": "sound card: post-party hush — dock wheels on concrete, the penthouse settling after guests, the held quiet of the dock at night; the conspiracy plays in room tone",
      "audio_note": "post-party hush, dock wheels on concrete, penthouse settling, held quiet of the dock at night",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "The dinner is over.",
      "disposition": "covered_by",
      "by": [
        "s10.e01"
      ]
    },
    {
      "span": "wheels A.V.A. back into the service dock",
      "disposition": "covered_by",
      "by": [
        "s10.e01"
      ]
    },
    {
      "span": "JIM holding the door, sweating",
      "disposition": "covered_by",
      "by": [
        "s10.e01"
      ]
    },
    {
      "span": "the understudy for a toaster",
      "disposition": "covered_by",
      "by": [
        "s10.e02"
      ]
    },
    {
      "span": "a four-hundred-series adaptive companion",
      "disposition": "covered_by",
      "by": [
        "s10.e02"
      ]
    },
    {
      "span": "a children's hospital funded",
      "disposition": "covered_by",
      "by": [
        "s10.e02"
      ]
    },
    {
      "span": "the unit stays at performance for sixty days",
      "disposition": "covered_by",
      "by": [
        "s10.e03"
      ]
    },
    {
      "span": "I can cover the gaps.",
      "disposition": "covered_by",
      "by": [
        "s10.e03"
      ]
    },
    {
      "span": "your own robot for two months",
      "disposition": "covered_by",
      "by": [
        "s10.e03"
      ]
    },
    {
      "span": "Nine weeks. It's not pretending — it's live debugging.",
      "disposition": "covered_by",
      "by": [
        "s10.e03"
      ]
    },
    {
      "span": "a felony wearing a nice dress",
      "disposition": "covered_by",
      "by": [
        "s10.e03"
      ]
    },
    {
      "span": "an NDA with consequences. Different thing.",
      "disposition": "covered_by",
      "by": [
        "s10.e03"
      ]
    },
    {
      "span": "a long look; then, beaten",
      "disposition": "covered_by",
      "by": [
        "s10.e04"
      ]
    },
    {
      "span": "someone on the inside. Doors, schedules",
      "disposition": "covered_by",
      "by": [
        "s10.e04"
      ]
    },
    {
      "span": "You'd help?",
      "disposition": "covered_by",
      "by": [
        "s10.e04"
      ]
    },
    {
      "span": "calls his own mother \"the board.\"",
      "disposition": "covered_by",
      "by": [
        "s10.e04"
      ]
    },
    {
      "span": "This is the most human thing to happen in this building in six years. I'm in.",
      "disposition": "covered_by",
      "by": [
        "s10.e04"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['MAYA', 'JIM'] | -  | The dinner is over. MAYA wheels A.V.A. back into the service dock — JIM holding 
i02 blk=['JIM', 'MAYA'] | JIM For the record: you are the understudy for a toaster. | JIM faces MAYA and speaks.
i03 blk=['MAYA'] | MAYA She's a four-hundred-series adaptive companion. | MAYA faces JIM and speaks.
i04 blk=['JIM'] | JIM You're the understudy for an expensive toaster. And the toas | JIM faces MAYA and speaks.
i05 blk=['MAYA'] | MAYA That was — look, the contract says the unit stays at perform | MAYA faces JIM and speaks.
i06 blk=['MAYA', 'JIM'] | JIM You want to keep pretending to be your own robot for two mon | JIM faces MAYA and speaks.
i07 blk=['MAYA'] | MAYA Nine weeks. It's not pretending — it's live debugging. Every | MAYA faces JIM and speaks.
i08 blk=['JIM'] | JIM It's a felony wearing a nice dress. | JIM faces MAYA and speaks.
i09 blk=['MAYA'] | MAYA It's an NDA with consequences. Different thing. | MAYA faces JIM and speaks.
i10 blk=['JIM', 'MAYA'] | JIM You're going to need someone on the inside. Doors, schedules | JIM faces MAYA and speaks.
i11 blk=['MAYA', 'JIM'] | MAYA You'd help? | MAYA faces JIM and speaks.
i12 blk=['JIM'] | JIM Lady, I drive a man who calls his own mother "the board." Th | JIM faces MAYA and speaks.