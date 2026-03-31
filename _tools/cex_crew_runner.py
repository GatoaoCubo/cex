#!/usr/bin/env python3
"""
cex_crew_runner.py -- Crew Runner: Lightweight DAG Executor for CEX

LangGraph-inspired state machine that executes CEX builder plans produced
by Motor 8F. Zero external deps beyond PyYAML (optional).

Design principles (from CREW_PATTERNS_RESEARCH.md Section 5):
  - Explicit DAG (not full LangGraph/CrewAI)
  - Typed state flow (BuilderOutput, RunState)
  - JSON plan as input (Motor 8F output)
  - Fixed token budget per builder (~7500 tokens for ISOs)
  - Graceful degradation: score >= 7.0 -> advance, < 7.0 -> retry, exhausted -> degrade

Modes:
  --dry-run  (DEFAULT): Generate prompts, save to files. No LLM calls.
  --execute:            Call LLM via anthropic SDK, apply quality gates.

Usage:
  python cex_crew_runner.py --plan plan.json --output-dir out/
  python cex_crew_runner.py --plan plan.json --step 2 --output-dir out/
  python cex_crew_runner.py --plan plan.json --execute --output-dir out/

Full pipeline:
  python cex_8f_motor.py --intent "cria agente de vendas" --output /tmp/plan.json
  python cex_crew_runner.py --plan /tmp/plan.json --output-dir /tmp/crew_out/
"""

import sys
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")

import json
import argparse
from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime

try:
    import yaml  # noqa: F401 — optional, for future config loading
except ImportError:
    yaml = None


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CEX_ROOT = Path(__file__).resolve().parent.parent
BUILDER_DIR = CEX_ROOT / "archetypes" / "builders"
BUILDER_MAX_BYTES = 30 * 1024  # 30KB total budget for builder ISO injection
DEFAULT_QUALITY_GATE = 7.0
MAX_RETRIES = 2
LLM_MODEL = "claude-sonnet-4-20250514"
LLM_MAX_TOKENS = 8000
FORK_OUTPUT_DIR = CEX_ROOT / ".cex" / "temp" / "fork_outputs"


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------


@dataclass
class BuilderOutput:
    """Result of a single builder execution."""

    builder_id: str
    content: str = ""
    quality_score: float = 0.0
    metadata: dict = field(default_factory=dict)
    status: str = "pending"  # pending | complete | degraded | failed


@dataclass
class RunState:
    """Mutable state that flows through the execution pipeline."""

    intent: str
    plan: dict
    outputs: dict = field(default_factory=dict)  # builder_id -> BuilderOutput
    current_step: int = 0
    retry_counts: dict = field(default_factory=dict)  # builder_id -> int
    warnings: list = field(default_factory=list)
    started_at: str = ""
    completed_at: str = ""


# ---------------------------------------------------------------------------
# Builder Context Loader
# ---------------------------------------------------------------------------

# Priority order for ISO file types within a builder directory
_ISO_PRIORITY = [
    "manifest",
    "instruction",
    "knowledge",
    "quality",
    "schema",
    "example",
    "config",
    "template",
]


def _iso_sort_key(filepath: Path) -> int:
    """Sort ISO files by content priority (manifest first, examples last)."""
    name = filepath.name.lower()
    for i, kw in enumerate(_ISO_PRIORITY):
        if kw in name:
            return i
    return len(_ISO_PRIORITY)


def load_builder_context(builder_id: str, builder_dir: Path = BUILDER_DIR) -> str:
    """Load ISO files for a builder.

    Scans archetypes/builders/{builder-id}/ for .md files.
    Budget: 30KB max. Files loaded in priority order.
    """
    builder_path = builder_dir / builder_id
    if not builder_path.exists():
        return f"[Builder '{builder_id}' not found at {builder_path}]"

    # Collect .md files (try bld_* pattern first, then any .md)
    md_files = sorted(builder_path.glob("bld_*.md"), key=_iso_sort_key)
    if not md_files:
        md_files = sorted(builder_path.glob("*.md"), key=_iso_sort_key)

    if not md_files:
        return f"[No ISO files found for builder '{builder_id}']"

    sections = []
    total_bytes = 0

    for f in md_files:
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue

        content_bytes = len(content.encode("utf-8"))
        if total_bytes + content_bytes > BUILDER_MAX_BYTES:
            sections.append(f"\n[... truncated at {BUILDER_MAX_BYTES // 1024}KB budget ...]")
            break

        sections.append(f"### {f.name}")
        sections.append(content.strip())
        sections.append("")
        total_bytes += content_bytes

    return "\n".join(sections)


# ---------------------------------------------------------------------------
# Prompt Composer
# ---------------------------------------------------------------------------


def _load_builder_memories(builder_id: str, intent: str) -> str:
    """Load relevant memories for a builder. Returns formatted injection or empty string."""
    try:
        from cex_memory_select import select_relevant_memories, format_memory_injection
        from cex_memory import scan_builder_memories

        headers = scan_builder_memories(builder_id)
        if not headers:
            return ""

        selected = select_relevant_memories(
            query=intent,
            memories=headers,
            builder_id=builder_id,
            top_k=5,
            use_cache=True,
        )
        if not selected:
            return ""

        return format_memory_injection(selected, total_observations=len(headers))
    except Exception:
        return ""


def compose_prompt(
    builder_id: str,
    function_name: str,
    intent: str,
    parsed: dict,
    quality_target: float,
    state: RunState,
    builder_dir: Path = BUILDER_DIR,
    retry_feedback: str = "",
) -> str:
    """Compose full prompt for a builder: ISOs + intent + prior outputs.

    Each builder gets:
    1. Header with execution context
    2. Builder ISO files (capped at 30KB)
    3. Relevant prior outputs (from earlier pipeline steps)
    4. Retry feedback (if retrying after quality gate failure)
    5. Execution instructions
    """
    parts = []

    # --- Header ---
    parts.append(f"# CEX Crew Runner -- Builder Execution")
    parts.append(f"**Builder**: `{builder_id}`")
    parts.append(f"**Function**: {function_name}")
    parts.append(f"**Intent**: {intent}")
    parts.append(f"**Quality Target**: >= {quality_target}")
    parts.append(f"**Timestamp**: {datetime.now().isoformat()}")
    parts.append("")

    # --- Intent Context ---
    parts.append("## Intent Context")
    parts.append(f"- **Verb**: {parsed.get('verb', 'N/A')}")
    obj = parsed.get("object", "N/A")
    if isinstance(obj, list):
        parts.append(f"- **Objects**: {', '.join(obj)}")
    else:
        parts.append(f"- **Object**: {obj}")
    parts.append(f"- **Domain**: {parsed.get('domain', 'N/A')}")
    parts.append(f"- **Multi-object**: {parsed.get('multi_object', False)}")
    parts.append("")

    # --- Builder ISO Context ---
    parts.append("## Builder Context (ISO Files)")
    context = load_builder_context(builder_id, builder_dir)
    parts.append(context)
    parts.append("")

    # --- Builder Memory (per-builder, not shared) ---
    memory_block = _load_builder_memories(builder_id, intent)
    if memory_block:
        parts.append(memory_block)

    # --- Prior Outputs ---
    # Only inject outputs from completed earlier steps (not current function)
    prior = {
        bid: out
        for bid, out in state.outputs.items()
        if out.status in ("complete", "degraded")
        and out.content
        and not out.content.startswith("[DRY-RUN]")
    }
    if prior:
        parts.append("## Prior Builder Outputs")
        parts.append("These outputs were produced by earlier pipeline steps.")
        parts.append("Use them as context — do not repeat their work.")
        parts.append("")
        for bid, out in prior.items():
            parts.append(f"### {bid} (score: {out.quality_score:.1f})")
            content = out.content
            if len(content) > 2000:
                content = content[:2000] + "\n\n[... truncated to 2KB ...]"
            parts.append(content)
            parts.append("")

    # --- Retry Feedback ---
    if retry_feedback:
        parts.append("## Retry Feedback")
        parts.append("Your previous attempt did not pass the quality gate.")
        parts.append(retry_feedback)
        parts.append("")

    # --- Execution Instructions ---
    parts.append("## Execution Instructions")
    parts.append(
        f"1. You are executing builder `{builder_id}` for pipeline function `{function_name}`."
    )
    parts.append(f"2. Follow the builder's ISO instructions precisely.")
    parts.append(f"3. Generate the complete output artifact.")
    parts.append(
        f"4. Quality target: >= {quality_target} (no filler, no repetition, no platitudes)."
    )
    parts.append(f"5. At the end, self-assess with: `quality: X.X`")
    parts.append("")

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Crew Runner
# ---------------------------------------------------------------------------


class CrewRunner:
    """Lightweight DAG executor for CEX builder plans."""

    def __init__(self, plan: dict, cex_root: Path = CEX_ROOT):
        self.plan = plan
        self.cex_root = cex_root
        self.builder_dir = cex_root / "archetypes" / "builders"
        self.intent = plan.get("intent", "")
        self.parsed = plan.get("parsed", {})
        self.functions = plan.get("functions", [])
        self.quality_target = self.parsed.get("quality", 9.0)

    def _get_active_builders(self, step: dict) -> list[dict]:
        """Filter to only active builders in a step."""
        return [b for b in step.get("builders", []) if b.get("active")]

    def _resolve_fork_context(self, builder: dict) -> str:
        """Determine execution mode for a builder based on fork_context.

        Returns: "fork" | "inline"
        """
        fc = builder.get("fork_context")
        if fc == "fork":
            return "fork"
        if fc == "inline" or fc is None:
            return "inline"
        # null -> runtime decides based on complexity
        return "inline"  # default to inline

    def _resolve_model(self, builder: dict) -> tuple[str, int]:
        """Resolve LLM model and max_tokens from builder effort config.

        Returns: (model_id, max_tokens)
        """
        model = builder.get("model", LLM_MODEL)
        max_tokens = builder.get("model_max_tokens", LLM_MAX_TOKENS)
        return model, max_tokens

    def _check_max_turns(self, builder_id: str, state: RunState) -> tuple[bool, int]:
        """Check if builder has exceeded max_turns. Returns (allowed, turns_used)."""
        turns_key = f"_turns_{builder_id}"
        turns_used = state.retry_counts.get(turns_key, 0)
        # Find max_turns from plan's builder entries
        max_turns = None
        for fn in self.functions:
            for b in fn.get("builders", []):
                if b["id"] == builder_id and b.get("max_turns"):
                    max_turns = b["max_turns"]
                    break
        if max_turns and turns_used >= max_turns:
            return False, turns_used
        # Increment
        state.retry_counts[turns_key] = turns_used + 1
        return True, turns_used + 1

    def _check_tool_allowed(self, tool_name: str, builder: dict) -> tuple[bool, str]:
        """Check if a tool is allowed for a builder."""
        denied = builder.get("denied_tools", [])
        if not denied:
            return True, "no deny list"
        if tool_name.lower() in [d.lower() for d in denied]:
            return False, f"tool '{tool_name}' is denied for builder '{builder['id']}'"
        return True, "allowed"

    def _execute_forked(
        self, builder: dict, prompt: str, model: str, max_tokens: int, output_dir: Path | None
    ) -> BuilderOutput:
        """Execute a builder in a forked sub-process (isolated context).

        The forked builder:
        - Inherits: builder ISOs + selected memory + query context
        - Does NOT inherit: context of other builders in the crew
        - Result returns via output file
        """
        bid = builder["id"]
        FORK_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        fork_file = FORK_OUTPUT_DIR / f"fork_{bid}_{datetime.now().strftime('%H%M%S')}.md"
        prompt_file = FORK_OUTPUT_DIR / f"fork_{bid}_prompt.md"

        # Write prompt to file for subprocess
        prompt_file.write_text(prompt, encoding="utf-8")

        try:
            import anthropic
            client = anthropic.Anthropic()
            response = client.messages.create(
                model=model,
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}],
            )
            content = response.content[0].text
            fork_file.write_text(content, encoding="utf-8")

            import re as _re
            score_m = _re.search(r"(?:quality|score)[\s:]*(\d+\.?\d*)", content.lower())
            score = float(score_m.group(1)) if score_m else 7.0

            return BuilderOutput(
                builder_id=bid,
                content=content,
                quality_score=score,
                metadata={
                    "mode": "fork",
                    "model": model,
                    "fork_output": str(fork_file),
                },
                status="complete",
            )
        except ImportError:
            # No SDK — write prompt as dry-run fork
            fork_file.write_text(f"[FORK-DRY-RUN] {bid}\n{prompt[:500]}", encoding="utf-8")
            return BuilderOutput(
                builder_id=bid,
                content=f"[FORK-DRY-RUN] Prompt saved to {fork_file}",
                quality_score=0.0,
                metadata={"mode": "fork-dry-run", "fork_output": str(fork_file)},
                status="complete",
            )
        except Exception as e:
            return BuilderOutput(
                builder_id=bid,
                content=f"[FORK-ERROR] {e}",
                quality_score=0.0,
                metadata={"mode": "fork", "error": str(e)},
                status="failed",
            )

    # --- Dry-Run Execution ---

    def execute_step_dry_run(
        self,
        step: dict,
        state: RunState,
        output_dir: Path | None = None,
    ) -> list[BuilderOutput]:
        """Generate prompts without calling LLM."""
        fn_name = step.get("name", f"step_{step.get('position', '?')}")
        position = step.get("position", 0)
        active = self._get_active_builders(step)
        results = []

        for builder in active:
            bid = builder["id"]
            prompt = compose_prompt(
                bid,
                fn_name,
                self.intent,
                self.parsed,
                self.quality_target,
                state,
                self.builder_dir,
            )
            prompt_bytes = len(prompt.encode("utf-8"))

            if output_dir:
                fname = f"{position:02d}_{fn_name}_{bid}.prompt.md"
                (output_dir / fname).write_text(prompt, encoding="utf-8")
                print(f"  [{fn_name}] {bid} -> {fname} ({prompt_bytes / 1024:.1f}KB)")

            out = BuilderOutput(
                builder_id=bid,
                content=f"[DRY-RUN] Prompt generated for {bid} ({prompt_bytes} bytes)",
                quality_score=0.0,
                metadata={
                    "function": fn_name,
                    "position": position,
                    "tier": builder["tier"],
                    "prompt_bytes": prompt_bytes,
                    "mode": "dry-run",
                },
                status="complete",
            )
            results.append(out)

        return results

    # --- Real Execution ---

    def execute_step_real(
        self,
        step: dict,
        state: RunState,
        output_dir: Path | None = None,
    ) -> list[BuilderOutput]:
        """Execute builders via LLM (anthropic SDK)."""
        fn_name = step.get("name", f"step_{step.get('position', '?')}")
        position = step.get("position", 0)
        active = self._get_active_builders(step)
        results = []

        # Lazy import — only needed in execute mode
        try:
            import anthropic

            client = anthropic.Anthropic()
        except ImportError:
            print("WARN: anthropic SDK not installed. Falling back to dry-run.", file=sys.stderr)
            return self.execute_step_dry_run(step, state, output_dir)
        except Exception as e:
            print(
                f"WARN: Anthropic client init failed: {e}. Falling back to dry-run.",
                file=sys.stderr,
            )
            return self.execute_step_dry_run(step, state, output_dir)

        for builder in active:
            bid = builder["id"]

            # Max turns check
            allowed, turns = self._check_max_turns(bid, state)
            if not allowed:
                out = BuilderOutput(
                    builder_id=bid,
                    content=f"[MAX-TURNS] Builder '{bid}' reached max_turns limit ({turns})",
                    quality_score=0.0,
                    metadata={"turns_used": turns, "max_turns_exceeded": True},
                    status="degraded",
                )
                state.warnings.append(f"{bid}: max_turns exceeded ({turns})")
                results.append(out)
                continue

            retries = state.retry_counts.get(bid, 0)
            retry_feedback = ""
            out = None

            # Resolve model from effort config
            model, max_tokens = self._resolve_model(builder)

            # Check fork context
            fork_mode = self._resolve_fork_context(builder)

            while retries <= MAX_RETRIES:
                prompt = compose_prompt(
                    bid,
                    fn_name,
                    self.intent,
                    self.parsed,
                    self.quality_target,
                    state,
                    self.builder_dir,
                    retry_feedback=retry_feedback,
                )

                # Fork execution path
                if fork_mode == "fork":
                    out = self._execute_forked(builder, prompt, model, max_tokens, output_dir)
                    if out.quality_score >= DEFAULT_QUALITY_GATE or out.status == "failed":
                        break
                    retries += 1
                    state.retry_counts[bid] = retries
                    retry_feedback = f"Fork score {out.quality_score:.1f} < gate. Retry {retries + 1}."
                    if retries > MAX_RETRIES:
                        out.status = "degraded"
                    continue

                # Inline execution path (original)
                try:
                    import re

                    response = client.messages.create(
                        model=model,
                        max_tokens=max_tokens,
                        messages=[{"role": "user", "content": prompt}],
                    )
                    content = response.content[0].text

                    # Extract self-assessed quality score
                    score_m = re.search(
                        r"(?:quality|score)[\s:]*(\d+\.?\d*)",
                        content.lower(),
                    )
                    score = float(score_m.group(1)) if score_m else 7.0

                    out = BuilderOutput(
                        builder_id=bid,
                        content=content,
                        quality_score=score,
                        metadata={
                            "function": fn_name,
                            "position": position,
                            "tier": builder["tier"],
                            "retries": retries,
                            "model": LLM_MODEL,
                            "mode": "execute",
                        },
                        status="complete",
                    )

                    if score >= DEFAULT_QUALITY_GATE:
                        break

                    retries += 1
                    state.retry_counts[bid] = retries
                    retry_feedback = (
                        f"Score {score:.1f} < gate {DEFAULT_QUALITY_GATE}. "
                        f"Improve quality. "
                        f"Attempt {retries + 1}/{MAX_RETRIES + 1}."
                    )

                    if retries > MAX_RETRIES:
                        out.status = "degraded"
                        state.warnings.append(
                            f"{bid}: degraded after {MAX_RETRIES + 1} attempts (score: {score:.1f})"
                        )
                        break

                except Exception as e:
                    out = BuilderOutput(
                        builder_id=bid,
                        content=f"[ERROR] {e}",
                        quality_score=0.0,
                        metadata={"error": str(e), "retries": retries},
                        status="failed",
                    )
                    state.warnings.append(f"{bid}: failed -- {e}")
                    break

            if out is None:
                out = BuilderOutput(
                    builder_id=bid,
                    content="[ERROR] No output produced",
                    status="failed",
                )

            # Save output file
            if output_dir and out.content:
                ext = "error.md" if out.status == "failed" else "output.md"
                fname = f"{position:02d}_{fn_name}_{bid}.{ext}"
                (output_dir / fname).write_text(out.content, encoding="utf-8")
                print(
                    f"  [{fn_name}] {bid} -> {fname} "
                    f"(score: {out.quality_score:.1f}, "
                    f"status: {out.status})"
                )

            results.append(out)

        return results

    # --- Main Run Loop ---

    def run(
        self,
        dry_run: bool = True,
        output_dir: Path | None = None,
        step_filter: int | None = None,
    ) -> RunState:
        """Execute the full plan (or a single step).

        Args:
            dry_run: If True, generate prompts only. If False, call LLM.
            output_dir: Directory for output files. Created if needed.
            step_filter: If set, only execute the function at this position.

        Returns:
            RunState with all outputs and metadata.
        """
        state = RunState(
            intent=self.intent,
            plan=self.plan,
            started_at=datetime.now().isoformat(),
        )

        # Sort functions by pipeline position
        functions = sorted(self.functions, key=lambda f: f.get("position", 99))

        if step_filter is not None:
            functions = [f for f in functions if f.get("position") == step_filter]
            if not functions:
                print(f"WARN: No function at position {step_filter}", file=sys.stderr)

        if output_dir:
            output_dir.mkdir(parents=True, exist_ok=True)

        mode_str = "DRY-RUN" if dry_run else "EXECUTE"
        total_active = sum(len(self._get_active_builders(fn)) for fn in functions)

        # --- Banner ---
        print(f"\n{'=' * 60}")
        print(f"CEX Crew Runner -- {mode_str}")
        print(f"Intent: {self.intent}")
        print(f"Functions: {len(functions)} | Active builders: {total_active}")
        print(f"Quality target: {self.quality_target}")
        if output_dir:
            print(f"Output: {output_dir}")
        print(f"{'=' * 60}\n")

        # --- Execute each function in order ---
        for fn in functions:
            fn_name = fn.get("name", "?")
            position = fn.get("position", 0)
            active_count = len(self._get_active_builders(fn))

            if active_count == 0:
                print(f"[{position}] {fn_name}: skipped (0 active builders)")
                continue

            print(f"[{position}] {fn_name}: {active_count} builder(s)")
            state.current_step = position

            if dry_run:
                outputs = self.execute_step_dry_run(fn, state, output_dir)
            else:
                outputs = self.execute_step_real(fn, state, output_dir)

            for out in outputs:
                state.outputs[out.builder_id] = out

        state.completed_at = datetime.now().isoformat()

        # --- Summary ---
        completed = sum(1 for o in state.outputs.values() if o.status == "complete")
        degraded = sum(1 for o in state.outputs.values() if o.status == "degraded")
        failed = sum(1 for o in state.outputs.values() if o.status == "failed")

        print(f"\n{'=' * 60}")
        print(f"COMPLETE -- {mode_str}")
        print(f"Builders: {completed} complete, {degraded} degraded, {failed} failed")

        if state.warnings:
            print(f"\nWarnings ({len(state.warnings)}):")
            for w in state.warnings:
                print(f"  - {w}")

        # --- Save run state ---
        if output_dir:
            state_dict = {
                "intent": state.intent,
                "mode": mode_str.lower().replace("-", "_"),
                "started_at": state.started_at,
                "completed_at": state.completed_at,
                "current_step": state.current_step,
                "quality_target": self.quality_target,
                "builders": {
                    bid: {
                        "status": out.status,
                        "quality_score": out.quality_score,
                        "metadata": out.metadata,
                    }
                    for bid, out in state.outputs.items()
                },
                "warnings": state.warnings,
                "summary": {
                    "total": len(state.outputs),
                    "complete": completed,
                    "degraded": degraded,
                    "failed": failed,
                },
            }

            state_file = output_dir / "_run_state.json"
            state_file.write_text(
                json.dumps(state_dict, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            print(f"\nRun state: {state_file}")

            # Also save a manifest of all generated files
            manifest = {
                "generated_at": state.completed_at,
                "mode": mode_str.lower(),
                "intent": state.intent,
                "files": sorted(
                    f.name for f in output_dir.glob("*.md") if not f.name.startswith("_")
                ),
                "total_files": len(list(output_dir.glob("*.md"))),
                "total_bytes": sum(f.stat().st_size for f in output_dir.glob("*.md")),
            }
            manifest_file = output_dir / "_manifest.json"
            manifest_file.write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

        print(f"{'=' * 60}\n")
        return state


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="CEX Crew Runner -- Lightweight DAG Executor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry-run (default) -- generate prompts:
  python cex_crew_runner.py --plan plan.json --output-dir out/

  # Single step only:
  python cex_crew_runner.py --plan plan.json --step 2 --output-dir out/

  # Real execution (calls LLM):
  python cex_crew_runner.py --plan plan.json --execute --output-dir out/

  # Full pipeline:
  python cex_8f_motor.py --intent "cria agente" --output /tmp/plan.json
  python cex_crew_runner.py --plan /tmp/plan.json --output-dir /tmp/crew/
        """,
    )
    parser.add_argument("--plan", required=True, help="Path to Motor 8F plan JSON")
    parser.add_argument("--output-dir", help="Output directory for prompts/outputs")
    parser.add_argument("--step", type=int, help="Execute only this step (by position 1-8)")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Generate prompts without LLM calls (DEFAULT)",
    )
    parser.add_argument(
        "--execute", action="store_true", help="Real execution -- calls LLM via anthropic SDK"
    )

    args = parser.parse_args()

    # Load plan
    plan_path = Path(args.plan)
    if not plan_path.exists():
        print(f"ERRO: Plan file not found: {plan_path}", file=sys.stderr)
        sys.exit(1)

    with open(plan_path, "r", encoding="utf-8") as f:
        plan = json.load(f)

    # Validate plan has expected structure
    if "functions" not in plan:
        print(
            "ERRO: Plan JSON missing 'functions' key. Is this a Motor 8F output?", file=sys.stderr
        )
        sys.exit(1)

    dry_run = not args.execute
    output_dir = Path(args.output_dir) if args.output_dir else None

    runner = CrewRunner(plan)
    state = runner.run(
        dry_run=dry_run,
        output_dir=output_dir,
        step_filter=args.step,
    )

    # Exit code: 1 if any builder failed
    failed = sum(1 for o in state.outputs.values() if o.status == "failed")
    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
