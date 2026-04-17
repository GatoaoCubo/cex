#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Compiler: converts .md examples to compiled YAML/JSON for LLM consumption."""

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_shared import split_frontmatter as _shared_split_frontmatter


class CEXEncoder(json.JSONEncoder):
    """JSON encoder that handles date/datetime from YAML frontmatter."""

    def default(self, o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        return super().default(o)


CEX_ROOT = Path(__file__).resolve().parent.parent

LP_DIRS = [
    "N00_genesis/P01_knowledge",
    "N00_genesis/P02_model",
    "N00_genesis/P03_prompt",
    "N00_genesis/P04_tools",
    "N00_genesis/P05_output",
    "N00_genesis/P06_schema",
    "N00_genesis/P07_evals",
    "N00_genesis/P08_architecture",
    "N00_genesis/P09_config",
    "N00_genesis/P10_memory",
    "N00_genesis/P11_feedback",
    "N00_genesis/P12_orchestration",
]


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from markdown text."""
    return _shared_split_frontmatter(text)


def load_schema(lp_dir: Path) -> dict:
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


def strip_markdown_decoration(text: str) -> str:
    """Remove bold, italic, links -- keep the text content."""
    # Links: [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Bold+italic: ***text*** or ___text___
    text = re.sub(r"\*{3}(.+?)\*{3}", r"\1", text)
    text = re.sub(r"_{3}(.+?)_{3}", r"\1", text)
    # Bold: **text** or __text__
    text = re.sub(r"\*{2}(.+?)\*{2}", r"\1", text)
    text = re.sub(r"_{2}(.+?)_{2}", r"\1", text)
    # Italic: *text* or _text_ (careful not to match mid-word underscores)
    text = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"\1", text)
    text = re.sub(r"(?<!\w)_(.+?)_(?!\w)", r"\1", text)
    return text


def normalize_key(header: str) -> str:
    """Convert markdown header text to a YAML key."""
    # Remove markdown decoration
    header = strip_markdown_decoration(header)
    # Lowercase, strip, replace spaces/special with underscore
    key = header.strip().lower()
    key = re.sub(r"[^a-z0-9]+", "_", key)
    key = key.strip("_")
    return key


def parse_body_sections(body: str) -> dict:
    """Parse markdown body into structured sections keyed by header."""
    sections = {}
    current_key = None
    current_lines = []
    in_code_block = False
    first_h1_skipped = False

    for line in body.split("\n"):
        stripped = line.strip()

        # Track code blocks -- don't parse headers inside them
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            current_lines.append(line)
            continue

        if in_code_block:
            current_lines.append(line)
            continue

        # Match ## or ### headers (content sections)
        header_match = re.match(r"^(#{1,3})\s+(.+)$", line)
        if header_match:
            level = len(header_match.group(1))
            # Skip the first # header (document title, duplicates frontmatter)
            if level == 1 and not first_h1_skipped:
                first_h1_skipped = True
                continue
            # Save previous section
            if current_key is not None:
                sections[current_key] = process_section_content("\n".join(current_lines))
            current_key = normalize_key(header_match.group(2))
            current_lines = []
        else:
            current_lines.append(line)

    # Save last section
    if current_key is not None:
        sections[current_key] = process_section_content("\n".join(current_lines))

    return sections


def process_section_content(content: str) -> object:
    """Process a section's content -- detect lists, code blocks, or plain text."""
    content = content.strip()
    if not content:
        return ""

    content = strip_markdown_decoration(content)

    # Check if content is primarily a numbered or bulleted list
    lines = content.split("\n")
    list_lines = []
    non_list_lines = []
    in_code_block = False
    code_block_lines = []
    has_code_block = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if in_code_block:
                in_code_block = False
                has_code_block = True
            else:
                in_code_block = True
                code_block_lines = []
            continue
        if in_code_block:
            code_block_lines.append(line)
            continue

        if re.match(r"^[-*]\s+", stripped):
            # Bullet list item -- strip the marker
            item = re.sub(r"^[-*]\s+", "", stripped)
            list_lines.append(item)
        elif re.match(r"^\d+\.\s+", stripped):
            # Numbered list item -- strip the number
            item = re.sub(r"^\d+\.\s+", "", stripped)
            list_lines.append(item)
        elif stripped:
            non_list_lines.append(stripped)

    # If it's purely a code block, return as multiline string
    if has_code_block and not list_lines and not non_list_lines:
        return "\n".join(code_block_lines)

    # If it's purely a list, return as list
    if list_lines and not non_list_lines:
        return list_lines

    # If it's a mix or table, return as multiline text
    if has_code_block:
        # Re-assemble without markdown fences
        result_lines = []
        in_cb = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("```"):
                in_cb = not in_cb
                continue
            result_lines.append(line)
        return "\n".join(result_lines).strip()

    # If it has a table, keep as-is (multiline)
    if any("|" in line and "---" not in line for line in lines):
        return content

    # Mixed content or plain prose
    if list_lines and non_list_lines:
        # Return everything as multiline
        return content

    # Plain text -- join into single string if short
    text = " ".join(non_list_lines)
    return text


def compile_md(md_path: Path, schema_formats: dict) -> tuple[dict, str, str]:
    """Compile a single .md file to structured data.

    Returns: (compiled_data, format_ext, error_or_none)
    """
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    fm, body = parse_frontmatter(text)
    if not fm:
        return {}, "", f"No frontmatter found in {md_path}"

    artifact_type = fm.get("kind", "")
    machine_format = schema_formats.get(artifact_type, "yaml")

    # Build compiled output
    compiled = {}

    # Add key frontmatter fields (skip decorative ones like title, lp for compiled)
    for key, val in fm.items():
        compiled[key] = val

    # Parse body sections
    sections = parse_body_sections(body)

    # Merge body sections into compiled output
    for key, val in sections.items():
        if not key:
            continue
        compiled[key] = val

    ext = "json" if machine_format == "json" else "yaml"
    return compiled, ext, None


def get_lp_dir_for_lp(lp_code: str) -> Path | None:
    """Find LP directory matching code like 'P03'."""
    for lp_dir_name in LP_DIRS:
        # lp_dir_name is e.g. "N00_genesis/P03_prompt"; basename starts with pillar code
        basename = lp_dir_name.split("/")[-1]
        if basename.startswith(lp_code + "_") or basename == lp_code:
            return CEX_ROOT / lp_dir_name
    return None


def compile_file(md_path: Path) -> bool:
    """Compile a single markdown file. Returns True on success."""
    md_path = md_path.resolve()

    # Determine LP from path
    lp_dir = md_path.parent.parent
    schema_formats = load_schema(lp_dir)

    compiled, ext, error = compile_md(md_path, schema_formats)
    if error:
        print(f"  SKIP: {error}")
        return False

    # Output path
    compiled_dir = lp_dir / "compiled"
    compiled_dir.mkdir(exist_ok=True)
    out_name = md_path.stem + "." + ext
    out_path = compiled_dir / out_name

    # Write
    with open(out_path, "w", encoding="utf-8") as f:
        if ext == "json":
            json.dump(compiled, f, indent=2, ensure_ascii=False, cls=CEXEncoder)
            f.write("\n")
        else:
            yaml.dump(
                compiled,
                f,
                default_flow_style=False,
                allow_unicode=True,
                sort_keys=False,
                width=120,
            )

    # Validate output
    with open(out_path, "r", encoding="utf-8") as f:
        content = f.read()
    try:
        if ext == "json":
            json.loads(content)
        else:
            yaml.safe_load(content)
    except Exception as e:
        print(f"  ERROR: Invalid {ext} output for {out_path}: {e}")
        return False

    print(f"  OK: {md_path.name} -> compiled/{out_name}")
    return True


def find_examples(lp_dir: Path) -> list[Path]:
    """Find all .md example files in an LP directory."""
    examples_dir = lp_dir / "examples"
    if not examples_dir.exists():
        return []
    return sorted(examples_dir.glob("*.md"))


## ---------------------------------------------------------------------------
## T10: Reverse-path renderers (CEX artifacts -> target format)
## ---------------------------------------------------------------------------

REVERSE_TARGETS = ["claude-md", "cursorrules", "customgpt", "mcp"]


def _load_compiled_artifacts(pillars=None):
    """Load all compiled YAML artifacts from specified pillars."""
    if pillars is None:
        pillars = ["P03", "P04", "P08", "P11"]
    artifacts = []
    for lp_name in LP_DIRS:
        code = lp_name.split("/")[-1].split("_")[0]
        if code not in pillars:
            continue
        compiled_dir = CEX_ROOT / lp_name / "compiled"
        if not compiled_dir.exists():
            continue
        for f in sorted(compiled_dir.glob("*.yaml")):
            try:
                data = yaml.safe_load(f.read_text(encoding="utf-8"))
                if data and isinstance(data, dict):
                    data["_source"] = str(f.relative_to(CEX_ROOT))
                    artifacts.append(data)
            except Exception:
                pass
    return artifacts


def _load_brand_context():
    """Load brand config if available."""
    brand_path = CEX_ROOT / ".cex" / "brand" / "brand_config.yaml"
    if not brand_path.exists():
        return {}
    try:
        return yaml.safe_load(brand_path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}


def render_claude_md(output_path=None):
    """T10: Render CEX artifacts into a CLAUDE.md project context file."""
    artifacts = _load_compiled_artifacts()
    brand = _load_brand_context()

    sections = []
    sections.append("# Project Context (auto-generated by CEX)")
    sections.append(f"# Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    sections.append("")

    # Brand section
    if brand:
        sections.append("## Brand Identity")
        for k, v in brand.items():
            if isinstance(v, str):
                sections.append(f"- **{k}**: {v}")
        sections.append("")

    # Group artifacts by kind
    by_kind = {}
    for a in artifacts:
        kind = a.get("kind", "unknown")
        by_kind.setdefault(kind, []).append(a)

    # System prompts first
    for kind in ["system_prompt", "instruction", "skill", "guardrail", "agent_card", "pattern"]:
        items = by_kind.pop(kind, [])
        if not items:
            continue
        sections.append(f"## {kind.replace('_', ' ').title()}s")
        for item in items:
            title = item.get("title", item.get("id", "untitled"))
            sections.append(f"### {title}")
            # Include key content fields
            for field in ["purpose", "tldr", "description", "content",
                          "when_to_use", "steps", "rules", "checks"]:
                val = item.get(field)
                if val:
                    if isinstance(val, list):
                        sections.append(f"**{field}**:")
                        for v in val:
                            sections.append(f"- {v}")
                    else:
                        sections.append(f"**{field}**: {val}")
            sections.append("")

    # Remaining kinds
    for kind, items in sorted(by_kind.items()):
        sections.append(f"## {kind.replace('_', ' ').title()}s")
        for item in items:
            title = item.get("title", item.get("id", "untitled"))
            sections.append(f"### {title}")
            tldr = item.get("tldr", "")
            if tldr:
                sections.append(f"> {tldr}")
            sections.append("")

    output = "\n".join(sections)
    out = Path(output_path) if output_path else CEX_ROOT / "CLAUDE_GENERATED.md"
    out.write_text(output, encoding="utf-8")
    print(f"  [OK] Rendered {len(artifacts)} artifacts -> {out} ({len(output)} bytes)")
    return str(out)


def render_cursorrules(output_path=None):
    """T10: Render CEX artifacts into a .cursorrules file."""
    artifacts = _load_compiled_artifacts(["P03", "P11"])
    brand = _load_brand_context()

    lines = []
    lines.append("# Project Rules (auto-generated by CEX)")
    lines.append("")

    if brand:
        lines.append(f"Brand: {brand.get('brand_name', 'Unknown')}")
        lines.append(f"Voice: {brand.get('brand_voice', '')}")
        lines.append("")

    for a in artifacts:
        kind = a.get("kind", "")
        title = a.get("title", a.get("id", ""))
        if kind == "guardrail":
            lines.append(f"## RULE: {title}")
            for field in ["checks", "rules", "content"]:
                val = a.get(field)
                if isinstance(val, list):
                    for v in val:
                        lines.append(f"- {v}")
                elif val:
                    lines.append(str(val))
            lines.append("")
        elif kind in ("system_prompt", "instruction"):
            lines.append(f"## {title}")
            content = a.get("content", a.get("tldr", ""))
            if content:
                lines.append(str(content))
            lines.append("")

    output = "\n".join(lines)
    out = Path(output_path) if output_path else CEX_ROOT / ".cursorrules"
    out.write_text(output, encoding="utf-8")
    print(f"  [OK] Rendered {len(artifacts)} artifacts -> {out}")
    return str(out)


def render_customgpt(output_path=None):
    """T10: Render CEX artifacts into CustomGPT instruction JSON."""
    artifacts = _load_compiled_artifacts()
    brand = _load_brand_context()

    instructions = []
    if brand:
        instructions.append(f"You are {brand.get('brand_name', 'an assistant')}.")
        voice = brand.get("brand_voice", "")
        if voice:
            instructions.append(f"Voice: {voice}")

    for a in artifacts:
        kind = a.get("kind", "")
        title = a.get("title", a.get("id", ""))
        tldr = a.get("tldr", "")
        if kind in ("system_prompt", "instruction", "guardrail"):
            instructions.append(f"[{kind}] {title}: {tldr}")

    payload = {
        "name": brand.get("brand_name", "CEX Agent"),
        "instructions": "\n".join(instructions),
        "artifact_count": len(artifacts),
    }

    out = Path(output_path) if output_path else CEX_ROOT / "customgpt_instructions.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False, cls=CEXEncoder), encoding="utf-8")
    print(f"  [OK] Rendered {len(artifacts)} artifacts -> {out}")
    return str(out)


TARGET_RENDERERS = {
    "claude-md": render_claude_md,
    "cursorrules": render_cursorrules,
    "customgpt": render_customgpt,
}


def main():
    parser = argparse.ArgumentParser(description="CEX Compiler: .md -> compiled YAML/JSON | reverse: compiled -> target format")
    parser.add_argument("file", nargs="?", help="Single .md file to compile")
    parser.add_argument("--all", action="store_true", help="Compile all examples in all LPs")
    parser.add_argument("--lp", help="Compile all examples in a specific LP (e.g., P03)")
    parser.add_argument("--target", choices=REVERSE_TARGETS, help="Reverse compile: render to target format")
    parser.add_argument("--output", "-o", help="Output path for --target")
    args = parser.parse_args()

    # --- T10: Reverse compilation ---
    if args.target:
        renderer = TARGET_RENDERERS.get(args.target)
        if not renderer:
            print(f"ERROR: Unknown target '{args.target}'. Available: {', '.join(REVERSE_TARGETS)}")
            sys.exit(1)
        renderer(args.output)
        sys.exit(0)

    if not args.file and not args.all and not args.lp:
        parser.print_help()
        sys.exit(1)

    total = 0
    success = 0

    if args.file:
        md_path = Path(args.file).resolve()
        if not md_path.exists():
            print(f"ERROR: File not found: {md_path}")
            sys.exit(1)
        total = 1
        if compile_file(md_path):
            success = 1

    elif args.lp:
        lp_dir = get_lp_dir_for_lp(args.lp)
        if not lp_dir or not lp_dir.exists():
            print(f"ERROR: LP directory not found for {args.lp}")
            sys.exit(1)
        print(f"Compiling {args.lp}...")
        for md_path in find_examples(lp_dir):
            total += 1
            if compile_file(md_path):
                success += 1

    elif args.all:
        for lp_dir_name in LP_DIRS:
            lp_dir = CEX_ROOT / lp_dir_name
            if not lp_dir.exists():
                continue
            examples = find_examples(lp_dir)
            if not examples:
                continue
            lp_code = lp_dir_name.split("/")[-1].split("_")[0]
            print(f"\n=== {lp_code} ({len(examples)} examples) ===")
            for md_path in examples:
                total += 1
                if compile_file(md_path):
                    success += 1

    print(f"\n--- Results: {success}/{total} compiled successfully ---")
    if success < total:
        sys.exit(1)


if __name__ == "__main__":
    main()
