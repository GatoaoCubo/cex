#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Schema Validator -- validates each P*/_schema.yaml for structural integrity."""

import sys

if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")
from pathlib import Path

import yaml

CEX_ROOT = Path(__file__).resolve().parent.parent
REQUIRED_TOP = {"lp", "name", "description"}
REQUIRED_TYPE_FIELDS = {"description", "naming", "constraints"}


def load_schema(path: Path) -> dict | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"  ERROR: Cannot parse {path}: {e}")
        return None


def validate_schema(lp_dir: Path) -> tuple[int, int]:
    schema_path = lp_dir / "_schema.yaml"
    lp_name = lp_dir.name
    passes = 0
    fails = 0

    if not schema_path.exists():
        print(f"  FAIL: {lp_name}/_schema.yaml not found")
        return 0, 1

    data = load_schema(schema_path)
    if data is None:
        return 0, 1

    # Check top-level required fields
    for field in REQUIRED_TOP:
        if field in data:
            passes += 1
        else:
            print(f"  FAIL: {lp_name} missing top-level field '{field}'")
            fails += 1

    # Check lp matches directory
    if "lp" in data:
        expected_lp = lp_name.split("_")[0]  # P01, P02, etc.
        if data["pillar"] != expected_lp:
            print(f"  FAIL: {lp_name} lp='{data['pillar']}' != expected '{expected_lp}'")
            fails += 1
        else:
            passes += 1

    # Check types section
    types = data.get("kinds")
    if not types or not isinstance(types, dict):
        print(f"  FAIL: {lp_name} missing or empty 'kinds' section")
        return passes, fails + 1

    for type_name, type_def in types.items():
        if not isinstance(type_def, dict):
            print(f"  FAIL: {lp_name}.{type_name} is not a dict")
            fails += 1
            continue

        # Check naming
        if "naming" in type_def:
            naming = type_def["naming"]
            lp_lower = data.get("pillar", "").lower()
            # agent_package and similar portable types use external paths (e.g. agents/)
            is_external_naming = type_name in ("agent_package",) or naming.startswith("agents/")
            if not naming.startswith(lp_lower) and not is_external_naming:
                print(
                    f"  FAIL: {lp_name}.{type_name} naming '{naming}'"
                    f" doesn't start with '{lp_lower}'"
                )
                fails += 1
            else:
                passes += 1
        else:
            print(f"  FAIL: {lp_name}.{type_name} missing 'naming'")
            fails += 1

        # Check description
        if "description" in type_def:
            if len(type_def["description"]) < 5:
                print(f"  FAIL: {lp_name}.{type_name} description too short")
                fails += 1
            else:
                passes += 1
        else:
            print(f"  FAIL: {lp_name}.{type_name} missing 'description'")
            fails += 1

        # Check constraints
        constraints = type_def.get("constraints")
        if constraints:
            if isinstance(constraints, dict) and "max_bytes" in constraints:
                passes += 1
            else:
                print(f"  FAIL: {lp_name}.{type_name} constraints missing 'max_bytes'")
                fails += 1
        else:
            print(f"  FAIL: {lp_name}.{type_name} missing 'constraints'")
            fails += 1

    return passes, fails


def main():
    print("=" * 60)
    print("CEX Schema Validator")
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
        p, f = validate_schema(lp_dir)
        total_pass += p
        total_fail += f
        status = "PASS" if f == 0 else "FAIL"
        results.append((lp_dir.name, status, p, f))
        print(f"  Result: {status} ({p} passed, {f} failed)")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for name, status, p, f in results:
        marker = "OK" if status == "PASS" else "XX"
        print(f"  [{marker}] {name}: {p} passed, {f} failed")

    print(f"\nTotal: {total_pass} passed, {total_fail} failed across {len(lp_dirs)} LPs")

    if total_fail > 0:
        print("\nSTATUS: FAIL")
        sys.exit(1)
    else:
        print("\nSTATUS: PASS")
        sys.exit(0)


if __name__ == "__main__":
    main()
