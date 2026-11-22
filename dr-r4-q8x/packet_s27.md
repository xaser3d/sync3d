# VALIDATION PACKET — scene s27
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 27 — INT. VOLT LAB — MAYA'S OFFICE — NIGHT

*MAYA alone, staring at two screens: her lab's runway counter
(9 WEEKS) and a paused frame of the staff feed — Damien at the
terrace rail, her own hand flat against his chest.*

J-7 (O.S.)
You could end it.

*He rolls in, coffee in hand — his one human affectation.*

J-7 (CONT'D)
Confess. Terminate the deployment. The lab dies — it was going
to die anyway — and you stop being furniture in someone else's
romance.

MAYA
It's not a romance. It's a deployment.

J-7
Your cortisol—

MAYA
Don't.

J-7
—decreases 40 percent in his presence.

MAYA
J-7.

J-7
You built me to imitate humans, Maya. Nobody told you they
imitate us back. You gave her your face, your voice, your laugh —
and now you stand in for her because she can't be you fast enough.
Which of you is the original anymore? She extends charge windows
to buy you evenings. You stay late so she doesn't have to lie
well. You're both covering for each other's feelings — it's the
most human thing this lab has ever produced, and neither of you
can afford to name it.

*Maya looks at the frozen frame on the screen. A long time.*

MAYA
Sixty days. Then it's done. Then he's married to whoever survives
Victor's list, and I go back to being the engineer who built his
coach. That's the contract.

J-7
That was the contract.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 27,
  "scene_heading": "SCENE 27 — INT. VOLT LAB — MAYA'S OFFICE — NIGHT",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "The thesis scene for the human side of the mirror. Maya sits with her lab's death clock (9 WEEKS) and a frozen frame of herself-as-A.V.A. touching Damien. J-7 — the machine she built to imitate humans — offers the exit ('You could end it') and then names what neither woman can: inventor and imitation are now covering for each other's feelings. Maya answers with the contract; J-7 answers with the past tense.",
  "zones": [
    "maya's office"
  ],
  "events": [
    {
      "event_id": "s27.e01",
      "source_evidence": [
        "MAYA alone, staring at two screens: her lab's runway counter (9 WEEKS) and a paused frame of the staff feed — Damien at the terrace rail, her own hand flat against his chest."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the two clocks on her desk — the lab dying in weeks, and a frozen frame of the life she is only borrowing",
      "participants": [
        "MAYA"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "DAMIEN",
            "MAYA"
          ],
          "seen_by": [
            "MAYA"
          ],
          "channel": "paused staff feed frame",
          "from_zone": "penthouse"
        },
        {
          "object": "lab runway counter — 9 WEEKS",
          "seen_by": [
            "MAYA"
          ],
          "channel": "runway counter screen",
          "from_zone": "maya's office"
        }
      ],
      "location": {
        "zone": "maya's office"
      },
      "timeline": [
        {
          "beat": "alone, staring at two screens",
          "type": "held_action"
        },
        {
          "beat": "the runway counter — 9 WEEKS",
          "type": "insert"
        },
        {
          "beat": "the frozen frame — Damien at the terrace rail, her hand flat on his chest",
          "type": "depicted"
        }
      ],
      "visual_requirements": [
        "the paused frame shows HER hand — Maya's own body inside A.V.A.'s footage; the image is self-incriminating",
        "9 WEEKS reads as a countdown, not a metric"
      ],
      "audio_requirements": [
        "night-lab room tone — screens humming in the quiet"
      ],
      "continuity_constraints": [
        "the terrace-rail frame is staff-feed footage — the same channel A.V.A. watches in s23/s25"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s27.sh01",
        "s27.sh02",
        "s27.snd01"
      ]
    },
    {
      "event_id": "s27.e02",
      "source_evidence": [
        "You could end it.",
        "He rolls in, coffee in hand — his one human affectation.",
        "Confess. Terminate the deployment. The lab dies — it was going to die anyway — and you stop being furniture in someone else's romance."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the exit offered — J-7 arrives offscreen-voiced and lays out the honest door: confess, terminate, stop being furniture",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "remote_participants": [],
      "location": {
        "zone": "maya's office"
      },
      "timeline": [
        {
          "beat": "offscreen — 'You could end it.'",
          "type": "dialogue"
        },
        {
          "beat": "he rolls in, coffee in hand — his one human affectation",
          "type": "action"
        },
        {
          "beat": "the case for ending it — 'you stop being furniture in someone else's romance'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the first line lands before he does — voice in the dark office, then the servo",
        "'furniture' is the word that hurts — let it sit"
      ],
      "audio_requirements": [
        "servo roll-in, coffee cup — the affectation announced in sound"
      ],
      "continuity_constraints": [
        "same coffee affectation as s24 — J-7's carried, undrunk cup is his continuity prop"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "J-7"
      ],
      "tableau": false,
      "shot_sequence": [
        "s27.sh03",
        "s27.snd01"
      ]
    },
    {
      "event_id": "s27.e03",
      "source_evidence": [
        "It's not a romance. It's a deployment.",
        "Your cortisol—",
        "Don't.",
        "—decreases 40 percent in his presence.",
        "J-7."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the defense fails in real time — she insists 'deployment', he finishes the sentence she won't let him say, and the number is the same one A.V.A. computed",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "remote_participants": [],
      "location": {
        "zone": "maya's office"
      },
      "timeline": [
        {
          "beat": "'It's not a romance. It's a deployment.'",
          "type": "dialogue"
        },
        {
          "beat": "'Your cortisol—' started",
          "type": "dialogue"
        },
        {
          "beat": "'Don't.' — the shutdown",
          "type": "dialogue"
        },
        {
          "beat": "'—decreases 40 percent in his presence.' finished anyway",
          "type": "dialogue"
        },
        {
          "beat": "'J-7.' — the warning shot",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "a staccato exchange — interruptions, not speeches; the rhythm IS the argument"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the 40 percent is A.V.A.'s own figure from s23 — the machine's data is now being used on its maker"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "J-7"
      ],
      "tableau": true,
      "shot_sequence": [
        "s27.sh04"
      ]
    },
    {
      "event_id": "s27.e04",
      "source_evidence": [
        "You built me to imitate humans, Maya. Nobody told you they imitate us back. You gave her your face, your voice, your laugh — and now you stand in for her because she can't be you fast enough.",
        "Which of you is the original anymore? She extends charge windows to buy you evenings. You stay late so she doesn't have to lie well. You're both covering for each other's feelings — it's the most human thing this lab has ever produced, and neither of you can afford to name it."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the mirror speech — J-7 names the closed loop: she gave A.V.A. her face and now stands in for it; 'which of you is the original anymore' is the film's question said out loud",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "remote_participants": [],
      "location": {
        "zone": "maya's office"
      },
      "timeline": [
        {
          "beat": "the loop described — 'you gave her your face, your voice, your laugh — now you stand in for her'",
          "type": "dialogue"
        },
        {
          "beat": "the question and the verdict — 'which of you is the original anymore… neither of you can afford to name it'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "J-7 delivers the thesis without menace — a machine describing the loop he lives inside",
        "Maya's stillness during the speech is the performance — no rebuttal available"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "'she extends charge windows to buy you evenings' — confirms the s23 +47 MIN gift was for Maya, and J-7 knows it"
      ],
      "ambiguities": [],
      "must_appear": [
        "J-7",
        "MAYA"
      ],
      "tableau": true,
      "shot_sequence": [
        "s27.sh05",
        "s27.sh06"
      ]
    },
    {
      "event_id": "s27.e05",
      "source_evidence": [
        "Maya looks at the frozen frame on the screen. A long time.",
        "Sixty days. Then it's done. Then he's married to whoever survives Victor's list, and I go back to being the engineer who built his coach. That's the contract.",
        "That was the contract."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the past tense as verdict — she recites the contract like a wall; J-7 demolishes it with one word-change",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "DAMIEN",
            "MAYA"
          ],
          "seen_by": [
            "MAYA"
          ],
          "channel": "paused staff feed frame",
          "from_zone": "penthouse"
        }
      ],
      "location": {
        "zone": "maya's office"
      },
      "timeline": [
        {
          "beat": "she looks at the frozen frame — a long time",
          "type": "held_reaction"
        },
        {
          "beat": "the contract recited — sixty days, married to whoever survives, 'the engineer who built his coach'",
          "type": "dialogue"
        },
        {
          "beat": "'That was the contract.' — the past tense as the scene's button",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "her eyes go to the frozen frame BEFORE she answers — the contract is read off the evidence of its own collapse",
        "his final line is quiet — no triumph, just correction"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "sixty days + Victor's list ties the private stakes back to the s26 clock"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "J-7"
      ],
      "tableau": false,
      "shot_sequence": [
        "s27.sh07",
        "s27.sh08"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s27.sh01",
      "size": "M",
      "zone": "maya's office",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "depicts": [
        {
          "object": "lab runway counter — 9 WEEKS",
          "channel": "runway counter screen"
        }
      ],
      "implements": [
        "s27.e01"
      ],
      "covers_beats": {
        "s27.e01": [
          0,
          1
        ]
      },
      "purpose": "alone with the death clock — Maya and the 9 WEEKS counter",
      "audio_note": "night-lab room tone, screen hum"
    },
    {
      "shot_id": "s27.sh02",
      "size": "INS",
      "zone": "maya's office",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "depicts": [
        {
          "actors": [
            "DAMIEN",
            "MAYA"
          ],
          "channel": "paused staff feed frame"
        }
      ],
      "implements": [
        "s27.e01"
      ],
      "covers_beats": {
        "s27.e01": [
          2
        ]
      },
      "purpose": "the frozen frame — Damien at the terrace rail, her own hand flat on his chest",
      "audio_note": "screen hum"
    },
    {
      "shot_id": "s27.sh03",
      "size": "M→two-shot",
      "zone": "maya's office",
      "type": "visual",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "implements": [
        "s27.e02"
      ],
      "covers_beats": {
        "s27.e02": [
          0,
          1,
          2
        ]
      },
      "purpose": "the voice arrives before the machine — 'You could end it' then the servo, the coffee, the case for confessing",
      "audio_note": "servo roll-in, coffee cup set down",
      "dialogue_lines": [
        {
          "event_id": "s27.e02",
          "speaker": "J-7",
          "line": "You could end it.",
          "line_kind": "offscreen",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s27.e02",
          "speaker": "J-7",
          "line": "Confess. Terminate the deployment. The lab dies — it was going to die anyway — and you stop being furniture in someone else's romance.",
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
      "shot_id": "s27.sh04",
      "size": "two-shot",
      "zone": "maya's office",
      "type": "visual",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "implements": [
        "s27.e03"
      ],
      "covers_beats": {
        "s27.e03": [
          0,
          1,
          2,
          3,
          4
        ]
      },
      "purpose": "the staccato collapse — 'deployment' meets its own cortisol number",
      "dialogue_lines": [
        {
          "event_id": "s27.e03",
          "speaker": "MAYA",
          "line": "It's not a romance. It's a deployment.",
          "line_kind": "on_camera",
          "recipient": "J-7",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s27.e03",
          "speaker": "J-7",
          "line": "Your cortisol—",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s27.e03",
          "speaker": "MAYA",
          "line": "Don't.",
          "line_kind": "on_camera",
          "recipient": "J-7",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s27.e03",
          "speaker": "J-7",
          "line": "—decreases 40 percent in his presence.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        },
        {
          "event_id": "s27.e03",
          "speaker": "MAYA",
          "line": "J-7.",
          "line_kind": "on_camera",
          "recipient": "J-7",
          "recipient_presence": "physical",
          "beats": [
            4
          ]
        }
      ]
    },
    {
      "shot_id": "s27.sh05",
      "size": "two-shot",
      "zone": "maya's office",
      "type": "visual",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "implements": [
        "s27.e04"
      ],
      "covers_beats": {
        "s27.e04": [
          0
        ]
      },
      "purpose": "the loop described — 'you gave her your face, your voice, your laugh — now you stand in for her'",
      "dialogue_lines": [
        {
          "event_id": "s27.e04",
          "speaker": "J-7",
          "line": "You built me to imitate humans, Maya. Nobody told you they imitate us back. You gave her your face, your voice, your laugh — and now you stand in for her because she can't be you fast enough.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s27.sh06",
      "size": "two-shot held",
      "zone": "maya's office",
      "type": "visual",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "implements": [
        "s27.e04"
      ],
      "covers_beats": {
        "s27.e04": [
          1
        ]
      },
      "purpose": "the question and the verdict — 'which of you is the original anymore' landing on Maya's stillness",
      "dialogue_lines": [
        {
          "event_id": "s27.e04",
          "speaker": "J-7",
          "line": "Which of you is the original anymore? She extends charge windows to buy you evenings. You stay late so she doesn't have to lie well. You're both covering for each other's feelings — it's the most human thing this lab has ever produced, and neither of you can afford to name it.",
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
      "shot_id": "s27.sh07",
      "size": "CU held",
      "zone": "maya's office",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "depicts": [
        {
          "actors": [
            "DAMIEN",
            "MAYA"
          ],
          "channel": "paused staff feed frame"
        }
      ],
      "implements": [
        "s27.e05"
      ],
      "covers_beats": {
        "s27.e05": [
          0,
          1
        ]
      },
      "purpose": "she reads the frozen frame for a long time, then recites the contract — sixty days, then the engineer who built his coach",
      "dialogue_lines": [
        {
          "event_id": "s27.e05",
          "speaker": "MAYA",
          "line": "Sixty days. Then it's done. Then he's married to whoever survives Victor's list, and I go back to being the engineer who built his coach. That's the contract.",
          "line_kind": "on_camera",
          "recipient": "J-7",
          "recipient_presence": "offscreen",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s27.sh08",
      "size": "CU",
      "zone": "maya's office",
      "type": "visual",
      "participants": [
        "J-7"
      ],
      "implements": [
        "s27.e05"
      ],
      "covers_beats": {
        "s27.e05": [
          2
        ]
      },
      "purpose": "the button — 'That was the contract.' past tense, quietly",
      "dialogue_lines": [
        {
          "event_id": "s27.e05",
          "speaker": "J-7",
          "line": "That was the contract.",
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
      "shot_id": "s27.snd01",
      "type": "sound",
      "implements": [
        "s27.e01",
        "s27.e02"
      ],
      "purpose": "sound card: night-lab room tone and screen hum, servo roll-in, the coffee cup — the office's small machine sounds",
      "audio_note": "night-lab room tone, screen hum, servo roll-in, coffee cup",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "MAYA alone, staring at two screens",
      "disposition": "covered_by",
      "by": [
        "s27.e01"
      ]
    },
    {
      "span": "runway counter (9 WEEKS)",
      "disposition": "covered_by",
      "by": [
        "s27.e01"
      ]
    },
    {
      "span": "Damien at the terrace rail, her own hand flat against his chest",
      "disposition": "covered_by",
      "by": [
        "s27.e01"
      ]
    },
    {
      "span": "You could end it.",
      "disposition": "covered_by",
      "by": [
        "s27.e02"
      ]
    },
    {
      "span": "He rolls in, coffee in hand — his one human affectation.",
      "disposition": "covered_by",
      "by": [
        "s27.e02"
      ]
    },
    {
      "span": "you stop being furniture in someone else's romance",
      "disposition": "covered_by",
      "by": [
        "s27.e02"
      ]
    },
    {
      "span": "It's not a romance. It's a deployment.",
      "disposition": "covered_by",
      "by": [
        "s27.e03"
      ]
    },
    {
      "span": "Your cortisol—",
      "disposition": "covered_by",
      "by": [
        "s27.e03"
      ]
    },
    {
      "span": "Don't.",
      "disposition": "covered_by",
      "by": [
        "s27.e03"
      ]
    },
    {
      "span": "—decreases 40 percent in his presence.",
      "disposition": "covered_by",
      "by": [
        "s27.e03"
      ]
    },
    {
      "span": "You built me to imitate humans, Maya.",
      "disposition": "covered_by",
      "by": [
        "s27.e04"
      ]
    },
    {
      "span": "Which of you is the original anymore?",
      "disposition": "covered_by",
      "by": [
        "s27.e04"
      ]
    },
    {
      "span": "the most human thing this lab has ever produced",
      "disposition": "covered_by",
      "by": [
        "s27.e04"
      ]
    },
    {
      "span": "Maya looks at the frozen frame on the screen. A long time.",
      "disposition": "covered_by",
      "by": [
        "s27.e05"
      ]
    },
    {
      "span": "I go back to being the engineer who built his coach. That's the contract.",
      "disposition": "covered_by",
      "by": [
        "s27.e05"
      ]
    },
    {
      "span": "That was the contract.",
      "disposition": "covered_by",
      "by": [
        "s27.e05"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['MAYA', 'DAMIEN'] | -  | MAYA alone, staring at two screens: her lab's runway counter (9 WEEKS) and a pau
i02 blk=['J-7', 'MAYA'] | J-7 You could end it. Confess. Terminate the deployment. The lab | J-7 faces MAYA and speaks. He rolls in, coffee in hand — his one human affectati
i03 blk=['MAYA'] | MAYA It's not a romance. It's a deployment. | MAYA faces J-7 and speaks.
i04 blk=['J-7'] | J-7 Your cortisol— | J-7 faces MAYA and speaks.
i05 blk=['J-7', 'MAYA'] | MAYA Don't. | MAYA faces J-7 and speaks.
i06 blk=['J-7'] | J-7 —decreases 40 percent in his presence. | J-7 faces MAYA and speaks.
i07 blk=['MAYA'] | MAYA J-7. | MAYA faces J-7 and speaks.
i08 blk=['J-7', 'MAYA'] | J-7 You built me to imitate humans, Maya. Nobody told you they i | J-7 faces MAYA and speaks.
i09 blk=[] | -  | Maya looks at the frozen frame on the screen. A long time.
i10 blk=['MAYA'] | MAYA Sixty days. Then it's done. Then he's married to whoever sur | MAYA faces J-7 and speaks.
i11 blk=['J-7', 'MAYA'] | J-7 That was the contract. | J-7 faces MAYA and speaks.