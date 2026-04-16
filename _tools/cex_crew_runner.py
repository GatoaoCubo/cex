#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_crew_runner.py -- Crew Runner: Lightweight DAG Executor for CEX

LangGraph-inspired state machine that executes CEX builder plans produced
by Motor 8F. Zero external deps beyond PyYAML (optional).

Design principles (from CREW_PATTERNS_RESEARCH.md Section 5):
  - Explicit DAG (not full LangGraph/CrewAI)
  - Typed state flow (BuilderOutput, RunState)
  - JSON plan as input (Motor 8F output)
  - Fixed token budget per builder (~7500 tokens for specs)
  - Graceful degradation: score >= 7.0 -> advance, < 7.0 -> retry, exhausted -> degrade

Modes:
  --dry-run  (DEFAULT): Generate prompts, save to files. No LLM calls.
  --execute:            Call LLM via claude CLI (subscription), apply quality gates.

Usage:
  python cex_crew_runner.py --plan plan.json --output-dir out/
  python cex_crew_runner.py --plan plan.json --step 2 --output-dir out/
  python cex_crew_runner.py --plan plan.json --execute --output-dir out/

Full pipeline:
  python cex_8f_motor.py --intent "cria agente de vendas" --output /tmp/plan.json
  python cex_crew_runner.py --plan /tmp/plan.json --output-dir /tmp/crew_out/
"""

import subprocess
import sys
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")

import json
import os
import re
import argparse
from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime

try:
    import yaml  # noqa: F401 -- optional, for future config loading
except ImportError:
    yaml = None


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CEX_ROOT = Path(__file__).resolve().parent.parent
ROOT = CEX_ROOT  # alias used by fork/inline execution paths
BUILDER_DIR = CEX_ROOT / "archetypes" / "builders"
BUILDER_MAX_BYTES = 30 * 1024  # 30KB total budget for builder spec injection
DEFAULT_QUALITY_GATE = 7.0
MAX_RETRIES = 2
# Short alias = subscription auth. Full ID = API credits (may be depleted).
LLM_MODEL = "sonnet"
LLM_MAX_TOKENS = 8000
FORK_OUTPUT_DIR = CEX_ROOT / ".cex" / "temp" / "fork_outputs"

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def _parse_md_frontmatter(text: str) -> dict:
    """YAML frontmatter parser.

    Prefers PyYAML when available (handles nested mappings like budget: {tokens, usd}).
    Falls back to a minimal parser (scalar keys + simple lists only) when PyYAML
    is missing, so callers never crash in bare environments.
    """
    m = _FM_RE.match(text)
    if not m:
        return {}
    raw = m.group(1)
    try:
        import yaml  # type: ignore
        loaded = yaml.safe_load(raw)
        return loaded if isinstance(loaded, dict) else {}
    except Exception:
        pass
    fm: dict = {}
    key = None
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if line.startswith("  - ") and key:
            val = line[4:].strip().strip('"').strip("'")
            if not isinstance(fm.get(key), list):
                fm[key] = []
            fm[key].append(val)
        elif ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            k = k.strip()
            v = v.strip()
            key = k
            if not v:
                fm[k] = []
            else:
                fm[k] = v.strip('"').strip("'")
    return fm


# ---------------------------------------------------------------------------
# Prompt Layers (compiled artifacts from pillar directories)
# ---------------------------------------------------------------------------
_prompt_layers = None


def _get_prompt_layers():
    """Get PromptLayers singleton (lazy import)."""
    global _prompt_layers
    if _prompt_layers is None:
        try:
            from cex_prompt_layers import get_layers
            _prompt_layers = get_layers()
        except ImportError:
            _prompt_layers = None
    return _prompt_layers


# 8F functions that receive guardrails (write-capable phases)
_GUARDRAIL_FUNCTIONS = {"CALL", "PRODUCE", "COLLABORATE"}
# 8F functions that receive verification protocol (quality gate)
_VERIFICATION_FUNCTIONS = {"GOVERN"}

# Compaction and memory extract thresholds
COMPACT_TRIGGER_RATIO = 0.85  # trigger compaction at 85% context budget
MEMORY_EXTRACT_INTERVAL = 5   # extract memories every N builder executions
_execution_counter = 0


# ---------------------------------------------------------------------------
# Wire 6: Context Compaction Trigger
# ---------------------------------------------------------------------------


def check_compaction_needed(prompt_text: str, max_tokens: int = 8192) -> dict:
    """Check if context compaction should be triggered.

    Returns: {"needed": bool, "usage_ratio": float, "skill_body": str}
    The caller decides whether to compact; this just checks and provides the skill.
    """
    try:
        from cex_token_budget import count_tokens
        current_tokens = count_tokens(prompt_text)
    except ImportError:
        # Fallback: ~1.3 tokens per word
        current_tokens = int(len(prompt_text.split()) * 1.3)

    ratio = current_tokens / max_tokens if max_tokens > 0 else 0

    result = {"needed": False, "usage_ratio": ratio, "skill_body": ""}

    if ratio >= COMPACT_TRIGGER_RATIO:
        result["needed"] = True
        layers = _get_prompt_layers()
        if layers:
            result["skill_body"] = layers.get("p04_skill_compact")

    return result


# ---------------------------------------------------------------------------
# Wire 7: Memory Extract Trigger
# ---------------------------------------------------------------------------


def check_memory_extract_needed() -> dict:
    """Check if background memory extraction should run.

    Returns: {"needed": bool, "skill_body": str, "counter": int}
    Called after each builder execution. Triggers every N executions.
    """
    global _execution_counter
    _execution_counter += 1

    result = {
        "needed": False,
        "skill_body": "",
        "counter": _execution_counter,
    }

    if _execution_counter % MEMORY_EXTRACT_INTERVAL == 0:
        result["needed"] = True
        layers = _get_prompt_layers()
        if layers:
            result["skill_body"] = layers.get("p04_skill_memory_extract")

    return result


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

# Priority order for builder spec file types within a builder directory
_SPEC_PRIORITY = [
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
    """Sort builder spec files by content priority (manifest first, examples last)."""
    name = filepath.name.lower()
    for i, kw in enumerate(_SPEC_PRIORITY):
        if kw in name:
            return i
    return len(_SPEC_PRIORITY)


def load_builder_context(builder_id: str, builder_dir: Path = BUILDER_DIR) -> str:
    """Load builder spec files (bld_*.md) for a builder.

    Strategy: Try SkillLoader first (handles sort, shared skills, conditionals).
    Fallback: manual glob (original behavior).
    Budget: 30KB max.
    """
    # --- T01: SkillLoader path (preferred) ---
    try:
        from cex_skill_loader import SkillLoader
        sl = SkillLoader()
        kind = builder_id.replace("-builder", "")
        isos = sl.load_builder(kind)
        if isos:
            sections = []
            total_bytes = 0
            for iso in isos:
                block = iso.get_prompt()
                block_bytes = len(block.encode("utf-8"))
                if total_bytes + block_bytes > BUILDER_MAX_BYTES:
                    sections.append(f"\n[... truncated at {BUILDER_MAX_BYTES // 1024}KB budget ...]")
                    break
                sections.append(f"### {iso.name}")
                sections.append(block.strip())
                sections.append("")
                total_bytes += block_bytes
            if sections:
                return "\n".join(sections)
    except Exception:
        pass  # D1: graceful fallback

    # --- Fallback: manual glob (original) ---
    builder_path = builder_dir / builder_id
    if not builder_path.exists():
        return f"[Builder '{builder_id}' not found at {builder_path}]"

    md_files = sorted(builder_path.glob("bld_*.md"), key=_iso_sort_key)
    if not md_files:
        md_files = sorted(builder_path.glob("*.md"), key=_iso_sort_key)

    if not md_files:
        return f"[No builder spec files found for builder '{builder_id}']"

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
    """Load relevant memories for a builder.

    T07: Enriched with memory type labels + freshness caveats.
    """
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

        base = format_memory_injection(selected, total_observations=len(headers))

        # --- T07: Enrich with type + freshness ---
        try:
            from cex_memory_age import memory_freshness_tag
            from cex_memory_types import parse_memory_type
            enrichments = []
            for s in selected:
                tags = []
                if hasattr(s, "type") and s.type:
                    tags.append(f"type={s.type}")
                if hasattr(s, "path") and s.path:
                    import os
                    try:
                        tag = memory_freshness_tag(os.path.getmtime(s.path))
                        tags.append(tag)
                    except Exception:
                        pass
                if tags:
                    enrichments.append(f"  [{', '.join(tags)}]")
            if enrichments:
                base += "\n" + "\n".join(enrichments)
        except Exception:
            pass  # enrichment is optional

        return base
    except Exception:
        return ""


def _load_relevant_kcs(intent: str, parsed: dict) -> str:
    """Load KCs relevant to the current intent via pure Python (local TF-IDF).

    Uses two strategies (zero external dependencies):
    1. feeds_kinds: find KCs that explicitly feed the target kind (motor KC library)
    2. semantic search: TF-IDF similarity via cex_retriever (local index)

    Falls back gracefully if retriever index not built.
    Returns formatted injection block or empty string.
    """
    kcs = []

    # Strategy 1: KCs that feed this kind (explicit link via motor KC library)
    target_kind = ""
    if isinstance(parsed.get("object"), list):
        target_kind = parsed["object"][0] if parsed["object"] else ""
    elif isinstance(parsed.get("object"), str):
        target_kind = parsed["object"]
    target_kind = target_kind.replace("-", "_")

    if target_kind:
        try:
            from cex_8f_motor import load_kc_library, lookup_kcs_for_kind
            kc_library = load_kc_library()
            pillar = parsed.get("pillar", "P01")
            matches = lookup_kcs_for_kind(kc_library, target_kind, pillar)
            for m in matches[:3]:
                kcs.append({
                    "id": m.get("id", ""),
                    "title": m.get("title", m.get("id", "?")),
                    "file_path": m.get("path", ""),
                    "domain": "",
                    "tldr": "",
                    "similarity": 0,
                })
        except Exception:
            pass

    # Strategy 2: TF-IDF semantic search (pure Python, no external services)
    try:
        from cex_retriever import load_index as load_retriever_index
        from cex_retriever import find_similar
        idx = load_retriever_index()
        if idx:
            results = find_similar(intent, index=idx, top_k=3)
            seen_ids = {kc["id"] for kc in kcs}
            for r in results:
                rid = r.get("id", "")
                if rid and rid not in seen_ids:
                    seen_ids.add(rid)
                    kcs.append({
                        "id": rid,
                        "title": r.get("title", r.get("id", "?")),
                        "file_path": r.get("path", ""),
                        "domain": r.get("kind", ""),
                        "tldr": r.get("tldr", ""),
                        "similarity": r.get("score", 0),
                    })
    except Exception:
        pass

    if not kcs:
        return ""

    # Format injection block (cap at 5 KCs, ~2K tokens total)
    parts = ["## Relevant Knowledge Cards (auto-retrieved, pure Python TF-IDF)"]
    parts.append("Use these as domain context. Cite specific facts when relevant.\n")

    for kc in kcs[:5]:
        title = kc.get("title", kc.get("id", "?"))
        tldr = kc.get("tldr", "")
        domain = kc.get("domain", "")
        sim = kc.get("similarity", 0)
        path = kc.get("file_path", "")
        sim_str = f" (sim={sim:.2f})" if sim else ""

        parts.append(f"### KC: {title}{sim_str}")
        if domain:
            parts.append(f"Domain: {domain}")
        if tldr:
            parts.append(f"TLDR: {tldr}")

        # Load actual KC body (truncated) for rich context
        try:
            full_path = Path(__file__).resolve().parent.parent / path
            if full_path.exists():
                content = full_path.read_text(encoding="utf-8")
                # Extract body after frontmatter
                fm_end = content.find("---", 3)
                if fm_end > 0:
                    body = content[fm_end + 3:].strip()[:800]
                    parts.append(body)
        except Exception:
            pass

        parts.append("")

    return "\n".join(parts)


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
    """Compose full prompt for a builder: specs + intent + prior outputs.

    Each builder gets:
    1. Header with execution context
    2. Builder spec files (capped at 30KB)
    3. Relevant prior outputs (from earlier pipeline steps)
    4. Retry feedback (if retrying after quality gate failure)
    5. Execution instructions
    6. Sin lens injection (identity lens from nucleus_sins.yaml)
    """
    parts = []

    # --- Sin Lens Injection (from nucleus_sins.yaml) ---
    try:
        from cex_theme import get_prompt_injection
        nucleus = os.environ.get("CEX_NUCLEUS", "n03").lower()
        sin_injection = get_prompt_injection(nucleus)
        if sin_injection:
            parts.append("## Your Identity Lens")
            parts.append(sin_injection)
            parts.append("")
    except Exception:
        pass  # sin injection is additive, never blocks

    # --- Prompt Layers (Wire 1-4: identity + behavioral + action + guardrails) ---
    layers = _get_prompt_layers()
    if layers:
        # Wire 1: Core identity (loaded FIRST, before everything)
        identity_body = layers.get("p03_sp_cex_core_identity")
        if identity_body:
            # Resolve {{INCLUDE}} directives
            for inc_id in ["p03_ins_doing_tasks", "p03_ins_action_protocol"]:
                inc_body = layers.get(inc_id)
                if inc_body:
                    identity_body = identity_body.replace(
                        "{{INCLUDE " + inc_id + "}}", inc_body
                    )
            # Strip remaining unresolved {{...}} placeholders
            identity_body = re.sub(r"\{\{[A-Z_]+\}\}", "[runtime]", identity_body)
            parts.append("## CEX Agent Identity")
            parts.append(identity_body)
            parts.append("")

        # Wire 4: Guardrails (for write-capable functions)
        if function_name.upper() in _GUARDRAIL_FUNCTIONS:
            guardrail_ids = layers.by_kind("guardrail")
            if guardrail_ids:
                parts.append("## Safety Guardrails (auto-injected)")
                for gid in guardrail_ids:
                    g_body = layers.get(gid)
                    g_meta = layers.get_meta(gid)
                    if g_body:
                        title = g_meta.get("title", gid)
                        severity = g_meta.get("severity", "?")
                        enforcement = g_meta.get("enforcement", "?")
                        parts.append(f"### {title} [severity={severity}, enforcement={enforcement}]")
                        parts.append(g_body)
                        parts.append("")

        # Wire 5: Verification protocol (for GOVERN function)
        if function_name.upper() in _VERIFICATION_FUNCTIONS:
            verify_body = layers.get("p03_sp_verification_agent")
            if verify_body:
                parts.append("## Verification Protocol (F7 GOVERN)")
                parts.append(verify_body)
                parts.append("")
            verify_skill = layers.get("p04_skill_verify")
            if verify_skill:
                parts.append("## Verification Skill")
                parts.append(verify_skill)
                parts.append("")

    # --- Wire: Prompt Compiler (F1 CONSTRAIN injection) ---
    if layers and function_name.upper() == "CONSTRAIN":
        pc_body = layers.get("p03_pc_cex_universal")
        if pc_body:
            parts.append("## Prompt Compiler (Intent Resolution -- F1 CONSTRAIN)")
            parts.append(pc_body)
            parts.append("")

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

    # --- Builder Spec Context ---
    parts.append("## Builder Context (Spec Files)")
    context = load_builder_context(builder_id, builder_dir)
    parts.append(context)
    parts.append("")

    # --- Brand Context Injection ---
    # If brand_config.yaml exists, inject relevant brand variables
    brand_config_path = CEX_ROOT / ".cex" / "brand" / "brand_config.yaml"
    if brand_config_path.exists():
        try:
            from brand_inject import load_brand_config, flatten
            brand_cfg = load_brand_config(brand_config_path)
            if brand_cfg:
                flat = flatten(brand_cfg)
                # Filter out placeholders (still {{...}})
                real = {k: v for k, v in flat.items()
                        if not str(v).startswith("{{") and v}
                if real:
                    parts.append("## Brand Context (auto-injected from .cex/brand/brand_config.yaml)")
                    for k, v in sorted(real.items()):
                        if not k.startswith(("identity.", "archetype.", "voice.",
                                             "audience.", "visual.", "positioning.",
                                             "monetization.")):
                            parts.append(f"- {k}: {v}")
                    parts.append("")
        except ImportError:
            pass  # brand_inject not available, skip silently

    # ================================================================
    # F3 INJECT: Synapse 8-Layer Context Envelope (A1 pattern)
    #
    # Canonical ordering ensures deterministic prompt structure:
    #   L0 Rules     -- .claude/rules/ (already injected above via Wire 1)
    #   L1 Global    -- brand config, nucleus identity (already injected above)
    #   L2 Agent     -- builder specs (already injected above)
    #   L3 Workflow   -- prior outputs from earlier pipeline steps
    #   L4 Task      -- intent context, retry feedback
    #   L5 (reserved) -- user session context (future)
    #   L6 Retrieval -- KCs, memory, auto-retrieved context
    #   L7 Commands  -- execution instructions (injected below)
    # ================================================================

    # --- L6 Retrieval: Knowledge Cards ---
    kc_block = _load_relevant_kcs(intent, parsed)
    if kc_block:
        parts.append("## [L6] Knowledge Card Context")
        parts.append(kc_block)

    # --- L6 Retrieval: Builder Memory ---
    memory_block = _load_builder_memories(builder_id, intent)
    if memory_block:
        parts.append("## [L6] Builder Memory")
        parts.append(memory_block)

    # --- L6 Retrieval: Auto-Retrieved Context (F5 CALL outputs) ---
    if hasattr(state, "tool_results") and state.tool_results.get("enrichment_text"):
        parts.append("## [L6] Auto-Retrieved Context (F5 CALL)")
        parts.append(state.tool_results["enrichment_text"])
        parts.append("")

    # --- L3 Workflow: Prior Outputs ---
    # Only inject outputs from completed earlier steps (not current function)
    prior = {
        bid: out
        for bid, out in state.outputs.items()
        if out.status in ("complete", "degraded")
        and out.content
        and not out.content.startswith("[DRY-RUN]")
    }
    if prior:
        parts.append("## [L3] Prior Builder Outputs")
        parts.append("These outputs were produced by earlier pipeline steps.")
        parts.append("Use them as context -- do not repeat their work.")
        parts.append("")
        for bid, out in prior.items():
            parts.append(f"### {bid} (score: {out.quality_score:.1f})")
            content = out.content
            if len(content) > 2000:
                content = content[:2000] + "\n\n[... truncated to 2KB ...]"
            parts.append(content)
            parts.append("")

    # --- L4 Task: Retry Feedback ---
    if retry_feedback:
        parts.append("## [L4] Retry Feedback")
        parts.append("Your previous attempt did not pass the quality gate.")
        parts.append(retry_feedback)
        parts.append("")

    # --- L7 Commands: Execution Instructions ---
    parts.append("## [L7] Execution Instructions")
    parts.append(
        f"1. You are executing builder `{builder_id}` for pipeline function `{function_name}`."
    )
    parts.append(f"2. Follow the builder's spec instructions precisely.")
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

    # ------------------------------------------------------------------
    # Composable-crew loader (Phase 2 of crew-wiring mini-wave)
    # ------------------------------------------------------------------
    @classmethod
    def load_from_crew_template(
        cls,
        crew_path: Path,
        charter_path: Path | None = None,
        cex_root: Path = CEX_ROOT,
    ) -> dict:
        """Parse a crew_template.md + optional team_charter.md into a runnable plan.

        crew_template.md shape (from archetypes/builders/crew-template-builder):
          frontmatter: crew_name, purpose, process, handoff_protocol_id, ...
          body `## Roles` table: | Role | Role Assignment ID | Reason |

        Each `Role Assignment ID` (e.g. `p02_ra_researcher.md`) is resolved by:
          1. sibling dir of crew file (e.g. N02_marketing/orchestration/)
          2. cex_root glob N0*/orchestration/<id>
          3. cex_root glob N0*/agents/<id>
          4. cex_root glob P02_*/**/<id>

        The role_assignment's frontmatter `agent_id` points to a builder
        or nucleus agent -- that becomes a builder entry in the plan.

        Returns a plan dict compatible with CrewRunner.run().
        """
        import re as _re

        # --- 1. Parse crew_template ---
        text = crew_path.read_text(encoding="utf-8", errors="replace")
        fm = _parse_md_frontmatter(text)
        body = text.split("---", 2)[-1] if text.startswith("---") else text

        crew_name = fm.get("crew_name", crew_path.stem)
        process = (fm.get("process") or "sequential").strip().lower()
        purpose = fm.get("purpose", f"Execute crew {crew_name}")
        handoff_proto = fm.get("handoff_protocol_id", "a2a-task")

        # --- 2. Parse `## Roles` table ---
        roles: list[dict] = []
        in_roles = False
        for line in body.splitlines():
            low = line.strip().lower()
            if low.startswith("## "):
                in_roles = low.startswith("## roles")
                continue
            if not in_roles:
                continue
            if not line.strip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 3:
                continue
            # skip header + separator rows
            if cells[0].lower() in ("role", "---", ":---"):
                continue
            if _re.match(r"^[-: ]+$", cells[0]):
                continue
            roles.append(
                {"role_name": cells[0], "assignment_id": cells[1], "reason": cells[2]}
            )

        if not roles:
            raise ValueError(
                f"crew_template {crew_path.name} has no `## Roles` rows -- "
                "cannot build plan"
            )

        # --- 3. Resolve each role_assignment.md ---
        resolved: list[dict] = []
        search_dirs = [
            crew_path.parent,
            *sorted((cex_root).glob("N0*/crews")),
            *sorted((cex_root).glob("P02_*")),
        ]
        for role in roles:
            aid = role["assignment_id"].strip()
            # strip template placeholder braces if any
            aid = _re.sub(r"\{\{.*?\}\}", "", aid).strip()
            if not aid or aid.startswith("<!--"):
                continue
            ra_path = None
            for d in search_dirs:
                candidate = d / aid
                if candidate.exists():
                    ra_path = candidate
                    break
                # glob fallback for pillar subdirs
                matches = list(d.rglob(aid)) if d.is_dir() else []
                if matches:
                    ra_path = matches[0]
                    break
            ra_fm: dict = {}
            agent_id = None
            if ra_path and ra_path.exists():
                ra_text = ra_path.read_text(encoding="utf-8", errors="replace")
                ra_fm = _parse_md_frontmatter(ra_text)
                agent_id = ra_fm.get("agent_id")
            # fallback: derive agent from role_name
            if not agent_id:
                agent_id = (
                    ra_fm.get("role_name", role["role_name"])
                    .lower()
                    .replace(" ", "-")
                    + "-builder"
                )
            resolved.append(
                {
                    "role_name": role["role_name"],
                    "assignment_id": aid,
                    "assignment_path": str(ra_path.resolve().relative_to(cex_root.resolve()))
                    if ra_path
                    else None,
                    "agent_id": agent_id,
                    "goal": ra_fm.get("goal", ""),
                    "backstory": ra_fm.get("backstory", ""),
                    "tools": ra_fm.get("tools", []),
                }
            )

        # --- 4. Optional charter merge ---
        charter_fm: dict = {}
        if charter_path and charter_path.exists():
            charter_fm = _parse_md_frontmatter(
                charter_path.read_text(encoding="utf-8", errors="replace")
            )

        # --- 5. Build plan.functions ---
        # sequential -> one step per role (ordered)
        # hierarchical -> one step, manager first then workers parallel
        # consensus -> one step, all parallel
        parallel = process != "sequential"
        builders = []
        for i, r in enumerate(resolved):
            agent_slug = (
                r["agent_id"]
                .replace(".md", "")
                .split("/")[-1]
            )
            builders.append(
                {
                    "id": agent_slug,
                    "tier": "primary",
                    "active": True,
                    "reason": f"role '{r['role_name']}' bound via {r['assignment_id']}",
                    "role_name": r["role_name"],
                    "order": i,
                    "goal": r["goal"],
                    "backstory": r["backstory"],
                }
            )

        function_entry = {
            "name": "CREW",
            "position": 6,  # PRODUCE slot
            "builders": builders,
            "deps": [],
            "parallel": parallel,
            "estimated_tokens": 4096 * len(builders),
            "process": process,
        }

        plan = {
            "intent": purpose,
            "parsed": {
                "verb": "execute",
                "object": crew_name,
                "domain": "crew",
                "quality": charter_fm.get("quality_gate", 9.0),
                "multi_object": False,
            },
            "classified_kinds": [],
            "functions": [function_entry],
            "total_builders": len(builders),
            "estimated_tokens": 4096 * len(builders),
            "turn_budgets": {b["id"]: 25 for b in builders},
            "warnings": [],
            "crew_meta": {
                "crew_name": crew_name,
                "process": process,
                "handoff_protocol": handoff_proto,
                "roles": resolved,
                "charter": {
                    "mission": charter_fm.get("mission_statement", ""),
                    "deliverables": charter_fm.get("deliverables", []),
                    "deadline": charter_fm.get("deadline", ""),
                    "budget": charter_fm.get("budget", {}),
                }
                if charter_fm
                else None,
                "source_template": str(crew_path.resolve().relative_to(cex_root.resolve())),
            },
        }
        return plan

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
        """Resolve LLM model and max_tokens. Builder-explicit > Router > default.

        Priority:
          1. Builder-explicit model (set in plan by motor)
          2. Router nucleus config (reads nucleus_models.yaml)
          3. LLM_MODEL constant (fallback)

        Returns: (model_id, max_tokens)
        """
        # --- 1. Builder-explicit model (highest priority) ---
        if builder.get("model"):
            return builder["model"], builder.get("model_max_tokens", LLM_MAX_TOKENS)

        # --- 2. Router path (CexRouter + nucleus_models.yaml) ---
        try:
            from cex_router import CexRouter, get_router, resolve_model_for
            nucleus = os.environ.get("CEX_NUCLEUS", "n03")
            # Try CexRouter provider-aware routing first
            router = get_router()
            if isinstance(router, CexRouter) and router.providers:
                try:
                    route = router.resolve_nucleus(nucleus)
                    if route.get("model"):
                        return route["model"], LLM_MAX_TOKENS
                except RuntimeError:
                    pass  # No healthy provider -- fall through to static
            # Fallback: static nucleus_models.yaml resolution
            model = resolve_model_for(nucleus, fallback="")
            if model:
                return model, LLM_MAX_TOKENS
        except Exception:
            pass  # D1: graceful fallback

        # --- 3. Default constant ---
        return LLM_MODEL, LLM_MAX_TOKENS

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
        - Inherits: builder specs + selected memory + query context
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
            # --- [1] Claude CLI first (uses subscription, zero cost) ---
            content = None
            try:
                result = subprocess.run(
                    ["claude", "-p", "--model", model],
                    input=prompt, capture_output=True, text=True,
                    timeout=120, cwd=str(ROOT), encoding="utf-8",
                )
                if result.returncode == 0 and result.stdout.strip():
                    content = result.stdout
            except FileNotFoundError:
                pass  # CLI not available, try SDK

            # --- [2] SDK fallback (only if CLI failed AND CEX_USE_API=1) ---
            if not content and os.environ.get("CEX_USE_API", "0") == "1":
                try:
                    sdk_root = str(Path(__file__).resolve().parent.parent)
                    if sdk_root not in sys.path:
                        sys.path.insert(0, sdk_root)
                    from cex_sdk.models.message import Message as SDKMessage
                    from cex_sdk.models.providers.anthropic import Claude as SDKClaude
                    sdk_model = SDKClaude(id=model, max_tokens=max_tokens)
                    response = sdk_model.invoke([SDKMessage(role="user", content=prompt)])
                    if response.content:
                        content = response.content
                        usage = response.response_usage
                        if usage:
                            print(f"  [SDK-API] {bid}: in={usage.input_tokens} out={usage.output_tokens}", file=sys.stderr)
                except Exception:
                    pass

            if not content:
                raise RuntimeError("No LLM provider available (CLI failed, API disabled)")
            fork_file.write_text(content, encoding="utf-8")

            import re as _re
            score_m = _re.search(r"(?:quality|score)[\s:]*(\d+\.?\d*)", content.lower())
            score = float(score_m.group(1)) if score_m else 7.0

            return BuilderOutput(
                builder_id=bid,
                content=content,
                quality_score=score,
                metadata={
                    "mode": "fork-cli",
                    "model": model,
                    "fork_output": str(fork_file),
                },
                status="complete",
            )
        except FileNotFoundError:
            # claude CLI not in PATH -- dry-run fallback
            fork_file.write_text(f"[FORK-DRY-RUN] {bid}\n{prompt[:500]}", encoding="utf-8")
            return BuilderOutput(
                builder_id=bid,
                content=f"[FORK-DRY-RUN] claude CLI not found. Prompt saved to {fork_file}",
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
        """Execute builders via claude CLI (subscription auth)."""
        fn_name = step.get("name", f"step_{step.get('position', '?')}")
        position = step.get("position", 0)
        active = self._get_active_builders(step)
        results = []

        # Verify claude CLI is available
        try:
            subprocess.run(["claude", "--version"], capture_output=True, timeout=5)
        except (FileNotFoundError, subprocess.TimeoutExpired):
            print("WARN: claude CLI not found. Falling back to dry-run.", file=sys.stderr)
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

                    cli_result = subprocess.run(
                        ["claude", "-p", "--model", model],
                        input=prompt, capture_output=True, text=True,
                        timeout=120, cwd=str(ROOT), encoding="utf-8",
                    )
                    if cli_result.returncode != 0:
                        raise RuntimeError(f"claude -p exit {cli_result.returncode}")
                    content = cli_result.stdout

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

            # Wire 6: Check if context compaction is needed
            prompt_so_far = " ".join(
                o.content for o in state.outputs.values()
                if o.content and not o.content.startswith("[")
            )
            compact_check = check_compaction_needed(prompt_so_far)
            if compact_check["needed"]:
                state.warnings.append(
                    f"[COMPACT] Context at {compact_check['usage_ratio']:.0%} capacity. "
                    f"Compaction skill available: p04_skill_compact"
                )

            # Wire 7: Check if memory extraction should run
            mem_check = check_memory_extract_needed()
            if mem_check["needed"]:
                state.warnings.append(
                    f"[MEMORY] Extraction trigger at execution #{mem_check['counter']}. "
                    f"Memory skill available: p04_skill_memory_extract"
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
    parser.add_argument("--plan", help="Path to Motor 8F plan JSON")
    parser.add_argument(
        "--crew",
        help="Path to crew_template.md (alternative to --plan; parses roles into plan dict)",
    )
    parser.add_argument(
        "--charter",
        help="Optional team_charter.md path -- merged as mission/deliverables into the plan",
    )
    parser.add_argument("--output-dir", help="Output directory for prompts/outputs")
    parser.add_argument("--step", type=int, help="Execute only this step (by position 1-8)")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Generate prompts without LLM calls (DEFAULT)",
    )
    parser.add_argument(
        "--execute", action="store_true", help="Real execution -- calls LLM via claude CLI (subscription)"
    )

    args = parser.parse_args()

    # Load plan (either from JSON or by compiling a crew_template.md)
    if not args.plan and not args.crew:
        print("ERROR: provide --plan <json> OR --crew <crew_template.md>", file=sys.stderr)
        sys.exit(1)

    if args.crew:
        crew_path = Path(args.crew)
        if not crew_path.exists():
            print(f"ERROR: crew_template not found: {crew_path}", file=sys.stderr)
            sys.exit(1)
        charter_path = Path(args.charter) if args.charter else None
        plan = CrewRunner.load_from_crew_template(crew_path, charter_path=charter_path)
        print(
            f"[CREW] loaded {crew_path.name}: "
            f"process={plan['crew_meta']['process']}, "
            f"roles={len(plan['crew_meta']['roles'])}, "
            f"active_builders={plan['total_builders']}"
        )
    else:
        plan_path = Path(args.plan)
        if not plan_path.exists():
            print(f"ERROR: Plan file not found: {plan_path}", file=sys.stderr)
            sys.exit(1)
        with open(plan_path, "r", encoding="utf-8") as f:
            plan = json.load(f)

    # Validate plan has expected structure
    if "functions" not in plan:
        print(
            "ERROR: Plan JSON missing 'functions' key. Is this a Motor 8F output?", file=sys.stderr
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
