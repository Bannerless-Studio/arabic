# Arabic pack: open items

Status 2026-09-26: pack, primer and passages built. All checks pass except
the stale-build guard's git-tracking half, since nothing is committed yet.
Not yet published.

Republish 09e90bc: sentence spans (15540/15540 linked words placed); inflected forms now cloze targets.
Republish ef44c6e: قنبلة A2→B1; عم B1→A2 (BLOOD exception) with override عم|noun "paternal uncle"; deleted override keys ثان|adj, صح|verb, علم|noun, مشاهدة|noun; set-counter and no-voice planner fixes
Open: عم "paternal uncle" still links homographs عَمِيَ "went blind" and عمّ "prevailed" (عم الصمت); 3 of its 7 examples are wrong senses (pre-existing, now at A2).

## Before publishing

- **Engine commit + submodule bump.** `langs/ar.py` and three small core
  hooks are uncommitted in vocab-engine: the `word_pos` spec hook
  (`langs/base.py`, called in `core/words.py`) and `fix_links_floor`
  (`langs/base.py`, used in `core/sentences.py`; 0 = off for every other
  language). `engine/` still points at
  a commit without `ar.py`, so `./check.sh` needs
  `PACKBUILDER_PATH=../vocab-engine/tools` until the bump.
- **Engine test.** `tests/test_passage_de_ru.py::HookOwners` now lists
  `"ar"` (uncommitted, with `ar.py`). It currently fails on `hi` (the
  untracked `langs/hi.py` from other work owns `passage_retag`), not on `ar`.
- **id map.** `tools/id_map_v1.json` was refrozen on 2026-09-26 from the
  re-QA'd build: ids w0001-w2000, contiguous, in level and rank order. From
  first publish on, never renumber: learner progress is keyed on these ids.
- **Live browser check** (RTL, font, primer, Read tab). External re-QA
  gave SHIP on 2026-09-26; the polish round after it is not re-QA'd.

## Sentence-link QA history (hand samples)

| Sample | Wrong links | Link accuracy |
|---|---|---|
| Seed 47, 48 sentences (tag t27) | 11 of 233 | 95.3% |
| Seed 48, 48 sentences (tag t30) | 9 of 230 | 96.1% |
| Seed 82, external QA snapshot | 21 of 236 | 91.1% |
| Seed 82, after the QA fix round (tag t42) | 4 of 239 | 98.3% |

The QA fix round added a per-sentence English check (`fix_links`): a
content-word link is dropped when the sentence English does not carry its
gloss and does carry another reading of the spelling (a rival dictionary
sense, a clitic split, or a proper name: يومي Yumi, بيتي Betty, كن Ken). It
never leaves a word with fewer than two sentences (`fix_links_floor`). In a
hand sample of 40 dropped links, 4 were false drops, all paraphrase.

## Residual defect classes (measured in hand samples, not fixed)

External QA (seed-82 snapshot) found seven classes. The fix round in `ar.py`
fixed them as classes: clitic/name guards on headwords, a per-sentence
English check on links (`fix_links`), verb + preposition pairs merged into
one card, display normalisation plus a Persian/typo sentence filter, primer
fixes, a political/religious drop pattern, and a romaniser for the missing
`pron`. What remains:

- **Homograph link check (`fix_links`) precision.** It drops a link when
  the English lacks the word's senses and carries a rival reading. Hand
  samples of 40 drops each: 48% false drops at re-QA, 10% after the polish
  round (stemmed English on both sides, the word's full dictionary senses,
  English words claimed by other links, no light-word evidence). Remaining
  false drops are paraphrase: جيد in "see to it", إمكان in "could you".
  A drop never leaves a word under 2 sentences (`fix_links_floor`).
- **Noun/verb homographs** the English cannot separate: عرض "offer" (noun)
  for "offered", صور "to photograph" for صُوَر "pictures", تحمل noun
  "endurance" for the verb أتحمل "I bear". Seed 82 after the fix round: 4
  wrong links of 239, two of them this class.
- **Other homograph links** seen in re-QA and not fixed: جسم "body" for a
  mistranslated حجم "size" sentence; إشعار, ضمن→ضمّ and مسجل did not recur
  in the rebuilt pack. Fixed in the polish round: وقع "to be located" (gloss),
  وحده/لوحده "alone" (now the وحد card, not حد or وحدة), خالية "empty" (not
  خال "uncle"), ألّا (not إلا).
- **Unsupported glosses.** 274 words have no sentence whose English carries
  a gloss word (431 in the QA snapshot). All were hand-reviewed. The rest
  are paraphrase ("Sami liked to party" for حضور الحفلات) and function
  words, not wrong senses.
- **Feminine noun read as masculine adjective.** جمهورية "republic" becomes
  جمهوري. A guard cannot tell these from real feminine adjectives (كبيرة)
  without context. جائز, whose tokens were all الجائزة "prize", is dropped.
- **Broken plural as its own lemma.** الأسر "families" feeds أسر
  "captivity". Sound feminine plurals lemmatise to a singular in ة (محلات to
  محلة). Collective plurals: الزهور links زهر, not زهرة.
- **Spelling variants of the English** defeat the link check: حي "alive"
  stays linked for الحيّ in a "neighbourhood" sentence (UK spelling vs the
  dictionary's "neighborhood").
- **Names that are pack words** (جمال, عمر, كريم) still link as the word
  unless the English carries the name. Passages avoid such names.
- **Elatives** (أرخص, أغلى, أسهل) are their own lemmas; most fall outside
  the 2000.
- **Typo filter.** A sentence with a token only the analyser's backoff
  reads is dropped unless the token transliterates an English word or is a
  Wiktionary headword (exact hamza spelling; a bare initial alif allowed) in
  the sense the English carries. That let the Berber sentences back (15
  ship: "learn Berber", "Berber keyboard"). Misspellings the analyser still
  reads (إبن, إسم) are normalised in display; three more (حَيْنَ, أصدقاءها
  as subject, بنسبتي لي) are dropped by pattern. Other such misspellings
  may remain.
- **Plural alts** must be the corpus's reading of that lemma at least 3
  times (not another headword's form: خطاء, عملة). 259 nouns carry one.
- **Audio:** none. Tatoeba has no permissively licensed Arabic
  recordings, so speech uses the browser's ar-SA voice.
- **Resolved (engine 122d88a, 2026-09-26): typed answers now fold hamza
  carriers and ة.** `typing.accents: lenient` drops hamza/madda on a
  carrier (أ/إ/آ → ا, ؤ → و, ئ → ی, and the extended hamza carriers), and
  folds ة → ه and ى → ی, so the common simplifications above are now
  accepted when typed. Every fold is guarded against collision with
  another pack word: a folded answer is rejected when it spells another
  entry's `w`/`alt` exactly (or its harakat/tatweel-stripped form). This
  pack has 25 such colliding pairs (PACK_SCHEMA.md's typing table),
  e.g. typing ما for ماء (w0009/w0206) or بدأ for بدا (w0112/w0128) is
  still wrong, both ways. The optional leading ال is still not folded for
  typing (كتاب ≠ الكتاب), matching search.

## Passages

- Machine-authored and QA'd by the builder plus an author self-check. Not
  native-reviewed and no external QA round yet.
- A1 has 13 of 40 mc keys verbatim in the text. That is under the ≤15
  target but the highest level.

## Republish 10706a9 (2026-10-08, port wave 3)
- Republish 10706a9: typed modes, day-aware scheduling, reading rotation, goals, pairs (script units keep their Review share), frequency tiers, Progress v2, redesigned tabs, session estimates. Pack diff vs 84b33f4: every word gains `ft` (A1 [100,440,60] A2 [0,525,175] B1 [0,420,280] ambient/core/peripheral); pack.json gains exactly the port flag block + `eta`; sentences, passages, script, attribution identical. `eta` measured with `tests/eta_checks.js --pack pack --calibrate --sessions 600` (tools/eta.json); check.sh now runs `packbuilder enrich --check`.
- Migration proof: rollback hash 84b33f4e695f3e4364803b36558d302c2f8713a7; previous live md5 index 7db059405c8003456b42cac32b871c05, sw 75d0b14fe476f7d06c7a46d6788142f3. Storage: new fields day/sn/t/u/f/p/pm/pv/pause/read.done s,ls/today.tw on first use (script records gain t/u, never p); boot writes nothing; previous build ef44c6e/aa00571 carries them (migration [port], primer learned).
