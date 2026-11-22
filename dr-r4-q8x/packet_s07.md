# VALIDATION PACKET — scene s07
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 7 — INT. PENTHOUSE — KITCHEN / INT. VOLT LAB — MORNING

*Dawn. JIM discovers the scene: A.V.A. charging beside the
espresso machine like a house guest who plugged herself in;
DAMIEN asleep on a stool, upright, arms crossed — a man who
fell asleep mid-inspection. Packing foam is exploded across
the foyer like a small weather event.*

JIM
Sir. There's a—

DAMIEN
(not opening his eyes)
The box hatched, Jim.

*The wallscreen lights itself: VICTOR — fresh, exercised, smug.*

VICTOR
You opened her early. You never could wait — it's why the
board loves you. How do you like my present?

DAMIEN
She unplugged my espresso machine.

VICTOR
Courtship calibration, little brother. She's the enforcement
arm of the trust clause — wedding-ready by the gala, or the
trust eats your life's work. And don't bother returning her.
The contract already thought of that.

*He's gone. Damien reads the warranty card. Punches the number.*

*INT. VOLT ROBOTICS LAB — CONTINUOUS. MAYA — sleeves rolled,
soldering iron behind one ear — answers on the third ring
because the entire phone tree is her.*

MAYA
Volt Robotics. Technical support, legal, and founder.

DAMIEN (V.O.)
I need the warranty line.

MAYA
You've reached it. All of it.

DAMIEN (V.O.)
Your appliance walked out of its packaging at 3 A.M. and
critiqued my espresso intake.

*The soldering iron comes down off her ear very slowly.*

MAYA
...Read me the serial. Slowly.

DAMIEN (V.O.)
Seven-seven-four-Charlie.

*Maya is already off her stool, headset cord trailing, J-7
rotating his whole chassis to watch her pace.*

MAYA
That unit shipped Friday because a client overrode my
sign-off in writing. What is her charge state?

DAMIEN (V.O.)
She said she's "half charged." Like a weather report.

MAYA
She IS a weather report. Listen carefully — do not let her
reach zero percent. Do not let anyone else "update" her.
Do not plug her into anything that isn't the dock in the
crate —

DAMIEN (V.O.)
The crate is full of foam.

MAYA
Then dig. I'll be there in forty minutes. And Mr. Cross?

DAMIEN (V.O.)
What.

MAYA
Stop feeding her baguettes.

DAMIEN (V.O.)
She's a machine.

MAYA
I know what she is. I'm her mother.

*She hangs up. Damien looks at A.V.A. — awake now, politely
pretending she was not listening.*

A.V.A.
How is she?

DAMIEN
Loud.

A.V.A.
(a beat of genuine warmth)
Yes.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 7,
  "scene_heading": "INT. PENTHOUSE — KITCHEN / INT. VOLT LAB — MORNING",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "The morning after S6's kitchen standoff. Three threads define the film from here: Victor's wallscreen call converts the gift into a contractual trap (trust clause, gala deadline, no returns); the warranty line delivers Maya — the maker running her own one-woman phone tree — whose 'I'm her mother' reframes everything; and the first soft beat between Damien and A.V.A. closes it. Structure: kitchen discovery → wallscreen threat → cross-town warranty call → two-line grace note.",
  "zones": [
    "penthouse kitchen",
    "volt robotics lab"
  ],
  "events": [
    {
      "event_id": "s07.e01",
      "source_evidence": [
        "Dawn. JIM discovers the scene: A.V.A. charging beside the espresso machine like a house guest who plugged herself in;",
        "DAMIEN asleep on a stool, upright, arms crossed — a man who fell asleep mid-inspection.",
        "Packing foam is exploded across the foyer like a small weather event."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the morning-after tableau — last night's standoff resolved into an image: the guest who plugged herself in and the host who fell asleep mid-inspection",
      "participants": [
        "JIM",
        "DAMIEN",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "penthouse kitchen"
      },
      "timeline": [
        {
          "beat": "dawn tableau — charging android, sleeping man, exploded foam",
          "type": "held_image"
        },
        {
          "beat": "Jim discovers the scene",
          "type": "action"
        }
      ],
      "visual_requirements": [
        "one frame must hold all three facts — charging android, sleeping man, foam debris; the comedy is compositional, no cutaways needed",
        "A.V.A. still in the freed espresso-machine outlet she annexed in S6 — same surgical cable tidiness"
      ],
      "audio_requirements": [
        "dawn room tone — fridge hum, the city quieter than the night floor of S6"
      ],
      "continuity_constraints": [
        "she charges at the outlet she took in S6 — the kitchen dock she was told is not a dock",
        "foam debris is the exploded crate from S5 — same weather event, still not cleaned up"
      ],
      "ambiguities": [],
      "must_appear": [
        "JIM",
        "DAMIEN",
        "A.V.A."
      ],
      "tableau": true,
      "shot_sequence": [
        "s07.sh01",
        "s07.snd01"
      ]
    },
    {
      "event_id": "s07.e02",
      "source_evidence": [
        "Sir. There's a—",
        "(not opening his eyes)",
        "The box hatched, Jim."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "his eyes stay closed — acceptance already happened overnight; the announcement Jim came to make is already old news",
      "participants": [
        "JIM",
        "DAMIEN",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "penthouse kitchen"
      },
      "timeline": [
        {
          "beat": "Jim's announcement dies at 'a—'",
          "type": "dialogue"
        },
        {
          "beat": "'The box hatched, Jim.' — eyes still closed",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Damien never opens his eyes — the line lands on a man already past surprise",
        "A.V.A. stays on her cable in the background — she is now furniture"
      ],
      "audio_requirements": [],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "JIM",
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s07.sh02"
      ]
    },
    {
      "event_id": "s07.e03",
      "source_evidence": [
        "The wallscreen lights itself: VICTOR — fresh, exercised, smug.",
        "You opened her early. You never could wait — it's why the board loves you. How do you like my present?",
        "She unplugged my espresso machine.",
        "Courtship calibration, little brother. She's the enforcement arm of the trust clause — wedding-ready by the gala, or the trust eats your life's work. And don't bother returning her. The contract already thought of that.",
        "He's gone."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the plot drops as a video call — Victor's gift revealed as a contractual trap, the trust clause given a face and a deadline",
      "participants": [
        "DAMIEN",
        "JIM",
        "A.V.A."
      ],
      "remote_participants": [
        {
          "actor": "VICTOR",
          "channel": "wallscreen video call",
          "direction": "two-way"
        }
      ],
      "location": {
        "zone": "penthouse kitchen"
      },
      "timeline": [
        {
          "beat": "the wallscreen lights itself — Victor appears, fresh, exercised, smug",
          "type": "reveal"
        },
        {
          "beat": "'You opened her early... How do you like my present?'",
          "type": "dialogue_remote"
        },
        {
          "beat": "'She unplugged my espresso machine.' — the wrong answer to a threat",
          "type": "dialogue"
        },
        {
          "beat": "enforcement arm of the trust clause — the contract already thought of returning her",
          "type": "dialogue_remote"
        },
        {
          "beat": "he's gone — the screen drops him",
          "type": "transition"
        }
      ],
      "visual_requirements": [
        "Victor exists only on the wallscreen — fresh/exercised/smug reads as produced self-image, never a physical presence",
        "Damien's espresso complaint is the wrong answer to 'how do you like my present' — play the mismatch deadpan"
      ],
      "audio_requirements": [
        "wallscreen wake tone — the screen asserting itself into the room"
      ],
      "continuity_constraints": [
        "trust clause + gala deadline — Victor's leverage formalized; 'don't bother returning her' forecloses the S5 '30-DAY RETURN' Post-it",
        "'courtship calibration' names the function A.V.A. recited in S6"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s07.sh03",
        "s07.sh04",
        "s07.snd01"
      ]
    },
    {
      "event_id": "s07.e04",
      "source_evidence": [
        "Damien reads the warranty card. Punches the number."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the planted warranty card gets used — the film's second thread begins with a punched number",
      "participants": [
        "DAMIEN",
        "A.V.A."
      ],
      "offscreen_present": [
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "penthouse kitchen"
      },
      "timeline": [
        {
          "beat": "he reads the warranty card — the handwritten side",
          "type": "insert"
        },
        {
          "beat": "he punches the number",
          "type": "action"
        }
      ],
      "visual_requirements": [
        "the card insert must read as the same card from S6 — Post-it side or handwritten side, either honest",
        "the punch is a decision, not a gesture — he is calling a stranger about the woman in his kitchen"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the card and its 'a human answers' warranty line were established in S6 — same handwriting, now used",
        "Maya is present in this object only as handwriting — document_evidence until the phone connects"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s07.sh05"
      ],
      "document_evidence": [
        {
          "author": "MAYA",
          "artifact": "warranty card — the 'a human answers' line",
          "channel": "document"
        }
      ]
    },
    {
      "event_id": "s07.e05",
      "source_evidence": [
        "INT. VOLT ROBOTICS LAB — CONTINUOUS. MAYA — sleeves rolled, soldering iron behind one ear — answers on the third ring because the entire phone tree is her.",
        "Volt Robotics. Technical support, legal, and founder.",
        "I need the warranty line.",
        "You've reached it. All of it.",
        "Your appliance walked out of its packaging at 3 A.M. and critiqued my espresso intake.",
        "The soldering iron comes down off her ear very slowly.",
        "...Read me the serial. Slowly.",
        "Seven-seven-four-Charlie."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "Maya enters the film working — one woman as the entire phone tree; the comedy of scale becomes a person the instant the serial number lands",
      "participants": [
        "MAYA"
      ],
      "remote_participants": [
        {
          "actor": "DAMIEN",
          "channel": "phone",
          "direction": "two-way"
        }
      ],
      "location": {
        "zone": "volt robotics lab"
      },
      "timeline": [
        {
          "beat": "Maya answers on the third ring — soldering iron behind one ear",
          "type": "action"
        },
        {
          "beat": "'Volt Robotics. Technical support, legal, and founder.'",
          "type": "dialogue"
        },
        {
          "beat": "'I need the warranty line.'",
          "type": "dialogue_remote"
        },
        {
          "beat": "'You've reached it. All of it.'",
          "type": "dialogue"
        },
        {
          "beat": "'Your appliance walked out of its packaging at 3 A.M....'",
          "type": "dialogue_remote"
        },
        {
          "beat": "the soldering iron comes down off her ear very slowly",
          "type": "action"
        },
        {
          "beat": "'...Read me the serial. Slowly.'",
          "type": "dialogue"
        },
        {
          "beat": "'Seven-seven-four-Charlie.'",
          "type": "dialogue_remote"
        }
      ],
      "visual_requirements": [
        "the lab is a working room, not a showroom — solder smoke, rolled sleeves, one person doing all the jobs",
        "the iron coming down is the turn — her whole posture changes before she asks for the serial"
      ],
      "audio_requirements": [
        "the phone rings to the third ring; solder-station lab quiet underneath"
      ],
      "continuity_constraints": [
        "serial 774-C matches the asset tag A.V.A. quoted in S6 — the number is now confirmed on both ends"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s07.sh06",
        "s07.sh07",
        "s07.snd01"
      ]
    },
    {
      "event_id": "s07.e06",
      "source_evidence": [
        "Maya is already off her stool, headset cord trailing, J-7 rotating his whole chassis to watch her pace.",
        "That unit shipped Friday because a client overrode my sign-off in writing. What is her charge state?",
        "She said she's \"half charged.\" Like a weather report.",
        "She IS a weather report. Listen carefully — do not let her reach zero percent. Do not let anyone else \"update\" her. Do not plug her into anything that isn't the dock in the crate —",
        "The crate is full of foam.",
        "Then dig. I'll be there in forty minutes. And Mr. Cross?",
        "What.",
        "Stop feeding her baguettes.",
        "She's a machine.",
        "I know what she is. I'm her mother.",
        "She hangs up."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the override confession and the care rules — Maya stakes her lab on a client signature, invents the battery triage list, and names herself: 'I'm her mother' lands as fact, not sentiment",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "remote_participants": [
        {
          "actor": "DAMIEN",
          "channel": "phone",
          "direction": "two-way"
        }
      ],
      "location": {
        "zone": "volt robotics lab"
      },
      "timeline": [
        {
          "beat": "off the stool, headset cord trailing — J-7 rotates his whole chassis to watch her pace",
          "type": "action"
        },
        {
          "beat": "'That unit shipped Friday because a client overrode my sign-off in writing.'",
          "type": "dialogue"
        },
        {
          "beat": "'She said she's \"half charged.\" Like a weather report.'",
          "type": "dialogue_remote"
        },
        {
          "beat": "'She IS a weather report' — the three rules",
          "type": "dialogue"
        },
        {
          "beat": "'The crate is full of foam.'",
          "type": "dialogue_remote"
        },
        {
          "beat": "'Then dig. I'll be there in forty minutes. And Mr. Cross?'",
          "type": "dialogue"
        },
        {
          "beat": "'What.'",
          "type": "dialogue_remote"
        },
        {
          "beat": "'Stop feeding her baguettes.'",
          "type": "dialogue"
        },
        {
          "beat": "'She's a machine.'",
          "type": "dialogue_remote"
        },
        {
          "beat": "'I know what she is. I'm her mother.'",
          "type": "dialogue"
        },
        {
          "beat": "she hangs up",
          "type": "action"
        }
      ],
      "visual_requirements": [
        "J-7's whole-chassis rotation is the lab's only witness — a machine watching its maker pace",
        "'I'm her mother' needs no emphasis — said like a technician correcting a specification error"
      ],
      "audio_requirements": [
        "headset cord trailing, the hang-up click"
      ],
      "continuity_constraints": [
        "the client override in writing is Victor — pays off in S8's 'Cross family prototype' demonstration",
        "the charge rules set up the dock (S8) and the zero-percent crisis (S30); 'four hours on, six charging' is invented here as a warning"
      ],
      "ambiguities": [
        "'I'm her mother' — literal builder claim vs emotional claim; performance should let both readings stand, flag for director"
      ],
      "must_appear": [
        "MAYA",
        "J-7"
      ],
      "tableau": false,
      "shot_sequence": [
        "s07.sh08",
        "s07.sh09",
        "s07.sh10",
        "s07.snd01"
      ]
    },
    {
      "event_id": "s07.e07",
      "source_evidence": [
        "Damien looks at A.V.A. — awake now, politely pretending she was not listening.",
        "How is she?",
        "Loud.",
        "(a beat of genuine warmth)",
        "Yes."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the film's first soft beat — A.V.A. asks after her maker like a daughter, Damien answers honestly, and 'Yes' carries warmth neither of them expected",
      "participants": [
        "DAMIEN",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "penthouse kitchen"
      },
      "timeline": [
        {
          "beat": "Damien looks at A.V.A. — awake, politely pretending she was not listening",
          "type": "action"
        },
        {
          "beat": "'How is she?'",
          "type": "dialogue"
        },
        {
          "beat": "'Loud.'",
          "type": "dialogue"
        },
        {
          "beat": "'Yes.' — a beat of genuine warmth",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "her polite pretense of not-listening is performed innocence — the audience must catch her catching herself",
        "the warmth beat is small — one breath, not a smile"
      ],
      "audio_requirements": [
        "kitchen quiet returns — morning room tone under the grace note"
      ],
      "continuity_constraints": [
        "the mother-daughter thread starts here — A.V.A.'s 'How is she?' will echo when Maya lives in the house"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s07.sh11a",
        "s07.sh11b",
        "s07.sh11c",
        "s07.snd01"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s07.sh01",
      "size": "W",
      "zone": "penthouse kitchen",
      "type": "visual",
      "participants": [
        "JIM",
        "DAMIEN",
        "A.V.A."
      ],
      "implements": [
        "s07.e01"
      ],
      "covers_beats": {
        "s07.e01": [
          0,
          1
        ]
      },
      "purpose": "the discovered tableau: A.V.A. charging beside the espresso machine, Damien asleep upright on a stool, foam exploded — Jim entering the evidence",
      "audio_note": "dawn room tone, fridge hum, city quieter than S6's night floor"
    },
    {
      "shot_id": "s07.sh02",
      "size": "M",
      "zone": "penthouse kitchen",
      "type": "visual",
      "participants": [
        "JIM",
        "DAMIEN",
        "A.V.A."
      ],
      "implements": [
        "s07.e02"
      ],
      "covers_beats": {
        "s07.e02": [
          0,
          1
        ]
      },
      "purpose": "Jim's announcement dies mid-syllable → 'The box hatched, Jim.' — eyes never open, A.V.A. on her cable behind",
      "dialogue_lines": [
        {
          "event_id": "s07.e02",
          "speaker": "JIM",
          "line": "Sir. There's a—",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s07.e02",
          "speaker": "DAMIEN",
          "line": "The box hatched, Jim.",
          "line_kind": "on_camera",
          "recipient": "JIM",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s07.sh03",
      "size": "M",
      "zone": "penthouse kitchen",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "A.V.A."
      ],
      "depicts": [
        {
          "actors": [
            "VICTOR"
          ],
          "channel": "wallscreen video call"
        }
      ],
      "implements": [
        "s07.e03"
      ],
      "covers_beats": {
        "s07.e03": [
          0,
          1
        ]
      },
      "purpose": "the wallscreen lights itself — Victor appears fresh and smug; 'How do you like my present?'",
      "audio_note": "wallscreen wake tone",
      "dialogue_lines": [
        {
          "event_id": "s07.e03",
          "speaker": "VICTOR",
          "line": "You opened her early. You never could wait — it's why the board loves you. How do you like my present?",
          "line_kind": "remote_channel",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s07.sh04",
      "size": "M",
      "zone": "penthouse kitchen",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "JIM"
      ],
      "depicts": [
        {
          "actors": [
            "VICTOR"
          ],
          "channel": "wallscreen video call"
        }
      ],
      "implements": [
        "s07.e03"
      ],
      "covers_beats": {
        "s07.e03": [
          2,
          3,
          4
        ]
      },
      "purpose": "'She unplugged my espresso machine.' → trust-clause speech → the screen drops him",
      "dialogue_lines": [
        {
          "event_id": "s07.e03",
          "speaker": "DAMIEN",
          "line": "She unplugged my espresso machine.",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "remote",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s07.e03",
          "speaker": "VICTOR",
          "line": "Courtship calibration, little brother. She's the enforcement arm of the trust clause — wedding-ready by the gala, or the trust eats your life's work. And don't bother returning her. The contract already thought of that.",
          "line_kind": "remote_channel",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        }
      ]
    },
    {
      "shot_id": "s07.sh05",
      "size": "INS",
      "zone": "penthouse kitchen",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "depicts": [
        {
          "object": "warranty card — Maya's handwriting side",
          "channel": "document"
        }
      ],
      "implements": [
        "s07.e04"
      ],
      "covers_beats": {
        "s07.e04": [
          0,
          1
        ]
      },
      "purpose": "the card from S6 read and used — he punches the warranty number",
      "audio_note": ""
    },
    {
      "shot_id": "s07.sh06",
      "size": "M",
      "zone": "volt robotics lab",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s07.e05"
      ],
      "covers_beats": {
        "s07.e05": [
          0,
          1,
          2,
          3
        ]
      },
      "purpose": "Maya answers on the third ring — the entire phone tree is one woman with a soldering iron behind her ear",
      "audio_note": "third ring, solder-station lab quiet",
      "dialogue_lines": [
        {
          "event_id": "s07.e05",
          "speaker": "MAYA",
          "line": "Volt Robotics. Technical support, legal, and founder.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "remote",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s07.e05",
          "speaker": "DAMIEN",
          "line": "I need the warranty line.",
          "line_kind": "vo",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s07.e05",
          "speaker": "MAYA",
          "line": "You've reached it. All of it.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "remote",
          "beats": [
            3
          ]
        }
      ]
    },
    {
      "shot_id": "s07.sh07",
      "size": "CU",
      "zone": "volt robotics lab",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s07.e05"
      ],
      "covers_beats": {
        "s07.e05": [
          4,
          5,
          6,
          7
        ]
      },
      "purpose": "the appliance report lands → the soldering iron comes down very slowly → the serial confirmed",
      "audio_note": "",
      "dialogue_lines": [
        {
          "event_id": "s07.e05",
          "speaker": "DAMIEN",
          "line": "Your appliance walked out of its packaging at 3 A.M. and critiqued my espresso intake.",
          "line_kind": "vo",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            4
          ]
        },
        {
          "event_id": "s07.e05",
          "speaker": "MAYA",
          "line": "...Read me the serial. Slowly.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "remote",
          "beats": [
            6
          ]
        },
        {
          "event_id": "s07.e05",
          "speaker": "DAMIEN",
          "line": "Seven-seven-four-Charlie.",
          "line_kind": "vo",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            7
          ]
        }
      ]
    },
    {
      "shot_id": "s07.sh08",
      "size": "M",
      "zone": "volt robotics lab",
      "type": "visual",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "implements": [
        "s07.e06"
      ],
      "covers_beats": {
        "s07.e06": [
          0,
          1,
          2
        ]
      },
      "purpose": "off the stool, cord trailing — J-7's whole chassis rotates to watch her pace → the override confession and the charge-state question",
      "audio_note": "headset cord trailing",
      "dialogue_lines": [
        {
          "event_id": "s07.e06",
          "speaker": "MAYA",
          "line": "That unit shipped Friday because a client overrode my sign-off in writing. What is her charge state?",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "remote",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s07.e06",
          "speaker": "DAMIEN",
          "line": "She said she's \"half charged.\" Like a weather report.",
          "line_kind": "vo",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s07.sh09",
      "size": "CU",
      "zone": "volt robotics lab",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s07.e06"
      ],
      "covers_beats": {
        "s07.e06": [
          3,
          4,
          5,
          6
        ]
      },
      "purpose": "'She IS a weather report' — the three rules delivered like a pre-flight checklist; foam problem; forty minutes",
      "dialogue_lines": [
        {
          "event_id": "s07.e06",
          "speaker": "MAYA",
          "line": "She IS a weather report. Listen carefully — do not let her reach zero percent. Do not let anyone else \"update\" her. Do not plug her into anything that isn't the dock in the crate —",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "remote",
          "beats": [
            3
          ]
        },
        {
          "event_id": "s07.e06",
          "speaker": "DAMIEN",
          "line": "The crate is full of foam.",
          "line_kind": "vo",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            4
          ]
        },
        {
          "event_id": "s07.e06",
          "speaker": "MAYA",
          "line": "Then dig. I'll be there in forty minutes. And Mr. Cross?",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "remote",
          "beats": [
            5
          ]
        },
        {
          "event_id": "s07.e06",
          "speaker": "DAMIEN",
          "line": "What.",
          "line_kind": "vo",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            6
          ]
        }
      ]
    },
    {
      "shot_id": "s07.sh10",
      "size": "CU",
      "zone": "volt robotics lab",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "implements": [
        "s07.e06"
      ],
      "covers_beats": {
        "s07.e06": [
          7,
          8,
          9,
          10
        ]
      },
      "purpose": "'Stop feeding her baguettes.' → 'She's a machine.' → 'I'm her mother.' → hang-up click",
      "audio_note": "the hang-up click",
      "dialogue_lines": [
        {
          "event_id": "s07.e06",
          "speaker": "MAYA",
          "line": "Stop feeding her baguettes.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "remote",
          "beats": [
            7
          ]
        },
        {
          "event_id": "s07.e06",
          "speaker": "DAMIEN",
          "line": "She's a machine.",
          "line_kind": "vo",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            8
          ]
        },
        {
          "event_id": "s07.e06",
          "speaker": "MAYA",
          "line": "I know what she is. I'm her mother.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "remote",
          "beats": [
            9
          ]
        }
      ]
    },
    {
      "shot_id": "s07.snd01",
      "type": "sound",
      "implements": [
        "s07.e01",
        "s07.e03",
        "s07.e05",
        "s07.e06",
        "s07.e07"
      ],
      "purpose": "sound card: dawn room tone (fridge hum, muted city), wallscreen wake tone, the phone's third ring and the hang-up click, solder-station lab quiet; held silence after 'I'm her mother'",
      "audio_note": "dawn room tone, fridge hum, wallscreen wake tone, phone rings to third ring, solder-station quiet, headset cord, hang-up click, kitchen quiet returns",
      "no_score": true
    },
    {
      "shot_id": "s07.sh11a",
      "size": "M",
      "zone": "penthouse kitchen",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "A.V.A."
      ],
      "implements": [
        "s07.e07"
      ],
      "covers_beats": {
        "s07.e07": [
          0
        ]
      },
      "purpose": "the caught pretense — A.V.A. politely pretending she was not listening; silent frame before the question",
      "audio_note": "kitchen quiet"
    },
    {
      "shot_id": "s07.sh11b",
      "size": "M",
      "zone": "penthouse kitchen",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "A.V.A."
      ],
      "implements": [
        "s07.e07"
      ],
      "covers_beats": {
        "s07.e07": [
          1,
          2
        ]
      },
      "purpose": "'How is she?' / 'Loud.' — the daughter-like question and the honest answer",
      "audio_note": "kitchen quiet",
      "dialogue_lines": [
        {
          "event_id": "s07.e07",
          "speaker": "A.V.A.",
          "line": "How is she?",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s07.e07",
          "speaker": "DAMIEN",
          "line": "Loud.",
          "line_kind": "on_camera",
          "recipient": "A.V.A.",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s07.sh11c",
      "size": "CU",
      "zone": "penthouse kitchen",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s07.e07"
      ],
      "covers_beats": {
        "s07.e07": [
          3
        ]
      },
      "purpose": "a beat of genuine warmth, then 'Yes.' — the grace note; the pause is the beat, not the word",
      "audio_note": "kitchen quiet, the held breath",
      "dialogue_lines": [
        {
          "event_id": "s07.e07",
          "speaker": "A.V.A.",
          "line": "Yes.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        }
      ]
    }
  ],
  "coverage": [
    {
      "span": "A.V.A. charging beside the espresso machine like a house guest who plugged herself in",
      "disposition": "covered_by",
      "by": [
        "s07.e01"
      ]
    },
    {
      "span": "asleep on a stool, upright, arms crossed",
      "disposition": "covered_by",
      "by": [
        "s07.e01"
      ]
    },
    {
      "span": "Packing foam is exploded across the foyer like a small weather event.",
      "disposition": "covered_by",
      "by": [
        "s07.e01"
      ]
    },
    {
      "span": "Sir. There's a—",
      "disposition": "covered_by",
      "by": [
        "s07.e02"
      ]
    },
    {
      "span": "The box hatched, Jim.",
      "disposition": "covered_by",
      "by": [
        "s07.e02"
      ]
    },
    {
      "span": "The wallscreen lights itself: VICTOR — fresh, exercised, smug.",
      "disposition": "covered_by",
      "by": [
        "s07.e03"
      ]
    },
    {
      "span": "How do you like my present?",
      "disposition": "covered_by",
      "by": [
        "s07.e03"
      ]
    },
    {
      "span": "She unplugged my espresso machine.",
      "disposition": "covered_by",
      "by": [
        "s07.e03"
      ]
    },
    {
      "span": "enforcement arm of the trust clause",
      "disposition": "covered_by",
      "by": [
        "s07.e03"
      ]
    },
    {
      "span": "He's gone.",
      "disposition": "covered_by",
      "by": [
        "s07.e03"
      ]
    },
    {
      "span": "Damien reads the warranty card. Punches the number.",
      "disposition": "covered_by",
      "by": [
        "s07.e04"
      ]
    },
    {
      "span": "soldering iron behind one ear",
      "disposition": "covered_by",
      "by": [
        "s07.e05"
      ]
    },
    {
      "span": "Volt Robotics. Technical support, legal, and founder.",
      "disposition": "covered_by",
      "by": [
        "s07.e05"
      ]
    },
    {
      "span": "I need the warranty line.",
      "disposition": "covered_by",
      "by": [
        "s07.e05"
      ]
    },
    {
      "span": "You've reached it. All of it.",
      "disposition": "covered_by",
      "by": [
        "s07.e05"
      ]
    },
    {
      "span": "critiqued my espresso intake",
      "disposition": "covered_by",
      "by": [
        "s07.e05"
      ]
    },
    {
      "span": "The soldering iron comes down off her ear very slowly.",
      "disposition": "covered_by",
      "by": [
        "s07.e05"
      ]
    },
    {
      "span": "...Read me the serial. Slowly.",
      "disposition": "covered_by",
      "by": [
        "s07.e05"
      ]
    },
    {
      "span": "Seven-seven-four-Charlie.",
      "disposition": "covered_by",
      "by": [
        "s07.e05"
      ]
    },
    {
      "span": "off her stool, headset cord trailing",
      "disposition": "covered_by",
      "by": [
        "s07.e06"
      ]
    },
    {
      "span": "J-7 rotating his whole chassis to watch her pace",
      "disposition": "covered_by",
      "by": [
        "s07.e06"
      ]
    },
    {
      "span": "overrode my sign-off in writing",
      "disposition": "covered_by",
      "by": [
        "s07.e06"
      ]
    },
    {
      "span": "She said she's \"half charged.\" Like a weather report.",
      "disposition": "covered_by",
      "by": [
        "s07.e06"
      ]
    },
    {
      "span": "She IS a weather report.",
      "disposition": "covered_by",
      "by": [
        "s07.e06"
      ]
    },
    {
      "span": "The crate is full of foam.",
      "disposition": "covered_by",
      "by": [
        "s07.e06"
      ]
    },
    {
      "span": "I'll be there in forty minutes. And Mr. Cross?",
      "disposition": "covered_by",
      "by": [
        "s07.e06"
      ]
    },
    {
      "span": "What.",
      "disposition": "covered_by",
      "by": [
        "s07.e06"
      ]
    },
    {
      "span": "Stop feeding her baguettes.",
      "disposition": "covered_by",
      "by": [
        "s07.e06"
      ]
    },
    {
      "span": "She's a machine.",
      "disposition": "covered_by",
      "by": [
        "s07.e06"
      ]
    },
    {
      "span": "I know what she is. I'm her mother.",
      "disposition": "covered_by",
      "by": [
        "s07.e06"
      ]
    },
    {
      "span": "She hangs up.",
      "disposition": "covered_by",
      "by": [
        "s07.e06"
      ]
    },
    {
      "span": "politely pretending she was not listening",
      "disposition": "covered_by",
      "by": [
        "s07.e07"
      ]
    },
    {
      "span": "How is she?",
      "disposition": "covered_by",
      "by": [
        "s07.e07"
      ]
    },
    {
      "span": "Loud.",
      "disposition": "covered_by",
      "by": [
        "s07.e07"
      ]
    },
    {
      "span": "a beat of genuine warmth",
      "disposition": "covered_by",
      "by": [
        "s07.e07"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['JIM', 'DAMIEN'] | JIM  | Dawn. JIM discovers the scene: A.V.A. charging beside the espresso machine like 
i02 blk=['JIM', 'DAMIEN'] | JIM Sir. There's a— | JIM faces DAMIEN and speaks.
i03 blk=['DAMIEN'] | DAMIEN The box hatched, Jim. | DAMIEN faces JIM and speaks.
i04 blk=['VICTOR'] | VICTOR You opened her early. You never could wait — it's why the bo | The wallscreen lights itself: VICTOR — fresh, exercised, smug.
i05 blk=['DAMIEN', 'VICTOR'] | DAMIEN She unplugged my espresso machine. | DAMIEN faces JIM and speaks.
i06 blk=['VICTOR'] | VICTOR Courtship calibration, little brother. She's the enforcement | VICTOR faces JIM and speaks.
i07 blk=['MAYA'] | MAYA  | He's gone. Damien reads the warranty card. Punches the number. INT. VOLT ROBOTIC
i08 blk=['MAYA'] | MAYA Volt Robotics. Technical support, legal, and founder. | MAYA faces JIM and speaks.
i09 blk=['DAMIEN'] | DAMIEN I need the warranty line. | DAMIEN faces JIM and speaks.
i10 blk=['MAYA'] | MAYA You've reached it. All of it. | MAYA faces JIM and speaks.
i11 blk=['DAMIEN'] | DAMIEN Your appliance walked out of its packaging at 3 A.M. and cri | DAMIEN faces JIM and speaks.
i12 blk=['MAYA', 'JIM'] | MAYA ...Read me the serial. Slowly. | The soldering iron comes down off her ear very slowly.
i13 blk=['DAMIEN'] | DAMIEN Seven-seven-four-Charlie. | DAMIEN faces JIM and speaks.
i14 blk=['J-7', 'MAYA'] | J-7  | Maya is already off her stool, headset cord trailing, J-7 rotating his whole cha
i15 blk=['MAYA'] | MAYA That unit shipped Friday because a client overrode my sign-o | MAYA faces JIM and speaks.
i16 blk=['DAMIEN'] | DAMIEN She said she's "half charged." Like a weather report. | DAMIEN faces JIM and speaks.
i17 blk=['MAYA'] | MAYA She IS a weather report. Listen carefully — do not let her r | MAYA faces JIM and speaks.
i18 blk=['DAMIEN', 'JIM'] | DAMIEN The crate is full of foam. | DAMIEN faces JIM and speaks.
i19 blk=['MAYA'] | MAYA Then dig. I'll be there in forty minutes. And Mr. Cross? | MAYA faces JIM and speaks.
i20 blk=['DAMIEN'] | DAMIEN What. | DAMIEN faces JIM and speaks.
i21 blk=['MAYA'] | MAYA Stop feeding her baguettes. | MAYA faces JIM and speaks.
i22 blk=['DAMIEN'] | DAMIEN She's a machine. | DAMIEN faces JIM and speaks.
i23 blk=['MAYA', 'JIM'] | MAYA I know what she is. I'm her mother. | MAYA faces JIM and speaks.
i24 blk=['DAMIEN'] | DAMIEN  | She hangs up. Damien looks at A.V.A. — awake now, politely pretending she was no
i25 blk=['DAMIEN', 'A.V.A.'] | A.V.A. How is she? | A.V.A. faces JIM and speaks.
i26 blk=['DAMIEN'] | DAMIEN Loud. | DAMIEN faces JIM and speaks.
i27 blk=['A.V.A.'] | A.V.A. Yes. | A.V.A. faces JIM and speaks.