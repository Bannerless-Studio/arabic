# Arabic trainer — agent notes

```
Tatoeba + hermitdave FrequencyWords + wordfreq + kaikki Wiktionary + CAMeL Tools (tagging)
        |
        v
tools/build_pack.py (packbuilder, langs/ar.py)  -->  pack/*.json (words, sentences,
        |                                              passages, script, attribution)
        v
engine/tools/jsonify_pack.py  -->  pack/*.js (generated)
        |
        v
build.sh (engine/app.html + engine/core.js + pack js)  -->  index.html + sw.js
        |
        v
GitHub Pages https://bannerless-studio.github.io/arabic/
progress lives in localStorage key vocab_ar on the shared origin
```

Why it is built this way: single-file site + service worker for offline; engine
as a git submodule so every language ships the same drills; pack ids frozen
(`tools/id_map_v1.json`) so learner progress survives rebuilds; Arabic-specific
rules (MSA dialect filter, clitic stripping, hamza/ة/ى folding, RTL passage
retagging) live in `engine/tools/packbuilder/langs/ar.py`, not in this repo.

## Commands (pinned)

- Rebuild pack: `python3 tools/build_pack.py` (shim for
  `PYTHONPATH=engine/tools python3 -m packbuilder build --lang ar --repo .`)
- Rebuild passages: `python3 tools/passages_gen/make.py` (only after editing
  `passages_gen/`), then
  `PYTHONPATH=engine/tools python3 -m packbuilder passages --lang ar .`
- Convert to JS: `python3 engine/tools/jsonify_pack.py pack`
- Build site: `./build.sh`
- Check (must pass before every commit of index.html): `./check.sh`
- Against a vocab-engine checkout other than the submodule: set
  `PACKBUILDER_PATH=../vocab-engine/tools`
- QA helpers: `PYTHONPATH=engine/tools python3 -m packbuilder {scan,sample} --lang ar --repo .`
- Engine tests live in vocab-engine (see its CLAUDE.md)

## Always

- Commit `index.html` and `sw.js` together; `check.sh`'s stale-build guard
  runs post-commit.
- Bump the engine submodule only to a vocab-engine main sha; rebuild after
  every bump.
- Keep ids append-only; never renumber (`tools/id_map_v1.json`).
- Bump `versions["tag"]` in `langs/ar.py` whenever a tagging rule changes
  (CAMeL's raw analyses are cached per text in `.cache/derived/`).
- Path-limited commits: `engine`, `index.html`, `sw.js`, `pack/`, `tools/`,
  `README.md`, `TODO.md`; never `.venv` or `.cache`.

## Never

- Edit `pack/*.json` by hand; change `tools/gloss_overrides.json`,
  `tools/forced_a1.txt` or `langs/ar.py` and rebuild.
- Edit `pack/*.js`, `index.html` or `sw.js` by hand (generated).
- Delete `sw.js` (use `engine/sw.disable.js`).
- Add comments that say what the code does; only why, or an external
  reference.
- Push to main without `git merge-base --is-ancestor origin/main HEAD`.

## Forbidden patterns

- No renumbering `tools/id_map_v1.json` — learner progress across rebuilds
  depends on stable ids.
- No hand edits to any generated file (see below).
- No what-comments in code, only why/external-reference comments.

## Generated files

`pack/*.js`, `index.html`, `sw.js`, `tools/REPORT.md`, `tools/REPORT_passages.md`
(manual QA sections inside them are preserved across regenerations),
`tools/id_map_v1.json` (frozen once published — hand-edit never after that
point).

## Where things are

`README.md` (end users), `tools/README.md` (builder inputs, file by file),
`TODO.md` (residual defect classes + STATUS history), `engine/` (submodule,
read-only here).
