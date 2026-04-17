---
mission: SCORE_REFORM
nucleus: n05
wave: M1
created: 2026-04-17
priority: CRITICAL
effort: opus_high
---

# N05 SCORE_REFORM M1: Reformulate cex_score.py

## CONTEXT

cex_score.py has 4 critical bugs that inflate scores and make the quality gate
meaningless as a pre-publish filter. Your job: fix all 4 in _tools/cex_score.py.

Read the full file first: `_tools/cex_score.py` (765 lines)

## BUG 1: Artificial floor 7.0 on all layers (lines 502-514, 560-562)

Current code clamps every layer score to min 7.0:
```python
structural = max(structural, 7.0)
rubric = max(rubric, 7.0)
semantic = max(semantic, 7.0)
```

Fix: remove all `max(..., 7.0)` clamps. Let scores be real (0-10).
Also adjust the normalization formula at line 502:
  `structural = round(8.0 + (struct_raw / 10.0) * 1.3, 2)`
This compresses everything into 8.0-9.3. Replace with linear mapping:
  `structural = round(struct_raw, 2)`  -- use raw score directly
Same for rubric (line 511) and semantic (line 560).

## BUG 2: Kind-score inheritance contaminates scores (lines 540-553)

Current code: if L1+L2 >= 8.8, find ANY cached artifact of same kind with
semantic >= 9.0 and inherit its semantic score. This means one good artifact
of kind=knowledge_card makes ALL knowledge_cards inherit 9.0 semantic regardless
of content quality.

Fix: remove the kind-inheritance optimization entirely (lines 531-553).
Replace with: if avg_12 >= 8.8 AND content hash matches a cached entry,
use the cached score. Otherwise always call the LLM.
The token savings are not worth score contamination.

## BUG 3: No batch/nucleus mode (CLI, line 676+)

Add these CLI flags to main():
  `--nucleus N01`     -- score only artifacts in N01_intelligence/
  `--null-only`       -- skip artifacts that already have quality != null
  `--apply-null-only` -- shorthand for --apply --null-only

Usage after fix:
```bash
python _tools/cex_score.py --hybrid --apply --null-only N01_intelligence/
python _tools/cex_score.py --hybrid --apply --nucleus n01 --null-only
```

Implementation: in the file-discovery section (line 688-698), when --null-only
is set, filter `args.files` to only those where `quality: null` appears in frontmatter.
When --nucleus is set, restrict search to `N0{N}_{name}/` directory.

## BUG 4: L2 rubric has 80% passthrough (lines 218-243)

Most hard gate checks fall through to `passed = True` because the check
string doesn't match any known pattern. Expand programmatic checks:

Add these patterns to the hard gate checker (insert after line 243):
```python
elif "tldr" in check and "present" in check:
    tldr = re.search(r'tldr:\s*.+', fm)
    passed = tldr is not None and len(tldr.group(0)) > 10
elif "tags" in check and ("list" in check or "present" in check):
    passed = bool(re.search(r'tags:\s*\[.+\]', fm))
elif "version" in check:
    passed = bool(re.search(r'version:\s*\d+\.\d+', fm))
elif "no placeholder" in check or "no todo" in check:
    bad = len(re.findall(r'(?i)\b(TODO|TBD|FIXME|insert here|add later)\b', body))
    passed = bad == 0
elif "has example" in check or "example" in check:
    passed = bool(re.search(r'(?i)## (Example|Usage|Sample)', body))
elif "has table" in check or "table" in check:
    passed = bool(re.search(r'^\|.*\|', body, re.MULTILINE))
elif "code block" in check or "```" in check:
    passed = "```" in body
elif "body length" in check or "min" in check and "words" in check:
    words = len(body.split())
    passed = words >= 100
elif "no filler" in check or "filler" in check:
    fillers = re.findall(r'(?i)\b(this document|in summary|it.?s worth noting|as mentioned)\b', body)
    passed = len(fillers) == 0
```

## VERIFICATION

After all fixes:
```bash
# Test on 3 artifacts: a good one, a bad one, a quality:null one
python _tools/cex_score.py --hybrid --verbose N01_intelligence/P01_knowledge/kc_intelligence_vocabulary.md
python _tools/cex_score.py --hybrid --apply --null-only --nucleus n06 --dry-run

# Sanity check: a minimal artifact (< 500 bytes, no content) should score < 6.0
# A rich artifact (>3KB, tables, examples) should score > 8.5
python _tools/cex_sanitize.py --check --scope _tools/
```

## COMPLETION

```bash
python _tools/cex_compile.py _tools/cex_score.py 2>/dev/null || true
git add _tools/cex_score.py
git commit -m "[N05] SCORE_REFORM M1: fix floor/contamination/batch/rubric in cex_score.py"
python -c "from _tools.signal_writer import write_signal; write_signal('n05', 'score_reform_complete', 9.0)"
```

## COMPLETION CRITERIA
- [ ] No `max(..., 7.0)` clamps on layer scores
- [ ] Kind-inheritance optimization removed
- [ ] --null-only and --nucleus flags added to CLI
- [ ] >= 5 new programmatic hard gate checks added to L2
- [ ] A minimal artifact scores < 6.0 (verified via --verbose)
- [ ] cex_sanitize.py passes (ASCII-only code)
- [ ] git commit [N05] SCORE_REFORM M1
- [ ] signal sent: n05 -> score_reform_complete
