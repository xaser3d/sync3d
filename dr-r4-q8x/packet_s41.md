# VALIDATION PACKET — scene s41
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 41 — INT. VOLT LAB — RELAUNCH EVENT — DAY

*The lab relaunch — press, investors, a stage with the new
product line: declared, honest, human + AI partnerships.*

*On stage: MAYA at the podium. Beside her — A.V.A., upgraded,
in a smart suit, holding a cue card she clearly doesn't need.*

MAYA (TO PRESS)
The A-500 series ships with a full disclosure page — what it
is, what it isn't, what it can never replace. The lesson of
the last year is that the market doesn't want a machine that
pretends to be human. It wants machines that are honest about
being machines, and humans who are brave enough to be human.

*A.V.A. steps to the mic, deadpan:*

A.V.A.
I have reviewed her remarks. They are accurate. Confidence:
ninety-six percent.

*Laughter. Somewhere in the crowd, JIM wipes his eye, and
SOPHIA — now the lab's head of investor relations, the trophy
who learned to work — applauds loudest.*

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 41,
  "scene_heading": "INT. VOLT LAB — RELAUNCH EVENT — DAY",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "The public verdict. The lab relaunches on the opposite premise from the gala: machines honest about being machines, humans brave enough to be human — the disclosure page is the company's whole thesis on one sheet. A.V.A. stands on stage in a suit holding a cue card she doesn't need — present, upgraded, and still incapable of saying anything warmer than 'Confidence: ninety-six percent.' Jim wipes his eye; Sophia, the trophy who learned to work, applauds loudest.",
  "zones": [
    "relaunch stage",
    "relaunch floor"
  ],
  "events": [
    {
      "event_id": "s41.e01",
      "source_evidence": [
        "The lab relaunch — press, investors, a stage with the new product line: declared, honest, human + AI partnerships.",
        "On stage: MAYA at the podium. Beside her — A.V.A., upgraded, in a smart suit, holding a cue card she clearly doesn't need."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the relaunch tableau — the company is reborn on honesty, and the two women share the stage: the founder at the podium, the product in a suit, holding a cue card she doesn't need",
      "participants": [
        "MAYA",
        "A.V.A.",
        "PRESS"
      ],
      "remote_participants": [],
      "location": {
        "zones": [
          "relaunch stage",
          "relaunch floor"
        ],
        "primary": "relaunch stage"
      },
      "timeline": [
        {
          "beat": "the relaunch — press, investors, a stage with the new declared-honest product line",
          "type": "atmosphere"
        },
        {
          "beat": "on stage — Maya at the podium, A.V.A. upgraded beside her with the cue card she doesn't need",
          "type": "reveal"
        }
      ],
      "visual_requirements": [
        "the new line reads as declared and honest — disclosure forward, no glamour-masking",
        "the unneeded cue card is the character beat — a prop she carries out of courtesy, not necessity"
      ],
      "audio_requirements": [
        "event-hall hubbub — press walla, camera shutters, stage PA idle"
      ],
      "continuity_constraints": [
        "A.V.A. is physically present and upgraded — no dock, no impersonation, no concealment; the opposite of the gala"
      ],
      "ambiguities": [
        "'investors' has no dedicated extras group — modeled inside the PRESS/floor crowd"
      ],
      "must_appear": [
        "MAYA",
        "A.V.A."
      ],
      "tableau": true,
      "shot_sequence": [
        "s41.sh01",
        "s41.snd01"
      ]
    },
    {
      "event_id": "s41.e02",
      "source_evidence": [
        "The A-500 series ships with a full disclosure page — what it is, what it isn't, what it can never replace.",
        "The lesson of the last year is that the market doesn't want a machine that pretends to be human. It wants machines that are honest about being machines, and humans who are brave enough to be human."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the thesis stated as product copy — the disclosure page is the film's ethics shipped as a feature; Maya's speech converts the year's catastrophe into a market position",
      "participants": [
        "MAYA",
        "A.V.A.",
        "PRESS"
      ],
      "offscreen_present": [
        "PRESS"
      ],
      "remote_participants": [],
      "location": {
        "zone": "relaunch stage"
      },
      "timeline": [
        {
          "beat": "the disclosure page — what it is, what it isn't, what it can never replace",
          "type": "dialogue"
        },
        {
          "beat": "the lesson — honest machines, brave humans",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the speech is delivered as product copy, not confession — she is a founder, not a penitent"
      ],
      "audio_requirements": [
        "podium PA — the speech live in the room"
      ],
      "continuity_constraints": [
        "'what it can never replace' directly answers the gala demonstration and the impersonation scheme"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s41.sh02",
        "s41.snd01"
      ]
    },
    {
      "event_id": "s41.e03",
      "source_evidence": [
        "A.V.A. steps to the mic, deadpan:",
        "I have reviewed her remarks. They are accurate. Confidence: ninety-six percent."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the product endorses the founder — A.V.A.'s deadpan fact-check is both the comedy beat and the proof that the honest-machine pitch is literal",
      "participants": [
        "A.V.A.",
        "MAYA",
        "PRESS"
      ],
      "offscreen_present": [
        "MAYA",
        "PRESS"
      ],
      "remote_participants": [],
      "location": {
        "zone": "relaunch stage"
      },
      "timeline": [
        {
          "beat": "A.V.A. steps to the mic, deadpan",
          "type": "action"
        },
        {
          "beat": "'I have reviewed her remarks. They are accurate. Confidence: ninety-six percent.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "she does not drop the cue card — the courtesy prop stays in hand while she improvises the review"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "ninety-six percent — the machine still reports affection as a confidence interval; nothing about her has been sentimentalized"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s41.sh03"
      ]
    },
    {
      "event_id": "s41.e04",
      "source_evidence": [
        "Laughter. Somewhere in the crowd, JIM wipes his eye, and SOPHIA — now the lab's head of investor relations, the trophy who learned to work — applauds loudest."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the landing — the laugh tells us the pitch worked, and the two planted reactions pay off arcs: Jim's tears for the machine he babysat, Sophia's applause as the trophy who learned to work",
      "participants": [
        "JIM",
        "SOPHIA",
        "PRESS"
      ],
      "remote_participants": [],
      "location": {
        "zone": "relaunch floor"
      },
      "timeline": [
        {
          "beat": "laughter somewhere in the crowd",
          "type": "reaction"
        },
        {
          "beat": "Jim wipes his eye",
          "type": "reaction"
        },
        {
          "beat": "Sophia — head of investor relations now — applauds loudest",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "find Jim and Sophia inside the crowd — reactions, not walk-ons"
      ],
      "audio_requirements": [
        "crowd laughter building to applause, Sophia's applause on top"
      ],
      "continuity_constraints": [
        "Sophia's title is established here — head of investor relations; the S44 card pays it off as 'scariest person in the building'"
      ],
      "ambiguities": [],
      "must_appear": [
        "JIM",
        "SOPHIA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s41.sh04",
        "s41.snd01"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s41.sh01",
      "size": "W",
      "zone": "relaunch stage",
      "type": "visual",
      "participants": [
        "MAYA",
        "A.V.A.",
        "PRESS"
      ],
      "implements": [
        "s41.e01"
      ],
      "covers_beats": {
        "s41.e01": [
          0,
          1
        ]
      },
      "purpose": "the relaunch stage over the floor — Maya at the podium, A.V.A. beside her with the unneeded cue card",
      "audio_note": "event-hall hubbub, press walla, camera shutters"
    },
    {
      "shot_id": "s41.sh02",
      "size": "two-shot",
      "zone": "relaunch stage",
      "type": "visual",
      "participants": [
        "MAYA",
        "A.V.A."
      ],
      "implements": [
        "s41.e02"
      ],
      "covers_beats": {
        "s41.e02": [
          0,
          1
        ]
      },
      "purpose": "the disclosure-page speech — founder at the podium, product at her shoulder",
      "audio_note": "podium PA live in the room",
      "dialogue_lines": [
        {
          "event_id": "s41.e02",
          "speaker": "MAYA",
          "line": "The A-500 series ships with a full disclosure page — what it is, what it isn't, what it can never replace.",
          "line_kind": "on_camera",
          "recipient": "PRESS",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s41.e02",
          "speaker": "MAYA",
          "line": "The lesson of the last year is that the market doesn't want a machine that pretends to be human. It wants machines that are honest about being machines, and humans who are brave enough to be human.",
          "line_kind": "on_camera",
          "recipient": "PRESS",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s41.sh03",
      "size": "M",
      "zone": "relaunch stage",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s41.e03"
      ],
      "covers_beats": {
        "s41.e03": [
          0,
          1
        ]
      },
      "purpose": "she steps to the mic, deadpan — the fact-check as endorsement",
      "audio_note": "mic presence, room held",
      "dialogue_lines": [
        {
          "event_id": "s41.e03",
          "speaker": "A.V.A.",
          "line": "I have reviewed her remarks. They are accurate. Confidence: ninety-six percent.",
          "line_kind": "on_camera",
          "recipient": "PRESS",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s41.sh04",
      "size": "M crowd",
      "zone": "relaunch floor",
      "type": "visual",
      "participants": [
        "JIM",
        "SOPHIA",
        "PRESS"
      ],
      "implements": [
        "s41.e04"
      ],
      "covers_beats": {
        "s41.e04": [
          0,
          1,
          2
        ]
      },
      "purpose": "the crowd lands it — laughter, Jim wiping his eye, Sophia applauding loudest",
      "audio_note": "crowd laughter into applause"
    },
    {
      "shot_id": "s41.snd01",
      "type": "sound",
      "implements": [
        "s41.e01",
        "s41.e02",
        "s41.e04"
      ],
      "purpose": "sound card: event-hall hubbub and podium PA for the stage, crowd laughter into applause for the floor — diegetic event sound, no score over the pitch",
      "audio_note": "press walla, camera shutters, podium PA live in the room, crowd laughter building to applause",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "The lab relaunch — press, investors, a stage with the new product line: declared, honest, human + AI partnerships.",
      "disposition": "covered_by",
      "by": [
        "s41.e01"
      ]
    },
    {
      "span": "On stage: MAYA at the podium. Beside her — A.V.A., upgraded, in a smart suit, holding a cue card she clearly doesn't need.",
      "disposition": "covered_by",
      "by": [
        "s41.e01"
      ]
    },
    {
      "span": "The A-500 series ships with a full disclosure page — what it is, what it isn't, what it can never replace.",
      "disposition": "covered_by",
      "by": [
        "s41.e02"
      ]
    },
    {
      "span": "A.V.A. steps to the mic, deadpan:",
      "disposition": "covered_by",
      "by": [
        "s41.e03"
      ]
    },
    {
      "span": "I have reviewed her remarks. They are accurate. Confidence: ninety-six percent.",
      "disposition": "covered_by",
      "by": [
        "s41.e03"
      ]
    },
    {
      "span": "JIM wipes his eye, and SOPHIA — now the lab's head of investor relations, the trophy who learned to work — applauds loudest.",
      "disposition": "covered_by",
      "by": [
        "s41.e04"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['MAYA', 'A.V.A.'] | -  | The lab relaunch — press, investors, a stage with the new product line: declared
i02 blk=['MAYA'] | -  | On stage: MAYA at the podium. Beside her — A.V.A., upgraded, in a smart formalwe
i03 blk=['MAYA', 'A.V.A.'] | MAYA The A-500 series ships with a full disclosure page — what it | MAYA faces A.V.A. and speaks.
i04 blk=['A.V.A.'] | A.V.A. I have reviewed her remarks. They are accurate. Confidence:  | A.V.A. steps to the mic, deadpan.
i05 blk=['JIM', 'SOPHIA'] | -  | Laughter. Somewhere in the crowd, JIM wipes his eye, and SOPHIA — now the lab's 