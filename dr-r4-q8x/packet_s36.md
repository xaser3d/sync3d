# VALIDATION PACKET — scene s36
Role: independent reviewer. Compare screenplay evidence vs director events/plans.
Check: presence precision (physical/remote/offscreen/depicted), verbatim lines, beat coverage, silent events, geography. Cite exact lines. List what you could NOT verify.

========== SCREENPLAY SCENE ==========

## SCENE 36 — INT. BALLROOM — LATER

*The crowd hasn't left — nobody leaves a story like this.
PENHALIGON stands, cane and all, at the trustee table.*

PENHALIGON
The trustees have read Section Fourteen, as drafted, for
thirty years. Tonight we were asked to read it as intended.
The clause vests control in an heir who is "married and
demonstrably so" — where "demonstrably" was defined by the
founder in a supplemental memorandum that most of us had never
actually read until this evening.

*He produces a yellowed page.*

PENHALIGON (CONT'D)
Quoting the founder: "The demonstration required is not the
ceremony. It is the change. If my son stands before you a
different man than the one who needed the clause — that is the
marriage I wanted for him. The wedding is paperwork. Signed,
Dad."

*He lowers the page. Something very old and very fond crosses
his face.*

PENHALIGON (CONT'D)
The trustees rule: the demonstration has been made. Control
vests — conditional on a six-month review, because we are
still lawyers. As for the respondent Victor Cross's attempted
manipulation of a family instrument — that will be a separate
meeting, and a much less pleasant one.

*Victor — somewhere in the crowd — has gone very pale. VEGA is
already photographing him.*

---



========== DIRECTOR EVENTS JSON ==========

{
  "scene_id": 36,
  "scene_heading": "INT. BALLROOM — LATER",
  "source": "Script/rework/HALF_CHARGED_screenplay.md",
  "global_context": "Immediate aftermath of scene 35's surrender. The crowd refuses to leave. Penhaligon produces the founder's supplemental memorandum — 'the demonstration required is not the ceremony. It is the change.' — and the trustees rule that the demonstration has been made: control vests in Damien on a six-month review, while Victor is formally warned that a separate, much less pleasant meeting is coming. The reversal arrives as legal prose, not applause.",
  "zones": [
    "ballroom floor",
    "trustee table"
  ],
  "events": [
    {
      "event_id": "s36.e01",
      "source_evidence": [
        "*The crowd hasn't left — nobody leaves a story like this.\nPENHALIGON stands, cane and all, at the trustee table.*"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the room refuses to leave — and the eldest trustee rises to turn Damien's surrender into a verdict",
      "participants": [
        "PENHALIGON",
        "TRUSTEES",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "location": {
        "zones": [
          "ballroom floor",
          "trustee table"
        ],
        "primary": "ballroom floor"
      },
      "timeline": [
        {
          "beat": "the crowd hasn't left — nobody leaves a story like this",
          "type": "atmosphere"
        },
        {
          "beat": "Penhaligon stands, cane and all, at the trustee table",
          "type": "action"
        }
      ],
      "visual_requirements": [
        "the lingering crowd is its own frame — nobody seated, nobody leaving",
        "Penhaligon rising reads as the room's seniority asserting itself"
      ],
      "audio_requirements": [
        "lingering crowd murmur"
      ],
      "continuity_constraints": [
        "same trustee table where Damien set the documents down in scene 35",
        "Penhaligon's raised finger from the end of scene 35 has become him standing"
      ],
      "ambiguities": [],
      "must_appear": [
        "PENHALIGON"
      ],
      "tableau": false,
      "shot_sequence": [
        "s36.sh01",
        "s36.sh02",
        "s36.snd01"
      ]
    },
    {
      "event_id": "s36.e02",
      "source_evidence": [
        "PENHALIGON\nThe trustees have read Section Fourteen, as drafted, for\nthirty years. Tonight we were asked to read it as intended.\nThe clause vests control in an heir who is \"married and\ndemonstrably so\" — where \"demonstrably\" was defined by the\nfounder in a supplemental memorandum that most of us had never\nactually read until this evening."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the setup — thirty years of 'as drafted' vs tonight 'as intended'; the supplemental memorandum is named before it is shown",
      "participants": [
        "PENHALIGON",
        "TRUSTEES",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "GUESTS"
      ],
      "location": {
        "zone": "trustee table"
      },
      "timeline": [
        {
          "beat": "Section Fourteen, drafted vs intended — the supplemental memorandum named",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "held on Penhaligon — the legal preamble that makes the quote in e03 land"
      ],
      "audio_requirements": [
        "dry legal cadence over a hushed room"
      ],
      "continuity_constraints": [
        "'a supplemental memorandum' — the same 'second page of adjectives' Damien cited in scene 35"
      ],
      "ambiguities": [],
      "must_appear": [
        "PENHALIGON"
      ],
      "tableau": false,
      "shot_sequence": [
        "s36.sh03"
      ]
    },
    {
      "event_id": "s36.e03",
      "source_evidence": [
        "*He produces a yellowed page.*",
        "PENHALIGON (CONT'D)\nQuoting the founder: \"The demonstration required is not the\nceremony. It is the change. If my son stands before you a\ndifferent man than the one who needed the clause — that is the\nmarriage I wanted for him. The wedding is paperwork. Signed,\nDad.\"",
        "*He lowers the page. Something very old and very fond crosses\nhis face.*"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the founder's voice enters the room — a yellowed page rewrites thirty years of reading and lands 'the wedding is paperwork. Signed, Dad.'",
      "participants": [
        "PENHALIGON",
        "TRUSTEES",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "TRUSTEES",
        "GUESTS"
      ],
      "document_evidence": [
        {
          "artifact": "the founder's yellowed supplemental memorandum defining 'demonstrably'",
          "channel": "document"
        }
      ],
      "location": {
        "zone": "trustee table"
      },
      "timeline": [
        {
          "beat": "he produces a yellowed page",
          "type": "insert"
        },
        {
          "beat": "quoting the founder — 'the demonstration required is not the ceremony. It is the change.'",
          "type": "dialogue"
        },
        {
          "beat": "he lowers the page — something very old and very fond crosses his face",
          "type": "held_reaction"
        }
      ],
      "visual_requirements": [
        "the yellowed page is a standalone insert — age and handwriting legible as evidence",
        "the fond look after lowering the page is Penhaligon knowing the founder, not performing him"
      ],
      "audio_requirements": [
        "the hush for the reading — paper, an old man's breath"
      ],
      "continuity_constraints": [
        "the memorandum is the physical counterpart of the trust documents scene 35 put down on the same table"
      ],
      "ambiguities": [
        "the founder exists only as handwriting — whether the page is shown as a legible insert or held as a glowing prop is a director call; either way 'Signed, Dad' must be heard, not read"
      ],
      "must_appear": [
        "PENHALIGON"
      ],
      "tableau": false,
      "shot_sequence": [
        "s36.sh04",
        "s36.sh05",
        "s36.sh06",
        "s36.snd01"
      ]
    },
    {
      "event_id": "s36.e04",
      "source_evidence": [
        "PENHALIGON (CONT'D)\nThe trustees rule: the demonstration has been made. Control\nvests — conditional on a six-month review, because we are\nstill lawyers. As for the respondent Victor Cross's attempted\nmanipulation of a family instrument — that will be a separate\nmeeting, and a much less pleasant one."
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the ruling — control vests in Damien on a six-month review; and the sentence turns toward Victor: 'a much less pleasant' meeting",
      "participants": [
        "PENHALIGON",
        "TRUSTEES",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [
        "GUESTS"
      ],
      "location": {
        "zone": "trustee table"
      },
      "timeline": [
        {
          "beat": "the trustees rule — demonstration made, control vests, conditional on a six-month review 'because we are still lawyers'",
          "type": "dialogue"
        },
        {
          "beat": "the warning — Victor Cross's attempted manipulation gets a separate, much less pleasant meeting",
          "type": "dialogue"
        }
      ],
      "visual_requirements": [
        "held on Penhaligon through the ruling — the Victor warning lands dry, as procedure, not threat"
      ],
      "audio_requirements": [
        "the ruling delivered flat"
      ],
      "continuity_constraints": [
        "'conditional on a six-month review' — the condition scene 38's 'the trustees are still arguing about what conditional means' refers back to"
      ],
      "ambiguities": [],
      "must_appear": [
        "PENHALIGON"
      ],
      "tableau": false,
      "shot_sequence": [
        "s36.sh07"
      ]
    },
    {
      "event_id": "s36.e05",
      "source_evidence": [
        "*Victor — somewhere in the crowd — has gone very pale. VEGA is\nalready photographing him.*"
      ],
      "evidence_kind": "verbatim",
      "dramatic_function": "the sentence lands on its target — Victor pale in the crowd, and Vega's camera already turning evidence into ammunition",
      "participants": [
        "VICTOR",
        "VEGA",
        "GUESTS"
      ],
      "remote_participants": [],
      "offscreen_present": [],
      "depicts_via_channel": [
        {
          "actors": [
            "VICTOR"
          ],
          "seen_by": [
            "VEGA"
          ],
          "channel": "camera",
          "from_zone": "ballroom floor"
        }
      ],
      "location": {
        "zone": "ballroom floor"
      },
      "timeline": [
        {
          "beat": "Victor — somewhere in the crowd — has gone very pale",
          "type": "reaction"
        },
        {
          "beat": "Vega is already photographing him",
          "type": "held_action"
        }
      ],
      "visual_requirements": [
        "Victor lost in the crowd — no stage left to stand on",
        "Vega's camera frame on Victor makes the photograph feel like a charge sheet"
      ],
      "audio_requirements": [
        "camera shutter under the murmur"
      ],
      "continuity_constraints": [
        "Vega's lens work continues her scene-30/34 evidence-gathering — same appetite, new target"
      ],
      "ambiguities": [],
      "must_appear": [
        "VICTOR",
        "VEGA"
      ],
      "tableau": false,
      "shot_sequence": [
        "s36.sh08",
        "s36.sh09"
      ]
    }
  ],
  "shots": [
    {
      "shot_id": "s36.sh01",
      "size": "W",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "GUESTS"
      ],
      "implements": [
        "s36.e01"
      ],
      "covers_beats": {
        "s36.e01": [
          0
        ]
      },
      "purpose": "the crowd hasn't left — nobody leaves a story like this",
      "audio_note": "lingering crowd murmur"
    },
    {
      "shot_id": "s36.sh02",
      "size": "M",
      "zone": "trustee table",
      "type": "visual",
      "participants": [
        "PENHALIGON",
        "TRUSTEES"
      ],
      "implements": [
        "s36.e01"
      ],
      "covers_beats": {
        "s36.e01": [
          1
        ]
      },
      "purpose": "Penhaligon stands, cane and all, at the trustee table — the eldest takes the room",
      "audio_note": "cane on the floor; murmur settling"
    },
    {
      "shot_id": "s36.sh03",
      "size": "M",
      "zone": "trustee table",
      "type": "visual",
      "participants": [
        "PENHALIGON",
        "TRUSTEES"
      ],
      "implements": [
        "s36.e02"
      ],
      "covers_beats": {
        "s36.e02": [
          0
        ]
      },
      "purpose": "Section Fourteen — 'as drafted' for thirty years vs 'as intended' tonight; the memorandum named",
      "audio_note": "dry legal cadence; room hushed",
      "dialogue_lines": [
        {
          "event_id": "s36.e02",
          "speaker": "PENHALIGON",
          "line": "The trustees have read Section Fourteen, as drafted, for thirty years. Tonight we were asked to read it as intended. The clause vests control in an heir who is \"married and demonstrably so\" — where \"demonstrably\" was defined by the founder in a supplemental memorandum that most of us had never actually read until this evening.",
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
      "shot_id": "s36.sh04",
      "size": "INS",
      "zone": "trustee table",
      "type": "visual",
      "participants": [
        "PENHALIGON"
      ],
      "depicts": [
        {
          "object": "the yellowed supplemental memorandum page",
          "channel": "prop insert"
        }
      ],
      "implements": [
        "s36.e03"
      ],
      "covers_beats": {
        "s36.e03": [
          0
        ]
      },
      "purpose": "the yellowed page produced — age and handwriting legible as evidence",
      "audio_note": "paper; the hush beginning"
    },
    {
      "shot_id": "s36.sh05",
      "size": "M/CU",
      "zone": "trustee table",
      "type": "visual",
      "participants": [
        "PENHALIGON"
      ],
      "implements": [
        "s36.e03"
      ],
      "covers_beats": {
        "s36.e03": [
          1
        ]
      },
      "purpose": "quoting the founder — 'It is the change… The wedding is paperwork. Signed, Dad.'",
      "audio_note": "the hush for the reading; an old man's breath on the page",
      "dialogue_lines": [
        {
          "event_id": "s36.e03",
          "speaker": "PENHALIGON",
          "line": "Quoting the founder: \"The demonstration required is not the ceremony. It is the change. If my son stands before you a different man than the one who needed the clause — that is the marriage I wanted for him. The wedding is paperwork. Signed, Dad.\"",
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
      "shot_id": "s36.sh06",
      "size": "CU",
      "zone": "trustee table",
      "type": "visual",
      "participants": [
        "PENHALIGON"
      ],
      "implements": [
        "s36.e03"
      ],
      "covers_beats": {
        "s36.e03": [
          2
        ]
      },
      "purpose": "he lowers the page — something very old and very fond crosses his face",
      "audio_note": "the hush holds"
    },
    {
      "shot_id": "s36.sh07",
      "size": "M",
      "zone": "trustee table",
      "type": "visual",
      "participants": [
        "PENHALIGON",
        "TRUSTEES"
      ],
      "implements": [
        "s36.e04"
      ],
      "covers_beats": {
        "s36.e04": [
          0,
          1
        ]
      },
      "purpose": "the trustees rule — control vests on review — then the dry warning toward Victor",
      "audio_note": "the ruling delivered flat",
      "dialogue_lines": [
        {
          "event_id": "s36.e04",
          "speaker": "PENHALIGON",
          "line": "The trustees rule: the demonstration has been made. Control vests — conditional on a six-month review, because we are still lawyers.",
          "line_kind": "on_camera",
          "recipient": "GUESTS",
          "recipient_presence": "offscreen",
          "beats": [
            0
          ]
        },
        {
          "event_id": "s36.e04",
          "speaker": "PENHALIGON",
          "line": "As for the respondent Victor Cross's attempted manipulation of a family instrument — that will be a separate meeting, and a much less pleasant one.",
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
      "shot_id": "s36.sh08",
      "size": "M/R",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "VICTOR",
        "GUESTS"
      ],
      "implements": [
        "s36.e05"
      ],
      "covers_beats": {
        "s36.e05": [
          0
        ]
      },
      "purpose": "Victor — somewhere in the crowd — has gone very pale",
      "audio_note": "crowd murmur"
    },
    {
      "shot_id": "s36.sh09",
      "size": "M",
      "zone": "ballroom floor",
      "type": "visual",
      "participants": [
        "VEGA"
      ],
      "depicts": [
        {
          "actors": [
            "VICTOR"
          ],
          "channel": "camera"
        }
      ],
      "implements": [
        "s36.e05"
      ],
      "covers_beats": {
        "s36.e05": [
          1
        ]
      },
      "purpose": "Vega already photographing him — the evidence machine has a new target",
      "audio_note": "camera shutter under the murmur"
    },
    {
      "shot_id": "s36.snd01",
      "type": "sound",
      "implements": [
        "s36.e01",
        "s36.e03"
      ],
      "purpose": "sound-states card for the ruling — lingering murmur settling into the hush for the yellowed page",
      "audio_note": "lingering crowd murmur settling into the hush for the reading — paper, breath, dry legal cadence; no score",
      "no_score": true
    }
  ],
  "coverage": [
    {
      "span": "*The crowd hasn't left — nobody leaves a story like this.\nPENHALIGON stands, cane and all, at the trustee table.*",
      "disposition": "covered_by",
      "by": [
        "s36.e01"
      ]
    },
    {
      "span": "PENHALIGON\nThe trustees have read Section Fourteen, as drafted, for\nthirty years. Tonight we were asked to read it as intended.\nThe clause vests control in an heir who is \"married and\ndemonstrably so\" — where \"demonstrably\" was defined by the\nfounder in a supplemental memorandum that most of us had never\nactually read until this evening.",
      "disposition": "covered_by",
      "by": [
        "s36.e02"
      ]
    },
    {
      "span": "*He produces a yellowed page.*",
      "disposition": "covered_by",
      "by": [
        "s36.e03"
      ]
    },
    {
      "span": "PENHALIGON (CONT'D)\nQuoting the founder: \"The demonstration required is not the\nceremony. It is the change. If my son stands before you a\ndifferent man than the one who needed the clause — that is the\nmarriage I wanted for him. The wedding is paperwork. Signed,\nDad.\"",
      "disposition": "covered_by",
      "by": [
        "s36.e03"
      ]
    },
    {
      "span": "*He lowers the page. Something very old and very fond crosses\nhis face.*",
      "disposition": "covered_by",
      "by": [
        "s36.e03"
      ]
    },
    {
      "span": "PENHALIGON (CONT'D)\nThe trustees rule: the demonstration has been made. Control\nvests — conditional on a six-month review, because we are\nstill lawyers. As for the respondent Victor Cross's attempted\nmanipulation of a family instrument — that will be a separate\nmeeting, and a much less pleasant one.",
      "disposition": "covered_by",
      "by": [
        "s36.e04"
      ]
    },
    {
      "span": "*Victor — somewhere in the crowd — has gone very pale. VEGA is\nalready photographing him.*",
      "disposition": "covered_by",
      "by": [
        "s36.e05"
      ]
    }
  ]
}


========== EXISTING STUDIO CARDS (compact) ==========

i01 blk=['PENHALIGON'] | -  | The crowd hasn't left — nobody leaves a story like this. PENHALIGON stands, cane
i02 blk=['PENHALIGON', 'VEGA'] | PENHALIGON The trustees have read Section Fourteen, as drafted, for thi | PENHALIGON faces VEGA and speaks.
i03 blk=['PENHALIGON'] | PENHALIGON Quoting the founder: "The demonstration required is not the  | He produces a yellowed page.
i04 blk=['PENHALIGON'] | PENHALIGON The trustees rule: the demonstration has been made. Control  | He lowers the page. Something very old and very fond crosses his face.
i05 blk=['VEGA', 'VICTOR'] | -  | Victor — somewhere in the crowd — has gone very pale. VEGA is already photograph