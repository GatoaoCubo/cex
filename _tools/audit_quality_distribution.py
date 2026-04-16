"""Audit W7 QUALITY DISTRIBUTION: corpus stats from artifact frontmatter.

Reads inventory_full.jsonl. For every artifact with quality field, builds:
- Histogram (buckets: 0-2 / 2-4 / 4-6 / 6-7 / 7-8 / 8-8.5 / 8.5-9 / 9-9.5 / 9.5-10 / null)
- Top 50 lowest-quality artifacts (embarrassment list)
- Counts by kind, by pillar, by nucleus
- Density stats (lines/file by kind)

Output: _reports/audit/quality_distribution.md
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ROOT / "_reports" / "audit" / "inventory_full.jsonl"
OUT = ROOT / "_reports" / "audit" / "quality_distribution.md"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
QUALITY_RE = re.compile(r"^quality\s*:\s*(.+?)$", re.MULTILINE)
KIND_RE = re.compile(r"^kind\s*:\s*(.+?)$", re.MULTILINE)


def load_inventory() -> list[dict]:
    """Stream inventory_full.jsonl into memory."""
    records = []
    with INVENTORY.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def parse_frontmatter(file_path: Path) -> tuple[float | None, str | None]:
    """Extract quality + kind from YAML frontmatter."""
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")[:4000]
    except OSError:
        return None, None
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, None
    body = m.group(1)
    qm = QUALITY_RE.search(body)
    km = KIND_RE.search(body)
    quality = None
    if qm:
        raw = qm.group(1).strip().strip("'\"")
        if raw and raw.lower() not in ("null", "none", "~"):
            try:
                quality = float(raw)
            except ValueError:
                quality = None
    kind = km.group(1).strip().strip("'\"") if km else None
    return quality, kind


def bucket(q: float | None) -> str:
    """Map quality to histogram bucket."""
    if q is None:
        return "null"
    if q < 2: return "0-2"
    if q < 4: return "2-4"
    if q < 6: return "4-6"
    if q < 7: return "6-7"
    if q < 8: return "7-8"
    if q < 8.5: return "8-8.5"
    if q < 9: return "8.5-9"
    if q < 9.5: return "9-9.5"
    return "9.5-10"


def pillar_of(path: str) -> str:
    """Map path to pillar tag."""
    m = re.match(r"P(\d{2})_", path)
    if m:
        return f"P{m.group(1)}"
    return "other"


def nucleus_of(path: str) -> str:
    """Map path to nucleus tag."""
    m = re.match(r"N(\d{2})_", path)
    if m:
        return f"N{m.group(1)}"
    return "other"


def main() -> int:
    """Run W7 quality distribution audit."""
    print("[W7] loading inventory...")
    records = load_inventory()

    md_records = [r for r in records if r["path"].endswith(".md")
                  and not r["path"].startswith(("_reports/", ".cex/runtime/",
                                                ".cex/archive/", ".cex/cache/",
                                                ".git/", ".venv", ".aider"))]
    print(f"[W7] scanning {len(md_records)} md files for frontmatter...")

    rows = []
    by_bucket: dict[str, int] = defaultdict(int)
    by_kind: dict[str, list[float]] = defaultdict(list)
    by_pillar: dict[str, list[float]] = defaultdict(list)
    by_nucleus: dict[str, list[float]] = defaultdict(list)

    for i, r in enumerate(md_records):
        if i % 1000 == 0:
            print(f"[W7]   parsed {i}/{len(md_records)}")
        path = r["path"]
        quality, kind = parse_frontmatter(ROOT / path)
        b = bucket(quality)
        by_bucket[b] += 1
        if kind:
            if quality is not None:
                by_kind[kind].append(quality)
        if quality is not None:
            by_pillar[pillar_of(path)].append(quality)
            by_nucleus[nucleus_of(path)].append(quality)
            rows.append({"path": path, "kind": kind, "quality": quality,
                         "lines": r["lines"]})

    print(f"[W7] {len(rows)} artifacts with numeric quality")

    rows.sort(key=lambda r: r["quality"])
    embarrassments = [r for r in rows if r["quality"] < 7.0]

    out = ["# W7 QUALITY DISTRIBUTION", ""]
    out.append(f"Generated from `_reports/audit/inventory_full.jsonl`. "
               f"{len(md_records)} md files scanned, {len(rows)} with numeric quality, "
               f"{by_bucket['null']} with `null` (uncoded).")
    out.append("")
    out.append("## Histogram")
    out.append("")
    out.append("| Bucket | Count | % of scanned |")
    out.append("|--------|-------|--------------|")
    bucket_order = ["null", "0-2", "2-4", "4-6", "6-7", "7-8",
                    "8-8.5", "8.5-9", "9-9.5", "9.5-10"]
    total = sum(by_bucket.values()) or 1
    for b in bucket_order:
        n = by_bucket.get(b, 0)
        pct = 100.0 * n / total
        out.append(f"| {b} | {n} | {pct:.1f}% |")
    out.append("")
    out.append(f"## Embarrassment list (quality < 7.0): {len(embarrassments)}")
    out.append("")
    if embarrassments:
        out.append("| Path | Kind | Quality | Lines |")
        out.append("|------|------|---------|-------|")
        for r in embarrassments[:50]:
            kind = r["kind"] or "?"
            out.append(f"| `{r['path']}` | {kind} | {r['quality']} | {r['lines']} |")
        if len(embarrassments) > 50:
            out.append(f"| ... | ... | ... | (+{len(embarrassments) - 50} more) |")
    else:
        out.append("_None below 7.0._")
    out.append("")
    out.append("## By pillar (avg / count / min)")
    out.append("")
    out.append("| Pillar | Count | Avg | Min | Max |")
    out.append("|--------|-------|-----|-----|-----|")
    for p in sorted(by_pillar.keys()):
        qs = by_pillar[p]
        if not qs: continue
        out.append(f"| {p} | {len(qs)} | {sum(qs)/len(qs):.2f} | "
                   f"{min(qs):.2f} | {max(qs):.2f} |")
    out.append("")
    out.append("## By nucleus (avg / count / min)")
    out.append("")
    out.append("| Nucleus | Count | Avg | Min | Max |")
    out.append("|---------|-------|-----|-----|-----|")
    for n in sorted(by_nucleus.keys()):
        qs = by_nucleus[n]
        if not qs: continue
        out.append(f"| {n} | {len(qs)} | {sum(qs)/len(qs):.2f} | "
                   f"{min(qs):.2f} | {max(qs):.2f} |")
    out.append("")
    out.append("## By kind (top 30 by count, sorted by avg quality)")
    out.append("")
    out.append("| Kind | Count | Avg | Min |")
    out.append("|------|-------|-----|-----|")
    kind_summary = []
    for k, qs in by_kind.items():
        if len(qs) >= 5:
            kind_summary.append((k, len(qs), sum(qs)/len(qs), min(qs)))
    kind_summary.sort(key=lambda x: x[2])
    for k, n, avg, mn in kind_summary[:30]:
        out.append(f"| {k} | {n} | {avg:.2f} | {mn:.2f} |")
    out.append("")
    out.append("## QUALITY_DISTRIBUTION_PASS")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"[W7] report written: {OUT}")
    print("[W7] DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
