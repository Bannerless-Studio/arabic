# Arabic (MSA) A1-B1 vocab pack

Live at **https://bannerless-studio.github.io/arabic/**. A free, offline-capable
vocabulary trainer for Modern Standard Arabic (MSA), built on the shared
[`vocab-engine`](https://github.com/Bannerless-Studio/vocab-engine). It teaches
2000 words spanning A1-B1, each with a short English gloss and a
romanisation. Every word has at least two example sentences with English
translations. The Read tab adds 60 short reading passages with comprehension
questions.

**Scope note:** this app is a vocabulary base for B1. An exam also needs
grammar, writing and speaking practice, which this app does not teach.

## Using the trainer

- **Script primer.** An abjad stage runs before A1. It teaches the Arabic
  alphabet in 36 units over 7 sets, with symbol-to-sound, recognition and
  word-reading items. It can be skipped with "I can read it" and reopened
  from Progress.
- **Today** runs one daily session: review, learn new words, listen, recall,
  sentences, then (once unlocked) a reading passage. Each stage skips itself
  when it has too little due material.
- **Words** is a searchable browser with per-set drills; **Test** has a
  placement test plus free tests; **Progress** shows stats and lets you
  export, import or reset your progress.
- **Read tab passages.** 60 short MSA reading texts (20 each at A1, A2, B1),
  4-5 comprehension questions each. A passage's spaced re-read (after 7
  days) becomes a listening pass when every sentence has audio: the text
  stays hidden and about half the questions are audio-only.
- **Offline.** The page is cached on first visit and keeps working without a
  connection; a new build updates the cache in the background.
- Your progress is stored only in your browser (`localStorage`). Use
  Progress to export a backup or move it to another device.

## Script and display

- Arabic is right to left. Words display unvocalised with their hamza
  (أكل, سأل, مسؤول). The font is
  [Noto Naskh Arabic](https://fonts.google.com/noto/specimen/Noto+Naskh+Arabic)
  (OFL). English glosses and romanisation stay left to right.
- **Romanisation** (`pron`) follows Wiktionary's DIN 31635-style reading.
- Typing drills accept the written form without diacritics (harakat are
  never written in ordinary Arabic text, so strict diacritic matching is
  never required); a typed answer also folds hamza carriers and ة/ى the way
  search does. The optional leading ال is not folded, so الكتاب and كتاب are
  distinct answers.

## Data quality

Tatoeba's "ara" sentence set mixes MSA with dialect sentences; sentences with
a dialect marker or a low MSA confidence score are dropped (2,632 dropped).
The Arabic filter also drops sentences with Persian letters or words,
misspelt tokens, and side-taking political or religious sentences. Shipped
text is normalised (Persian ی/ک → ي/ى and ك; hamza on an alif-wasl noun such
as إبن, إسم → plain alif).

Tatoeba leaves some words with fewer than two usable sentences, so **285 of
the 3,024 example sentences were written for this pack** (marked `"src":
"gen"` in `pack/sentences.json`, listed in `tools/generated_examples.tsv`).
69 words have only written sentences; these are machine-authored and not
native-reviewed.

Sentence-to-word links are machine-generated and checked by an automated
English-side heuristic, not by a native speaker; known residual link errors
(mostly noun/verb homographs the English can't disambiguate, e.g. عرض, صور)
are tracked in `TODO.md`.

The Read tab passages were machine-written and checked by the builder's
automated QA plus an author self-check; they have not had an external QA
round or a native-speaker review.

Tatoeba has no permissively licensed Arabic recordings, so the pack has no
sentence audio; speech uses the browser's `ar-SA` voice. All 2000 words have
a romanisation.

Level bands (A1/A2/B1) are a reproducible frequency-based proxy for CEFR,
not an official classification. Against the Kelly reference list, 32.0% of
matched lemmas sit at the same level and 71.8% within one level.

## Sources and licences

| Data | Source | Licence | Used for |
|---|---|---|---|
| Subtitle frequency | [hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords) (`ar_full.txt`) | CC BY-SA 4.0 | word ranking |
| Written frequency | [`wordfreq`](https://github.com/rspeer/wordfreq) | CC BY-SA 4.0 | word ranking |
| Glosses, POS, romanisation, plurals | [kaikki.org](https://kaikki.org) Arabic Wiktionary extract | CC BY-SA 3.0 / GFDL | glosses, POS, `pron` |
| Tagging, lemmas, dialect ID (build time only) | [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools) 1.6.0 (MIT) with calima-msa-r13 (GPL-2.0 data), disambig-bert-unfactored-msa and DIDModel6 | see each package | corpus lemmas, MSA filter. No model files ship. |
| Example sentences | [Tatoeba](https://tatoeba.org) `ara_sentences_detailed.tsv` | CC BY 2.0 FR | sentence text (contributors in `pack/attribution.json`) |
| Sentence translations | Tatoeba `eng_sentences.tsv` + `ara-eng_links.tsv` | CC BY 2.0 FR | English translations |
| Written sentences | `tools/generated_examples.tsv`, written for this pack | same as this repo | 285 sentences marked `"src": "gen"` |
| Font | Noto Naskh Arabic via Google Fonts | SIL OFL 1.1 | display only |

## Rebuild and publish

This repo holds the Arabic data pack and the data files its build reads.
`vocab-engine` (above) is a git submodule at `engine/` and holds the shared
UI, drill logic and pack builder; all Arabic-specific rules live in
`engine/tools/packbuilder/langs/ar.py`. For the exact rebuild/check commands
and file-by-file notes on `tools/`, see `tools/README.md` and `CLAUDE.md`.
