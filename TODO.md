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
- Live proof 568852a (2026-10-08) KEEP: 12-session seed with primer learned from 84b33f4 byte-equal after boot/reload/Progress open (leaving Progress adds only prog.pv); one Today session writes w/sets/sessions/script/sn/day/pm; that record boots on 84b33f4 byte-equal (boot + reload), one key vocab_ar, a session runs there; back on live byte-equal; 0 console errors, 0 failed requests. Today shows "≈ 160 sessions" at session 13.
- Migration proof on engine 8745de1 (2026-10-09, scratch, live to follow): rollback hash 788dd8bc4c255eee8e4ed9f103a6711445ee66d0; previous live md5 index e42c942884605a2135341bd7814fb6ac, sw ea6071eaba731bffd09bb4a4d29db8e0. Storage: new fields read.done[pid].t, prog.pl and prog.script choice on a placement; boot writes nothing (migrations [rs] [pc]); previous build 10706a9 carries them. 12-session seed (primer learned) from 788dd8b byte-equal after boot/reload/Progress open (leaving Progress adds only prog.pv); one Today session on the new build; that record boots on 788dd8b byte-equal (boot + reload), one key vocab_ar, a session runs there; back on the new build byte-equal; 13/13 checks, 0 console errors, 0 failed requests.
- Live proof 8745de1 (2026-10-09) KEEP: live md5 index 23597135eed75339608e8a2ded145aea, sw 7f5808d28b7c1cf52def0a11c056b863 equal to local; the same 13/13 checks run against the live URL, 0 console errors, 0 failed requests.
- Migration proof on engine d2876d8 (2026-10-13, scratch, live to follow): rollback hash 9e047c8d19853f838ac2734b11501d3012827d1a; previous live md5 index 23597135eed75339608e8a2ded145aea, sw 7f5808d28b7c1cf52def0a11c056b863. KEEP: 42/42 proof checks (the 12-session seed from the 8745de1-era record boots on the new build byte-equal after boot/reload/Progress and back both directions; placed record from the previous build and a record that took the level exam (crit kept) boot unchanged and back). Feature check 22/22 on 360x780 touch, light and dark: placement 17 items, "Start at A2, set 36" = Learn's set; a Review miss on a placed word ends its prov (pl kept); level exam ready at A1, 20 bare items, 3 misses gave "Exam misses 3 left", Words flags exactly those 3, Review includes a critical item; Sentences drill 39 multiple-choice items, 0 options in their stimulus; notranslate present; 0 console errors, 0 failed requests. The arabic proof step 1 starts from the 12-session seed record rather than 12 sessions from a fresh record, because the fresh record opens on the script primer.
- Migration proof on engine 4f44f6b (2026-10-14, scratch, live to follow): rollback hash f01dc0d; previous live md5 index 1d303fb6e5f264f5986a231f859a4992, sw 2af8d7a615574d44882c4ffdb5c65357. New build index 38316b93b7a0cc58a1966037f8762311, sw 55acc9c22a979aa30e46036734a081e8. Rebuild on 4f44f6b before republish: pack byte-identical to f01dc0d (2000 word ids, 3023 sentence ids, no id map diff). Storage: boot writes nothing; the 12-session seed from the previous build boots byte-equal on the new build (boot, reload, Progress; a session runs) and back both ways; a placed record and a record with the level exam (crit kept) boot unchanged both ways; 42/42 proof checks KEEP. Feature check 26/26 on 360x780 touch, light and dark: placement 17 items "Start at A2, set 36" = Learn set; Learn card renders; Review miss on a placed word ends its prov (pl kept); level exam ready at A1, 20 bare items, 3 misses gave "Exam misses 3 left" and exactly those 3 critical words; changed gloss جو "weather; atmosphere" renders in Words and as a Review drill reveal; primer rule showPronOn true before the primer; Sentences drill 39 multiple-choice items, 0 leaks; notranslate present; 0 console errors, 0 failed requests.
- Migration proof on engine 1fd9546 (2026-10-14, scratch, live to follow): rollback hash 8a48428866b87304893b6091a0f0d93486430996 (republish PREV; live page md5 index 38316b93b7a0cc58a1966037f8762311, sw 55acc9c22a979aa30e46036734a081e8). New build md5 index b7968addff82635a079edacbb58347d7, sw 8121bcd5f46faf67dbf2c31679e7265f. Pack diff: pack.json eta only; passages.json unchanged in this commit (20 passages p0061-p0080 shipped in 1a53f1e, 8a48428). KEEP: proof 52 checks, 0 fails, 0 errors (12-session seed from the previous build boots on the new build byte-equal after boot, reload and Progress, and back both ways; placed, exam-2 and crit records unchanged both ways; a record with read.done p0001 boots byte-equal on both builds, p0001 stays done, p0061 absent). Feature check 20/20 on 360x780 touch, light and dark: placement to A1 set 1 in 12 items, Learn card renders, Today estimate shows numbers (fresh ≈170, established ≈58 sessions), Read tab lists 80 passages (A1 20, A2 30, B1 30), new A2 passage p0061 opens, word tap glosses, questions run and feedback shows a passage sentence, level exam ready at A1, 20 bare items, Test row "20 of 20, today", A2 opens; notranslate present; 0 console errors, 0 failed requests. No voice: Listen test skipped by design.
- Migration proof on engine 62db0cc (round H, 2026-10-15): linker fixes (hamza seat, hollow jussive, cross-POS lexeme, adverb vs noun, elative plural), passages relinked. Ids: w1999 (هدد) and w2000 (راتب) dropped, w2001 imam and w2002 completeness added; 17 sentence ids dropped and 17 added, surviving texts unchanged; p0079 declares راتب out of pack. Storage: nothing new. Rollback hash 4485bc0 (live md5 index b7968addff82635a079edacbb58347d7, sw 8121bcd5f46faf67dbf2c31679e7265f). Proof 18 of 19 literal: the one flagged check is prog.pv written on leaving Progress, the same allowed write as before; orphan record with w1999 pair streak boots on the new build without error, Progress ignores it, is kept, and boots on 4485bc0 byte-equal. Browser add-on 13 of 13 (80 listed, p0052 and p0079 open, taps gloss, questions run, Today shows numbers); the older check.js targets header ids that no longer exist, so it was not run. Controls: pack_flags 39/39, port_sites arabic 27/27, flagoff failures accepted.
