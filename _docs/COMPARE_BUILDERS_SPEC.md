---
title: Compare Builders Script Spec
status: SPEC
version: 1.0.0
author: PYTHA
created: 2026-03-28
wave: 6B
quality: 9.0
purpose: Spec for _tools/compare_builders.py — EDISON implements from this
target_implementer: EDISON
---

# Compare Builders Script Spec
**`_tools/compare_builders.py`** | **For EDISON to implement** | **v1.0.0**

> This spec defines the exact behavior of the comparison script used in Wave 6C
> self-build validation. EDISON reads this file and produces the implementation.
> No design decisions left open — all algorithms are fully specified.

---

## 1. Interface

### CLI Usage

```bash
# Basic comparison
python _tools/compare_builders.py \
  --original archetypes/builders/signal-builder/ \
  --generated /tmp/signal-builder/

# With custom output path
python _tools/compare_builders.py \
  --original archetypes/builders/agent-builder/ \
  --generated _tools/output/agent-builder/ \
  --output _tools/reports/comparison_agent.json

# Human-readable table (no JSON)
python _tools/compare_builders.py \
  --original archetypes/builders/signal-builder/ \
  --generated /tmp/signal-builder/ \
  --format table

# Strict mode: exit code 1 if any file FAILs
python _tools/compare_builders.py \
  --original archetypes/builders/signal-builder/ \
  --generated /tmp/signal-builder/ \
  --strict
```

### Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `--original` | path | YES | Directory containing the original 13 builder files |
| `--generated` | path | YES | Directory containing the reconstructed 13 files |
| `--output` | path | NO | JSON output path. Default: `_tools/reports/comparison_{builder_name}_{timestamp}.json` |
| `--format` | enum | NO | `json` (default) or `table` (human-readable markdown table to stdout) |
| `--strict` | flag | NO | Exit with code 1 if any file verdict is FAIL |
| `--skip-quality` | flag | NO | Skip Quality 5D column (leave as `null` — not automatable) |

---

## 2. File Matching

The script matches files by **base name** (not full path):

```python
# Collect originals
originals = {f.name: f for f in Path(original_dir).glob("*.md")}

# Collect generated
generated = {f.name: f for f in Path(generated_dir).glob("*.md")}

# Pair them
pairs = []
for name in originals:
    if name in generated:
        pairs.append((originals[name], generated[name]))
    else:
        pairs.append((originals[name], None))  # missing file

# Files in generated but not in original
extra_files = [name for name in generated if name not in originals]
```

**Missing files**: Report `null` for all metrics. Verdict = FAIL.
**Extra files**: Log as warning in output. Do not include in metric calculations.

---

## 3. Algorithm: Structural Similarity

**Goal**: % of original `##` headers present in reconstructed file, in the same relative order.

```python
import re

def extract_headers(text: str) -> list[str]:
    """Extract ## (h2) headers only. Normalize: lowercase, strip whitespace."""
    pattern = r'^##\s+(.+)$'
    headers = re.findall(pattern, text, re.MULTILINE)
    return [h.strip().lower() for h in headers]

def lcs_length(a: list, b: list) -> int:
    """Standard LCS dynamic programming."""
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def structural_similarity(orig_text: str, gen_text: str) -> float:
    """Returns 0.0-100.0"""
    orig_headers = extract_headers(orig_text)
    gen_headers = extract_headers(gen_text)
    if not orig_headers:
        return 100.0  # no headers to compare = trivially similar
    lcs = lcs_length(orig_headers, gen_headers)
    return round(lcs / len(orig_headers) * 100, 1)
```

**Edge cases**:
- Original has 0 `##` headers: return `100.0` (no structure to violate)
- Generated has 0 `##` headers but original has some: return `0.0`
- Headers with trailing colons (`## Overview:`) normalize to `overview`

---

## 4. Algorithm: Field Coverage

**Goal**: % of fields (frontmatter keys + body field table rows + `{{variables}}`) from original present in reconstructed.

```python
import re
import yaml

def extract_frontmatter_fields(text: str) -> set[str]:
    """Extract YAML frontmatter keys (top-level only)."""
    match = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    if not match:
        return set()
    try:
        data = yaml.safe_load(match.group(1))
        if isinstance(data, dict):
            return {k.lower().replace('-', '_') for k in data.keys()}
    except Exception:
        pass
    return set()

def extract_table_fields(text: str) -> set[str]:
    """Extract field names from markdown tables with | Field | pattern.
    Matches rows like: | field_name | ... | (first column after leading |)
    Skips header rows (contains 'field' as header) and separator rows (---)."""
    fields = set()
    # Find all table rows
    rows = re.findall(r'^\|([^|]+)\|', text, re.MULTILINE)
    for row in rows:
        cell = row.strip().lower()
        # Skip header row and separator
        if cell in ('field', 'name', 'key', 'parameter', '---', ':---', '---:'):
            continue
        if re.match(r'^[-:]+$', cell):
            continue
        # Normalize: remove backticks, strip
        cell = cell.replace('`', '').strip()
        if cell and len(cell) < 60:  # ignore overly long cells (descriptions)
            fields.add(cell.replace('-', '_'))
    return fields

def extract_template_variables(text: str) -> set[str]:
    """Extract {{variable}} slots from output templates."""
    vars_ = re.findall(r'\{\{([a-z_][a-z0-9_]*)\}\}', text)
    return {v.lower() for v in vars_}

def extract_all_fields(text: str) -> set[str]:
    fields = set()
    fields |= extract_frontmatter_fields(text)
    fields |= extract_table_fields(text)
    fields |= extract_template_variables(text)
    return fields

def field_coverage(orig_text: str, gen_text: str) -> float:
    """Returns 0.0-100.0"""
    orig_fields = extract_all_fields(orig_text)
    gen_fields = extract_all_fields(gen_text)
    if not orig_fields:
        return 100.0
    overlap = orig_fields & gen_fields
    return round(len(overlap) / len(orig_fields) * 100, 1)
```

**Edge cases**:
- YAML frontmatter parse error: fall back to regex key extraction (`^(\w+):`)
- Table with merged cells: take only first column value
- `{{type_name}}` and `{{type-name}}` normalize to same key (`type_name`)

---

## 5. Algorithm: Content Similarity

**Goal**: Jaccard similarity of token sets (body text only, stopwords removed).

```python
import re

STOPWORDS_PT = {
    'a', 'o', 'e', 'de', 'da', 'do', 'para', 'com', 'que', 'em',
    'se', 'por', 'um', 'uma', 'no', 'na', 'os', 'as', 'ou', 'ao',
    'dos', 'das', 'nos', 'nas', 'mais', 'mas', 'nao', 'eh', 'ser',
    'seu', 'sua', 'seus', 'suas', 'este', 'esta', 'isso', 'esse',
    'the', 'a', 'an', 'of', 'to', 'in', 'is', 'are', 'and', 'or',
    'not', 'for', 'on', 'with', 'at', 'by', 'from', 'be', 'it',
    'as', 'if', 'this', 'that', 'all', 'when', 'than', 'then',
}

def extract_body(text: str) -> str:
    """Remove frontmatter block (between first and second ---)."""
    parts = text.split('---', 2)
    if len(parts) >= 3:
        return parts[2]
    return text

def tokenize(text: str) -> set[str]:
    """Lowercase, split on non-alphanumeric, remove stopwords and short tokens."""
    tokens = re.findall(r'[a-z0-9_]{2,}', text.lower())
    return {t for t in tokens if t not in STOPWORDS_PT}

def content_similarity(orig_text: str, gen_text: str) -> float:
    """Returns Jaccard similarity 0.0-1.0"""
    orig_tokens = tokenize(extract_body(orig_text))
    gen_tokens = tokenize(extract_body(gen_text))
    if not orig_tokens and not gen_tokens:
        return 1.0
    if not orig_tokens or not gen_tokens:
        return 0.0
    intersection = orig_tokens & gen_tokens
    union = orig_tokens | gen_tokens
    return round(len(intersection) / len(union), 3)
```

**Edge cases**:
- Files with only frontmatter and no body: body = `""` → similarity = 1.0 (nothing to compare)
- Code blocks (` ```...``` `): include in token set (code terms matter for coverage)
- Numbers: kept as tokens (e.g., `9`, `0`, `85` are meaningful thresholds)

---

## 6. Algorithm: Size Delta

```python
def size_delta(orig_path: Path, gen_path: Path) -> float:
    """Returns unsigned percentage delta 0.0-100.0+"""
    orig_bytes = orig_path.stat().st_size
    gen_bytes = gen_path.stat().st_size
    if orig_bytes == 0:
        return 0.0 if gen_bytes == 0 else 100.0
    delta = abs(gen_bytes - orig_bytes) / orig_bytes * 100
    return round(delta, 1)
```

**Note**: Size delta > 100% is valid (generated file is more than 2x original).

---

## 7. Quality 5D

Quality score is **not computed by this script**. The script:
1. Outputs `null` for the `quality_5d` column by default
2. Accepts `--quality-file path/to/quality.json` to inject pre-scored values

Quality file format (manual input by reviewer):
```json
{
  "bld_manifest_signal.md": 9.2,
  "bld_schema_signal.md": 9.5,
  "bld_examples_signal.md": 8.8
}
```

Files not present in quality file → `null` in output.

---

## 8. Verdict Logic

```python
THRESHOLDS = {
    "structural": {"pass": 85.0, "warn": 70.0},  # % — above pass=PASS, above warn=WARN, else FAIL
    "fields":     {"pass": 90.0, "warn": 80.0},
    "content":    {"pass": 0.70, "warn": 0.55},   # 0.0-1.0
    "size_delta": {"pass": 20.0, "warn": 35.0},   # % — INVERTED: below pass=PASS, below warn=WARN
    "quality_5d": {"pass": 9.0,  "warn": 8.0},
}

def file_verdict(metrics: dict) -> str:
    """Returns PASS | WARN | FAIL"""
    verdicts = []
    for metric, value in metrics.items():
        if value is None:
            continue  # skip unscored (quality_5d)
        t = THRESHOLDS[metric]
        if metric == "size_delta":
            # Inverted: lower is better
            if value <= t["pass"]:
                verdicts.append("PASS")
            elif value <= t["warn"]:
                verdicts.append("WARN")
            else:
                verdicts.append("FAIL")
        else:
            if value >= t["pass"]:
                verdicts.append("PASS")
            elif value >= t["warn"]:
                verdicts.append("WARN")
            else:
                verdicts.append("FAIL")
    if "FAIL" in verdicts:
        return "FAIL"
    if "WARN" in verdicts:
        return "WARN"
    return "PASS"

def builder_verdict(file_verdicts: list[str]) -> str:
    """Returns PASS | WARN | FAIL for the entire builder (13 files)."""
    fail_count = file_verdicts.count("FAIL")
    pass_count = file_verdicts.count("PASS")
    warn_count = file_verdicts.count("WARN")
    if fail_count > 2:
        return "FAIL"
    if pass_count + warn_count >= 10 and fail_count <= 2:
        return "WARN" if fail_count > 0 else "PASS"
    return "FAIL"
```

---

## 9. Output Format

### JSON Output (`--format json`, default)

```json
{
  "builder_name": "signal-builder",
  "original_dir": "archetypes/builders/signal-builder",
  "generated_dir": "_tools/output/signal-builder",
  "timestamp": "2026-03-28T14:30:00-03:00",
  "files": [
    {
      "name": "bld_manifest_signal.md",
      "metrics": {
        "structural": 92.0,
        "fields": 100.0,
        "content": 0.87,
        "size_delta": 5.2,
        "quality_5d": null
      },
      "verdict": "PASS"
    }
  ],
  "aggregate": {
    "structural": {"mean": 91.5, "min": 78.0, "max": 100.0},
    "fields":     {"mean": 94.2, "min": 83.0, "max": 100.0},
    "content":    {"mean": 0.82, "min": 0.71, "max": 0.95},
    "size_delta": {"mean": 12.3, "min": 2.0,  "max": 28.0},
    "quality_5d": null
  },
  "summary": {
    "total_files": 13,
    "pass": 11,
    "warn": 1,
    "fail": 1,
    "missing": 0,
    "extra": 0
  },
  "verdict": "WARN",
  "warnings": [
    "bld_memory_signal.md: size_delta=28.0% (WARN threshold: 20-35%)",
    "bld_examples_signal.md: FAIL — structural=62% below threshold 70%"
  ]
}
```

### Table Output (`--format table`)

Prints to stdout:

```
# Comparison: signal-builder
| File | Structural | Fields | Content | Size Delta | Quality | Verdict |
|------|-----------|--------|---------|------------|---------|---------|
| bld_manifest_signal.md | 92% | 100% | 0.87 | +5% | - | PASS |
| bld_schema_signal.md   | 100% | 100% | 0.93 | +2% | - | PASS |
| ...                    | ... | ...  | ...  | ... | - | ...  |

Overall: 11/13 PASS | 1/13 WARN | 1/13 FAIL
Verdict: WARN
```

---

## 10. Dependencies

**Zero heavy dependencies.** Script must run with Python 3.9+ stdlib only:

| Module | Use |
|--------|-----|
| `re` | Regex extraction |
| `pathlib` | File handling |
| `json` | Output serialization |
| `datetime` | Timestamp |
| `argparse` | CLI |
| `sys` | Exit codes |

Optional (soft import, graceful fallback):
```python
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    # fall back to regex frontmatter key extraction
```

**Why no numpy/sklearn?**: Jaccard on sets requires no external libs. Avoids dependency hell in CODEXA environments without scipy.

---

## 11. Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Success (PASS or WARN) |
| `1` | Strict mode + at least 1 file FAIL |
| `2` | Input error (directory not found, no .md files) |
| `3` | Unexpected exception |

---

## 12. File Structure Post-Implementation

```
_tools/
  compare_builders.py          # Main script (EDISON implements)
  reports/
    comparison_{builder}_{ts}.json   # JSON output per run
  output/
    {builder}/                 # Generated files from Crew Runner
      bld_manifest_{type}.md
      bld_schema_{type}.md
      ... (13 files)
  dry_run/
    {builder}/
      bld_manifest_{type}.prompt.txt   # Rendered prompts (dry-run mode)
```

---

*COMPARE_BUILDERS_SPEC.md — PYTHA Wave 6B | CEX v1.0.0 | 2026-03-28*
