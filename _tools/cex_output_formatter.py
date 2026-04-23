#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Output Formatter -- validate and fix LLM output against kind schemas.

Uses jsonschema to validate frontmatter against pillar schemas.
Auto-fixes common issues (missing quality:null, wrong types, missing fields).
Integrates into F7 GOVERN for stronger validation.

Usage:
    python cex_output_formatter.py --validate path/to/artifact.md
    python cex_output_formatter.py --fix path/to/artifact.md
    python cex_output_formatter.py --schema agent    # Show schema for kind
    python cex_output_formatter.py --batch N03       # Validate all in nucleus
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_shared import load_yaml, parse_frontmatter

CEX_ROOT = Path(__file__).resolve().parent.parent
KINDS_META = CEX_ROOT / ".cex" / "kinds_meta.json"

try:
    import jsonschema
    _JSONSCHEMA_AVAILABLE = True
except ImportError:
    _JSONSCHEMA_AVAILABLE = False


# ---------------------------------------------------------------------------
# Schema Loading
# ---------------------------------------------------------------------------


def load_kinds_meta() -> dict:
    """Load the kinds metadata registry."""
    if not KINDS_META.exists():
        return {}
    return json.loads(KINDS_META.read_text(encoding="utf-8"))


def load_pillar_schema(pillar: str) -> dict:
    """Load _schema.yaml for a pillar."""
    for d in CEX_ROOT.glob(f"{pillar}_*"):
        if d.is_dir():
            schema_path = d / "_schema.yaml"
            if schema_path.exists():
                return load_yaml(schema_path)
    return {}


def get_kind_constraints(kind: str) -> dict:
    """Get validation constraints for a kind from kinds_meta + pillar schema."""
    meta = load_kinds_meta()
    kind_meta = meta.get(kind, {})

    pillar = kind_meta.get("pillar", "")
    pillar_schema = load_pillar_schema(pillar)
    kind_schema = pillar_schema.get("kinds", {}).get(kind, {})

    return {
        "pillar": pillar,
        "max_bytes": kind_meta.get("max_bytes", 5120),
        "naming": kind_meta.get("naming", ""),
        "boundary": kind_meta.get("boundary", ""),
        "llm_function": kind_meta.get("llm_function", ""),
        "id_pattern": kind_schema.get("id_pattern", ""),
        "required_fields": kind_schema.get("frontmatter_required", [
            "id", "kind", "pillar", "title", "version", "quality",
        ]),
    }


# ---------------------------------------------------------------------------
# Frontmatter Validation
# ---------------------------------------------------------------------------

# Universal rules that apply to ALL kinds
UNIVERSAL_RULES = [
    ("quality_null", "quality must be null", lambda fm: fm.get("quality") is None),
    ("has_id", "id field required", lambda fm: bool(fm.get("id"))),
    ("has_kind", "kind field required", lambda fm: bool(fm.get("kind"))),
    ("has_pillar", "pillar field required", lambda fm: bool(fm.get("pillar"))),
    ("has_title", "title field required", lambda fm: bool(fm.get("title"))),
]


def validate_frontmatter(fm: dict, kind: str) -> list[dict]:
    """Validate frontmatter against universal + kind-specific rules.

    Returns list of {rule, message, passed} dicts.
    """
    results = []

    # Universal rules
    for rule_id, message, check in UNIVERSAL_RULES:
        passed = check(fm)
        results.append({"rule": rule_id, "message": message, "passed": passed})

    # Kind-specific rules
    constraints = get_kind_constraints(kind)

    # ID pattern check
    id_pattern = constraints.get("id_pattern")
    if id_pattern and fm.get("id"):
        matched = bool(re.match(id_pattern, str(fm["id"])))
        results.append({
            "rule": "id_pattern",
            "message": f"id must match /{id_pattern}/",
            "passed": matched,
        })

    # Required fields
    for field in constraints.get("required_fields", []):
        results.append({
            "rule": f"field_{field}",
            "message": f"required field: {field}",
            "passed": field in fm,
        })

    # Kind match
    if fm.get("kind") and fm["kind"] != kind:
        results.append({
            "rule": "kind_match",
            "message": f"kind should be '{kind}', got '{fm['kind']}'",
            "passed": False,
        })

    return results


def validate_body(body: str, kind: str) -> list[dict]:
    """Validate artifact body structure."""
    results = []
    constraints = get_kind_constraints(kind)

    # Size check
    body_bytes = len(body.encode("utf-8"))
    max_bytes = constraints.get("max_bytes", 5120)
    results.append({
        "rule": "body_size",
        "message": f"body size {body_bytes}B <= {max_bytes}B max",
        "passed": body_bytes <= max_bytes,
    })

    # Section check
    sections = re.findall(r"^#{1,3}\s+\S", body, re.MULTILINE)
    results.append({
        "rule": "has_sections",
        "message": f"body has {len(sections)} section(s)",
        "passed": len(sections) >= 1,
    })

    # Non-empty body
    results.append({
        "rule": "body_nonempty",
        "message": "body is not empty",
        "passed": len(body.strip()) > 50,
    })

    return results


# ---------------------------------------------------------------------------
# jsonschema Validation
# ---------------------------------------------------------------------------


def build_jsonschema(kind: str) -> dict:
    """Build a JSON Schema for a kind's frontmatter."""
    constraints = get_kind_constraints(kind)

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "kind": {"type": "string", "const": kind},
            "pillar": {"type": "string", "pattern": r"^P\d{2}$"},
            "title": {"type": "string", "minLength": 3},
            "version": {"type": "string", "pattern": r"^\d+\.\d+\.\d+$"},
            "quality": {"type": "null"},
        },
        "required": constraints.get("required_fields", ["id", "kind", "pillar", "title", "quality"]),
    }

    id_pattern = constraints.get("id_pattern")
    if id_pattern:
        schema["properties"]["id"]["pattern"] = id_pattern

    return schema


def validate_with_jsonschema(fm: dict, kind: str) -> list[dict]:
    """Validate frontmatter using jsonschema library."""
    if not _JSONSCHEMA_AVAILABLE:
        return [{"rule": "jsonschema", "message": "jsonschema not installed", "passed": True}]

    schema = build_jsonschema(kind)
    validator = jsonschema.Draft7Validator(schema)
    errors = list(validator.iter_errors(fm))

    results = []
    if not errors:
        results.append({"rule": "jsonschema", "message": "Schema valid", "passed": True})
    else:
        for err in errors:
            path = ".".join(str(p) for p in err.absolute_path) if err.absolute_path else "root"
            results.append({
                "rule": f"jsonschema_{path}",
                "message": f"{path}: {err.message}",
                "passed": False,
            })

    return results


# ---------------------------------------------------------------------------
# Full Validation
# ---------------------------------------------------------------------------


def validate_artifact(filepath: Path) -> dict:
    """Full validation of an artifact file. Returns summary dict."""
    text = filepath.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if not fm:
        return {
            "path": str(filepath),
            "valid": False,
            "results": [{"rule": "parse", "message": "Cannot parse frontmatter", "passed": False}],
        }

    kind = fm.get("kind", "unknown")

    # Strip frontmatter for body validation
    body = text
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            body = text[end + 3:].strip()

    results = []
    results.extend(validate_frontmatter(fm, kind))
    results.extend(validate_body(body, kind))
    results.extend(validate_with_jsonschema(fm, kind))

    passed = sum(1 for r in results if r["passed"])
    failed = [r for r in results if not r["passed"]]

    return {
        "path": str(filepath),
        "kind": kind,
        "valid": len(failed) == 0,
        "passed": passed,
        "total": len(results),
        "results": results,
        "failures": [r["message"] for r in failed],
    }


# ---------------------------------------------------------------------------
# Auto-Fix
# ---------------------------------------------------------------------------


def auto_fix_frontmatter(text: str) -> tuple[str, list[str]]:
    """Auto-fix common frontmatter issues. Returns (fixed_text, list_of_fixes)."""
    fixes = []
    fm = parse_frontmatter(text)
    if not fm:
        return text, ["Cannot parse frontmatter -- manual fix needed"]

    lines = text.split("\n")
    # Find frontmatter boundaries
    if not lines[0].startswith("---"):
        return text, []

    end_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx < 0:
        return text, []

    fm_lines = lines[1:end_idx]
    changed = False

    # Fix 1: quality must be null
    quality_val = fm.get("quality")
    if quality_val is not None:
        for j, line in enumerate(fm_lines):
            if line.startswith("quality:"):
                fm_lines[j] = "quality: null"
                fixes.append(f"quality: {quality_val} -> null")
                changed = True
                break

    # Fix 2: Add missing quality field
    if "quality" not in fm:
        fm_lines.append("quality: null")
        fixes.append("added quality: null")
        changed = True

    # Fix 3: version format
    version = fm.get("version", "")
    if version and not re.match(r"^\d+\.\d+\.\d+$", str(version)):
        for j, line in enumerate(fm_lines):
            if line.startswith("version:"):
                fm_lines[j] = "version: 1.0.0"
                fixes.append(f"version: {version} -> 1.0.0")
                changed = True
                break

    if changed:
        result = ["---"] + fm_lines + ["---"] + lines[end_idx + 1:]
        return "\n".join(result), fixes
    return text, []


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="CEX Output Formatter -- validate & fix artifacts")
    parser.add_argument("--validate", "-v", help="Validate artifact file")
    parser.add_argument("--fix", help="Auto-fix artifact file")
    parser.add_argument("--schema", help="Show JSON Schema for a kind")
    parser.add_argument("--batch", help="Validate all artifacts in a nucleus (e.g. N03)")
    args = parser.parse_args()

    if args.validate:
        result = validate_artifact(Path(args.validate))
        print(f"\n=== Validation: {result['path']} ===")
        print(f"  Kind:   {result.get('kind', '?')}")
        print(f"  Status: {'VALID' if result['valid'] else 'INVALID'}")
        print(f"  Checks: {result['passed']}/{result['total']} passed")

        if result.get("failures"):
            print("\n  Failures:")
            for f in result["failures"]:
                print(f"    - {f}")
        return

    if args.fix:
        p = Path(args.fix)
        text = p.read_text(encoding="utf-8")
        fixed, fixes = auto_fix_frontmatter(text)
        if fixes:
            p.write_text(fixed, encoding="utf-8")
            print(f"  Fixed {len(fixes)} issue(s) in {p.name}:")
            for f in fixes:
                print(f"    - {f}")
        else:
            print(f"  No fixes needed for {p.name}")
        return

    if args.schema:
        schema = build_jsonschema(args.schema)
        print(json.dumps(schema, indent=2))
        return

    if args.batch:
        nuc_map = {
            "N01": "N01_intelligence", "N02": "N02_marketing", "N03": "N03_engineering",
            "N04": "N04_knowledge", "N05": "N05_operations", "N06": "N06_commercial",
            "N07": "N07_admin",
        }
        nuc_dir = CEX_ROOT / nuc_map.get(args.batch.upper(), "")
        if not nuc_dir.exists():
            print(f"Nucleus directory not found: {nuc_dir}")
            sys.exit(1)

        results = []
        for md in sorted(nuc_dir.rglob("*.md")):
            if md.name.startswith("README") or "_schema" in md.name or "compiled" in str(md):
                continue
            fm = parse_frontmatter(md.read_text(encoding="utf-8"))
            if not fm or "kind" not in fm:
                continue
            result = validate_artifact(md)
            results.append(result)

        valid = sum(1 for r in results if r["valid"])
        print(f"\n=== Batch Validation: {args.batch} ({len(results)} artifacts) ===")
        print(f"  Valid:   {valid}/{len(results)} ({valid / len(results):.0%})" if results else "  No artifacts found")

        invalid = [r for r in results if not r["valid"]]
        if invalid:
            print(f"\n  Invalid ({len(invalid)}):")
            for r in invalid[:20]:
                print(f"    {r['kind']:20s} {r['path']}")
                for f in r["failures"][:3]:
                    print(f"      - {f}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
