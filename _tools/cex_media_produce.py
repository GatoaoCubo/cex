#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_media_produce.py -- CEX Media Production Pipeline.

Produces multi-format teaching content from CEX concepts.
Formats: text (markdown), audio (NotebookLM), video (NotebookLM), ppt (Marp).

Usage:
  python _tools/cex_media_produce.py --concept 8f --format text --lens factory --lang en
  python _tools/cex_media_produce.py --concept nuclei --format ppt --lens city --lang pt-br
  python _tools/cex_media_produce.py --concept knowledge_card --format all --lang both
  python _tools/cex_media_produce.py --concept 8f --format audio --lang en --skip-upload
  python _tools/cex_media_produce.py --concept 8f --format all --lang both --dry-run

Spec: _docs/specs/spec_mentor_didactic_engine.md (Wave 4)
Config: N05_operations/P09_config/media_config.yaml
"""

import argparse
import subprocess
import sys
import textwrap
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = CEX_ROOT / "N05_operations" / "P09_config" / "media_config.yaml"


# ---------------------------------------------------------------------------
# YAML loader
# ---------------------------------------------------------------------------

def _yaml():
    try:
        import yaml
        return yaml
    except ImportError:
        print("[FAIL] PyYAML required: pip install pyyaml", file=sys.stderr)
        sys.exit(1)


def load_config(override_path=None):
    p = Path(override_path) if override_path else CONFIG_PATH
    if not p.exists():
        print(f"[FAIL] Config not found: {p}", file=sys.stderr)
        sys.exit(1)
    return _yaml().safe_load(p.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Template rendering (simple mustache-like substitution)
# ---------------------------------------------------------------------------

def render_template(template_text, variables):
    """Render mustache-like template with variable substitution.

    Supports: {{var}}, {{#var}}...{{/var}} (conditional sections).
    """
    result = template_text

    # Conditional sections: {{#var}}content{{/var}}
    import re
    for key, val in variables.items():
        pattern = r"\{\{#" + re.escape(key) + r"\}\}(.*?)\{\{/" + re.escape(key) + r"\}\}"
        if val:
            result = re.sub(pattern, r"\1", result, flags=re.DOTALL)
        else:
            result = re.sub(pattern, "", result, flags=re.DOTALL)

    # Simple substitution: {{var}}
    for key, val in variables.items():
        result = result.replace("{{" + key + "}}", str(val) if val else "")

    return result


def strip_frontmatter(text):
    """Remove YAML frontmatter (--- ... ---) from markdown content."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return text


def load_template(path):
    """Load a prompt_template .md file, extracting the template body."""
    p = CEX_ROOT / path
    if not p.exists():
        return None
    content = p.read_text(encoding="utf-8")
    # Extract content between ```mustache and ```
    import re
    match = re.search(r"```mustache\s*\n(.*?)```", content, re.DOTALL)
    if match:
        return match.group(1)
    return None


# ---------------------------------------------------------------------------
# Lens + concept resolution
# ---------------------------------------------------------------------------

def resolve_lens(config, lens_name):
    """Load a lens KC file and extract its content."""
    aliases = config.get("lens_aliases", {})
    resolved = aliases.get(lens_name, lens_name)
    lenses = config.get("lenses", {})
    path = lenses.get(resolved)
    if not path:
        print(f"[FAIL] Unknown lens: {lens_name}. Available: {list(lenses.keys())}")
        return None
    p = CEX_ROOT / path
    if not p.exists():
        print(f"[WARN] Lens KC not found: {p}")
        print("  Wave 1 (Lens System) may not be complete yet.")
        return None
    return strip_frontmatter(p.read_text(encoding="utf-8"))


def _load_concept_registry(config_path=None):
    """Load the concept registry (separate file referenced by media_config)."""
    cfg = load_config(config_path)
    reg_path = cfg.get("concept_registry")
    if reg_path:
        p = CEX_ROOT / reg_path
        if p.exists():
            return _yaml().safe_load(p.read_text(encoding="utf-8"))
    return cfg


def resolve_source_module(concept_name, config_path=None):
    """Load source module content if concept has one in the registry."""
    reg = _load_concept_registry(config_path)
    for entry in reg.get("concepts", []):
        if entry.get("slug") == concept_name:
            src = entry.get("source_module")
            if src:
                p = CEX_ROOT / src
                if p.exists():
                    return strip_frontmatter(p.read_text(encoding="utf-8"))
    return None


def resolve_concept(concept_name):
    """Resolve a concept name to its type and technical definition."""
    concept_map = {
        "8": ("pipeline", "The 8-function reasoning protocol: F1-F8"),
        "8f_pipeline": ("pipeline", "The 8-function reasoning protocol: F1-F8"),
        "12p": ("system", "The 12-pillar domain architecture: P01-P12"),
        "pillars": ("system", "The 12-pillar domain architecture: P01-P12"),
        "nuclei": ("system", "The 7 sin-driven operational agents: N01-N07"),
        "nucleus": ("system", "A sin-driven operational agent in the CEX system"),
        "kind": ("system", "An atomic artifact type from the 293-kind taxonomy"),
        "builder": ("system", "A 12-ISO agent that produces one kind via 8F"),
        "iso": ("system", "An instruction set for one pillar of a builder"),
        "gdp": ("system", "Guided Decision Protocol: user decides WHAT, LLM decides HOW"),
        "sin_lens": ("system", "Cultural DNA that shapes nucleus optimization bias"),
        "kinds": ("system", "The 293-type artifact taxonomy: one kind per atomic output"),
        "kind": ("system", "An atomic artifact type from the 293-kind taxonomy"),
        "dispatch": ("system", "Grid orchestration: solo/grid/swarm dispatch to nuclei"),
        "crews": ("system", "Multi-role composable team with sequential/hierarchical/consensus topology"),
        "crew": ("system", "A composable multi-role team producing one coherent deliverable"),
        "signals": ("system", "Inter-agent completion and state communication protocol"),
        "signal": ("system", "A completion notification from nucleus to orchestrator"),
        "memory": ("system", "4-type persistent knowledge system: correction/preference/convention/context"),
    }

    # Check static map
    key = concept_name.lower().replace("-", "_").replace(" ", "_")
    if key in concept_map:
        return key, concept_map[key][0], concept_map[key][1]

    # Check if it's a kind name
    meta_path = CEX_ROOT / ".cex" / "kinds_meta.json"
    if meta_path.exists():
        import json
        kinds = json.loads(meta_path.read_text(encoding="utf-8"))
        if isinstance(kinds, dict):
            for k in kinds:
                if k.lower() == key:
                    info = kinds[k]
                    pillar = info.get("pillar", "unknown")
                    return k, "kind", f"A {pillar} artifact kind in the CEX taxonomy"

    # Check if it's a nucleus
    if key.startswith("n0") and len(key) == 3 and key[2].isdigit():
        return key, "nucleus", f"Operational nucleus {key.upper()}"

    # Check if it's a pillar
    if key.startswith("p") and len(key) == 3 and key[1:].isdigit():
        return key, "pillar", f"Domain pillar {key.upper()}"

    return key, "concept", f"CEX concept: {concept_name}"


def resolve_locale(config, lang):
    """Load locale voice directive for a language (brief summary, not full template)."""
    locale_map = {
        "en": (
            "Write in English. Use direct, builder-first tone. "
            "Short sentences, action verbs, active voice. "
            "Prefer: build, ship, run, test, deploy. "
            "Avoid: leverage, synergy, utilize, facilitate."
        ),
        "pt-br": (
            "Escreva em portugues brasileiro. Tom conversacional, direto, pratico. "
            "Frases curtas, verbos de acao, voz ativa. "
            "Use referencias culturais brasileiras quando natural."
        ),
    }
    return locale_map.get(lang, "")


# ---------------------------------------------------------------------------
# Format producers
# ---------------------------------------------------------------------------

def produce_text(concept, concept_type, tech_def, lens_name, lens_content,
                 locale_voice, lang, output_dir, config, dry_run=False):
    """Produce markdown text via storyteller template."""
    tpl_path = config.get("teaching", {}).get("storyteller",
               "N04_knowledge/P03_prompt/mentor_storyteller.md")
    template = load_template(tpl_path)

    if not template:
        tpl_path = config.get("notebooklm", {}).get("source_template",
                   "N05_operations/P03_prompt/prompt_notebooklm_source.md")
        template = load_template(tpl_path)

    if not template:
        print("[WARN] No storyteller or source template found. Using inline fallback.")
        template = textwrap.dedent("""\
            # {{concept_name}} -- {{lens_name}} Lens

            {{locale_voice}}

            {{#source_content}}
            ## Module Content

            {{source_content}}
            {{/source_content}}

            ## The {{lens_name}} Analogy

            {{lens_content}}

            ## Key Takeaways

            1. {{concept_name}} is essential for the CEX pipeline
            2. Through the {{lens_name}} lens, it becomes intuitive
            3. For solo builders, this means faster professional output
            """)

    source_content = resolve_source_module(
        concept.lower().replace(" ", "_").replace("-", "_"),
        config.get("_config_path"))
    variables = {
        "concept_name": concept,
        "concept_type": concept_type,
        "lens_name": lens_name,
        "lens_content": lens_content or "[Lens KC not yet available]",
        "language": lang,
        "locale_voice": locale_voice,
        "audience": config.get("audience", "non_dev_solo_builders"),
        "related_concepts": "",
        "technical_definition": tech_def,
        "source_content": source_content or "",
    }

    out_path = output_dir / f"text_{lens_name}.md"

    if dry_run:
        print(f"  [DRY] Would write: {out_path}")
        print(f"  [DRY] Template: {tpl_path}")
        print(f"  [DRY] Variables: {list(variables.keys())}")
        return True

    rendered = render_template(template, variables)

    # Quality gate: min word count
    min_words = config.get("quality", {}).get("min_text_words", 500)
    word_count = len(rendered.split())
    if word_count < min_words:
        print(f"  [WARN] Text only {word_count} words (min: {min_words})")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(rendered, encoding="utf-8")
    print(f"  [OK] Text: {out_path} ({word_count} words)")
    return True


def produce_audio_source(concept, concept_type, tech_def, lens_name, lens_content,
                         locale_voice, lang, output_dir, config, dry_run=False,
                         skip_upload=False):
    """Produce NotebookLM source doc and optionally upload."""
    tpl_path = config.get("notebooklm", {}).get("source_template",
               "N05_operations/P03_prompt/prompt_notebooklm_source.md")
    template = load_template(tpl_path)

    if not template:
        print("[FAIL] NotebookLM source template not found.")
        return False

    source_content = resolve_source_module(
        concept.lower().replace(" ", "_").replace("-", "_"),
        config.get("_config_path"))
    variables = {
        "concept_name": concept,
        "concept_type": concept_type,
        "lens_name": lens_name,
        "lens_content": lens_content or "[Lens KC not yet available]",
        "language": lang,
        "locale_voice": locale_voice,
        "audience": config.get("audience", "non_dev_solo_builders"),
        "related_concepts": "",
        "technical_definition": tech_def,
        "source_content": source_content or "",
    }

    out_path = output_dir / "audio_source.md"

    if dry_run:
        print(f"  [DRY] Would write: {out_path}")
        if not skip_upload:
            print("  [DRY] Would upload to NotebookLM via cex_notebooklm.py")
        return True

    rendered = render_template(template, variables)

    # Quality gate: char limit
    max_chars = config.get("quality", {}).get("audio_source_max_chars", 200000)
    if len(rendered) > max_chars:
        print(f"  [WARN] Source doc {len(rendered)} chars exceeds limit {max_chars}")
        rendered = rendered[:max_chars]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(rendered, encoding="utf-8")
    print(f"  [OK] Audio source: {out_path} ({len(rendered)} chars)")

    if not skip_upload:
        notebooklm_tool = CEX_ROOT / config.get("notebooklm", {}).get("tool",
                          "_tools/cex_notebooklm.py")
        if notebooklm_tool.exists():
            domain = f"{config.get('notebooklm', {}).get('domain_prefix', 'mentor')}_{concept}_{lang}"
            cmd = [
                sys.executable, str(notebooklm_tool),
                "--upload", str(out_path),
                "--domain", domain,
            ]
            print(f"  [>>] Uploading to NotebookLM (domain: {domain})...")
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=120,
                                       cwd=str(CEX_ROOT))
                if result.returncode == 0:
                    print("  [OK] NotebookLM upload complete")
                    # Activate audio overview
                    for line in result.stdout.splitlines():
                        if "notebook_id:" in line.lower() or "id:" in line.lower():
                            print(f"  [i] {line.strip()}")
                else:
                    print(f"  [WARN] NotebookLM upload returned code {result.returncode}")
                    if result.stderr:
                        for line in result.stderr.strip().splitlines()[:5]:
                            print(f"  [i] {line}")
            except subprocess.TimeoutExpired:
                print("  [WARN] NotebookLM upload timed out (120s)")
            except Exception as e:
                print(f"  [WARN] NotebookLM upload failed: {e}")
        else:
            print(f"  [WARN] NotebookLM tool not found: {notebooklm_tool}")

    return True


def produce_ppt(concept, concept_type, tech_def, lens_name, lens_content,
                locale_voice, lang, output_dir, config, dry_run=False):
    """Produce Marp slide deck and compile to PPTX/PDF."""
    tpl_path = config.get("marp", {}).get("slide_template",
               "N05_operations/P03_prompt/prompt_ppt_generator.md")
    template = load_template(tpl_path)

    if not template:
        print("[FAIL] PPT generator template not found.")
        return False

    source_content = resolve_source_module(
        concept.lower().replace(" ", "_").replace("-", "_"),
        config.get("_config_path"))
    variables = {
        "concept_name": concept,
        "concept_type": concept_type,
        "lens_name": lens_name,
        "lens_mappings": _extract_lens_mappings(lens_content, concept) if lens_content else "[Lens mappings not yet available]",
        "language": lang,
        "locale_voice": locale_voice,
        "subtitle": f"Teaching {concept} through the {lens_name} lens",
        "author_name": "CEX Mentor",
        "total_slides": "12",
        "include_quiz": "true",
        "audience": config.get("audience", "non_dev_solo_builders"),
        "source_content": source_content or "",
    }

    slides_path = output_dir / "slides.md"

    if dry_run:
        print(f"  [DRY] Would write: {slides_path}")
        print(f"  [DRY] Would compile via: {config.get('marp', {}).get('command', 'npx @marp-team/marp-cli')}")
        return True

    rendered = render_template(template, variables)

    # Quality gate: slide count
    slide_count = rendered.count("\n---\n") + 1
    min_slides = config.get("quality", {}).get("min_slides", 8)
    max_slides = config.get("quality", {}).get("max_slides", 20)
    if slide_count < min_slides:
        print(f"  [WARN] Only {slide_count} slides (min: {min_slides})")
    elif slide_count > max_slides:
        print(f"  [WARN] {slide_count} slides exceeds max ({max_slides})")

    slides_path.parent.mkdir(parents=True, exist_ok=True)
    slides_path.write_text(rendered, encoding="utf-8")
    print(f"  [OK] Slides markdown: {slides_path} ({slide_count} slides)")

    # Compile with Marp
    marp_cmd = config.get("marp", {}).get("command", "npx @marp-team/marp-cli")
    output_formats = config.get("marp", {}).get("output_formats", ["pptx"])

    for fmt in output_formats:
        out_file = output_dir / f"slides.{fmt}"
        cmd_parts = marp_cmd.split() + [str(slides_path), f"--{fmt}", "-o", str(out_file)]
        print(f"  [>>] Compiling {fmt}: {' '.join(cmd_parts)}")
        try:
            result = subprocess.run(
                cmd_parts, capture_output=True, text=True,
                timeout=60, cwd=str(CEX_ROOT)
            )
            if result.returncode == 0:
                print(f"  [OK] {fmt.upper()}: {out_file}")
            else:
                print(f"  [WARN] Marp {fmt} failed (code {result.returncode})")
                if result.stderr:
                    for line in result.stderr.strip().splitlines()[:3]:
                        print(f"  [i] {line}")
        except FileNotFoundError:
            print("  [WARN] Marp CLI not found. Install: npm install -g @marp-team/marp-cli")
            break
        except subprocess.TimeoutExpired:
            print(f"  [WARN] Marp {fmt} timed out (60s)")

    return True


def _extract_lens_mappings(lens_content, concept):
    """Extract relevant mappings from a lens KC for slide presentation."""
    if not lens_content:
        return ""
    lines = []
    in_table = False
    for line in lens_content.splitlines():
        if "|" in line and ("CEX" in line or "Concept" in line or "Kind" in line):
            in_table = True
        if in_table and "|" in line:
            lines.append(line)
            if len(lines) >= 12:
                break
        elif in_table and not line.strip():
            break
    return "\n".join(lines) if lines else f"[See lens KC for {concept} mappings]"


# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------

def produce(args):
    config = load_config(args.config)
    config["_config_path"] = args.config

    concept_key, concept_type, tech_def = resolve_concept(args.concept)
    display_name = args.concept.replace("_", " ").title()

    formats = []
    if args.format == "all":
        formats = config.get("formats", ["text", "audio", "video", "ppt"])
    else:
        formats = [args.format]

    languages = []
    if args.lang == "both":
        languages = config.get("languages", ["en"]) + config.get("community_languages", [])
    else:
        languages = [args.lang]

    lens_content = resolve_lens(config, args.lens)
    if not lens_content and not args.dry_run:
        print(f"[WARN] Lens '{args.lens}' KC not available. Proceeding with fallback content.")

    print("\n=== CEX Media Pipeline ===")
    print(f"Concept: {display_name} ({concept_type})")
    print(f"Formats: {', '.join(formats)}")
    print(f"Languages: {', '.join(languages)}")
    print(f"Lens: {args.lens}")
    if args.dry_run:
        print("Mode: DRY RUN")
    print("========================\n")

    results = {}
    base_output = Path(config.get("output_dir", "_output/mentor"))
    if not base_output.is_absolute():
        base_output = CEX_ROOT / base_output

    for lang in languages:
        locale_voice = resolve_locale(config, lang)
        output_dir = base_output / concept_key / lang

        print(f"--- {lang.upper()} ---")

        for fmt in formats:
            if fmt == "text":
                ok = produce_text(
                    display_name, concept_type, tech_def, args.lens, lens_content,
                    locale_voice, lang, output_dir, config, args.dry_run
                )
            elif fmt == "audio":
                ok = produce_audio_source(
                    display_name, concept_type, tech_def, args.lens, lens_content,
                    locale_voice, lang, output_dir, config, args.dry_run, args.skip_upload
                )
            elif fmt == "video":
                ok = produce_audio_source(
                    display_name, concept_type, tech_def, args.lens, lens_content,
                    locale_voice, lang, output_dir, config, args.dry_run, args.skip_upload
                )
            elif fmt == "ppt":
                ok = produce_ppt(
                    display_name, concept_type, tech_def, args.lens, lens_content,
                    locale_voice, lang, output_dir, config, args.dry_run
                )
            else:
                print(f"  [WARN] Unknown format: {fmt}")
                ok = False

            results[f"{lang}/{fmt}"] = ok

        print()

    # Summary
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    print(f"=== Results: {passed}/{total} formats produced ===")
    for key, ok in results.items():
        status = "[OK]" if ok else "[FAIL]"
        print(f"  {status} {key}")

    return 0 if all(results.values()) else 3


def main():
    parser = argparse.ArgumentParser(
        description="CEX Media Production Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              %(prog)s --concept 8f --format text --lens factory --lang en
              %(prog)s --concept nuclei --format ppt --lens city --lang pt-br
              %(prog)s --concept knowledge_card --format all --lang both
              %(prog)s --concept 8f --format audio --lang en --skip-upload
              %(prog)s --concept 8f --format all --lang both --dry-run
        """)
    )

    parser.add_argument("--concept", required=True,
                        help="CEX concept to produce (e.g., 8f, knowledge_card, nuclei)")
    parser.add_argument("--format", required=True,
                        choices=["text", "audio", "video", "ppt", "all"],
                        help="Output format")
    cfg = load_config()
    available_lenses = list(cfg.get("lenses", {}).keys())
    if "index" in available_lenses:
        available_lenses.remove("index")
    aliases = cfg.get("lens_aliases", {})
    all_lens_names = sorted(set(available_lenses + list(aliases.keys())))
    parser.add_argument("--lens", default="factory",
                        choices=all_lens_names,
                        help="Analogy lens (default: factory)")
    parser.add_argument("--lang", default="en",
                        choices=["en", "pt-br", "both"],
                        help="Language: en (default), community languages via --lang, or 'both' for all configured")
    parser.add_argument("--output-dir",
                        help="Override output directory")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be produced without executing")
    parser.add_argument("--skip-upload", action="store_true",
                        help="Skip NotebookLM upload (audio/video only)")
    parser.add_argument("--config",
                        help="Override media_config.yaml path")

    args = parser.parse_args()
    sys.exit(produce(args))


if __name__ == "__main__":
    main()
