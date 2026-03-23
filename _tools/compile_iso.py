#!/usr/bin/env python3
"""CEX ISO Compiler — compiles CEX LP sources into a portable ISO Package.

Usage:
    python _tools/compile_iso.py --agent ads --source ./P02_model/agents/ads/
    python _tools/compile_iso.py --agent ads  # auto-discovers from LP dirs
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

import yaml

CEX_ROOT = Path(__file__).resolve().parent.parent

# LP directory -> ISO file mapping
LP_FILE_MAP = {
    "P02_model": ("manifest.yaml", "agent definition"),
    "P03_prompt": ("system_instruction.md", "system prompt"),
    "P05_output": ("output_template.md", "output schema"),
    "P06_schema": ("input_schema.yaml", "input schema"),
    "P07_evals": ("examples.md", "examples"),
    "P08_architecture": ("architecture.md", "architecture"),
    "P11_feedback": ("error_handling.md", "error handling"),
}

HARDCODED_PATH_PATTERNS = [
    r"[A-Z]:\\",  # Windows absolute paths
    r"/home/\w+",  # Linux home dirs
    r"/Users/\w+",  # macOS home dirs
    r"/tmp/\w+",  # temp dirs
]

REQUIRED_FILES = {"manifest.yaml", "system_instruction.md", "instructions.md"}
RECOMMENDED_FILES = {"architecture.md", "output_template.md", "examples.md", "error_handling.md"}
OPTIONAL_FILES = {
    "quick_start.md",
    "input_schema.yaml",
    "upload_kit.md",
    "upload_kit_whitelabel.md",
}


def find_agent_sources(agent_name: str) -> dict[str, Path]:
    """Auto-discover agent files across LP directories."""
    sources = {}

    for lp_dir_name, (iso_name, desc) in LP_FILE_MAP.items():
        lp_dir = CEX_ROOT / lp_dir_name
        if not lp_dir.exists():
            continue

        # Search for agent-specific files
        candidates = list(lp_dir.rglob(f"*{agent_name}*"))
        if candidates:
            # Prefer .md or .yaml files
            best = None
            for c in candidates:
                if c.suffix in (".md", ".yaml", ".yml"):
                    best = c
                    break
            sources[iso_name] = best or candidates[0]

    return sources


def estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token for English/mixed content."""
    return len(text) // 4


def calculate_density(text: str) -> float:
    """Calculate information density (non-whitespace ratio, adjusted)."""
    if not text.strip():
        return 0.0
    lines = text.strip().split("\n")
    non_empty = [line for line in lines if line.strip()]
    if not lines:
        return 0.0
    return len(non_empty) / len(lines)


def check_hardcoded_paths(text: str) -> list[str]:
    """Scan for hardcoded absolute paths."""
    violations = []
    for pattern in HARDCODED_PATH_PATTERNS:
        matches = re.findall(pattern, text)
        for m in matches:
            violations.append(m)
    return violations


def classify_tier(files: set[str]) -> str:
    """Classify ISO Package tier based on present files."""
    has_required = REQUIRED_FILES.issubset(files)
    has_recommended = RECOMMENDED_FILES.issubset(files)
    has_optional = OPTIONAL_FILES.intersection(files)
    has_whitelabel = any("whitelabel" in f for f in files)

    if has_whitelabel and len(files) >= 12:
        return "whitelabel"
    if has_required and has_recommended and len(has_optional) >= 2:
        return "complete"
    if has_required and has_recommended:
        return "standard"
    if has_required:
        return "minimal"
    return "incomplete"


def generate_manifest(agent_name: str, files: set[str], tier: str) -> str:
    """Generate a manifest.yaml for the ISO Package."""
    manifest = {
        "id": agent_name,
        "version": "1.0.0",
        "type": "iso_package",
        "title": agent_name.replace("-", " ").replace("_", " ").title(),
        "description": f"ISO Package for {agent_name} agent",
        "domain": "general",
        "quality": 8.0,
        "tier": tier,
        "capabilities": [],
        "target_llms": ["claude", "gpt4", "gemini", "llama"],
        "min_context": 8192,
        "tools_required": [],
        "variables": {},
        "tags": [agent_name],
        "files": sorted(files),
        "created": "2026-03-23",
        "updated": "2026-03-23",
    }
    return yaml.dump(manifest, default_flow_style=False, allow_unicode=True, sort_keys=False)


def compile_agent(agent_name: str, source_dir: Path | None = None) -> bool:
    """Compile an agent into ISO Package format."""
    output_dir = CEX_ROOT / "output" / "agents" / agent_name
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nCompiling ISO Package: {agent_name}")
    print(f"Output: {output_dir}")

    compiled_files = set()
    issues = []

    if source_dir and source_dir.exists():
        # Copy all files from source directory
        for src_file in source_dir.iterdir():
            if src_file.is_file():
                dst = output_dir / src_file.name
                shutil.copy2(src_file, dst)
                compiled_files.add(src_file.name)
                print(f"  + {src_file.name} (from source)")
    else:
        # Auto-discover from LP directories
        sources = find_agent_sources(agent_name)
        if not sources:
            print(f"  ERROR: No sources found for agent '{agent_name}'")
            return False

        for iso_name, src_path in sources.items():
            dst = output_dir / iso_name
            shutil.copy2(src_path, dst)
            compiled_files.add(iso_name)
            print(f"  + {iso_name} <- {src_path.relative_to(CEX_ROOT)}")

    # Generate instructions.md if missing
    if "instructions.md" not in compiled_files:
        instructions = f"# {agent_name} — Instructions\n\n"
        instructions += "## When to Use\n\nUse this agent when you need specialized assistance.\n\n"
        instructions += "## How to Use\n\n1. Provide input as described in the manifest\n"
        instructions += "2. Review the output against the output template\n"
        instructions += "3. Iterate if needed\n"
        (output_dir / "instructions.md").write_text(instructions, encoding="utf-8")
        compiled_files.add("instructions.md")
        print("  + instructions.md (generated)")

    # Classify tier
    tier = classify_tier(compiled_files)

    # Generate manifest if missing
    if "manifest.yaml" not in compiled_files:
        manifest_content = generate_manifest(agent_name, compiled_files, tier)
        (output_dir / "manifest.yaml").write_text(manifest_content, encoding="utf-8")
        compiled_files.add("manifest.yaml")
        print("  + manifest.yaml (generated)")

    # Validate all .md files
    for fname in compiled_files:
        fpath = output_dir / fname
        if fpath.suffix == ".md":
            content = fpath.read_text(encoding="utf-8")
            tokens = estimate_tokens(content)
            density = calculate_density(content)
            paths = check_hardcoded_paths(content)

            if fname == "system_instruction.md" and tokens > 4096:
                issues.append(f"  WARN: {fname} has {tokens} tokens (max 4096)")
            if density < 0.8:
                issues.append(f"  WARN: {fname} density {density:.2f} (min 0.8)")
            if paths:
                issues.append(f"  WARN: {fname} has hardcoded paths: {paths}")

    # Report
    missing_required = REQUIRED_FILES - compiled_files
    if missing_required:
        issues.append(f"  FAIL: Missing required files: {missing_required}")

    print(f"\n  Tier: {tier}")
    print(f"  Files: {len(compiled_files)}")

    if issues:
        print("\n  Issues:")
        for issue in issues:
            print(f"    {issue}")

    status = "OK" if not missing_required else "INCOMPLETE"
    print(
        f"\n  ISO Package compiled: {agent_name} | {len(compiled_files)} files | {tier} | {status}"
    )
    return len(missing_required) == 0


def main():
    parser = argparse.ArgumentParser(description="Compile CEX LP sources into ISO Package")
    parser.add_argument("--agent", required=True, help="Agent name (e.g., ads, anuncio)")
    parser.add_argument("--source", type=Path, help="Source directory (auto-discovers if omitted)")
    args = parser.parse_args()

    success = compile_agent(args.agent, args.source)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
