# VALIDATION PACKET — scene s09
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 9 — INT. PENTHOUSE — SERVICE CORRIDOR — CONTINUOUS

*MAYA and JIM haul A.V.A.'s rigid body into the service corridor
off the kitchen — a procession of lies and catering trays.*

MAYA
Battery was supposed to hold four hours. She burned it in
ninety minutes — dinner party load is triple what I modeled.

JIM
So dock her. Charge her. The table thinks she's praying.

MAYA
Docking takes six hours. The dinner has ninety minutes left
and Victor's buyers are photographing her like a showroom.
If the prototype bricks on night one, Cross voids the
contract and my lab dies in eleven weeks. Ten, now.

*She looks at the frozen android. At the identical face in the
corridor's steel reflection — the face A.V.A. was built from.
Hers.*

MAYA (CONT'D)
How formal is the rest of the dinner?

JIM
Dessert, toasts, the donor pitch for the children's hospital —
wait. No. Maya. No.

*Maya is already pulling the evening wrap off A.V.A.'s
shoulders.*

MAYA
Same face. Same voice — I wrote her phoneme table off my own
larynx. The cadence I can do. Get her to the service dock,
keep anyone off this corridor, and when I signal, wheel her
out as if she finished meditating.

JIM
You're going to walk in there and pretend to be a robot.

MAYA
I built her. I know exactly how she walks.

JIM
That's what worries me.

*INT. DINING ROOM — LATER. MAYA enters in A.V.A.'s wrap —
shoulders back, glide-step perfect, smile of textbook precision.
She takes her seat. The table barely notices the switch.*

DONOR'S WIFE
Welcome back, dear. We were saying the children need a new
wing.

MAYA-A.V.A.
A cardiac wing. Damien — the foundation's last imaging suite
is four years behind spec. The hospital's director is at this
table and too polite to say it. You could fund the wing
before dessert and still have time to look reluctant about
it.

*A beat of silence. Then the hospital director laughs — really
laughs. Damien studies "the android" with new interest.*

DAMIEN
She's never been direct before. She's usually... statistical.

MAYA-A.V.A.
(recovering fast)
Post-charge recalibration. Warm mode. Flagging it as a beta
feature.

DAMIEN
Keep it.

*The toasts begin. Damien raises his glass and delivers, dry as
paper: "To the donors — whose generosity is exceeded only by
their need for tax instruments." Polite, cold laughter. And
from Maya — a real laugh, arriving a half-beat late, like it
was buffering.*

*Damien turns. Studies her.*

DAMIEN (CONT'D)
You laughed at my joke.

MAYA-A.V.A.
It was... funny.

DAMIEN
On a delay. Like it was buffering.

MAYA-A.V.A.
Processing humor involves a lookup table. The table has...
latency.

JIM (appearing with a tray, to Damien, fast)
I'll put a ticket in with IT.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 9,
  "scene_heading": "INT. PENTHOUSE — SERVICE CORRIDOR — CONTINUOUS",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "The swap — the film's hinge scene. Corridor triage turns math into a plan: ninety minutes burned, six hours to dock, eleven weeks of lab. The corridor's steel reflection gives the audience the face-mirror reveal, then Maya walks back into the dining room wearing A.V.A.'s wrap and outperforms the product — funding a children's hospital wing and laughing a half-beat late, like it was buffering. Every beat either tightens the disguise or risks it.",
  "zones": [
    "service corridor",
    "dining room"
  ],
  "events": [
    {
      "event_id": "s09.e01",
      "source_evidence": [
        "MAYA and JIM haul A.V.A.'s rigid body into the service corridor off the kitchen — a procession of lies and catering trays."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "extraction under cover — the frozen product carried out like catering; the conspiracy becomes physical labor",
      "participants": [
        "MAYA",
        "JIM",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "service corridor"
      },
      "timeline": [
        {
          "beat": "they haul her rigid body in — a procession of lies and catering trays",
          "type": "action"
        },
        {
          "beat": "the frozen smile still pleasant on the carried body",
          "type": "held_image"
        }
      ],
      "visual_requirements": [
        "the carry must read covert — trays as cover, her posture still 'meditating' while two people move her like freight",
        "the corridor is backstage — steel, carts, fluorescent honesty; the opposite of the dining room's candlelight"
      ],
      "audio_requirements": [
        "corridor hush — the party audible only through the door"
      ],
      "continuity_constraints": [
        "she is still mid-'meditation mode' from S8 — the body arrives frozen, not powered down"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "JIM",
        "A.V.A."
      ],
      "tableau": true,
      "shot_sequence": [
        "s09.sh01",
        "s09.snd01"
      ]
    },
    {
      "event_id": "s09.e02",
      "source_evidence": [
        "Battery was supposed to hold four hours. She burned it in ninety minutes — dinner party load is triple what I modeled.",
        "So dock her. Charge her. The table thinks she's praying.",
        "Docking takes six hours. The dinner has ninety minutes left and Victor's buyers are photographing her like a showroom. If the prototype bricks on night one, Cross voids the contract and my lab dies in eleven weeks. Ten, now."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the math of failure said aloud — ninety minutes burned, six hours to dock, eleven weeks to live; the deadline stack that forces the swap",
      "participants": [
        "MAYA",
        "JIM",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "service corridor"
      },
      "timeline": [
        {
          "beat": "'She burned it in ninety minutes' — dinner party load is triple the model",
          "type": "dialogue"
        },
        {
          "beat": "'So dock her. Charge her. The table thinks she's praying.'",
          "type": "dialogue"
        },
        {
          "beat": "'Docking takes six hours' — buyers photographing, lab dies in eleven weeks. Ten, now.",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the triage is spoken over the body — she is present for her own failure report",
        "Maya's pace is engineering tempo against Jim's butler calm"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the four-hour window from S8 e03's diagnosis is proven exactly as warned — the model was right and it still failed"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "JIM"
      ],
      "tableau": false,
      "shot_sequence": [
        "s09.sh02",
        "s09.sh03"
      ]
    },
    {
      "event_id": "s09.e03",
      "source_evidence": [
        "She looks at the frozen android. At the identical face in the corridor's steel reflection — the face A.V.A. was built from. Hers."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the quiet reveal — builder and build share a face; the idea arrives in the audience's head before the plan arrives in Maya's",
      "participants": [
        "MAYA",
        "A.V.A.",
        "JIM"
      ],
      "offscreen_present": [
        "JIM"
      ],
      "remote_participants": [],
      "location": {
        "zone": "service corridor"
      },
      "timeline": [
        {
          "beat": "Maya looks at the frozen android",
          "type": "held_image"
        },
        {
          "beat": "the identical face in the corridor's steel reflection — hers",
          "type": "reveal"
        }
      ],
      "visual_requirements": [
        "the reflection does the exposition — two versions of one face in a single frame, no dialogue, no push-in needed",
        "the audience must be allowed to do the math alone — the corridor gives them the evidence"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "pays off 'I'm her mother' from S7 — the face is the mother made literal; seeds the wrap transfer and every Maya-as-A.V.A. scene after"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "A.V.A."
      ],
      "tableau": true,
      "shot_sequence": [
        "s09.sh04"
      ],
      "decisions": [
        {
          "topic": "Maya/A.V.A. facial identity reveal",
          "status": "resolved-decision",
          "decision": "S9 is the first reliable visual proof of the same-face design — the reveal plays as discovery, not confirmation",
          "basis": "director_choice",
          "consequence": "S4–S8 coverage keeps A.V.A. legible but never gives the audience a frontal, comparable portrait: angles, partial frames, action-context only — no beauty-pass face framing before S9; S9's mirror/match coverage may then assert the identity plainly",
          "resolved_from": "how literally identical Maya and A.V.A. read on camera — whether the film has hidden it until now"
        }
      ]
    },
    {
      "event_id": "s09.e04",
      "source_evidence": [
        "How formal is the rest of the dinner?",
        "Dessert, toasts, the donor pitch for the children's hospital — wait. No. Maya. No.",
        "Maya is already pulling the evening wrap off A.V.A.'s shoulders.",
        "Same face. Same voice — I wrote her phoneme table off my own larynx. The cadence I can do. Get her to the service dock, keep anyone off this corridor, and when I signal, wheel her out as if she finished meditating.",
        "You're going to walk in there and pretend to be a robot.",
        "I built her. I know exactly how she walks.",
        "That's what worries me."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the heist pitch in miniature — the plan described as stage directions while she undresses the android; Jim's 'No. Maya. No.' is the audience's objection said for them",
      "participants": [
        "MAYA",
        "JIM",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "service corridor"
      },
      "timeline": [
        {
          "beat": "'How formal is the rest of the dinner?' — the plan already forming",
          "type": "dialogue"
        },
        {
          "beat": "'Dessert, toasts, the donor pitch — wait. No. Maya. No.'",
          "type": "dialogue"
        },
        {
          "beat": "the evening wrap comes off A.V.A.'s shoulders",
          "type": "action"
        },
        {
          "beat": "'Same face. Same voice' — the plan as instructions: dock, corridor, signal",
          "type": "dialogue"
        },
        {
          "beat": "'You're going to walk in there and pretend to be a robot.'",
          "type": "dialogue"
        },
        {
          "beat": "'I built her. I know exactly how she walks.'",
          "type": "dialogue"
        },
        {
          "beat": "'That's what worries me.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the wrap transfer is the costume change the rest of the film depends on — the swap must be readable as a decision, not a stunt",
        "two tempos: Jim's dread accelerating against Maya's already-committed calm"
      ],
      "audio_requirements": [
        "the fabric of the evening wrap coming off"
      ],
      "continuity_constraints": [
        "the wrap becomes Maya-as-A.V.A.'s costume through the end of the scene and into S10",
        "'when I signal, wheel her out as if she finished meditating' — the cover story that S10's debrief confirms held"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "JIM",
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s09.sh05",
        "s09.sh06",
        "s09.sh07"
      ]
    },
    {
      "event_id": "s09.e05",
      "source_evidence": [
        "INT. DINING ROOM — LATER. MAYA enters in A.V.A.'s wrap — shoulders back, glide-step perfect, smile of textbook precision.",
        "She takes her seat. The table barely notices the switch."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the performance begins — the fraud walking on two feet; the tension engine for the rest of the scene is 'when does someone notice'",
      "participants": [
        "MAYA",
        "GUESTS",
        "DAMIEN",
        "DONOR'S WIFE"
      ],
      "remote_participants": [],
      "location": {
        "zone": "dining room"
      },
      "timeline": [
        {
          "beat": "Maya enters in A.V.A.'s wrap — shoulders back, glide-step perfect, textbook smile",
          "type": "action"
        },
        {
          "beat": "she takes her seat",
          "type": "action"
        },
        {
          "beat": "the table barely notices the switch",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "the glide-step must read machine-perfect — her body's thesis statement, not an impression",
        "'barely notices' is the indictment — the room's inattention is what makes the swap possible"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "she wears the wrap taken off A.V.A.'s shoulders in e04 — the costume continuity is the deception"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s09.sh08",
        "s09.sh09"
      ]
    },
    {
      "event_id": "s09.e06",
      "source_evidence": [
        "Welcome back, dear. We were saying the children need a new wing.",
        "A cardiac wing. Damien — the foundation's last imaging suite is four years behind spec. The hospital's director is at this table and too polite to say it. You could fund the wing before dessert and still have time to look reluctant about it.",
        "A beat of silence. Then the hospital director laughs — really laughs. Damien studies \"the android\" with new interest.",
        "She's never been direct before. She's usually... statistical.",
        "Post-charge recalibration. Warm mode. Flagging it as a beta feature.",
        "Keep it."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the performance pays — Maya-as-A.V.A. does what the product never could: names the room's hypocrisy and gets a hospital funded; Damien's interest turns",
      "participants": [
        "MAYA",
        "DONOR'S WIFE",
        "DAMIEN",
        "GUESTS"
      ],
      "remote_participants": [],
      "location": {
        "zone": "dining room"
      },
      "timeline": [
        {
          "beat": "'Welcome back, dear' — the children need a new wing",
          "type": "dialogue"
        },
        {
          "beat": "'A cardiac wing' — the pitch that names the room",
          "type": "dialogue"
        },
        {
          "beat": "a beat of silence — then the hospital director really laughs",
          "type": "held_reaction"
        },
        {
          "beat": "Damien studies 'the android' with new interest",
          "type": "reaction"
        },
        {
          "beat": "'She's never been direct before. She's usually... statistical.'",
          "type": "dialogue"
        },
        {
          "beat": "'Post-charge recalibration. Warm mode. Flagging it as a beta feature.'",
          "type": "dialogue"
        },
        {
          "beat": "'Keep it.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the cardiac-wing pitch must sound nothing like the demo's 'statistical' register — Maya's own directness leaking through the disguise",
        "the hospital director's laugh is a real laugh in a room of polite ones — the table's one honest person"
      ],
      "audio_requirements": [
        "the director's real laugh breaking through table politeness"
      ],
      "continuity_constraints": [
        "'warm mode' is the excuse Maya invents on the spot — it becomes product vocabulary (recurs in S30's 'Warm mode. Dance.')"
      ],
      "ambiguities": [
        "the hospital's director is an unnamed member of the table — modeled inside GUESTS; flag for director if she needs a named role"
      ],
      "must_appear": [
        "MAYA",
        "DAMIEN",
        "DONOR'S WIFE"
      ],
      "tableau": false,
      "shot_sequence": [
        "s09.sh10",
        "s09.sh11",
        "s09.sh12",
        "s09.snd01"
      ]
    },
    {
      "event_id": "s09.e07",
      "source_evidence": [
        "The toasts begin. Damien raises his glass and delivers, dry as paper: \"To the donors — whose generosity is exceeded only by their need for tax instruments.\" Polite, cold laughter.",
        "And from Maya — a real laugh, arriving a half-beat late, like it was buffering."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the tell — her laugh arrives human and half a beat late; the machine's daughter is more alive than the room, and only that gives her away",
      "participants": [
        "DAMIEN",
        "MAYA",
        "GUESTS"
      ],
      "remote_participants": [],
      "location": {
        "zone": "dining room"
      },
      "timeline": [
        {
          "beat": "the toasts begin — Damien raises his glass",
          "type": "action"
        },
        {
          "beat": "the toast — generosity exceeded only by the need for tax instruments",
          "type": "dialogue"
        },
        {
          "beat": "polite, cold laughter",
          "type": "reaction"
        },
        {
          "beat": "from Maya — a real laugh, a half-beat late, like it was buffering",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "two laughs for contrast — the room's cold currency laugh against her one warm, late one",
        "the half-beat lateness is readable as buffering only because she has been performing 'machine' all evening"
      ],
      "audio_requirements": [
        "polite cold laughter against one real laugh"
      ],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s09.sh13",
        "s09.sh14",
        "s09.snd01"
      ]
    },
    {
      "event_id": "s09.e08",
      "source_evidence": [
        "Damien turns. Studies her.",
        "You laughed at my joke.",
        "It was... funny.",
        "On a delay. Like it was buffering.",
        "Processing humor involves a lookup table. The table has... latency.",
        "I'll put a ticket in with IT."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "inspection under pressure — Damien probes the anomaly, Maya patches her cover with the right vocabulary, and Jim closes the breach; attraction disguised as QA",
      "participants": [
        "DAMIEN",
        "MAYA",
        "JIM"
      ],
      "remote_participants": [],
      "location": {
        "zone": "dining room"
      },
      "timeline": [
        {
          "beat": "Damien turns — studies her",
          "type": "action"
        },
        {
          "beat": "'You laughed at my joke.'",
          "type": "dialogue"
        },
        {
          "beat": "'It was... funny.'",
          "type": "dialogue"
        },
        {
          "beat": "'On a delay. Like it was buffering.'",
          "type": "dialogue"
        },
        {
          "beat": "'Processing humor involves a lookup table. The table has... latency.'",
          "type": "dialogue"
        },
        {
          "beat": "'I'll put a ticket in with IT.' — Jim closing the breach",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Damien's study is interest mislabeled as inspection — he is looking at her the way he has not looked at the product",
        "Maya's recovery is pure engineering vocabulary — latency, lookup table; the disguise repairs itself in jargon"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "Jim returns with a tray — he has already executed the service-dock leg of the plan from e04"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "MAYA",
        "JIM"
      ],
      "tableau": false,
      "shot_sequence": [
        "s09.sh15",
        "s09.sh16"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s09.sh01",
      "size": "M",
      "zone": "service corridor",
      "type": "visual",
      "participants": [
        "MAYA",
        "JIM",
        "A.V.A."
      ],
      "implements": [
        "s09.e01"
      ],
      "covers_beats": {
        "s09.e01": [
          0,
          1
        ]
      },
      "purpose": "the haul — Maya and Jim carry her rigid, still-smiling body down the corridor behind a screen of catering trays",
      "audio_note": "corridor hush, the party audible only through the door"
    },
    {
      "shot_id": "s09.sh02",
      "size": "two-shot",
      "zone": "service corridor",
      "type": "visual",
      "participants": [
        "MAYA",
        "JIM",
        "A.V.A."
      ],
      "implements": [
        "s09.e02"
      ],
      "covers_beats": {
        "s09.e02": [
          0,
          1
        ]
      },
      "purpose": "triage over the body — 'she burned it in ninety minutes' / 'dock her... the table thinks she's praying'",
      "dialogue_lines": [
        {
          "event_id": "s09.e02",
          "speaker": "MAYA",
          "line": "Battery was supposed to hold four hours. She burned it in ninety minutes — dinner party load is triple what I modeled.",
          "line_kind": "on_camera",
          "recipient": "JIM",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s09.e02",
          "speaker": "JIM",
          "line": "So dock her. Charge her. The table thinks she's praying.",
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
      "shot_id": "s09.sh03",
      "size": "CU",
      "zone": "service corridor",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s09.e02"
      ],
      "covers_beats": {
        "s09.e02": [
          2
        ]
      },
      "purpose": "the deadline stack — six hours to dock, ninety minutes of dinner, eleven weeks of lab. 'Ten, now.'",
      "dialogue_lines": [
        {
          "event_id": "s09.e02",
          "speaker": "MAYA",
          "line": "Docking takes six hours. The dinner has ninety minutes left and Victor's buyers are photographing her like a showroom. If the prototype bricks on night one, Cross voids the contract and my lab dies in eleven weeks. Ten, now.",
          "line_kind": "on_camera",
          "recipient": "JIM",
          "recipient_presence": "offscreen",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s09.sh04",
      "size": "M+INS",
      "zone": "service corridor",
      "type": "visual",
      "participants": [
        "MAYA",
        "A.V.A."
      ],
      "implements": [
        "s09.e03"
      ],
      "covers_beats": {
        "s09.e03": [
          0,
          1
        ]
      },
      "purpose": "she looks at the frozen android — and at the identical face in the steel reflection. The face A.V.A. was built from. Hers.",
      "audio_note": "corridor hush"
    },
    {
      "shot_id": "s09.sh05",
      "size": "two-shot",
      "zone": "service corridor",
      "type": "visual",
      "participants": [
        "JIM",
        "MAYA"
      ],
      "implements": [
        "s09.e04"
      ],
      "covers_beats": {
        "s09.e04": [
          0,
          1
        ]
      },
      "purpose": "'How formal is the rest of the dinner?' → Jim's inventory curdles into 'wait. No. Maya. No.'",
      "dialogue_lines": [
        {
          "event_id": "s09.e04",
          "speaker": "MAYA",
          "line": "How formal is the rest of the dinner?",
          "line_kind": "on_camera",
          "recipient": "JIM",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s09.e04",
          "speaker": "JIM",
          "line": "Dessert, toasts, the donor pitch for the children's hospital — wait. No. Maya. No.",
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
      "shot_id": "s09.sh06",
      "size": "CU/INS",
      "zone": "service corridor",
      "type": "visual",
      "participants": [
        "MAYA",
        "A.V.A."
      ],
      "implements": [
        "s09.e04"
      ],
      "covers_beats": {
        "s09.e04": [
          2
        ]
      },
      "purpose": "the evening wrap comes off A.V.A.'s shoulders — the costume change that starts the heist",
      "audio_note": "fabric of the evening wrap coming off"
    },
    {
      "shot_id": "s09.sh07",
      "size": "two-shot",
      "zone": "service corridor",
      "type": "visual",
      "participants": [
        "MAYA",
        "JIM"
      ],
      "implements": [
        "s09.e04"
      ],
      "covers_beats": {
        "s09.e04": [
          3,
          4,
          5,
          6
        ]
      },
      "purpose": "'Same face. Same voice' — the plan as instructions → 'pretend to be a robot' → 'I know exactly how she walks' → 'That's what worries me.'",
      "dialogue_lines": [
        {
          "event_id": "s09.e04",
          "speaker": "MAYA",
          "line": "Same face. Same voice — I wrote her phoneme table off my own larynx. The cadence I can do. Get her to the service dock, keep anyone off this corridor, and when I signal, wheel her out as if she finished meditating.",
          "line_kind": "on_camera",
          "recipient": "JIM",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        },
        {
          "event_id": "s09.e04",
          "speaker": "JIM",
          "line": "You're going to walk in there and pretend to be a robot.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            4
          ]
        },
        {
          "event_id": "s09.e04",
          "speaker": "MAYA",
          "line": "I built her. I know exactly how she walks.",
          "line_kind": "on_camera",
          "recipient": "JIM",
          "recipient_presence": "physical",
          "beats": [
            5
          ]
        },
        {
          "event_id": "s09.e04",
          "speaker": "JIM",
          "line": "That's what worries me.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            6
          ]
        }
      ]
    },
    {
      "shot_id": "s09.sh08",
      "size": "M",
      "zone": "dining room",
      "type": "visual",
      "participants": [
        "MAYA",
        "GUESTS"
      ],
      "implements": [
        "s09.e05"
      ],
      "covers_beats": {
        "s09.e05": [
          0,
          1
        ]
      },
      "purpose": "the entrance — Maya in A.V.A.'s wrap, glide-step perfect, textbook smile; she takes her seat",
      "audio_note": "dinner walla, quartet continuing"
    },
    {
      "shot_id": "s09.sh09",
      "size": "M",
      "zone": "dining room",
      "type": "visual",
      "participants": [
        "GUESTS",
        "DAMIEN",
        "DONOR'S WIFE"
      ],
      "implements": [
        "s09.e05"
      ],
      "covers_beats": {
        "s09.e05": [
          2
        ]
      },
      "purpose": "the table barely notices the switch — the room's inattention made visible",
      "audio_note": ""
    },
    {
      "shot_id": "s09.sh10",
      "size": "M",
      "zone": "dining room",
      "type": "visual",
      "participants": [
        "DONOR'S WIFE",
        "MAYA"
      ],
      "implements": [
        "s09.e06"
      ],
      "covers_beats": {
        "s09.e06": [
          0,
          1
        ]
      },
      "purpose": "'Welcome back, dear' → the cardiac wing — the pitch that names the room's hypocrisy in product's clothing",
      "dialogue_lines": [
        {
          "event_id": "s09.e06",
          "speaker": "DONOR'S WIFE",
          "line": "Welcome back, dear. We were saying the children need a new wing.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s09.e06",
          "speaker": "MAYA",
          "line": "A cardiac wing. Damien — the foundation's last imaging suite is four years behind spec. The hospital's director is at this table and too polite to say it. You could fund the wing before dessert and still have time to look reluctant about it.",
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
      "shot_id": "s09.sh11",
      "size": "M",
      "zone": "dining room",
      "type": "visual",
      "participants": [
        "GUESTS",
        "DAMIEN",
        "MAYA"
      ],
      "implements": [
        "s09.e06"
      ],
      "covers_beats": {
        "s09.e06": [
          2,
          3
        ]
      },
      "purpose": "the held silence → the hospital director really laughs → Damien studies 'the android' with new interest",
      "audio_note": "the director's real laugh breaking through table politeness"
    },
    {
      "shot_id": "s09.sh12",
      "size": "two-shot",
      "zone": "dining room",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "implements": [
        "s09.e06"
      ],
      "covers_beats": {
        "s09.e06": [
          4,
          5,
          6
        ]
      },
      "purpose": "'usually... statistical' → 'Post-charge recalibration. Warm mode.' → 'Keep it.'",
      "dialogue_lines": [
        {
          "event_id": "s09.e06",
          "speaker": "DAMIEN",
          "line": "She's never been direct before. She's usually... statistical.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            4
          ]
        },
        {
          "event_id": "s09.e06",
          "speaker": "MAYA",
          "line": "Post-charge recalibration. Warm mode. Flagging it as a beta feature.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            5
          ]
        },
        {
          "event_id": "s09.e06",
          "speaker": "DAMIEN",
          "line": "Keep it.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            6
          ]
        }
      ]
    },
    {
      "shot_id": "s09.sh13",
      "size": "M",
      "zone": "dining room",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "GUESTS"
      ],
      "implements": [
        "s09.e07"
      ],
      "covers_beats": {
        "s09.e07": [
          0,
          1,
          2
        ]
      },
      "purpose": "the toast — dry as paper, generosity vs tax instruments; the room answers with polite, cold laughter",
      "audio_note": "polite, cold laughter",
      "dialogue_lines": [
        {
          "event_id": "s09.e07",
          "speaker": "DAMIEN",
          "line": "To the donors — whose generosity is exceeded only by their need for tax instruments.",
          "line_kind": "on_camera",
          "recipient": "GUESTS",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s09.sh14",
      "size": "CU",
      "zone": "dining room",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s09.e07"
      ],
      "covers_beats": {
        "s09.e07": [
          3
        ]
      },
      "purpose": "from Maya — a real laugh, arriving a half-beat late, like it was buffering",
      "audio_note": "one real laugh, half a beat late"
    },
    {
      "shot_id": "s09.sh15",
      "size": "two-shot",
      "zone": "dining room",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "implements": [
        "s09.e08"
      ],
      "covers_beats": {
        "s09.e08": [
          0,
          1,
          2,
          3,
          4
        ]
      },
      "purpose": "Damien turns and studies her → the laugh interrogation → 'the table has... latency' — the cover repairs itself in jargon",
      "dialogue_lines": [
        {
          "event_id": "s09.e08",
          "speaker": "DAMIEN",
          "line": "You laughed at my joke.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s09.e08",
          "speaker": "MAYA",
          "line": "It was... funny.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s09.e08",
          "speaker": "DAMIEN",
          "line": "On a delay. Like it was buffering.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        },
        {
          "event_id": "s09.e08",
          "speaker": "MAYA",
          "line": "Processing humor involves a lookup table. The table has... latency.",
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
      "shot_id": "s09.sh16",
      "size": "M",
      "zone": "dining room",
      "type": "visual",
      "participants": [
        "JIM",
        "DAMIEN"
      ],
      "implements": [
        "s09.e08"
      ],
      "covers_beats": {
        "s09.e08": [
          5
        ]
      },
      "purpose": "Jim appears with a tray and files the cover story — 'I'll put a ticket in with IT.'",
      "dialogue_lines": [
        {
          "event_id": "s09.e08",
          "speaker": "JIM",
          "line": "I'll put a ticket in with IT.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            5
          ]
        }
      ]
    },
    {
      "shot_id": "s09.snd01",
      "type": "sound",
      "implements": [
        "s09.e01",
        "s09.e06",
        "s09.e07"
      ],
      "purpose": "sound card: corridor hush with party bleed through the door; inside the dining room — the hospital director's one real laugh breaking table politeness, then cold laughter against Maya's warm late one",
      "audio_note": "corridor hush, party audible through the door, the director's real laugh, polite cold laughter, one real laugh a half-beat late",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "haul A.V.A.'s rigid body into the service corridor",
      "disposition": "covered_by",
      "by": [
        "s09.e01"
      ]
    },
    {
      "span": "a procession of lies and catering trays",
      "disposition": "covered_by",
      "by": [
        "s09.e01"
      ]
    },
    {
      "span": "She burned it in ninety minutes",
      "disposition": "covered_by",
      "by": [
        "s09.e02"
      ]
    },
    {
      "span": "The table thinks she's praying.",
      "disposition": "covered_by",
      "by": [
        "s09.e02"
      ]
    },
    {
      "span": "my lab dies in eleven weeks. Ten, now.",
      "disposition": "covered_by",
      "by": [
        "s09.e02"
      ]
    },
    {
      "span": "the identical face in the corridor's steel reflection",
      "disposition": "covered_by",
      "by": [
        "s09.e03"
      ]
    },
    {
      "span": "the face A.V.A. was built from. Hers.",
      "disposition": "covered_by",
      "by": [
        "s09.e03"
      ]
    },
    {
      "span": "How formal is the rest of the dinner?",
      "disposition": "covered_by",
      "by": [
        "s09.e04"
      ]
    },
    {
      "span": "the donor pitch for the children's hospital — wait. No. Maya. No.",
      "disposition": "covered_by",
      "by": [
        "s09.e04"
      ]
    },
    {
      "span": "pulling the evening wrap off A.V.A.'s shoulders",
      "disposition": "covered_by",
      "by": [
        "s09.e04"
      ]
    },
    {
      "span": "I wrote her phoneme table off my own larynx",
      "disposition": "covered_by",
      "by": [
        "s09.e04"
      ]
    },
    {
      "span": "pretend to be a robot",
      "disposition": "covered_by",
      "by": [
        "s09.e04"
      ]
    },
    {
      "span": "I know exactly how she walks.",
      "disposition": "covered_by",
      "by": [
        "s09.e04"
      ]
    },
    {
      "span": "That's what worries me.",
      "disposition": "covered_by",
      "by": [
        "s09.e04"
      ]
    },
    {
      "span": "shoulders back, glide-step perfect, smile of textbook precision",
      "disposition": "covered_by",
      "by": [
        "s09.e05"
      ]
    },
    {
      "span": "The table barely notices the switch.",
      "disposition": "covered_by",
      "by": [
        "s09.e05"
      ]
    },
    {
      "span": "We were saying the children need a new wing.",
      "disposition": "covered_by",
      "by": [
        "s09.e06"
      ]
    },
    {
      "span": "A cardiac wing.",
      "disposition": "covered_by",
      "by": [
        "s09.e06"
      ]
    },
    {
      "span": "the hospital director laughs — really laughs",
      "disposition": "covered_by",
      "by": [
        "s09.e06"
      ]
    },
    {
      "span": "usually... statistical",
      "disposition": "covered_by",
      "by": [
        "s09.e06"
      ]
    },
    {
      "span": "Post-charge recalibration. Warm mode.",
      "disposition": "covered_by",
      "by": [
        "s09.e06"
      ]
    },
    {
      "span": "Keep it.",
      "disposition": "covered_by",
      "by": [
        "s09.e06"
      ]
    },
    {
      "span": "generosity is exceeded only by their need for tax instruments",
      "disposition": "covered_by",
      "by": [
        "s09.e07"
      ]
    },
    {
      "span": "a real laugh, arriving a half-beat late, like it was buffering",
      "disposition": "covered_by",
      "by": [
        "s09.e07"
      ]
    },
    {
      "span": "Damien turns. Studies her.",
      "disposition": "covered_by",
      "by": [
        "s09.e08"
      ]
    },
    {
      "span": "You laughed at my joke.",
      "disposition": "covered_by",
      "by": [
        "s09.e08"
      ]
    },
    {
      "span": "It was... funny.",
      "disposition": "covered_by",
      "by": [
        "s09.e08"
      ]
    },
    {
      "span": "Like it was buffering.",
      "disposition": "covered_by",
      "by": [
        "s09.e08"
      ]
    },
    {
      "span": "The table has... latency.",
      "disposition": "covered_by",
      "by": [
        "s09.e08"
      ]
    },
    {
      "span": "I'll put a ticket in with IT.",
      "disposition": "covered_by",
      "by": [
        "s09.e08"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['MAYA', 'JIM'] | -  | MAYA and JIM haul A.V.A.'s rigid body into the service corridor off the kitchen 
i02 blk=['MAYA', 'JIM'] | MAYA Battery was supposed to hold four hours. She burned it in ni | MAYA faces JIM and speaks.
i03 blk=['JIM'] | JIM So dock her. Charge her. The table thinks she's praying. | JIM faces MAYA and speaks.
i04 blk=['MAYA'] | MAYA Docking takes six hours. The dinner has ninety minutes left  | MAYA faces JIM and speaks.
i05 blk=['JIM'] | -  | She looks at the frozen android. At the identical face in the corridor's steel r
i06 blk=['JIM', 'MAYA'] | MAYA How formal is the rest of the dinner? | MAYA faces JIM and speaks.
i07 blk=['JIM', 'MAYA'] | JIM Dessert, toasts, the donor pitch for the children's hospital | JIM faces MAYA and speaks.
i08 blk=['MAYA'] | MAYA Same face. Same voice — I wrote her phoneme table off my own | Maya is already pulling the evening wrap off A.V.A.'s shoulders.
i09 blk=['JIM'] | JIM You're going to walk in there and pretend to be a robot. | JIM faces MAYA and speaks.
i10 blk=['MAYA', 'JIM'] | MAYA I built her. I know exactly how she walks. | MAYA faces JIM and speaks.
i11 blk=['JIM'] | JIM That's what worries me. | JIM faces MAYA and speaks.
i12 blk=['MAYA'] | -  | INT. DINING ROOM — LATER. MAYA enters in A.V.A.'s wrap — shoulders back, glide-s
i13 blk=["DONOR'S WIFE", 'MAYA'] | DONOR'S WIFE Welcome back, dear. We were saying the children need a new w | DONOR'S WIFE faces MAYA and speaks.
i14 blk=['MAYA'] | MAYA A cardiac wing. Damien — the foundation's last imaging suite | MAYA faces JIM and speaks.
i15 blk=['DAMIEN'] | -  | A beat of silence. Then the hospital director laughs — really laughs. Damien stu
i16 blk=['MAYA', 'DAMIEN'] | DAMIEN She's never been direct before. She's usually... statistical | DAMIEN faces MAYA and speaks.
i17 blk=['MAYA'] | MAYA Post-charge recalibration. Warm mode. Flagging it as a beta  | MAYA faces JIM and speaks.
i18 blk=['DAMIEN'] | DAMIEN Keep it. | DAMIEN faces MAYA and speaks.
i19 blk=['DAMIEN', 'MAYA'] | -  | The toasts begin. Damien raises his glass and delivers, dry as paper: Polite, co
i20 blk=['DAMIEN', 'MAYA'] | DAMIEN You laughed at my joke. | Damien turns. Studies her.
i21 blk=['MAYA'] | MAYA It was... funny. | MAYA faces JIM and speaks.
i22 blk=['DAMIEN'] | DAMIEN On a delay. Like it was buffering. | DAMIEN faces MAYA and speaks.
i23 blk=['MAYA'] | MAYA Processing humor involves a lookup table. The table has... l | MAYA faces JIM and speaks.
i24 blk=['MAYA', 'JIM'] | JIM I'll put a ticket in with IT. | JIM faces MAYA and speaks.