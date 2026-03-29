#!/usr/bin/env python3
"""
cex_8f_runner.py -- 8F Runner: Stateful artifact production pipeline.

Each function (F1-F8) produces state that the next CONSUMES.
Wave 1: F1 CONSTRAIN, F2 BECOME, F3 INJECT, F6 PRODUCE, F8 COLLABORATE.
Wave 2 adds: F4 REASON, F7 GOVERN (+ retry loop).
Wave 3 adds: F5 CALL, multi-kind, proofs.

Usage:
  python cex_8f_runner.py "create a chunking config for markdown"
  python cex_8f_runner.py "create agent for sales" --execute
  python cex_8f_runner.py --kind chunk_strategy --dry-run
  python cex_8f_runner.py --list-kinds
  python cex_8f_runner.py "create eval" --step 3 --verbose
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

import argparse
import re
import time
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERRO: PyYAML necessario. pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Imports from Motor + Intent
# ---------------------------------------------------------------------------

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_8f_motor import (
    CEX_ROOT,
    OBJECT_TO_KINDS,
    parse_intent,
    classify_objects,
    fan_out,
    load_builder_map,
    load_kc_library,
    lookup_kcs_for_kind,
    generate_output,
)
from cex_intent import execute_prompt

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BUILDER_DIR = CEX_ROOT / "archetypes" / "builders"

# Pillar directory names keyed by code
PILLAR_DIRS = {
    f"P{i:02d}": d.name
    for i, d in enumerate(sorted(CEX_ROOT.glob("P[0-9][0-9]_*")), start=0)
    if d.is_dir()
}
# Rebuild with correct index from actual directory names
PILLAR_DIRS = {}
for d in sorted(CEX_ROOT.glob("P[0-9][0-9]_*")):
    if d.is_dir():
        code = d.name[:3]  # e.g. "P01"
        PILLAR_DIRS[code] = d.name

# ISO prefix -> function mapping
ISO_TO_FUNCTION = {
    "bld_schema": "F1",
    "bld_config": "F1",
    "bld_system_prompt": "F2",
    "bld_manifest": "F2",
    "bld_knowledge_card": "F3",
    "bld_examples": "F3",
    "bld_memory": "F3",
    "bld_architecture": "F3",
    "bld_instruction": "F6",
    "bld_output_template": "F6",
    "bld_quality_gate": "F7",
    "bld_tools": "F5",
    "bld_collaboration": "F8",
}

ALL_ISO_PREFIXES = list(ISO_TO_FUNCTION.keys())


# ---------------------------------------------------------------------------
# RunState
# ---------------------------------------------------------------------------


@dataclass
class RunState:
    """Accumulated state across 8 functions."""

    intent: str = ""
    kind: str = ""
    pillar: str = ""
    builder_dir: Path | None = None

    # F1 CONSTRAIN
    constraints: dict = field(default_factory=dict)
    # F2 BECOME
    identity: dict = field(default_factory=dict)
    # F3 INJECT
    knowledge: dict = field(default_factory=dict)
    # F4 REASON (wave 2)
    reasoning: dict = field(default_factory=dict)
    # F5 CALL (wave 3)
    tool_results: dict = field(default_factory=dict)
    # F6 PRODUCE
    artifact: str = ""
    # F7 GOVERN (wave 2)
    verdict: dict = field(default_factory=dict)
    # F8 COLLABORATE
    result: dict = field(default_factory=dict)

    # Meta
    timings: dict = field(default_factory=dict)
    errors: list = field(default_factory=list)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def find_builder_dir(kind: str) -> Path | None:
    """Locate builder directory for a CEX kind."""
    slug = kind.replace("_", "-")
    direct = BUILDER_DIR / f"{slug}-builder"
    if direct.exists():
        return direct
    # Partial match fallback
    for d in BUILDER_DIR.iterdir():
        if d.is_dir() and slug in d.name:
            return d
    return None


def load_iso(builder_dir: Path, prefix: str, kind_slug: str) -> str:
    """Read a single builder ISO file. Returns content or empty string."""
    target = builder_dir / f"{prefix}_{kind_slug}.md"
    if target.exists():
        return target.read_text(encoding="utf-8")
    # Fallback: any file matching prefix
    for f in builder_dir.glob(f"{prefix}_*.md"):
        return f.read_text(encoding="utf-8")
    return ""


def strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter from markdown text."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            return text[end + 3 :].strip()
    return text


def extract_frontmatter_dict(text: str) -> dict:
    """Parse YAML frontmatter into a dict."""
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end < 0:
        return {}
    try:
        return yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return {}


def load_pillar_schema(pillar: str) -> dict:
    """Load _schema.yaml for a pillar and return the full schema dict."""
    dir_name = PILLAR_DIRS.get(pillar)
    if not dir_name:
        return {}
    schema_path = CEX_ROOT / dir_name / "_schema.yaml"
    if not schema_path.exists():
        return {}
    try:
        with open(schema_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except yaml.YAMLError:
        return {}


def load_kind_schema(kind: str, pillar: str) -> dict:
    """Extract kind-specific constraints from pillar _schema.yaml."""
    schema = load_pillar_schema(pillar)
    kinds = schema.get("kinds", {})
    return kinds.get(kind, {})


# ---------------------------------------------------------------------------
# EightFRunner
# ---------------------------------------------------------------------------


class EightFRunner:
    """Stateful 8-function pipeline for artifact production."""

    def __init__(
        self,
        intent: str,
        kind: str | None = None,
        dry_run: bool = True,
        verbose: bool = False,
        output_dir: Path | None = None,
    ):
        self.dry_run = dry_run
        self.verbose = verbose
        self.output_dir = output_dir
        self.state = RunState(intent=intent)

        # Motor parse + classify
        self.parsed = parse_intent(intent)
        if kind:
            self.classified = classify_objects([kind])
        else:
            self.classified = classify_objects(self.parsed["objects"])

        # Set primary kind
        if self.classified:
            c = self.classified[0]
            self.state.kind = c["kind"]
            self.state.pillar = c["pillar"]
        else:
            self.state.kind = "generic"
            self.state.pillar = "P01"

        # Locate builder
        self.state.builder_dir = find_builder_dir(self.state.kind)
        self.kind_slug = self.state.kind.replace("-", "_")

        # Motor plan (for F3 KC injection)
        builder_map = load_builder_map()
        self.kc_library = load_kc_library()
        functions = fan_out(
            classified=self.classified,
            intent_lower=intent.lower(),
            quality=self.parsed["quality"],
            builder_map=builder_map,
            verb_action=self.parsed["verb_action"],
            kc_library=self.kc_library,
        )
        self.plan = generate_output(intent, self.parsed, self.classified, functions)

    def _log(self, fn: str, msg: str):
        if self.verbose:
            print(f"  [{fn}] {msg}", file=sys.stderr)

    def _timed(self, fn_name: str, func):
        """Run a function and record its timing."""
        t0 = time.perf_counter()
        try:
            func()
        except Exception as e:
            self.state.errors.append(f"{fn_name}: {e}")
            self._log(fn_name, f"ERROR: {e}")
        elapsed = (time.perf_counter() - t0) * 1000
        self.state.timings[fn_name] = round(elapsed, 1)
        self._log(fn_name, f"done ({elapsed:.1f}ms)")

    # -- F1 CONSTRAIN -------------------------------------------------------

    def f1_constrain(self):
        """Load _schema.yaml + bld_schema + bld_config -> state.constraints."""
        bdir = self.state.builder_dir
        kind = self.state.kind
        pillar = self.state.pillar

        # 1. Pillar schema constraints
        kind_schema = load_kind_schema(kind, pillar)
        constraints = dict(kind_schema.get("constraints", {}))
        constraints["frontmatter_required"] = kind_schema.get("frontmatter_required", [])
        constraints["naming"] = kind_schema.get("naming", "")
        constraints["boundary"] = kind_schema.get("boundary", "")

        # 2. bld_schema -> id_pattern, field types
        if bdir:
            schema_text = load_iso(bdir, "bld_schema", self.kind_slug)
            if schema_text:
                body = strip_frontmatter(schema_text)
                # Extract ID pattern regex
                m = re.search(r"Regex:\s*`([^`]+)`", body)
                if m:
                    constraints["id_pattern"] = m.group(1)
                constraints["_schema_body"] = body
                self._log("F1", f"bld_schema loaded ({len(schema_text)} chars)")

        # 3. bld_config -> naming rules, paths, size limits
        if bdir:
            config_text = load_iso(bdir, "bld_config", self.kind_slug)
            if config_text:
                body = strip_frontmatter(config_text)
                constraints["config_rules"] = body
                # Extract max bytes from config if present
                m = re.search(r"max\s+(\d+)\s*bytes", body, re.IGNORECASE)
                if m and "max_bytes" not in constraints:
                    constraints["max_bytes"] = int(m.group(1))
                self._log("F1", f"bld_config loaded ({len(config_text)} chars)")

        self.state.constraints = constraints
        self._log("F1", f"constraints: {len(constraints)} keys")

    # -- F2 BECOME ----------------------------------------------------------

    def f2_become(self):
        """Load bld_system_prompt + bld_manifest -> state.identity."""
        bdir = self.state.builder_dir
        identity = {}

        if bdir:
            # System prompt (persona)
            sp_text = load_iso(bdir, "bld_system_prompt", self.kind_slug)
            if sp_text:
                identity["system_prompt"] = strip_frontmatter(sp_text)
                fm = extract_frontmatter_dict(sp_text)
                identity["persona"] = fm.get("persona", "")
                identity["knowledge_boundary"] = fm.get("knowledge_boundary", "")
                self._log("F2", f"bld_system_prompt loaded ({len(sp_text)} chars)")

            # Manifest (builder name, domain)
            man_text = load_iso(bdir, "bld_manifest", self.kind_slug)
            if man_text:
                fm = extract_frontmatter_dict(man_text)
                identity["builder_name"] = fm.get("id", "")
                identity["domain"] = fm.get("domain", "")
                identity["pillar_boundary"] = strip_frontmatter(man_text)
                self._log("F2", f"bld_manifest loaded ({len(man_text)} chars)")

        # Schema boundary
        identity["kind_boundary"] = self.state.constraints.get("boundary", "")

        self.state.identity = identity
        self._log("F2", f"identity: {list(identity.keys())}")

    # -- F3 INJECT ----------------------------------------------------------

    def f3_inject(self):
        """Load KC library + builder KCs + examples + memory + architecture -> state.knowledge."""
        bdir = self.state.builder_dir
        knowledge = {}

        # 1. Builder knowledge card
        if bdir:
            kc_text = load_iso(bdir, "bld_knowledge_card", self.kind_slug)
            if kc_text:
                knowledge["kc_builder"] = strip_frontmatter(kc_text)
                self._log("F3", "bld_knowledge_card loaded")

        # 2. KC-Domain matches from library
        kc_matches = lookup_kcs_for_kind(self.kc_library, self.state.kind, self.state.pillar)
        kc_domains = []
        for kc in kc_matches[:3]:  # Max 3 to control token budget
            kc_path = CEX_ROOT / kc["path"]
            if kc_path.exists():
                text = kc_path.read_text(encoding="utf-8")
                body = strip_frontmatter(text)
                if body.strip():
                    kc_domains.append(
                        f"### KC: {kc.get('title', kc.get('id', 'unknown'))}\n\n{body}"
                    )
        knowledge["kc_domains"] = kc_domains
        self._log("F3", f"KC-Domains matched: {len(kc_domains)}")

        # 3. Few-shot examples
        if bdir:
            ex_text = load_iso(bdir, "bld_examples", self.kind_slug)
            if ex_text:
                knowledge["few_shots"] = strip_frontmatter(ex_text)
                self._log("F3", "bld_examples loaded")

        # 4. Memory (persistent learnings)
        if bdir:
            mem_text = load_iso(bdir, "bld_memory", self.kind_slug)
            if mem_text:
                knowledge["memory"] = strip_frontmatter(mem_text)
                self._log("F3", "bld_memory loaded")

        # 5. Architecture (patterns, dependencies)
        if bdir:
            arch_text = load_iso(bdir, "bld_architecture", self.kind_slug)
            if arch_text:
                knowledge["architecture"] = strip_frontmatter(arch_text)
                self._log("F3", "bld_architecture loaded")

        self.state.knowledge = knowledge
        self._log("F3", f"knowledge: {list(knowledge.keys())}")

    # -- F6 PRODUCE ---------------------------------------------------------

    def f6_produce(self):
        """Compose STRUCTURED prompt with 7 labeled sections -> state.artifact."""
        sections = []

        # 1. IDENTITY (from F2)
        sp = self.state.identity.get("system_prompt", "")
        if sp:
            sections.append(f"# IDENTITY\n\n{sp}")

        # 2. CONSTRAINTS (from F1)
        c = self.state.constraints
        constraint_lines = []
        if c.get("max_bytes"):
            constraint_lines.append(f"- Max body size: {c['max_bytes']} bytes")
        if c.get("id_pattern"):
            constraint_lines.append(f"- ID pattern: `{c['id_pattern']}`")
        if c.get("frontmatter_required"):
            constraint_lines.append(
                f"- Required frontmatter: {', '.join(c['frontmatter_required'])}"
            )
        if c.get("boundary"):
            constraint_lines.append(f"- Boundary: {c['boundary']}")
        if c.get("naming"):
            constraint_lines.append(f"- Naming: {c['naming']}")
        constraint_lines.append("- quality: null (NEVER self-score)")
        if constraint_lines:
            sections.append("# CONSTRAINTS\n\n" + "\n".join(constraint_lines))

        # 3. KNOWLEDGE (from F3)
        k = self.state.knowledge
        knowledge_parts = []
        if k.get("kc_builder"):
            knowledge_parts.append(f"## Builder Knowledge\n\n{k['kc_builder']}")
        for kc_domain in k.get("kc_domains", []):
            knowledge_parts.append(f"## Domain Knowledge\n\n{kc_domain}")
        if k.get("architecture"):
            knowledge_parts.append(f"## Architecture\n\n{k['architecture']}")
        if k.get("memory"):
            knowledge_parts.append(f"## Memory (Past Learnings)\n\n{k['memory']}")
        if knowledge_parts:
            sections.append("# KNOWLEDGE\n\n" + "\n\n".join(knowledge_parts))

        # 4. EXAMPLES (from F3)
        if k.get("few_shots"):
            sections.append(f"# EXAMPLES\n\n{k['few_shots']}")

        # 5. INSTRUCTION (bld_instruction body)
        bdir = self.state.builder_dir
        if bdir:
            instr_text = load_iso(bdir, "bld_instruction", self.kind_slug)
            if instr_text:
                sections.append(f"# INSTRUCTION\n\n{strip_frontmatter(instr_text)}")

        # 6. TEMPLATE (bld_output_template body)
        if bdir:
            tpl_text = load_iso(bdir, "bld_output_template", self.kind_slug)
            if tpl_text:
                sections.append(f"# TEMPLATE\n\n{strip_frontmatter(tpl_text)}")

        # 7. TASK (user intent)
        task_lines = [
            f"**Intent**: {self.state.intent}",
            f"**Kind**: {self.state.kind}",
            f"**Pillar**: {self.state.pillar}",
            f"**Verb**: {self.parsed.get('verb', 'cria')}"
            f" ({self.parsed.get('verb_action', 'create')})",
            "**Quality**: set quality: null (NEVER self-score)",
        ]
        sections.append("# TASK\n\n" + "\n".join(task_lines))

        prompt = "\n\n---\n\n".join(sections)

        if self.dry_run:
            self.state.artifact = prompt
            self._log("F6", f"dry-run prompt composed ({len(prompt.split())} words)")
        else:
            self._log("F6", f"executing prompt ({len(prompt.split())} words)...")
            response = execute_prompt(prompt)
            self.state.artifact = response
            self._log("F6", f"LLM response received ({len(response)} chars)")

    # -- F8 COLLABORATE -----------------------------------------------------

    def f8_collaborate(self):
        """Save artifact to file, compile -> state.result."""
        if self.dry_run:
            # In dry-run, just report the prompt
            out_path = None
            if self.output_dir:
                out_path = Path(self.output_dir) / f"{self.state.kind}_prompt.md"
                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_text(self.state.artifact, encoding="utf-8")
                self._log("F8", f"prompt saved to {out_path}")

            self.state.result = {
                "path": str(out_path) if out_path else None,
                "compiled": False,
                "committed": False,
                "mode": "dry-run",
                "prompt_words": len(self.state.artifact.split()),
            }
        else:
            # Execute mode: save artifact
            out_dir = self.output_dir or (
                CEX_ROOT / PILLAR_DIRS.get(self.state.pillar, "P01_knowledge") / "examples"
            )
            out_dir = Path(out_dir)
            out_dir.mkdir(parents=True, exist_ok=True)

            # Generate filename from intent
            slug = re.sub(r"[^a-z0-9]+", "_", self.state.intent.lower()).strip("_")[:40]
            filename = f"{self.state.pillar.lower()}_{self.state.kind}_{slug}.md"
            out_path = out_dir / filename

            out_path.write_text(self.state.artifact, encoding="utf-8")
            self._log("F8", f"artifact saved to {out_path}")

            # Try compile
            compiled = False
            try:
                compile_script = CEX_ROOT / "_tools" / "cex_compile.py"
                if compile_script.exists():
                    import subprocess

                    subprocess.run(
                        [sys.executable, str(compile_script), str(out_path)],
                        capture_output=True,
                        timeout=30,
                    )
                    compiled = True
            except Exception as e:
                self._log("F8", f"compile skipped: {e}")

            self.state.result = {
                "path": str(out_path),
                "compiled": compiled,
                "committed": False,
                "mode": "execute",
            }

    # -- run() pipeline -----------------------------------------------------

    def run(self, stop_at: int | None = None) -> RunState:
        """Execute F1->F2->F3->F6->F8 pipeline (wave 1: skip F4,F5,F7)."""
        steps = [
            ("F1", self.f1_constrain),
            ("F2", self.f2_become),
            ("F3", self.f3_inject),
            # F4 REASON  -- wave 2
            # F5 CALL    -- wave 3
            ("F6", self.f6_produce),
            # F7 GOVERN  -- wave 2
            ("F8", self.f8_collaborate),
        ]

        step_num = 0
        for name, func in steps:
            step_num += 1
            self._timed(name, func)
            if stop_at and step_num >= stop_at:
                self._log("run", f"stopped at step {step_num} (--step {stop_at})")
                break

        return self.state


# ---------------------------------------------------------------------------
# CLI: list-kinds
# ---------------------------------------------------------------------------


def list_kinds():
    """Print all available kinds grouped by pillar."""
    by_pillar: dict[str, list[tuple[str, str]]] = {}
    seen = set()
    for keyword, kinds_list in sorted(OBJECT_TO_KINDS.items()):
        for kind, pillar, fn in kinds_list:
            key = (kind, pillar)
            if key not in seen:
                seen.add(key)
                by_pillar.setdefault(pillar, []).append((kind, fn))

    print("\n=== CEX Kinds (8F Runner) ===\n")
    for pillar in sorted(by_pillar.keys()):
        kinds = sorted(by_pillar[pillar], key=lambda x: x[0])
        print(f"\n  {pillar}:")
        for kind, fn in kinds:
            bdir = find_builder_dir(kind)
            has = "+" if bdir else " "
            print(f"    {has} {kind:<30s} [{fn}]")
    print(f"\n  Total: {len(seen)} kinds")
    print("  + = builder exists in archetypes/builders/\n")


# ---------------------------------------------------------------------------
# CLI: banner
# ---------------------------------------------------------------------------


def print_banner(state: RunState, elapsed_ms: float):
    """Print run summary banner."""
    print(f"\n{'=' * 70}")
    print("  CEX 8F Runner -- Stateful Artifact Pipeline")
    print(f"{'=' * 70}")
    print(f"  Intent:      {state.intent}")
    print(f"  Kind:        {state.kind}")
    print(f"  Pillar:      {state.pillar}")
    print(f"  Builder:     {state.builder_dir or 'NONE'}")
    print(f"  Mode:        {'DRY-RUN' if state.result.get('mode') == 'dry-run' else 'EXECUTE'}")

    # Constraints summary
    c = state.constraints
    parts = []
    if c.get("max_bytes"):
        parts.append(f"max={c['max_bytes']}b")
    if c.get("id_pattern"):
        parts.append(f"id=/{c['id_pattern']}/")
    if c.get("frontmatter_required"):
        parts.append(f"fm={len(c['frontmatter_required'])} fields")
    if parts:
        print(f"  Constraints: {', '.join(parts)}")

    # Knowledge summary
    k = state.knowledge
    kc_count = len(k.get("kc_domains", []))
    kc_parts = []
    if k.get("kc_builder"):
        kc_parts.append("builder-KC")
    if kc_count:
        kc_parts.append(f"{kc_count} domain-KCs")
    if k.get("few_shots"):
        kc_parts.append("examples")
    if k.get("memory"):
        kc_parts.append("memory")
    if k.get("architecture"):
        kc_parts.append("architecture")
    print(f"  Knowledge:   {', '.join(kc_parts) if kc_parts else 'none'}")

    # Artifact
    if state.artifact:
        words = len(state.artifact.split())
        sections = state.artifact.count("\n# ")
        print(f"  Artifact:    {words} words, {sections} sections")

    # Output
    if state.result.get("path"):
        print(f"  Output:      {state.result['path']}")

    # Timing
    if state.timings:
        timing_str = " | ".join(f"{k}={v}ms" for k, v in state.timings.items())
        print(f"  Timing:      {timing_str} | total={elapsed_ms:.0f}ms")

    # Errors
    if state.errors:
        for err in state.errors:
            print(f"  ! ERROR: {err}")

    print(f"{'=' * 70}\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="cex_8f_runner.py -- 8F Stateful Artifact Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cex_8f_runner.py "create a chunking config for markdown"
  python cex_8f_runner.py "create agent for sales" --execute
  python cex_8f_runner.py --kind chunk_strategy --dry-run
  python cex_8f_runner.py --list-kinds
  python cex_8f_runner.py "create eval" --step 3 --verbose
        """,
    )
    parser.add_argument("intent", nargs="?", help="Natural language intent")
    parser.add_argument("--kind", help="Override kind classification (skip Motor)")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Show composed prompt without LLM call (default)",
    )
    parser.add_argument("--execute", action="store_true", help="Call LLM to produce artifact")
    parser.add_argument("--list-kinds", action="store_true", help="Print all available kinds")
    parser.add_argument("--verbose", action="store_true", help="Show per-F details")
    parser.add_argument("--step", type=int, metavar="N", help="Stop after function N (1-8)")
    parser.add_argument("--output-dir", metavar="DIR", help="Save outputs to this directory")

    args = parser.parse_args()

    if args.list_kinds:
        list_kinds()
        return

    if not args.intent and not args.kind:
        parser.print_help()
        sys.exit(1)

    intent = args.intent or f"create {args.kind}"
    dry_run = not args.execute

    runner = EightFRunner(
        intent=intent,
        kind=args.kind,
        dry_run=dry_run,
        verbose=args.verbose,
        output_dir=args.output_dir,
    )

    t0 = time.perf_counter()
    state = runner.run(stop_at=args.step)
    elapsed = (time.perf_counter() - t0) * 1000

    # Banner
    print_banner(state, elapsed)

    # Show artifact
    if state.artifact:
        if state.result.get("mode") == "dry-run":
            print("--- STRUCTURED PROMPT (8F) ---\n")
            print(state.artifact)
            print(f"\n--- END ({len(state.artifact.split())} words) ---")
        else:
            print("--- ARTIFACT ---\n")
            print(state.artifact[:2000])
            if len(state.artifact) > 2000:
                print(f"\n... (truncated, full: {len(state.artifact)} chars)")


if __name__ == "__main__":
    main()
