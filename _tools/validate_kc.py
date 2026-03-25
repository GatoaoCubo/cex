#!/usr/bin/env python3
"""validate_kc.py — 18-gate Knowledge Card validator for CEX."""

import re
import sys
import yaml
from pathlib import Path

FILLER_PHRASES = [
    "this document",
    "in summary",
    "as mentioned",
    "it is worth noting",
    "it should be noted",
    "as we can see",
    "in conclusion",
    "to summarize",
    "as previously stated",
    "in this section",
]

INTERNAL_PATH_PATTERNS = [
    r"records/core",
    r"records/pool",
    r"records/satellites",
    r"records/agents",
    r"records/skills",
    r"records/framework",
]

CEX_ID_PATTERN = re.compile(r"p\d{2}_[a-z]+_[a-z_]+")


def parse_frontmatter(text: str):
    """Parse YAML frontmatter from markdown text."""
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        fm = yaml.safe_load(parts[1])
        body = parts[2].strip()
        return fm, body
    except yaml.YAMLError as e:
        return {"_yaml_error": str(e)}, text


def get_body_sections(body: str):
    """Extract ## sections from body."""
    sections = []
    current = None
    for line in body.split("\n"):
        if line.startswith("## "):
            if current is not None:
                sections.append(current)
            current = {"title": line, "lines": []}
        elif current is not None:
            current["lines"].append(line)
    if current is not None:
        sections.append(current)
    return sections


def section_size(section: dict) -> int:
    return len("\n".join(section["lines"]).strip())


def get_all_bullets(body: str) -> list[str]:
    """Extract all bullet lines (- or *) from body."""
    bullets = []
    for line in body.split("\n"):
        stripped = line.strip()
        if stripped.startswith("- ") or stripped.startswith("* "):
            bullets.append(stripped)
    return bullets


def validate_kc(filepath: Path) -> dict:
    """Run 18 gates + YAML parse check on a KC file."""
    text = filepath.read_text(encoding="utf-8")
    file_size = len(text.encode("utf-8"))
    stem = filepath.stem

    fm, body = parse_frontmatter(text)
    results = {}

    # Gate 0: YAML parse
    if fm is None:
        results["yaml_parse"] = (False, "No frontmatter found")
        return results
    if "_yaml_error" in fm:
        results["yaml_parse"] = (False, fm["_yaml_error"])
        return results
    results["yaml_parse"] = (True, "OK")

    # Gate 1: id == filename stem
    kc_id = fm.get("id", "")
    results["01_id_matches_filename"] = (
        kc_id == stem,
        f"id={kc_id!r} vs stem={stem!r}",
    )

    # Gate 2: type == knowledge_card
    kc_type = fm.get("type", "")
    results["02_type_knowledge_card"] = (
        kc_type == "knowledge_card",
        f"type={kc_type!r}",
    )

    # Gate 3: quality is null
    quality = fm.get("quality")
    results["03_quality_null"] = (
        quality is None,
        f"quality={quality!r}",
    )

    # Gate 4: author != STELLA
    author = fm.get("author", "")
    results["04_author_not_stella"] = (
        author.upper() != "STELLA",
        f"author={author!r}",
    )

    # Gate 5: tldr <= 160 chars
    tldr = fm.get("tldr", "")
    results["05_tldr_length"] = (
        len(tldr) <= 160,
        f"len={len(tldr)}",
    )

    # Gate 6: when_to_use present
    wtu = fm.get("when_to_use", "")
    results["06_when_to_use"] = (
        bool(wtu),
        f"present={bool(wtu)}",
    )

    # Gate 7: linked_artifacts present
    la = fm.get("linked_artifacts")
    results["07_linked_artifacts"] = (
        la is not None,
        f"present={la is not None}",
    )

    # Gate 8: data_source present
    ds = fm.get("data_source", "")
    results["08_data_source"] = (
        bool(ds),
        f"present={bool(ds)}",
    )

    # Gate 9: total size <= 5120 bytes
    results["09_size_limit"] = (
        file_size <= 5120,
        f"size={file_size}",
    )

    # Gate 10: body sections >= 4
    sections = get_body_sections(body)
    results["10_min_sections"] = (
        len(sections) >= 4,
        f"sections={len(sections)}",
    )

    # Gate 11: largest section >= 30% of body
    body_len = len(body.strip())
    if body_len > 0 and sections:
        largest = max(section_size(s) for s in sections)
        pct = largest / body_len * 100
    else:
        pct = 0
    results["11_largest_section_30pct"] = (
        pct >= 30,
        f"largest={pct:.1f}%",
    )

    # Gate 12: no filler phrases
    body_lower = body.lower()
    found_filler = [p for p in FILLER_PHRASES if p in body_lower]
    results["12_no_filler"] = (
        len(found_filler) == 0,
        f"found={found_filler}" if found_filler else "clean",
    )

    # Gate 13: all bullets <= 80 chars
    bullets = get_all_bullets(body)
    long_bullets = [b for b in bullets if len(b) > 80]
    results["13_bullets_80_chars"] = (
        len(long_bullets) == 0,
        f"long={len(long_bullets)}/{len(bullets)}" if long_bullets else f"all_ok={len(bullets)}",
    )

    # Gate 14: has tables (pipe chars)
    has_tables = bool(re.search(r"\|.*\|.*\|", body))
    results["14_has_tables"] = (has_tables, "")

    # Gate 15: has code blocks
    has_code = "```" in body
    results["15_has_code_blocks"] = (has_code, "")

    # Gate 16: has external refs (http)
    has_http = bool(re.search(r"https?://", body))
    results["16_has_external_refs"] = (has_http, "")

    # Gate 17: has deepens refs (CEX artifact IDs)
    has_deepens = bool(CEX_ID_PATTERN.search(body))
    results["17_has_deepens_refs"] = (has_deepens, "")

    # Gate 18: no internal paths
    found_internal = [p for p in INTERNAL_PATH_PATTERNS if re.search(p, text)]
    results["18_no_internal_paths"] = (
        len(found_internal) == 0,
        f"found={found_internal}" if found_internal else "clean",
    )

    return results


def print_results(filepath: Path, results: dict):
    """Print gate results for one file."""
    passed = sum(1 for v, _ in results.values() if v)
    total = len(results)
    status = "PASS" if passed == total else "FAIL"

    print(f"\n{'=' * 60}")
    print(f"  {filepath.name}  [{status}] {passed}/{total} gates")
    print(f"{'=' * 60}")

    for gate, (ok, detail) in results.items():
        icon = "+" if ok else "X"
        detail_str = f"  ({detail})" if detail else ""
        print(f"  [{icon}] {gate}{detail_str}")

    return passed, total


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_kc.py [file.md | directory/]")
        sys.exit(1)

    target = Path(sys.argv[1])
    files = []

    if target.is_file():
        files = [target]
    elif target.is_dir():
        files = sorted(target.glob("*.md"))
    else:
        print(f"Error: {target} not found")
        sys.exit(1)

    if not files:
        print(f"No .md files found in {target}")
        sys.exit(1)

    total_passed = 0
    total_gates = 0
    total_files = 0
    pass_files = 0

    for f in files:
        results = validate_kc(f)
        p, t = print_results(f, results)
        total_passed += p
        total_gates += t
        total_files += 1
        if p == t:
            pass_files += 1

    print(f"\n{'=' * 60}")
    print(f"  SUMMARY: {pass_files}/{total_files} files pass all gates")
    print(f"  Gates: {total_passed}/{total_gates} total")
    print(f"{'=' * 60}")

    sys.exit(0 if pass_files == total_files else 1)


if __name__ == "__main__":
    main()
