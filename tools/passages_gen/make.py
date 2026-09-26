"""Assemble tools/passages_src.json from the per-level authoring modules (a1/a2/b1)."""
import importlib.util, json, pathlib, re
HERE = pathlib.Path(__file__).parent
RULES = {"coverage": {"A1": .95, "A2": .95, "B1": .93}, "budget": {"A1": ["A2", 3], "A2": ["B1", 3], "B1": [None, 0]},
         "words_per_passage": {"A1": [60, 90], "A2": [90, 120], "B1": [110, 150]}, "questions": [4, 5]}
out, n, mc_i = [], 0, 0
for lv in ("a1", "a2", "b1"):
    f = HERE / f"{lv}.py"
    if not f.exists():
        continue
    spec = importlib.util.spec_from_file_location(lv, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for p in m.P:
        n += 1
        qs = []
        for q in p["q"]:
            if q[0] == "mc":
                _, qq, en, opts, words, s = q
                pos = mc_i % 4; mc_i += 1
                o = opts[1:]; o.insert(pos, opts[0])
                qs.append({"q": qq, "en": en, "type": "mc", "options": o, "answer": pos, "words": words, "sentence": s})
            else:
                _, qq, en, ans, words, s = q
                qs.append({"q": qq, "en": en, "type": "tf", "options": None, "answer": ans, "words": words, "sentence": s})
        out.append({"id": f"p{n:04d}", "lv": lv.upper(), "title": p["title"], "oop": {k: "name" for k in p["names"]},
                    "names": p["names"], "sentences": [list(x) for x in p["s"]], "questions": qs})
dst = HERE.parent / "passages_src.json"
dst.write_text(json.dumps({"rules": RULES, "passages": out}, ensure_ascii=False, indent=1) + "\n")
print(n, "passages ->", dst)
