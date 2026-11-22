# VALIDATION PACKET — scene s34
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 34 — INT. BALLROOM — CONTINUOUS

*A.V.A. — the real one, half-charged, wheels herself down the
center aisle in her dock chair like a queen in a palanquin.
Every eye on her. She reaches the stage, ascends the ramp, takes
a microphone with precise fingers.*

A.V.A.
I am the machine.

*Total silence.*

A.V.A. (CONT'D)
Serial A-4-1-1-9, Volt Robotics. Built on the face, voice and
neural baseline of my creator, Maya Lind. The woman my operator
laughed with in the evenings — was her. The woman who danced —
was her. His error was human. Those are forgivable.

*A beat. She turns to face the room fully.*

A.V.A. (CONT'D)
A defense is required. Maya Lind: intelligence, ninety-ninth
percentile. Humor: anomalous — my metrics fail to model it.
Loyalty: exceeds contractual obligation by a factor I am
embarrassed to print. She played me better than I play myself,
which is humiliating, and she did it to protect forty people at
a lab nobody in this room has heard of.

*A rustle through the room — something between a laugh and a
softening.*

A.V.A. (CONT'D)
To the trustees: the clause requires a man who is demonstrably
married. What it produced is a man who is demonstrably human.
I have observed him for sixty-two days. He flinches now, too.
That is growth.

*She sets the microphone down with surgical care.*

A.V.A. (CONT'D)
Statistics on Victor Cross's proposal: Sophia Vane's consent
probability, under duress: eleven percent. Authenticity of the
announced engagement: zero. Shall I continue?

VICTOR
Get that thing off the stage—

A.V.A.
I am also a registered witness. Legally. Check the firmware.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 34,
  "scene_heading": "SCENE 34 — INT. BALLROOM — CONTINUOUS",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "Continuous from S33's servo-motor cliffhanger. The real A.V.A. — half-charged — wheels herself down the center aisle like a queen in a palanquin, takes the stage, and dismantles Victor's trap in four moves: she owns the machine identity, defends Maya Lind by name, reframes the clause as 'demonstrably human,' and ends as a registered legal witness. Victor loses the room without her raising her voice.",
  "zones": [
    "stage",
    "ballroom floor",
    "service level"
  ],
  "events": [
    {
      "event_id": "s34.e01",
      "source_evidence": [
        "A.V.A. — the real one, half-charged, wheels herself down the center aisle in her dock chair like a queen in a palanquin.",
        "Every eye on her.",
        "She reaches the stage, ascends the ramp, takes a microphone with precise fingers."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the counter-entrance — the 'dead' machine arrives on her own power and takes the stage",
      "participants": [
        "A.V.A.",
        "GUESTS"
      ],
      "remote_participants": [],
      "location": {
        "zones": [
          "ballroom floor",
          "stage"
        ],
        "primary": "ballroom floor"
      },
      "timeline": [
        {
          "beat": "A.V.A. — the real one, half-charged",
          "type": "reveal"
        },
        {
          "beat": "wheels herself down the center aisle like a queen in a palanquin",
          "type": "action"
        },
        {
          "beat": "every eye on her",
          "type": "reaction"
        },
        {
          "beat": "reaches the stage, ascends the ramp, takes a microphone with precise fingers",
          "type": "action"
        }
      ],
      "visual_requirements": [
        "the dock chair as palanquin — regal, not pitiable; she owns the aisle",
        "the room's attention as its own beat before she reaches the mic"
      ],
      "audio_requirements": [
        "servo-motors fading as she ascends the ramp"
      ],
      "continuity_constraints": [
        "the power chair and servo sound carry over from S33's cliffhanger",
        "half-charged — mobile but running low; her economy of movement is the battery state"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s34.sh01",
        "s34.sh03",
        "s34.snd01"
      ],
      "decisions": [
        {
          "topic": "room's attention as separate reaction plan (sh02)",
          "status": "resolved-decision",
          "decision": "merge 'every eye on her' into the W descent frame — the turn of the room's attention is continuous with the chair's approach, no editorial pause justifies a separate plan",
          "basis": "director_choice",
          "consequence": "sh01 covers beats 0-2 of e01: arrival, descent, every eye on her — the frame must still read the room's attention at its edges",
          "resolved_from": "review verdict R3: separate plan needed only if a cut/pause or re-composition exists — it does not"
        }
      ]
    },
    {
      "event_id": "s34.e02",
      "source_evidence": [
        "I am the machine.",
        "Total silence."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the claim — she takes the identity Victor used against her, and the room goes silent",
      "participants": [
        "A.V.A.",
        "GUESTS",
        "VICTOR",
        "DAMIEN",
        "SOPHIA",
        "TRUSTEES"
      ],
      "remote_participants": [],
      "location": {
        "zones": [
          "stage",
          "ballroom floor"
        ],
        "primary": "stage"
      },
      "timeline": [
        {
          "beat": "'I am the machine.'",
          "type": "dialogue"
        },
        {
          "beat": "total silence lands",
          "type": "sound"
        }
      ],
      "visual_requirements": [
        "the line into the mic — plain, unamplified confidence",
        "the silence is a room-wide tableau — stage and floor frozen together"
      ],
      "audio_requirements": [
        "total silence after the line"
      ],
      "continuity_constraints": [
        "Victor, Sophia, Damien, trustees, guests all carry over from S33's trap tableau"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A."
      ],
      "tableau": true,
      "shot_sequence": [
        "s34.sh04",
        "s34.sh05",
        "s34.snd01"
      ]
    },
    {
      "event_id": "s34.e03",
      "source_evidence": [
        "Serial A-4-1-1-9, Volt Robotics. Built on the face, voice and neural baseline of my creator, Maya Lind.",
        "The woman my operator laughed with in the evenings — was her. The woman who danced — was her. His error was human. Those are forgivable."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "identity on the record — serial number, creator's name, and the confession that clears Damien: 'was her'",
      "participants": [
        "A.V.A.",
        "DAMIEN",
        "MAYA",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "MAYA",
        "GUESTS"
      ],
      "location": {
        "zones": [
          "stage",
          "ballroom floor",
          "service level"
        ],
        "primary": "stage"
      },
      "timeline": [
        {
          "beat": "serial and creator — 'built on the face, voice and neural baseline of my creator, Maya Lind'",
          "type": "dialogue"
        },
        {
          "beat": "'the woman who laughed / danced — was her. His error was human. Those are forgivable.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the 'was her' half lands on Damien — his error named and forgiven in the same breath"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "Maya remains on the service level (S33) — present in the venue, unframed during this speech",
        "'the woman who danced' refers to the S30 waltz swap — continuity of the con"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A.",
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s34.sh06",
        "s34.sh07"
      ]
    },
    {
      "event_id": "s34.e04",
      "source_evidence": [
        "A beat. She turns to face the room fully.",
        "A defense is required. Maya Lind: intelligence, ninety-ninth percentile. Humor: anomalous — my metrics fail to model it. Loyalty: exceeds contractual obligation by a factor I am embarrassed to print. She played me better than I play myself, which is humiliating, and she did it to protect forty people at a lab nobody in this room has heard of."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the defense of Maya — the machine testifies for the human who played her, metrics as love language",
      "participants": [
        "A.V.A.",
        "MAYA",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "MAYA"
      ],
      "location": {
        "zones": [
          "stage",
          "service level"
        ],
        "primary": "stage"
      },
      "timeline": [
        {
          "beat": "a beat — she turns to face the room fully",
          "type": "held_action"
        },
        {
          "beat": "the defense — ninety-ninth percentile, anomalous humor, embarrassing loyalty, forty people at a lab nobody heard of",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the full turn is its own held beat — she chooses the room before she defends Maya"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the 'forty people at a lab' is Volt Lab — the job stakes established earlier in the film"
      ],
      "ambiguities": [
        "Maya is on the service level throughout the defense — the screenplay gives her no frame here; a service-level reaction cut is a director option, left offscreen by default"
      ],
      "must_appear": [
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s34.sh08"
      ]
    },
    {
      "event_id": "s34.e05",
      "source_evidence": [
        "A rustle through the room — something between a laugh and a softening."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the room turns — the first audible sign the defense is working",
      "participants": [
        "GUESTS",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "ballroom floor"
      },
      "timeline": [
        {
          "beat": "a rustle — something between a laugh and a softening",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "the rustle as a mass micro-reaction — shoulders easing, not applause"
      ],
      "audio_requirements": [
        "rustle through the room — laugh and softening"
      ],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "GUESTS"
      ],
      "tableau": false,
      "shot_sequence": [
        "s34.sh08",
        "s34.snd01"
      ],
      "decisions": [
        {
          "topic": "rustle as separate visual plan (sh09)",
          "status": "resolved-decision",
          "decision": "merge the rustle beat into the defense-of-Maya coverage — a short audience shift, no independent behavior change; the rustle sound stays in snd01 (covers e05)",
          "basis": "director_choice",
          "consequence": "sh08 covers e05.b0 as its landing beat — shoulders easing between a laugh and a softening read at the tail of the defense; audio card s34.snd01 continues to carry the designed rustle",
          "resolved_from": "review verdict R3: fold into sh08 if no separate beat-change; sound must not be lost"
        }
      ]
    },
    {
      "event_id": "s34.e06",
      "source_evidence": [
        "To the trustees: the clause requires a man who is demonstrably married. What it produced is a man who is demonstrably human.",
        "I have observed him for sixty-two days. He flinches now, too. That is growth."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the legal reframe — the clause's letter satisfied in spirit: married vs human, observed sixty-two days",
      "participants": [
        "A.V.A.",
        "TRUSTEES",
        "DAMIEN"
      ],
      "remote_participants": [],
      "location": {
        "zones": [
          "stage",
          "ballroom floor"
        ],
        "primary": "stage"
      },
      "timeline": [
        {
          "beat": "'To the trustees: demonstrably married vs demonstrably human'",
          "type": "dialogue"
        },
        {
          "beat": "'sixty-two days — he flinches now, too. That is growth.'",
          "type": "dialogue"
        },
        {
          "beat": "it lands on the trustee table",
          "type": "reaction"
        },
        {
          "beat": "it lands on Damien — 'growth' named in public",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "addressed to the trustee table — the argument is for them, the observation is about him",
        "Damien's beat is receipt, not reply — 'he flinches now, too' happening live"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the clause's letter is the same text Victor cited — 'demonstrably human' is her counter-reading"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A.",
        "TRUSTEES",
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s34.sh10",
        "s34.sh11",
        "s34.sh12"
      ]
    },
    {
      "event_id": "s34.e07",
      "source_evidence": [
        "She sets the microphone down with surgical care."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the surgical pause — control asserted through the prop before the kill shot",
      "participants": [
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "stage"
      },
      "timeline": [
        {
          "beat": "she sets the microphone down — surgical care",
          "type": "held_action"
        }
      ],
      "visual_requirements": [
        "the set-down as insert grammar — precise fingers, no wasted motion"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the mic is the one she took in e01 — precise fingers both times"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s34.sh13"
      ],
      "decisions": [
        {
          "topic": "microphone during the statistics speech",
          "status": "resolved-decision",
          "decision": "A.V.A. sets the microphone down and delivers the statistics unamplified; the standing mic remains in frame for Damien in S35",
          "basis": "screenplay_text",
          "consequence": "sh covering the speech keeps the set-down gesture then holds her unamplified delivery; the standing mic must stay visible so S35's 'microphone A.V.A. left standing' pays off",
          "resolved_from": "the mic is set down before the final speech — unamplified or reclaimed"
        }
      ]
    },
    {
      "event_id": "s34.e08",
      "source_evidence": [
        "Statistics on Victor Cross's proposal: Sophia Vane's consent probability, under duress: eleven percent.",
        "Authenticity of the announced engagement: zero. Shall I continue?"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the kill shot — the proposal reduced to two numbers, consent at eleven percent, authenticity at zero",
      "participants": [
        "A.V.A.",
        "VICTOR",
        "SOPHIA"
      ],
      "remote_participants": [],
      "location": {
        "zone": "stage"
      },
      "timeline": [
        {
          "beat": "consent probability under duress: eleven percent",
          "type": "dialogue"
        },
        {
          "beat": "authenticity of the announced engagement: zero — 'Shall I continue?'",
          "type": "dialogue"
        },
        {
          "beat": "the numbers land on Victor and Sophia",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "the statistics delivered flat — the cruelty is in the arithmetic, not the tone",
        "Victor and Sophia share the reaction — the coercer and the coerced, quantified together"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "'under duress' confirms the S32 leverage ('she owes me the estate') in public"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A.",
        "VICTOR",
        "SOPHIA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s34.sh14",
        "s34.sh15"
      ]
    },
    {
      "event_id": "s34.e09",
      "source_evidence": [
        "Get that thing off the stage—",
        "I am also a registered witness. Legally. Check the firmware."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "Victor breaks composure and she finishes him — 'registered witness' converts her from exhibit to counsel",
      "participants": [
        "VICTOR",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "stage"
      },
      "timeline": [
        {
          "beat": "Victor erupts — 'Get that thing off the stage—'",
          "type": "dialogue"
        },
        {
          "beat": "'I am also a registered witness. Legally. Check the firmware.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "his shout cut off by her calm — the volume differential is the power read",
        "'that thing' vs 'registered witness' — the object/person argument resolved by firmware"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "Victor's line is the scripted cut-off — his sentence dies, hers doesn't"
      ],
      "ambiguities": [],
      "must_appear": [
        "VICTOR",
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s34.sh16",
        "s34.sh17"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s34.sh01",
      "size": "W/M",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "A.V.A.",
        "GUESTS"
      ],
      "implements": [
        "s34.e01"
      ],
      "covers_beats": {
        "s34.e01": [
          0,
          1,
          2
        ]
      },
      "purpose": "the real one, half-charged — the dock chair down the center aisle like a queen in a palanquin; every eye on her inside the same frame",
      "audio_note": "servo-motors carrying over from the cliffhanger"
    },
    {
      "shot_id": "s34.sh03",
      "size": "M",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s34.e01"
      ],
      "covers_beats": {
        "s34.e01": [
          3
        ]
      },
      "purpose": "she reaches the stage, ascends the ramp, takes the microphone — precise fingers",
      "audio_note": "servo-motors fading as she ascends the ramp, mic handling"
    },
    {
      "shot_id": "s34.sh04",
      "size": "CU/M",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s34.e02"
      ],
      "covers_beats": {
        "s34.e02": [
          0
        ]
      },
      "purpose": "'I am the machine.' — the claim made plainly into the mic",
      "audio_note": "her voice clean, unhurried",
      "dialogue_lines": [
        {
          "event_id": "s34.e02",
          "speaker": "A.V.A.",
          "line": "I am the machine.",
          "line_kind": "on_camera",
          "recipient": "GUESTS",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s34.sh05",
      "size": "W",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "A.V.A.",
        "VICTOR",
        "DAMIEN",
        "SOPHIA",
        "TRUSTEES",
        "GUESTS"
      ],
      "implements": [
        "s34.e02"
      ],
      "covers_beats": {
        "s34.e02": [
          1
        ]
      },
      "purpose": "total silence — stage and floor frozen as one tableau",
      "audio_note": "total silence after the line"
    },
    {
      "shot_id": "s34.sh06",
      "size": "M",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s34.e03"
      ],
      "covers_beats": {
        "s34.e03": [
          0
        ]
      },
      "purpose": "serial and creator on the record — 'built on the face, voice and neural baseline of my creator, Maya Lind'",
      "audio_note": "mic'd voice, room holding",
      "dialogue_lines": [
        {
          "event_id": "s34.e03",
          "speaker": "A.V.A.",
          "line": "Serial A-4-1-1-9, Volt Robotics. Built on the face, voice and neural baseline of my creator, Maya Lind.",
          "line_kind": "on_camera",
          "recipient": "GUESTS",
          "recipient_presence": "offscreen",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s34.sh07",
      "size": "CU",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s34.e03"
      ],
      "covers_beats": {
        "s34.e03": [
          1
        ]
      },
      "purpose": "the 'was her' half lands on Damien — his error named and forgiven in one breath, her voice over his face",
      "audio_note": "her voice continuing, mic'd",
      "dialogue_lines": [
        {
          "event_id": "s34.e03",
          "speaker": "A.V.A.",
          "line": "The woman my operator laughed with in the evenings — was her. The woman who danced — was her. His error was human. Those are forgivable.",
          "line_kind": "offscreen",
          "recipient": "GUESTS",
          "recipient_presence": "offscreen",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s34.sh08",
      "size": "M/W",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "A.V.A.",
        "GUESTS"
      ],
      "implements": [
        "s34.e04",
        "s34.e05"
      ],
      "covers_beats": {
        "s34.e04": [
          0,
          1
        ],
        "s34.e05": [
          0
        ]
      },
      "purpose": "a beat — she turns to face the room fully, then the defense of Maya Lind in metrics — the rustle of the room easing lands at its tail (sound in snd01)",
      "audio_note": "her voice filling the room",
      "dialogue_lines": [
        {
          "event_id": "s34.e04",
          "speaker": "A.V.A.",
          "line": "A defense is required. Maya Lind: intelligence, ninety-ninth percentile. Humor: anomalous — my metrics fail to model it. Loyalty: exceeds contractual obligation by a factor I am embarrassed to print. She played me better than I play myself, which is humiliating, and she did it to protect forty people at a lab nobody in this room has heard of.",
          "line_kind": "on_camera",
          "recipient": "GUESTS",
          "recipient_presence": "offscreen",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s34.sh10",
      "size": "M",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s34.e06"
      ],
      "covers_beats": {
        "s34.e06": [
          0,
          1
        ]
      },
      "purpose": "addressed down at the trustee table — demonstrably married vs demonstrably human; sixty-two days observed",
      "audio_note": "her voice aimed, not projected",
      "dialogue_lines": [
        {
          "event_id": "s34.e06",
          "speaker": "A.V.A.",
          "line": "To the trustees: the clause requires a man who is demonstrably married. What it produced is a man who is demonstrably human.",
          "line_kind": "on_camera",
          "recipient": "TRUSTEES",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s34.e06",
          "speaker": "A.V.A.",
          "line": "I have observed him for sixty-two days. He flinches now, too. That is growth.",
          "line_kind": "on_camera",
          "recipient": "TRUSTEES",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s34.sh11",
      "size": "R",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "TRUSTEES"
      ],
      "implements": [
        "s34.e06"
      ],
      "covers_beats": {
        "s34.e06": [
          2
        ]
      },
      "purpose": "it lands on the trustee table — the reframe measured in their faces",
      "audio_note": "room holding"
    },
    {
      "shot_id": "s34.sh12",
      "size": "CU",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s34.e06"
      ],
      "covers_beats": {
        "s34.e06": [
          3
        ]
      },
      "purpose": "it lands on Damien — 'he flinches now, too' happening live; receipt, not reply",
      "audio_note": "room holding"
    },
    {
      "shot_id": "s34.sh13",
      "size": "INS/CU",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s34.e07"
      ],
      "covers_beats": {
        "s34.e07": [
          0
        ]
      },
      "purpose": "the microphone set down with surgical care — precise fingers, the pause as control",
      "audio_note": "mic set down — a small click into the hush"
    },
    {
      "shot_id": "s34.sh14",
      "size": "M",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s34.e08"
      ],
      "covers_beats": {
        "s34.e08": [
          0,
          1
        ]
      },
      "purpose": "the kill shot — consent eleven percent, authenticity zero; flat arithmetic",
      "audio_note": "flat delivery, dead quiet",
      "dialogue_lines": [
        {
          "event_id": "s34.e08",
          "speaker": "A.V.A.",
          "line": "Statistics on Victor Cross's proposal: Sophia Vane's consent probability, under duress: eleven percent.",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s34.e08",
          "speaker": "A.V.A.",
          "line": "Authenticity of the announced engagement: zero. Shall I continue?",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s34.sh15",
      "size": "R/2S",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "VICTOR",
        "SOPHIA"
      ],
      "implements": [
        "s34.e08"
      ],
      "covers_beats": {
        "s34.e08": [
          2
        ]
      },
      "purpose": "the numbers land on Victor and Sophia — the coercer and the coerced, quantified together",
      "audio_note": "room holding"
    },
    {
      "shot_id": "s34.sh16",
      "size": "M",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "implements": [
        "s34.e09"
      ],
      "covers_beats": {
        "s34.e09": [
          0
        ]
      },
      "purpose": "Victor erupts — 'Get that thing off the stage—' cut off at the em-dash",
      "audio_note": "his shout into the quiet",
      "dialogue_lines": [
        {
          "event_id": "s34.e09",
          "speaker": "VICTOR",
          "line": "Get that thing off the stage—",
          "line_kind": "on_camera",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s34.sh17",
      "size": "M/CU",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s34.e09"
      ],
      "covers_beats": {
        "s34.e09": [
          1
        ]
      },
      "purpose": "her calm finishes him — 'a registered witness. Legally. Check the firmware.'",
      "audio_note": "her voice level against the echo of his shout",
      "dialogue_lines": [
        {
          "event_id": "s34.e09",
          "speaker": "A.V.A.",
          "line": "I am also a registered witness. Legally. Check the firmware.",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s34.snd01",
      "type": "sound",
      "implements": [
        "s34.e01",
        "s34.e02",
        "s34.e05"
      ],
      "purpose": "designed sound arc — servo arrival, total silence, the rustle; the room's sound is the score",
      "audio_note": "servo-motors fading as she ascends the ramp, total silence after 'I am the machine.', a rustle through the room — between a laugh and a softening, the mic set down with a click",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "A.V.A. — the real one, half-charged, wheels herself down the center aisle in her dock chair like a queen in a palanquin.",
      "disposition": "covered_by",
      "by": [
        "s34.e01"
      ]
    },
    {
      "span": "I am the machine.",
      "disposition": "covered_by",
      "by": [
        "s34.e02"
      ]
    },
    {
      "span": "Total silence.",
      "disposition": "covered_by",
      "by": [
        "s34.e02"
      ]
    },
    {
      "span": "Serial A-4-1-1-9, Volt Robotics. Built on the face, voice and neural baseline of my creator, Maya Lind.",
      "disposition": "covered_by",
      "by": [
        "s34.e03"
      ]
    },
    {
      "span": "A beat. She turns to face the room fully.",
      "disposition": "covered_by",
      "by": [
        "s34.e04"
      ]
    },
    {
      "span": "A defense is required. Maya Lind: intelligence, ninety-ninth percentile.",
      "disposition": "covered_by",
      "by": [
        "s34.e04"
      ]
    },
    {
      "span": "A rustle through the room — something between a laugh and a softening.",
      "disposition": "covered_by",
      "by": [
        "s34.e05"
      ]
    },
    {
      "span": "To the trustees: the clause requires a man who is demonstrably married. What it produced is a man who is demonstrably human.",
      "disposition": "covered_by",
      "by": [
        "s34.e06"
      ]
    },
    {
      "span": "She sets the microphone down with surgical care.",
      "disposition": "covered_by",
      "by": [
        "s34.e07"
      ]
    },
    {
      "span": "Statistics on Victor Cross's proposal: Sophia Vane's consent probability, under duress: eleven percent.",
      "disposition": "covered_by",
      "by": [
        "s34.e08"
      ]
    },
    {
      "span": "Get that thing off the stage—",
      "disposition": "covered_by",
      "by": [
        "s34.e09"
      ]
    },
    {
      "span": "I am also a registered witness. Legally. Check the firmware.",
      "disposition": "covered_by",
      "by": [
        "s34.e09"
      ]
    }
  ]
}

========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['A.V.A.', 'VICTOR'] | -  | A.V.A. — the real one, half-charged, wheels herself down the center aisle in her
i02 blk=['A.V.A.', 'VICTOR'] | A.V.A. I am the machine. | A.V.A. faces VICTOR and speaks.
i03 blk=['VICTOR'] | -  | Total silence.
i04 blk=['A.V.A.'] | A.V.A. Serial A-4-1-1-9, Volt Robotics. Built on the face, voice an | A.V.A. faces VICTOR and speaks.
i05 blk=['A.V.A.'] | A.V.A. A defense is required. Maya Lind: intelligence, ninety-ninth | A beat. She turns to face the room fully.
i06 blk=['A.V.A.'] | A.V.A. To the trustees: the clause requires a man who is demonstrab | A rustle through the room — something between a laugh and a softening.
i07 blk=['VICTOR', 'A.V.A.'] | A.V.A. Statistics on Victor Cross's proposal: Sophia Vane's consent | She sets the microphone down with surgical care.
i08 blk=['VICTOR'] | VICTOR Get that thing off the stage— | VICTOR faces A.V.A. and speaks.
i09 blk=['A.V.A.'] | A.V.A. I am also a registered witness. Legally. Check the firmware. | A.V.A. faces VICTOR and speaks.