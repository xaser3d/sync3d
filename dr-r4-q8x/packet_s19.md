# VALIDATION PACKET — scene s19
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 19 — INT. CROSS TOWER — VIDEO CONFERENCE — DAY

*DAMIEN and A.V.A. face a wall screen: HALVORSEN, a corporate raider
on video, mid-threat.*

HALVORSEN (ON SCREEN)
Walk away from the Bergen acquisition, Cross, or I take this board
fight public. You have forty-eight hours.

DAMIEN
Your last three acquisitions underperformed—

A.V.A.
(stepping slightly forward)
Mr. Halvorsen. Your pulse is visible on this feed at your carotid.
It spiked when you said "walk away." You cannot afford to walk away
— the Bergen position is leveraged against your flagship fund.
Fold now or the market folds for you within six weeks. Confidence:
ninety-two percent.

*Silence on the screen. Halvorsen's face does several small things.*

HALVORSEN (ON SCREEN)
...I'll call you.

*The call ends. Damien turns slowly to A.V.A.*

DAMIEN
You diagnosed his leverage from his neck.

A.V.A.
The neck is honest. The words were not.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 19,
  "scene_heading": "INT. CROSS TOWER — VIDEO CONFERENCE — DAY",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "The morning after the strategy meeting — A.V.A. is no longer in the corner. A corporate raider's ultimatum gets read off his own carotid artery on a compressed video feed. The scene is the audit-committee consequence in action: she wins the board fight in one look, and Damien is left holding the strangeness of what she just did.",
  "zones": [
    "video conference room"
  ],
  "events": [
    {
      "event_id": "s19.e01",
      "source_evidence": [
        "DAMIEN and A.V.A. face a wall screen: HALVORSEN, a corporate raider on video, mid-threat.",
        "Walk away from the Bergen acquisition, Cross, or I take this board fight public. You have forty-eight hours.",
        "Your last three acquisitions underperformed—"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the ultimatum — a raider on a screen sets a forty-eight-hour clock, and Damien's parry is already running on yesterday's weapons",
      "participants": [
        "DAMIEN",
        "A.V.A."
      ],
      "remote_participants": [
        {
          "actor": "HALVORSEN",
          "channel": "wall screen video call",
          "direction": "screen → room"
        }
      ],
      "depicts_via_channel": [
        {
          "actors": [
            "HALVORSEN"
          ],
          "seen_by": [
            "DAMIEN",
            "A.V.A."
          ],
          "channel": "wall screen",
          "from_zone": "remote"
        }
      ],
      "location": {
        "zone": "video conference room"
      },
      "timeline": [
        {
          "beat": "Damien and A.V.A. face the wall screen — Halvorsen mid-threat",
          "type": "held_image"
        },
        {
          "beat": "the ultimatum — 'walk away from Bergen... you have forty-eight hours'",
          "type": "dialogue_remote"
        },
        {
          "beat": "Damien's parry — 'Your last three acquisitions underperformed—' cut short",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the wall screen dominates — Halvorsen is a head at giant scale, compressed and confident",
        "Damien's line must die in the air — the cut-off is scripted, not a flub"
      ],
      "audio_requirements": [
        "his voice arrives compressed through the call — boardroom menace at speakerphone fidelity"
      ],
      "continuity_constraints": [
        "Halvorsen exists only on the screen — he never shares the room; all his power is picture and voice"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "A.V.A."
      ],
      "tableau": true,
      "shot_sequence": [
        "s19.sh01"
      ]
    },
    {
      "event_id": "s19.e02",
      "source_evidence": [
        "(stepping slightly forward)",
        "Mr. Halvorsen. Your pulse is visible on this feed at your carotid. It spiked when you said \"walk away.\" You cannot afford to walk away — the Bergen position is leveraged against your flagship fund. Fold now or the market folds for you within six weeks. Confidence: ninety-two percent."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the counter-ultimatum — she steps forward once and dismantles him with his own pulse; the machine prices a bluff at ninety-two percent confidence",
      "participants": [
        "DAMIEN",
        "A.V.A."
      ],
      "remote_participants": [
        {
          "actor": "HALVORSEN",
          "channel": "wall screen video call",
          "direction": "screen → room"
        }
      ],
      "location": {
        "zone": "video conference room"
      },
      "timeline": [
        {
          "beat": "she steps slightly forward — one step, the only movement she needs",
          "type": "action"
        },
        {
          "beat": "the diagnosis as threat — pulse at the carotid, leverage priced, 'fold now'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the step forward is the whole choreography — she enters the call's power frame and never has to touch anything",
        "her delivery stays clinical — 'Confidence: ninety-two percent' is scarier than any raised voice"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "this is the real A.V.A. operating at full read — same instrument as the expense arithmetic (S18), new target"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s19.sh02"
      ]
    },
    {
      "event_id": "s19.e03",
      "source_evidence": [
        "Silence on the screen. Halvorsen's face does several small things.",
        "...I'll call you.",
        "The call ends."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the fold — a raider's face performing arithmetic in real time, then retreating behind 'I'll call you'; the whole fight ends inside his expression",
      "participants": [
        "DAMIEN",
        "A.V.A."
      ],
      "offscreen_present": [
        "DAMIEN",
        "A.V.A."
      ],
      "remote_participants": [
        {
          "actor": "HALVORSEN",
          "channel": "wall screen video call",
          "direction": "screen → room"
        }
      ],
      "depicts_via_channel": [
        {
          "actors": [
            "HALVORSEN"
          ],
          "seen_by": [
            "DAMIEN",
            "A.V.A."
          ],
          "channel": "wall screen",
          "from_zone": "remote"
        }
      ],
      "location": {
        "zone": "video conference room"
      },
      "timeline": [
        {
          "beat": "silence on the screen — his face does several small things",
          "type": "held_reaction"
        },
        {
          "beat": "'...I'll call you.' — the retreat",
          "type": "dialogue_remote"
        },
        {
          "beat": "the call ends — the screen goes dead",
          "type": "action"
        }
      ],
      "visual_requirements": [
        "this is a screen-within-frame event — the room's two watchers stay out of the picture while his face runs the numbers",
        "'several small things' is the performance brief: fear, recalculation, face-saving — in that order"
      ],
      "audio_requirements": [
        "compressed silence on the feed while his face does small things",
        "the call ends — channel click into room tone"
      ],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [],
      "tableau": false,
      "shot_sequence": [
        "s19.sh03",
        "s19.snd01"
      ]
    },
    {
      "event_id": "s19.e04",
      "source_evidence": [
        "Damien turns slowly to A.V.A.",
        "You diagnosed his leverage from his neck.",
        "The neck is honest. The words were not."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the debrief — Damien names what he just watched and she gives him the film's most quotable definition of her gift",
      "participants": [
        "DAMIEN",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "video conference room"
      },
      "timeline": [
        {
          "beat": "Damien turns slowly to her — the board fight already behind him",
          "type": "action"
        },
        {
          "beat": "'You diagnosed his leverage from his neck.'",
          "type": "dialogue"
        },
        {
          "beat": "'The neck is honest. The words were not.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the slow turn is measured — a man recalibrating what is standing next to him",
        "her answer is flat and factual — she is not bragging; that is what makes it land"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "this is A.V.A. the machine, not Maya — Damien is describing the unit's capability, unaware how much of it he has been falling for"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "A.V.A."
      ],
      "tableau": true,
      "shot_sequence": [
        "s19.sh04"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s19.sh01",
      "size": "WS",
      "zone": "video conference room",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "A.V.A."
      ],
      "depicts": [
        {
          "actors": [
            "HALVORSEN"
          ],
          "channel": "wall screen"
        }
      ],
      "implements": [
        "s19.e01"
      ],
      "covers_beats": {
        "s19.e01": [
          0,
          1,
          2
        ]
      },
      "purpose": "the wall screen dominates — Halvorsen's ultimatum at giant scale, Damien's parry dying in the air",
      "audio_note": "his voice compressed through the call; room quiet",
      "dialogue_lines": [
        {
          "event_id": "s19.e01",
          "speaker": "HALVORSEN",
          "line": "Walk away from the Bergen acquisition, Cross, or I take this board fight public. You have forty-eight hours.",
          "line_kind": "remote_channel",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s19.e01",
          "speaker": "DAMIEN",
          "line": "Your last three acquisitions underperformed—",
          "line_kind": "on_camera",
          "recipient": "HALVORSEN",
          "recipient_presence": "remote",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s19.sh02",
      "size": "MCU→M",
      "zone": "video conference room",
      "type": "visual",
      "participants": [
        "A.V.A.",
        "DAMIEN"
      ],
      "implements": [
        "s19.e02"
      ],
      "covers_beats": {
        "s19.e02": [
          0,
          1
        ]
      },
      "purpose": "one step forward into the call's power frame — the counter-ultimatum read off his carotid",
      "dialogue_lines": [
        {
          "event_id": "s19.e02",
          "speaker": "A.V.A.",
          "line": "Mr. Halvorsen. Your pulse is visible on this feed at your carotid. It spiked when you said \"walk away.\" You cannot afford to walk away — the Bergen position is leveraged against your flagship fund. Fold now or the market folds for you within six weeks. Confidence: ninety-two percent.",
          "line_kind": "on_camera",
          "recipient": "HALVORSEN",
          "recipient_presence": "remote",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s19.sh03",
      "size": "INS screen",
      "zone": "video conference room",
      "type": "visual",
      "participants": [],
      "depicts": [
        {
          "actors": [
            "HALVORSEN"
          ],
          "channel": "wall screen"
        }
      ],
      "implements": [
        "s19.e03"
      ],
      "covers_beats": {
        "s19.e03": [
          0,
          1,
          2
        ]
      },
      "purpose": "the fold — his face runs the arithmetic in compressed silence, then '...I'll call you.', then the dead channel",
      "audio_note": "compressed feed silence, channel click into room tone",
      "dialogue_lines": [
        {
          "event_id": "s19.e03",
          "speaker": "HALVORSEN",
          "line": "...I'll call you.",
          "line_kind": "remote_channel",
          "recipient": "DAMIEN",
          "recipient_presence": "offscreen",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s19.sh04",
      "size": "two-shot",
      "zone": "video conference room",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "A.V.A."
      ],
      "implements": [
        "s19.e04"
      ],
      "covers_beats": {
        "s19.e04": [
          0,
          1,
          2
        ]
      },
      "purpose": "the slow turn and the debrief — 'You diagnosed his leverage from his neck.' / 'The neck is honest. The words were not.'",
      "dialogue_lines": [
        {
          "event_id": "s19.e04",
          "speaker": "DAMIEN",
          "line": "You diagnosed his leverage from his neck.",
          "line_kind": "on_camera",
          "recipient": "A.V.A.",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s19.e04",
          "speaker": "A.V.A.",
          "line": "The neck is honest. The words were not.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s19.snd01",
      "type": "sound",
      "implements": [
        "s19.e03"
      ],
      "purpose": "sound card: compressed silence on the feed while his face does small things; the call ends — channel click into room tone; no score",
      "audio_note": "compressed silence on the feed, dead channel click into room tone, no score",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "DAMIEN and A.V.A. face a wall screen: HALVORSEN, a corporate raider on video, mid-threat.",
      "disposition": "covered_by",
      "by": [
        "s19.e01"
      ]
    },
    {
      "span": "Walk away from the Bergen acquisition, Cross, or I take this board fight public. You have forty-eight hours.",
      "disposition": "covered_by",
      "by": [
        "s19.e01"
      ]
    },
    {
      "span": "Your last three acquisitions underperformed—",
      "disposition": "covered_by",
      "by": [
        "s19.e01"
      ]
    },
    {
      "span": "stepping slightly forward",
      "disposition": "covered_by",
      "by": [
        "s19.e02"
      ]
    },
    {
      "span": "Mr. Halvorsen. Your pulse is visible on this feed at your carotid. It spiked when you said \"walk away.\" You cannot afford to walk away — the Bergen position is leveraged against your flagship fund. Fold now or the market folds for you within six weeks. Confidence: ninety-two percent.",
      "disposition": "covered_by",
      "by": [
        "s19.e02"
      ]
    },
    {
      "span": "Silence on the screen. Halvorsen's face does several small things.",
      "disposition": "covered_by",
      "by": [
        "s19.e03"
      ]
    },
    {
      "span": "...I'll call you.",
      "disposition": "covered_by",
      "by": [
        "s19.e03"
      ]
    },
    {
      "span": "The call ends. Damien turns slowly to A.V.A.",
      "disposition": "covered_by",
      "by": [
        "s19.e03",
        "s19.e04"
      ]
    },
    {
      "span": "You diagnosed his leverage from his neck.",
      "disposition": "covered_by",
      "by": [
        "s19.e04"
      ]
    },
    {
      "span": "The neck is honest. The words were not.",
      "disposition": "covered_by",
      "by": [
        "s19.e04"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['DAMIEN', 'HALVORSEN'] | -  | DAMIEN and A.V.A. face a wall screen: HALVORSEN, a corporate raider on video, mi
i02 blk=['HALVORSEN', 'DAMIEN'] | HALVORSEN Walk away from the Bergen acquisition, Cross, or I take this | HALVORSEN faces DAMIEN and speaks.
i03 blk=['DAMIEN'] | DAMIEN Your last three acquisitions underperformed— | DAMIEN faces HALVORSEN and speaks.
i04 blk=['A.V.A.'] | A.V.A. Mr. Halvorsen. Your pulse is visible on this feed at your ca | A.V.A. faces HALVORSEN and speaks.
i05 blk=[] | -  | Silence on the screen. Halvorsen's face does several small things.
i06 blk=['DAMIEN', 'HALVORSEN'] | HALVORSEN ...I'll call you. | HALVORSEN faces DAMIEN and speaks.
i07 blk=['DAMIEN', 'HALVORSEN'] | DAMIEN You diagnosed his leverage from his neck. | The call ends. Damien turns slowly to A.V.A.
i08 blk=['A.V.A.'] | A.V.A. The neck is honest. The words were not. | A.V.A. faces HALVORSEN and speaks.