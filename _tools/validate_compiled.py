#!/usr/bin/env python3
"""CEX Compiled Validator: checks all compiled/ files for validity and correspondence."""

import json
import sys
from pathlib import Path

import yaml

CEX_ROOT = Path(__file__).resolve().parent.parent

LP_DIRS = [
    "P01_knowledge",
    "P02_model",
    "P03_prompt",
    "P04_tools",
    "P05_output",
    "P06_schema",
    "P07_evals",
    "P08_architecture",
    "P09_config",
    "P10_memory",
    "P11_feedback",
    "P12_orchestration",
]


def load_schema_formats(lp_dir: Path) -> dict:
    """Load _schema.yaml and return type -> machine_format mapping."""
    schema_path = lp_dir / "_schema.yaml"
    if not schema_path.exists():
        return {}
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = yaml.safe_load(f)
    if not schema or "kinds" not in schema:
        return {}
    result = {}
    for type_name, type_def in schema["kinds"].items():
        if isinstance(type_def, dict) and "machine_format" in type_def:
            result[type_name] = type_def["machine_format"]
    return result


def validate_compiled_file(
    compiled_path: Path, schema_formats: dict, examples_dir: Path
) -> list[str]:
    """Validate a single compiled file. Returns list of errors (empty = valid)."""
    errors = []
    ext = compiled_path.suffix.lower()

    # 1. Parse validity
    with open(compiled_path, "r", encoding="utf-8") as f:
        content = f.read()

    data = None
    if ext == ".yaml" or ext == ".yml":
        try:
            data = yaml.safe_load(content)
        except yaml.YAMLError as e:
            errors.append(f"Invalid YAML: {e}")
            return errors
    elif ext == ".json":
        try:
            data = json.loads(content)
        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON: {e}")
            return errors
    else:
        errors.append(f"Unexpected extension: {ext}")
        return errors

    if not isinstance(data, dict):
        errors.append("Compiled file is not a dict/object")
        return errors

    # 2. Check required fields
    if "id" not in data:
        errors.append("Missing 'id' field")
    if "kind" not in data:
        errors.append("Missing 'kind' field")

    # 3. Check machine_format matches extension
    artifact_type = data.get("kind", "")
    expected_format = schema_formats.get(artifact_type, "yaml")
    expected_ext = ".json" if expected_format == "json" else ".yaml"
    if ext != expected_ext:
        errors.append(f"Format mismatch: type '{artifact_type}' expects {expected_ext}, got {ext}")

    # 4. Check corresponding .md exists in examples/
    stem = compiled_path.stem
    md_path = examples_dir / (stem + ".md")
    if not md_path.exists():
        errors.append(f"No corresponding .md in examples/ ({md_path.name})")

    return errors


def main():
    total = 0
    valid = 0
    invalid = 0
    missing_compiled = 0
    errors_list = []

    for lp_dir_name in LP_DIRS:
        lp_dir = CEX_ROOT / lp_dir_name
        if not lp_dir.exists():
            continue

        compiled_dir = lp_dir / "compiled"
        examples_dir = lp_dir / "examples"
        schema_formats = load_schema_formats(lp_dir)

        # Check compiled files
        compiled_files = []
        if compiled_dir.exists():
            compiled_files = sorted(
                list(compiled_dir.glob("*.yaml"))
                + list(compiled_dir.glob("*.yml"))
                + list(compiled_dir.glob("*.json"))
            )

        lp_code = lp_dir_name.split("_")[0]

        for cf in compiled_files:
            total += 1
            errs = validate_compiled_file(cf, schema_formats, examples_dir)
            if errs:
                invalid += 1
                for e in errs:
                    errors_list.append(f"  {lp_code}/{cf.name}: {e}")
            else:
                valid += 1

        # Check for examples without compiled counterpart
        if examples_dir.exists():
            for md_file in sorted(examples_dir.glob("*.md")):
                stem = md_file.stem
                has_compiled = (compiled_dir / (stem + ".yaml")).exists() or (
                    compiled_dir / (stem + ".json")
                ).exists()
                if not has_compiled:
                    missing_compiled += 1
                    errors_list.append(f"  {lp_code}/{md_file.name}: no compiled output found")

    # Report
    print("=" * 50)
    print("CEX Compiled Validation Report")
    print("=" * 50)
    print(f"Total compiled files:  {total}")
    print(f"Valid:                 {valid}")
    print(f"Invalid:               {invalid}")
    print(f"Missing compiled:      {missing_compiled}")
    print("=" * 50)

    if errors_list:
        print("\nErrors:")
        for e in errors_list:
            print(e)
        sys.exit(1)
    else:
        print("\nAll checks passed!")


if __name__ == "__main__":
    main()
