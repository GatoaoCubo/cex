#!/usr/bin/env python3
"""validate_kc.py v2.0 - CEX KC Quality Gate."""

import json, re, sys, yaml
from pathlib import Path
from collections import Counter

HARD, SOFT = "HARD", "SOFT"

FILLER = [
    "this document describes", "this document explains",
    "in summary", "as mentioned", "it is worth noting",
    "it should be noted", "as we can see", "in conclusion",
    "to summarize", "as previously stated", "in this section",
    "este documento", "este kc", "neste documento",
    "como mencionado", "vale notar", "em resumo"]
SELF_REF = ["this document", "this kc", "this knowledge card",
    "este documento", "este kc", "esta knowledge card"]
INT_PATHS = [r"records/", r"\.claude/", r"/home/"]
CEX_RE = re.compile(r"p\d{2}_[a-z]+_[a-z_]+")
SEM_RE = re.compile(r"^\d+\.\d+\.\d+$")
DAT_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REQ = ["id","type","lp","title","version","created","updated",
    "author","domain","quality","tags","tldr","when_to_use"]

def parse_fm(text):
    if not text.startswith("---"): return None, text
    parts = text.split("---", 2)
    if len(parts) < 3: return None, text
    try: return yaml.safe_load(parts[1]), parts[2].strip()
    except yaml.YAMLError as e: return {"_err": str(e)}, text

def get_secs(body):
    out, cur = [], None
    for ln in body.split("\n"):
        if ln.startswith("## "):
            if cur: out.append(cur)
            cur = {"t": ln.lstrip("# ").strip(), "lines": []}
        elif cur is not None: cur["lines"].append(ln)
    if cur: out.append(cur)
    return out

def sec_bytes(s): return len("\n".join(s["lines"]).strip().encode("utf-8"))
def sec_ne(s): return sum(1 for l in s["lines"] if l.strip())
def get_bul(b): return [l.strip() for l in b.split("\n") if l.strip().startswith("- ") or l.strip().startswith("* ")]

def jaccard(a, b):
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)

def find_dupes(body, th=0.85):
    sents = [s.strip() for s in re.split(r"[.!?\n]", body) if len(s.strip()) > 20]
    ws = [(s, set(s.lower().split())) for s in sents]
    return [(ws[i][0][:60], ws[j][0][:60])
        for i in range(len(ws)) for j in range(i+1, len(ws))
        if jaccard(ws[i][1], ws[j][1]) >= th]

class Gate:
    def __init__(self, n, sv, d):
        self.name, self.sev, self.desc = n, sv, d
        self.ok, self.detail, self.fix = False, "", ""
    def to_dict(self):
        d = {"name": self.name, "severity": self.sev, "passed": self.ok, "detail": self.detail}
        if not self.ok and self.fix: d["fix"] = self.fix
        return d

def validate_kc(fp):
    text = fp.read_text(encoding="utf-8")
    stem = fp.stem; G = []
    def mk(n, sv, d):
        gate = Gate(n, sv, d); G.append(gate); return gate
    h = mk("H01_yaml", HARD, "Valid YAML")
    fm, body = parse_fm(text)
    if fm is None: h.detail = "No frontmatter"; return _res(fp, G)
    if "_err" in fm: h.detail = str(fm["_err"]); return _res(fp, G)
    h.ok = True; h.detail = "OK"
    kid = fm.get("id", "")
    h = mk("H02_id", HARD, "id==filename"); h.ok = kid == stem; h.detail = f"id={kid!r} f={stem!r}"
    h = mk("H03_fmt", HARD, "id pattern"); h.ok = bool(re.match(r"^p\d{2}_kc_[a-z][a-z0-9_]+$", str(kid))); h.detail = f"{kid!r}"
    h = mk("H04_type", HARD, "type=kc"); h.ok = fm.get("type") == "knowledge_card"; h.detail = f"{fm.get('type')!r}"
    h = mk("H05_qual", HARD, "quality=null"); h.ok = fm.get("quality") is None; h.detail = f"{fm.get('quality')!r}"
    h = mk("H06_fields", HARD, "13 required")
    miss = [f for f in REQ if f != "quality" and (fm.get(f) is None or fm.get(f) == "")]
    h.ok = not miss; h.detail = f"miss={miss}" if miss else "13/13"
    h = mk("H07_tags", HARD, "tags=list"); h.ok = isinstance(fm.get("tags"), list); h.detail = f"{type(fm.get('tags')).__name__}"
    h = mk("H08_size", HARD, "200-5120B"); bb = len(body.encode("utf-8")); h.ok = 200 <= bb <= 5120; h.detail = f"{bb}B"
    h = mk("H09_paths", HARD, "no int paths"); fp2 = [p for p in INT_PATHS if re.search(p, text)]
    h.ok = not fp2; h.detail = f"found={fp2}" if fp2 else "clean"
    h = mk("H10_author", HARD, "not STELLA"); h.ok = str(fm.get("author","")).upper() != "STELLA"; h.detail = f"{fm.get('author')!r}"
    secs = get_secs(body); tl = str(fm.get("tldr",""))
    s = mk("S01_tldr", SOFT, "<=160"); s.ok = 0 < len(tl) <= 160; s.detail = f"{len(tl)}ch"
    s = mk("S02_self", SOFT, "standalone"); sr = [p for p in SELF_REF if p in tl.lower()]; s.ok = not sr; s.detail = f"{sr}" if sr else "ok"
    s = mk("S03_title", SOFT, "5-100ch"); ti = str(fm.get("title","")); s.ok = 5 <= len(ti) <= 100; s.detail = f"{len(ti)}ch"
    s = mk("S04_semver", SOFT, "X.Y.Z"); s.ok = bool(SEM_RE.match(str(fm.get("version","")))); s.detail = f"{fm.get('version')!r}"
    s = mk("S05_dates", SOFT, "YYYY-MM-DD")
    s.ok = bool(DAT_RE.match(str(fm.get("created","")))) and bool(DAT_RE.match(str(fm.get("updated",""))))
    s.detail = f"{fm.get('created')} {fm.get('updated')}"
    s = mk("S06_secs", SOFT, ">=4"); s.ok = len(secs) >= 4; s.detail = f"{len(secs)}"
    s = mk("S07_lrg", SOFT, ">=30%"); lp = max((sec_bytes(x) for x in secs), default=0) / max(bb, 1) * 100
    s.ok = lp >= 30; s.detail = f"{lp:.1f}%"; s.fix = f"Expand ({lp:.1f}%<30%)"
    s = mk("S08_thin", SOFT, "no thin"); thin = [x["t"] for x in secs if sec_ne(x) < 3]
    s.ok = not thin; s.detail = f"thin={thin}" if thin else "ok"
    s = mk("S09_filler", SOFT, "no filler"); ff = [p for p in FILLER if p in body.lower()]
    s.ok = not ff; s.detail = f"{ff}" if ff else "clean"
    s = mk("S10_bul", SOFT, "<=80ch"); bul = get_bul(body); lb = [b for b in bul if len(b) > 80]
    s.ok = not lb; s.detail = f"{len(lb)}long/{len(bul)}" if lb else f"{len(bul)}ok"
    s = mk("S11_tbl", SOFT, "tables"); s.ok = bool(re.search(r"|.*|.*|", body)); s.detail = "y" if s.ok else "n"
    s = mk("S12_code", SOFT, "code"); s.ok = "```" in body; s.detail = "y" if s.ok else "n"; s.fix = "Add code"
    s = mk("S13_urls", SOFT, "ext URLs"); urls = re.findall(r"https?://[^\s)]+", body)
    s.ok = len(urls) > 0; s.detail = f"{len(urls)}" if urls else "0"; s.fix = "Add source URL"
    s = mk("S14_deep", SOFT, "refs KCs"); brefs = CEX_RE.findall(body); fmr = []
    la = fm.get("linked_artifacts", {})
    if isinstance(la, dict):
        if la.get("primary"): fmr.append(str(la["primary"]))
        for r in (la.get("related") or []): fmr.append(str(r))
    ar = brefs + [r for r in fmr if CEX_RE.match(r)]
    s.ok = len(ar) > 0; s.detail = f"{len(ar)}refs"; s.fix = "Add related KCs"
    s = mk("S15_src", SOFT, "data_source"); ds = fm.get("data_source")
    s.ok = ds is not None and str(ds).strip() not in ("", "null"); s.detail = "y" if s.ok else "n"
    s = mk("S16_kw", SOFT, "keywords"); kw = fm.get("keywords"); s.ok = isinstance(kw, list) and len(kw) >= 2
    s.detail = f"{len(kw) if isinstance(kw, list) else 0}"
    s = mk("S17_lt", SOFT, "long_tails"); lt = fm.get("long_tails"); s.ok = isinstance(lt, list) and len(lt) >= 1
    s.detail = f"{len(lt) if isinstance(lt, list) else 0}"
    s = mk("S18_ax", SOFT, "axioms"); ax = fm.get("axioms"); s.ok = isinstance(ax, list) and len(ax) >= 1
    s.detail = f"{len(ax) if isinstance(ax, list) else 0}"
    s = mk("S19_dupes", SOFT, "no dupes"); dp = find_dupes(body); s.ok = not dp; s.detail = f"{len(dp)}" if dp else "0"
    s = mk("S20_la", SOFT, "la struct"); la2 = fm.get("linked_artifacts", {})
    s.ok = isinstance(la2, dict) and "primary" in la2 and "related" in la2; s.detail = "y" if s.ok else "n"
    return _res(fp, G)

def _res(fp, G):
    hg = [x for x in G if x.sev == HARD]; sg = [x for x in G if x.sev == SOFT]
    hp, sp = sum(1 for x in hg if x.ok), sum(1 for x in sg if x.ok)
    ht, st = len(hg), len(sg)
    sc = round((sp / st * 10) if st > 0 else 0, 1); hok = hp == ht
    if not hok: v = "REJECTED"
    elif sc >= 9.5: v = "GOLDEN"
    elif sc >= 8.0: v = "PUBLISH"
    elif sc >= 7.0: v = "ACCEPTABLE"
    else: v = "NEEDS_WORK"
    return {"file": fp.name, "path": str(fp), "hard_pass": hok,
        "hard_score": f"{hp}/{ht}", "soft_passed": sp, "soft_total": st,
        "score": sc, "verdict": v, "gates": [x.to_dict() for x in G]}

def pr_human(r):
    v = r["verdict"]; sep = "=" * 64
    print()
    print(sep)
    fn = r["file"]; hs = r["hard_score"]; sc = r["score"]
    sp = r["soft_passed"]; st = r["soft_total"]
    print("  {}  [{}]  HARD {}  SCORE {}/10  ({}/{} soft)".format(fn, v, hs, sc, sp, st))
    print(sep)
    fixes = []
    for gate in r["gates"]:
        ico = "+" if gate["passed"] else "X"
        sv = "!" if gate["severity"] == HARD else " "
        det = "  ({})".format(gate["detail"]) if gate.get("detail") else ""
        print("  [{}]{} {}{}".format(ico, sv, gate["name"], det))
        if not gate["passed"] and gate.get("fix"):
            fixes.append("  -> {}".format(gate["fix"]))
    if fixes:
        print("  " + "~" * 40)
        print("  FIX:")
        for fx in fixes: print(fx)

def pr_sum(r):
    pad = " " * max(0, 48 - len(r["file"]))
    print("  {}{}{:>12}  {:>4}/10  HARD {}".format(r["file"], pad, r["verdict"], r["score"], r["hard_score"]))

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_kc.py <file|dir> [--json] [--summary]"); sys.exit(1)
    target = Path(sys.argv[1])
    jm = "--json" in sys.argv; sm = "--summary" in sys.argv
    if target.is_file(): files = [target]
    elif target.is_dir():
        files = sorted(target.glob("p01_kc_*.md"))
        if not files: files = sorted(target.glob("*.md"))
    else: print("Not found: {}".format(target)); sys.exit(1)
    if not files: print("No KCs in {}".format(target)); sys.exit(1)
    R = [validate_kc(f) for f in files]
    if jm:
        print(json.dumps(R, indent=2, ensure_ascii=False))
    elif sm:
        print("=" * 80)
        for r in R: pr_sum(r)
        vc = Counter(r["verdict"] for r in R)
        ss = [r["score"] for r in R]; av = sum(ss)/len(ss) if ss else 0
        print("=" * 80)
        print("  {} files | avg {:.1f}/10 | {} GOLD {} PUB {} ACC {} NW {} REJ".format(
            len(R), av, vc.get("GOLDEN",0), vc.get("PUBLISH",0),
            vc.get("ACCEPTABLE",0), vc.get("NEEDS_WORK",0), vc.get("REJECTED",0)))
        print("=" * 80)
    else:
        for r in R: pr_human(r)
        t = len(R); rej = sum(1 for r in R if not r["hard_pass"])
        ss = [r["score"] for r in R]; av = sum(ss)/len(ss) if ss else 0
        print()
        print("=" * 64)
        print("  BATCH: {} files | {} rejected | avg {:.1f}/10".format(t, rej, av))
        vc = Counter(r["verdict"] for r in R)
        for vv in ["GOLDEN","PUBLISH","ACCEPTABLE","NEEDS_WORK","REJECTED"]:
            if vc.get(vv,0) > 0: print("    {}: {}".format(vv, vc[vv]))
        print("=" * 64)
    sys.exit(1 if any(not r["hard_pass"] for r in R) else 0)

if __name__ == "__main__": main()
