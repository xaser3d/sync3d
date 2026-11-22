# VALIDATION PACKET — scene s01
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 1 — INT. CROSS TOWER — BOARDROOM — DAY

*Glass, altitude, twelve people who earn more per hour than most houses.
Across the table: MR. OKAFOR, a raider with a famous poker face, and his
army of lawyers. DAMIEN CROSS sits at the head — 31, immaculate, a face
that was designed for quarterly reports and never finished for anything
else.*

OKAFOR
Our counteroffer stands, Mr. Cross. Sixty-one a share. Take the weekend
to— 

DAMIEN
Your counteroffer assumes I need this deal.

*He doesn't raise his voice. He never does.*

DAMIEN (CONT'D)
While you've been talking, my desk repriced your liquidity. You have
eleven days of operating cash. Twelve if you cancel the ribbon-cutting
in Rotterdam — please don't, the mayor already ordered the scissors.

*Okafor's poker face develops a small crack.*

DAMIEN (CONT'D)
The number on the screen isn't my offer anymore.

*On the wall screen, the figure quietly ticks down.*

DAMIEN (CONT'D)
It's your countdown.

*Silence. Okafor's lead lawyer leans in, whispers. Okafor nods once.
Hands extend. Signatures land. It took four minutes.*

*In the corridor, a PR ASSISTANT steps up with a photographer.*

PR ASSISTANT
Mr. Cross — the deal announcement needs a photo. Could you smile?

*Damien attempts to smile. His face performs an operation it has never
been trained for. Something happens around the mouth that technically
qualifies as an expression. The photographer lowers the camera slowly.*

PHOTOGRAPHER
We'll use the file photo.

DAMIEN
Which file photo?

PHOTOGRAPHER
The one from the charity thing. Where you were almost— it's a good
photo, sir.

*He flees. Damien watches him go, then turns to the window — forty
floors of his city, and not one person in it who would call him.*

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 1,
  "scene_heading": "INT. CROSS TOWER — BOARDROOM — DAY",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "Cold open. Damien Cross is established by what he does to a room: he wins a hostile negotiation in four minutes without raising his voice, then fails to produce a smile for a deal-announcement photo. The boardroom victory and the corridor defeat are one event-spine — competence at altitude, poverty at ground level. The final image (forty floors of his city, nobody who would call) is the thesis the rest of the film argues with.",
  "zones": [
    "boardroom",
    "corridor"
  ],
  "events": [
    {
      "event_id": "s01.e01",
      "source_evidence": [
        "Glass, altitude, twelve people who earn more per hour than most houses.",
        "Across the table: MR. OKAFOR, a raider with a famous poker face, and his army of lawyers.",
        "DAMIEN CROSS sits at the head — 31, immaculate, a face that was designed for quarterly reports and never finished for anything else.",
        "Our counteroffer stands, Mr. Cross. Sixty-one a share. Take the weekend to—",
        "Your counteroffer assumes I need this deal.",
        "He doesn't raise his voice. He never does."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the geometry of power stated in one exchange — Okafor offers a deadline, Damien declines the premise of needing anything",
      "participants": [
        "DAMIEN",
        "OKAFOR",
        "LAWYERS",
        "EXECUTIVES"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "location": {
        "zone": "boardroom"
      },
      "timeline": [
        {
          "beat": "glass, altitude, twelve people — the boardroom established with Damien at the head",
          "type": "atmosphere"
        },
        {
          "beat": "Okafor's counteroffer — sixty-one a share, take the weekend",
          "type": "dialogue"
        },
        {
          "beat": "Damien's refusal — 'your counteroffer assumes I need this deal'; he doesn't raise his voice, he never does",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the power geometry is the shot: Damien alone at the head, Okafor's army massed across",
        "no raised voice anywhere — the stillness is the threat"
      ],
      "audio_requirements": [
        "boardroom hush — the quiet of very expensive people listening"
      ],
      "continuity_constraints": [
        "Damien's flat vocal register here is the baseline every later scene measures warmth against"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "OKAFOR"
      ],
      "tableau": true,
      "shot_sequence": [
        "s01.sh01",
        "s01.sh02",
        "s01.sh03",
        "s01.snd01"
      ]
    },
    {
      "event_id": "s01.e02",
      "source_evidence": [
        "While you've been talking, my desk repriced your liquidity. You have eleven days of operating cash. Twelve if you cancel the ribbon-cutting in Rotterdam — please don't, the mayor already ordered the scissors.",
        "Okafor's poker face develops a small crack."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the kill shot delivered as courtesy — Damien reveals he has already moved while Okafor was still talking",
      "participants": [
        "DAMIEN",
        "OKAFOR",
        "LAWYERS",
        "EXECUTIVES"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "EXECUTIVES"
      ],
      "location": {
        "zone": "boardroom"
      },
      "timeline": [
        {
          "beat": "the liquidity speech — eleven days of operating cash, the Rotterdam scissors",
          "type": "dialogue"
        },
        {
          "beat": "the famous poker face develops a small crack",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "the comedy is the mismatch — maximum violence of information, minimum violence of delivery",
        "the crack in Okafor's face is small; do not oversell it"
      ],
      "audio_requirements": [],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "OKAFOR"
      ],
      "tableau": false,
      "shot_sequence": [
        "s01.sh04",
        "s01.sh05"
      ]
    },
    {
      "event_id": "s01.e03",
      "source_evidence": [
        "The number on the screen isn't my offer anymore.",
        "On the wall screen, the figure quietly ticks down.",
        "It's your countdown."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the deal figure reframed as a countdown — Damien converts Okafor's own clock into the weapon",
      "participants": [
        "DAMIEN",
        "OKAFOR",
        "LAWYERS",
        "EXECUTIVES"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "LAWYERS",
        "EXECUTIVES"
      ],
      "location": {
        "zone": "boardroom"
      },
      "timeline": [
        {
          "beat": "'the number on the screen isn't my offer anymore'",
          "type": "dialogue"
        },
        {
          "beat": "the wall-screen figure quietly ticks down",
          "type": "insert"
        },
        {
          "beat": "'It's your countdown.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the ticking figure carries the beat — the audience must see the number move before the line names it"
      ],
      "audio_requirements": [
        "the soft tick of the falling figure — almost subliminal"
      ],
      "continuity_constraints": [
        "the figure on the wall screen is the same number Okafor offered — the countdown is HIS price decaying"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s01.sh06",
        "s01.sh07",
        "s01.sh08",
        "s01.snd01"
      ]
    },
    {
      "event_id": "s01.e04",
      "source_evidence": [
        "Silence. Okafor's lead lawyer leans in, whispers. Okafor nods once. Hands extend. Signatures land. It took four minutes."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "capitulation rendered as procedure — a whisper, a nod, signatures; the takeover completes in four minutes",
      "participants": [
        "DAMIEN",
        "OKAFOR",
        "LAWYERS",
        "EXECUTIVES"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "EXECUTIVES"
      ],
      "location": {
        "zone": "boardroom"
      },
      "timeline": [
        {
          "beat": "silence — the room decides",
          "type": "held_reaction"
        },
        {
          "beat": "the lead lawyer leans in and whispers; Okafor nods once",
          "type": "action"
        },
        {
          "beat": "hands extend, signatures land — it took four minutes",
          "type": "action"
        }
      ],
      "visual_requirements": [
        "the whisper is performed, not heard — we see the lean-in, not the words",
        "'It took four minutes' is elapsed-time information, not a visible clock — the montage pace carries it"
      ],
      "audio_requirements": [
        "pen scratches on signatures inside the held silence"
      ],
      "continuity_constraints": [
        "'four minutes' is the same span Victor later quotes in S3 — the number is characterization, keep it exact"
      ],
      "ambiguities": [],
      "must_appear": [
        "OKAFOR"
      ],
      "tableau": false,
      "shot_sequence": [
        "s01.sh09",
        "s01.sh10",
        "s01.snd01"
      ]
    },
    {
      "event_id": "s01.e05",
      "source_evidence": [
        "In the corridor, a PR ASSISTANT steps up with a photographer.",
        "Mr. Cross — the deal announcement needs a photo. Could you smile?",
        "Damien attempts to smile. His face performs an operation it has never been trained for. Something happens around the mouth that technically qualifies as an expression. The photographer lowers the camera slowly.",
        "We'll use the file photo."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the man who can do anything cannot smile on request — competence fails at the exact moment it stops mattering commercially",
      "participants": [
        "DAMIEN",
        "PR ASSISTANT",
        "PHOTOGRAPHER"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "location": {
        "zone": "corridor"
      },
      "timeline": [
        {
          "beat": "the corridor — the PR assistant steps up with a photographer",
          "type": "action"
        },
        {
          "beat": "'the deal announcement needs a photo — could you smile?'",
          "type": "dialogue"
        },
        {
          "beat": "Damien attempts to smile — an operation his face was never trained for",
          "type": "action"
        },
        {
          "beat": "the photographer lowers the camera slowly",
          "type": "reaction"
        },
        {
          "beat": "'We'll use the file photo.'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the smile attempt must be readable as sincere effort producing something technically-an-expression — comedy through failure, not mugging",
        "the camera lowers instead of firing — no shutter sound is the joke"
      ],
      "audio_requirements": [
        "the camera lowered slowly — no shutter ever fires"
      ],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "PHOTOGRAPHER",
        "PR ASSISTANT"
      ],
      "tableau": true,
      "shot_sequence": [
        "s01.sh11",
        "s01.sh12",
        "s01.sh13",
        "s01.snd01"
      ]
    },
    {
      "event_id": "s01.e06",
      "source_evidence": [
        "Which file photo?",
        "The one from the charity thing. Where you were almost— it's a good photo, sir.",
        "He flees. Damien watches him go, then turns to the window — forty floors of his city, and not one person in it who would call him."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the retreat and the reveal — the photographer escapes mid-sentence and the film states its thesis: forty floors of his city, nobody who would call",
      "participants": [
        "DAMIEN",
        "PHOTOGRAPHER",
        "PR ASSISTANT"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "PR ASSISTANT"
      ],
      "location": {
        "zone": "corridor"
      },
      "timeline": [
        {
          "beat": "'Which file photo?'",
          "type": "dialogue"
        },
        {
          "beat": "'the charity thing — where you were almost—'",
          "type": "dialogue"
        },
        {
          "beat": "he flees; Damien watches him go",
          "type": "action"
        },
        {
          "beat": "the window — forty floors of his city, not one person who would call",
          "type": "held_image"
        }
      ],
      "visual_requirements": [
        "the photographer's exit is a flight, not a walk-off",
        "the window frame holds — the city is vast and entirely without a name Damien could dial"
      ],
      "audio_requirements": [
        "the corridor empties — city hum through forty floors of glass"
      ],
      "continuity_constraints": [
        "the charity-thing photo is the file the world sees — the 'almost' smile becomes the public face"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s01.sh14",
        "s01.sh15",
        "s01.sh16",
        "s01.snd01"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s01.sh01",
      "size": "W",
      "zone": "boardroom",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "OKAFOR",
        "LAWYERS",
        "EXECUTIVES"
      ],
      "implements": [
        "s01.e01"
      ],
      "covers_beats": {
        "s01.e01": [
          0
        ]
      },
      "purpose": "the boardroom established — glass, altitude, twelve people, Damien alone at the head",
      "audio_note": "boardroom hush"
    },
    {
      "shot_id": "s01.sh02",
      "size": "CU",
      "zone": "boardroom",
      "type": "visual",
      "participants": [
        "OKAFOR"
      ],
      "implements": [
        "s01.e01"
      ],
      "covers_beats": {
        "s01.e01": [
          1
        ]
      },
      "purpose": "Okafor's counteroffer — sixty-one a share, the poker face delivering its rehearsed deadline",
      "dialogue_lines": [
        {
          "event_id": "s01.e01",
          "speaker": "OKAFOR",
          "line": "Our counteroffer stands, Mr. Cross. Sixty-one a share. Take the weekend to—",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "offscreen",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s01.sh03",
      "size": "CU",
      "zone": "boardroom",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s01.e01"
      ],
      "covers_beats": {
        "s01.e01": [
          2
        ]
      },
      "purpose": "Damien's refusal — level voice, 'he never does' read in the flatness",
      "audio_note": "boardroom hush under level voice",
      "dialogue_lines": [
        {
          "event_id": "s01.e01",
          "speaker": "DAMIEN",
          "line": "Your counteroffer assumes I need this deal.",
          "line_kind": "on_camera",
          "recipient": "OKAFOR",
          "recipient_presence": "offscreen",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s01.sh04",
      "size": "M",
      "zone": "boardroom",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s01.e02"
      ],
      "covers_beats": {
        "s01.e02": [
          0
        ]
      },
      "purpose": "the liquidity speech — eleven days of cash, the Rotterdam scissors as a courtesy",
      "dialogue_lines": [
        {
          "event_id": "s01.e02",
          "speaker": "DAMIEN",
          "line": "While you've been talking, my desk repriced your liquidity. You have eleven days of operating cash. Twelve if you cancel the ribbon-cutting in Rotterdam — please don't, the mayor already ordered the scissors.",
          "line_kind": "on_camera",
          "recipient": "OKAFOR",
          "recipient_presence": "offscreen",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s01.sh05",
      "size": "CU",
      "zone": "boardroom",
      "type": "visual",
      "participants": [
        "OKAFOR",
        "LAWYERS"
      ],
      "implements": [
        "s01.e02"
      ],
      "covers_beats": {
        "s01.e02": [
          1
        ]
      },
      "purpose": "the poker face develops a small crack — lawyers frozen at his shoulder",
      "audio_note": "held room silence"
    },
    {
      "shot_id": "s01.sh06",
      "size": "M",
      "zone": "boardroom",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s01.e03"
      ],
      "covers_beats": {
        "s01.e03": [
          0
        ]
      },
      "purpose": "'the number on the screen isn't my offer anymore' — delivered without emphasis",
      "dialogue_lines": [
        {
          "event_id": "s01.e03",
          "speaker": "DAMIEN",
          "line": "The number on the screen isn't my offer anymore.",
          "line_kind": "on_camera",
          "recipient": "OKAFOR",
          "recipient_presence": "offscreen",
          "beats": [
            0
          ]
        }
      ]
    },
    {
      "shot_id": "s01.sh07",
      "size": "INS",
      "zone": "boardroom",
      "type": "visual",
      "participants": [],
      "depicts": [
        {
          "object": "wall-screen deal figure ticking down",
          "channel": "in-frame screen"
        }
      ],
      "implements": [
        "s01.e03"
      ],
      "covers_beats": {
        "s01.e03": [
          1
        ]
      },
      "purpose": "the figure quietly ticks down — the number visibly decaying",
      "audio_note": "the soft tick of the falling figure"
    },
    {
      "shot_id": "s01.sh08",
      "size": "two-shot",
      "zone": "boardroom",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "OKAFOR"
      ],
      "implements": [
        "s01.e03"
      ],
      "covers_beats": {
        "s01.e03": [
          2
        ]
      },
      "purpose": "'It's your countdown.' — the line lands across the table on Okafor's face",
      "dialogue_lines": [
        {
          "event_id": "s01.e03",
          "speaker": "DAMIEN",
          "line": "It's your countdown.",
          "line_kind": "on_camera",
          "recipient": "OKAFOR",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        }
      ]
    },
    {
      "shot_id": "s01.sh09",
      "size": "M",
      "zone": "boardroom",
      "type": "visual",
      "participants": [
        "OKAFOR",
        "LAWYERS"
      ],
      "implements": [
        "s01.e04"
      ],
      "covers_beats": {
        "s01.e04": [
          0,
          1
        ]
      },
      "purpose": "the silence, then the lean-in whisper and the single nod — capitulation as procedure",
      "audio_note": "held silence, murmured whisper under"
    },
    {
      "shot_id": "s01.sh10",
      "size": "INS",
      "zone": "boardroom",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "OKAFOR",
        "LAWYERS"
      ],
      "implements": [
        "s01.e04"
      ],
      "covers_beats": {
        "s01.e04": [
          2
        ]
      },
      "purpose": "hands extend, signatures land — four minutes of paperwork ending a company",
      "audio_note": "pen scratches on signatures inside the held silence"
    },
    {
      "shot_id": "s01.sh11",
      "size": "M",
      "zone": "corridor",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "PR ASSISTANT",
        "PHOTOGRAPHER"
      ],
      "implements": [
        "s01.e05"
      ],
      "covers_beats": {
        "s01.e05": [
          0,
          1
        ]
      },
      "purpose": "the corridor — the PR assistant steps up with the photographer, the request delivered",
      "dialogue_lines": [
        {
          "event_id": "s01.e05",
          "speaker": "PR ASSISTANT",
          "line": "Mr. Cross — the deal announcement needs a photo. Could you smile?",
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
      "shot_id": "s01.sh12",
      "size": "CU",
      "zone": "corridor",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "PHOTOGRAPHER"
      ],
      "implements": [
        "s01.e05"
      ],
      "covers_beats": {
        "s01.e05": [
          2,
          3
        ]
      },
      "purpose": "the smile attempt — an untrained operation around the mouth; the camera lowers slowly instead of firing",
      "audio_note": "no shutter — the camera lowered slowly"
    },
    {
      "shot_id": "s01.sh13",
      "size": "CU",
      "zone": "corridor",
      "type": "visual",
      "participants": [
        "PHOTOGRAPHER"
      ],
      "implements": [
        "s01.e05"
      ],
      "covers_beats": {
        "s01.e05": [
          4
        ]
      },
      "purpose": "the professional verdict — 'we'll use the file photo'",
      "dialogue_lines": [
        {
          "event_id": "s01.e05",
          "speaker": "PHOTOGRAPHER",
          "line": "We'll use the file photo.",
          "line_kind": "on_camera",
          "recipient": "DAMIEN",
          "recipient_presence": "offscreen",
          "beats": [
            4
          ]
        }
      ]
    },
    {
      "shot_id": "s01.sh14",
      "size": "M",
      "zone": "corridor",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "PHOTOGRAPHER"
      ],
      "implements": [
        "s01.e06"
      ],
      "covers_beats": {
        "s01.e06": [
          0,
          1
        ]
      },
      "purpose": "'which file photo?' — the photographer backpedaling through 'the charity thing' explanation",
      "dialogue_lines": [
        {
          "event_id": "s01.e06",
          "speaker": "DAMIEN",
          "line": "Which file photo?",
          "line_kind": "on_camera",
          "recipient": "PHOTOGRAPHER",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s01.e06",
          "speaker": "PHOTOGRAPHER",
          "line": "The one from the charity thing. Where you were almost— it's a good photo, sir.",
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
      "shot_id": "s01.sh15",
      "size": "M",
      "zone": "corridor",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "PHOTOGRAPHER"
      ],
      "implements": [
        "s01.e06"
      ],
      "covers_beats": {
        "s01.e06": [
          2
        ]
      },
      "purpose": "he flees — the photographer exits frame at speed while Damien watches",
      "audio_note": "retreating footsteps"
    },
    {
      "shot_id": "s01.sh16",
      "size": "W held",
      "zone": "corridor",
      "type": "visual",
      "participants": [
        "DAMIEN"
      ],
      "implements": [
        "s01.e06"
      ],
      "covers_beats": {
        "s01.e06": [
          3
        ]
      },
      "purpose": "the window — forty floors of his city and not one person in it who would call",
      "audio_note": "corridor empties, city hum through glass"
    },
    {
      "shot_id": "s01.snd01",
      "type": "sound",
      "implements": [
        "s01.e01",
        "s01.e03",
        "s01.e04",
        "s01.e05",
        "s01.e06"
      ],
      "purpose": "sound card: boardroom hush, the figure's soft tick, pen scratches in silence, a shutter that never fires, city hum through the glass",
      "audio_note": "boardroom hush; soft tick of the falling figure; pen scratches on signatures inside held silence; camera lowered, no shutter; corridor empties to city hum through glass",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "Glass, altitude, twelve people who earn more per hour than most houses.",
      "disposition": "covered_by",
      "by": [
        "s01.e01"
      ]
    },
    {
      "span": "Across the table: MR. OKAFOR, a raider with a famous poker face, and his army of lawyers.",
      "disposition": "covered_by",
      "by": [
        "s01.e01"
      ]
    },
    {
      "span": "DAMIEN CROSS sits at the head — 31, immaculate, a face that was designed for quarterly reports and never finished for anything else.",
      "disposition": "covered_by",
      "by": [
        "s01.e01"
      ]
    },
    {
      "span": "Our counteroffer stands, Mr. Cross. Sixty-one a share. Take the weekend to—",
      "disposition": "covered_by",
      "by": [
        "s01.e01"
      ]
    },
    {
      "span": "Your counteroffer assumes I need this deal.",
      "disposition": "covered_by",
      "by": [
        "s01.e01"
      ]
    },
    {
      "span": "He doesn't raise his voice. He never does.",
      "disposition": "covered_by",
      "by": [
        "s01.e01"
      ]
    },
    {
      "span": "While you've been talking, my desk repriced your liquidity. You have eleven days of operating cash. Twelve if you cancel the ribbon-cutting in Rotterdam — please don't, the mayor already ordered the scissors.",
      "disposition": "covered_by",
      "by": [
        "s01.e02"
      ]
    },
    {
      "span": "Okafor's poker face develops a small crack.",
      "disposition": "covered_by",
      "by": [
        "s01.e02"
      ]
    },
    {
      "span": "The number on the screen isn't my offer anymore.",
      "disposition": "covered_by",
      "by": [
        "s01.e03"
      ]
    },
    {
      "span": "On the wall screen, the figure quietly ticks down.",
      "disposition": "covered_by",
      "by": [
        "s01.e03"
      ]
    },
    {
      "span": "It's your countdown.",
      "disposition": "covered_by",
      "by": [
        "s01.e03"
      ]
    },
    {
      "span": "Silence. Okafor's lead lawyer leans in, whispers. Okafor nods once. Hands extend. Signatures land. It took four minutes.",
      "disposition": "covered_by",
      "by": [
        "s01.e04"
      ]
    },
    {
      "span": "In the corridor, a PR ASSISTANT steps up with a photographer.",
      "disposition": "covered_by",
      "by": [
        "s01.e05"
      ]
    },
    {
      "span": "Mr. Cross — the deal announcement needs a photo. Could you smile?",
      "disposition": "covered_by",
      "by": [
        "s01.e05"
      ]
    },
    {
      "span": "Damien attempts to smile. His face performs an operation it has never been trained for. Something happens around the mouth that technically qualifies as an expression. The photographer lowers the camera slowly.",
      "disposition": "covered_by",
      "by": [
        "s01.e05"
      ]
    },
    {
      "span": "We'll use the file photo.",
      "disposition": "covered_by",
      "by": [
        "s01.e05"
      ]
    },
    {
      "span": "Which file photo?",
      "disposition": "covered_by",
      "by": [
        "s01.e06"
      ]
    },
    {
      "span": "The one from the charity thing. Where you were almost— it's a good photo, sir.",
      "disposition": "covered_by",
      "by": [
        "s01.e06"
      ]
    },
    {
      "span": "He flees. Damien watches him go, then turns to the window — forty floors of his city, and not one person in it who would call him.",
      "disposition": "covered_by",
      "by": [
        "s01.e06"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['DAMIEN', 'OKAFOR'] | -  | Glass, altitude, twelve people who earn more per hour than most houses. Across t
i02 blk=['OKAFOR', 'DAMIEN'] | OKAFOR Our counteroffer stands, Mr. Cross. Sixty-one a share. Take  | OKAFOR faces DAMIEN and speaks.
i03 blk=['DAMIEN'] | DAMIEN Your counteroffer assumes I need this deal. While you've bee | DAMIEN faces OKAFOR and speaks. He doesn't raise his voice. He never does.
i04 blk=['OKAFOR'] | -  | Okafor's poker face develops a small crack.
i05 blk=['DAMIEN'] | DAMIEN The number on the screen isn't my offer anymore. | DAMIEN faces OKAFOR and speaks.
i06 blk=[] | -  | On the wall screen, the figure quietly ticks down.
i07 blk=['OKAFOR', 'DAMIEN'] | DAMIEN It's your countdown. | DAMIEN faces OKAFOR and speaks.
i08 blk=['OKAFOR'] | -  | Silence. Okafor's lead lawyer leans in, whispers. Okafor nods once. Hands extend
i09 blk=['PR ASSISTANT'] | PR ASSISTANT Mr. Cross — the deal announcement needs a photo. Could you s | In the corridor, a PR ASSISTANT steps up with a photographer.
i10 blk=['DAMIEN', 'PHOTOGRAPHER'] | -  | Damien attempts to smile. His face performs an operation it has never been train
i11 blk=['PHOTOGRAPHER'] | PHOTOGRAPHER We'll use the file photo. | PHOTOGRAPHER faces OKAFOR and speaks.
i12 blk=['DAMIEN', 'PHOTOGRAPHER'] | DAMIEN Which file photo? | DAMIEN faces OKAFOR and speaks.
i13 blk=['PHOTOGRAPHER'] | PHOTOGRAPHER The one from the charity thing. Where you were almost— it's  | PHOTOGRAPHER faces OKAFOR and speaks.
i14 blk=['DAMIEN'] | -  | He flees. Damien watches him go, then turns to the window — forty floors of his 