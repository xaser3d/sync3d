# VALIDATION PACKET — scene s33
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 33 — INT. GRAND BALLROOM — THE BIRTHDAY GALA — NIGHT

*The deadline gala — Damien's 32nd birthday, the trust's trigger
date. Five hundred guests, a stage, a screen the size of a bus.
The trustees sit at a front table like a tribunal. DAMIEN stands
at the stage edge — tonight he either announces a marriage or
loses the empire.*

*VICTOR takes the stage first, all warmth and brotherhood.*

VICTOR
Before the toast — a gift. My brother's companionship these
months has been remarkable. You all noticed. He smiles. He dances.
He — forgive the word — *feels*.

*Polite laughter. Damien, offstage, feels the floor tilt before
he knows why.*

VICTOR (CONT'D)
So in the spirit of transparency — the trustees' favorite word —
a small demonstration of what made it possible.

*The screen lights up. The service-corridor photo fills it: two
identical women — one rigid on a gurney, one alive and adjusting
her dress.*

VICTOR (CONT'D)
Ladies and gentlemen — the companion is a fraud. The robot you
applauded is a woman. A paid performer. My brother has been
"coached" by a person pretending to be a machine — which, I
believe, makes his engagement prospects, and his claim on this
trust, somewhat... theatrical.

*The room detonates — whispers, flashbulbs, the trustees going
very still. Damien stands motionless. On the service level, MAYA
watches the screen — her face, doubled, on a wall ten meters tall.*

VICTOR (CONT'D)
But the clause can still be honored tonight — that's the comedy
of it. Because, ladies and gentlemen, I'm also delighted to
announce my brother's engagement — to a woman of impeccable,
human, unquestionably organic standing.

*He extends a hand to the wings. SOPHIA VANE steps out — in white,
in front of everyone, pre-written press already releasing on
phones around the room.*

VICTOR (CONT'D)
Sophia Vane. Sign tonight, brother, and the clause is satisfied.
Marry a real woman — even a reluctant one — and you keep it all.
That's the letter of the law your father wrote.

*The trap is laid out before the whole city: sign with the fake
bride, or lose everything. Damien looks at the screen — at the
two faces. At Sophia, standing in white like a hostage. At the
trustees, who are doing math.*

*Then — from the back of the ballroom — a sound. Servo-motors.
A power chair ascending the aisle on its own.*

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 33,
  "scene_heading": "SCENE 33 — INT. GRAND BALLROOM — THE BIRTHDAY GALA — NIGHT",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "Act-3 opening set piece — the deadline gala itself, the trust's trigger date. Victor stages the public execution exactly as narrated in S32: the photo on a screen the size of a bus, the 'fraud' speech, the pre-arranged engagement to Sophia in white, press already releasing on phones. The trap is complete until a sound arrives from the back of the ballroom: servo-motors, and a power chair ascending the aisle on its own.",
  "zones": [
    "stage",
    "ballroom floor",
    "service level"
  ],
  "events": [
    {
      "event_id": "s33.e01",
      "source_evidence": [
        "The deadline gala — Damien's 32nd birthday, the trust's trigger date.",
        "Five hundred guests, a stage, a screen the size of a bus.",
        "The trustees sit at a front table like a tribunal.",
        "DAMIEN stands at the stage edge — tonight he either announces a marriage or loses the empire."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "establish the stakes frame — the trigger date, the tribunal, the man at the edge",
      "participants": [
        "DAMIEN",
        "GUESTS",
        "TRUSTEES"
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
          "beat": "the deadline gala at scale — five hundred guests, a screen like a bus",
          "type": "atmosphere"
        },
        {
          "beat": "the trustees — a front table like a tribunal",
          "type": "reveal"
        },
        {
          "beat": "Damien at the stage edge — announce a marriage or lose the empire",
          "type": "held_reaction"
        }
      ],
      "visual_requirements": [
        "the empty dark screen must read — it is the scene's loaded gun",
        "the trustee table composed like a tribunal, not like guests"
      ],
      "audio_requirements": [
        "gala murmur, glasses, scale"
      ],
      "continuity_constraints": [
        "the screen is the one Victor requisitioned in S32 — size established here before it lights"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "TRUSTEES"
      ],
      "tableau": true,
      "shot_sequence": [
        "s33.sh01",
        "s33.sh02"
      ]
    },
    {
      "event_id": "s33.e02",
      "source_evidence": [
        "VICTOR takes the stage first, all warmth and brotherhood.",
        "Before the toast — a gift. My brother's companionship these months has been remarkable. You all noticed. He smiles. He dances. He — forgive the word — *feels*.",
        "Polite laughter. Damien, offstage, feels the floor tilt before he knows why."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the knife wrapped as a toast — warmth, brotherhood, and the word 'feels' aimed at the machine",
      "participants": [
        "VICTOR",
        "DAMIEN",
        "GUESTS"
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
          "beat": "Victor takes the stage — all warmth and brotherhood",
          "type": "action"
        },
        {
          "beat": "the gift speech — 'He smiles. He dances. He — forgive the word — *feels*.'",
          "type": "dialogue"
        },
        {
          "beat": "polite laughter",
          "type": "reaction"
        },
        {
          "beat": "Damien, offstage — the floor tilts before he knows why",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "Victor's warmth must be buyable — the room laughs politely because the trap is invisible",
        "Damien's tilt is interior — a small shift, not a reaction shot played big"
      ],
      "audio_requirements": [
        "polite laughter under the speech"
      ],
      "continuity_constraints": [
        "Damien is at the stage edge, offstage — physically present, outside the spotlight"
      ],
      "ambiguities": [],
      "must_appear": [
        "VICTOR",
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s33.sh03",
        "s33.sh04",
        "s33.sh06",
        "s33.snd01"
      ]
    },
    {
      "event_id": "s33.e03",
      "source_evidence": [
        "So in the spirit of transparency — the trustees' favorite word — a small demonstration of what made it possible."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "he names the jury — 'transparency' is the trustees' word thrown back at them",
      "participants": [
        "VICTOR",
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
          "beat": "the transparency line — aimed at the trustees' table",
          "type": "dialogue"
        },
        {
          "beat": "the trustees take it — thin smiles, no warmth",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "the joke lands on the trustee table — their reaction is the definition being cited"
      ],
      "audio_requirements": [],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "VICTOR",
        "TRUSTEES"
      ],
      "tableau": false,
      "shot_sequence": [
        "s33.sh07",
        "s33.sh08"
      ],
      "decisions": [
        {
          "topic": "trustee reaction at the transparency joke (sh08)",
          "status": "resolved-decision",
          "decision": "keep sh08 as its own plan — trustees as complicit audience: thin smiles, no warmth, the joke landing on their favorite word",
          "basis": "screenplay_text",
          "consequence": "distinct from sh21's jury-mode math; trustee arc held as three states: laugh (sh08) -> stillness at the detonation (sh12) -> math (sh21); do not collapse into one generic 'trustee reaction'"
        }
      ]
    },
    {
      "event_id": "s33.e04",
      "source_evidence": [
        "The screen lights up. The service-corridor photo fills it: two identical women — one rigid on a gurney, one alive and adjusting her dress."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the evidence goes public — the S31 frame at the size of a bus",
      "participants": [
        "VICTOR",
        "DAMIEN",
        "GUESTS"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "MAYA",
            "A.V.A."
          ],
          "seen_by": [
            "VICTOR",
            "DAMIEN",
            "GUESTS"
          ],
          "channel": "ballroom screen",
          "from_zone": "stage"
        }
      ],
      "location": {
        "zones": [
          "stage",
          "ballroom floor"
        ],
        "primary": "stage"
      },
      "timeline": [
        {
          "beat": "the screen lights — the service-corridor photo fills it",
          "type": "insert"
        },
        {
          "beat": "the room sees two identical women",
          "type": "reveal"
        }
      ],
      "visual_requirements": [
        "the photo legible at gala scale — gurney, corridor, the double",
        "screen and room both present in coverage — the image and the seeing of it"
      ],
      "audio_requirements": [
        "the screen's power-up thrum before the room reacts"
      ],
      "continuity_constraints": [
        "identical frame to S32's office screen — the same photograph, now public"
      ],
      "ambiguities": [],
      "must_appear": [],
      "tableau": false,
      "shot_sequence": [
        "s33.sh09",
        "s33.sh10"
      ]
    },
    {
      "event_id": "s33.e05",
      "source_evidence": [
        "Ladies and gentlemen — the companion is a fraud. The robot you applauded is a woman. A paid performer. My brother has been \"coached\" by a person pretending to be a machine — which, I believe, makes his engagement prospects, and his claim on this trust, somewhat... theatrical."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the charge spoken over the evidence — fraud, performer, and the claim called 'theatrical'",
      "participants": [
        "VICTOR"
      ],
      "remote_participants": [],
      "location": {
        "zone": "stage"
      },
      "timeline": [
        {
          "beat": "the fraud speech — companion, performer, 'theatrical'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Victor beside his own evidence — prosecution theater, not anger"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "this is the 'detonates on a stage' half of the S32 plan being executed verbatim"
      ],
      "ambiguities": [],
      "must_appear": [
        "VICTOR"
      ],
      "tableau": false,
      "shot_sequence": [
        "s33.sh11"
      ]
    },
    {
      "event_id": "s33.e06",
      "source_evidence": [
        "The room detonates — whispers, flashbulbs, the trustees going very still.",
        "Damien stands motionless.",
        "On the service level, MAYA watches the screen — her face, doubled, on a wall ten meters tall."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "three detonations at once — the room erupts, Damien freezes, and Maya watches herself become evidence",
      "participants": [
        "GUESTS",
        "TRUSTEES",
        "DAMIEN",
        "MAYA"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "MAYA",
            "A.V.A."
          ],
          "seen_by": [
            "MAYA"
          ],
          "channel": "ballroom screen",
          "from_zone": "service level"
        }
      ],
      "location": {
        "zones": [
          "ballroom floor",
          "service level",
          "stage"
        ],
        "primary": "ballroom floor"
      },
      "timeline": [
        {
          "beat": "the room detonates — whispers, flashbulbs",
          "type": "reaction"
        },
        {
          "beat": "the trustees go very still",
          "type": "held_reaction"
        },
        {
          "beat": "Damien stands motionless",
          "type": "held_reaction"
        },
        {
          "beat": "Maya on the service level — her face, doubled, ten meters tall",
          "type": "reveal"
        }
      ],
      "visual_requirements": [
        "stillness inside the detonation — trustees and Damien are the calm the noise is measured against",
        "Maya's doubled face on the screen is the scene's deepest frame — she watches herself become the evidence"
      ],
      "audio_requirements": [
        "detonation — whispers, flashbulb chatter, phones"
      ],
      "continuity_constraints": [
        "Maya is still on the service level vantage established earlier — she is physical, not remote",
        "the frozen woman on the gurney in the photo is A.V.A.; the live one is Maya — blocking keeps the double readable"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "MAYA",
        "TRUSTEES"
      ],
      "tableau": false,
      "shot_sequence": [
        "s33.sh12",
        "s33.sh13",
        "s33.sh14",
        "s33.snd01"
      ]
    },
    {
      "event_id": "s33.e07",
      "source_evidence": [
        "But the clause can still be honored tonight — that's the comedy of it. Because, ladies and gentlemen, I'm also delighted to announce my brother's engagement — to a woman of impeccable, human, unquestionably organic standing."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the pivot — the same clause that condemns Damien is offered back as his rescue",
      "participants": [
        "VICTOR",
        "GUESTS"
      ],
      "remote_participants": [],
      "location": {
        "zone": "stage"
      },
      "timeline": [
        {
          "beat": "the engagement announcement — 'impeccable, human, unquestionably organic'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the word 'organic' played as a compliment — the insult is inside the adjective list"
      ],
      "audio_requirements": [],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "VICTOR"
      ],
      "tableau": false,
      "shot_sequence": [
        "s33.sh15"
      ]
    },
    {
      "event_id": "s33.e08",
      "source_evidence": [
        "He extends a hand to the wings. SOPHIA VANE steps out — in white, in front of everyone, pre-written press already releasing on phones around the room."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the bride produced on cue — her entrance and the press release were prepared before she was asked",
      "participants": [
        "VICTOR",
        "SOPHIA",
        "GUESTS"
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
          "beat": "Victor extends a hand to the wings",
          "type": "action"
        },
        {
          "beat": "Sophia Vane steps out — in white, in front of everyone",
          "type": "reveal"
        },
        {
          "beat": "pre-written press releasing on phones around the room",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "the white dress reads bridal before a word is said — costume as fait accompli",
        "phones lighting around the room — the press was pre-written; the engagement predates consent"
      ],
      "audio_requirements": [
        "phones buzzing — press notifications"
      ],
      "continuity_constraints": [
        "the 'she'll say yes to anything' leverage from S32 is now on stage",
        "the gurney photo stays on the screen behind the bride — the two exhibits share the stage"
      ],
      "ambiguities": [],
      "must_appear": [
        "SOPHIA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s33.sh16",
        "s33.sh17",
        "s33.snd01"
      ]
    },
    {
      "event_id": "s33.e09",
      "source_evidence": [
        "Sophia Vane. Sign tonight, brother, and the clause is satisfied. Marry a real woman — even a reluctant one — and you keep it all. That's the letter of the law your father wrote."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the terms dictated to Damien in front of the city — 'even a reluctant one' admits the coercion aloud",
      "participants": [
        "VICTOR",
        "SOPHIA",
        "DAMIEN"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "DAMIEN"
      ],
      "location": {
        "zone": "stage"
      },
      "timeline": [
        {
          "beat": "the terms — sign tonight, marry a real woman, keep it all",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Sophia beside him as exhibit B — the reluctant bride standing inside her own leverage"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "'your father wrote' — the clause is the dead father's law, established backstory"
      ],
      "ambiguities": [],
      "must_appear": [
        "VICTOR",
        "SOPHIA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s33.sh18"
      ]
    },
    {
      "event_id": "s33.e10",
      "source_evidence": [
        "The trap is laid out before the whole city: sign with the fake bride, or lose everything.",
        "Damien looks at the screen — at the two faces.",
        "At Sophia, standing in white like a hostage.",
        "At the trustees, who are doing math."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the ultimatum mapped — Damien's look tours the three exhibits: the evidence, the bride, the jury",
      "participants": [
        "DAMIEN",
        "SOPHIA",
        "TRUSTEES"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "MAYA",
            "A.V.A."
          ],
          "seen_by": [
            "DAMIEN"
          ],
          "channel": "ballroom screen",
          "from_zone": "stage"
        }
      ],
      "location": {
        "zones": [
          "stage",
          "ballroom floor"
        ],
        "primary": "stage"
      },
      "timeline": [
        {
          "beat": "the trap legible to the whole city — sign or lose everything",
          "type": "held_image"
        },
        {
          "beat": "Damien looks at the screen — the two faces",
          "type": "action"
        },
        {
          "beat": "Sophia in white like a hostage",
          "type": "held_reaction"
        },
        {
          "beat": "the trustees doing math",
          "type": "held_reaction"
        }
      ],
      "visual_requirements": [
        "the look is the spine — three targets, three holds; the room reads what Damien is choosing between",
        "Sophia held 'like a hostage' — her stillness is the tell, not her expression"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the screen still holds the corridor photo — Damien looks at the same two faces we saw in S32"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "SOPHIA",
        "TRUSTEES"
      ],
      "tableau": false,
      "shot_sequence": [
        "s33.sh19",
        "s33.sh20",
        "s33.sh21"
      ],
      "decisions": [
        {
          "topic": "trustee reaction at the mapped ultimatum (sh21)",
          "status": "resolved-decision",
          "decision": "keep sh21 as its own plan — trustees as the deciding jury, doing math under Damien's look",
          "basis": "screenplay_text",
          "consequence": "the power shift the scene exists for; trustee arc held as three states: laugh (sh08) -> stillness at the detonation (sh12) -> math (sh21); do not collapse into one generic 'trustee reaction'"
        }
      ]
    },
    {
      "event_id": "s33.e11",
      "source_evidence": [
        "Then — from the back of the ballroom — a sound. Servo-motors.",
        "A power chair ascending the aisle on its own."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the cliffhanger — the trap's subject answers by arriving; the machine wheels herself in",
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
          "beat": "a sound from the back of the ballroom — servo-motors",
          "type": "sound"
        },
        {
          "beat": "a power chair ascending the aisle on its own",
          "type": "reveal"
        },
        {
          "beat": "the room turns toward the sound",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "the chair reads before the occupant — from behind, a silhouette ascending the aisle",
        "'on its own' is the room's read — coverage withholds her face without hiding the chair"
      ],
      "audio_requirements": [
        "servo-motors rising from the back of the hall"
      ],
      "continuity_constraints": [
        "the occupant is A.V.A. — confirmed 'the real one' at S34's first line; her presence is declared, her reveal withheld"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s33.sh22",
        "s33.snd01"
      ],
      "decisions": [
        {
          "topic": "power-chair occupant",
          "status": "resolved-decision",
          "decision": "keep the occupant a rear-view silhouette only — no profile, no face reveal inside S33; identity opens S34",
          "basis": "screenplay_text",
          "consequence": "sh22 coverage stays back-of-chair/servo-sound framing; no insert may resolve her face before scene 34's 'the real one'",
          "resolved_from": "the screenplay withholds the occupant ('on its own'); whether a profile hint is allowed"
        }
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s33.sh01",
      "size": "EST/W",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "GUESTS",
        "TRUSTEES"
      ],
      "implements": [
        "s33.e01"
      ],
      "covers_beats": {
        "s33.e01": [
          0,
          1
        ]
      },
      "purpose": "the gala at scale — five hundred guests, the dark screen like a bus, trustees composed as a tribunal",
      "audio_note": "gala murmur, glasses"
    },
    {
      "shot_id": "s33.sh02",
      "size": "M",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s33.e01"
      ],
      "covers_beats": {
        "s33.e01": [
          2
        ]
      },
      "purpose": "Damien alone at the stage edge — announce or lose the empire",
      "audio_note": "gala murmur"
    },
    {
      "shot_id": "s33.sh03",
      "size": "M/W",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "implements": [
        "s33.e02"
      ],
      "covers_beats": {
        "s33.e02": [
          0
        ]
      },
      "purpose": "Victor takes the stage first — warmth and brotherhood as a performance",
      "audio_note": "room settling"
    },
    {
      "shot_id": "s33.sh04",
      "size": "M/W",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "VICTOR",
        "GUESTS"
      ],
      "implements": [
        "s33.e02"
      ],
      "covers_beats": {
        "s33.e02": [
          1,
          2
        ]
      },
      "purpose": "the gift speech — 'he smiles, he dances, he *feels*' — the knife inside the toast; the room's polite laughter lands inside the same frame, the trap invisible",
      "audio_note": "his voice warm over the room",
      "dialogue_lines": [
        {
          "event_id": "s33.e02",
          "speaker": "VICTOR",
          "line": "Before the toast — a gift. My brother's companionship these months has been remarkable. You all noticed. He smiles. He dances. He — forgive the word — *feels*.",
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
      "shot_id": "s33.sh06",
      "size": "CU",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s33.e02"
      ],
      "covers_beats": {
        "s33.e02": [
          3
        ]
      },
      "purpose": "Damien at the stage edge — the floor tilts before he knows why; small, interior",
      "audio_note": "laughter distant around him"
    },
    {
      "shot_id": "s33.sh07",
      "size": "M",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "implements": [
        "s33.e03"
      ],
      "covers_beats": {
        "s33.e03": [
          0
        ]
      },
      "purpose": "'the spirit of transparency' — the trustees' word thrown back at their table",
      "audio_note": "murmur",
      "dialogue_lines": [
        {
          "event_id": "s33.e03",
          "speaker": "VICTOR",
          "line": "So in the spirit of transparency — the trustees' favorite word — a small demonstration of what made it possible.",
          "line_kind": "on_camera",
          "recipient": "TRUSTEES",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s33.sh08",
      "size": "R",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "TRUSTEES"
      ],
      "implements": [
        "s33.e03"
      ],
      "covers_beats": {
        "s33.e03": [
          1
        ]
      },
      "purpose": "the trustee table takes the joke — thin smiles, no warmth",
      "audio_note": "murmur"
    },
    {
      "shot_id": "s33.sh09",
      "size": "INS",
      "zone": "stage",
      "type": "visual",
      "participants": [],
      "depicts": [
        {
          "actors": [
            "MAYA",
            "A.V.A."
          ],
          "channel": "ballroom screen"
        }
      ],
      "implements": [
        "s33.e04"
      ],
      "covers_beats": {
        "s33.e04": [
          0
        ]
      },
      "purpose": "the screen lights — the service-corridor photo fills it; gurney, corridor, the double at the size of a bus",
      "audio_note": "the screen's power-up thrum"
    },
    {
      "shot_id": "s33.sh10",
      "size": "W",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "VICTOR",
        "DAMIEN",
        "GUESTS"
      ],
      "implements": [
        "s33.e04"
      ],
      "covers_beats": {
        "s33.e04": [
          1
        ]
      },
      "purpose": "the room sees two identical women — Victor beside his evidence, Damien at the edge, five hundred heads up",
      "audio_note": "the first whispers beginning"
    },
    {
      "shot_id": "s33.sh11",
      "size": "M",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "VICTOR"
      ],
      "implements": [
        "s33.e05"
      ],
      "covers_beats": {
        "s33.e05": [
          0
        ]
      },
      "purpose": "the fraud speech — prosecution theater beside his own evidence",
      "audio_note": "his voice over the rising whispers",
      "dialogue_lines": [
        {
          "event_id": "s33.e05",
          "speaker": "VICTOR",
          "line": "Ladies and gentlemen — the companion is a fraud. The robot you applauded is a woman. A paid performer. My brother has been \"coached\" by a person pretending to be a machine — which, I believe, makes his engagement prospects, and his claim on this trust, somewhat... theatrical.",
          "line_kind": "on_camera",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s33.sh12",
      "size": "W/R",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "GUESTS",
        "TRUSTEES"
      ],
      "implements": [
        "s33.e06"
      ],
      "covers_beats": {
        "s33.e06": [
          0,
          1
        ]
      },
      "purpose": "the room detonates — whispers and flashbulbs around the trustee table gone very still",
      "audio_note": "whispers, flashbulb chatter, phones"
    },
    {
      "shot_id": "s33.sh13",
      "size": "CU",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s33.e06"
      ],
      "covers_beats": {
        "s33.e06": [
          2
        ]
      },
      "purpose": "Damien motionless — the still center the detonation is measured against",
      "audio_note": "the room noise around him"
    },
    {
      "shot_id": "s33.sh14",
      "size": "M",
      "zone": "service level",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "depicts": [
        {
          "actors": [
            "MAYA",
            "A.V.A."
          ],
          "channel": "ballroom screen"
        }
      ],
      "implements": [
        "s33.e06"
      ],
      "covers_beats": {
        "s33.e06": [
          3
        ]
      },
      "purpose": "Maya on the service level watching her own face doubled on a wall ten meters tall — she has become the evidence",
      "audio_note": "the detonation below, distant"
    },
    {
      "shot_id": "s33.sh15",
      "size": "M/W",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "VICTOR",
        "GUESTS"
      ],
      "implements": [
        "s33.e07"
      ],
      "covers_beats": {
        "s33.e07": [
          0
        ]
      },
      "purpose": "the pivot — the same clause offered back as rescue; 'organic' played as a compliment",
      "audio_note": "the room leaning in",
      "dialogue_lines": [
        {
          "event_id": "s33.e07",
          "speaker": "VICTOR",
          "line": "But the clause can still be honored tonight — that's the comedy of it. Because, ladies and gentlemen, I'm also delighted to announce my brother's engagement — to a woman of impeccable, human, unquestionably organic standing.",
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
      "shot_id": "s33.sh16",
      "size": "M/W",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "VICTOR",
        "SOPHIA"
      ],
      "implements": [
        "s33.e08"
      ],
      "covers_beats": {
        "s33.e08": [
          0,
          1
        ]
      },
      "purpose": "the hand to the wings — Sophia steps out in white, bridal before a word is said, the photo still on the screen behind her",
      "audio_note": "a breath through the room"
    },
    {
      "shot_id": "s33.sh17",
      "size": "INS",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "GUESTS"
      ],
      "implements": [
        "s33.e08"
      ],
      "covers_beats": {
        "s33.e08": [
          2
        ]
      },
      "purpose": "phones lighting around the room — the press release was written before she was asked",
      "audio_note": "phones buzzing — press notifications"
    },
    {
      "shot_id": "s33.sh18",
      "size": "M-2S",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "VICTOR",
        "SOPHIA"
      ],
      "implements": [
        "s33.e09"
      ],
      "covers_beats": {
        "s33.e09": [
          0
        ]
      },
      "purpose": "the terms dictated — Sophia beside him as exhibit B; 'even a reluctant one' admits it aloud",
      "audio_note": "his voice, the room silent now",
      "dialogue_lines": [
        {
          "event_id": "s33.e09",
          "speaker": "VICTOR",
          "line": "Sophia Vane. Sign tonight, brother, and the clause is satisfied. Marry a real woman — even a reluctant one — and you keep it all. That's the letter of the law your father wrote.",
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
      "shot_id": "s33.sh19",
      "size": "CU",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "depicts": [
        {
          "actors": [
            "MAYA",
            "A.V.A."
          ],
          "channel": "ballroom screen"
        }
      ],
      "implements": [
        "s33.e10"
      ],
      "covers_beats": {
        "s33.e10": [
          0,
          1
        ]
      },
      "purpose": "Damien's look — the trap legible, then his eyes to the screen's two faces",
      "audio_note": "the room holding"
    },
    {
      "shot_id": "s33.sh20",
      "size": "M",
      "zone": "stage",
      "type": "visual",
      "participants": [
        "SOPHIA"
      ],
      "implements": [
        "s33.e10"
      ],
      "covers_beats": {
        "s33.e10": [
          2
        ]
      },
      "purpose": "Sophia in white like a hostage — stillness as the tell",
      "audio_note": "room hush"
    },
    {
      "shot_id": "s33.sh21",
      "size": "M",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "TRUSTEES"
      ],
      "implements": [
        "s33.e10"
      ],
      "covers_beats": {
        "s33.e10": [
          3
        ]
      },
      "purpose": "the trustees doing math — the jury's arithmetic visible on their faces",
      "audio_note": "room hush"
    },
    {
      "shot_id": "s33.sh22",
      "size": "W",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "A.V.A.",
        "GUESTS"
      ],
      "implements": [
        "s33.e11"
      ],
      "covers_beats": {
        "s33.e11": [
          0,
          1,
          2
        ]
      },
      "purpose": "from behind — a power chair ascending the aisle on its own, occupant a withheld silhouette; servo-motors first, then five hundred heads turning toward the sound",
      "audio_note": "servo-motors under the hush, the room's turn rustling through it"
    },
    {
      "shot_id": "s33.snd01",
      "type": "sound",
      "implements": [
        "s33.e02",
        "s33.e06",
        "s33.e08",
        "s33.e11"
      ],
      "purpose": "gala soundscape — polite laughter, the detonation, the phones, and the servo-motors that end the scene",
      "audio_note": "polite laughter under the speech, the detonation — whispers and flashbulb chatter, phones buzzing with press notifications, servo-motors rising from the back of the hall",
      "no_score": false
    }
  ],
  "coverage": [
    {
      "span": "The deadline gala — Damien's 32nd birthday, the trust's trigger date.",
      "disposition": "covered_by",
      "by": [
        "s33.e01"
      ]
    },
    {
      "span": "VICTOR takes the stage first, all warmth and brotherhood.",
      "disposition": "covered_by",
      "by": [
        "s33.e02"
      ]
    },
    {
      "span": "Before the toast — a gift. My brother's companionship these months has been remarkable.",
      "disposition": "covered_by",
      "by": [
        "s33.e02"
      ]
    },
    {
      "span": "Polite laughter. Damien, offstage, feels the floor tilt before he knows why.",
      "disposition": "covered_by",
      "by": [
        "s33.e02"
      ]
    },
    {
      "span": "So in the spirit of transparency — the trustees' favorite word —",
      "disposition": "covered_by",
      "by": [
        "s33.e03"
      ]
    },
    {
      "span": "The screen lights up. The service-corridor photo fills it: two identical women — one rigid on a gurney, one alive and adjusting her dress.",
      "disposition": "covered_by",
      "by": [
        "s33.e04"
      ]
    },
    {
      "span": "the companion is a fraud. The robot you applauded is a woman.",
      "disposition": "covered_by",
      "by": [
        "s33.e05"
      ]
    },
    {
      "span": "The room detonates — whispers, flashbulbs, the trustees going very still. Damien stands motionless.",
      "disposition": "covered_by",
      "by": [
        "s33.e06"
      ]
    },
    {
      "span": "But the clause can still be honored tonight — that's the comedy of it.",
      "disposition": "covered_by",
      "by": [
        "s33.e07"
      ]
    },
    {
      "span": "SOPHIA VANE steps out — in white, in front of everyone, pre-written press already releasing on phones around the room.",
      "disposition": "covered_by",
      "by": [
        "s33.e08"
      ]
    },
    {
      "span": "Sophia Vane. Sign tonight, brother, and the clause is satisfied.",
      "disposition": "covered_by",
      "by": [
        "s33.e09"
      ]
    },
    {
      "span": "The trap is laid out before the whole city: sign with the fake bride, or lose everything.",
      "disposition": "covered_by",
      "by": [
        "s33.e10"
      ]
    },
    {
      "span": "Then — from the back of the ballroom — a sound. Servo-motors. A power chair ascending the aisle on its own.",
      "disposition": "covered_by",
      "by": [
        "s33.e11"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['DAMIEN'] | -  | The deadline gala — Damien's 32nd birthday, the trust's trigger date. Five hundr
i02 blk=['VICTOR', 'DAMIEN'] | VICTOR Before the toast — a gift. My brother's companionship these  | VICTOR takes the stage first, all warmth and brotherhood.
i03 blk=['VICTOR'] | VICTOR So in the spirit of transparency — the trustees' favorite wo | Polite laughter. Damien, offstage, feels the floor tilt before he knows why.
i04 blk=['DAMIEN'] | -  | The screen lights up. The service-corridor photo fills it: two identical women —
i05 blk=['VICTOR'] | VICTOR Ladies and gentlemen — the companion is a fraud. The robot y | VICTOR faces DAMIEN and speaks.
i06 blk=['MAYA', 'DAMIEN'] | -  | The room detonates — whispers, flashbulbs, the trustees going very still. Damien
i07 blk=['VICTOR'] | VICTOR But the clause can still be honored tonight — that's the com | VICTOR faces DAMIEN and speaks.
i08 blk=['SOPHIA'] | -  | He extends a hand to the wings. SOPHIA VANE steps out — in white, in front of ev
i09 blk=['SOPHIA', 'VICTOR'] | VICTOR Sophia Vane. Sign tonight, brother, and the clause is satisf | VICTOR faces DAMIEN and speaks.
i10 blk=['DAMIEN', 'SOPHIA'] | -  | The trap is laid out before the whole city: sign with the fake bride, or lose ev
i11 blk=['DAMIEN'] | -  | Then — from the back of the ballroom — a sound. Servo-motors. A power chair asce