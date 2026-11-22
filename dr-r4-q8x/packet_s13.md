# VALIDATION PACKET — scene s13
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 13 — INT. CROSS TOWER — DAMIEN'S OFFICE — DAY

*VICTOR spreads a tablet of candidate profiles like a card dealer.*

VICTOR
The shortlist. Pre-vetted, family-clean, board-approved, each one
signed to a discretion agreement thicker than her résumé.

*On screen: SOPHIA VANE — stunning, socialite, yacht-adjacent.*

VICTOR (CONT'D)
Sophia Vane. Old money, new problems. Photographs like a dream,
golfs, donates to everything that has a dinner.

JIM (reading over Damien's shoulder)
Hobbies: "yachts, yacht litigation."

VICTOR
She's fun.

*Next: OCTAVIA MARLOWE — severe elegance, a smile that's been
notarized.*

VICTOR (CONT'D)
Octavia Marlowe. Steel dynasty, third generation. She once talked
a hedge fund into apologizing to her.

DAMIEN
In a good way?

VICTOR
There isn't a bad way to do that.

*Next: DR. ANNA REYES — warm, normal, a pediatric surgeon. She looks
like she wandered into the slide deck by mistake.*

VICTOR (CONT'D)
And Anna Reyes. Children's cardiac surgeon. Victor's note: wildcard —
the board wanted a "relatable" option for optics. She's alarmingly
sincere. Handle with tongs.

DAMIEN
Three candidates, eight weeks.

VICTOR
Two dates each. First impressions, then the compatibility retreat
weekend —

DAMIEN
There is no compatibility retreat weekend.

VICTOR
There is now. I own the resort.

*He gathers the tablet, pauses at the door — and his smile goes
genuine for the first time, which is somehow worse.*

VICTOR (CONT'D)
One more thing, brother. The trust clause is specific — the marriage
must be registered by your birthday gala. Not engaged. Married.
I've taken the liberty of holding a slot at the registrar. Consider
it a gift.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 13,
  "scene_heading": "INT. CROSS TOWER — DAMIEN'S OFFICE — DAY",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "Victor deals the marriage market like a card dealer: three pre-vetted candidates — Sophia Vane, Octavia Marlowe, Anna Reyes — each reduced to a slide and a pitch line. The scene is the machine of the trust clause made visible, and its last beat is the trap springing: 'Not engaged. Married.' plus a registrar slot booked as 'a gift.' Dates one and two (S14, S15) execute this shortlist in order.",
  "zones": [
    "damien's office"
  ],
  "events": [
    {
      "event_id": "s13.e01",
      "source_evidence": [
        "VICTOR spreads a tablet of candidate profiles like a card dealer.",
        "The shortlist. Pre-vetted, family-clean, board-approved, each one",
        "signed to a discretion agreement thicker than her résumé."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the market opens — courtship presented as a deal flow, candidates as paper",
      "participants": [
        "VICTOR",
        "DAMIEN",
        "JIM"
      ],
      "remote_participants": [],
      "location": {
        "zone": "damien's office"
      },
      "timeline": [
        {
          "beat": "Victor spreads the tablet of candidate profiles like a card dealer",
          "type": "action"
        },
        {
          "beat": "'The shortlist. Pre-vetted, family-clean, board-approved...'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the tablet handling is dealer's-work — profiles fanned like cards, people as inventory"
      ],
      "audio_requirements": [
        "tablet surface tap and swipe sounds — the deck being dealt"
      ],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "VICTOR",
        "DAMIEN",
        "JIM"
      ],
      "tableau": true,
      "shot_sequence": [
        "s13.sh01"
      ]
    },
    {
      "event_id": "s13.e02",
      "source_evidence": [
        "On screen: SOPHIA VANE — stunning, socialite, yacht-adjacent.",
        "Sophia Vane. Old money, new problems. Photographs like a dream,",
        "golfs, donates to everything that has a dinner.",
        "Hobbies: \"yachts, yacht litigation.\"",
        "She's fun."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "candidate one — the yacht-adjacent socialite; Jim's aside quietly files the evidence S14 will weaponize",
      "participants": [
        "VICTOR",
        "DAMIEN",
        "JIM"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "SOPHIA"
          ],
          "seen_by": [
            "VICTOR",
            "DAMIEN",
            "JIM"
          ],
          "channel": "tablet candidate profiles",
          "from_zone": "offsite"
        }
      ],
      "location": {
        "zone": "damien's office"
      },
      "timeline": [
        {
          "beat": "profile on screen — stunning, socialite, yacht-adjacent",
          "type": "insert"
        },
        {
          "beat": "'Sophia Vane. Old money, new problems...'",
          "type": "dialogue"
        },
        {
          "beat": "Jim over Damien's shoulder — 'Hobbies: \"yachts, yacht litigation.\"'",
          "type": "dialogue"
        },
        {
          "beat": "'She's fun.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "Sophia exists here only as a profile image — photographed perfection, not a person yet",
        "Jim reads over Damien's shoulder — he audits the deck, not the room"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the yacht fixation planted here — 'yachts, yacht litigation' is the loaded gun of date one (S14)"
      ],
      "ambiguities": [],
      "must_appear": [
        "JIM"
      ],
      "tableau": false,
      "shot_sequence": [
        "s13.sh02",
        "s13.sh03"
      ]
    },
    {
      "event_id": "s13.e03",
      "source_evidence": [
        "Next: OCTAVIA MARLOWE — severe elegance, a smile that's been",
        "notarized.",
        "Octavia Marlowe. Steel dynasty, third generation. She once talked",
        "a hedge fund into apologizing to her.",
        "In a good way?",
        "There isn't a bad way to do that."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "candidate two — the steel dynasty; even the pitch admits she out-negotiates predators",
      "participants": [
        "VICTOR",
        "DAMIEN"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "OCTAVIA"
          ],
          "seen_by": [
            "VICTOR",
            "DAMIEN"
          ],
          "channel": "tablet candidate profiles",
          "from_zone": "offsite"
        }
      ],
      "location": {
        "zone": "damien's office"
      },
      "timeline": [
        {
          "beat": "next profile — severe elegance, a smile that's been notarized",
          "type": "insert"
        },
        {
          "beat": "'Octavia Marlowe. Steel dynasty, third generation...'",
          "type": "dialogue"
        },
        {
          "beat": "'In a good way?'",
          "type": "dialogue"
        },
        {
          "beat": "'There isn't a bad way to do that.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the hedge-fund anecdote should land as admiration with a warning label — Victor enjoys her menace"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the 'chair' and merger vocabulary of S15 is prefigured — the pitch already frames her as an entity, not a bride"
      ],
      "ambiguities": [],
      "must_appear": [
        "VICTOR",
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s13.sh04",
        "s13.sh05"
      ]
    },
    {
      "event_id": "s13.e04",
      "source_evidence": [
        "Next: DR. ANNA REYES — warm, normal, a pediatric surgeon. She looks",
        "like she wandered into the slide deck by mistake.",
        "And Anna Reyes. Children's cardiac surgeon. Victor's note: wildcard —",
        "the board wanted a \"relatable\" option for optics. She's alarmingly",
        "sincere. Handle with tongs."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "candidate three — the wildcard; a sincere person inside a deck of strategic assets, flagged 'handle with tongs'",
      "participants": [
        "VICTOR",
        "DAMIEN"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "ANNA"
          ],
          "seen_by": [
            "VICTOR",
            "DAMIEN"
          ],
          "channel": "tablet candidate profiles",
          "from_zone": "offsite"
        }
      ],
      "location": {
        "zone": "damien's office"
      },
      "timeline": [
        {
          "beat": "next profile — warm, normal, wandered into the slide deck by mistake",
          "type": "insert"
        },
        {
          "beat": "'And Anna Reyes. Children's cardiac surgeon... Handle with tongs.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "her profile photo must not look cast for the part — warmth that reads accidental among the sharks"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "'alarmingly sincere' is the tell — the only candidate who threatens the plan by being real"
      ],
      "ambiguities": [],
      "must_appear": [
        "VICTOR",
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s13.sh06"
      ]
    },
    {
      "event_id": "s13.e05",
      "source_evidence": [
        "Three candidates, eight weeks.",
        "Two dates each. First impressions, then the compatibility retreat",
        "weekend —",
        "There is no compatibility retreat weekend.",
        "There is now. I own the resort."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the terms — a schedule set like a sprint, and Victor inventing infrastructure mid-sentence to own the outcome",
      "participants": [
        "DAMIEN",
        "VICTOR"
      ],
      "remote_participants": [],
      "location": {
        "zone": "damien's office"
      },
      "timeline": [
        {
          "beat": "'Three candidates, eight weeks.'",
          "type": "dialogue"
        },
        {
          "beat": "'Two dates each. First impressions, then the compatibility retreat weekend —'",
          "type": "dialogue"
        },
        {
          "beat": "'There is no compatibility retreat weekend.'",
          "type": "dialogue"
        },
        {
          "beat": "'There is now. I own the resort.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "'I own the resort' delivered as convenience, not threat — Victor's power move wears a concierge smile"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "two dates each is the stated plan — S14/S15 execute candidates one and two under this rule"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "VICTOR"
      ],
      "tableau": true,
      "shot_sequence": [
        "s13.sh07"
      ]
    },
    {
      "event_id": "s13.e06",
      "source_evidence": [
        "He gathers the tablet, pauses at the door — and his smile goes",
        "genuine for the first time, which is somehow worse.",
        "One more thing, brother. The trust clause is specific — the marriage",
        "must be registered by your birthday gala. Not engaged. Married.",
        "I've taken the liberty of holding a slot at the registrar. Consider",
        "it a gift."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the trap disclosed as kindness — the deadline and the pre-booked registrar slot, delivered with the first genuine smile",
      "participants": [
        "VICTOR",
        "DAMIEN"
      ],
      "remote_participants": [],
      "location": {
        "zone": "damien's office"
      },
      "timeline": [
        {
          "beat": "he gathers the tablet, pauses at the door — his smile goes genuine for the first time, which is somehow worse",
          "type": "held_reaction"
        },
        {
          "beat": "'One more thing, brother... Not engaged. Married... Consider it a gift.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the genuine smile is the scare — everything else Victor does is performed, this is not"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "the birthday-gala deadline is the clock S30 runs on — 'registered,' not engaged, is the operative word"
      ],
      "ambiguities": [],
      "must_appear": [
        "VICTOR",
        "DAMIEN"
      ],
      "tableau": true,
      "shot_sequence": [
        "s13.sh08"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s13.sh01",
      "size": "M three-shot",
      "zone": "damien's office",
      "type": "visual",
      "participants": [
        "VICTOR",
        "DAMIEN",
        "JIM"
      ],
      "implements": [
        "s13.e01"
      ],
      "covers_beats": {
        "s13.e01": [
          0,
          1
        ]
      },
      "purpose": "the dealer's spread — tablet fanned like cards, the shortlist announced",
      "audio_note": "tablet tap and swipe",
      "dialogue_lines": [
        {
          "event_id": "s13.e01",
          "speaker": "VICTOR",
          "line": "The shortlist. Pre-vetted, family-clean, board-approved, each one signed to a discretion agreement thicker than her résumé.",
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
      "shot_id": "s13.sh02",
      "size": "INS+M",
      "zone": "damien's office",
      "type": "visual",
      "participants": [
        "VICTOR",
        "DAMIEN"
      ],
      "depicts": [
        {
          "actors": [
            "SOPHIA"
          ],
          "channel": "tablet candidate profiles"
        }
      ],
      "implements": [
        "s13.e02"
      ],
      "covers_beats": {
        "s13.e02": [
          0,
          1
        ]
      },
      "purpose": "candidate one on screen — yacht-adjacent profile + 'old money, new problems' pitch",
      "audio_note": "tablet swipe",
      "dialogue_lines": [
        {
          "event_id": "s13.e02",
          "speaker": "VICTOR",
          "line": "Sophia Vane. Old money, new problems. Photographs like a dream, golfs, donates to everything that has a dinner.",
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
      "shot_id": "s13.sh03",
      "size": "M",
      "zone": "damien's office",
      "type": "visual",
      "participants": [
        "JIM",
        "VICTOR"
      ],
      "implements": [
        "s13.e02"
      ],
      "covers_beats": {
        "s13.e02": [
          2,
          3
        ]
      },
      "purpose": "Jim reading over Damien's shoulder — 'yachts, yacht litigation' → 'She's fun.'",
      "dialogue_lines": [
        {
          "event_id": "s13.e02",
          "speaker": "JIM",
          "line": "Hobbies: \"yachts, yacht litigation.\"",
          "line_kind": "on_camera",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s13.e02",
          "speaker": "VICTOR",
          "line": "She's fun.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "offscreen",
          "beats": [
            3
          ]
        }
      ]
    },
    {
      "shot_id": "s13.sh04",
      "size": "INS+M",
      "zone": "damien's office",
      "type": "visual",
      "participants": [
        "VICTOR",
        "DAMIEN"
      ],
      "depicts": [
        {
          "actors": [
            "OCTAVIA"
          ],
          "channel": "tablet candidate profiles"
        }
      ],
      "implements": [
        "s13.e03"
      ],
      "covers_beats": {
        "s13.e03": [
          0,
          1
        ]
      },
      "purpose": "candidate two on screen — notarized smile + the hedge-fund apology pitch",
      "audio_note": "tablet swipe",
      "dialogue_lines": [
        {
          "event_id": "s13.e03",
          "speaker": "VICTOR",
          "line": "Octavia Marlowe. Steel dynasty, third generation. She once talked a hedge fund into apologizing to her.",
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
      "shot_id": "s13.sh05",
      "size": "two-shot",
      "zone": "damien's office",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "VICTOR"
      ],
      "implements": [
        "s13.e03"
      ],
      "covers_beats": {
        "s13.e03": [
          2,
          3
        ]
      },
      "purpose": "'In a good way?' / 'There isn't a bad way to do that.' — menace admired",
      "dialogue_lines": [
        {
          "event_id": "s13.e03",
          "speaker": "DAMIEN",
          "line": "In a good way?",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s13.e03",
          "speaker": "VICTOR",
          "line": "There isn't a bad way to do that.",
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
      "shot_id": "s13.sh06",
      "size": "INS+M",
      "zone": "damien's office",
      "type": "visual",
      "participants": [
        "VICTOR",
        "DAMIEN"
      ],
      "depicts": [
        {
          "actors": [
            "ANNA"
          ],
          "channel": "tablet candidate profiles"
        }
      ],
      "implements": [
        "s13.e04"
      ],
      "covers_beats": {
        "s13.e04": [
          0,
          1
        ]
      },
      "purpose": "candidate three — the wildcard surgeon who wandered into the slide deck; 'handle with tongs'",
      "audio_note": "tablet swipe",
      "dialogue_lines": [
        {
          "event_id": "s13.e04",
          "speaker": "VICTOR",
          "line": "And Anna Reyes. Children's cardiac surgeon. Victor's note: wildcard — the board wanted a \"relatable\" option for optics. She's alarmingly sincere. Handle with tongs.",
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
      "shot_id": "s13.sh07",
      "size": "two-shot",
      "zone": "damien's office",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "VICTOR"
      ],
      "implements": [
        "s13.e05"
      ],
      "covers_beats": {
        "s13.e05": [
          0,
          1,
          2,
          3
        ]
      },
      "purpose": "the terms — eight weeks, two dates each, and a retreat weekend invented into existence",
      "dialogue_lines": [
        {
          "event_id": "s13.e05",
          "speaker": "DAMIEN",
          "line": "Three candidates, eight weeks.",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s13.e05",
          "speaker": "VICTOR",
          "line": "Two dates each. First impressions, then the compatibility retreat weekend —",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s13.e05",
          "speaker": "DAMIEN",
          "line": "There is no compatibility retreat weekend.",
          "line_kind": "on_camera",
          "recipient": "VICTOR",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s13.e05",
          "speaker": "VICTOR",
          "line": "There is now. I own the resort.",
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
      "shot_id": "s13.sh08",
      "size": "M",
      "zone": "damien's office",
      "type": "visual",
      "participants": [
        "VICTOR",
        "DAMIEN"
      ],
      "implements": [
        "s13.e06"
      ],
      "covers_beats": {
        "s13.e06": [
          0,
          1
        ]
      },
      "purpose": "the pause at the door — the genuine smile, then 'Not engaged. Married.' + the registrar slot 'gift'",
      "audio_note": "tablet gathered, door-frame quiet",
      "dialogue_lines": [
        {
          "event_id": "s13.e06",
          "speaker": "VICTOR",
          "line": "One more thing, brother. The trust clause is specific — the marriage must be registered by your birthday gala. Not engaged. Married. I've taken the liberty of holding a slot at the registrar. Consider it a gift.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    }
  ],
  "coverage": [
    {
      "span": "VICTOR spreads a tablet of candidate profiles like a card dealer.",
      "disposition": "covered_by",
      "by": [
        "s13.e01"
      ]
    },
    {
      "span": "The shortlist. Pre-vetted, family-clean, board-approved, each one signed to a discretion agreement thicker than her résumé.",
      "disposition": "covered_by",
      "by": [
        "s13.e01"
      ]
    },
    {
      "span": "On screen: SOPHIA VANE — stunning, socialite, yacht-adjacent.",
      "disposition": "covered_by",
      "by": [
        "s13.e02"
      ]
    },
    {
      "span": "Sophia Vane. Old money, new problems. Photographs like a dream,",
      "disposition": "covered_by",
      "by": [
        "s13.e02"
      ]
    },
    {
      "span": "Hobbies: \"yachts, yacht litigation.\"",
      "disposition": "covered_by",
      "by": [
        "s13.e02"
      ]
    },
    {
      "span": "She's fun.",
      "disposition": "covered_by",
      "by": [
        "s13.e02"
      ]
    },
    {
      "span": "Next: OCTAVIA MARLOWE — severe elegance, a smile that's been notarized.",
      "disposition": "covered_by",
      "by": [
        "s13.e03"
      ]
    },
    {
      "span": "She once talked a hedge fund into apologizing to her.",
      "disposition": "covered_by",
      "by": [
        "s13.e03"
      ]
    },
    {
      "span": "In a good way?",
      "disposition": "covered_by",
      "by": [
        "s13.e03"
      ]
    },
    {
      "span": "There isn't a bad way to do that.",
      "disposition": "covered_by",
      "by": [
        "s13.e03"
      ]
    },
    {
      "span": "Next: DR. ANNA REYES — warm, normal, a pediatric surgeon. She looks like she wandered into the slide deck by mistake.",
      "disposition": "covered_by",
      "by": [
        "s13.e04"
      ]
    },
    {
      "span": "Children's cardiac surgeon. Victor's note: wildcard —",
      "disposition": "covered_by",
      "by": [
        "s13.e04"
      ]
    },
    {
      "span": "Three candidates, eight weeks.",
      "disposition": "covered_by",
      "by": [
        "s13.e05"
      ]
    },
    {
      "span": "Two dates each. First impressions, then the compatibility retreat weekend —",
      "disposition": "covered_by",
      "by": [
        "s13.e05"
      ]
    },
    {
      "span": "There is no compatibility retreat weekend.",
      "disposition": "covered_by",
      "by": [
        "s13.e05"
      ]
    },
    {
      "span": "There is now. I own the resort.",
      "disposition": "covered_by",
      "by": [
        "s13.e05"
      ]
    },
    {
      "span": "He gathers the tablet, pauses at the door — and his smile goes genuine for the first time, which is somehow worse.",
      "disposition": "covered_by",
      "by": [
        "s13.e06"
      ]
    },
    {
      "span": "The trust clause is specific — the marriage must be registered by your birthday gala.",
      "disposition": "covered_by",
      "by": [
        "s13.e06"
      ]
    },
    {
      "span": "Consider it a gift.",
      "disposition": "covered_by",
      "by": [
        "s13.e06"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['VICTOR'] | -  | VICTOR spreads a tablet of candidate profiles like a card dealer.
i02 blk=['VICTOR', 'JIM'] | VICTOR The shortlist. Pre-vetted, family-clean, board-approved, eac | VICTOR faces JIM and speaks. On screen: SOPHIA VANE — stunning, socialite, yacht
i03 blk=['JIM'] | JIM Hobbies: "yachts, yacht litigation." | JIM faces VICTOR and speaks.
i04 blk=['VICTOR'] | VICTOR She's fun. Octavia Marlowe. Steel dynasty, third generation. | VICTOR faces JIM and speaks. Next: OCTAVIA MARLOWE — severe elegance, a smile th
i05 blk=['VICTOR', 'DAMIEN'] | DAMIEN In a good way? | DAMIEN faces VICTOR and speaks.
i06 blk=['VICTOR'] | VICTOR There isn't a bad way to do that. | VICTOR faces JIM and speaks.
i07 blk=['ANNA'] | -  | Next: DR. ANNA REYES — warm, normal, a pediatric surgeon. She looks like she wan
i08 blk=['VICTOR'] | VICTOR And Anna Reyes. Children's cardiac surgeon. Victor's note: w | VICTOR faces JIM and speaks.
i09 blk=['DAMIEN', 'VICTOR'] | DAMIEN Three candidates, eight weeks. | DAMIEN faces VICTOR and speaks.
i10 blk=['VICTOR', 'JIM'] | VICTOR Two dates each. First impressions, then the compatibility re | VICTOR faces JIM and speaks.
i11 blk=['DAMIEN'] | DAMIEN There is no compatibility retreat weekend. | DAMIEN faces VICTOR and speaks.
i12 blk=['VICTOR'] | VICTOR There is now. I own the resort. | VICTOR faces JIM and speaks.
i13 blk=['JIM'] | -  | He gathers the tablet, pauses at the door — and his smile goes genuine for the f
i14 blk=['JIM', 'VICTOR'] | VICTOR One more thing, brother. The trust clause is specific — the  | VICTOR faces JIM and speaks.