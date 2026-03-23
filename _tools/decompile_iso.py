import sys
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")
#!/usr/bin/env python3
"""CEX ISO Decompiler — decompiles existing ISO Packages into CEX LP structure.

Usage:
    python _tools/decompile_iso.py --iso records/agents/anuncio/iso_vectorstore/
    python _tools/decompile_iso.py --iso output/agents/ads/
"""

import argparse
import re
import sys
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parent.parent

# ISO file -> LP mapping (reverse of compile)
ISO_TO_LP = {
    "manifest": ("P02_model", "agent"),
    "system_instruction": ("P03_prompt", "system_prompt"),
    "instructions": ("P03_prompt", "instruction"),
    "architecture": ("P08_architecture", "pattern"),
    "output_template": ("P05_output", "output_schema"),
    "examples": ("P07_evals", "golden_test"),
    "error_handling": ("P11_feedback", "bugloop"),
    "quick_start": ("P01_knowledge", "knowledge_card"),
    "input_schema": ("P06_schema", "input_schema"),
    "upload_kit": ("P04_tools", "skill"),
    "upload_kit_whitelabel": ("P04_tools", "skill_whitelabel"),
    "system_instruction_whitelabel": ("P03_prompt", "system_prompt_whitelabel"),
}

# Patterns to identify ISO file types from legacy naming (ISO_{SAT}_{NNN}_{TYPE}.md)
LEGACY_TYPE_PATTERNS = {
    "MANIFEST": "manifest",
    "SYSTEM_INSTRUCTION": "system_instruction",
    "INSTRUCTIONS": "instructions",
    "ARCHITECTURE": "architecture",
    "OUTPUT_TEMPLATE": "output_template",
    "EXAMPLES": "examples",
    "ERROR_HANDLING": "error_handling",
    "QUICK_START": "quick_start",
    "UPLOAD_KIT_WHITELABEL": "upload_kit_whitelabel",
    "UPLOAD_KIT": "upload_kit",
    "PRIME": "instructions",  # PRIME maps to instructions
    "README": "quick_start",  # README maps to quick_start
}


def identify_file_type(filename: str) -> str | None:
    """Identify the ISO type of a file from its name."""
    name_upper = (
        filename.upper()
        .replace(".MD", "")
        .replace(".YAML", "")
        .replace(".YML", "")
        .replace(".JSON", "")
    )

    # Check canonical names first
    stem = Path(filename).stem.lower()
    if stem in ISO_TO_LP:
        return stem

    # Check legacy ISO naming: ISO_{SAT}_{NNN}_{TYPE}.md
    legacy_match = re.match(r"ISO_\w+_\d+_(.+)", name_upper)
    if legacy_match:
        type_part = legacy_match.group(1)
        # Check from longest patterns first to avoid partial matches
        for pattern in sorted(LEGACY_TYPE_PATTERNS.keys(), key=len, reverse=True):
            if type_part.startswith(pattern):
                return LEGACY_TYPE_PATTERNS[pattern]

    return None


def extract_agent_name(iso_dir: Path) -> str:
    """Extract agent name from ISO directory path."""
    # Try parent directory name (e.g., records/agents/anuncio/iso_vectorstore -> anuncio)
    if iso_dir.name == "iso_vectorstore":
        return iso_dir.parent.name

    # Use directory name directly
    return iso_dir.name


def decompile_iso(iso_dir: Path) -> bool:
    """Decompile an ISO Package into CEX LP structure."""
    if not iso_dir.exists():
        print(f"ERROR: Directory not found: {iso_dir}")
        return False

    agent_name = extract_agent_name(iso_dir)
    print(f"\nDecompiling ISO Package: {agent_name}")
    print(f"Source: {iso_dir}")

    # Scan all files
    files = [f for f in iso_dir.iterdir() if f.is_file()]
    if not files:
        print("  ERROR: No files found in ISO directory")
        return False

    classified = {}
    unclassified = []

    for f in files:
        iso_type = identify_file_type(f.name)
        if iso_type:
            classified[iso_type] = f
        else:
            unclassified.append(f)

    print(f"\n  Classified: {len(classified)} files")
    print(f"  Unclassified: {len(unclassified)} files")

    # Output to CEX LP structure
    output_base = CEX_ROOT / "output" / "decompiled" / agent_name
    decompiled_count = 0

    for iso_type, src_file in sorted(classified.items()):
        if iso_type not in ISO_TO_LP:
            print(f"  SKIP: {src_file.name} (type '{iso_type}' has no LP mapping)")
            continue

        lp_dir_name, lp_type = ISO_TO_LP[iso_type]
        target_dir = output_base / lp_dir_name / "agents" / agent_name
        target_dir.mkdir(parents=True, exist_ok=True)

        # Determine output filename
        lp_prefix = lp_dir_name.split("_")[0].lower()  # p02, p03, etc.
        ext = src_file.suffix
        target_name = f"{lp_prefix}_{lp_type}_{agent_name}{ext}"
        target_path = target_dir / target_name

        # Copy content
        content = src_file.read_bytes()
        target_path.write_bytes(content)

        print(f"  {src_file.name} -> {lp_dir_name}/agents/{agent_name}/{target_name}")
        decompiled_count += 1

    # Handle unclassified files
    if unclassified:
        extras_dir = output_base / "_extras"
        extras_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n  Unclassified files (copied to _extras/):")
        for f in unclassified:
            (extras_dir / f.name).write_bytes(f.read_bytes())
            print(f"    {f.name}")

    # Report
    print(f"\n  Decompilation report:")
    print(f"    Agent: {agent_name}")
    print(f"    Input files: {len(files)}")
    print(f"    Decompiled: {decompiled_count}")
    print(f"    Unclassified: {len(unclassified)}")
    print(f"    Output: {output_base}")

    return True


def main():
    parser = argparse.ArgumentParser(description="Decompile ISO Package into CEX LP structure")
    parser.add_argument("--iso", required=True, type=Path, help="Path to ISO package directory")
    args = parser.parse_args()

    # Resolve relative paths against CEX_ROOT
    iso_dir = args.iso
    if not iso_dir.is_absolute():
        iso_dir = CEX_ROOT / iso_dir

    success = decompile_iso(iso_dir)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
