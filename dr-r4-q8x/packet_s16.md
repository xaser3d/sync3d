# VALIDATION PACKET — scene s16
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 16 — INT. NEIGHBORHOOD BISTRO — NIGHT (DATE THREE)

*DR. ANNA REYES — normal clothes, tired eyes, warm laugh, no angle.
The bistro is small and loud and she clearly chose it herself.*

ANNA
—so the kid looks at the X-ray of his own heart and says "it looks
like a ghost." And honestly? He's not wrong. Pediatric cardiology
is basically ghost management.

*Damien laughs. Actually laughs — the sound surprises him as much
as her. At the lab, MAYA watches the feed, jaw tightening.*

MAYA (V.O.)
He's laughing. Nobody laughs on date three. It's in the manual.
Ask about the fellowship.

DAMIEN
The fellowship in Minneapolis — Anna, that's a thousand miles—

ANNA
It funds itself if I write the grant well enough. You'd be amazed
what you get when you stop asking committees and start asking the
person who lost someone. Speaking of — you lost your dad young,
right? The trust thing is public, sorry, I did read the dossier.

*Damien goes still. At the lab, Maya leans toward the mic — and
stops. This isn't a line she can feed him.*

DAMIEN
(slowly)
I was twenty-three. He died on a Tuesday, between meetings. I gave
the eulogy in the tone of an earnings call.

ANNA
(quiet)
And nobody corrected you.

DAMIEN
How did you know that?

ANNA
Because people like us — people who take care of things — we get
graded on the tone, not the content. I'm sorry, Damien. That's a
terrible way to lose someone.

*The feed keeps running. At the lab, Maya's hand rests on the mute
switch. She doesn't press it. She watches Damien — actually talking,
unguarded for the first time all film — with another woman.*

J-7
You are grinding your teeth. Shall I log it as a software conflict?

MAYA
Log it as a bad candidate fit.

J-7
She has a 96% compatibility index with your own profile, Maya.

MAYA
Log it anyway.

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 16,
  "scene_heading": "INT. NEIGHBORHOOD BISTRO — NIGHT (DATE THREE)",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "Date three, cross-cut between the bistro and the lab where Maya monitors the date on a feed. Anna is not a mark or a rival to beat — she is a person who reads Damien accurately inside an hour. Maya coaches through the earpiece until the date stops being coachable, then keeps watching with her hand on a mute switch she will not press. The film's triangle is quietly declared here.",
  "zones": [
    "neighborhood bistro",
    "lab"
  ],
  "events": [
    {
      "event_id": "s16.e01",
      "source_evidence": [
        "DR. ANNA REYES — normal clothes, tired eyes, warm laugh, no angle. The bistro is small and loud and she clearly chose it herself.",
        "—so the kid looks at the X-ray of his own heart and says \"it looks like a ghost.\" And honestly? He's not wrong. Pediatric cardiology is basically ghost management.",
        "Damien laughs. Actually laughs — the sound surprises him as much as her."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the date works on its own terms before we know it's surveilled — Anna's register and his unguarded laugh establish what the lab will be watching",
      "participants": [
        "DAMIEN",
        "ANNA"
      ],
      "remote_participants": [
        {
          "actor": "MAYA",
          "channel": "date feed",
          "direction": "lab → bistro, observing"
        }
      ],
      "location": {
        "zone": "neighborhood bistro"
      },
      "timeline": [
        {
          "beat": "Anna's ghost-management story — the register of the whole date",
          "type": "dialogue"
        },
        {
          "beat": "Damien laughs — actually laughs; the sound surprises him as much as her",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "the bistro is small and loud — warmth and crowd as a deliberate contrast to the lab's surveillance quiet",
        "the laugh must read as involuntary — a sound he didn't schedule"
      ],
      "audio_requirements": [
        "small loud bistro walla under the date — she chose a room with no silence in it"
      ],
      "continuity_constraints": [
        "Anna is introduced as ANNA REYES — normal clothes, no angle; she is not playing anything"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "ANNA"
      ],
      "tableau": true,
      "shot_sequence": [
        "s16.sh01"
      ]
    },
    {
      "event_id": "s16.e02",
      "source_evidence": [
        "At the lab, MAYA watches the feed, jaw tightening."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the watcher revealed — the laugh registers somewhere else as data and as something else",
      "participants": [
        "MAYA"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "DAMIEN",
            "ANNA"
          ],
          "seen_by": [
            "MAYA"
          ],
          "channel": "date feed",
          "from_zone": "neighborhood bistro"
        }
      ],
      "location": {
        "zone": "lab"
      },
      "timeline": [
        {
          "beat": "Maya watches the feed, jaw tightening",
          "type": "held_reaction"
        }
      ],
      "visual_requirements": [
        "the feed is a screen inside the frame — Damien and Anna are depicted, not present",
        "jaw tightening is the whole performance — no larger reaction is earned yet"
      ],
      "audio_requirements": [
        "lab quiet under the faint feed audio"
      ],
      "continuity_constraints": [
        "Maya's presence in the scene is lab-side only — she never physically enters the bistro"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s16.sh02"
      ]
    },
    {
      "event_id": "s16.e03",
      "source_evidence": [
        "He's laughing. Nobody laughs on date three. It's in the manual. Ask about the fellowship.",
        "The fellowship in Minneapolis — Anna, that's a thousand miles—"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the coaching loop exposed — her voice in his ear turns the date into a rehearsed module, and he immediately makes the fed question his own",
      "participants": [
        "DAMIEN",
        "ANNA"
      ],
      "remote_participants": [
        {
          "actor": "MAYA",
          "channel": "earpiece",
          "direction": "lab → DAMIEN, coaching"
        }
      ],
      "location": {
        "zone": "neighborhood bistro"
      },
      "timeline": [
        {
          "beat": "Maya's V.O. lands in his earpiece — 'it's in the manual'",
          "type": "dialogue_remote"
        },
        {
          "beat": "Damien asks about the fellowship — the fed line made his own",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "hold on Damien receiving the earpiece — the audience should catch the half-beat where the coaching becomes his question"
      ],
      "audio_requirements": [
        "her V.O. in his earpiece stays private — Anna never hears it"
      ],
      "continuity_constraints": [
        "the earpiece channel is established infrastructure — the same link Maya uses on her evening shifts"
      ],
      "ambiguities": [
        "how much of Maya's V.O. the audience hears as literal earpiece audio vs. over the lab feed — flag for director; either is defensible"
      ],
      "must_appear": [
        "DAMIEN"
      ],
      "tableau": false,
      "shot_sequence": [
        "s16.sh03"
      ]
    },
    {
      "event_id": "s16.e04",
      "source_evidence": [
        "It funds itself if I write the grant well enough. You'd be amazed what you get when you stop asking committees and start asking the person who lost someone. Speaking of — you lost your dad young, right? The trust thing is public, sorry, I did read the dossier.",
        "Damien goes still."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "Anna does the thing no module can coach around — she names his grief as public information and her own move as homework, and the date leaves the script",
      "participants": [
        "DAMIEN",
        "ANNA"
      ],
      "remote_participants": [
        {
          "actor": "MAYA",
          "channel": "date feed",
          "direction": "lab → bistro, observing"
        }
      ],
      "location": {
        "zone": "neighborhood bistro"
      },
      "timeline": [
        {
          "beat": "the dossier reveal — 'you lost your dad young, right?'",
          "type": "dialogue"
        },
        {
          "beat": "Damien goes still",
          "type": "reaction"
        }
      ],
      "visual_requirements": [
        "the stillness is the event — he is being read, not fed, and the face must show the difference"
      ],
      "audio_requirements": [],
      "continuity_constraints": [
        "'the dossier' is Anna's admission — she researched him openly; no surveillance equivalence to Maya's feed"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "ANNA"
      ],
      "tableau": true,
      "shot_sequence": [
        "s16.sh04"
      ]
    },
    {
      "event_id": "s16.e05",
      "source_evidence": [
        "At the lab, Maya leans toward the mic — and stops. This isn't a line she can feed him."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the coach reaches the edge of coaching — she starts to intervene and recognizes this belongs to him",
      "participants": [
        "MAYA"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "DAMIEN",
            "ANNA"
          ],
          "seen_by": [
            "MAYA"
          ],
          "channel": "date feed",
          "from_zone": "neighborhood bistro"
        }
      ],
      "location": {
        "zone": "lab"
      },
      "timeline": [
        {
          "beat": "Maya leans toward the mic — the reflex to feed",
          "type": "action"
        },
        {
          "beat": "she stops — this isn't a line she can feed him",
          "type": "held_action"
        }
      ],
      "visual_requirements": [
        "the lean and the arrest are one physical event — the decision happens in the body before it happens anywhere else"
      ],
      "audio_requirements": [
        "lab quiet; the mic is close enough to hear her not use it"
      ],
      "continuity_constraints": [],
      "ambiguities": [],
      "must_appear": [
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s16.sh05"
      ]
    },
    {
      "event_id": "s16.e06",
      "source_evidence": [
        "I was twenty-three. He died on a Tuesday, between meetings. I gave the eulogy in the tone of an earnings call.",
        "And nobody corrected you.",
        "How did you know that?",
        "Because people like us — people who take care of things — we get graded on the tone, not the content. I'm sorry, Damien. That's a terrible way to lose someone."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the confession neither of them was coached for — he tells the eulogy truth and she answers it from inside the same damage; 'graded on the tone, not the content' is the scene's thesis",
      "participants": [
        "DAMIEN",
        "ANNA"
      ],
      "remote_participants": [
        {
          "actor": "MAYA",
          "channel": "date feed",
          "direction": "lab → bistro, observing — silent"
        }
      ],
      "location": {
        "zone": "neighborhood bistro"
      },
      "timeline": [
        {
          "beat": "'I was twenty-three... the tone of an earnings call' — slowly, unprompted",
          "type": "dialogue"
        },
        {
          "beat": "'And nobody corrected you.' — quiet",
          "type": "dialogue"
        },
        {
          "beat": "'How did you know that?'",
          "type": "dialogue"
        },
        {
          "beat": "'people like us — graded on the tone, not the content'",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the exchange plays in two-shot and over-shoulder only — no insert, no cutaway; the intimacy is in coverage restraint",
        "'unguarded for the first time all film' must be visible in his body, not stated"
      ],
      "audio_requirements": [
        "the loud room falls away under the confession — bistro walla drops to almost nothing"
      ],
      "continuity_constraints": [
        "the eulogy detail is the load-bearing fact — it will resurface on the terrace (S21) as the thing Maya should not know"
      ],
      "ambiguities": [],
      "must_appear": [
        "DAMIEN",
        "ANNA"
      ],
      "tableau": true,
      "shot_sequence": [
        "s16.sh06",
        "s16.sh07",
        "s16.snd01"
      ]
    },
    {
      "event_id": "s16.e07",
      "source_evidence": [
        "The feed keeps running. At the lab, Maya's hand rests on the mute switch. She doesn't press it. She watches Damien — actually talking, unguarded for the first time all film — with another woman."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the withheld mute — she could silence what is hurting her and chooses not to; watching him be real with another woman is the wound she logs",
      "participants": [
        "MAYA"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "DAMIEN",
            "ANNA"
          ],
          "seen_by": [
            "MAYA"
          ],
          "channel": "date feed",
          "from_zone": "neighborhood bistro"
        }
      ],
      "location": {
        "zone": "lab"
      },
      "timeline": [
        {
          "beat": "her hand rests on the mute switch",
          "type": "held_action"
        },
        {
          "beat": "she doesn't press it",
          "type": "held_action"
        },
        {
          "beat": "she watches him — unguarded for the first time all film — with another woman",
          "type": "held_reaction"
        }
      ],
      "visual_requirements": [
        "the mute switch is the shot — hand resting, never pressing; the restraint is the declaration",
        "the feed keeps running — the picture must stay alive inside her frame"
      ],
      "audio_requirements": [
        "the withheld mute — the feed keeps running under her hand; silence she refuses to take"
      ],
      "continuity_constraints": [
        "'first time all film' is narrator information — rendered as how long the shot holds, not as a caption"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s16.sh08",
        "s16.snd01"
      ]
    },
    {
      "event_id": "s16.e08",
      "source_evidence": [
        "You are grinding your teeth. Shall I log it as a software conflict?",
        "Log it as a bad candidate fit.",
        "She has a 96% compatibility index with your own profile, Maya.",
        "Log it anyway."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "J-7 names what the mute switch was hiding — the 96% compatibility index turns her denial into arithmetic, and 'Log it anyway' is her first honest order",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "remote_participants": [],
      "depicts_via_channel": [
        {
          "actors": [
            "DAMIEN",
            "ANNA"
          ],
          "seen_by": [
            "MAYA",
            "J-7"
          ],
          "channel": "date feed",
          "from_zone": "neighborhood bistro"
        }
      ],
      "location": {
        "zone": "lab"
      },
      "timeline": [
        {
          "beat": "J-7 observes the grinding — 'shall I log it as a software conflict?'",
          "type": "dialogue"
        },
        {
          "beat": "'Log it as a bad candidate fit.' — the deflection",
          "type": "dialogue"
        },
        {
          "beat": "the 96% compatibility index — J-7 prices the denial",
          "type": "dialogue"
        },
        {
          "beat": "'Log it anyway.' — the first honest order",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "the comedy and the ache live in stillness — two watchers at a feed, no movement the scene doesn't need",
        "the 96% lands on her face, not on a display"
      ],
      "audio_requirements": [
        "feed murmur continuing under the exchange — the date is still running"
      ],
      "continuity_constraints": [
        "J-7 says her name — 'Maya', not a unit designation; the intimacy of the lab is different from the penthouse"
      ],
      "ambiguities": [],
      "must_appear": [
        "MAYA",
        "J-7"
      ],
      "tableau": true,
      "shot_sequence": [
        "s16.sh09"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s16.sh01",
      "size": "two-shot",
      "zone": "neighborhood bistro",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "ANNA"
      ],
      "implements": [
        "s16.e01"
      ],
      "covers_beats": {
        "s16.e01": [
          0,
          1
        ]
      },
      "purpose": "the ghost-management story and the laugh that surprises him — the date working on its own terms",
      "audio_note": "loud bistro walla, glasses, close chatter",
      "dialogue_lines": [
        {
          "event_id": "s16.e01",
          "speaker": "ANNA",
          "line": "—so the kid looks at the X-ray of his own heart and says \"it looks like a ghost.\" And honestly? He's not wrong. Pediatric cardiology is basically ghost management.",
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
      "shot_id": "s16.sh02",
      "size": "MCU",
      "zone": "lab",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "depicts": [
        {
          "actors": [
            "DAMIEN",
            "ANNA"
          ],
          "channel": "date feed"
        }
      ],
      "implements": [
        "s16.e02"
      ],
      "covers_beats": {
        "s16.e02": [
          0
        ]
      },
      "purpose": "the watcher revealed — feed alive in frame, jaw tightening",
      "audio_note": "lab quiet, faint feed audio"
    },
    {
      "shot_id": "s16.sh03",
      "size": "CU",
      "zone": "neighborhood bistro",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "ANNA"
      ],
      "implements": [
        "s16.e03"
      ],
      "covers_beats": {
        "s16.e03": [
          0,
          1
        ]
      },
      "purpose": "earpiece coaching lands → he asks about the fellowship — the fed question made his own",
      "audio_note": "her V.O. private in his earpiece; bistro walla for the room",
      "dialogue_lines": [
        {
          "event_id": "s16.e03",
          "speaker": "MAYA",
          "line": "He's laughing. Nobody laughs on date three. It's in the manual. Ask about the fellowship.",
          "line_kind": "earpiece",
          "recipient": "DAMIEN",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s16.e03",
          "speaker": "DAMIEN",
          "line": "The fellowship in Minneapolis — Anna, that's a thousand miles—",
          "line_kind": "on_camera",
          "recipient": "ANNA",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        }
      ]
    },
    {
      "shot_id": "s16.sh04",
      "size": "OTS",
      "zone": "neighborhood bistro",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "ANNA"
      ],
      "implements": [
        "s16.e04"
      ],
      "covers_beats": {
        "s16.e04": [
          0,
          1
        ]
      },
      "purpose": "the dossier reveal lands — her directness, his stillness",
      "dialogue_lines": [
        {
          "event_id": "s16.e04",
          "speaker": "ANNA",
          "line": "It funds itself if I write the grant well enough. You'd be amazed what you get when you stop asking committees and start asking the person who lost someone. Speaking of — you lost your dad young, right? The trust thing is public, sorry, I did read the dossier.",
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
      "shot_id": "s16.sh05",
      "size": "MCU",
      "zone": "lab",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "depicts": [
        {
          "actors": [
            "DAMIEN",
            "ANNA"
          ],
          "channel": "date feed"
        }
      ],
      "implements": [
        "s16.e05"
      ],
      "covers_beats": {
        "s16.e05": [
          0,
          1
        ]
      },
      "purpose": "she leans toward the mic — and stops; no line she can feed him",
      "audio_note": "lab quiet, feed murmur; the mic unused"
    },
    {
      "shot_id": "s16.sh06",
      "size": "two-shot",
      "zone": "neighborhood bistro",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "ANNA"
      ],
      "implements": [
        "s16.e06"
      ],
      "covers_beats": {
        "s16.e06": [
          0,
          1
        ]
      },
      "purpose": "the eulogy confession and 'nobody corrected you' — unguarded for the first time",
      "audio_note": "bistro walla drops away under the confession",
      "dialogue_lines": [
        {
          "event_id": "s16.e06",
          "speaker": "DAMIEN",
          "line": "I was twenty-three. He died on a Tuesday, between meetings. I gave the eulogy in the tone of an earnings call.",
          "line_kind": "on_camera",
          "recipient": "ANNA",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s16.e06",
          "speaker": "ANNA",
          "line": "And nobody corrected you.",
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
      "shot_id": "s16.sh07",
      "size": "OTS",
      "zone": "neighborhood bistro",
      "type": "visual",
      "participants": [
        "DAMIEN",
        "ANNA"
      ],
      "implements": [
        "s16.e06"
      ],
      "covers_beats": {
        "s16.e06": [
          2,
          3
        ]
      },
      "purpose": "'How did you know that?' → 'people like us — graded on the tone, not the content'",
      "audio_note": "bistro walla still low — the loud room has gone quiet for them",
      "dialogue_lines": [
        {
          "event_id": "s16.e06",
          "speaker": "DAMIEN",
          "line": "How did you know that?",
          "line_kind": "on_camera",
          "recipient": "ANNA",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s16.e06",
          "speaker": "ANNA",
          "line": "Because people like us — people who take care of things — we get graded on the tone, not the content. I'm sorry, Damien. That's a terrible way to lose someone.",
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
      "shot_id": "s16.sh08",
      "size": "CU",
      "zone": "lab",
      "type": "visual",
      "participants": [
        "MAYA"
      ],
      "depicts": [
        {
          "actors": [
            "DAMIEN",
            "ANNA"
          ],
          "channel": "date feed"
        }
      ],
      "implements": [
        "s16.e07"
      ],
      "covers_beats": {
        "s16.e07": [
          0,
          1,
          2
        ]
      },
      "purpose": "the withheld mute — hand on the switch, feed still running, him unguarded with another woman",
      "audio_note": "feed audio keeps running; her thumb rests on the mute switch, never pressed"
    },
    {
      "shot_id": "s16.sh09",
      "size": "two-shot",
      "zone": "lab",
      "type": "visual",
      "participants": [
        "MAYA",
        "J-7"
      ],
      "depicts": [
        {
          "actors": [
            "DAMIEN",
            "ANNA"
          ],
          "channel": "date feed"
        }
      ],
      "implements": [
        "s16.e08"
      ],
      "covers_beats": {
        "s16.e08": [
          0,
          1,
          2,
          3
        ]
      },
      "purpose": "J-7 prices the denial — software conflict → bad candidate fit → 96% → 'Log it anyway.'",
      "audio_note": "feed murmur under the exchange; lab quiet",
      "dialogue_lines": [
        {
          "event_id": "s16.e08",
          "speaker": "J-7",
          "line": "You are grinding your teeth. Shall I log it as a software conflict?",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s16.e08",
          "speaker": "MAYA",
          "line": "Log it as a bad candidate fit.",
          "line_kind": "on_camera",
          "recipient": "J-7",
          "recipient_presence": "physical",
          "beats": [
            1
          ]
        },
        {
          "event_id": "s16.e08",
          "speaker": "J-7",
          "line": "She has a 96% compatibility index with your own profile, Maya.",
          "line_kind": "on_camera",
          "recipient": "MAYA",
          "recipient_presence": "physical",
          "beats": [
            2
          ]
        },
        {
          "event_id": "s16.e08",
          "speaker": "MAYA",
          "line": "Log it anyway.",
          "line_kind": "on_camera",
          "recipient": "J-7",
          "recipient_presence": "physical",
          "beats": [
            3
          ]
        }
      ]
    },
    {
      "shot_id": "s16.snd01",
      "type": "sound",
      "implements": [
        "s16.e06",
        "s16.e07"
      ],
      "purpose": "sound card: bistro walla falls away under the eulogy; lab feed keeps running — the mute never taken; no score",
      "audio_note": "bistro walla drops under the confession; feed audio continues in lab quiet; thumb on the mute switch, never pressed",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "DR. ANNA REYES — normal clothes, tired eyes, warm laugh, no angle. The bistro is small and loud and she clearly chose it herself.",
      "disposition": "covered_by",
      "by": [
        "s16.e01"
      ]
    },
    {
      "span": "—so the kid looks at the X-ray of his own heart and says \"it looks like a ghost.\" And honestly? He's not wrong. Pediatric cardiology is basically ghost management.",
      "disposition": "covered_by",
      "by": [
        "s16.e01"
      ]
    },
    {
      "span": "Damien laughs. Actually laughs — the sound surprises him as much as her.",
      "disposition": "covered_by",
      "by": [
        "s16.e01"
      ]
    },
    {
      "span": "At the lab, MAYA watches the feed, jaw tightening.",
      "disposition": "covered_by",
      "by": [
        "s16.e02"
      ]
    },
    {
      "span": "He's laughing. Nobody laughs on date three. It's in the manual. Ask about the fellowship.",
      "disposition": "covered_by",
      "by": [
        "s16.e03"
      ]
    },
    {
      "span": "The fellowship in Minneapolis — Anna, that's a thousand miles—",
      "disposition": "covered_by",
      "by": [
        "s16.e03"
      ]
    },
    {
      "span": "It funds itself if I write the grant well enough. You'd be amazed what you get when you stop asking committees and start asking the person who lost someone. Speaking of — you lost your dad young, right? The trust thing is public, sorry, I did read the dossier.",
      "disposition": "covered_by",
      "by": [
        "s16.e04"
      ]
    },
    {
      "span": "Damien goes still.",
      "disposition": "covered_by",
      "by": [
        "s16.e04"
      ]
    },
    {
      "span": "At the lab, Maya leans toward the mic — and stops. This isn't a line she can feed him.",
      "disposition": "covered_by",
      "by": [
        "s16.e05"
      ]
    },
    {
      "span": "I was twenty-three. He died on a Tuesday, between meetings. I gave the eulogy in the tone of an earnings call.",
      "disposition": "covered_by",
      "by": [
        "s16.e06"
      ]
    },
    {
      "span": "And nobody corrected you.",
      "disposition": "covered_by",
      "by": [
        "s16.e06"
      ]
    },
    {
      "span": "How did you know that?",
      "disposition": "covered_by",
      "by": [
        "s16.e06"
      ]
    },
    {
      "span": "Because people like us — people who take care of things — we get graded on the tone, not the content. I'm sorry, Damien. That's a terrible way to lose someone.",
      "disposition": "covered_by",
      "by": [
        "s16.e06"
      ]
    },
    {
      "span": "The feed keeps running. At the lab, Maya's hand rests on the mute switch. She doesn't press it. She watches Damien — actually talking, unguarded for the first time all film — with another woman.",
      "disposition": "covered_by",
      "by": [
        "s16.e07"
      ]
    },
    {
      "span": "You are grinding your teeth. Shall I log it as a software conflict?",
      "disposition": "covered_by",
      "by": [
        "s16.e08"
      ]
    },
    {
      "span": "Log it as a bad candidate fit.",
      "disposition": "covered_by",
      "by": [
        "s16.e08"
      ]
    },
    {
      "span": "She has a 96% compatibility index with your own profile, Maya.",
      "disposition": "covered_by",
      "by": [
        "s16.e08"
      ]
    },
    {
      "span": "Log it anyway.",
      "disposition": "covered_by",
      "by": [
        "s16.e08"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['ANNA'] | ANNA  | DR. ANNA REYES — normal clothes, tired eyes, warm laugh, no angle. The bistro is
i02 blk=['ANNA', 'MAYA'] | ANNA —so the kid looks at the X-ray of his own heart and says "it | ANNA faces MAYA and speaks.
i03 blk=['MAYA', 'DAMIEN'] | -  | Damien laughs. Actually laughs — the sound surprises him as much as her. At the 
i04 blk=['MAYA'] | MAYA He's laughing. Nobody laughs on date three. It's in the manu | MAYA faces ANNA and speaks.
i05 blk=['DAMIEN'] | DAMIEN The fellowship in Minneapolis — Anna, that's a thousand mile | DAMIEN faces ANNA and speaks.
i06 blk=['DAMIEN', 'ANNA'] | ANNA It funds itself if I write the grant well enough. You'd be a | ANNA faces MAYA and speaks.
i07 blk=['DAMIEN', 'MAYA'] | -  | Damien goes still. At the lab, Maya leans toward the mic — and stops. This isn't
i08 blk=['DAMIEN', 'ANNA'] | DAMIEN I was twenty-three. He died on a Tuesday, between meetings.  | DAMIEN faces ANNA and speaks.
i09 blk=['ANNA'] | ANNA And nobody corrected you. | ANNA faces MAYA and speaks.
i10 blk=['DAMIEN', 'ANNA'] | DAMIEN How did you know that? | DAMIEN faces ANNA and speaks.
i11 blk=['ANNA'] | ANNA Because people like us — people who take care of things — we | ANNA faces MAYA and speaks.
i12 blk=['DAMIEN', 'MAYA'] | -  | The feed keeps running. At the lab, Maya's hand rests on the mute switch. She do
i13 blk=['J-7'] | J-7 You are grinding your teeth. Shall I log it as a software co | J-7 faces ANNA and speaks.
i14 blk=['MAYA', 'ANNA'] | MAYA Log it as a bad candidate fit. | MAYA faces ANNA and speaks.
i15 blk=['MAYA', 'J-7'] | J-7 She has a 96% compatibility index with your own profile, May | J-7 faces ANNA and speaks.
i16 blk=['MAYA'] | MAYA Log it anyway. | MAYA faces ANNA and speaks.