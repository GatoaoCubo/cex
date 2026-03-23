#!/usr/bin/env python3
"""CEX ISO Validator — validates ISO Packages for completeness and quality.

Usage:
    python _tools/validate_iso.py --iso agents/anuncio/
    python _tools/validate_iso.py --iso output/agents/ads/
    python _tools/validate_iso.py --iso records/agents/anuncio/iso_vectorstore/ --codexa-core ../codexa-core
"""

import argparse
import re
import sys
from pathlib import Path

import yaml

CEX_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = {"manifest.yaml", "system_instruction.md", "instructions.md"}
RECOMMENDED_FILES = {"architecture.md", "output_template.md", "examples.md", "error_handling.md"}
OPTIONAL_FILES = {
    "quick_start.md",
    "input_schema.yaml",
    "upload_kit.md",
    "upload_kit_whitelabel.md",
}
ALL_KNOWN_FILES = REQUIRED_FILES | RECOMMENDED_FILES | OPTIONAL_FILES

HARDCODED_PATH_PATTERNS = [
    (r"[A-Z]:\\", "Windows absolute path"),
    (r"/home/\w+", "Linux home directory"),
    (r"/Users/\w+", "macOS home directory"),
    (r"/tmp/\w+", "Temp directory"),
]

# Legacy ISO naming: ISO_{SAT}_{NNN}_{TYPE}.md
LEGACY_TYPE_MAP = {
    "MANIFEST": "manifest.yaml",
    "SYSTEM_INSTRUCTION_WHITELABEL": "system_instruction_whitelabel.md",
    "SYSTEM_INSTRUCTION": "system_instruction.md",
    "INSTRUCTIONS": "instructions.md",
    "ARCHITECTURE": "architecture.md",
    "OUTPUT_TEMPLATE": "output_template.md",
    "EXAMPLES": "examples.md",
    "ERROR_HANDLING": "error_handling.md",
    "QUICK_START": "quick_start.md",
    "UPLOAD_KIT_WHITELABEL": "upload_kit_whitelabel.md",
    "UPLOAD_KIT": "upload_kit.md",
    "PRIME": "instructions.md",
    "README": "quick_start.md",
}

MANIFEST_REQUIRED_FIELDS = {"id", "version", "type", "title", "description"}


def estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token."""
    return len(text) // 4


def calculate_density(text: str) -> float:
    """Information density: ratio of non-empty lines to total lines."""
    if not text.strip():
        return 0.0
    lines = text.strip().split("\n")
    non_empty = [line for line in lines if line.strip()]
    return len(non_empty) / len(lines) if lines else 0.0


def map_legacy_to_canonical(filename: str) -> str | None:
    """Map legacy ISO naming to canonical file name."""
    upper = filename.upper().replace(".MD", "").replace(".YAML", "").replace(".YML", "")
    match = re.match(r"ISO_\w+_\d+_(.+)", upper)
    if match:
        type_part = match.group(1)
        for pattern in sorted(LEGACY_TYPE_MAP.keys(), key=len, reverse=True):
            if type_part.startswith(pattern):
                return LEGACY_TYPE_MAP[pattern]
    return None


def classify_tier(present_canonical: set[str]) -> str:
    """Classify package tier based on present canonical files."""
    has_required = REQUIRED_FILES.issubset(present_canonical)
    has_recommended = RECOMMENDED_FILES.issubset(present_canonical)
    has_whitelabel = any("whitelabel" in f for f in present_canonical)

    if has_whitelabel and len(present_canonical) >= 12:
        return "whitelabel"
    if has_required and has_recommended and len(present_canonical) >= 10:
        return "complete"
    if has_required and has_recommended:
        return "standard"
    if has_required:
        return "minimal"
    return "incomplete"


def calculate_portability_score(issues: list[dict]) -> int:
    """Calculate portability score 0-100 based on issues."""
    score = 100
    for issue in issues:
        if issue["severity"] == "error":
            score -= 20
        elif issue["severity"] == "warning":
            score -= 5
        elif issue["severity"] == "info":
            score -= 1
    return max(0, score)


def validate_iso(iso_dir: Path) -> dict:
    """Validate an ISO Package directory. Returns validation report."""
    report = {
        "agent": iso_dir.name if iso_dir.name != "iso_vectorstore" else iso_dir.parent.name,
        "path": str(iso_dir),
        "files_total": 0,
        "files_canonical": {},
        "tier": "incomplete",
        "issues": [],
        "portability_score": 0,
        "passed": False,
    }

    if not iso_dir.exists():
        report["issues"].append(
            {
                "severity": "error",
                "file": str(iso_dir),
                "message": "Directory not found",
            }
        )
        return report

    # Scan files
    all_files = [f for f in iso_dir.iterdir() if f.is_file()]
    report["files_total"] = len(all_files)

    # Map files to canonical names
    canonical_present = set()
    file_map = {}

    for f in all_files:
        # Check if it's already canonical
        if f.name in ALL_KNOWN_FILES:
            canonical_present.add(f.name)
            file_map[f.name] = f
        else:
            # Try legacy mapping
            canonical = map_legacy_to_canonical(f.name)
            if canonical:
                canonical_present.add(canonical)
                file_map[canonical] = f

    report["files_canonical"] = {k: v.name for k, v in sorted(file_map.items())}

    # Check required files
    for req in sorted(REQUIRED_FILES):
        if req not in canonical_present:
            report["issues"].append(
                {
                    "severity": "error",
                    "file": req,
                    "message": f"Required file missing: {req}",
                }
            )

    # Check recommended files
    for rec in sorted(RECOMMENDED_FILES):
        if rec not in canonical_present:
            report["issues"].append(
                {
                    "severity": "warning",
                    "file": rec,
                    "message": f"Recommended file missing: {rec}",
                }
            )

    # Validate manifest.yaml
    manifest_file = file_map.get("manifest.yaml")
    if manifest_file:
        try:
            with open(manifest_file, "r", encoding="utf-8") as mf:
                manifest_data = yaml.safe_load(mf)
            if isinstance(manifest_data, dict):
                for field in MANIFEST_REQUIRED_FIELDS:
                    if field not in manifest_data:
                        report["issues"].append(
                            {
                                "severity": "error",
                                "file": manifest_file.name,
                                "message": f"Manifest missing required field: {field}",
                            }
                        )
            else:
                report["issues"].append(
                    {
                        "severity": "error",
                        "file": manifest_file.name,
                        "message": "Manifest is not a valid YAML dict",
                    }
                )
        except Exception as e:
            report["issues"].append(
                {
                    "severity": "error",
                    "file": manifest_file.name,
                    "message": f"Manifest parse error: {e}",
                }
            )

    # Validate system_instruction.md token count
    sys_instr_file = file_map.get("system_instruction.md")
    if sys_instr_file:
        content = sys_instr_file.read_text(encoding="utf-8")
        tokens = estimate_tokens(content)
        if tokens > 4096:
            report["issues"].append(
                {
                    "severity": "warning",
                    "file": sys_instr_file.name,
                    "message": f"System instruction has {tokens} tokens (max recommended: 4096)",
                }
            )

    # Validate density and hardcoded paths in all .md files
    for canonical_name, actual_file in file_map.items():
        if actual_file.suffix not in (".md",):
            continue

        content = actual_file.read_text(encoding="utf-8")

        # Density check
        density = calculate_density(content)
        if density < 0.8:
            report["issues"].append(
                {
                    "severity": "warning",
                    "file": actual_file.name,
                    "message": f"Density {density:.2f} below threshold 0.80",
                }
            )

        # Hardcoded paths
        for pattern, desc in HARDCODED_PATH_PATTERNS:
            matches = re.findall(pattern, content)
            if matches:
                report["issues"].append(
                    {
                        "severity": "warning",
                        "file": actual_file.name,
                        "message": f"Hardcoded {desc} found: {matches[0]}",
                    }
                )

    # Check examples count
    examples_file = file_map.get("examples.md")
    if examples_file:
        content = examples_file.read_text(encoding="utf-8")
        # Count example sections (## Example, ### Example, **Example**, etc.)
        example_count = len(
            re.findall(r"(?i)(#{1,3}\s*example|input\s*[:/]|example\s*\d)", content)
        )
        if example_count < 2:
            report["issues"].append(
                {
                    "severity": "warning",
                    "file": examples_file.name,
                    "message": f"Only ~{example_count} examples found (min recommended: 2)",
                }
            )

    # Classify tier
    report["tier"] = classify_tier(canonical_present)

    # Portability score
    report["portability_score"] = calculate_portability_score(report["issues"])

    # Overall pass/fail
    errors = [i for i in report["issues"] if i["severity"] == "error"]
    report["passed"] = len(errors) == 0

    return report


def print_report(report: dict) -> None:
    """Pretty-print a validation report."""
    status = "PASS" if report["passed"] else "FAIL"
    print(f"\n{'=' * 60}")
    print(f"ISO Package Validation: {report['agent']}")
    print(f"{'=' * 60}")
    print(f"  Path: {report['path']}")
    print(f"  Total files: {report['files_total']}")
    print(f"  Tier: {report['tier']}")
    print(f"  Portability: {report['portability_score']}/100")

    if report["files_canonical"]:
        print(f"\n  Canonical mapping:")
        for canonical, actual in report["files_canonical"].items():
            marker = (
                "R"
                if canonical in REQUIRED_FILES
                else ("~" if canonical in RECOMMENDED_FILES else "O")
            )
            print(f"    [{marker}] {canonical} <- {actual}")

    if report["issues"]:
        print(f"\n  Issues ({len(report['issues'])}):")
        for issue in report["issues"]:
            icon = {"error": "XX", "warning": "!!", "info": "--"}[issue["severity"]]
            print(f"    [{icon}] {issue['file']}: {issue['message']}")

    print(f"\n  Status: {status}")
    print(f"{'=' * 60}")


def main():
    parser = argparse.ArgumentParser(
        description="Validate ISO Package for completeness and quality"
    )
    parser.add_argument("--iso", required=True, type=Path, help="Path to ISO package directory")
    args = parser.parse_args()

    iso_dir = args.iso
    if not iso_dir.is_absolute():
        iso_dir = CEX_ROOT / iso_dir

    report = validate_iso(iso_dir)
    print_report(report)

    sys.exit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
