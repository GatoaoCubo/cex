#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Handoff Composer -- auto-select builders, KCs, templates for nucleus dispatch.

Closes GAP G7: Nucleus starts producing on turn 1 instead of spending 5 turns
discovering files. Reads kinds_meta.json, finds builder paths, finds KCs,
resolves schemas and examples, and composes a complete handoff file.

Usage:
    # From task description (auto-detect kinds via keyword match)
    python _tools/cex_handoff_composer.py --task "build agent card for auth" --nucleus n03

    # Explicit kinds
    python _tools/cex_handoff_composer.py --kinds agent_card,agent --nucleus n03 --mission MYRUN

    # From intent (uses cex_query TF-IDF if available)
    python _tools/cex_handoff_composer.py --task "monetizar curso hotmart" --nucleus n06

    # Dry-run (print to stdout, don't write file)
    python _tools/cex_handoff_composer.py --task "create webhook tool" --nucleus n05 --dry-run

    # With extra instructions appended
    python _tools/cex_handoff_composer.py --kinds workflow --nucleus n03 --extra "Use DAG pattern"

    # JSON output (for programmatic use by cex_mission_runner)
    python _tools/cex_handoff_composer.py --kinds agent --nucleus n03 --json

API:
    from _tools.cex_handoff_composer import compose_handoff, discover_kinds

    kinds = discover_kinds("build agent card for auth module")
    handoff = compose_handoff(
        task="Build agent card for auth module",
        nucleus="n03",
        kinds=kinds,
        mission="FULLGRID_20260407",
    )
    print(handoff.markdown)
    handoff.write()  # -> .cex/runtime/handoffs/FULLGRID_20260407_n03.md
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
KINDS_META = ROOT / ".cex" / "kinds_meta.json"
HANDOFF_DIR = ROOT / ".cex" / "runtime" / "handoffs"
DECISION_MANIFEST = ROOT / ".cex" / "runtime" / "decisions" / "decision_manifest.yaml"
BUILDERS_DIR = ROOT / "archetypes" / "builders"
KC_DIR = ROOT / "N00_genesis" / "P01_knowledge" / "library" / "kind"
EXAMPLES_DIR = ROOT / "N00_genesis" / "P01_knowledge" / "examples"
SCHEMAS_DIR = ROOT  # P{XX}_*/_schema.yaml lives under ROOT

# Nucleus domain map (fallback if nucleus_models.yaml unavailable)
NUCLEUS_DOMAINS = {
    "n01": "research",
    "n02": "marketing",
    "n03": "build",
    "n04": "knowledge",
    "n05": "operations",
    "n06": "commercial",
    "n07": "orchestration",
}

# 13 ISO file stems per builder
ISO_STEMS = [
    "manifest", "instruction", "system_prompt", "memory", "scoring",
    "hooks", "style", "quality", "template", "examples",
    "context", "tools", "schema",
]


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------
@dataclass
class KindContext:
    """Everything discovered about a single kind."""
    kind: str
    pillar: str = ""
    core: bool = False
    description: str = ""
    builder_dir: Optional[Path] = None
    kc_path: Optional[Path] = None
    schema_path: Optional[Path] = None
    example_paths: List[Path] = field(default_factory=list)
    iso_paths: List[Path] = field(default_factory=list)
    naming: str = ""

    def to_dict(self) -> dict:
        def p(v):
            if v is None:
                return None
            if isinstance(v, Path):
                try:
                    return str(v.relative_to(ROOT))
                except ValueError:
                    return str(v)
            return v

        return {
            "kind": self.kind,
            "pillar": self.pillar,
            "core": self.core,
            "description": self.description,
            "builder_dir": p(self.builder_dir),
            "kc_path": p(self.kc_path),
            "schema_path": p(self.schema_path),
            "example_paths": [p(e) for e in self.example_paths],
            "iso_count": len(self.iso_paths),
            "naming": self.naming,
        }


@dataclass
class ComposedHandoff:
    """A composed handoff document ready for writing."""
    nucleus: str
    task: str
    mission: str
    kinds: List[KindContext]
    extra: str = ""
    created: str = ""
    markdown: str = ""
    path: Optional[Path] = None

    def write(self) -> Path:
        """Write handoff to .cex/runtime/handoffs/."""
        HANDOFF_DIR.mkdir(parents=True, exist_ok=True)
        if self.mission:
            filename = f"{self.mission}_{self.nucleus}.md"
        else:
            filename = f"{self.nucleus}_task.md"
        self.path = HANDOFF_DIR / filename
        self.path.write_text(self.markdown, encoding="utf-8")
        return self.path


# ---------------------------------------------------------------------------
# Kind registry
# ---------------------------------------------------------------------------
def load_kinds_meta() -> Dict[str, dict]:
    """Load kinds_meta.json. Returns {} on failure."""
    if not KINDS_META.exists():
        print(f"[WARN] kinds_meta.json not found at {KINDS_META}", file=sys.stderr)
        return {}
    try:
        return json.loads(KINDS_META.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"[WARN] Failed to load kinds_meta.json: {exc}", file=sys.stderr)
        return {}


# ---------------------------------------------------------------------------
# Discovery: kind from task text (keyword match)
# ---------------------------------------------------------------------------
_STOP_WORDS = {
    "a", "an", "the", "and", "or", "o", "to", "in", "for", "with", "on",
    "is", "it", "this", "that", "from", "by", "at", "be", "as", "are",
    "criar", "create", "build", "make", "novo", "new", "um", "uma",
    "para", "com", "de", "do", "da", "que", "se", "por", "o", "e",
}


def _normalize(text: str) -> str:
    text = text.lower().strip()
    for src, dst in [
        ("\u00e1", "a"), ("\u00e0", "a"), ("\u00e3", "a"), ("\u00e2", "a"),
        ("\u00e9", "e"), ("\u00ea", "e"), ("\u00ed", "i"), ("\u00f3", "o"),
        ("\u00f4", "o"), ("\u00f5", "o"), ("\u00fa", "u"), ("\u00fc", "u"),
        ("\u00e7", "c"),
    ]:
        text = text.replace(src, dst)
    text = re.sub(r"[-_]", " ", text)
    text = re.sub(r"[^a-z0-9 ]", "", text)
    return text


def _tokenize(text: str) -> List[str]:
    return [w for w in _normalize(text).split() if w not in _STOP_WORDS and len(w) >= 2]


def discover_kinds(task: str, kinds_meta: Optional[dict] = None, top_n: int = 5) -> List[str]:
    """Discover relevant kinds from a task description via keyword scoring.

    Scoring:
      - Exact kind name in text      = +10
      - Kind name as substring        = +5
      - Token overlap with description = +1 per token
      - Core kind bonus               = +2

    Returns sorted list of kind names (max top_n).
    """
    if kinds_meta is None:
        kinds_meta = load_kinds_meta()
    if not kinds_meta:
        return []

    task_lower = task.lower().replace("-", "_")
    task_tokens = set(_tokenize(task))
    scores: Dict[str, float] = {}

    for kind, meta in kinds_meta.items():
        score = 0.0
        kind_words = kind.replace("_", " ")

        # Exact kind name match
        if kind in task_lower or kind.replace("_", " ") in task_lower:
            score += 10
        # Kind name words as substrings
        elif any(w in task_lower for w in kind.split("_") if len(w) >= 3):
            score += 5

        # Token overlap with description + boundary
        desc = meta.get("description", "") + " " + meta.get("boundary", "")
        desc_tokens = set(_tokenize(desc))
        overlap = task_tokens & desc_tokens
        score += len(overlap)

        # Core kind bonus
        if meta.get("core"):
            score += 2

        if score > 0:
            scores[kind] = score

    ranked = sorted(scores, key=lambda k: scores[k], reverse=True)
    return ranked[:top_n]


# ---------------------------------------------------------------------------
# Context resolution: builder ISOs, KCs, schemas, examples
# ---------------------------------------------------------------------------
def resolve_kind_context(kind: str, kinds_meta: dict) -> KindContext:
    """Resolve all file paths for a given kind."""
    meta = kinds_meta.get(kind, {})
    ctx = KindContext(
        kind=kind,
        pillar=meta.get("pillar", ""),
        core=meta.get("core", False),
        description=meta.get("description", ""),
        naming=meta.get("naming", ""),
    )

    # Builder directory
    builder_slug = kind.replace("_", "-")
    builder_dir = BUILDERS_DIR / f"{builder_slug}-builder"
    if builder_dir.is_dir():
        ctx.builder_dir = builder_dir
        # Discover ISOs
        for stem in ISO_STEMS:
            iso_file = builder_dir / f"bld_{stem}_{kind}.md"
            if iso_file.exists():
                ctx.iso_paths.append(iso_file)

    # Knowledge Card
    kc_file = KC_DIR / f"kc_{kind}.md"
    if kc_file.exists():
        ctx.kc_path = kc_file

    # Schema (find pillar dir)
    if ctx.pillar:
        pillar_dirs = list(ROOT.glob(f"{ctx.pillar}_*"))
        for pd in pillar_dirs:
            schema_file = pd / "_schema.yaml"
            if schema_file.exists():
                ctx.schema_path = schema_file
                break

    # Examples (search in P01 examples + compiled)
    example_prefix = f"ex_{kind}_"
    if EXAMPLES_DIR.is_dir():
        for f in sorted(EXAMPLES_DIR.iterdir()):
            if f.name.startswith(example_prefix) and f.suffix == ".md":
                ctx.example_paths.append(f)

    return ctx


def resolve_all_kinds(kinds: List[str], kinds_meta: dict) -> List[KindContext]:
    """Resolve context for multiple kinds."""
    return [resolve_kind_context(k, kinds_meta) for k in kinds]


# ---------------------------------------------------------------------------
# Handoff composition
# ---------------------------------------------------------------------------
def _rel(path: Optional[Path]) -> str:
    """Relative path string from ROOT, or empty."""
    if path is None:
        return ""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def compose_handoff(
    task: str,
    nucleus: str,
    kinds: Optional[List[str]] = None,
    mission: str = "",
    extra: str = "",
    kinds_meta: Optional[dict] = None,
    include_decisions: bool = True,
) -> ComposedHandoff:
    """Compose a complete handoff document.

    Args:
        task: Natural-language task description.
        nucleus: Target nucleus (n01-n07).
        kinds: Explicit kind list. If None, auto-discovered from task.
        mission: Mission ID (e.g., FULLGRID_20260407). Optional.
        extra: Additional instructions to append.
        kinds_meta: Pre-loaded kinds registry. Loaded if None.
        include_decisions: Include decision manifest reference.

    Returns:
        ComposedHandoff with .markdown populated and .write() ready.
    """
    if kinds_meta is None:
        kinds_meta = load_kinds_meta()

    nucleus = nucleus.lower()
    if nucleus not in NUCLEUS_DOMAINS:
        raise ValueError(f"Invalid nucleus '{nucleus}'. Must be n01-n07.")

    # Discover kinds if not provided
    if not kinds:
        kinds = discover_kinds(task, kinds_meta)

    # Resolve all context
    kind_contexts = resolve_all_kinds(kinds, kinds_meta)

    now = datetime.now(timezone.utc)
    created = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    # --- Build markdown ---
    lines = []

    # Frontmatter
    lines.append("---")
    lines.append(f"nucleus: {nucleus.upper()}")
    lines.append("task: dispatch")
    if mission:
        lines.append(f"mission: {mission}")
    lines.append(f"created: {created}")
    lines.append(f"domain: {NUCLEUS_DOMAINS.get(nucleus, 'unknown')}")
    lines.append(f"kinds: [{', '.join(kinds)}]")
    lines.append("auto_composed: true")
    lines.append("---")
    lines.append("")

    # Task header
    lines.append(f"# Task for {nucleus.upper()}")
    lines.append("")
    lines.append(task)
    lines.append("")

    # Context section: builders, KCs, schemas
    if kind_contexts:
        lines.append("## Context (auto-discovered)")
        lines.append("")
        lines.append("The following files are pre-resolved. Load them BEFORE producing.")
        lines.append("")

        for ctx in kind_contexts:
            lines.append(f"### Kind: `{ctx.kind}`")
            lines.append("")
            if ctx.description:
                lines.append(f"> {ctx.description}")
                lines.append("")

            lines.append("| Resource | Path | Status |")
            lines.append("|----------|------|--------|")

            # Builder ISOs
            if ctx.builder_dir:
                lines.append(
                    f"| Builder dir | `{_rel(ctx.builder_dir)}/` | "
                    f"{len(ctx.iso_paths)}/13 ISOs |"
                )
                for iso in ctx.iso_paths:
                    stem = iso.stem.replace("bld_", "").replace(f"_{ctx.kind}", "")
                    lines.append(f"| ISO: {stem} | `{_rel(iso)}` | OK |")
            else:
                lines.append("| Builder dir | (not found) | MISSING |")

            # KC
            if ctx.kc_path:
                lines.append(f"| Knowledge Card | `{_rel(ctx.kc_path)}` | OK |")
            else:
                lines.append("| Knowledge Card | (not found) | MISSING |")

            # Schema
            if ctx.schema_path:
                lines.append(f"| Pillar schema | `{_rel(ctx.schema_path)}` | {ctx.pillar} |")

            # Examples
            for ex in ctx.example_paths[:3]:
                lines.append(f"| Example | `{_rel(ex)}` | OK |")

            # Naming
            if ctx.naming:
                lines.append(f"| Naming convention | `{ctx.naming}` | - |")

            lines.append("")

    # Decision manifest reference
    if include_decisions and DECISION_MANIFEST.exists():
        lines.append("## Decisions (from user -- DO NOT re-ask)")
        lines.append("")
        lines.append(f"Read: `{_rel(DECISION_MANIFEST)}`")
        lines.append("All subjective decisions were already made with the user.")
        lines.append("Execute using those decisions. Do NOT override them.")
        lines.append("")

    # Extra instructions
    if extra:
        lines.append("## Additional Instructions")
        lines.append("")
        lines.append(extra)
        lines.append("")

    # Completion protocol
    lines.append("## On Completion")
    lines.append("")
    lines.append("1. Commit your work: `git add -A && git commit -m \"[{nuc}] <description>\"`".format(
        nuc=nucleus.upper()
    ))
    lines.append("2. Signal complete:")
    lines.append("")
    lines.append("```python")
    lines.append(
        f"python -c \"from _tools.signal_writer import write_signal; "
        f"write_signal('{nucleus}', 'complete', 9.0"
        + (f", '{mission}'" if mission else "")
        + ")\""
    )
    lines.append("```")

    markdown = "\n".join(lines) + "\n"

    return ComposedHandoff(
        nucleus=nucleus,
        task=task,
        mission=mission,
        kinds=kind_contexts,
        extra=extra,
        created=created,
        markdown=markdown,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="CEX Handoff Composer -- auto-select builders, KCs, templates for dispatch",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python _tools/cex_handoff_composer.py --task "build agent card" --nucleus n03
  python _tools/cex_handoff_composer.py --kinds agent,workflow --nucleus n03 --mission MY_RUN
  python _tools/cex_handoff_composer.py --task "create webhook" --nucleus n05 --dry-run
  python _tools/cex_handoff_composer.py --task "build landing page" --nucleus n02 --json
""",
    )
    parser.add_argument("--task", "-t", type=str, default="",
                        help="Natural-language task description")
    parser.add_argument("--nucleus", "-n", type=str, required=True,
                        help="Target nucleus (n01-n07)")
    parser.add_argument("--kinds", "-k", type=str, default="",
                        help="Comma-separated kind list (skips auto-discovery)")
    parser.add_argument("--mission", "-m", type=str, default="",
                        help="Mission ID prefix for filename")
    parser.add_argument("--extra", "-e", type=str, default="",
                        help="Additional instructions to append")
    parser.add_argument("--top", type=int, default=5,
                        help="Max kinds to auto-discover (default: 5)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print to stdout, don't write file")
    parser.add_argument("--json", action="store_true",
                        help="Output JSON context (for programmatic use)")
    parser.add_argument("--discover-only", action="store_true",
                        help="Only discover kinds, don't compose handof")

    args = parser.parse_args()

    if not args.task and not args.kinds:
        parser.error("Provide --task (for auto-discovery) or --kinds (explicit)")

    kinds_meta = load_kinds_meta()

    # Determine kinds
    if args.kinds:
        kinds = [k.strip() for k in args.kinds.split(",") if k.strip()]
        # Validate against registry
        for k in kinds:
            if k not in kinds_meta:
                print(f"[WARN] Kind '{k}' not in kinds_meta.json", file=sys.stderr)
    else:
        kinds = discover_kinds(args.task, kinds_meta, top_n=args.top)
        if not kinds:
            print("[WARN] No kinds discovered from task. Check task description.", file=sys.stderr)

    # Discover-only mode
    if args.discover_only:
        contexts = resolve_all_kinds(kinds, kinds_meta)
        if args.json:
            print(json.dumps([c.to_dict() for c in contexts], indent=2))
        else:
            print(f"Discovered {len(kinds)} kinds: {', '.join(kinds)}")
            for ctx in contexts:
                print(f"  {ctx.kind}: builder={'OK' if ctx.builder_dir else 'MISSING'} "
                      f"kc={'OK' if ctx.kc_path else 'MISSING'} "
                      f"isos={len(ctx.iso_paths)} "
                      f"examples={len(ctx.example_paths)}")
        return

    # Compose
    handoff = compose_handoff(
        task=args.task or f"Build artifacts for kinds: {', '.join(kinds)}",
        nucleus=args.nucleus,
        kinds=kinds,
        mission=args.mission,
        extra=args.extra,
        kinds_meta=kinds_meta,
    )

    # JSON output
    if args.json:
        out = {
            "nucleus": handoff.nucleus,
            "task": handoff.task,
            "mission": handoff.mission,
            "created": handoff.created,
            "kinds": [c.to_dict() for c in handoff.kinds],
            "path": str(handoff.path) if handoff.path else None,
        }
        if not args.dry_run:
            path = handoff.write()
            out["path"] = str(path.relative_to(ROOT))
            print(json.dumps(out, indent=2))
            print(f"\n[OK] Handoff written: {path.relative_to(ROOT)}", file=sys.stderr)
        else:
            print(json.dumps(out, indent=2))
        return

    # Markdown output
    if args.dry_run:
        print(handoff.markdown)
    else:
        path = handoff.write()
        print(f"[OK] Handoff written: {path.relative_to(ROOT)}")
        print(f"     Kinds: {', '.join(k.kind for k in handoff.kinds)}")
        print(f"     ISOs: {sum(len(k.iso_paths) for k in handoff.kinds)} total")
        print(f"     KCs: {sum(1 for k in handoff.kinds if k.kc_path)} found")


if __name__ == "__main__":
    main()
