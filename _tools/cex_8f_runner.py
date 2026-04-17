#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_8f_runner.py -- 8F Runner: Stateful artifact production pipeline.

Each function (F1-F8) produces state that the next CONSUMES.
Wave 1: F1 CONSTRAIN, F2 BECOME, F3 INJECT, F6 PRODUCE, F8 COLLABORATE.
Wave 2: + F4 REASON (LLM planning), F7 GOVERN (6 hard gates + retry loop).
Wave 3 adds: F5 CALL, multi-kind, proofs.

Usage:
  python cex_8f_runner.py "create a chunking config for markdown"
  python cex_8f_runner.py "create agent for sales" --execute
  python cex_8f_runner.py --kind chunk_strategy --dry-run
  python cex_8f_runner.py --list-kinds
  python cex_8f_runner.py "create eval" --step 3 --verbose
"""

import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

import argparse
import json
import re
import subprocess
import time

import yaml
from dataclasses import dataclass, field
from pathlib import Path

try:
    import importlib.util
    if importlib.util.find_spec("yaml") is None:
        raise ImportError
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# --- Imports from Motor + Intent ---

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_8f_motor import (
    CEX_ROOT,
    OBJECT_TO_KINDS,
    classify_objects,
    fan_out,
    generate_output,
    load_builder_map,
    load_kc_library,
    lookup_kcs_for_kind,
    parse_intent,
)
from cex_intent import execute_prompt
from cex_shared import extract_frontmatter_dict as _shared_extract_frontmatter_dict
from cex_shared import find_builder_dir as _shared_find_builder_dir
from cex_shared import load_iso as _shared_load_iso
from cex_shared import load_yaml
from cex_shared import strip_frontmatter as _shared_strip_frontmatter
from cex_shared import write_learning_record as _shared_write_learning_record

# --- Optional tools (degrade gracefully) ---
try:
    from cex_retriever import (
        find_examples_for_kind,
        find_similar as _find_similar,
    )
    from cex_retriever import (
        load_index as load_retriever_index,
    )
    _RETRIEVER_AVAILABLE = True
except ImportError:
    _RETRIEVER_AVAILABLE = False

try:
    from cex_token_budget import count_tokens, TokenBudget as _TokenBudget
    _TOKEN_BUDGET_AVAILABLE = True
except ImportError:
    _TOKEN_BUDGET_AVAILABLE = False

try:
    from cex_gdp import GDPEnforcer as _GDPEnforcer
    from cex_gdp import NeedsUserDecision as _NeedsUserDecision
    _GDP_AVAILABLE = True
except ImportError:
    _GDP_AVAILABLE = False

try:
    from cex_memory import get_injection_context as _memory_inject
    _MEMORY_AVAILABLE = True
except ImportError:
    _MEMORY_AVAILABLE = False

try:
    from cex_output_formatter import validate_frontmatter as _validate_fm
    _FORMATTER_AVAILABLE = True
except ImportError:
    _FORMATTER_AVAILABLE = False

try:
    from cex_prompt_optimizer import suggest_improvements as _suggest_improvements
    _OPTIMIZER_AVAILABLE = True
except ImportError:
    _OPTIMIZER_AVAILABLE = False

try:
    from cex_quality_monitor import quality_report as _quality_report
    from cex_quality_monitor import save_snapshot as _save_snapshot
    from cex_quality_monitor import scan_artifacts as _scan_artifacts
    _MONITOR_AVAILABLE = True
except ImportError:
    _MONITOR_AVAILABLE = False

try:
    from cex_query import query_builders as _query_builders
    _QUERY_AVAILABLE = True
except ImportError:
    _QUERY_AVAILABLE = False

try:
    from cex_provider_discovery import discover_providers as _discover_providers
    _PROVIDER_AVAILABLE = True
except ImportError:
    _PROVIDER_AVAILABLE = False

try:
    from cex_theme import get_sin as _get_sin
    _THEME_AVAILABLE = True
except ImportError:
    _THEME_AVAILABLE = False

try:
    from cex_prompt_layers import get_layers as _get_prompt_layers
    _LAYERS_AVAILABLE = True
except ImportError:
    _LAYERS_AVAILABLE = False

try:
    from cex_skill_loader import get_skill_loader as _get_skill_loader
    _SKILL_LOADER_AVAILABLE = True
except ImportError:
    _SKILL_LOADER_AVAILABLE = False

try:
    from brand_inject import load_brand_config as _load_brand_config
    from brand_inject import flatten as _flatten_brand
    _BRAND_INJECT_AVAILABLE = True
except ImportError:
    _BRAND_INJECT_AVAILABLE = False

# Load .env for API keys
for _ep in [CEX_ROOT / ".env", CEX_ROOT.parent / "organization-core" / ".env"]:
    if _ep.exists():
        for _line in _ep.read_text().splitlines():
            if "=" in _line and not _line.startswith("#"):
                _k, _v = _line.split("=", 1)
                if _k.strip() not in os.environ:
                    os.environ[_k.strip()] = _v.strip()
        break

# --- Constants ---

BUILDER_DIR = CEX_ROOT / "archetypes" / "builders"

# Pillar directory names keyed by code (e.g. "P01" -> "P01_knowledge")
# Root P01-P12 dirs are now under N00_genesis/
PILLAR_DIRS = {}
_n00 = CEX_ROOT / "N00_genesis"
for d in sorted(_n00.glob("P[0-9][0-9]_*")):
    if d.is_dir():
        code = d.name[:3]  # e.g. "P01"
        PILLAR_DIRS[code] = "N00_genesis/" + d.name

# Builder spec prefix -> function mapping
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

# Function labels for verbose output
F_LABELS = {
    "F1": "CONSTRAIN",
    "F2": "BECOME",
    "F3": "INJECT",
    "F4": "REASON",
    "F5": "CALL",
    "F6": "PRODUCE",
    "F7": "GOVERN",
    "F8": "COLLABORATE",
}

# --- RunState ---

@dataclass
class RunState:
    """Accumulated state across 8 functions."""

    intent: str = ""
    context: str = ""
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


# --- Helpers ---


# Delegates to cex_shared (single source of truth)
find_builder_dir = _shared_find_builder_dir
load_iso = _shared_load_iso
strip_frontmatter = _shared_strip_frontmatter
extract_frontmatter_dict = _shared_extract_frontmatter_dict


def load_pillar_schema(pillar: str) -> dict:
    """Load _schema.yaml for a pillar."""
    dir_name = PILLAR_DIRS.get(pillar)
    if not dir_name:
        return {}
    schema_path = CEX_ROOT / dir_name / "_schema.yaml"
    if not schema_path.exists():
        return {}
    try:
        return load_yaml(schema_path)
    except Exception:
        return {}


def load_kind_schema(kind: str, pillar: str) -> dict:
    """Extract kind-specific constraints from pillar _schema.yaml."""
    return load_pillar_schema(pillar).get("kinds", {}).get(kind, {})


# --- EightFRunner ---


class EightFRunner:
    """Stateful 8-function pipeline for artifact production."""

    def __init__(
        self,
        intent: str,
        kind: str | None = None,
        dry_run: bool = False,
        verbose: bool = False,
        output_dir: Path | None = None,
        context: str = "",
        model: str = "",
    ):
        self.dry_run = dry_run
        self.verbose = verbose
        self.output_dir = output_dir
        self.model = model  # e.g. "ollama/qwen3:8b" or "claude-sonnet-4-6"
        self.state = RunState(intent=intent, context=context)

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

    def _state_summary(self, fn: str) -> str:
        """One-line summary of state after function fn completes."""
        s = self.state
        c, k, v = s.constraints, s.knowledge, s.verdict
        summaries: dict[str, str] = {
            "F1": lambda: "constraints: {" + ", ".join(filter(None, [
                f"max_bytes: {c['max_bytes']}" if c.get("max_bytes") else "",
                f"fields: {len(c.get('frontmatter_required', []))}",
                f"id_pattern: /{c['id_pattern']}/" if c.get("id_pattern") else "",
            ])) + "}",
            "F2": lambda: f"identity: {len(s.identity)} keys ({', '.join(list(s.identity)[:3])})",
            "F3": lambda: f"ISOs: {sum(1 for x in k.values() if x)}, KCs injected: {len(k.get('kc_domains', []))}",
            "F4": lambda: f"plan: {len(s.reasoning.get('plan', '').split())} words (model={s.reasoning.get('model_used', '?')})",
            "F5": lambda: f"tools: {len(s.tool_results.get('tools_available', []))}, existing: {len(s.tool_results.get('existing_artifacts', []))}, executed: {len(s.tool_results.get('tool_outputs', {}))}",
            "F6": lambda: f"artifact: {len(s.artifact.split()) if s.artifact else 0} words",
            "F7": lambda: (f"gates: {sum(1 for g in v.get('hard_gates', []) if g.get('passed'))}/{len(v.get('hard_gates', []))}, retries: {v.get('retries', 0)}" if v else "pending"),
            "F8": lambda: f"mode: {s.result.get('mode', '?')}, path: {s.result.get('path', 'none')}",
        }
        return summaries.get(fn, lambda: "")()

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
        # Verbose timing line: [F1 CONSTRAIN] 12ms | summary
        base = fn_name.split(".")[0]  # strip .retryN suffix
        label = F_LABELS.get(base, "")
        summary = self._state_summary(base)
        if self.verbose:
            print(
                f"  [{fn_name} {label}] {elapsed:.1f}ms | {summary}",
                file=sys.stderr,
            )

    # -- F1 CONSTRAIN -------------------------------------------------------

    def f1_constrain(self) -> None:
        """Load _schema.yaml + bld_schema + bld_config -> state.constraints.

        T04: Token budget allocation at pipeline start.
        """
        # --- T04: Token budget ---
        if _TOKEN_BUDGET_AVAILABLE:
            try:
                budget = _TokenBudget()
                self.state.token_budget = budget
                self._log("F1", f"token budget: input={budget.input_limit} output={budget.output_limit}")
            except Exception:
                self.state.token_budget = None
        else:
            self.state.token_budget = None

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

    def f2_become(self) -> None:
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

        # Prompt optimizer: improvement hints from learning records
        if _OPTIMIZER_AVAILABLE:
            try:
                hints = _suggest_improvements(self.state.kind)
                if hints:
                    identity["optimizer_hints"] = hints
                    self._log("F2", f"prompt optimizer: {len(hints)} hints")
            except Exception as e:
                self._log("F2", f"prompt optimizer unavailable: {e}")

        self.state.identity = identity
        self._log("F2", f"identity: {list(identity.keys())}")

    # -- F3 INJECT ----------------------------------------------------------

    def f3_inject(self) -> None:
        """Assemble ALL context from files -- pure Python, zero subprocess.

        Single source of truth for context injection. Loads 14 source types:
          1. Builder knowledge card (ISO)
          2. Dedicated kind KC (1:1 per kind)
          3. Cluster domain KCs (supplementary, max 2)
          4. Few-shot examples (ISO)
          5. Memory / persistent learnings (ISO)
          6. Architecture / patterns (ISO)
          7. Domain context (--context flag)
          8. Build memory (past performance via cex_memory)
          9. Semantic retrieval (TF-IDF via cex_retriever)
         10. Prompt layers (compiled pillar artifacts)
         11. Brand context (brand_config.yaml variables)
         12. Sin lens (nucleus identity from nucleus_sins.yaml)
         13. Skill loader ISOs (multi-source, priority-ordered)
         14. Shared skills (cross-builder skills from _shared/)
        """
        bdir = self.state.builder_dir
        knowledge: dict = {}

        # 1. Builder knowledge card
        if bdir:
            kc_text = load_iso(bdir, "bld_knowledge_card", self.kind_slug)
            if kc_text:
                knowledge["kc_builder"] = strip_frontmatter(kc_text)
                self._log("F3", "bld_knowledge_card loaded")

        # 2. Dedicated kind KC (primary -- 1:1 per kind)
        kind_kc_path = CEX_ROOT / "N00_genesis" / "P01_knowledge" / "library" / "kind" / f"kc_{self.kind_slug}.md"
        if kind_kc_path.exists():
            text = kind_kc_path.read_text(encoding="utf-8")
            body = strip_frontmatter(text)
            if body.strip():
                knowledge["kc_dedicated"] = body
                self._log("F3", f"dedicated kind KC loaded: kc_{self.kind_slug}.md")

        # 3. Cluster domain KCs from library (supplementary, max 2)
        kc_matches = lookup_kcs_for_kind(self.kc_library, self.state.kind, self.state.pillar)
        kc_domains = []
        for kc in kc_matches[:2]:
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

        # 4. Few-shot examples
        if bdir:
            ex_text = load_iso(bdir, "bld_examples", self.kind_slug)
            if ex_text:
                knowledge["few_shots"] = strip_frontmatter(ex_text)
                self._log("F3", "bld_examples loaded")

        # 5. Memory (persistent learnings)
        if bdir:
            mem_text = load_iso(bdir, "bld_memory", self.kind_slug)
            if mem_text:
                knowledge["memory"] = strip_frontmatter(mem_text)
                self._log("F3", "bld_memory loaded")

        # 6. Architecture (patterns, dependencies)
        if bdir:
            arch_text = load_iso(bdir, "bld_architecture", self.kind_slug)
            if arch_text:
                knowledge["architecture"] = strip_frontmatter(arch_text)
                self._log("F3", "bld_architecture loaded")

        # 7. Domain context (from --context flag or nucleus seed)
        if self.state.context:
            knowledge["domain_context"] = self.state.context
            self._log("F3", f"domain context injected ({len(self.state.context)} chars)")

        # 8. Build memory injection (past performance for this kind)
        if _MEMORY_AVAILABLE:
            try:
                mem_context = _memory_inject(self.state.kind)
                if mem_context and mem_context.strip():
                    knowledge["build_memory"] = mem_context
                    self._log("F3", f"build memory injected ({len(mem_context)} chars)")
            except Exception as e:
                self._log("F3", f"build memory unavailable: {e}")

        # 9. Semantic retrieval (TF-IDF similar artifacts)
        if _RETRIEVER_AVAILABLE:
            try:
                idx = load_retriever_index()
                if idx:
                    similar = find_examples_for_kind(
                        kind=self.state.kind,
                        intent=self.state.intent,
                        index=idx,
                        top_k=3,
                    )
                    if similar:
                        parts = []
                        for s in similar:
                            parts.append(
                                f"- **{s['title']}** (kind={s['kind']}, "
                                f"score={s['score']:.3f}): {s.get('tldr', '')[:150]}"
                            )
                        knowledge["semantic_matches"] = "\n".join(parts)
                        self._log("F3", f"retriever: {len(similar)} semantic matches")
            except Exception as e:
                self._log("F3", f"retriever unavailable: {e}")

        # 10. Prompt layers (compiled pillar artifacts -- identity, guardrails, skills)
        if _LAYERS_AVAILABLE:
            try:
                layers = _get_prompt_layers()
                layer_data: dict = {}

                # Wire 1: Core identity
                identity_body = layers.get("p03_sp_cex_core_identity")
                if identity_body:
                    # Resolve {{INCLUDE}} directives
                    for inc_id in ["p03_ins_doing_tasks", "p03_ins_action_protocol"]:
                        inc_body = layers.get(inc_id)
                        if inc_body:
                            identity_body = identity_body.replace(
                                "{{INCLUDE " + inc_id + "}}", inc_body
                            )
                    identity_body = re.sub(
                        r"\{\{[A-Z_]+\}\}", "[runtime]", identity_body
                    )
                    layer_data["identity"] = identity_body

                # Wire 4: Guardrails
                guardrail_ids = layers.by_kind("guardrail")
                if guardrail_ids:
                    guardrail_parts = []
                    for gid in guardrail_ids:
                        g_body = layers.get(gid)
                        g_meta = layers.get_meta(gid)
                        if g_body:
                            title = g_meta.get("title", gid)
                            severity = g_meta.get("severity", "?")
                            guardrail_parts.append(
                                f"### {title} [severity={severity}]\n{g_body}"
                            )
                    if guardrail_parts:
                        layer_data["guardrails"] = "\n\n".join(guardrail_parts)

                # Wire 5: Verification protocol
                verify_body = layers.get("p03_sp_verification_agent")
                if verify_body:
                    layer_data["verification"] = verify_body

                # Wire 2-3: Behavioral + action skills
                skill_ids = layers.by_kind("skill")
                if skill_ids:
                    skill_parts = []
                    for sid in skill_ids:
                        s_body = layers.get(sid)
                        s_meta = layers.get_meta(sid)
                        if s_body:
                            title = s_meta.get("title", sid)
                            skill_parts.append(f"### {title}\n{s_body}")
                    if skill_parts:
                        layer_data["skills"] = "\n\n".join(skill_parts)

                if layer_data:
                    knowledge["prompt_layers"] = layer_data
                    self._log(
                        "F3",
                        f"prompt layers loaded: {list(layer_data.keys())}",
                    )
            except Exception as e:
                self._log("F3", f"prompt layers unavailable: {e}")

        # 11. Brand context (brand_config.yaml -- pure Python, no subprocess)
        if _BRAND_INJECT_AVAILABLE:
            try:
                brand_config_path = CEX_ROOT / ".cex" / "brand" / "brand_config.yaml"
                if brand_config_path.exists():
                    brand_cfg = _load_brand_config(brand_config_path)
                    if brand_cfg:
                        flat = _flatten_brand(brand_cfg)
                        real = {
                            k: v
                            for k, v in flat.items()
                            if v and not str(v).startswith("{{")
                        }
                        if real:
                            knowledge["brand_context"] = real
                            self._log("F3", f"brand context: {len(real)} variables")
            except Exception as e:
                self._log("F3", f"brand context unavailable: {e}")

        # 12. Sin lens (nucleus identity from nucleus_sins.yaml)
        if _THEME_AVAILABLE:
            try:
                nucleus = os.environ.get("CEX_NUCLEUS", "n03").lower()
                sin = _get_sin(nucleus)
                if sin:
                    knowledge["sin_lens"] = sin
                    self._log("F3", f"sin lens: {sin.get('virtue', '?')}")
            except Exception as e:
                self._log("F3", f"sin lens unavailable: {e}")

        # 13. Skill loader ISOs (multi-source, priority-ordered, dedup'd)
        if _SKILL_LOADER_AVAILABLE:
            try:
                loader = _get_skill_loader()
                isos = loader.load_builder(self.state.kind.replace("_", "-"))
                if isos:
                    # Count by source for logging
                    by_source = {}
                    for iso in isos:
                        by_source[iso.source] = by_source.get(iso.source, 0) + 1
                    knowledge["skill_loader_sources"] = by_source
                    self._log(
                        "F3",
                        f"skill loader: {len(isos)} ISOs from {dict(by_source)}",
                    )

                    # 14. Shared skills (cross-builder, from _shared/)
                    shared = [i for i in isos if i.source == "shared"]
                    if shared:
                        shared_parts = []
                        for s in shared:
                            shared_parts.append(f"### {s.name}\n{s.content[:2000]}")
                        knowledge["shared_skills"] = "\n\n".join(shared_parts)
                        self._log("F3", f"shared skills: {len(shared)}")
            except Exception as e:
                self._log("F3", f"skill loader unavailable: {e}")

        self.state.knowledge = knowledge
        self._log("F3", f"knowledge: {list(knowledge.keys())}")

    # -- F4 REASON ----------------------------------------------------------

    def f4_reason(self) -> None:
        """LLM plans the artifact: fields, decisions, tradeoffs -> state.reasoning.

        T03: GDP gate -- if unresolved USER-scope decisions exist for this kind,
        raises NeedsUserDecision instead of proceeding (D2: raise = halt pipeline).
        """
        # --- T03: GDP gate ---
        if _GDP_AVAILABLE:
            try:
                gdp = _GDPEnforcer()
                pending = gdp.get_pending()
                for d in pending:
                    if d.kind == self.state.kind or d.scope.value == "GLOBAL":
                        self._log("F4", f"GDP BLOCKED: unresolved decision '{d.id}' ({d.scope.value})")
                        raise _NeedsUserDecision(d)
            except _NeedsUserDecision:
                raise
            except Exception as e:
                self._log("F4", f"GDP check skipped: {e}")

        # Compose reasoning prompt from accumulated state
        parts = []
        parts.append("You are planning what artifact to produce. Think step-by-step.")
        parts.append(f"\n## Intent\n{self.state.intent}")
        parts.append(f"\n## Kind\n{self.state.kind} (pillar: {self.state.pillar})")

        # Identity context
        persona = self.state.identity.get("persona", "")
        if persona:
            parts.append(f"\n## Builder Persona\n{persona}")

        # Constraints summary
        c = self.state.constraints
        c_lines = []
        if c.get("id_pattern"):
            c_lines.append(f"- ID pattern: `{c['id_pattern']}`")
        if c.get("frontmatter_required"):
            c_lines.append(f"- Required frontmatter: {', '.join(c['frontmatter_required'])}")
        if c.get("max_bytes"):
            c_lines.append(f"- Max size: {c['max_bytes']} bytes")
        if c.get("boundary"):
            c_lines.append(f"- Boundary: {c['boundary']}")
        if c_lines:
            parts.append("\n## Constraints\n" + "\n".join(c_lines))

        # Knowledge summary (condensed)
        k = self.state.knowledge
        kc_count = len(k.get("kc_domains", []))
        if kc_count:
            parts.append(f"\n## Available Knowledge\n{kc_count} domain KCs available.")
        if k.get("kc_builder"):
            # First 300 chars of builder KC as context
            parts.append(f"\n## Builder KC (excerpt)\n{k['kc_builder'][:300]}...")

        parts.append(
            "\n## Task\n"
            "Plan the artifact. List:\n"
            "1. Which frontmatter fields to include and their values\n"
            "2. Key decisions and tradeoffs\n"
            "3. Body structure outline\n"
            "Be concise (under 500 words)."
        )

        prompt = "\n".join(parts)

        if self.dry_run:
            self.state.reasoning = {"plan": prompt, "model_used": "dry-run"}
            self._log("F4", f"dry-run reasoning prompt ({len(prompt.split())} words)")
        else:
            # Token optimization: skip LLM reasoning if F3 found existing
            # artifacts of the same kind (template-first approach).
            # The plan is predictable: adapt from template structure.
            existing_count = len(self.state.knowledge.get("similar", []))
            kc_builder = self.state.knowledge.get("kc_builder", "")
            has_template = bool(kc_builder and len(kc_builder) > 200)

            # Ollama models: ALWAYS use deterministic plan (skip F4 LLM call)
            # Saves ~280s on weak hardware. F6 already sends full context.
            is_ollama = self.model and self.model.startswith("ollama/")

            if existing_count >= 1 and has_template or is_ollama:
                # Deterministic plan from template (saves ~5K tokens)
                c = self.state.constraints
                plan_lines = [
                    f"## F4 Reasoning Plan (template-first, zero LLM tokens)",
                    f"Kind: {self.state.kind} | Pillar: {self.state.pillar}",
                    f"Approach: adapt from {existing_count} existing artifact(s)",
                    f"",
                    f"1. Frontmatter: id, kind, pillar, title, version, quality: null, "
                    f"tags, tldr, domain, created, updated, density_score",
                    f"2. Structure: follow output template sections",
                    f"3. Content: domain-specific, no filler, density >= 0.85",
                    f"4. Quality: target 9.0+, all hard gates PASS",
                ]
                if c.get("boundary"):
                    plan_lines.append(f"5. Boundary: {c['boundary']}")
                response = "\n".join(plan_lines)
                skip_reason = "ollama-skip" if is_ollama else "template-skip"
                self.state.reasoning = {"plan": response, "model_used": skip_reason}
                self._log("F4", f"deterministic plan ({skip_reason}, LLM skipped)")
            else:
                self._log("F4", "calling LLM for reasoning plan...")
                response = execute_prompt(prompt, model_override=self.model)
                model_tag = self.model or "default"
                self.state.reasoning = {"plan": response, "model_used": model_tag}
                self._log("F4", f"reasoning plan received ({len(response)} chars)")

    # -- F5 CALL ------------------------------------------------------------

    def f5_call(self) -> None:
        """Load bld_tools spec, scan existing artifacts, EXECUTE active tools -> state.tool_results."""
        bdir = self.state.builder_dir
        tool_results = {
            "existing_artifacts": [],
            "tools_available": [],
            "tool_outputs": {},
            "enrichment_text": "",
        }

        # --- Phase 1: Parse bld_tools spec (backwards compat) ---
        if bdir:
            tools_text = load_iso(bdir, "bld_tools", self.kind_slug)
            if tools_text:
                body = strip_frontmatter(tools_text)
                for line in body.split("\n"):
                    line = line.strip()
                    if (
                        line.startswith("|")
                        and "---" not in line
                        and "Tool" not in line
                        and "Source" not in line
                    ):
                        cols = [c.strip() for c in line.split("|")[1:-1]]
                        if len(cols) >= 2 and cols[0]:
                            tool_results["tools_available"].append(
                                {
                                    "name": cols[0],
                                    "purpose": cols[1] if len(cols) > 1 else "",
                                    "status": cols[3] if len(cols) > 3 else "unknown",
                                }
                            )
                self._log(
                    "F5",
                    f"bld_tools loaded, {len(tool_results['tools_available'])} tools parsed",
                )

        # --- Phase 2: Scan existing artifacts in pillar examples dir ---
        pillar_dir_name = PILLAR_DIRS.get(self.state.pillar)
        if pillar_dir_name:
            examples_dir = CEX_ROOT / pillar_dir_name / "examples"
            if examples_dir.exists():
                kind_slug = self.state.kind.replace("-", "_")
                for f in sorted(examples_dir.glob(f"ex_{kind_slug}*.md")):
                    tool_results["existing_artifacts"].append(f.name)

        existing = tool_results["existing_artifacts"]
        if existing:
            self._log(
                "F5",
                f"WARNING: {len(existing)} similar artifact(s) exist: "
                + ", ".join(existing[:5]),
            )

        # --- Phase 3: Auto-execute tools for context enrichment ---
        intent = self.state.intent
        executed = 0

        # 3a. Retriever: find similar artifacts by TF-IDF
        if _RETRIEVER_AVAILABLE:
            try:
                idx = load_retriever_index()
                if idx:
                    results = _find_similar(intent, index=idx, top_k=3)
                    if results:
                        tool_results["tool_outputs"]["retriever"] = results
                        executed += 1
                        self._log("F5", f"retriever: {len(results)} similar artifacts found")
            except Exception as e:
                self._log("F5", f"retriever failed: {e} (non-blocking)")

        # 3b. Query: discover related builders by TF-IDF
        if _QUERY_AVAILABLE:
            try:
                builders = _query_builders(intent, top_k=3)
                if builders:
                    tool_results["tool_outputs"]["query"] = builders
                    executed += 1
                    self._log("F5", f"query: {len(builders)} related builders discovered")
            except Exception as e:
                self._log("F5", f"query failed: {e} (non-blocking)")

        # 3c. Memory: recall relevant build memories
        if _MEMORY_AVAILABLE:
            try:
                kind = self.state.kind
                memory_ctx = _memory_inject(kind)
                if memory_ctx and memory_ctx.strip():
                    tool_results["tool_outputs"]["memory"] = memory_ctx
                    executed += 1
                    self._log("F5", f"memory: context loaded for kind={kind}")
            except Exception as e:
                self._log("F5", f"memory failed: {e} (non-blocking)")

        # 3d. Provider discovery: check health
        if _PROVIDER_AVAILABLE:
            try:
                providers = _discover_providers(use_cache=True)
                if providers:
                    alive = sum(1 for p in providers.values() if p.get("status") == "OK")
                    tool_results["tool_outputs"]["providers"] = {
                        "alive": alive,
                        "total": len(providers),
                        "detail": {k: v.get("status", "?") for k, v in providers.items()},
                    }
                    executed += 1
                    self._log("F5", f"providers: {alive}/{len(providers)} alive")
            except Exception as e:
                self._log("F5", f"provider discovery failed: {e} (non-blocking)")

        # 3e. Brand config -- MOVED to F3 INJECT (pure Python, single source of truth)
        # F5 reads from F3 state if needed:
        if self.state.knowledge.get("brand_context"):
            tool_results["tool_outputs"]["brand"] = self.state.knowledge["brand_context"]
            executed += 1
            self._log("F5", "brand context: from F3 (already loaded)")

        # 3f. Sin lens -- MOVED to F3 INJECT (pure Python, single source of truth)
        if self.state.knowledge.get("sin_lens"):
            tool_results["tool_outputs"]["sin"] = self.state.knowledge["sin_lens"]
            executed += 1
            self._log("F5", "sin lens: from F3 (already loaded)")

        # --- Phase 4: Build enrichment text for F6 injection ---
        if tool_results["tool_outputs"]:
            enrichments = []
            for tool_name, output in tool_results["tool_outputs"].items():
                if tool_name == "retriever" and isinstance(output, list):
                    lines = [f"### Similar Artifacts ({len(output)} matches)"]
                    for item in output[:3]:
                        lines.append(
                            f"- **{item.get('id', '?')}** ({item.get('kind', '?')}) "
                            f"score={item.get('score', 0):.2f} -- {item.get('tldr', '')[:120]}"
                        )
                    enrichments.append("\n".join(lines))
                elif tool_name == "query" and isinstance(output, list):
                    lines = [f"### Related Builders ({len(output)} discovered)"]
                    for item in output[:3]:
                        lines.append(
                            f"- **{item.get('builder_id', item.get('id', '?'))}** "
                            f"score={item.get('score', 0):.2f}"
                        )
                    enrichments.append("\n".join(lines))
                elif tool_name == "memory" and isinstance(output, str):
                    enrichments.append(f"### Build Memory\n{output[:2000]}")
                elif tool_name == "providers" and isinstance(output, dict):
                    enrichments.append(
                        f"### Provider Health\n"
                        f"{output.get('alive', 0)}/{output.get('total', 0)} providers alive"
                    )
                elif tool_name == "brand" and isinstance(output, dict):
                    brand_name = output.get("identity", {}).get("name", "?")
                    enrichments.append(f"### Brand Context\nBrand: {brand_name}")
                elif tool_name == "sin" and isinstance(output, dict):
                    enrichments.append(
                        f"### Sin Lens\n"
                        f"Virtue: {output.get('virtue', '?')} | "
                        f"Tagline: {output.get('tagline', '?')}"
                    )
                else:
                    # Generic fallback
                    enrichments.append(
                        f"### {tool_name}\n{json.dumps(output, indent=2, default=str)[:2000]}"
                    )

            tool_results["enrichment_text"] = "\n\n".join(enrichments)

        self.state.tool_results = tool_results
        self._log(
            "F5",
            f"tools: {len(tool_results['tools_available'])}, "
            f"existing: {len(existing)}, "
            f"executed: {executed}, "
            f"enrichments: {len(tool_results['tool_outputs'])}",
        )

    # -- F6 PRODUCE ---------------------------------------------------------

    def f6_produce(self, retry_feedback: str = "") -> None:
        """Compose STRUCTURED prompt with labeled sections -> state.artifact."""
        sections = []

        # 0. PROMPT LAYERS (from F3 -- injected FIRST, before everything)
        k = self.state.knowledge
        pl = k.get("prompt_layers", {})
        if pl.get("identity"):
            sections.append(f"# CEX AGENT IDENTITY\n\n{pl['identity']}")
        if k.get("sin_lens"):
            sin = k["sin_lens"]
            sections.append(
                f"# IDENTITY LENS\n\n"
                f"Virtue: {sin.get('virtue', '?')} | "
                f"Tagline: {sin.get('tagline', '?')}"
            )
        if pl.get("guardrails"):
            sections.append(f"# GUARDRAILS\n\n{pl['guardrails']}")

        # 0b. BRAND CONTEXT (from F3)
        brand = k.get("brand_context")
        if brand and isinstance(brand, dict):
            brand_lines = [f"- {bk}: {bv}" for bk, bv in sorted(brand.items())
                           if not bk.startswith(("identity.", "archetype.", "voice.",
                                                 "audience.", "visual.", "positioning.",
                                                 "monetization."))]
            if brand_lines:
                sections.append("# BRAND CONTEXT\n\n" + "\n".join(brand_lines))

        # 0c. SHARED SKILLS (from F3)
        if k.get("shared_skills"):
            sections.append(f"# SHARED SKILLS\n\n{k['shared_skills']}")

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
        if k.get("domain_context"):
            knowledge_parts.append("## Domain Context\n\n" + k["domain_context"])
        if k.get("build_memory"):
            knowledge_parts.append(
                "## Build Memory (past performance)\n\n" + k["build_memory"]
            )
        if k.get("semantic_matches"):
            knowledge_parts.append(
                "## Similar Artifacts (semantic retrieval)\n\n" + k["semantic_matches"]
            )
        if knowledge_parts:
            sections.append("# KNOWLEDGE\n\n" + "\n\n".join(knowledge_parts))

        # 4. EXAMPLES (from F3)
        if k.get("few_shots"):
            sections.append(f"# EXAMPLES\n\n{k['few_shots']}")

        # 5. PLAN (from F4 reasoning)
        plan = self.state.reasoning.get("plan", "")
        if plan:
            sections.append(f"# PLAN\n\n{plan}")

        # 5b. TOOLS (from F5 call)
        tr = self.state.tool_results
        if tr.get("tools_available") or tr.get("existing_artifacts"):
            tool_lines = []
            if tr.get("tools_available"):
                tool_lines.append("## Available Tools")
                for t in tr["tools_available"]:
                    status = t.get("status", "")
                    tool_lines.append(f"- **{t['name']}**: {t['purpose']} [{status}]")
            if tr.get("existing_artifacts"):
                tool_lines.append(f"\n## Existing Artifacts ({len(tr['existing_artifacts'])})")
                for a in tr["existing_artifacts"][:5]:
                    tool_lines.append(f"- {a}")
                tool_lines.append(
                    "\n> NOTE: Similar artifacts exist. Ensure your output is "
                    "distinct and adds value."
                )
            sections.append("# TOOLS\n\n" + "\n".join(tool_lines))

        # 5b-extra. F5 AUTO-RETRIEVED CONTEXT (tool execution outputs)
        enrichment = tr.get("enrichment_text", "")
        if enrichment:
            sections.append("# AUTO-RETRIEVED CONTEXT (F5 CALL)\n\n" + enrichment)

        # 5c. OPTIMIZER HINTS (from F2 prompt_optimizer)
        hints = self.state.identity.get("optimizer_hints", [])
        if hints:
            sections.append(
                "# OPTIMIZER HINTS\n\n"
                "Based on past builds, pay attention to:\n"
                + "\n".join(f"- {h}" for h in hints)
            )

        # 6. INSTRUCTION (bld_instruction body)
        bdir = self.state.builder_dir
        if bdir:
            instr_text = load_iso(bdir, "bld_instruction", self.kind_slug)
            if instr_text:
                sections.append(f"# INSTRUCTION\n\n{strip_frontmatter(instr_text)}")

        # 7. TEMPLATE (bld_output_template body)
        if bdir:
            tpl_text = load_iso(bdir, "bld_output_template", self.kind_slug)
            if tpl_text:
                sections.append(f"# TEMPLATE\n\n{strip_frontmatter(tpl_text)}")

        # 8. TASK (user intent)
        task_lines = [
            f"**Intent**: {self.state.intent}",
            f"**Kind**: {self.state.kind}",
            f"**Pillar**: {self.state.pillar}",
            f"**Verb**: {self.parsed.get('verb', 'cria')}"
            f" ({self.parsed.get('verb_action', 'create')})",
            "**Quality**: set quality: null (NEVER self-score)",
            "",
            "## CRITICAL OUTPUT RULES",
            "1. Output ONLY the artifact. NO preamble, NO explanation, NO tool calls.",
            "2. Start your response with exactly `---` on the first line.",
            "3. Then YAML frontmatter fields (id, kind, pillar, title, etc).",
            "4. Then `---` to close frontmatter.",
            "5. Then Markdown body with ## sections.",
            "6. Do NOT wrap in code fences (no ```yaml or ```markdown).",
            "7. Do NOT include any text before the opening `---`.",
        ]
        sections.append("# TASK\n\n" + "\n".join(task_lines))

        # 9. RETRY FEEDBACK (from F7, if retrying)
        if retry_feedback:
            sections.append(
                f"# RETRY FEEDBACK\n\n"
                f"Your previous output FAILED validation. Fix these issues:\n\n"
                f"{retry_feedback}"
            )

        prompt = "\n\n---\n\n".join(sections)

        # Ollama ultra-lite mode: aggressive prompt reduction for local models
        # Local models on weak hardware (4GB VRAM, CPU offload) need <3K tokens
        if self.model and self.model.startswith("ollama/"):
            keep_headers = {
                "# IDENTITY", "# CONSTRAINTS", "# INSTRUCTION",
                "# TEMPLATE", "# TASK",
            }
            lite_sections = []
            for sec in sections:
                header = sec.split("\n")[0].strip()
                if header in keep_headers:
                    # Truncate long sections to ~500 chars
                    if len(sec) > 600 and header not in ("# TASK",):
                        sec = sec[:600] + "\n[...truncated for local model...]"
                    lite_sections.append(sec)
            # Always include TASK (last)
            if not any(s.startswith("# TASK") for s in lite_sections):
                lite_sections.append(sections[-1])
            prompt = "\n\n---\n\n".join(lite_sections)
            self._log("F6", f"Ollama ultra-lite: {len(sections)} -> {len(lite_sections)} sections")

        # Token budget analysis (if available)
        token_count = len(prompt.split())  # fallback: word count
        if _TOKEN_BUDGET_AVAILABLE:
            token_count = count_tokens(prompt)
            self._log("F6", f"prompt: {token_count:,} tokens (tiktoken)")

        if self.dry_run:
            self.state.artifact = prompt
            self._log("F6", f"dry-run prompt composed ({token_count:,} tokens)")
        else:
            self._log("F6", f"executing prompt ({token_count:,} tokens) via {self.model or 'default'}...")
            response = execute_prompt(prompt, model_override=self.model)
            self.state.artifact = response
            self._log("F6", f"LLM response received ({len(response)} chars)")

            # --- T04b: Token budget output check ---
            if getattr(self.state, "token_budget", None):
                try:
                    out_tokens = count_tokens(response) if _TOKEN_BUDGET_AVAILABLE else len(response.split())
                    limit = self.state.token_budget.output_limit
                    if limit and out_tokens > limit:
                        self._log("F6", f"WARN: output {out_tokens} tokens exceeds budget {limit}")
                except Exception:
                    pass

    # -- helpers: clean LLM output ------------------------------------------

    def _clean_llm_output(self, text: str) -> str:
        """Strip preamble, code fences, and tool calls from LLM output."""
        t = text.strip()

        # Strip everything before first --- (preamble, tool calls, etc.)
        idx = t.find("---\n")
        if idx > 0:
            t = t[idx:]
        elif idx < 0 and not t.startswith("---"):
            for marker in ["---\r\n", "---\n", "\n---"]:
                pos = t.find(marker)
                if pos >= 0:
                    t = t[pos:].lstrip("\n\r")
                    break

        # Strip code fences wrapping the whole thing
        bt = chr(96) * 3
        if t.startswith(bt):
            nl = t.find(chr(10))
            if nl > 0:
                t = t[nl + 1:]
            close = t.rfind(bt)
            if close > 0:
                t = t[:close].strip()

        # Ensure starts with ---
        if not t.startswith("---"):
            t = "---\n" + t

        return t

    # -- F7 GOVERN ----------------------------------------------------------

    def f7_govern(self) -> None:
        """Validate artifact against 6 hard gates. Retry via F6 if fails (max 2)."""
        max_retries = 2
        retries = 0

        # Clean LLM output before validation
        self.state.artifact = self._clean_llm_output(self.state.artifact)

        while True:
            artifact = self.state.artifact
            hard_gates: list[dict] = []
            issues: list[str] = []

            def _gate(gate: str, check: str, passed: bool, fail_msg: str = "") -> None:
                hard_gates.append({"gate": gate, "check": check, "passed": passed})  # noqa: B023
                if not passed and fail_msg:
                    issues.append(fail_msg)  # noqa: B023

            fm = extract_frontmatter_dict(artifact)
            _gate("H01", "YAML frontmatter parses", bool(fm),
                  "H01: Frontmatter missing or invalid YAML")

            id_pattern = self.state.constraints.get("id_pattern", "")
            artifact_id = fm.get("id", "")
            h02 = bool(re.match(id_pattern, str(artifact_id))) if (id_pattern and artifact_id) else (not id_pattern)
            _gate("H02", "id matches id_pattern", h02,
                  f"H02: id '{artifact_id}' does not match pattern /{id_pattern}/")

            artifact_kind = fm.get("kind", "")
            _gate("H03", "kind matches", str(artifact_kind) == self.state.kind if fm else True,
                  f"H03: kind '{artifact_kind}' != expected '{self.state.kind}'")

            h04 = fm.get("quality") is None if fm else True
            _gate("H04", "quality is null", h04,
                  f"H04: quality must be null, got '{fm.get('quality')}'")

            required = self.state.constraints.get("frontmatter_required", [])
            missing = [f for f in required if f not in fm] if fm else list(required)
            _gate("H05", "required fields present", len(missing) == 0,
                  f"H05: Missing required fields: {', '.join(missing)}")

            max_bytes = self.state.constraints.get("max_bytes")
            body_size = len(strip_frontmatter(artifact).encode("utf-8"))
            _gate("H06", "body <= max_bytes", body_size <= int(max_bytes) if max_bytes else True,
                  f"H06: Body {body_size} bytes > max {max_bytes} bytes")

            # Output formatter validation (jsonschema-based, soft -- non-blocking)
            soft_warnings: list[str] = []
            if _FORMATTER_AVAILABLE and fm:
                try:
                    fm_results = _validate_fm(fm, self.state.kind)
                    for r in fm_results:
                        if not r.get("passed"):
                            soft_warnings.append(f"S_{r['rule']}: {r['message']}")
                    self._log("F7", f"formatter: {len(fm_results)} rules, {len(soft_warnings)} warnings")
                except Exception as e:
                    self._log("F7", f"formatter unavailable: {e}")

            all_passed = all(g["passed"] for g in hard_gates)

            if all_passed:
                self.state.verdict = {
                    "passed": True,
                    "hard_gates": hard_gates,
                    "soft_warnings": soft_warnings,
                    "issues": [],
                    "feedback": "",
                    "retries": retries,
                }
                self._log("F7", f"PASSED all {len(hard_gates)} hard gates (retries={retries})"
                           + (f", {len(soft_warnings)} soft warnings" if soft_warnings else ""))
                break

            # Gates failed
            retries += 1
            feedback = "HARD GATE FAILURES:\n" + "\n".join(f"- {i}" for i in issues)

            if retries <= max_retries:
                self._log("F7", f"FAILED ({len(issues)} issues), retry {retries}/{max_retries}")
                # Retry: call f6_produce with feedback
                self._timed(
                    f"F6.retry{retries}", lambda fb=feedback: self.f6_produce(retry_feedback=fb)
                )
                # Clean output after retry
                self.state.artifact = self._clean_llm_output(self.state.artifact)
            else:
                # Max retries exhausted -> save as draft with issues
                self.state.verdict = {
                    "passed": False,
                    "hard_gates": hard_gates,
                    "issues": issues,
                    "feedback": feedback,
                    "retries": retries,
                }
                self._log("F7", f"FAILED after {max_retries} retries: {issues}")
                break

    # -- Learning Record -----------------------------------------------------

    def _write_learning_record(self) -> None:
        """Capture build outcome as learning_record (delegates to cex_shared)."""
        _shared_write_learning_record(
            kind=self.state.kind,
            intent=self.state.intent,
            verdict=self.state.verdict,
            timings=self.state.timings,
            builder_dir=self.state.builder_dir,
            logger=self._log,
        )

    # -- F8 COLLABORATE -----------------------------------------------------

    def f8_collaborate(self) -> None:
        """Save artifact to file, compile -> state.result."""
        # Write learning record (pre-save, captures build outcome regardless)
        if not self.dry_run:
            self._write_learning_record()

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

            # Generate filename: try to extract id from artifact, fallback to intent slug
            fm_pre = extract_frontmatter_dict(self.state.artifact)
            artifact_id = fm_pre.get("id", "") if fm_pre else ""
            if artifact_id and re.match(r"^[a-z0-9_]+$", str(artifact_id)):
                filename = f"{artifact_id}.md"
            else:
                slug = re.sub(r"[^a-z0-9]+", "_", self.state.intent.lower()).strip("_")[:40]
                filename = f"{self.state.pillar.lower()}_{self.state.kind}_{slug}.md"
            out_path = out_dir / filename

            # Clean code fences from LLM output (safety net -- F7 already cleans)
            art = self._clean_llm_output(self.state.artifact)
            self.state.artifact = art
            out_path.write_text(art, encoding="utf-8")
            self._log("F8", f"artifact saved to {out_path}")

            # Try compile
            compiled = False
            try:
                compile_script = CEX_ROOT / "_tools" / "cex_compile.py"
                if compile_script.exists():
                    subprocess.run(
                        [sys.executable, str(compile_script), str(out_path)],
                        capture_output=True,
                        timeout=30,
                    )
                    compiled = True
            except Exception as e:
                self._log("F8", f"compile skipped: {e}")

            # Re-index after creation (full cycle)
            indexed = False
            try:
                index_script = CEX_ROOT / "_tools" / "cex_index.py"
                if index_script.exists():
                    subprocess.run(
                        [sys.executable, str(index_script)],
                        capture_output=True,
                        timeout=60,
                    )
                    indexed = True
                    self._log("F8", "index rebuilt")
            except Exception as e:
                self._log("F8", f"index skipped: {e}")

            # Auto-commit if gates passed
            committed = False
            if self.state.verdict.get("passed"):
                try:
                    subprocess.run(
                        ["git", "add", str(out_path)],
                        capture_output=True, timeout=10,
                    )
                    # Also add compiled version if exists
                    compiled_dir = out_path.parent / "compiled"
                    if compiled_dir.exists():
                        subprocess.run(
                            ["git", "add", str(compiled_dir)],
                            capture_output=True, timeout=10,
                        )
                    msg = f"[8F] {self.state.kind}: {self.state.intent[:60]}"
                    subprocess.run(
                        ["git", "commit", "-m", msg],
                        capture_output=True, timeout=10,
                    )
                    committed = True
                    self._log("F8", "auto-committed to git")
                except Exception as e:
                    self._log("F8", f"auto-commit skipped: {e}")

            # Quality monitor: track build in snapshot
            monitored = False
            if _MONITOR_AVAILABLE and self.state.verdict.get("passed"):
                try:
                    _save_snapshot([{
                        "path": str(out_path),
                        "kind": self.state.kind,
                        "pillar": self.state.pillar,
                        "score": 8.0,  # baseline; peer review adjusts later
                    }])
                    monitored = True
                    self._log("F8", "quality snapshot updated")
                except Exception as e:
                    self._log("F8", f"quality monitor skipped: {e}")

            # NotebookLM auto-upload for knowledge_card artifacts
            notebooklm_uploaded = False
            if committed and self.state.kind == "knowledge_card":
                try:
                    nlm_config_path = CEX_ROOT / ".cex" / "config" / "notebooklm_notebooks.yaml"
                    if nlm_config_path.exists():
                        nlm_cfg = yaml.safe_load(
                            nlm_config_path.read_text(encoding="utf-8")
                        ) or {}
                        if nlm_cfg.get("publish_mode") == "auto":
                            nlm_tool = CEX_ROOT / "_tools" / "cex_notebooklm.py"
                            if nlm_tool.exists():
                                nlm_result = subprocess.run(
                                    [sys.executable, str(nlm_tool),
                                     "--upload", str(out_path)],
                                    capture_output=True, text=True, timeout=120,
                                )
                                if nlm_result.returncode == 0:
                                    notebooklm_uploaded = True
                                    self._log("F8", "NotebookLM auto-upload OK")
                                else:
                                    self._log(
                                        "F8",
                                        "NotebookLM upload failed: "
                                        + nlm_result.stderr[:200],
                                    )
                except Exception as e:
                    self._log("F8", f"NotebookLM upload skipped: {e}")

            self.state.result = {
                "path": str(out_path),
                "compiled": compiled,
                "indexed": indexed,
                "committed": committed,
                "monitored": monitored,
                "notebooklm": notebooklm_uploaded,
                "mode": "execute",
            }

    # -- run() pipeline -----------------------------------------------------

    def run(self, stop_at: int | None = None) -> RunState:
        """Execute F1->F2->F3->F4->F5->F6->F7->F8 pipeline (wave 3: full)."""
        steps = [
            ("F1", self.f1_constrain),
            ("F2", self.f2_become),
            ("F3", self.f3_inject),
            ("F4", self.f4_reason),
            ("F5", self.f5_call),
            ("F6", self.f6_produce),
            ("F7", self.f7_govern),
            ("F8", self.f8_collaborate),
        ]

        for step_num, (name, func) in enumerate(steps, 1):
            self._timed(name, func)
            if stop_at and step_num >= stop_at:
                self._log("run", f"stopped at step {step_num} (--step {stop_at})")
                break

        return self.state


# --- CLI: list-kinds ---


def list_kinds():
    """Print all available kinds grouped by pillar."""
    by_pillar: dict[str, list[tuple[str, str]]] = {}
    seen = set()
    for _keyword, kinds_list in sorted(OBJECT_TO_KINDS.items()):
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


# --- CLI: banner ---


def print_banner(state: RunState, elapsed_ms: float) -> None:
    """Print compact run summary."""
    sep = "=" * 70
    mode = "DRY-RUN" if state.result.get("mode") == "dry-run" else "EXECUTE"
    c, k, v = state.constraints, state.knowledge, state.verdict
    lines = [
        f"\n{sep}",
        f"  CEX 8F Runner | {state.kind} | {state.pillar} | {mode}",
        sep,
        f"  Intent:  {state.intent}",
        f"  Builder: {state.builder_dir or 'NONE'}",
    ]
    c_parts = ([f"max={c['max_bytes']}b"] if c.get("max_bytes") else [])
    if c.get("frontmatter_required"):
        c_parts.append(f"fm={len(c['frontmatter_required'])} fields")
    if c_parts:
        lines.append(f"  Constrain: {', '.join(c_parts)}")
    k_parts = [label for key, label in [("kc_builder", "builder-KC"), ("few_shots", "examples"), ("memory", "memory")] if k.get(key)]
    if k.get("kc_domains"):
        k_parts.insert(1, f"{len(k['kc_domains'])} KCs")
    if k.get("build_memory"):
        k_parts.append("memory")
    if k.get("semantic_matches"):
        k_parts.append("retriever")
    if k_parts:
        lines.append(f"  Knowledge: {', '.join(k_parts)}")
    if state.artifact:
        lines.append(f"  Artifact: {len(state.artifact.split())} words")
    if v:
        g = v.get("hard_gates", [])
        ok = sum(1 for x in g if x.get("passed"))
        lines.append(f"  Verdict:  {'PASS' if v.get('passed') else 'FAIL'} ({ok}/{len(g)} gates, {v.get('retries', 0)} retries)")
        lines.extend(f"    ! {issue}" for issue in v.get("issues", []))
    if state.result.get("path"):
        lines.append(f"  Output:   {state.result['path']}")
    if state.timings:
        lines.append(f"  Timing:   {' | '.join(f'{tk}={tv}ms' for tk, tv in state.timings.items())} | total={elapsed_ms:.0f}ms")
    lines.extend(f"  ! ERROR: {err}" for err in state.errors)
    lines.append(sep)
    print("\n".join(lines))


# --- Main ---


NUC_DIRS = {
    "N01": "N01_intelligence", "N02": "N02_marketing", "N03": "N03_engineering",
    "N04": "N04_knowledge", "N05": "N05_operations", "N06": "N06_commercial",
    "N07": "N07_admin",
}
NUC_DOMAINS = {
    "N01": "research, intelligence, papers, benchmarks",
    "N02": "copywriting, ads, campaigns, social media",
    "N03": "meta-construction, 8F pipeline, scaffolding",
    "N04": "RAG, embeddings, chunking, taxonomy",
    "N05": "testing, CI/CD, deployment, monitoring",
    "N06": "pricing, sales funnels, monetization",
    "N07": "orchestration, dispatch, quality validation",
}
KIND_TO_SUBDIR = {
    "agent": "agents", "knowledge_card": "knowledge", "dispatch_rule": "orchestration",
    "workflow": "orchestration", "quality_gate": "feedback", "embedding_config": "knowledge",
    "rag_source": "knowledge", "chunk_strategy": "knowledge", "retriever_config": "knowledge",
    "checkpoint": "memory", "spawn_config": "orchestration", "prompt_template": "prompts",
    "action_prompt": "prompts", "system_prompt": "prompts", "scoring_rubric": "quality",
    "signal": "orchestration", "dag": "orchestration", "handoff": "orchestration",
    "fallback_chain": "agents", "pattern": "architecture", "agent_card": "architecture",
}


def _resolve_nucleus(nucleus: str, kind_override: str | None, intent: str) -> tuple[str, str]:
    """Resolve nucleus output dir and domain context."""
    nuc = nucleus.upper()
    if nuc not in NUC_DIRS:
        return "", ""
    kind_for_dir = kind_override or ""
    if not kind_for_dir:
        parsed = parse_intent(intent)
        if parsed.get("objects"):
            kind_for_dir = parsed["objects"][0]
    subdir = KIND_TO_SUBDIR.get(kind_for_dir, "artifacts")
    output_dir = str(CEX_ROOT / NUC_DIRS[nuc] / subdir)
    ctx = f"Nucleus: {nuc} ({NUC_DIRS[nuc]}). Domain: {NUC_DOMAINS.get(nuc, '')}. All content must be specific to this nucleus domain."
    return output_dir, ctx


def main() -> None:
    parser = argparse.ArgumentParser(description="cex_8f_runner.py -- 8F Stateful Artifact Pipeline")
    parser.add_argument("intent", nargs="?", help="Natural language intent")
    parser.add_argument("--kind", help="Override kind classification (skip Motor)")
    parser.add_argument("--dry-run", action="store_true", help="Preview prompt without LLM (default)")
    parser.add_argument("--execute", action="store_true", help="Call LLM to produce artifact")
    parser.add_argument("--list-kinds", action="store_true", help="Print all available kinds")
    parser.add_argument("--verbose", action="store_true", help="Show per-F details")
    parser.add_argument("--step", type=int, metavar="N", help="Stop after function N (1-8)")
    parser.add_argument("--output-dir", metavar="DIR", help="Save outputs to this directory")
    parser.add_argument("--nucleus", metavar="N0X", help="Target nucleus (e.g. N01, N05)")
    parser.add_argument("--context", metavar="TEXT", help="Domain context to inject")
    parser.add_argument("--model", metavar="MODEL",
                        help="Model override (e.g. 'ollama/qwen3:8b', 'claude-sonnet-4-6')")
    args = parser.parse_args()

    if args.list_kinds:
        list_kinds()
        return
    if not args.intent and not args.kind:
        parser.print_help()
        sys.exit(1)

    intent = args.intent or f"create {args.kind}"
    context = args.context or ""
    if args.nucleus:
        output_dir, nuc_context = _resolve_nucleus(args.nucleus, args.kind, intent)
        if not args.output_dir:
            args.output_dir = output_dir
        if not context:
            context = nuc_context

    parsed = parse_intent(intent)
    classified = classify_objects(parsed["objects"]) if not args.kind else []
    if len(classified) > 1:
        print(f"\n  Multi-kind detected: {len(classified)} kinds")
        for i, c in enumerate(classified):
            print(f"    [{i + 1}] {c['kind']} (pillar={c['pillar']})")
    kinds_to_run = [c["kind"] for c in classified] if len(classified) > 1 else [args.kind]

    for kind_i, kind in enumerate(kinds_to_run):
        if len(kinds_to_run) > 1:
            print(f"\n{'#' * 70}\n  Multi-kind [{kind_i + 1}/{len(kinds_to_run)}]: {kind}\n{'#' * 70}")
        runner = EightFRunner(
            intent=intent, context=context, kind=kind,
            dry_run=not args.execute, verbose=args.verbose, output_dir=args.output_dir,
            model=getattr(args, "model", "") or "",
        )
        t0 = time.perf_counter()
        state = runner.run(stop_at=args.step)
        print_banner(state, (time.perf_counter() - t0) * 1000)
        if state.artifact:
            if state.result.get("mode") == "dry-run":
                print(f"--- STRUCTURED PROMPT (8F) ---\n\n{state.artifact}\n\n--- END ({len(state.artifact.split())} words) ---")
            else:
                print(f"--- ARTIFACT ---\n\n{state.artifact[:2000]}")
                if len(state.artifact) > 2000:
                    print(f"\n... (truncated, full: {len(state.artifact)} chars)")


if __name__ == "__main__":
    main()
