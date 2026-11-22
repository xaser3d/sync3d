# VALIDATION PACKET — scene s42
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 42 — INT. CROSS PENTHOUSE — BREAKFAST — MORNING

*The penthouse, softer now — books, a plant that's survived,
evidence of a person. DAMIEN at the counter. MAYA steals the
toast off his plate, unbothered.*

*In the corner — A.V.A. on a home dock, charging, eyes closed.*

DAMIEN
You're eating my toast.

MAYA
Community property. It's in the trust clause — page two,
the adjectives.

DAMIEN
Those adjectives cost me an empire and got me a partner who
steals toast. Worst trade I ever made.

MAYA
Best trade. I've read the filings.

*A.V.A.'s eyes open — mid-boot, unasked:*

A.V.A.
Your calendar shows a board crisis at ten. I have already
solved it. You're welcome.

DAMIEN
(to Maya)
She's gotten smug since the relaunch.

MAYA
She gets it from me.

A.V.A.
Also: probability of a marriage proposal from this unit's
observations — within ninety days: seventy-eight percent.
I have already compiled the statistics on your union.

*Beat. Maya freezes mid-toast-bite. Damien goes very still.*

A.V.A. (CONT'D)
They are... promising. Probably.

*She closes her eyes and returns to meditation mode — mission
accomplished. Maya and Damien look at each other. The toast,
forgotten, goes cold.*

MAYA
She's not wrong. She's never wrong — it's her worst feature.

DAMIEN
Seventy-eight percent is a terrible margin for a proposal.
I'd want better numbers.

MAYA
Then improve the sample size.

*He kisses her. From the dock — without opening her eyes:*

A.V.A.
Logging. Sample size: improved.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 42,
  "scene_heading": "INT. CROSS PENTHOUSE — BREAKFAST — MORNING",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "Domestic proof. The penthouse that hosted the gala's cold geometry is now soft — books, a plant that survived, toast worth stealing. The comedy engine is A.V.A. on a home dock in the corner, eyes closed, who wakes mid-boot only to inform the couple she has already compiled the statistics on their union: a marriage proposal within ninety days at seventy-eight percent. 'Then improve the sample size' is how these two flirt — and when he kisses her, she logs the improved sample without opening her eyes.",
  "zones": [
    "penthouse kitchen counter",
    "penthouse dock corner"
  ],
  "events": [
    {
      "event_id": "s42.e01",
      "source_evidence": [
        "The penthouse, softer now — books, a plant that's survived, evidence of a person. DAMIEN at the counter. MAYA steals the toast off his plate, unbothered.",
        "In the corner — A.V.A. on a home dock, charging, eyes closed."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the softened penthouse — domesticity as set dressing: a living plant, stolen toast, and the third member of the household meditating on her dock in the corner",
      "participants": [
        "DAMIEN",
        "MAYA",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zones": [
          "penthouse kitchen counter",
          "penthouse dock corner"
        ],
        "primary": "penthouse kitchen counter"
      },
      "timeline": [
        {
          "beat": "the penthouse softer — books, a plant that's survived, evidence of a person",
          "type": "atmosphere"
        },
        {
          "beat": "Damien at the counter; Maya steals the toast off his plate, unbothered",
          "type": "action"
        },
        {
          "beat": "in the corner — A.V.A. on a home dock, charging, eyes closed",
          "type": "held_image"
        }
      ],
      "visual_requirements": [
        "the softness must be legible — this is the same room as the gala-era penthouse, warmed by occupancy",
        "A.V.A. on the home dock reads as furniture-adjacent family — present, charging, unbothered"
      ],
      "audio_requirements": [
        "quiet breakfast room tone — toast, plate, dock charge hum from the corner"
      ],
      "continuity_constraints": [
        "the plant that survived pays off the dead-plant penthouse of the early acts",
        "the toast theft is casual — established-married energy, not courtship"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "MAYA",
        "A.V.A."
      ],
      "tableau": true,
      "shot_sequence": [
        "s42.sh01",
        "s42.snd01"
      ]
    },
    {
      "event_id": "s42.e02",
      "source_evidence": [
        "You're eating my toast.",
        "Community property. It's in the trust clause — page two, the adjectives.",
        "Those adjectives cost me an empire and got me a partner who steals toast. Worst trade I ever made.",
        "Best trade. I've read the filings."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the toast arbitration — the trust clause that detonated the act now governs breakfast; 'worst trade' / 'best trade' is the whole third act compressed into a volley",
      "participants": [
        "DAMIEN",
        "MAYA",
        "A.V.A."
      ],
      "offscreen_present": [
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zone": "penthouse kitchen counter"
      },
      "timeline": [
        {
          "beat": "'You're eating my toast.'",
          "type": "dialogue"
        },
        {
          "beat": "'Community property... page two, the adjectives.'",
          "type": "dialogue"
        },
        {
          "beat": "'Worst trade I ever made.'",
          "type": "dialogue"
        },
        {
          "beat": "'Best trade. I've read the filings.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "a domestic two-shot — the volley is relaxed; both of them have already won the argument"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "'the trust clause — page two, the adjectives' — same document Penhaligon ruled on in S40, now governing toast"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s42.sh02"
      ]
    },
    {
      "event_id": "s42.e03",
      "source_evidence": [
        "A.V.A.'s eyes open — mid-boot, unasked:",
        "Your calendar shows a board crisis at ten. I have already solved it. You're welcome.",
        "She's gotten smug since the relaunch.",
        "She gets it from me."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the unsolicited assist — A.V.A. wakes mid-boot purely to announce she has already solved their day; 'smug since the relaunch' / 'she gets it from me' assigns her authorship to Maya",
      "participants": [
        "DAMIEN",
        "MAYA",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zones": [
          "penthouse dock corner",
          "penthouse kitchen counter"
        ],
        "primary": "penthouse dock corner"
      },
      "timeline": [
        {
          "beat": "A.V.A.'s eyes open — mid-boot, unasked",
          "type": "action"
        },
        {
          "beat": "'Your calendar shows a board crisis at ten. I have already solved it. You're welcome.'",
          "type": "dialogue"
        },
        {
          "beat": "Damien to Maya — 'She's gotten smug since the relaunch.'",
          "type": "dialogue"
        },
        {
          "beat": "'She gets it from me.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "she does not leave the dock or open her eyes before she has to — the interjection arrives mid-boot, still seated",
        "the smugness exchange plays between the couple, not at the dock — they discuss her like parents"
      ],
      "audio_requirements": [
        "a small mid-boot wake sound as her eyes open — the dock's voice, not a fanfare"
      ],
      "continuity_constraints": [
        "'since the relaunch' dates the smugness to S41's ninety-six percent — she has been unbearable for weeks"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A.",
        "DAMIEN",
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s42.sh03",
        "s42.sh04",
        "s42.snd01"
      ]
    },
    {
      "event_id": "s42.e04",
      "source_evidence": [
        "Also: probability of a marriage proposal from this unit's observations — within ninety days: seventy-eight percent. I have already compiled the statistics on your union.",
        "Beat. Maya freezes mid-toast-bite. Damien goes very still.",
        "They are... promising. Probably.",
        "She closes her eyes and returns to meditation mode — mission accomplished. Maya and Damien look at each other. The toast, forgotten, goes cold."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the proposal statistics drop — A.V.A. announces their engagement before it exists, freezes them both mid-bite, hedges ('probably'), and returns to meditation mode mission accomplished; the toast goes cold like a held frame",
      "participants": [
        "DAMIEN",
        "MAYA",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zones": [
          "penthouse dock corner",
          "penthouse kitchen counter"
        ],
        "primary": "penthouse dock corner"
      },
      "timeline": [
        {
          "beat": "'within ninety days: seventy-eight percent' — the statistics on their union, already compiled",
          "type": "dialogue"
        },
        {
          "beat": "Maya freezes mid-toast-bite; Damien goes very still",
          "type": "reaction"
        },
        {
          "beat": "'They are... promising. Probably.'",
          "type": "dialogue"
        },
        {
          "beat": "she closes her eyes — back to meditation mode, mission accomplished",
          "type": "action"
        },
        {
          "beat": "Maya and Damien look at each other; the toast, forgotten, goes cold",
          "type": "held_reaction"
        }
      ],
      "visual_requirements": [
        "the freeze is the scene's pivot — two adults stopped by a percentage; hold it a beat too long",
        "'probably' is the biggest word she has ever learned — let the hedge land before the eyes close",
        "the cold toast is the punchline of the silence — breakfast abandoned mid-bite"
      ],
      "audio_requirements": [
        "eyes-closed return to dock hum — the power-down of a delivered bomb"
      ],
      "continuity_constraints": [
        "ninety days / seventy-eight percent echo S39's trial period — the machine's calendar is the film's courtship clock",
        "'from this unit's observations' — she has been watching them the way J-7 taught her to watch"
      ],
      "ambiguities": [],
      "must_appear": [
        "A.V.A.",
        "DAMIEN",
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s42.sh05",
        "s42.sh06",
        "s42.sh07",
        "s42.sh08",
        "s42.snd01"
      ]
    },
    {
      "event_id": "s42.e05",
      "source_evidence": [
        "She's not wrong. She's never wrong — it's her worst feature.",
        "Seventy-eight percent is a terrible margin for a proposal. I'd want better numbers.",
        "Then improve the sample size.",
        "He kisses her. From the dock — without opening her eyes:",
        "Logging. Sample size: improved."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the flirtation in her units — 'improve the sample size' is the proposal-adjacent banter, the kiss is the improved sample, and A.V.A. logs it from the dock without opening her eyes",
      "participants": [
        "DAMIEN",
        "MAYA",
        "A.V.A."
      ],
      "remote_participants": [],
      "location": {
        "zones": [
          "penthouse kitchen counter",
          "penthouse dock corner"
        ],
        "primary": "penthouse kitchen counter"
      },
      "timeline": [
        {
          "beat": "'She's not wrong. She's never wrong — it's her worst feature.'",
          "type": "dialogue"
        },
        {
          "beat": "'Seventy-eight percent is a terrible margin... I'd want better numbers.'",
          "type": "dialogue"
        },
        {
          "beat": "'Then improve the sample size.'",
          "type": "dialogue"
        },
        {
          "beat": "he kisses her",
          "type": "action"
        },
        {
          "beat": "from the dock, eyes closed — 'Logging. Sample size: improved.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the kiss is small and domestic — a breakfast kiss, not a gala kiss",
        "A.V.A.'s logging line lands from the dock with eyes still closed — she measured the kiss without watching it"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "'logging' is her wedding-day vocabulary too — S43's 'For convention.' / 'Logging.' pair starts here"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "MAYA",
        "A.V.A."
      ],
      "tableau": false,
      "shot_sequence": [
        "s42.sh09",
        "s42.sh10",
        "s42.sh11",
        "s42.snd01"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s42.sh01",
      "size": "W",
      "zone": "penthouse kitchen counter",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "MAYA",
        "A.V.A."
      ],
      "implements": [
        "s42.e01"
      ],
      "covers_beats": {
        "s42.e01": [
          0,
          1,
          2
        ]
      },
      "purpose": "the softened penthouse — Damien at the counter, Maya stealing his toast, A.V.A. charging in the corner",
      "audio_note": "quiet breakfast room tone, toast and plate, dock charge hum from the corner"
    },
    {
      "shot_id": "s42.sh02",
      "size": "two-shot",
      "zone": "penthouse kitchen counter",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "implements": [
        "s42.e02"
      ],
      "covers_beats": {
        "s42.e02": [
          0,
          1,
          2,
          3
        ]
      },
      "purpose": "the toast arbitration — trust clause cited over breakfast",
      "dialogue_lines": [
        {
          "event_id": "s42.e02",
          "speaker": "DAMIEN",
          "line": "You're eating my toast.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s42.e02",
          "speaker": "MAYA",
          "line": "Community property. It's in the trust clause — page two, the adjectives.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s42.e02",
          "speaker": "DAMIEN",
          "line": "Those adjectives cost me an empire and got me a partner who steals toast. Worst trade I ever made.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s42.e02",
          "speaker": "MAYA",
          "line": "Best trade. I've read the filings.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        }
      ]
    },
    {
      "shot_id": "s42.sh03",
      "size": "M",
      "zone": "penthouse dock corner",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s42.e03"
      ],
      "covers_beats": {
        "s42.e03": [
          0,
          1
        ]
      },
      "purpose": "mid-boot, unasked — her eyes open on the dock and the assist arrives",
      "audio_note": "small mid-boot wake sound, dock hum",
      "dialogue_lines": [
        {
          "event_id": "s42.e03",
          "speaker": "A.V.A.",
          "line": "Your calendar shows a board crisis at ten. I have already solved it. You're welcome.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s42.sh04",
      "size": "two-shot",
      "zone": "penthouse kitchen counter",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "implements": [
        "s42.e03"
      ],
      "covers_beats": {
        "s42.e03": [
          2,
          3
        ]
      },
      "purpose": "the parents discuss the child — 'smug since the relaunch' / 'she gets it from me'",
      "dialogue_lines": [
        {
          "event_id": "s42.e03",
          "speaker": "DAMIEN",
          "line": "She's gotten smug since the relaunch.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s42.e03",
          "speaker": "MAYA",
          "line": "She gets it from me.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        }
      ]
    },
    {
      "shot_id": "s42.sh05",
      "size": "M",
      "zone": "penthouse dock corner",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s42.e04"
      ],
      "covers_beats": {
        "s42.e04": [
          0
        ]
      },
      "purpose": "the statistics drop — 'within ninety days: seventy-eight percent'",
      "dialogue_lines": [
        {
          "event_id": "s42.e04",
          "speaker": "A.V.A.",
          "line": "Also: probability of a marriage proposal from this unit's observations — within ninety days: seventy-eight percent.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s42.e04",
          "speaker": "A.V.A.",
          "line": "I have already compiled the statistics on your union.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s42.sh06",
      "size": "two-shot",
      "zone": "penthouse kitchen counter",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "implements": [
        "s42.e04"
      ],
      "covers_beats": {
        "s42.e04": [
          1
        ]
      },
      "purpose": "the freeze — Maya mid-toast-bite, Damien very still",
      "audio_note": "the held silence of the freeze"
    },
    {
      "shot_id": "s42.sh07",
      "size": "M",
      "zone": "penthouse dock corner",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s42.e04"
      ],
      "covers_beats": {
        "s42.e04": [
          2,
          3
        ]
      },
      "purpose": "'They are... promising. Probably.' — then the eyes close, mission accomplished",
      "audio_note": "eyes-closed return to dock hum",
      "dialogue_lines": [
        {
          "event_id": "s42.e04",
          "speaker": "A.V.A.",
          "line": "They are... promising. Probably.",
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
      "shot_id": "s42.sh08",
      "size": "two-shot",
      "zone": "penthouse kitchen counter",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "implements": [
        "s42.e04"
      ],
      "covers_beats": {
        "s42.e04": [
          4
        ]
      },
      "purpose": "they look at each other — the toast, forgotten, goes cold",
      "audio_note": "kitchen quiet over the cold toast"
    },
    {
      "shot_id": "s42.sh09",
      "size": "two-shot",
      "zone": "penthouse kitchen counter",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "implements": [
        "s42.e05"
      ],
      "covers_beats": {
        "s42.e05": [
          0,
          1,
          2
        ]
      },
      "purpose": "the margin talk — 'worst feature' / 'terrible margin' / 'improve the sample size'",
      "dialogue_lines": [
        {
          "event_id": "s42.e05",
          "speaker": "MAYA",
          "line": "She's not wrong. She's never wrong — it's her worst feature.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s42.e05",
          "speaker": "DAMIEN",
          "line": "Seventy-eight percent is a terrible margin for a proposal. I'd want better numbers.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s42.e05",
          "speaker": "MAYA",
          "line": "Then improve the sample size.",
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
      "shot_id": "s42.sh10",
      "size": "two-shot",
      "zone": "penthouse kitchen counter",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "MAYA"
      ],
      "implements": [
        "s42.e05"
      ],
      "covers_beats": {
        "s42.e05": [
          3
        ]
      },
      "purpose": "he kisses her — the sample improved",
      "audio_note": "kitchen quiet"
    },
    {
      "shot_id": "s42.sh11",
      "size": "M",
      "zone": "penthouse dock corner",
      "type": "visual",
      "participants": [
        "A.V.A."
      ],
      "implements": [
        "s42.e05"
      ],
      "covers_beats": {
        "s42.e05": [
          4
        ]
      },
      "purpose": "from the dock, eyes still closed — 'Logging. Sample size: improved.'",
      "dialogue_lines": [
        {
          "event_id": "s42.e05",
          "speaker": "A.V.A.",
          "line": "Logging. Sample size: improved.",
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
      "shot_id": "s42.snd01",
      "type": "sound",
      "implements": [
        "s42.e01",
        "s42.e03",
        "s42.e04",
        "s42.e05"
      ],
      "purpose": "sound card: quiet breakfast room tone and dock charge hum; a small mid-boot wake sound when her eyes open; the return to dock hum after 'Probably.' — no score, the household hum is the music",
      "audio_note": "quiet breakfast room tone, toast and plate, dock charge hum, small mid-boot wake sound, eyes-closed return to dock hum",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "The penthouse, softer now — books, a plant that's survived, evidence of a person.",
      "disposition": "covered_by",
      "by": [
        "s42.e01"
      ]
    },
    {
      "span": "In the corner — A.V.A. on a home dock, charging, eyes closed.",
      "disposition": "covered_by",
      "by": [
        "s42.e01"
      ]
    },
    {
      "span": "You're eating my toast.",
      "disposition": "covered_by",
      "by": [
        "s42.e02"
      ]
    },
    {
      "span": "Community property. It's in the trust clause — page two, the adjectives.",
      "disposition": "covered_by",
      "by": [
        "s42.e02"
      ]
    },
    {
      "span": "Those adjectives cost me an empire and got me a partner who steals toast. Worst trade I ever made.",
      "disposition": "covered_by",
      "by": [
        "s42.e02"
      ]
    },
    {
      "span": "Best trade. I've read the filings.",
      "disposition": "covered_by",
      "by": [
        "s42.e02"
      ]
    },
    {
      "span": "A.V.A.'s eyes open — mid-boot, unasked:",
      "disposition": "covered_by",
      "by": [
        "s42.e03"
      ]
    },
    {
      "span": "Your calendar shows a board crisis at ten. I have already solved it. You're welcome.",
      "disposition": "covered_by",
      "by": [
        "s42.e03"
      ]
    },
    {
      "span": "She's gotten smug since the relaunch.",
      "disposition": "covered_by",
      "by": [
        "s42.e03"
      ]
    },
    {
      "span": "probability of a marriage proposal from this unit's observations — within ninety days: seventy-eight percent.",
      "disposition": "covered_by",
      "by": [
        "s42.e04"
      ]
    },
    {
      "span": "Beat. Maya freezes mid-toast-bite. Damien goes very still.",
      "disposition": "covered_by",
      "by": [
        "s42.e04"
      ]
    },
    {
      "span": "They are... promising. Probably.",
      "disposition": "covered_by",
      "by": [
        "s42.e04"
      ]
    },
    {
      "span": "She closes her eyes and returns to meditation mode — mission accomplished.",
      "disposition": "covered_by",
      "by": [
        "s42.e04"
      ]
    },
    {
      "span": "She's not wrong. She's never wrong — it's her worst feature.",
      "disposition": "covered_by",
      "by": [
        "s42.e05"
      ]
    },
    {
      "span": "Seventy-eight percent is a terrible margin for a proposal. I'd want better numbers.",
      "disposition": "covered_by",
      "by": [
        "s42.e05"
      ]
    },
    {
      "span": "Then improve the sample size.",
      "disposition": "covered_by",
      "by": [
        "s42.e05"
      ]
    },
    {
      "span": "He kisses her. From the dock — without opening her eyes:",
      "disposition": "covered_by",
      "by": [
        "s42.e05"
      ]
    },
    {
      "span": "Logging. Sample size: improved.",
      "disposition": "covered_by",
      "by": [
        "s42.e05"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['DAMIEN', 'MAYA'] | -  | The penthouse, softer now — books, a plant that's survived, evidence of a person
i02 blk=['DAMIEN', 'MAYA'] | DAMIEN You're eating my toast. | In the corner — A.V.A. on a home dock, charging, eyes closed.
i03 blk=['MAYA'] | MAYA Community property. It's in the trust clause — page two, the | MAYA faces DAMIEN and speaks.
i04 blk=['DAMIEN'] | DAMIEN Those adjectives cost me an empire and got me a partner who  | DAMIEN faces MAYA and speaks.
i05 blk=['MAYA'] | MAYA Best trade. I've read the filings. | MAYA faces DAMIEN and speaks.
i06 blk=['DAMIEN', 'A.V.A.'] | A.V.A. Your calendar shows a board crisis at ten. I have already so | A.V.A.'s eyes open — mid-boot, unasked.
i07 blk=['DAMIEN'] | DAMIEN She's gotten smug since the relaunch. | DAMIEN faces MAYA and speaks.
i08 blk=['MAYA'] | MAYA She gets it from me. | MAYA faces DAMIEN and speaks.
i09 blk=['A.V.A.'] | A.V.A. Also: probability of a marriage proposal from this unit's ob | A.V.A. faces DAMIEN and speaks.
i10 blk=['DAMIEN', 'MAYA'] | -  | Beat. Maya freezes mid-toast-bite. Damien goes very still.
i11 blk=['A.V.A.', 'DAMIEN'] | A.V.A. They are... promising. Probably. | A.V.A. faces DAMIEN and speaks.
i12 blk=['DAMIEN', 'MAYA'] | -  | She closes her eyes and returns to meditation mode — mission accomplished. Maya 
i13 blk=['MAYA', 'DAMIEN'] | MAYA She's not wrong. She's never wrong — it's her worst feature. | MAYA faces DAMIEN and speaks.
i14 blk=['DAMIEN'] | DAMIEN Seventy-eight percent is a terrible margin for a proposal. I | DAMIEN faces MAYA and speaks.
i15 blk=['MAYA'] | MAYA Then improve the sample size. | MAYA faces DAMIEN and speaks.
i16 blk=['A.V.A.'] | A.V.A. Logging. Sample size: improved. | He kisses her. From the dock — without opening her eyes.