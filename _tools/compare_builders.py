#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compare_builders.py -- Compare original vs reconstructed builder files.

Measures 5 metrics per file: structural similarity, field coverage,
content similarity (Jaccard), size delta, and quality 5D (manual).

Usage:
  python compare_builders.py --original archetypes/builders/signal-builder/ --generated /tmp/signal-builder/
  python compare_builders.py --original archetypes/builders/signal-builder/ --generated /tmp/signal-builder/ --format table
  python compare_builders.py --original archetypes/builders/signal-builder/ --generated /tmp/signal-builder/ --strict
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml

    HAS_YAML = True
except ImportError:
    HAS_YAML = False


# ---------------------------------------------------------------------------
# Stopwords (PT + EN)
# ---------------------------------------------------------------------------

STOPWORDS = {
    "a",
    "o",
    "e",
    "de",
    "da",
    "do",
    "para",
    "com",
    "que",
    "em",
    "se",
    "por",
    "um",
    "uma",
    "no",
    "na",
    "os",
    "as",
    "ou",
    "ao",
    "dos",
    "das",
    "nos",
    "nas",
    "mais",
    "mas",
    "nao",
    "eh",
    "ser",
    "seu",
    "sua",
    "seus",
    "suas",
    "este",
    "esta",
    "isso",
    "esse",
    "the",
    "an",
    "o",
    "to",
    "in",
    "is",
    "are",
    "and",
    "or",
    "not",
    "for",
    "on",
    "with",
    "at",
    "by",
    "from",
    "be",
    "it",
    "i",
    "this",
    "that",
    "all",
    "when",
    "than",
    "then",
}

# ---------------------------------------------------------------------------
# Thresholds
# ---------------------------------------------------------------------------

THRESHOLDS = {
    "structural": {"pass": 85.0, "warn": 70.0},
    "fields": {"pass": 90.0, "warn": 80.0},
    "content": {"pass": 0.70, "warn": 0.55},
    "size_delta": {"pass": 20.0, "warn": 35.0},
    "quality_5d": {"pass": 9.0, "warn": 8.0},
}


# ---------------------------------------------------------------------------
# Algorithm: Structural Similarity (LCS of ## headers)
# ---------------------------------------------------------------------------


def extract_headers(text: str) -> list:
    """Extract normalized level-two headings from markdown text."""
    pattern = r"^##\s+(.+)$"
    headers = re.findall(pattern, text, re.MULTILINE)
    return [h.strip().lower().rstrip(":") for h in headers]


def lcs_length(a: list, b: list) -> int:
    """Compute the longest common subsequence length for two header lists."""
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def structural_similarity(orig_text: str, gen_text: str) -> float:
    """Score heading-order similarity between two builder documents."""
    orig_headers = extract_headers(orig_text)
    gen_headers = extract_headers(gen_text)
    if not orig_headers:
        return 100.0
    lcs = lcs_length(orig_headers, gen_headers)
    return round(lcs / len(orig_headers) * 100, 1)


# ---------------------------------------------------------------------------
# Algorithm: Field Coverage (frontmatter + table + {{variables}})
# ---------------------------------------------------------------------------


def extract_frontmatter_fields(text: str) -> set:
    """Extract normalized frontmatter keys from a markdown document."""
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return set()
    raw = match.group(1)
    if HAS_YAML:
        try:
            data = yaml.safe_load(raw)
            if isinstance(data, dict):
                return {k.lower().replace("-", "_") for k in data.keys()}
        except Exception:
            pass
    # Regex fallback
    keys = re.findall(r"^(\w[\w-]*):", raw, re.MULTILINE)
    return {k.lower().replace("-", "_") for k in keys}


def extract_table_fields(text: str) -> set:
    """Extract likely field names from markdown table rows."""
    fields = set()
    rows = re.findall(r"^\|([^|]+)\|", text, re.MULTILINE)
    for row in rows:
        cell = row.strip().lower()
        if cell in ("field", "name", "key", "parameter", "---", ":---", "---:"):
            continue
        if re.match(r"^[-:]+$", cell):
            continue
        cell = cell.replace("`", "").strip()
        if cell and len(cell) < 60:
            fields.add(cell.replace("-", "_"))
    return fields


def extract_template_variables(text: str) -> set:
    """Extract template variable names wrapped in double braces."""
    vars_ = re.findall(r"\{\{([a-z_][a-z0-9_]*)\}\}", text)
    return {v.lower() for v in vars_}


def extract_all_fields(text: str) -> set:
    """Combine field names discovered across all supported sources."""
    fields = set()
    fields |= extract_frontmatter_fields(text)
    fields |= extract_table_fields(text)
    fields |= extract_template_variables(text)
    return fields


def field_coverage(orig_text: str, gen_text: str) -> float:
    """Measure how many original fields are preserved in the generated file."""
    orig_fields = extract_all_fields(orig_text)
    gen_fields = extract_all_fields(gen_text)
    if not orig_fields:
        return 100.0
    overlap = orig_fields & gen_fields
    return round(len(overlap) / len(orig_fields) * 100, 1)


# ---------------------------------------------------------------------------
# Algorithm: Content Similarity (Jaccard)
# ---------------------------------------------------------------------------


def extract_body(text: str) -> str:
    """Return markdown content after the first frontmatter block when present."""
    parts = text.split("---", 2)
    if len(parts) >= 3:
        return parts[2]
    return text


def tokenize(text: str) -> set:
    """Tokenize text into normalized content words."""
    tokens = re.findall(r"[a-z0-9_]{2,}", text.lower())
    return {t for t in tokens if t not in STOPWORDS}


def content_similarity(orig_text: str, gen_text: str) -> float:
    """Compute Jaccard similarity across normalized document bodies."""
    orig_tokens = tokenize(extract_body(orig_text))
    gen_tokens = tokenize(extract_body(gen_text))
    if not orig_tokens and not gen_tokens:
        return 1.0
    if not orig_tokens or not gen_tokens:
        return 0.0
    intersection = orig_tokens & gen_tokens
    union = orig_tokens | gen_tokens
    return round(len(intersection) / len(union), 3)


# ---------------------------------------------------------------------------
# Algorithm: Size Delta
# ---------------------------------------------------------------------------


def size_delta(orig_path: Path, gen_path: Path) -> float:
    """Measure absolute byte-size drift as a percentage."""
    orig_bytes = orig_path.stat().st_size
    gen_bytes = gen_path.stat().st_size
    if orig_bytes == 0:
        return 0.0 if gen_bytes == 0 else 100.0
    delta = abs(gen_bytes - orig_bytes) / orig_bytes * 100
    return round(delta, 1)


# ---------------------------------------------------------------------------
# Verdict Logic
# ---------------------------------------------------------------------------


def file_verdict(metrics: dict) -> str:
    """Reduce per-metric scores into a single file verdict."""
    verdicts = []
    for metric, value in metrics.items():
        if value is None:
            continue
        t = THRESHOLDS[metric]
        if metric == "size_delta":
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


def builder_verdict(file_verdicts: list) -> str:
    """Aggregate file verdicts into a builder-level outcome."""
    fail_count = file_verdicts.count("FAIL")
    pass_count = file_verdicts.count("PASS")
    warn_count = file_verdicts.count("WARN")
    if fail_count > 2:
        return "FAIL"
    if pass_count + warn_count >= 10 and fail_count <= 2:
        return "WARN" if fail_count > 0 else "PASS"
    if fail_count == 0:
        return "PASS" if warn_count == 0 else "WARN"
    return "FAIL"


# ---------------------------------------------------------------------------
# File Matching
# ---------------------------------------------------------------------------


def match_files(original_dir: Path, generated_dir: Path):
    """Pair original markdown files with generated matches by filename."""
    originals = {f.name: f for f in original_dir.glob("*.md")}
    generated = {f.name: f for f in generated_dir.glob("*.md")}

    pairs = []
    for name in sorted(originals):
        if name in generated:
            pairs.append((originals[name], generated[name]))
        else:
            pairs.append((originals[name], None))

    extra = [name for name in generated if name not in originals]
    return pairs, extra


# ---------------------------------------------------------------------------
# Main Comparison
# ---------------------------------------------------------------------------


def compare(
    original_dir: Path, generated_dir: Path, quality_data: dict = None, skip_quality: bool = True
):
    """Compare two builder directories and return file-level and aggregate metrics."""
    pairs, extra = match_files(original_dir, generated_dir)
    builder_name = original_dir.name

    files_results = []
    all_verdicts = []
    warnings = []

    for orig_path, gen_path in pairs:
        name = orig_path.name
        if gen_path is None:
            files_results.append(
                {
                    "name": name,
                    "metrics": {
                        "structural": None,
                        "fields": None,
                        "content": None,
                        "size_delta": None,
                        "quality_5d": None,
                    },
                    "verdict": "FAIL",
                }
            )
            all_verdicts.append("FAIL")
            warnings.append(f"{name}: MISSING in generated directory")
            continue

        orig_text = orig_path.read_text(encoding="utf-8", errors="replace")
        gen_text = gen_path.read_text(encoding="utf-8", errors="replace")

        metrics = {
            "structural": structural_similarity(orig_text, gen_text),
            "fields": field_coverage(orig_text, gen_text),
            "content": content_similarity(orig_text, gen_text),
            "size_delta": size_delta(orig_path, gen_path),
            "quality_5d": quality_data.get(name) if quality_data else None,
        }

        verdict = file_verdict(metrics)
        files_results.append({"name": name, "metrics": metrics, "verdict": verdict})
        all_verdicts.append(verdict)

        # Collect warnings
        for metric, value in metrics.items():
            if value is None:
                continue
            t = THRESHOLDS[metric]
            if metric == "size_delta":
                if value > t["pass"] and value <= t["warn"]:
                    warnings.append(
                        f"{name}: {metric}={value}% (WARN threshold: {t['pass']}-{t['warn']}%)"
                    )
                elif value > t["warn"]:
                    warnings.append(
                        f"{name}: FAIL -- {metric}={value}% above threshold {t['warn']}%"
                    )
            else:
                if value < t["pass"] and value >= t["warn"]:
                    warnings.append(
                        f"{name}: {metric}={value} (WARN threshold: {t['warn']}-{t['pass']})"
                    )
                elif value < t["warn"]:
                    warnings.append(f"{name}: FAIL -- {metric}={value} below threshold {t['warn']}")

    if extra:
        for e in extra:
            warnings.append(f"Extra file in generated: {e}")

    # Aggregate
    def agg(key):
        """Summarize a metric across all compared files."""
        vals = [f["metrics"][key] for f in files_results if f["metrics"][key] is not None]
        if not vals:
            return None
        return {
            "mean": round(sum(vals) / len(vals), 1 if key != "content" else 3),
            "min": min(vals),
            "max": max(vals),
        }

    aggregate = {
        "structural": agg("structural"),
        "fields": agg("fields"),
        "content": agg("content"),
        "size_delta": agg("size_delta"),
        "quality_5d": agg("quality_5d"),
    }

    overall = builder_verdict(all_verdicts)

    return {
        "builder_name": builder_name,
        "original_dir": str(original_dir),
        "generated_dir": str(generated_dir),
        "timestamp": datetime.now().isoformat(),
        "files": files_results,
        "aggregate": aggregate,
        "summary": {
            "total_files": len(pairs),
            "pass": all_verdicts.count("PASS"),
            "warn": all_verdicts.count("WARN"),
            "fail": all_verdicts.count("FAIL"),
            "missing": sum(1 for _, g in pairs if g is None),
            "extra": len(extra),
        },
        "verdict": overall,
        "warnings": warnings,
    }


def print_table(result: dict):
    """Render comparison results as a human-readable markdown table."""
    print(f"\n# Comparison: {result['builder_name']}")
    print("| File | Structural | Fields | Content | Size Delta | Quality | Verdict |")
    print("|------|-----------|--------|---------|------------|---------|---------|")
    for f in result["files"]:
        m = f["metrics"]
        s = f"{m['structural']}%" if m["structural"] is not None else "MISS"
        fl = f"{m['fields']}%" if m["fields"] is not None else "MISS"
        c = f"{m['content']}" if m["content"] is not None else "MISS"
        sd = f"+{m['size_delta']}%" if m["size_delta"] is not None else "MISS"
        q = f"{m['quality_5d']}" if m["quality_5d"] is not None else "-"
        print(
            f"| {f['name']:<35s} | {s:>6s} | {fl:>6s} | {c:>5s} | {sd:>6s} | {q:>3s} | {f['verdict']:<4s} |"
        )

    s = result["summary"]
    print(
        f"\nOverall: {s['pass']}/{s['total_files']} PASS | {s['warn']}/{s['total_files']} WARN | {s['fail']}/{s['total_files']} FAIL"
    )
    print(f"Verdict: {result['verdict']}")

    if result["warnings"]:
        print("\nWarnings:")
        for w in result["warnings"]:
            print(f"  - {w}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    """Parse CLI arguments, run the comparison, and emit the requested output."""
    parser = argparse.ArgumentParser(description="Compare original vs reconstructed builder files")
    parser.add_argument("--original", required=True, help="Directory with original builder files")
    parser.add_argument("--generated", required=True, help="Directory with reconstructed files")
    parser.add_argument("--output", help="JSON output path")
    parser.add_argument("--format", choices=["json", "table"], default="json", help="Output format")
    parser.add_argument("--strict", action="store_true", help="Exit 1 if any FAIL")
    parser.add_argument("--skip-quality", action="store_true", default=True, help="Skip quality 5D")
    parser.add_argument("--quality-file", help="JSON file with pre-scored quality values")

    args = parser.parse_args()

    orig_dir = Path(args.original)
    gen_dir = Path(args.generated)

    if not orig_dir.is_dir():
        print(f"ERROR: Original directory not found: {orig_dir}", file=sys.stderr)
        sys.exit(2)
    if not gen_dir.is_dir():
        print(f"ERROR: Generated directory not found: {gen_dir}", file=sys.stderr)
        sys.exit(2)

    quality_data = None
    if args.quality_file:
        with open(args.quality_file, "r", encoding="utf-8") as f:
            quality_data = json.load(f)

    try:
        result = compare(orig_dir, gen_dir, quality_data)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(3)

    if args.format == "table":
        print_table(result)
    else:
        output_json = json.dumps(result, ensure_ascii=False, indent=2)
        if args.output:
            out_path = Path(args.output)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(output_json, encoding="utf-8")
            print(f"Report saved: {out_path}", file=sys.stderr)
        else:
            print(output_json)

    if args.strict and result["summary"]["fail"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
