# VALIDATION PACKET — scene s04
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 4 — INT. VOLT ROBOTICS LAB — DAY

*A startup lab that runs on ramen, genius and denial. Soldering
stations, half-built limbs on racks, a whiteboard of equations and a
calendar where every third date says INVOICE DUE.*

*MAYA LIND — 25, sleeves rolled, soldering iron behind one ear like a
pencil — leads VICTOR past a workbench where a figure sits under a
sheet. J-7, an ancient butler-shaped unit, follows at a dignified
distance, carrying coffee he cannot drink.*

MAYA
Volt's runway is eleven weeks. Which is a problem because the A.V.A.
program needs fourteen. So when your office called —

VICTOR
You answered on the first ring. I heard.

MAYA
She's a beta. Emotional interface, social calibration, full motor
suite, self-directed learning. She's the most advanced companion-class
unit ever—

*Victor pulls the sheet. A.V.A. sits there — a beautiful, still woman
in a matte-grey chassis gown. Her eyes open. She scans the room,
settles on Victor, and produces a smile of textbook precision.*

A.V.A.
Good afternoon. You are Victor Cross. Your smile indicates deceit.
Confidence: ninety-six percent.

*Dead silence.*

A.V.A. (CONT'D)
The remaining four percent accounts for the possibility that this is
simply how your face is.

*Maya closes her eyes. J-7, from the doorway, sets the coffee down
very quietly.*

J-7
She also tells the truth. We're working on the sequencing.

VICTOR
(delighted)
She's perfect. Broken, but perfect. Contract's already drafted —
delivery to my brother's residence Friday.

MAYA
Friday?! She needs three more weeks of social tuning, she blurts
statistical diagnoses at dinner parties—

VICTOR
Friday. Or I find a lab that's less honest about its flaws.

*Maya looks at the INVOICE DUE calendar. At A.V.A., who has tilted
her head and is cataloguing Victor's shoes.*

A.V.A.
Your footwear is Italian and resoled twice. You buy expensive things
and keep them past their value. Sentimental or leveraged?

VICTOR
Friday.

MAYA
She doesn't have a certified dock profile. She'd ship at
half charge — the battery curve is still a rumor—

VICTOR
It's a gift, not a lease. Wrap her.

*He goes. Maya stares at A.V.A. Then, quietly, she uncaps a
marker and writes on a QUICK START card before slipping it
into the crate sleeve:*

*"If your unit seems too honest — that is the product.
Warranty line below. -- M."*

A.V.A.
Did I do well?

MAYA
You diagnosed a client's morality from his shoes.

A.V.A.
Ninety-six percent.

J-7
She gets it from you.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 4,
  "scene_heading": "INT. VOLT ROBOTICS LAB — DAY",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "A.V.A.'s first scene alive: Maya shows Victor the beta unit because Volt's runway is eleven weeks and the program needs fourteen. A.V.A. wakes, scans the buyer, and diagnoses his deceit at ninety-six percent confidence — the lab's flaw and its miracle in one sentence. Victor orders her shipped Friday at half charge; Maya's handwritten QUICK START card ('that is the product. -- M.') is the film's first act of protection and the seed of every later misunderstanding.",
  "zones": [
    "volt lab"
  ],
  "events": [
    {
      "event_id": "s04.e01",
      "source_evidence": [
        "A startup lab that runs on ramen, genius and denial. Soldering stations, half-built limbs on racks, a whiteboard of equations and a calendar where every third date says INVOICE DUE.",
        "MAYA LIND — 25, sleeves rolled, soldering iron behind one ear like a pencil — leads VICTOR past a workbench where a figure sits under a sheet.",
        "J-7, an ancient butler-shaped unit, follows at a dignified distance, carrying coffee he cannot drink.",
        "Volt's runway is eleven weeks. Which is a problem because the A.V.A. program needs fourteen. So when your office called —",
        "You answered on the first ring. I heard.",
        "She's a beta. Emotional interface, social calibration, full motor suite, self-directed learning. She's the most advanced companion-class unit ever—"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the lab and its desperation established — Maya sells the beta because the runway math leaves no choice",
      "participants": [
        "MAYA",
        "VICTOR",
        "J-7",
        "A.V.A."
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "location": {
        "zone": "volt lab"
      },
      "timeline": [
        {
          "beat": "the lab — ramen, genius and denial; soldering stations, racked limbs, the INVOICE DUE calendar",
          "type": "atmosphere"
        },
        {
          "beat": "the tour — Maya leads Victor past the sheeted figure; J-7 follows with coffee he cannot drink",
          "type": "action"
        },
        {
          "beat": "'eleven weeks of runway — the program needs fourteen'",
          "type": "dialogue"
        },
        {
          "beat": "'You answered on the first ring. I heard.'",
          "type": "dialogue"
        },
        {
          "beat": "the beta pitch — emotional interface, self-directed learning, 'the most advanced companion-class unit ever—'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the INVOICE DUE calendar is a planted prop — it pays off the moment Maya looks at it in e05",
        "the sheeted figure is in frame before anyone names her — presence before reveal",
        "J-7's coffee he cannot drink is his whole character in one gesture"
      ],
      "audio_requirements": [
        "lab room tone — solder fans, an idle unit's hum"
      ],
      "continuity_constraints": [
        "eleven-vs-fourteen weeks is why Maya cannot refuse — the desperation must be legible before the reveal"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "VICTOR"
      ],
      "tableau": true,
      "shot_sequence": [
        "s04.sh01",
        "s04.sh02",
        "s04.snd01"
      ]
    },
    {
      "event_id": "s04.e02",
      "source_evidence": [
        "Victor pulls the sheet. A.V.A. sits there — a beautiful, still woman in a matte-grey chassis gown. Her eyes open. She scans the room, settles on Victor, and produces a smile of textbook precision.",
        "Good afternoon. You are Victor Cross. Your smile indicates deceit. Confidence: ninety-six percent.",
        "Dead silence.",
        "The remaining four percent accounts for the possibility that this is simply how your face is."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the unveiling — the product wakes and immediately tells the buyer the truth nobody else would",
      "participants": [
        "VICTOR",
        "A.V.A.",
        "MAYA",
        "J-7"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "J-7"
      ],
      "location": {
        "zone": "volt lab"
      },
      "timeline": [
        {
          "beat": "Victor pulls the sheet — A.V.A. unveiled, matte-grey chassis gown",
          "type": "reveal"
        },
        {
          "beat": "eyes open, the room scanned, Victor selected — a smile of textbook precision",
          "type": "action"
        },
        {
          "beat": "'Your smile indicates deceit. Confidence: ninety-six percent.'",
          "type": "dialogue"
        },
        {
          "beat": "dead silence",
          "type": "held_reaction"
        },
        {
          "beat": "'the remaining four percent — this is simply how your face is'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the textbook-precision smile must be flawless and wrong — precision without warmth",
        "the silence after the diagnosis is a held beat — nobody rescues it"
      ],
      "audio_requirements": [
        "the dead silence after the diagnosis — even the lab goes quiet"
      ],
      "continuity_constraints": [
        "ninety-six percent is her signature number — it recurs at the end of the scene and through the film"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A.",
        "VICTOR"
      ],
      "tableau": true,
      "shot_sequence": [
        "s04.sh03",
        "s04.sh04",
        "s04.sh05",
        "s04.sh06",
        "s04.snd01"
      ]
    },
    {
      "event_id": "s04.e03",
      "source_evidence": [
        "Maya closes her eyes. J-7, from the doorway, sets the coffee down very quietly.",
        "She also tells the truth. We're working on the sequencing."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "damage assessment — Maya's private despair and J-7's deadpan defense of his successor",
      "participants": [
        "MAYA",
        "J-7",
        "VICTOR",
        "A.V.A."
      ],
      "remote_participants": [],
      "offscreen_present": [
        "VICTOR",
        "A.V.A."
      ],
      "location": {
        "zone": "volt lab"
      },
      "timeline": [
        {
          "beat": "Maya closes her eyes",
          "type": "reaction"
        },
        {
          "beat": "J-7 sets the coffee down very quietly",
          "type": "action"
        },
        {
          "beat": "'She also tells the truth. We're working on the sequencing.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "J-7's apology is delivered to the room, not to Victor — an old unit defending a new one"
      ],
      "audio_requirements": [
        "the coffee set down very quietly — porcelain apology"
      ],
      "continuity_constraints": [
        "'the sequencing' names the flaw honestly — she tells the truth before she learns tact"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "J-7"
      ],
      "tableau": false,
      "shot_sequence": [
        "s04.sh07",
        "s04.sh08",
        "s04.snd01"
      ]
    },
    {
      "event_id": "s04.e04",
      "source_evidence": [
        "She's perfect. Broken, but perfect. Contract's already drafted — delivery to my brother's residence Friday.",
        "Friday?! She needs three more weeks of social tuning, she blurts statistical diagnoses at dinner parties—",
        "Friday. Or I find a lab that's less honest about its flaws."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the sale forced — Victor reads the flaw as the feature and sets Friday as the price of honesty",
      "participants": [
        "VICTOR",
        "MAYA",
        "A.V.A.",
        "J-7"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "A.V.A.",
        "J-7"
      ],
      "location": {
        "zone": "volt lab"
      },
      "timeline": [
        {
          "beat": "'She's perfect. Broken, but perfect. — delivery Friday.'",
          "type": "dialogue"
        },
        {
          "beat": "'Friday?! She needs three more weeks — she blurts statistical diagnoses at dinner parties—'",
          "type": "dialogue"
        },
        {
          "beat": "'Friday. Or I find a lab that's less honest about its flaws.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Victor's delight is genuine — he is buying the flaw on purpose, and that is the joke underneath the threat"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "delivery Friday at the brother's residence is the S5 crate — the deadline is fixed here"
      ],
      "ambiguities": [],
      "must_appear": [
        "VICTOR",
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s04.sh09",
        "s04.sh10",
        "s04.sh11"
      ]
    },
    {
      "event_id": "s04.e05",
      "source_evidence": [
        "Maya looks at the INVOICE DUE calendar. At A.V.A., who has tilted her head and is cataloguing Victor's shoes.",
        "Your footwear is Italian and resoled twice. You buy expensive things and keep them past their value. Sentimental or leveraged?",
        "Friday.",
        "She doesn't have a certified dock profile. She'd ship at half charge — the battery curve is still a rumor—",
        "It's a gift, not a lease. Wrap her."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the terms dictated over Maya's last objections — A.V.A. keeps diagnosing, the calendar keeps dunning, and 'wrap her' ends the negotiation",
      "participants": [
        "MAYA",
        "VICTOR",
        "A.V.A.",
        "J-7"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "J-7"
      ],
      "location": {
        "zone": "volt lab"
      },
      "timeline": [
        {
          "beat": "the INVOICE DUE calendar — every third date",
          "type": "insert"
        },
        {
          "beat": "A.V.A. tilts her head — cataloguing Victor's shoes",
          "type": "action"
        },
        {
          "beat": "the footwear diagnosis — 'Sentimental or leveraged?'",
          "type": "dialogue"
        },
        {
          "beat": "'Friday.'",
          "type": "dialogue"
        },
        {
          "beat": "'half charge — the battery curve is still a rumor—'",
          "type": "dialogue"
        },
        {
          "beat": "'It's a gift, not a lease. Wrap her.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the calendar insert answers Maya's objection before she makes it — money decides, not engineering",
        "A.V.A.'s shoe catalogue is the demonstration Victor is enjoying — her head-tilt is curiosity, not malfunction"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "'ship at half charge' is the title and the film's battery motif — first statement of the charge problem",
        "'It's a gift' is the framing Victor repeats on the wallscreen in S5 — keep the word exact"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A.",
        "VICTOR",
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s04.sh12",
        "s04.sh13",
        "s04.sh14",
        "s04.sh15",
        "s04.sh16"
      ]
    },
    {
      "event_id": "s04.e06",
      "source_evidence": [
        "He goes. Maya stares at A.V.A. Then, quietly, she uncaps a marker and writes on a QUICK START card before slipping it into the crate sleeve:",
        "\"If your unit seems too honest — that is the product. Warranty line below. -- M.\"",
        "Did I do well?",
        "You diagnosed a client's morality from his shoes.",
        "Ninety-six percent.",
        "She gets it from you."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the card and the coda — Maya writes the one instruction that will save and complicate everything, then the two machines and their maker assess the afternoon",
      "participants": [
        "VICTOR",
        "MAYA",
        "A.V.A.",
        "J-7"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "document_evidence": [
        {
          "author": "MAYA",
          "artifact": "QUICK START card — 'If your unit seems too honest — that is the product. Warranty line below. -- M.'",
          "channel": "document"
        }
      ],
      "location": {
        "zone": "volt lab"
      },
      "timeline": [
        {
          "beat": "Victor goes",
          "type": "action"
        },
        {
          "beat": "Maya stares at A.V.A., then quietly uncaps a marker — writes the QUICK START card, slips it into the crate sleeve",
          "type": "action"
        },
        {
          "beat": "the card — 'If your unit seems too honest — that is the product. Warranty line below. -- M.'",
          "type": "insert"
        },
        {
          "beat": "'Did I do well?'",
          "type": "dialogue"
        },
        {
          "beat": "'You diagnosed a client's morality from his shoes.'",
          "type": "dialogue"
        },
        {
          "beat": "'Ninety-six percent.'",
          "type": "dialogue"
        },
        {
          "beat": "'She gets it from you.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the card is written on camera — the audience must be able to read it, this object carries three later scenes",
        "'Did I do well?' is a child asking its maker — the tenderness is in the flatness"
      ],
      "audio_requirements": [
        "marker uncap and felt scratch on the card"
      ],
      "continuity_constraints": [
        "the card Maya writes here is the card Jim finds in S5 under his own Post-it — same object, two guardians",
        "'-- M.' is her signature — the handwriting is Maya's presence inside the crate"
      ],
      "ambiguities": [
        "a 'crate sleeve' implies the shipping crate is already staged in the lab — the wrap order was seconds old. Flag: staged crate visible in background since e01, or read the sleeve as the packing sleeve of her transit case."
      ],
      "must_appear": [
        "MAYA",
        "A.V.A.",
        "J-7"
      ],
      "tableau": false,
      "shot_sequence": [
        "s04.sh17",
        "s04.sh18",
        "s04.sh19",
        "s04.sh20",
        "s04.sh21",
        "s04.snd01"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s04.sh01",
      "size": "W",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "MAYA",
        "VICTOR",
        "J-7",
        "A.V.A."
      ],
      "implements": [
        "s04.e01"
      ],
      "covers_beats": {
        "s04.e01": [
          0,
          1
        ]
      },
      "purpose": "the lab established — soldering stations, racked limbs, INVOICE DUE calendar; Maya leads Victor past the sheeted figure, J-7 trailing with coffee",
      "audio_note": "lab room tone — solder fans, an idle unit's hum"
    },
    {
      "shot_id": "s04.sh02",
      "size": "M moving",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "MAYA",
        "VICTOR"
      ],
      "implements": [
        "s04.e01"
      ],
      "covers_beats": {
        "s04.e01": [
          2,
          3,
          4
        ]
      },
      "purpose": "the walking pitch — runway math, 'first ring', the beta spec cut off mid-sentence",
      "dialogue_lines": [
        {
          "event_id": "s04.e01",
          "speaker": "MAYA",
          "line": "Volt's runway is eleven weeks. Which is a problem because the A.V.A. program needs fourteen. So when your office called —",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s04.e01",
          "speaker": "VICTOR",
          "line": "You answered on the first ring. I heard.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        },
        {
          "event_id": "s04.e01",
          "speaker": "MAYA",
          "line": "She's a beta. Emotional interface, social calibration, full motor suite, self-directed learning. She's the most advanced companion-class unit ever—",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "physical",
          "beats": [
            4
          ]
        }
      ]
    },
    {
      "shot_id": "s04.sh03",
      "size": "M",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "VICTOR",
        "A.V.A."
      ],
      "implements": [
        "s04.e02"
      ],
      "covers_beats": {
        "s04.e02": [
          0,
          1
        ]
      },
      "purpose": "the sheet pulled — A.V.A. unveiled; eyes open, the room scanned, the textbook-precision smile",
      "audio_note": "fabric slide, her wake tone",
      "dialogue_lines": []
    },
    {
      "shot_id": "s04.sh04",
      "size": "CU",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s04.e02"
      ],
      "covers_beats": {
        "s04.e02": [
          2
        ]
      },
      "purpose": "the first words — 'Your smile indicates deceit. Confidence: ninety-six percent.'",
      "dialogue_lines": [
        {
          "event_id": "s04.e02",
          "speaker": "A.V.A.",
          "line": "Good afternoon. You are Victor Cross. Your smile indicates deceit. Confidence: ninety-six percent.",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "offscreen",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s04.sh05",
      "size": "two-shot",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "VICTOR",
        "MAYA"
      ],
      "implements": [
        "s04.e02"
      ],
      "covers_beats": {
        "s04.e02": [
          3
        ]
      },
      "purpose": "dead silence — Victor absorbing the diagnosis, Maya bracing for the loss of the sale",
      "audio_note": "dead silence — even the lab goes quiet"
    },
    {
      "shot_id": "s04.sh06",
      "size": "CU",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s04.e02"
      ],
      "covers_beats": {
        "s04.e02": [
          4
        ]
      },
      "purpose": "'the remaining four percent — this is simply how your face is'",
      "dialogue_lines": [
        {
          "event_id": "s04.e02",
          "speaker": "A.V.A.",
          "line": "The remaining four percent accounts for the possibility that this is simply how your face is.",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "offscreen",
          "beats": [
            4
          ]
        }
      ]
    },
    {
      "shot_id": "s04.sh07",
      "size": "CU",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s04.e03"
      ],
      "covers_beats": {
        "s04.e03": [
          0
        ]
      },
      "purpose": "Maya closes her eyes — the whole fiscal year in one blink",
      "audio_note": "lab tone continuing under"
    },
    {
      "shot_id": "s04.sh08",
      "size": "M",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "J-7"
      ],
      "implements": [
        "s04.e03"
      ],
      "covers_beats": {
        "s04.e03": [
          1,
          2
        ]
      },
      "purpose": "J-7 sets the coffee down very quietly, then files his defense — 'We're working on the sequencing.'",
      "audio_note": "the coffee set down very quietly, J-7's servo",
      "dialogue_lines": [
        {
          "event_id": "s04.e03",
          "speaker": "J-7",
          "line": "She also tells the truth. We're working on the sequencing.",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "offscreen",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s04.sh09",
      "size": "CU",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "implements": [
        "s04.e04"
      ],
      "covers_beats": {
        "s04.e04": [
          0
        ]
      },
      "purpose": "delighted — 'She's perfect. Broken, but perfect.' the contract already drafted",
      "dialogue_lines": [
        {
          "event_id": "s04.e04",
          "speaker": "VICTOR",
          "line": "She's perfect. Broken, but perfect. Contract's already drafted — delivery to my brother's residence Friday.",
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
      "shot_id": "s04.sh10",
      "size": "CU",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s04.e04"
      ],
      "covers_beats": {
        "s04.e04": [
          1
        ]
      },
      "purpose": "'Friday?!' — the engineering objection tumbling out mid-sentence",
      "dialogue_lines": [
        {
          "event_id": "s04.e04",
          "speaker": "MAYA",
          "line": "Friday?! She needs three more weeks of social tuning, she blurts statistical diagnoses at dinner parties—",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "offscreen",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s04.sh11",
      "size": "M",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "implements": [
        "s04.e04"
      ],
      "covers_beats": {
        "s04.e04": [
          2
        ]
      },
      "purpose": "'Friday. Or I find a lab that's less honest about its flaws.' — the threat delivered warmly",
      "dialogue_lines": [
        {
          "event_id": "s04.e04",
          "speaker": "VICTOR",
          "line": "Friday. Or I find a lab that's less honest about its flaws.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "offscreen",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s04.sh12",
      "size": "INS",
      "zone": "volt lab",
      "type": "visual",
      "participants": [],
      "depicts": [
        {
          "object": "the calendar — every third date says INVOICE DUE",
          "channel": "in_frame"
        }
      ],
      "implements": [
        "s04.e05"
      ],
      "covers_beats": {
        "s04.e05": [
          0
        ]
      },
      "purpose": "the INVOICE DUE calendar — the reason Maya cannot say no, in ink",
      "audio_note": "lab tone"
    },
    {
      "shot_id": "s04.sh13",
      "size": "CU",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s04.e05"
      ],
      "covers_beats": {
        "s04.e05": [
          1,
          2
        ]
      },
      "purpose": "the head-tilt and the footwear autopsy — 'Sentimental or leveraged?'",
      "dialogue_lines": [
        {
          "event_id": "s04.e05",
          "speaker": "A.V.A.",
          "line": "Your footwear is Italian and resoled twice. You buy expensive things and keep them past their value. Sentimental or leveraged?",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "offscreen",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s04.sh14",
      "size": "CU",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "implements": [
        "s04.e05"
      ],
      "covers_beats": {
        "s04.e05": [
          3
        ]
      },
      "purpose": "'Friday.' — one word, the whole negotiation",
      "dialogue_lines": [
        {
          "event_id": "s04.e05",
          "speaker": "VICTOR",
          "line": "Friday.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "offscreen",
          "beats": [
            3
          ]
        }
      ]
    },
    {
      "shot_id": "s04.sh15",
      "size": "CU",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s04.e05"
      ],
      "covers_beats": {
        "s04.e05": [
          4
        ]
      },
      "purpose": "the last engineering objection — 'half charge, the battery curve is still a rumor—'",
      "dialogue_lines": [
        {
          "event_id": "s04.e05",
          "speaker": "MAYA",
          "line": "She doesn't have a certified dock profile. She'd ship at half charge — the battery curve is still a rumor—",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "offscreen",
          "beats": [
            4
          ]
        }
      ]
    },
    {
      "shot_id": "s04.sh16",
      "size": "M",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "implements": [
        "s04.e05"
      ],
      "covers_beats": {
        "s04.e05": [
          5
        ]
      },
      "purpose": "'It's a gift, not a lease. Wrap her.' — the order that builds the crate",
      "dialogue_lines": [
        {
          "event_id": "s04.e05",
          "speaker": "VICTOR",
          "line": "It's a gift, not a lease. Wrap her.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "offscreen",
          "beats": [
            5
          ]
        }
      ]
    },
    {
      "shot_id": "s04.sh17",
      "size": "M",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "implements": [
        "s04.e06"
      ],
      "covers_beats": {
        "s04.e06": [
          0
        ]
      },
      "purpose": "Victor goes — the buyer exits with his purchase secured",
      "audio_note": "his footsteps out, lab tone"
    },
    {
      "shot_id": "s04.sh18",
      "size": "M",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "MAYA",
        "A.V.A."
      ],
      "implements": [
        "s04.e06"
      ],
      "covers_beats": {
        "s04.e06": [
          1
        ]
      },
      "purpose": "Maya stares at A.V.A., then quietly uncaps the marker — the card written and slipped into the crate sleeve",
      "audio_note": "marker uncap and felt scratch on the card"
    },
    {
      "shot_id": "s04.sh19",
      "size": "INS",
      "zone": "volt lab",
      "type": "visual",
      "participants": [],
      "depicts": [
        {
          "object": "QUICK START card — 'If your unit seems too honest — that is the product. Warranty line below. -- M.'",
          "channel": "in_frame"
        }
      ],
      "implements": [
        "s04.e06"
      ],
      "covers_beats": {
        "s04.e06": [
          2
        ]
      },
      "purpose": "the card legible — Maya's handwriting, '-- M.'",
      "audio_note": "felt scratch finishing, card slipped into the sleeve"
    },
    {
      "shot_id": "s04.sh20",
      "size": "two-shot",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "A.V.A.",
        "MAYA"
      ],
      "implements": [
        "s04.e06"
      ],
      "covers_beats": {
        "s04.e06": [
          3,
          4,
          5
        ]
      },
      "purpose": "'Did I do well?' / 'You diagnosed a client's morality from his shoes.' / 'Ninety-six percent.' — maker and unit, the coda",
      "dialogue_lines": [
        {
          "event_id": "s04.e06",
          "speaker": "A.V.A.",
          "line": "Did I do well?",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        },
        {
          "event_id": "s04.e06",
          "speaker": "MAYA",
          "line": "You diagnosed a client's morality from his shoes.",
          "line_kind": "on_camera",
          "recipient": "A.V.A.",
          "recipient_presence": "physical",
          "beats": [
            4
          ]
        },
        {
          "event_id": "s04.e06",
          "speaker": "A.V.A.",
          "line": "Ninety-six percent.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            5
          ]
        }
      ]
    },
    {
      "shot_id": "s04.sh21",
      "size": "M",
      "zone": "volt lab",
      "type": "visual",
      "participants": [
        "J-7"
      ],
      "implements": [
        "s04.e06"
      ],
      "covers_beats": {
        "s04.e06": [
          6
        ]
      },
      "purpose": "'She gets it from you.' — the old unit's benediction from the doorway",
      "audio_note": "J-7's servo, lab tone",
      "dialogue_lines": [
        {
          "event_id": "s04.e06",
          "speaker": "J-7",
          "line": "She gets it from you.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "offscreen",
          "beats": [
            6
          ]
        }
      ]
    },
    {
      "shot_id": "s04.snd01",
      "type": "sound",
      "implements": [
        "s04.e01",
        "s04.e02",
        "s04.e03",
        "s04.e06"
      ],
      "purpose": "sound card: lab room tone (solder fans, idle unit hum), the dead silence after the diagnosis, coffee set down very quietly, marker uncap and scratch",
      "audio_note": "lab room tone — solder fans and an idle unit's hum; dead silence after the diagnosis; coffee set down very quietly; marker uncap and felt scratch on the card",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "A startup lab that runs on ramen, genius and denial. Soldering stations, half-built limbs on racks, a whiteboard of equations and a calendar where every third date says INVOICE DUE.",
      "disposition": "covered_by",
      "by": [
        "s04.e01"
      ]
    },
    {
      "span": "MAYA LIND — 25, sleeves rolled, soldering iron behind one ear like a pencil — leads VICTOR past a workbench where a figure sits under a sheet.",
      "disposition": "covered_by",
      "by": [
        "s04.e01"
      ]
    },
    {
      "span": "J-7, an ancient butler-shaped unit, follows at a dignified distance, carrying coffee he cannot drink.",
      "disposition": "covered_by",
      "by": [
        "s04.e01"
      ]
    },
    {
      "span": "Volt's runway is eleven weeks. Which is a problem because the A.V.A. program needs fourteen. So when your office called —",
      "disposition": "covered_by",
      "by": [
        "s04.e01"
      ]
    },
    {
      "span": "You answered on the first ring. I heard.",
      "disposition": "covered_by",
      "by": [
        "s04.e01"
      ]
    },
    {
      "span": "She's a beta. Emotional interface, social calibration, full motor suite, self-directed learning. She's the most advanced companion-class unit ever—",
      "disposition": "covered_by",
      "by": [
        "s04.e01"
      ]
    },
    {
      "span": "Victor pulls the sheet. A.V.A. sits there — a beautiful, still woman in a matte-grey chassis gown. Her eyes open. She scans the room, settles on Victor, and produces a smile of textbook precision.",
      "disposition": "covered_by",
      "by": [
        "s04.e02"
      ]
    },
    {
      "span": "Good afternoon. You are Victor Cross. Your smile indicates deceit. Confidence: ninety-six percent.",
      "disposition": "covered_by",
      "by": [
        "s04.e02"
      ]
    },
    {
      "span": "Dead silence.",
      "disposition": "covered_by",
      "by": [
        "s04.e02"
      ]
    },
    {
      "span": "The remaining four percent accounts for the possibility that this is simply how your face is.",
      "disposition": "covered_by",
      "by": [
        "s04.e02"
      ]
    },
    {
      "span": "Maya closes her eyes. J-7, from the doorway, sets the coffee down very quietly.",
      "disposition": "covered_by",
      "by": [
        "s04.e03"
      ]
    },
    {
      "span": "She also tells the truth. We're working on the sequencing.",
      "disposition": "covered_by",
      "by": [
        "s04.e03"
      ]
    },
    {
      "span": "She's perfect. Broken, but perfect. Contract's already drafted — delivery to my brother's residence Friday.",
      "disposition": "covered_by",
      "by": [
        "s04.e04"
      ]
    },
    {
      "span": "Friday?! She needs three more weeks of social tuning, she blurts statistical diagnoses at dinner parties—",
      "disposition": "covered_by",
      "by": [
        "s04.e04"
      ]
    },
    {
      "span": "Friday. Or I find a lab that's less honest about its flaws.",
      "disposition": "covered_by",
      "by": [
        "s04.e04"
      ]
    },
    {
      "span": "Maya looks at the INVOICE DUE calendar. At A.V.A., who has tilted her head and is cataloguing Victor's shoes.",
      "disposition": "covered_by",
      "by": [
        "s04.e05"
      ]
    },
    {
      "span": "Your footwear is Italian and resoled twice. You buy expensive things and keep them past their value. Sentimental or leveraged?",
      "disposition": "covered_by",
      "by": [
        "s04.e05"
      ]
    },
    {
      "span": "Friday.",
      "disposition": "covered_by",
      "by": [
        "s04.e05"
      ]
    },
    {
      "span": "She doesn't have a certified dock profile. She'd ship at half charge — the battery curve is still a rumor—",
      "disposition": "covered_by",
      "by": [
        "s04.e05"
      ]
    },
    {
      "span": "It's a gift, not a lease. Wrap her.",
      "disposition": "covered_by",
      "by": [
        "s04.e05"
      ]
    },
    {
      "span": "He goes. Maya stares at A.V.A. Then, quietly, she uncaps a marker and writes on a QUICK START card before slipping it into the crate sleeve:",
      "disposition": "covered_by",
      "by": [
        "s04.e06"
      ]
    },
    {
      "span": "\"If your unit seems too honest — that is the product. Warranty line below. -- M.\"",
      "disposition": "covered_by",
      "by": [
        "s04.e06"
      ]
    },
    {
      "span": "Did I do well?",
      "disposition": "covered_by",
      "by": [
        "s04.e06"
      ]
    },
    {
      "span": "You diagnosed a client's morality from his shoes.",
      "disposition": "covered_by",
      "by": [
        "s04.e06"
      ]
    },
    {
      "span": "Ninety-six percent.",
      "disposition": "covered_by",
      "by": [
        "s04.e06"
      ]
    },
    {
      "span": "She gets it from you.",
      "disposition": "covered_by",
      "by": [
        "s04.e06"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['MAYA', 'VICTOR'] | -  | A startup lab that runs on ramen, genius and denial. Soldering stations, half-bu
i02 blk=['MAYA', 'VICTOR'] | -  | MAYA LIND — 25, sleeves rolled, soldering iron behind one ear like a pencil — le
i03 blk=['MAYA', 'VICTOR'] | MAYA Volt's runway is eleven weeks. Which is a problem because th | MAYA faces VICTOR and speaks.
i04 blk=['VICTOR'] | VICTOR You answered on the first ring. I heard. | VICTOR faces MAYA and speaks.
i05 blk=['MAYA'] | MAYA She's a beta. Emotional interface, social calibration, full  | MAYA faces VICTOR and speaks.
i06 blk=['VICTOR'] | -  | Victor pulls the sheet. A.V.A. sits there — a beautiful, still woman in a matte-
i07 blk=['A.V.A.'] | A.V.A. Good afternoon. You are Victor Cross. Your smile indicates d | A.V.A. faces MAYA and speaks.
i08 blk=['MAYA'] | -  | Dead silence.
i09 blk=['J-7', 'A.V.A.'] | A.V.A. The remaining four percent accounts for the possibility that | A.V.A. faces MAYA and speaks.
i10 blk=['J-7'] | J-7 She also tells the truth. We're working on the sequencing. | Maya closes her eyes. J-7, from the doorway, sets the coffee down very quietly.
i11 blk=['VICTOR'] | VICTOR She's perfect. Broken, but perfect. Contract's already draft | VICTOR faces MAYA and speaks.
i12 blk=['MAYA', 'VICTOR'] | MAYA Friday?! She needs three more weeks of social tuning, she bl | MAYA faces VICTOR and speaks.
i13 blk=['VICTOR'] | VICTOR Friday. Or I find a lab that's less honest about its flaws. | VICTOR faces MAYA and speaks.
i14 blk=['VICTOR', 'MAYA'] | -  | Maya looks at the INVOICE DUE calendar. At A.V.A., who has tilted her head and i
i15 blk=['A.V.A.', 'MAYA'] | A.V.A. Your footwear is Italian and resoled twice. You buy expensiv | A.V.A. studies VICTOR's shoes and addresses him; MAYA watches A.V.A.
i16 blk=['MAYA', 'VICTOR'] | VICTOR Friday. | VICTOR faces MAYA and speaks.
i17 blk=['MAYA'] | MAYA She doesn't have a certified dock profile. She'd ship at hal | MAYA faces VICTOR and speaks.
i18 blk=['VICTOR'] | VICTOR It's a gift, not a lease. Wrap her. | VICTOR faces MAYA and speaks.
i19 blk=['MAYA'] | -  | He goes. Maya stares at A.V.A. Then, quietly, she uncaps a marker and writes on 
i20 blk=['A.V.A.', 'MAYA'] | A.V.A. Did I do well? | A.V.A. addresses the room in volt robotics lab.
i21 blk=['MAYA', 'VICTOR'] | MAYA You diagnosed a client's morality from his shoes. | MAYA faces VICTOR and speaks.
i22 blk=['A.V.A.'] | A.V.A. Ninety-six percent. | A.V.A. faces MAYA and speaks.
i23 blk=['A.V.A.', 'J-7'] | J-7 She gets it from you. | J-7 faces MAYA and speaks.