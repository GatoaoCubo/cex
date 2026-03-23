import sys
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")
#!/usr/bin/env python3
"""CEX Generator Validator — checks _generator.md completeness per LP."""

import sys
import yaml
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parent.parent
REQUIRED_SECTIONS = ["QUANDO USAR", "PASSO A PASSO", "ANTI-PATTERNS"]


def load_schema_types(lp_dir: Path) -> list[str]:
    schema_path = lp_dir / "_schema.yaml"
    if not schema_path.exists():
        return []
    try:
        with open(schema_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        types = data.get("types", {})
        return list(types.keys()) if isinstance(types, dict) else []
    except Exception:
        return []


def validate_generator(lp_dir: Path) -> tuple[int, int, list[str]]:
    gen_path = lp_dir / "_generator.md"
    lp_name = lp_dir.name
    passes = 0
    fails = 0
    issues = []

    # Check existence
    if not gen_path.exists():
        return 0, 1, [f"{lp_name}: _generator.md not found"]

    try:
        content = gen_path.read_text(encoding="utf-8")
    except Exception as e:
        return 0, 1, [f"{lp_name}: cannot read _generator.md: {e}"]

    content_upper = content.upper()

    # Check required sections
    for section in REQUIRED_SECTIONS:
        if section.upper() in content_upper:
            passes += 1
        else:
            fails += 1
            issues.append(f"missing section: {section}")

    # Check schema type coverage
    schema_types = load_schema_types(lp_dir)
    if schema_types:
        mentioned = 0
        missing_types = []
        for t in schema_types:
            # Check if type name appears in generator (flexible matching)
            t_variants = [t, t.replace("_", " "), t.replace("_", "-")]
            found = any(v.lower() in content.lower() for v in t_variants)
            if found:
                mentioned += 1
            else:
                missing_types.append(t)

        if missing_types:
            fails += 1
            issues.append(f"types not mentioned: {', '.join(missing_types)}")
        else:
            passes += 1

        coverage = (mentioned / len(schema_types) * 100) if schema_types else 0
    else:
        coverage = 0
        issues.append("no schema types found to validate against")

    # Check minimum content length
    lines = [l for l in content.strip().split("\n") if l.strip()]
    if len(lines) >= 10:
        passes += 1
    else:
        fails += 1
        issues.append(f"too short ({len(lines)} lines, min 10)")

    return passes, fails, issues


def main():
    print("=" * 60)
    print("CEX Generator Validator")
    print("=" * 60)

    lp_dirs = sorted(CEX_ROOT.glob("P[0-9]*_*"))
    if not lp_dirs:
        print("ERROR: No P* directories found")
        sys.exit(1)

    total_pass = 0
    total_fail = 0
    results = []

    for lp_dir in lp_dirs:
        print(f"\n--- {lp_dir.name} ---")
        p, f, issues = validate_generator(lp_dir)
        total_pass += p
        total_fail += f
        status = "PASS" if f == 0 else "FAIL"

        schema_types = load_schema_types(lp_dir)
        gen_path = lp_dir / "_generator.md"
        if gen_path.exists():
            content = gen_path.read_text(encoding="utf-8").lower()
            mentioned = sum(
                1
                for t in schema_types
                if any(v.lower() in content for v in [t, t.replace("_", " ")])
            )
            coverage = f"{mentioned}/{len(schema_types)}" if schema_types else "N/A"
        else:
            coverage = "N/A"

        results.append((lp_dir.name, status, p, f, coverage))

        if issues:
            for issue in issues:
                print(f"  ISSUE: {issue}")
        print(f"  Result: {status} | types coverage: {coverage}")

    print("\n" + "=" * 60)
    print("COMPLETENESS REPORT")
    print("=" * 60)
    print(f"  {'LP':<20} {'Status':<8} {'Pass':<6} {'Fail':<6} {'Types'}")
    print(f"  {'-' * 20} {'-' * 8} {'-' * 6} {'-' * 6} {'-' * 10}")
    for name, status, p, f, cov in results:
        marker = "OK" if status == "PASS" else "XX"
        print(f"  [{marker}] {name:<16} {status:<8} {p:<6} {f:<6} {cov}")

    print(f"\nTotal: {total_pass} passed, {total_fail} failed across {len(lp_dirs)} LPs")

    if total_fail > 0:
        print("\nSTATUS: FAIL")
        sys.exit(1)
    else:
        print("\nSTATUS: ALL GENERATORS COMPLETE")
        sys.exit(0)


if __name__ == "__main__":
    main()
