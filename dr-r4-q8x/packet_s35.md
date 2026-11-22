# VALIDATION PACKET — scene s35
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 35 — INT. BALLROOM — CONTINUOUS

*The room is a held breath. DAMIEN walks slowly onto the stage —
past Victor, past Sophia, to the microphone A.V.A. left standing.*

DAMIEN
The clause is real. So is the fraud — the lab lied, the evenings
were a person, and I paid for a coach who turned out to be...

*He stops. Finds the word.*

DAMIEN (CONT'D)
...the first thing in years I didn't want to return for warranty
service.

*Laughter — real, surprised laughter, breaking the tension.*

DAMIEN (CONT'D)
Victor offers a solution: sign tonight, marry a stranger who
doesn't want me, satisfy the letter, keep the company. It's a
good deal. I've done deals like it my whole life — I've been
a deal like it my whole life.

*He looks at Sophia — and she looks back, waiting, terrified.*

DAMIEN (CONT'D)
Sophia — you're free to sit down. You don't owe my brother your
estate. (to the trustees) The loan paper on the Vane property —
held by a shell that traces to my brother — is about to become
a very public document. Maya's lab saw to that this morning.
She doesn't like being managed either.

*Sophia stands a second longer — then takes off the white veil,
hands it to Victor, and walks off the stage to the first applause
of the night.*

DAMIEN (CONT'D)
Now — the clause. "Married and demonstrably so." My father
anticipated a technicality. He wrote a second page of adjectives,
and I've read it every night for eight weeks. He didn't want a
wife-shaped signature. He wanted a son who could stand in a room
like this and tell the truth in front of people who could
destroy him.

*He takes the trust documents from the trustee table. Holds them.*

DAMIEN (CONT'D)
I can't produce a marriage tonight. I won't produce a fake one.
The clause drops — and I let it.

*He sets the documents down. The room is silent — the empire,
surrendered on a stage.*

DAMIEN (CONT'D)
I spent thirty-one years being the most optimized man in any
room. It took a defective robot and the woman inside her to
demonstrate the flaw in the product. Father — wherever the
adjectives came from — the clause worked. Just not the way
the lawyers meant.

*He steps down. The trustees confer — agitated, urgent. PENHALIGON,
ancient and delighted, raises one finger for silence.*

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 35,
  "scene_heading": "INT. BALLROOM — CONTINUOUS",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "Act-3 reversal, continuous on A.V.A.'s public unmasking of Victor's scheme. Damien takes the stage and confesses the fraud himself, frees Sophia, exposes Victor's shell, and lets the clause drop rather than produce a fake marriage — the empire is surrendered on a stage. Ends with the trustees conferring and Penhaligon raising one finger for silence, handing the room to scene 36's ruling.",
  "zones": [
    "ballroom stage",
    "trustee table",
    "ballroom floor"
  ],
  "events": [
    {
      "event_id": "s35.e01",
      "source_evidence": [
        "*The room is a held breath. DAMIEN walks slowly onto the stage — past Victor, past Sophia, to the microphone A.V.A. left standing.*"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "held breath — the confession begins as a walk; Damien claims the mic A.V.A. abandoned",
      "participants": [
        "DAMIEN",
        "VICTOR",
        "SOPHIA",
        "A.V.A.",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "A.V.A."
      ],
      "location": {
        "zones": [
          "ballroom stage",
          "ballroom floor"
        ],
        "primary": "ballroom stage"
      },
      "timeline": [
        {
          "beat": "the room is a held breath",
          "type": "atmosphere"
        },
        {
          "beat": "Damien walks slowly onto the stage — past Victor, past Sophia",
          "type": "action"
        },
        {
          "beat": "arrives at the microphone A.V.A. left standing",
          "type": "held_image"
        }
      ],
      "visual_requirements": [
        "the walk crosses the stage — Victor and Sophia are passed, not addressed",
        "the abandoned mic reads as scene-34 evidence: she stepped away mid-verdict"
      ],
      "audio_requirements": [
        "held-breath room tone"
      ],
      "continuity_constraints": [
        "Victor and Sophia are still on stage from scene 34 — the walk passes both"
      ],
      "ambiguities": [
        "A.V.A.'s position after leaving the mic is unspecified — modeled present-but-unseen; if she exited the stage entirely, drop her from participants"
      ],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": true,
      "shot_sequence": [
        "s35.sh02",
        "s35.snd01"
      ],
      "decisions": [
        {
          "topic": "held-breath room as separate atmosphere plan (sh01)",
          "status": "resolved-decision",
          "decision": "merge the held breath into the W walk frame — the room's suspension is the same continuous moment as Damien's walk to the abandoned mic; no editorial pause justifies a separate plan",
          "basis": "director_choice",
          "consequence": "sh02 covers beats 0-2 of e01: held breath, the walk past Victor and Sophia, arrival at the mic A.V.A. left standing — the W frame must read the stopped room around the walk"
        }
      ]
    },
    {
      "event_id": "s35.e02",
      "source_evidence": [
        "DAMIEN\nThe clause is real. So is the fraud — the lab lied, the evenings\nwere a person, and I paid for a coach who turned out to be..."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "public confession — he names the fraud before anyone can charge him with it, and trails off mid-list",
      "participants": [
        "DAMIEN",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "GUESTS"
      ],
      "location": {
        "zone": "ballroom stage"
      },
      "timeline": [
        {
          "beat": "the confession, cut off mid-list — 'turned out to be...'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "held on him — no cutaway; the room has not earned a reaction frame yet"
      ],
      "audio_requirements": [
        "close dry mic over a silent room"
      ],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s35.sh03"
      ]
    },
    {
      "event_id": "s35.e03",
      "source_evidence": [
        "*He stops. Finds the word.*",
        "DAMIEN (CONT'D)\n...the first thing in years I didn't want to return for warranty\nservice.",
        "*Laughter — real, surprised laughter, breaking the tension.*"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the pivot word — the joke that turns the room from tribunal back into an audience",
      "participants": [
        "DAMIEN",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "location": {
        "zones": [
          "ballroom stage",
          "ballroom floor"
        ],
        "primary": "ballroom stage"
      },
      "timeline": [
        {
          "beat": "he stops — finds the word",
          "type": "held_action"
        },
        {
          "beat": "'warranty service' lands",
          "type": "dialogue"
        },
        {
          "beat": "laughter — real, surprised, breaking the tension",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "the pause is its own beat — the search for the word is visible",
        "laughter is a room frame, not a close-up on him"
      ],
      "audio_requirements": [
        "real surprised laughter breaking tension"
      ],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "GUESTS"
      ],
      "tableau": false,
      "shot_sequence": [
        "s35.sh04",
        "s35.sh05",
        "s35.snd01"
      ]
    },
    {
      "event_id": "s35.e04",
      "source_evidence": [
        "DAMIEN (CONT'D)\nVictor offers a solution: sign tonight, marry a stranger who\ndoesn't want me, satisfy the letter, keep the company. It's a\ngood deal. I've done deals like it my whole life — I've been\na deal like it my whole life."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "he names Victor's deal out loud — and self-indicts: 'I've been a deal like it my whole life'",
      "participants": [
        "DAMIEN",
        "VICTOR",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "VICTOR",
        "GUESTS"
      ],
      "location": {
        "zone": "ballroom stage"
      },
      "timeline": [
        {
          "beat": "the deal spelled out, ending on 'I've been a deal like it my whole life'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "held on him — Victor's exposure plays in the words, not a cut to Victor"
      ],
      "audio_requirements": [
        "held quiet under the self-indictment"
      ],
      "continuity_constraints": [
        "Victor is still on stage, out of this frame — his answer to exposure is delayed to scene 36"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s35.sh06"
      ]
    },
    {
      "event_id": "s35.e05",
      "source_evidence": [
        "*He looks at Sophia — and she looks back, waiting, terrified.*"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the look — her fate is still in his hands for one more breath",
      "participants": [
        "DAMIEN",
        "SOPHIA"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "location": {
        "zone": "ballroom stage"
      },
      "timeline": [
        {
          "beat": "he looks at Sophia",
          "type": "action"
        },
        {
          "beat": "she looks back — waiting, terrified",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "the exchange is two frames, not one two-shot — her terror gets its own hold"
      ],
      "audio_requirements": [
        "held silence between the looks"
      ],
      "continuity_constraints": [
        "Sophia is still on stage in the wedding costume and white veil — the veil matters in e07"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "SOPHIA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s35.sh07",
        "s35.sh08"
      ]
    },
    {
      "event_id": "s35.e06",
      "source_evidence": [
        "DAMIEN (CONT'D)\nSophia — you're free to sit down. You don't owe my brother your\nestate. (to the trustees) The loan paper on the Vane property —\nheld by a shell that traces to my brother — is about to become\na very public document. Maya's lab saw to that this morning.\nShe doesn't like being managed either."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "release and indictment in one turn — Sophia freed, Victor's shell named on the record, Maya's lab credited",
      "participants": [
        "DAMIEN",
        "SOPHIA",
        "TRUSTEES",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "SOPHIA",
        "TRUSTEES",
        "GUESTS"
      ],
      "location": {
        "zone": "ballroom stage"
      },
      "timeline": [
        {
          "beat": "the release to Sophia, then the address pivots to the trustees — the loan paper becomes a very public document",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "held on him through the address pivot — Sophia and the trustees answer in e07 and scene 36, not here"
      ],
      "audio_requirements": [
        "close mic direct address"
      ],
      "continuity_constraints": [
        "'Maya's lab saw to that this morning' — ties to the offscreen lab action; no flashback needed"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s35.sh09"
      ]
    },
    {
      "event_id": "s35.e07",
      "source_evidence": [
        "*Sophia stands a second longer — then takes off the white veil,\nhands it to Victor, and walks off the stage to the first applause\nof the night.*"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "Sophia's exit — the costume returned to its owner, the first applause of the night",
      "participants": [
        "SOPHIA",
        "VICTOR",
        "DAMIEN",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "location": {
        "zones": [
          "ballroom stage",
          "ballroom floor"
        ],
        "primary": "ballroom stage"
      },
      "timeline": [
        {
          "beat": "she stands a second longer",
          "type": "held_action"
        },
        {
          "beat": "takes off the white veil, hands it to Victor",
          "type": "action"
        },
        {
          "beat": "walks off the stage to the first applause of the night",
          "type": "action"
        }
      ],
      "visual_requirements": [
        "the veil handoff is the frame — the wedding costume returned to the man who arranged it",
        "the exit wide carries Damien still at the mic — her freedom happens in his sentence"
      ],
      "audio_requirements": [
        "first applause of the night"
      ],
      "continuity_constraints": [
        "veil state: on her in e05, in Victor's hands after this event"
      ],
      "ambiguities": [],
      "must_appear": [
        "SOPHIA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s35.sh10",
        "s35.sh11",
        "s35.snd01"
      ]
    },
    {
      "event_id": "s35.e08",
      "source_evidence": [
        "DAMIEN (CONT'D)\nNow — the clause. \"Married and demonstrably so.\" My father\nanticipated a technicality. He wrote a second page of adjectives,\nand I've read it every night for eight weeks. He didn't want a\nwife-shaped signature. He wanted a son who could stand in a room\nlike this and tell the truth in front of people who could\ndestroy him."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "reframe — the clause was never about a signature; 'demonstrably' meant changed, and his father wrote the test",
      "participants": [
        "DAMIEN",
        "TRUSTEES",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "TRUSTEES",
        "GUESTS"
      ],
      "location": {
        "zone": "ballroom stage"
      },
      "timeline": [
        {
          "beat": "the clause re-read as intent — 'a son who could stand in a room like this and tell the truth'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "held on him — this is the argument scene 36 rules on"
      ],
      "audio_requirements": [
        "close mic"
      ],
      "continuity_constraints": [
        "'a second page of adjectives' — the supplemental memorandum Penhaligon produces in scene 36"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s35.sh12"
      ]
    },
    {
      "event_id": "s35.e09",
      "source_evidence": [
        "*He takes the trust documents from the trustee table. Holds them.*",
        "DAMIEN (CONT'D)\nI can't produce a marriage tonight. I won't produce a fake one.\nThe clause drops — and I let it.",
        "*He sets the documents down. The room is silent — the empire,\nsurrendered on a stage.*"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "THE surrender — documents taken, held, refused, set down; the empire dropped by hand",
      "participants": [
        "DAMIEN",
        "TRUSTEES",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "depicts_via_channel": [],
      "document_evidence": [
        {
          "artifact": "the trust documents — the clause and its second page of adjectives",
          "channel": "document"
        }
      ],
      "location": {
        "zones": [
          "ballroom stage",
          "trustee table",
          "ballroom floor"
        ],
        "primary": "ballroom stage"
      },
      "timeline": [
        {
          "beat": "takes the trust documents from the trustee table — holds them",
          "type": "action"
        },
        {
          "beat": "'I can't produce a marriage tonight. I won't produce a fake one. The clause drops — and I let it.'",
          "type": "dialogue"
        },
        {
          "beat": "sets the documents down",
          "type": "action"
        },
        {
          "beat": "the room is silent — the empire, surrendered on a stage",
          "type": "held_image"
        }
      ],
      "visual_requirements": [
        "the documents are the prop — take, hold, set down is the whole physical act",
        "the silence after is a room frame: nobody applauds a surrender"
      ],
      "audio_requirements": [
        "dead silence after the documents are set down"
      ],
      "continuity_constraints": [
        "documents live at the trustee table — same table Penhaligon stands at in scene 36",
        "the clause is now legally dropped — scene 36's ruling must read as reversal, not confirmation"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": true,
      "shot_sequence": [
        "s35.sh13",
        "s35.sh14",
        "s35.sh15",
        "s35.snd01"
      ]
    },
    {
      "event_id": "s35.e10",
      "source_evidence": [
        "DAMIEN (CONT'D)\nI spent thirty-one years being the most optimized man in any\nroom. It took a defective robot and the woman inside her to\ndemonstrate the flaw in the product. Father — wherever the\nadjectives came from — the clause worked. Just not the way\nthe lawyers meant."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "eulogy-credo — 'the clause worked. Just not the way the lawyers meant.' The film's thesis said out loud",
      "participants": [
        "DAMIEN",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "GUESTS"
      ],
      "location": {
        "zone": "ballroom stage"
      },
      "timeline": [
        {
          "beat": "thirty-one years optimized — 'a defective robot and the woman inside her' — 'the clause worked'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "held on him — last frame of Damien at the mic before he steps down"
      ],
      "audio_requirements": [
        "close mic, eulogy cadence"
      ],
      "continuity_constraints": [
        "'the woman inside her' — Maya's secret is his to keep in public; the phrasing credits her without naming her"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s35.sh16"
      ]
    },
    {
      "event_id": "s35.e11",
      "source_evidence": [
        "*He steps down. The trustees confer — agitated, urgent. PENHALIGON,\nancient and delighted, raises one finger for silence.*"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "handoff — he steps down; the trustees take the room; Penhaligon's raised finger buys the silence scene 36 speaks into",
      "participants": [
        "DAMIEN",
        "TRUSTEES",
        "PENHALIGON",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "GUESTS"
      ],
      "location": {
        "zones": [
          "ballroom stage",
          "trustee table"
        ],
        "primary": "trustee table"
      },
      "timeline": [
        {
          "beat": "he steps down",
          "type": "action"
        },
        {
          "beat": "the trustees confer — agitated, urgent",
          "type": "reaction"
        },
        {
          "beat": "Penhaligon, ancient and delighted, raises one finger for silence",
          "type": "action"
        }
      ],
      "visual_requirements": [
        "one frame holds all three beats — step down, agitated table, the single raised finger"
      ],
      "audio_requirements": [
        "agitated trustee murmur hushed by the raised finger"
      ],
      "continuity_constraints": [
        "Penhaligon's raised finger is the bridge — scene 36 opens with him already standing at the same table"
      ],
      "ambiguities": [],
      "must_appear": [
        "PENHALIGON"
      ],
      "tableau": true,
      "shot_sequence": [
        "s35.sh17",
        "s35.snd01"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s35.sh02",
      "size": "W/M",
      "zone": "ballroom stage",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "VICTOR",
        "SOPHIA",
        "GUESTS"
      ],
      "implements": [
        "s35.e01"
      ],
      "covers_beats": {
        "s35.e01": [
          0,
          1,
          2
        ]
      },
      "purpose": "the room a held breath — Damien walks slowly onto the stage, past Victor, past Sophia, to the microphone A.V.A. left standing — and stops at it",
      "audio_note": "room tone; footsteps on the stage"
    },
    {
      "shot_id": "s35.sh03",
      "size": "M/CU",
      "zone": "ballroom stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s35.e02"
      ],
      "covers_beats": {
        "s35.e02": [
          0
        ]
      },
      "purpose": "the confession at the mic — 'the clause is real. So is the fraud' — trailing off mid-list",
      "audio_note": "close dry mic; room silent",
      "dialogue_lines": [
        {
          "event_id": "s35.e02",
          "speaker": "DAMIEN",
          "line": "The clause is real. So is the fraud — the lab lied, the evenings were a person, and I paid for a coach who turned out to be...",
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
      "shot_id": "s35.sh04",
      "size": "CU",
      "zone": "ballroom stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s35.e03"
      ],
      "covers_beats": {
        "s35.e03": [
          0,
          1
        ]
      },
      "purpose": "he stops — finds the word — 'warranty service'",
      "audio_note": "held quiet; the mic carries the pause",
      "dialogue_lines": [
        {
          "event_id": "s35.e03",
          "speaker": "DAMIEN",
          "line": "...the first thing in years I didn't want to return for warranty service.",
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
      "shot_id": "s35.sh05",
      "size": "R/W",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "GUESTS"
      ],
      "implements": [
        "s35.e03"
      ],
      "covers_beats": {
        "s35.e03": [
          2
        ]
      },
      "purpose": "the room breaks — real, surprised laughter, tension gone",
      "audio_note": "real surprised laughter breaking tension"
    },
    {
      "shot_id": "s35.sh06",
      "size": "M",
      "zone": "ballroom stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s35.e04"
      ],
      "covers_beats": {
        "s35.e04": [
          0
        ]
      },
      "purpose": "Victor's deal spelled out — 'I've been a deal like it my whole life'",
      "audio_note": "held quiet under the self-indictment",
      "dialogue_lines": [
        {
          "event_id": "s35.e04",
          "speaker": "DAMIEN",
          "line": "Victor offers a solution: sign tonight, marry a stranger who doesn't want me, satisfy the letter, keep the company. It's a good deal. I've done deals like it my whole life — I've been a deal like it my whole life.",
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
      "shot_id": "s35.sh07",
      "size": "M",
      "zone": "ballroom stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s35.e05"
      ],
      "covers_beats": {
        "s35.e05": [
          0
        ]
      },
      "purpose": "he looks at Sophia — the decision before the sentence",
      "audio_note": "held silence between the looks"
    },
    {
      "shot_id": "s35.sh08",
      "size": "M/CU",
      "zone": "ballroom stage",
      "type": "visual",
      "participants": [
        "SOPHIA"
      ],
      "implements": [
        "s35.e05"
      ],
      "covers_beats": {
        "s35.e05": [
          1
        ]
      },
      "purpose": "she looks back — waiting, terrified, still in the veil",
      "audio_note": "held silence between the looks"
    },
    {
      "shot_id": "s35.sh09",
      "size": "M",
      "zone": "ballroom stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s35.e06"
      ],
      "covers_beats": {
        "s35.e06": [
          0
        ]
      },
      "purpose": "'Sophia — you're free to sit down' — pivoting mid-turn to the trustees: the loan paper goes public",
      "audio_note": "close mic direct address",
      "dialogue_lines": [
        {
          "event_id": "s35.e06",
          "speaker": "DAMIEN",
          "line": "Sophia — you're free to sit down. You don't owe my brother your estate.",
          "line_kind": "on_camera",
          "recipient": "SOPHIA",
          "recipient_presence": "offscreen",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s35.e06",
          "speaker": "DAMIEN",
          "line": "(to the trustees) The loan paper on the Vane property — held by a shell that traces to my brother — is about to become a very public document. Maya's lab saw to that this morning. She doesn't like being managed either.",
          "line_kind": "on_camera",
          "recipient": "TRUSTEES",
          "recipient_presence": "offscreen",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s35.sh10",
      "size": "M",
      "zone": "ballroom stage",
      "type": "visual",
      "participants": [
        "SOPHIA",
        "VICTOR"
      ],
      "implements": [
        "s35.e07"
      ],
      "covers_beats": {
        "s35.e07": [
          0,
          1
        ]
      },
      "purpose": "a second longer — then the white veil comes off and is handed to Victor",
      "audio_note": "the room inhaling; first claps beginning"
    },
    {
      "shot_id": "s35.sh11",
      "size": "W",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "SOPHIA",
        "DAMIEN",
        "GUESTS"
      ],
      "implements": [
        "s35.e07"
      ],
      "covers_beats": {
        "s35.e07": [
          2
        ]
      },
      "purpose": "she walks off the stage into the first applause of the night — Damien still at the mic",
      "audio_note": "first applause of the night"
    },
    {
      "shot_id": "s35.sh12",
      "size": "M",
      "zone": "ballroom stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s35.e08"
      ],
      "covers_beats": {
        "s35.e08": [
          0
        ]
      },
      "purpose": "'Now — the clause' — the founder's intent argued: a son telling the truth in front of people who could destroy him",
      "audio_note": "close mic",
      "dialogue_lines": [
        {
          "event_id": "s35.e08",
          "speaker": "DAMIEN",
          "line": "Now — the clause. \"Married and demonstrably so.\" My father anticipated a technicality. He wrote a second page of adjectives, and I've read it every night for eight weeks. He didn't want a wife-shaped signature. He wanted a son who could stand in a room like this and tell the truth in front of people who could destroy him.",
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
      "shot_id": "s35.sh13",
      "size": "INS/M",
      "zone": "trustee table",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "TRUSTEES"
      ],
      "implements": [
        "s35.e09"
      ],
      "covers_beats": {
        "s35.e09": [
          0
        ]
      },
      "purpose": "he takes the trust documents from the trustee table — and holds them",
      "audio_note": "paper in hand; room holding"
    },
    {
      "shot_id": "s35.sh14",
      "size": "CU",
      "zone": "ballroom stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s35.e09"
      ],
      "covers_beats": {
        "s35.e09": [
          1
        ]
      },
      "purpose": "the refusal — 'The clause drops — and I let it.'",
      "audio_note": "close mic; dead quiet",
      "dialogue_lines": [
        {
          "event_id": "s35.e09",
          "speaker": "DAMIEN",
          "line": "I can't produce a marriage tonight. I won't produce a fake one. The clause drops — and I let it.",
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
      "shot_id": "s35.sh15",
      "size": "W",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "TRUSTEES",
        "GUESTS"
      ],
      "implements": [
        "s35.e09"
      ],
      "covers_beats": {
        "s35.e09": [
          2,
          3
        ]
      },
      "purpose": "the documents set down — the room silent, the empire surrendered on a stage",
      "audio_note": "dead silence after the documents are set down"
    },
    {
      "shot_id": "s35.sh16",
      "size": "M",
      "zone": "ballroom stage",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s35.e10"
      ],
      "covers_beats": {
        "s35.e10": [
          0
        ]
      },
      "purpose": "the credo — 'the clause worked. Just not the way the lawyers meant.'",
      "audio_note": "close mic, eulogy cadence",
      "dialogue_lines": [
        {
          "event_id": "s35.e10",
          "speaker": "DAMIEN",
          "line": "I spent thirty-one years being the most optimized man in any room. It took a defective robot and the woman inside her to demonstrate the flaw in the product. Father — wherever the adjectives came from — the clause worked. Just not the way the lawyers meant.",
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
      "shot_id": "s35.sh17",
      "size": "W",
      "zone": "trustee table",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "TRUSTEES",
        "PENHALIGON"
      ],
      "implements": [
        "s35.e11"
      ],
      "covers_beats": {
        "s35.e11": [
          0,
          1,
          2
        ]
      },
      "purpose": "he steps down — the table confers, agitated — Penhaligon's single raised finger buys silence",
      "audio_note": "agitated trustee murmur hushed by the raised finger"
    },
    {
      "shot_id": "s35.snd01",
      "type": "sound",
      "implements": [
        "s35.e01",
        "s35.e03",
        "s35.e07",
        "s35.e09",
        "s35.e11"
      ],
      "purpose": "sound-states card for the public confession — breath, laughter, first applause, surrender silence, trustee murmur",
      "audio_note": "held-breath room tone → real surprised laughter breaking tension → first applause of the night → dead silence after the documents are set down → agitated trustee murmur hushed by a raised finger",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "*The room is a held breath. DAMIEN walks slowly onto the stage — past Victor, past Sophia, to the microphone A.V.A. left standing.*",
      "disposition": "covered_by",
      "by": [
        "s35.e01"
      ]
    },
    {
      "span": "DAMIEN\nThe clause is real. So is the fraud — the lab lied, the evenings\nwere a person, and I paid for a coach who turned out to be...",
      "disposition": "covered_by",
      "by": [
        "s35.e02"
      ]
    },
    {
      "span": "*He stops. Finds the word.*",
      "disposition": "covered_by",
      "by": [
        "s35.e03"
      ]
    },
    {
      "span": "DAMIEN (CONT'D)\n...the first thing in years I didn't want to return for warranty\nservice.",
      "disposition": "covered_by",
      "by": [
        "s35.e03"
      ]
    },
    {
      "span": "*Laughter — real, surprised laughter, breaking the tension.*",
      "disposition": "covered_by",
      "by": [
        "s35.e03"
      ]
    },
    {
      "span": "DAMIEN (CONT'D)\nVictor offers a solution: sign tonight, marry a stranger who\ndoesn't want me, satisfy the letter, keep the company. It's a\ngood deal. I've done deals like it my whole life — I've been\na deal like it my whole life.",
      "disposition": "covered_by",
      "by": [
        "s35.e04"
      ]
    },
    {
      "span": "*He looks at Sophia — and she looks back, waiting, terrified.*",
      "disposition": "covered_by",
      "by": [
        "s35.e05"
      ]
    },
    {
      "span": "DAMIEN (CONT'D)\nSophia — you're free to sit down. You don't owe my brother your\nestate. (to the trustees) The loan paper on the Vane property —\nheld by a shell that traces to my brother — is about to become\na very public document. Maya's lab saw to that this morning.\nShe doesn't like being managed either.",
      "disposition": "covered_by",
      "by": [
        "s35.e06"
      ]
    },
    {
      "span": "*Sophia stands a second longer — then takes off the white veil,\nhands it to Victor, and walks off the stage to the first applause\nof the night.*",
      "disposition": "covered_by",
      "by": [
        "s35.e07"
      ]
    },
    {
      "span": "DAMIEN (CONT'D)\nNow — the clause. \"Married and demonstrably so.\" My father\nanticipated a technicality. He wrote a second page of adjectives,\nand I've read it every night for eight weeks. He didn't want a\nwife-shaped signature. He wanted a son who could stand in a room\nlike this and tell the truth in front of people who could\ndestroy him.",
      "disposition": "covered_by",
      "by": [
        "s35.e08"
      ]
    },
    {
      "span": "*He takes the trust documents from the trustee table. Holds them.*",
      "disposition": "covered_by",
      "by": [
        "s35.e09"
      ]
    },
    {
      "span": "DAMIEN (CONT'D)\nI can't produce a marriage tonight. I won't produce a fake one.\nThe clause drops — and I let it.",
      "disposition": "covered_by",
      "by": [
        "s35.e09"
      ]
    },
    {
      "span": "*He sets the documents down. The room is silent — the empire,\nsurrendered on a stage.*",
      "disposition": "covered_by",
      "by": [
        "s35.e09"
      ]
    },
    {
      "span": "DAMIEN (CONT'D)\nI spent thirty-one years being the most optimized man in any\nroom. It took a defective robot and the woman inside her to\ndemonstrate the flaw in the product. Father — wherever the\nadjectives came from — the clause worked. Just not the way\nthe lawyers meant.",
      "disposition": "covered_by",
      "by": [
        "s35.e10"
      ]
    },
    {
      "span": "*He steps down. The trustees confer — agitated, urgent. PENHALIGON,\nancient and delighted, raises one finger for silence.*",
      "disposition": "covered_by",
      "by": [
        "s35.e11"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['DAMIEN', 'VICTOR'] | -  | The room is a held breath. DAMIEN walks slowly onto the stage — past Victor, pas
i02 blk=['DAMIEN', 'SOPHIA'] | DAMIEN The clause is real. So is the fraud — the lab lied, the even | DAMIEN faces VICTOR and speaks. He stops. Finds the word.
i03 blk=['DAMIEN'] | DAMIEN Victor offers a solution: sign tonight, marry a stranger who | Laughter — real, surprised laughter, breaking the tension.
i04 blk=['SOPHIA'] | -  | He looks at Sophia — and she looks back, waiting, terrified.
i05 blk=['DAMIEN'] | DAMIEN Sophia — you're free to sit down. You don't owe my brother y | DAMIEN faces VICTOR and speaks.
i06 blk=['VICTOR', 'SOPHIA'] | -  | Sophia stands a second longer — then takes off the white veil, hands it to Victo
i07 blk=['DAMIEN'] | DAMIEN Now — the clause. "Married and demonstrably so." My father a | DAMIEN faces VICTOR and speaks.
i08 blk=['PENHALIGON', 'DAMIEN'] | DAMIEN I can't produce a marriage tonight. I won't produce a fake o | He takes the trust documents from the trustee table. Holds them.
i09 blk=['DAMIEN'] | DAMIEN I spent thirty-one years being the most optimized man in any | He sets the documents down. The room is silent — the empire, surrendered on a st
i10 blk=['PENHALIGON'] | -  | He steps down. The trustees confer — agitated, urgent. PENHALIGON, ancient and d