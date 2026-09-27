# tools/ — Arabic pack builder inputs (dev/agent notes)

Purpose: everything the pack build reads or writes for the Arabic (`ar`) pack.
The actual build logic lives in vocab-engine's `engine/tools/packbuilder` and
`engine/tools/packbuilder/langs/ar.py`; this directory holds Arabic's
hand-maintained overrides plus the generated reports and frozen id map. Read
this before deciding what else in `tools/` you need to open.

## Hand-maintained (edit these to change the pack)

- `build_pack.py` — shim that runs
  `python3 -m packbuilder build --lang ar --repo .`. No Arabic logic here.
- `gloss_overrides.json` — hand gloss fixes, keyed `"lemma|pos"`.
- `forced_a1.txt` — the A1 core word list (closed grammatical sets such as
  pronouns/prepositions live in `langs/ar.py` instead).
- `generated_examples.tsv` — the 285 example sentences written for this pack
  (marked `"src": "gen"` in `pack/sentences.json`); append-only.
- `passages_src.json` — source text for the 60 reading passages.
- `passages_gen/` — authoring scaffolding that writes `passages_src.json`:
  `make.py` plus one module per level (`a1.py`, `a2.py`, `b1.py`).
- `requirements.txt` — packbuilder deps plus `camel-tools` and its data
  packages.

## Generated (do not hand-edit; rebuild instead)

- `id_map_v1.json` — frozen `"lemma|pos"` -> word id map. Keeps learner
  progress stable across rebuilds; append-only even before a schema change.
- `REPORT.md` — full build report (word-selection funnel, sentence stats,
  CEFR cross-check). The manual QA/verdict section inside is preserved
  across regenerations.
- `REPORT_passages.md` — per-passage coverage numbers and QA notes for the
  Read tab passages.

## Not part of the pack build

- `requirements.txt` is installed once into `.venv`; sources for the build
  itself (Tatoeba, FrequencyWords, wordfreq, kaikki Wiktionary, CAMeL Tools
  models) download into `.cache/` (gitignored) and are not tracked here.

## Rebuilding from scratch

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
reruns the model.

## Word-selection and level-band methodology

Candidate (lemma, POS) pairs are ranked by the mean of the log subtitle rank
and the log `wordfreq` rank. Words seen fewer than 3 times in the tagged
corpus are dropped. A1 takes every forced item (313, from `forced_a1.txt`
plus closed sets in `langs/ar.py`), then the best-ranked words up to 600. A2
takes the next 700 and B1 the next 700. Full funnel numbers (exclusion
counts, POS/level breakdown, CEFR cross-check against Kelly) are in the
generated `REPORT.md`.

A token keeps its clitics (وبالكتاب) but its lemma is the host's (كتاب); the
article, proclitics and pronoun suffixes never reach a lemma. This is a
`langs/ar.py` rule, not something `tools/` overrides.
