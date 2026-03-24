import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")
#!/usr/bin/env python3
"""CEX Example Validator — validates examples against schema naming, size, density."""

import re
import sys
import yaml
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parent.parent


def load_schema(lp_dir: Path) -> dict | None:
    schema_path = lp_dir / "_schema.yaml"
    if not schema_path.exists():
        return None
    try:
        with open(schema_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception:
        return None


def match_type_for_example(
    filename: str,
    schema_types: dict,
    lp_code: str,
    file_path: Path | None = None,
) -> tuple[str | None, dict | None]:
    """Match an example filename to its schema type via naming pattern or frontmatter."""
    lp_lower = lp_code.lower()
    for type_name, type_def in schema_types.items():
        naming = type_def.get("naming", "")
        # Extract prefix from naming pattern (e.g. "p01_kc_" from "p01_kc_{{topic}}.md")
        prefix_match = re.match(r"(" + re.escape(lp_lower) + r"_\w+_)", naming)
        if prefix_match:
            prefix = prefix_match.group(1)
            if filename.startswith(prefix):
                return type_name, type_def
        else:
            # Try simpler match: lp + type abbreviation
            simple = re.match(r"(" + re.escape(lp_lower) + r"_[a-z]+_)", naming)
            if simple and filename.startswith(simple.group(1)):
                return type_name, type_def

    # Fallback: read YAML frontmatter 'type' field from ex_* files
    if file_path and file_path.name.startswith("ex_"):
        try:
            text = file_path.read_text(encoding="utf-8")
            fm_match = re.match(r"^---\s*\n(.+?)\n---", text, re.DOTALL)
            if fm_match:
                fm = yaml.safe_load(fm_match.group(1))
                if isinstance(fm, dict) and "type" in fm:
                    fm_type = fm["type"]
                    if fm_type in schema_types:
                        return fm_type, schema_types[fm_type]
        except Exception:
            pass

    return None, None


def estimate_density(content: str) -> float:
    """Estimate content density: lines with data / total lines."""
    lines = content.strip().split("\n")
    if not lines:
        return 0.0

    data_lines = 0
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # Skip pure structural lines (headers, separators, empty bullets)
        if stripped in ("---", "```", "```yaml", "```markdown"):
            continue
        if re.match(r"^#{1,6}\s*$", stripped):
            continue
        if stripped in ("-", "*", ">"):
            continue
        data_lines += 1

    total_non_empty = sum(1 for line in lines if line.strip())
    return (data_lines / total_non_empty) if total_non_empty > 0 else 0.0


def validate_example(file_path: Path, schema_types: dict, lp_code: str) -> dict:
    """Validate a single example file."""
    result = {
        "file": file_path.name,
        "passes": 0,
        "fails": 0,
        "issues": [],
        "type_match": None,
        "size_bytes": 0,
        "density": 0.0,
    }

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        result["fails"] += 1
        result["issues"].append(f"cannot read: {e}")
        return result

    result["size_bytes"] = len(content.encode("utf-8"))

    # 1. Naming match
    type_name, type_def = match_type_for_example(file_path.stem, schema_types, lp_code, file_path)
    if type_name:
        result["type_match"] = type_name
        result["passes"] += 1
    else:
        result["fails"] += 1
        result["issues"].append("naming doesn't match any schema type")

    # 2. Size check
    if type_def:
        constraints = type_def.get("constraints", {})
        max_bytes = constraints.get("max_bytes") if isinstance(constraints, dict) else None
        if max_bytes:
            if result["size_bytes"] <= max_bytes:
                result["passes"] += 1
            else:
                result["fails"] += 1
                result["issues"].append(f"size {result['size_bytes']}B > max {max_bytes}B")
        else:
            result["passes"] += 1  # no constraint = pass
    else:
        # Can't check size without type match
        pass

    # 3. Density
    density = estimate_density(content)
    result["density"] = round(density, 2)

    if type_def:
        constraints = type_def.get("constraints", {})
        density_min = constraints.get("density_min", 0.0) if isinstance(constraints, dict) else 0.0
        if density_min and density < density_min:
            result["fails"] += 1
            result["issues"].append(f"density {density:.2f} < min {density_min}")
        else:
            result["passes"] += 1
    else:
        if density >= 0.7:
            result["passes"] += 1
        else:
            result["fails"] += 1
            result["issues"].append(f"density {density:.2f} below 0.7 baseline")

    return result


def main():
    print("=" * 60)
    print("CEX Example Validator")
    print("=" * 60)

    lp_dirs = sorted(CEX_ROOT.glob("P[0-9]*_*"))
    if not lp_dirs:
        print("ERROR: No P* directories found")
        sys.exit(1)

    total_pass = 0
    total_fail = 0
    total_examples = 0
    all_results = []

    for lp_dir in lp_dirs:
        examples_dir = lp_dir / "examples"
        if not examples_dir.exists():
            continue

        schema = load_schema(lp_dir)
        if not schema:
            continue

        lp_code = schema.get("lp", lp_dir.name.split("_")[0])
        schema_types = schema.get("types", {})

        examples = sorted(examples_dir.glob("*"))
        examples = [e for e in examples if e.is_file()]

        if not examples:
            continue

        print(f"\n--- {lp_dir.name} ({len(examples)} examples) ---")

        for ex in examples:
            result = validate_example(ex, schema_types, lp_code)
            total_pass += result["passes"]
            total_fail += result["fails"]
            total_examples += 1
            all_results.append((lp_dir.name, result))

            status = "PASS" if result["fails"] == 0 else "FAIL"
            type_str = result["type_match"] or "???"
            print(
                f"  [{status}] {result['file']}"
                f" | type={type_str}"
                f" | {result['size_bytes']}B"
                f" | density={result['density']}"
            )
            for issue in result["issues"]:
                print(f"        ! {issue}")

    print("\n" + "=" * 60)
    print("QUALITY REPORT")
    print("=" * 60)
    print(f"  Examples validated: {total_examples}")
    print(f"  Checks passed: {total_pass}")
    print(f"  Checks failed: {total_fail}")

    if total_examples > 0:
        densities = [r["density"] for _, r in all_results]
        avg_density = sum(densities) / len(densities)
        print(f"  Average density: {avg_density:.2f}")

        # By LP summary
        lps = {}
        for lp_name, r in all_results:
            if lp_name not in lps:
                lps[lp_name] = {"pass": 0, "fail": 0, "count": 0}
            lps[lp_name]["pass"] += r["passes"]
            lps[lp_name]["fail"] += r["fails"]
            lps[lp_name]["count"] += 1

        print(f"\n  {'LP':<20} {'Examples':<10} {'Pass':<8} {'Fail'}")
        print(f"  {'-' * 20} {'-' * 10} {'-' * 8} {'-' * 8}")
        for lp_name, stats in sorted(lps.items()):
            marker = "OK" if stats["fail"] == 0 else "XX"
            print(
                f"  [{marker}] {lp_name:<16} {stats['count']:<10}"
                f" {stats['pass']:<8} {stats['fail']}"
            )

    if total_fail > 0:
        print(f"\nSTATUS: FAIL ({total_fail} issues)")
        sys.exit(1)
    else:
        print("\nSTATUS: ALL EXAMPLES VALID")
        sys.exit(0)


if __name__ == "__main__":
    main()
