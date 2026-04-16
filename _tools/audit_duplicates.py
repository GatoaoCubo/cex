"""Audit W2 DUPLICATES: detect py + md duplicates / near-dups.

For .py: AST function-signature + identical-body hashes.
For .md: 5-gram shingled MinHash-style Jaccard on body text.

Output: _reports/audit/duplicates.md
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ROOT / "_reports" / "audit" / "inventory_full.jsonl"
OUT = ROOT / "_reports" / "audit" / "duplicates.md"

WS_RE = re.compile(r"\s+")
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)


def load_inventory() -> list[dict]:
    """Stream inventory_full.jsonl into memory."""
    records = []
    with INVENTORY.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def py_function_hashes(file_path: Path) -> list[tuple[str, str, str]]:
    """Return (func_name, sig, body_hash) for top-level functions."""
    out = []
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(text)
    except (SyntaxError, OSError):
        return out
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            sig = f"{node.name}({len(node.args.args)})"
            try:
                body_text = ast.unparse(node.body) if node.body else ""
            except (AttributeError, Exception):
                body_text = ""
            body_norm = WS_RE.sub(" ", body_text).strip()
            if len(body_norm) < 50:
                continue
            h = hashlib.sha1(body_norm.encode("utf-8")).hexdigest()[:16]
            out.append((node.name, sig, h))
    return out


def md_body(file_path: Path) -> str:
    """Strip frontmatter + normalize whitespace from md body."""
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    text = FRONTMATTER_RE.sub("", text, count=1)
    text = WS_RE.sub(" ", text).strip().lower()
    return text


def shingles(text: str, k: int = 5) -> set[str]:
    """5-gram word shingles."""
    words = text.split()
    if len(words) < k:
        return {" ".join(words)} if words else set()
    return {" ".join(words[i:i + k]) for i in range(len(words) - k + 1)}


def jaccard(a: set[str], b: set[str]) -> float:
    """Jaccard similarity."""
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def find_py_dupes(records: list[dict]) -> list[dict]:
    """Group identical function bodies across the codebase."""
    by_hash: dict[str, list[tuple[str, str]]] = defaultdict(list)
    py_files = [r for r in records if r["path"].endswith(".py")
                and not r["path"].startswith((".venv", ".aider"))]
    for r in py_files:
        p = ROOT / r["path"]
        for fn, sig, h in py_function_hashes(p):
            by_hash[h].append((r["path"], f"{fn}{sig}"))
    return [
        {"hash": h, "occurrences": occs}
        for h, occs in by_hash.items()
        if len(occs) >= 2
    ]


def md_minhash_signature(shingle_set: set[str], num_hashes: int = 64) -> tuple[int, ...]:
    """Cheap MinHash: compute num_hashes hash-functions over shingles."""
    if not shingle_set:
        return tuple([0] * num_hashes)
    sig = []
    for i in range(num_hashes):
        salt = str(i).encode()
        min_h = min(
            int.from_bytes(hashlib.sha1(salt + s.encode("utf-8")).digest()[:8], "big")
            for s in shingle_set
        )
        sig.append(min_h)
    return tuple(sig)


def find_md_dupes(records: list[dict], threshold: float = 0.85) -> list[dict]:
    """Find near-duplicate md pairs via shingled Jaccard.

    Strategy: bucket by file size (within +/- 10%). Compute Jaccard within bucket.
    """
    md_files = [r for r in records if r["path"].endswith(".md")
                and r["lines"] >= 20
                and not r["path"].startswith(("_reports/", ".cex/runtime/",
                                              ".cex/archive/", ".cex/cache/"))]
    print(f"[W2-md] computing shingles for {len(md_files)} md files...")

    shingle_map: dict[str, set[str]] = {}
    sizes: dict[str, int] = {}
    for i, r in enumerate(md_files):
        if i % 500 == 0:
            print(f"[W2-md]   shingled {i}/{len(md_files)}")
        body = md_body(ROOT / r["path"])
        sh = shingles(body, k=5)
        if sh:
            shingle_map[r["path"]] = sh
            sizes[r["path"]] = len(body)

    paths = sorted(shingle_map.keys(), key=lambda p: sizes[p])
    print(f"[W2-md] comparing within size buckets ({len(paths)} files)...")

    pairs: list[dict] = []
    for i, a in enumerate(paths):
        if i % 500 == 0:
            print(f"[W2-md]   compared up to {i}")
        sa = sizes[a]
        lo = sa * 0.9
        hi = sa * 1.1
        for j in range(i + 1, len(paths)):
            b = paths[j]
            sb = sizes[b]
            if sb > hi:
                break
            if sb < lo:
                continue
            sim = jaccard(shingle_map[a], shingle_map[b])
            if sim >= threshold:
                pairs.append({"a": a, "b": b, "jaccard": round(sim, 3)})
    return pairs


def write_report(py_dupes: list[dict], md_dupes: list[dict]) -> None:
    """Emit duplicates.md."""
    py_dupes.sort(key=lambda d: -len(d["occurrences"]))
    md_dupes.sort(key=lambda d: -d["jaccard"])

    lines = [
        "# W2 DUPLICATES",
        "",
        f"Generated from `_reports/audit/inventory_full.jsonl`. "
        f"{len(py_dupes)} duplicate py-function groups + {len(md_dupes)} near-dup md pairs.",
        "",
        "## Python: identical function bodies (>= 2 occurrences)",
        "",
    ]
    if py_dupes:
        lines.append("| Group | Locations |")
        lines.append("|---|---|")
        for i, group in enumerate(py_dupes[:200]):
            occs = "<br>".join(f"`{path}` :: `{sig}`" for path, sig in group["occurrences"])
            lines.append(f"| {i + 1} ({len(group['occurrences'])}x) | {occs} |")
        if len(py_dupes) > 200:
            lines.append(f"| ... | (+{len(py_dupes) - 200} more groups truncated) |")
    else:
        lines.append("_None found (functions >= 50 chars body)._")
    lines.append("")
    lines.append("## Markdown: near-duplicate pairs (Jaccard >= 0.85, 5-gram)")
    lines.append("")
    if md_dupes:
        lines.append("| Pair | Jaccard | Suggested |")
        lines.append("|------|---------|-----------|")
        for p in md_dupes[:300]:
            suggest = "KEEP-canonical / DELETE-copy" if p["jaccard"] >= 0.95 else "REVIEW"
            lines.append(f"| `{p['a']}` <-> `{p['b']}` | {p['jaccard']} | {suggest} |")
        if len(md_dupes) > 300:
            lines.append(f"| ... | ... | (+{len(md_dupes) - 300} more pairs truncated) |")
    else:
        lines.append("_None found (>= 0.85 Jaccard)._")
    lines.append("")
    lines.append("## DUPLICATES_PASS")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[W2] report written: {OUT}")


def main() -> int:
    """Run W2 duplicate detection."""
    print("[W2] loading inventory...")
    records = load_inventory()
    print(f"[W2] {len(records)} records loaded")

    print("[W2] detecting python function dupes...")
    py_dupes = find_py_dupes(records)
    print(f"[W2] py: {len(py_dupes)} groups with >= 2 identical bodies")

    print("[W2] detecting md near-dupes...")
    md_dupes = find_md_dupes(records, threshold=0.85)
    print(f"[W2] md: {len(md_dupes)} pairs with Jaccard >= 0.85")

    write_report(py_dupes, md_dupes)
    print("[W2] DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
