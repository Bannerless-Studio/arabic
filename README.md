# Arabic (MSA) A1-B1 vocab pack

Static data pack for a language-agnostic vocab trainer (`key: "ar"`). It
teaches Modern Standard Arabic. It has 2000 words spanning A1-B1, each with a
short English gloss and a romanisation. Every word has at least two example
sentences with English translations. The Read tab adds 60 short reading
passages with comprehension questions.

**Script primer.** An abjad stage runs before A1. It teaches the Arabic
alphabet in 36 units over 7 sets, with symbol-to-sound, recognition and
word-reading items. It can be skipped with "I can read it" and reopened from
Progress.

This repo holds the Arabic data pack and the data files its build reads.
[`vocab-engine`](https://github.com/ishmum123/vocab-engine) is a git
submodule at `engine/`. The engine holds the shared UI, the drill logic and
the shared pack builder, `engine/tools/packbuilder`. All Arabic rules live in
`engine/tools/packbuilder/langs/ar.py`.

**Scope note:** this app is a vocabulary base for B1. An exam also needs
grammar, writing and speaking practice, which this app does not teach.

**Data quality.** Tatoeba's "ara" set mixes MSA with dialect sentences. The
MSA filter drops a sentence when it holds a dialect marker word. It also
drops a sentence when CAMeL's dialect ID gives it under 5% MSA and one of
its tokens has no MSA analysis. 2,632 Tatoeba sentences were dropped this
way. Beyond the shared content policy, the Arabic filter drops sentences
with Persian letters or words, sentences with a misspelt token (a word only
the analyser's backoff reads that is no transliterated name, loanword or
Wiktionary headword in the English's sense), and
side-taking political or religious sentences (Israel/Palestine, Kabylie
independence, proselytising, side-taking claims about a religious or
ethnic group; an English-side pattern in `ar.py`). Shipped
text is normalised: Persian ی/ک become ي/ى and ك, and hamza written on an
alif-wasl noun (إبن, إسم) becomes a plain alif. Tatoeba leaves some words
with fewer than two usable sentences, so
**285 of the 3,024 example sentences were written for this pack**. They are
marked `"src": "gen"` in `pack/sentences.json` and listed in
`tools/generated_examples.tsv`. 69 words have only written sentences. The
written sentences are machine-authored and not native-reviewed. Sentence-link
samples, checked by hand:

| Sample | Wrong links | Link accuracy |
|---|---|---|
| Seed 47, 48 sentences (tag t27) | 11 of 233 | 95.3% |
| Seed 48, 48 sentences (tag t30) | 9 of 230 | 96.1% |
| Seed 82, external QA snapshot | 21 of 236 | 91.1% |
| Seed 82, after the QA fix round (tag t42) | 4 of 239 | 98.3% |

The QA fix round added a per-sentence English check. A content-word link
is dropped when the sentence English does not carry its gloss and does
carry another reading of the spelling: a rival dictionary sense, a clitic
split, or a proper name (يومي Yumi, بيتي Betty, كن Ken). It never leaves a
word with fewer than two sentences. In a hand sample of 40 dropped links, 4
were false drops, all paraphrase. The remaining wrong links are noun/verb
homographs (عرض, صور) and thin glosses. Known
residuals are in `TODO.md`. Tatoeba has no permissively
licensed Arabic recordings, so the pack has no sentence audio. Speech uses
the browser's ar-SA voice. All 2000 words have a romanisation.

## Reading passages (Read tab)

`pack/passages.json` holds 60 short MSA reading texts, 20 each at A1, A2 and
B1. Each has 4-5 comprehension questions: 255 in all, 126 multiple-choice
and 129 true/false. The source is `tools/passages_src.json`.
`tools/passages_gen/` holds the authoring scaffolding that writes it:
`make.py` plus one module per level. Rebuild with:

```
python3 tools/passages_gen/make.py                                   # only after editing passages_gen/
PYTHONPATH=engine/tools python3 -m packbuilder passages --lang ar .  # --check: report only
python3 engine/tools/jsonify_pack.py pack                            # passages go into sentences.js
```

The builder enforces in-pack coverage of at least 95% at A1 and A2 and 93%
at B1. Word bands are 60-90 at A1, 90-120 at A2 and 110-150 at B1. An A1
passage may use at most 3 A2 words, and an A2 passage at most 3 B1 words.
All 60 passages reach full coverage apart from declared names. Arabic has no
capitals, so every name is declared in its passage's `oop` list. The Arabic
passage hook retags a name behind a proclitic (وسلمى, لرنا). A declared name
that is also a pack word (كريم, عمر, حسن, جمال) would still link to that
word, so the passages avoid such names. Per-passage numbers and the QA notes
are in `tools/REPORT_passages.md`.

The passages and questions were machine-written by Claude and checked by
the builder's automated QA plus an author self-check. They have not had an
external QA round or a native-speaker review.

## Script and display

- Arabic is right to left. `pack/pack.json` sets `rtl: true`,
  `langTag: "ar"` and a 1.8 line height. The font is
  [Noto Naskh Arabic](https://fonts.google.com/noto/specimen/Noto+Naskh+Arabic)
  (OFL), loaded from Google Fonts. English glosses and romanisation stay left
  to right.
- Words display unvocalised with their hamza (أكل, سأل, مسؤول). Matching
  folds hamza carriers, ة/ه and ى/ي and strips harakat, since unvocalised
  text writes them inconsistently.
- A token keeps its clitics (وبالكتاب), and the lemma is the host's (كتاب).
  The article, proclitics and pronoun suffixes never reach a lemma.
- **Romanisation** (`pron`) is Wiktionary's DIN 31635-style reading. Where
  Wiktionary has none, `ar.py` romanises a vocalised headword (Wiktionary's,
  else CAMeL's diacritisation) to the same scheme.
- Typing drills are off (`typing: null`). Recall and cloze drills use
  multiple choice.

## Sources and licences

| Data | Source | Licence | Used for |
|---|---|---|---|
| Subtitle frequency | [hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords) (`ar_full.txt`) | CC BY-SA 4.0 | word ranking |
| Written frequency | [`wordfreq`](https://github.com/rspeer/wordfreq) | CC BY-SA 4.0 | word ranking |
| Glosses, POS, romanisation, plurals | [kaikki.org](https://kaikki.org) Arabic Wiktionary extract | CC BY-SA 3.0 / GFDL | glosses, POS, `pron` |
| Tagging, lemmas, dialect ID (build time only) | [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools) 1.6.0 (MIT) with calima-msa-r13 (GPL-2.0 data), disambig-bert-unfactored-msa and DIDModel6 | see each package | corpus lemmas, MSA filter. No model files ship. |
| Example sentences | [Tatoeba](https://tatoeba.org) `ara_sentences_detailed.tsv` | CC BY 2.0 FR | sentence text (contributors in `pack/attribution.json`) |
| Sentence translations | Tatoeba `eng_sentences.tsv` + `ara-eng_links.tsv` | CC BY 2.0 FR | English translations |
| Written sentences | `tools/generated_examples.tsv`, written for this pack | same as this repo | 248 sentences marked `"src": "gen"` |
| Font | Noto Naskh Arabic via Google Fonts | SIL OFL 1.1 | display only |

Kelly's Arabic list is read at build time only for the CEFR cross-check in
`tools/REPORT.md`. It is not shipped.

## Level bands

Candidate (lemma, POS) pairs are ranked by the mean of the log subtitle rank
and the log `wordfreq` rank. Words seen fewer than 3 times in the tagged
corpus are dropped. A1 takes every forced item (313), then the best-ranked
words up to 600. A2 takes the next 700 and B1 the next 700. This is a
reproducible proxy for CEFR level. It is not an official CEFR
classification. Against Kelly, 32.0% of matched lemmas sit at the same level
and 71.8% within one level.

## Layout

```
pack/                pack.json, words.json, sentences.json, passages.json, script.json, attribution.json (+ generated .js)
engine/              git submodule -> vocab-engine (UI, drills, tools/packbuilder, langs/ar.py)
tools/
  build_pack.py      shim: python3 -m packbuilder build --lang ar --repo .
  gloss_overrides.json   hand gloss fixes ("lemma|pos")
  forced_a1.txt      A1 core list (closed sets are in langs/ar.py)
  generated_examples.tsv  sentences written for this pack (append only)
  id_map_v1.json     frozen "lemma|pos" -> word id (keeps learner progress across rebuilds)
  passages_src.json  reading passages source; passages_gen/ writes it
  requirements.txt   packbuilder deps + camel-tools (and its data packages)
  REPORT.md, REPORT_passages.md   generated build reports (manual sections kept)
build.sh             builds index.html from pack/ + engine/
check.sh             packbuilder check + engine validator + stale-build guard
```

## Rebuilding

```
git clone --recurse-submodules <this repo>
cd arabic
python3 -m venv .venv && source .venv/bin/activate
pip install -r tools/requirements.txt
CAMELTOOLS_DATA=.cache/camel_tools camel_data -i morphology-db-msa-r13 \
  disambig-mle-calima-msa-r13 disambig-bert-unfactored-msa dialectid-model6

python3 tools/build_pack.py               # pack/*.json + tools/REPORT.md
PYTHONPATH=engine/tools python3 -m packbuilder passages --lang ar .
python3 engine/tools/jsonify_pack.py pack # pack/*.js
./build.sh                                # index.html + sw.js
./check.sh                                # checks + stale-build guard
```

Sources download once into `.cache/` (gitignored). The build is
deterministic: two runs from cache give byte-identical `pack/*.json`. CAMeL's
raw analyses are cached per text in `.cache/derived/`, so a rule change never
reruns the model. Bump `versions["tag"]` in `langs/ar.py` whenever a tagging
rule changes. To build against a vocab-engine checkout other than the
submodule, set `PACKBUILDER_PATH=../vocab-engine/tools` for
`tools/build_pack.py` and `./check.sh`. QA helpers run with
`PYTHONPATH=engine/tools python3 -m packbuilder {scan,sample} --lang ar --repo .`.
