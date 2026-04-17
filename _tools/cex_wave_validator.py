#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_wave_validator.py -- Pre-commit ISO gate for CEX builder archetypes.

Runs 7 systemic checks on bld_*.md files (builder ISOs) before they reach git.
Catches generator-side defects (qwen3 / gemma4 / direct-edit) that the
8F pipeline and builder self-validation may miss.

The 7 checks (all surfaced in HYBRID_REVIEW audits):

  C1 system_prompt_llm_function   bld_system_prompt_*.md must have
                                  llm_function: BECOME

  C2 schema_quality_null          every ISO must have quality: null
                                  (peer review assigns quality)

  C3 h02_pattern_references_schema id declared in frontmatter must match the
                                  ID Pattern declared in the kind's bld_schema

  C4 domain_keywords_present      body must contain at least one domain
                                  keyword for the kind (e.g. voice_pipeline
                                  body must mention STT / TTS / audio / ...)

  C5 no_wrong_domain_keywords     body must not leak keywords from foreign
                                  domains (crypto terms in non-crypto kinds)

  C6 placeholders_resolved        no bare {{x}} outside fenced code blocks
                                  (unfilled template variables)

  C7 frontmatter_complete         required fields present:
                                  id, kind, pillar, title, quality, tags

Usage:
  python _tools/cex_wave_validator.py --scope archetypes/builders/voice-pipeline-builder/
  python _tools/cex_wave_validator.py --all archetypes/builders/
  python _tools/cex_wave_validator.py --staged
  python _tools/cex_wave_validator.py --scope <dir> --strict     # warn -> fail

Exit codes:
  0  all files pass
  1  one or more files fail
  2  bad invocation (missing args, scope not found, etc.)
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_shared import CEX_ROOT, parse_frontmatter  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BUILDER_DIR = CEX_ROOT / "archetypes" / "builders"

# ---------------------------------------------------------------------------
# Per-ISO expected llm_function
# ---------------------------------------------------------------------------
# Only files whose llm_function is fixed by design are listed here. Others
# (e.g. schema with CONSTRAIN, config with CONSTRAIN) are validated via the
# broader ISO_LLM_FUNCTION map below when --strict is set.

ISO_LLM_FUNCTION = {
    "bld_system_prompt":   "BECOME",
    "bld_manifest":        "BECOME",
    "bld_instruction":     "REASON",
    "bld_knowledge_card":  "INJECT",
    "bld_memory":          "INJECT",
    "bld_output_template": "PRODUCE",
    "bld_tools":           "CALL",
    "bld_collaboration":   "COLLABORATE",
    "bld_quality_gate":    "GOVERN",
    "bld_examples":        "GOVERN",
    "bld_architecture":    "CONSTRAIN",
    "bld_config":          "CONSTRAIN",
    "bld_schema":          "CONSTRAIN",
}

REQUIRED_FM_FIELDS = ["id", "kind", "pillar", "title", "quality", "tags"]

# ---------------------------------------------------------------------------
# Domain keywords (per kind)
# ---------------------------------------------------------------------------
# For high-signal kinds, define at least one keyword set. For kinds not listed
# we fall back to "kind name split into tokens" (voice_pipeline -> {voice,
# pipeline}). Missing ALL keywords = C4 fail.

DOMAIN_KEYWORDS: dict[str, list[str]] = {
    # Voice / audio
    "voice_pipeline":      ["STT", "TTS", "NLU", "audio", "voice", "ASR", "speech"],
    "realtime_session":    ["realtime", "websocket", "WebRTC", "session", "stream"],
    "tts_provider":        ["TTS", "synthesis", "voice", "speech"],
    "stt_provider":        ["STT", "ASR", "transcription", "speech"],
    "vad_config":          ["VAD", "voice activity", "silence", "speech"],
    "prosody_config":      ["prosody", "pitch", "rate", "intonation", "SSML"],
    "audio_tool":          ["audio", "waveform", "sample rate", "codec"],

    # Agent / model
    "agent":               ["agent", "role", "persona", "mission"],
    "agent_card":          ["agent", "capabilities", "contract", "card"],
    "agent_profile":       ["agent", "profile", "identity"],
    "agent_package":       ["agent", "package", "bundle", "distribution"],
    "agent_computer_interface": ["ACI", "interface", "agent", "computer"],
    "model_provider":      ["model", "provider", "API", "inference"],
    "model_card":          ["model", "card", "metrics", "evaluation"],
    "model_registry":      ["registry", "model", "version"],
    "model_architecture":  ["architecture", "model", "layers", "parameters"],
    "computer_use":        ["screen", "mouse", "keyboard", "computer use"],

    # Prompt / reasoning
    "prompt_template":     ["prompt", "template", "variable"],
    "system_prompt":       ["system prompt", "persona", "rules", "role"],
    "multimodal_prompt":   ["prompt", "image", "multimodal", "vision"],
    "prompt_cache":        ["cache", "prompt", "hit rate", "TTL"],
    "prompt_compiler":     ["compiler", "prompt", "optimization"],
    "prompt_optimizer":    ["optimizer", "prompt", "evaluation"],
    "prompt_technique":    ["technique", "prompting", "strategy"],
    "prompt_version":      ["version", "prompt", "revision"],
    "chain":               ["chain", "step", "prompt"],
    "few_shot_example":    ["few-shot", "example", "demonstration"],
    "instruction":         ["instruction", "step", "directive"],
    "reasoning_strategy":  ["reasoning", "chain-of-thought", "strategy"],
    "reasoning_trace":     ["reasoning", "trace", "step"],
    "planning_strategy":   ["planning", "plan", "strategy"],
    "thinking_config":     ["thinking", "budget", "tokens"],

    # Tools / integration
    "cli_tool":            ["CLI", "command", "argv", "subprocess"],
    "browser_tool":        ["browser", "DOM", "scrape", "HTML", "URL"],
    "api_client":          ["API", "HTTP", "REST", "endpoint", "request"],
    "webhook":             ["webhook", "HTTP POST", "callback", "event"],
    "mcp_server":          ["MCP", "server", "tool", "capability"],
    "code_executor":       ["execute", "sandbox", "runtime", "code"],
    "search_tool":         ["search", "query", "index", "retrieval"],
    "vision_tool":         ["vision", "image", "OCR", "caption"],
    "db_connector":        ["database", "connection", "query", "SQL"],
    "research_pipeline":   ["research", "pipeline", "source", "synthesis"],

    # Output / format
    "landing_page":        ["landing", "hero", "CTA", "conversion"],
    "diagram":             ["diagram", "node", "edge", "layout"],
    "formatter":           ["format", "output", "render"],
    "parser":              ["parser", "grammar", "tokens", "AST"],
    "response_format":     ["response", "format", "structured"],
    "edit_format":         ["edit", "diff", "patch"],
    "tagline":             ["tagline", "slogan", "hook"],

    # Schema / type
    "schema":              ["schema", "field", "type", "required"],
    "validation_schema":   ["validation", "schema", "constraint"],
    "input_schema":        ["input", "schema", "validation"],
    "type_def":            ["type", "definition", "field"],
    "interface":           ["interface", "contract", "method"],
    "enum_def":            ["enum", "variant", "value"],
    "function_def":        ["function", "parameter", "return"],

    # Evaluation
    "quality_gate":        ["quality", "gate", "threshold", "pass"],
    "scoring_rubric":      ["rubric", "score", "dimension", "weight"],
    "benchmark":           ["benchmark", "metric", "baseline"],
    "benchmark_suite":     ["benchmark", "suite", "test case"],
    "eval_framework":      ["evaluation", "framework", "harness"],
    "eval_metric":         ["metric", "evaluation", "score"],
    "eval_dataset":        ["dataset", "evaluation", "sample"],
    "llm_judge":           ["judge", "LLM", "evaluation", "rubric"],
    "judge_config":        ["judge", "config", "rubric"],
    "unit_eval":           ["unit", "test", "eval"],
    "smoke_eval":          ["smoke", "test", "minimal"],
    "e2e_eval":            ["end-to-end", "e2e", "integration"],
    "trajectory_eval":     ["trajectory", "sequence", "step"],
    "red_team_eval":       ["red team", "adversarial", "attack"],
    "regression_check":    ["regression", "baseline", "check"],
    "golden_test":         ["golden", "snapshot", "expected"],
    "bias_audit":          ["bias", "fairness", "demographic"],

    # Architecture
    "decision_record":     ["decision", "ADR", "context", "consequence"],
    "component_map":       ["component", "dependency", "map"],
    "naming_rule":         ["naming", "convention", "pattern"],
    "ontology":            ["ontology", "concept", "relation"],
    "knowledge_graph":     ["graph", "node", "edge", "relation"],
    "pattern":             ["pattern", "problem", "solution"],
    "mental_model":        ["mental model", "analogy", "abstraction"],
    "axiom":               ["axiom", "principle", "invariant"],
    "invariant":           ["invariant", "must", "always"],
    "repo_map":            ["repository", "map", "structure"],

    # Config / runtime
    "env_config":          ["environment", "variable", "config"],
    "path_config":         ["path", "directory", "config"],
    "secret_config":       ["secret", "credential", "encryption"],
    "feature_flag":        ["flag", "toggle", "feature"],
    "rate_limit_config":   ["rate limit", "throttle", "quota"],
    "sandbox_config":      ["sandbox", "isolation", "permission"],
    "boot_config":         ["boot", "startup", "init"],
    "batch_config":        ["batch", "job", "parallelism"],
    "hook_config":         ["hook", "trigger", "event"],
    "transport_config":    ["transport", "protocol", "connection"],
    "streaming_config":    ["streaming", "chunk", "delta"],
    "context_window_config": ["context", "window", "tokens"],
    "compression_config":  ["compression", "ratio", "algorithm"],
    "quantization_config": ["quantization", "bits", "precision"],
    "multi_modal_config":  ["multimodal", "image", "audio", "modality"],
    "experiment_config":   ["experiment", "variant", "config"],
    "finetune_config":     ["finetune", "training", "epochs"],
    "trace_config":        ["trace", "observability", "span"],

    # Memory / knowledge
    "knowledge_card":      ["knowledge", "card", "fact"],
    "knowledge_index":     ["index", "retrieval", "search"],
    "entity_memory":       ["entity", "memory", "recall"],
    "memory_scope":        ["memory", "scope", "user", "project"],
    "memory_summary":      ["summary", "memory", "compression"],
    "memory_type":         ["memory", "type", "short-term", "long-term"],
    "memory_architecture": ["memory", "architecture", "layer"],
    "memory_benchmark":    ["memory", "benchmark", "recall"],
    "procedural_memory":   ["procedural", "skill", "routine"],
    "consolidation_policy": ["consolidation", "policy", "memory"],
    "lifecycle_rule":      ["lifecycle", "ttl", "retention"],
    "session_state":       ["session", "state", "conversation"],
    "session_backend":     ["session", "backend", "storage"],
    "runtime_state":       ["runtime", "state", "process"],
    "checkpoint":          ["checkpoint", "snapshot", "resume"],
    "glossary_entry":      ["glossary", "term", "definition"],
    "citation":            ["citation", "source", "reference"],
    "lens":                ["lens", "perspective", "view"],
    "reference":           ["reference", "pointer", "source"],
    "context_doc":         ["context", "doc", "grounding"],
    "dataset_card":        ["dataset", "card", "source"],
    "rag_source":          ["RAG", "source", "corpus"],
    "retriever":           ["retriever", "search", "top-k"],
    "retriever_config":    ["retriever", "config", "top-k"],
    "reranker_config":     ["reranker", "rank", "score"],
    "embedder_provider":   ["embedder", "embedding", "model"],
    "embedding_config":    ["embedding", "dimension", "model"],
    "vector_store":        ["vector", "store", "similarity"],
    "chunk_strategy":      ["chunk", "strategy", "split"],
    "document_loader":     ["document", "loader", "parse"],
    "graph_rag_config":    ["graph", "RAG", "retrieval"],
    "agentic_rag":         ["agent", "RAG", "retrieval"],
    "search_strategy":     ["search", "strategy", "query"],

    # Feedback / safety
    "bugloop":             ["bug", "loop", "fix"],
    "guardrail":           ["guardrail", "safety", "constraint"],
    "content_filter":      ["filter", "content", "moderation"],
    "safety_policy":       ["safety", "policy", "harmful"],
    "threat_model":        ["threat", "attacker", "asset"],
    "incident_report":     ["incident", "report", "impact"],
    "compliance_framework": ["compliance", "regulation", "audit"],
    "permission":          ["permission", "grant", "deny"],
    "output_validator":    ["validator", "output", "check"],
    "validator":           ["validator", "check", "rule"],
    "validation_schema":   ["validation", "rule", "constraint"],
    "learning_record":     ["learning", "record", "outcome"],
    "reward_model":        ["reward", "model", "preference"],
    "reward_signal":       ["reward", "signal", "feedback"],
    "content_monetization": ["monetization", "pricing", "revenue"],
    "cost_budget":         ["cost", "budget", "spend"],

    # Orchestration
    "workflow":            ["workflow", "step", "orchestration"],
    "workflow_node":       ["node", "workflow", "step"],
    "workflow_primitive":  ["primitive", "workflow", "operation"],
    "dispatch_rule":       ["dispatch", "route", "rule"],
    "schedule":            ["schedule", "cron", "timing"],
    "supervisor":          ["supervisor", "coordinator", "worker"],
    "router":              ["router", "route", "decision"],
    "handoff":             ["handoff", "transfer", "context"],
    "handoff_protocol":    ["handoff", "protocol", "transfer"],
    "collaboration_pattern": ["collaboration", "pattern", "agents"],
    "spawn_config":        ["spawn", "process", "config"],
    "fallback_chain":      ["fallback", "chain", "provider"],
    "dual_loop_architecture": ["dual loop", "orchestrator", "worker"],
    "self_improvement_loop": ["improvement", "loop", "iteration"],
    "skill":               ["skill", "capability", "invoke"],
    "toolkit":             ["toolkit", "tools", "bundle"],
    "action_paradigm":     ["action", "paradigm", "pattern"],
    "action_prompt":       ["action", "prompt", "invoke"],
    "plugin":              ["plugin", "extension", "load"],
    "hook":                ["hook", "event", "callback"],
    "dag":                 ["DAG", "directed", "acyclic"],
    "daemon":              ["daemon", "background", "service"],
    "signal":              ["signal", "event", "notify"],
    "notifier":            ["notifier", "alert", "channel"],
    "runtime_rule":        ["runtime", "rule", "policy"],
    "visual_workflow":     ["visual", "workflow", "canvas"],
    "effort_profile":      ["effort", "budget", "depth"],
    "constraint_spec":     ["constraint", "spec", "limit"],
    "diff_strategy":       ["diff", "patch", "merge"],
    "optimizer":           ["optimizer", "objective", "update"],
    "rl_algorithm":        ["RL", "policy", "gradient"],
    "training_method":     ["training", "method", "loss"],
    "experiment_tracker":  ["experiment", "tracker", "metric"],
    "hitl_config":         ["human", "in-the-loop", "HITL"],

    # Brand / content
    "brand":               ["brand", "identity", "voice"],
    "software_project":    ["project", "software", "repository"],
    "supabase_data_layer": ["Supabase", "Postgres", "data"],
    "social_publisher":    ["social", "publish", "channel"],
}

# ---------------------------------------------------------------------------
# Foreign-domain leak blacklists
# ---------------------------------------------------------------------------
# If the kind is NOT in the "allowed" set, these keywords in the body indicate
# template/LLM leakage (e.g. gemma4 injecting crypto tutorial text into a
# voice_pipeline builder).

CRYPTO_TERMS = [
    "solana", "ethereum", "staking", "DeFi", "NFT", "smart contract",
    "blockchain", "tokenomics", "airdrop", "wallet address",
]

# kinds that legitimately discuss crypto (none currently; whitelist if added)
CRYPTO_ALLOWED_KINDS: set[str] = set()

# ---------------------------------------------------------------------------
# Frontmatter + body extraction
# ---------------------------------------------------------------------------

FM_RE = re.compile(r"^---\n(.*?)\n---\s*", re.DOTALL)
PLACEHOLDER_RE = re.compile(r"\{\{[A-Za-z_][A-Za-z0-9_ ]*\}\}")
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")

ID_PATTERN_RE = re.compile(r"`(\^[^`]+\$)`")


def split_frontmatter(content: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_str). Empty dict if no frontmatter."""
    fm = parse_frontmatter(content)
    if fm is None:
        return {}, content
    m = FM_RE.match(content)
    body = content[m.end():] if m else content
    return fm, body


def strip_code_fences(body: str) -> str:
    """Remove fenced AND inline code so placeholder scans ignore examples.

    Placeholders wrapped in backticks (e.g. `{{vars}}`) are documentation
    references, not unfilled template slots.
    """
    without_fences = CODE_FENCE_RE.sub("", body)
    return INLINE_CODE_RE.sub("", without_fences)


def kind_from_filename(name: str) -> str:
    """bld_system_prompt_voice_pipeline.md -> voice_pipeline.

    Strips the leading bld_{iso}_ prefix. Returns '' if not a builder ISO.
    """
    if not name.startswith("bld_") or not name.endswith(".md"):
        return ""
    stem = name[4:-3]  # strip bld_ and .md
    for iso in ISO_LLM_FUNCTION:
        prefix = iso[4:] + "_"  # e.g. system_prompt_
        if stem.startswith(prefix):
            return stem[len(prefix):]
    return ""


def iso_type_from_filename(name: str) -> str:
    """bld_system_prompt_voice_pipeline.md -> bld_system_prompt."""
    if not name.startswith("bld_") or not name.endswith(".md"):
        return ""
    stem = name[:-3]
    for iso in ISO_LLM_FUNCTION:
        if stem.startswith(iso + "_") or stem == iso:
            return iso
    return ""


# ---------------------------------------------------------------------------
# The 7 checks
# ---------------------------------------------------------------------------


def check_system_prompt_llm_function(fm: dict, iso: str) -> list[str]:
    """C1: bld_system_prompt_*.md must have llm_function: BECOME.

    Applied to all ISO types with a fixed expected value.
    """
    expected = ISO_LLM_FUNCTION.get(iso)
    if not expected:
        return []
    actual = str(fm.get("llm_function", "")).strip()
    if actual != expected:
        return [f"llm_function is '{actual or 'MISSING'}' (expected '{expected}')"]
    return []


def check_schema_quality_null(fm: dict) -> list[str]:
    """C2: quality must be null (unscored) OR a numeric peer-review score.

    The authoring rule is 'quality: null' -- the author never self-scores.
    Peer review (cex_score.py, AUTO cycles) then writes a numeric value.
    So both states are valid at rest:
      - null:           awaiting peer review (fresh artifact)
      - float in 5..10: peer-reviewed

    Real defects caught here:
      - 'quality' field missing entirely
      - non-numeric string ('high', 'good')
      - out-of-range numeric (<5 or >10)
    """
    if "quality" not in fm:
        return ["quality field missing from frontmatter"]
    q = fm["quality"]
    if q is None:
        return []
    if isinstance(q, (int, float)):
        try:
            f = float(q)
        except (TypeError, ValueError):
            return [f"quality '{q}' is not null and not numeric"]
        if 5.0 <= f <= 10.0:
            return []
        return [f"quality {f} is out of valid range [5.0, 10.0]"]
    return [f"quality '{q}' is not null and not numeric"]


def check_h02_id_pattern(fm: dict, kind: str, schema_pattern: str | None) -> list[str]:
    """C3: id references a valid schema-style pattern.

    Builder ISOs use their own id conventions (bld_{iso}_{kind},
    p{NN}_{slug}_builder, etc.) -- they should NOT match the runtime artifact
    ID Pattern declared inside the kind's bld_schema (that pattern is for
    future artifacts of the kind, not for the specs themselves).

    What we actually enforce:
      - id must be present and non-empty
      - id must match one of the accepted shapes:
          a. starts with 'bld_'
          b. starts with 'p\\d{2}_' (pillar prefix)
      - pillar, if declared, must match P## pattern (checked in C7)
    """
    iid = str(fm.get("id", "")).strip()
    if not iid:
        return ["id field missing or empty"]

    if iid.startswith("bld_"):
        return []
    if re.match(r"^p\d{2}_", iid, re.IGNORECASE):
        return []
    if iid.endswith("-builder") or iid.endswith("_builder"):
        return []

    return [
        f"id '{iid}' has no recognized prefix/suffix "
        "(expected 'bld_...', 'p##_...', or '...-builder')"
    ]


def check_domain_keywords_present(body: str, kind: str) -> list[str]:
    """C4: body must contain at least one domain-specific keyword."""
    if not kind:
        return []
    keywords = DOMAIN_KEYWORDS.get(kind)
    if not keywords:
        tokens = [t for t in kind.split("_") if len(t) > 2]
        keywords = tokens or [kind]
    lower = body.lower()
    if any(kw.lower() in lower for kw in keywords):
        return []
    shown = ", ".join(f"'{k}'" for k in keywords[:5])
    return [f"body missing domain keyword for '{kind}' (expected one of: {shown})"]


def check_no_wrong_domain_keywords(body: str, kind: str) -> list[str]:
    """C5: body must not leak foreign-domain keywords (crypto in non-crypto).

    Uses word boundaries so 'DeFi' does not match 'definitions' and 'NFT'
    does not match 'NFTable'.
    """
    if kind in CRYPTO_ALLOWED_KINDS:
        return []
    hits = []
    for term in CRYPTO_TERMS:
        # escape and anchor with word boundaries
        pattern = r"\b" + re.escape(term) + r"\b"
        if re.search(pattern, body, re.IGNORECASE):
            hits.append(term)
    if hits:
        return [f"foreign-domain keyword(s) leaked into body: {', '.join(hits)}"]
    return []


def check_placeholders_resolved(body: str, iso: str) -> list[str]:
    """C6: no bare {{x}} outside fenced code blocks.

    Placeholders are legitimate content in:
      - bld_output_template_* (the whole point of the file)
      - bld_config_* (paths like {{base}}/{{name}}/)
      - bld_schema_* (schema examples sometimes show {{var}})

    For those, C6 is skipped entirely. For other ISOs, we still allow the
    two universal placeholders {{name}} and {{kind}} (templating seeds).
    """
    if iso in ("bld_output_template", "bld_config", "bld_schema"):
        return []
    stripped = strip_code_fences(body)
    leaks = PLACEHOLDER_RE.findall(stripped)
    allow = {"{{name}}", "{{kind}}", "{{brand}}"}
    brand_pat = re.compile(r"^\{\{BRAND_[A-Z_]+\}\}$")
    path_allow = {"{{APP_ROOT}}", "{{USER_DIR}}", "{{base_dir}}"}
    leaks = [p for p in leaks
             if p not in allow
             and p not in path_allow
             and not brand_pat.match(p)]
    if leaks:
        unique = sorted(set(leaks))[:5]
        return [f"unresolved placeholder(s) in body: {', '.join(unique)}"]
    return []


def check_frontmatter_complete(fm: dict) -> list[str]:
    """C7: required frontmatter fields present."""
    errs = []
    for field in REQUIRED_FM_FIELDS:
        if field not in fm:
            errs.append(f"frontmatter missing required field: {field}")
    pillar = str(fm.get("pillar", "")).strip()
    if pillar and not re.match(r"^P\d{2}$", pillar):
        errs.append(f"pillar '{pillar}' does not match P## pattern")
    tags = fm.get("tags")
    if "tags" in fm and not isinstance(tags, list):
        errs.append(f"tags must be a list, got {type(tags).__name__}")
    return errs


# ---------------------------------------------------------------------------
# Schema pattern lookup per-kind
# ---------------------------------------------------------------------------


def load_schema_pattern(builder_dir: Path, kind: str) -> str | None:
    """Extract the ID Pattern regex from bld_schema_{kind}.md, if present."""
    if not kind:
        return None
    schema_path = builder_dir / f"bld_schema_{kind}.md"
    if not schema_path.exists():
        return None
    try:
        text = schema_path.read_text(encoding="utf-8")
    except OSError:
        return None
    m = ID_PATTERN_RE.search(text)
    if m:
        return m.group(1)
    return None


# ---------------------------------------------------------------------------
# File validator (runs all 7 checks)
# ---------------------------------------------------------------------------


def validate_file(path: Path) -> list[str]:
    """Return a list of error messages; empty = PASS."""
    errors: list[str] = []
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as e:
        return [f"cannot read file: {e}"]

    fm, body = split_frontmatter(content)
    if not fm:
        return ["no valid YAML frontmatter"]

    name = path.name
    iso = iso_type_from_filename(name)
    kind = kind_from_filename(name)

    schema_pattern = load_schema_pattern(path.parent, kind)

    errors += check_system_prompt_llm_function(fm, iso)
    errors += check_schema_quality_null(fm)
    errors += check_h02_id_pattern(fm, kind, schema_pattern)
    errors += check_domain_keywords_present(body, kind)
    errors += check_no_wrong_domain_keywords(body, kind)
    # Meta-builder templates in _builder-builder/ are literal templates: their
    # unfilled {{placeholders}} are the product, not a bug. Skip C6 for them.
    if "_builder-builder" not in str(path).replace("\\", "/"):
        errors += check_placeholders_resolved(body, iso)
    errors += check_frontmatter_complete(fm)

    return errors


# ---------------------------------------------------------------------------
# Runners (scope, all, staged)
# ---------------------------------------------------------------------------


def iter_builder_files(scope: Path) -> Iterable[Path]:
    """Yield every bld_*.md file under scope (recursive)."""
    if scope.is_file():
        if scope.name.startswith("bld_") and scope.suffix == ".md":
            yield scope
        return
    if not scope.exists():
        return
    for p in sorted(scope.rglob("bld_*.md")):
        yield p


def get_staged_builder_files() -> list[Path]:
    """Return staged archetypes/builders/*/bld_*.md files."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            capture_output=True, text=True, timeout=10,
        )
    except Exception:
        return []
    files = []
    for line in result.stdout.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        if not line.endswith(".md"):
            continue
        norm = line.replace("\\", "/")
        if "archetypes/builders/" not in norm:
            continue
        if not Path(line).name.startswith("bld_"):
            continue
        files.append(CEX_ROOT / line)
    return files


def run_validation(files: list[Path], label: str = "") -> int:
    """Validate a list of files; print results and return exit code."""
    if not files:
        print("cex_wave_validator: no files to check")
        return 0

    if label:
        print(f"cex_wave_validator scanning {label}")

    pass_count = 0
    fail_count = 0
    first_dir = None
    for path in files:
        try:
            rel = path.relative_to(CEX_ROOT)
        except ValueError:
            rel = path
        rel_str = str(rel).replace("\\", "/")

        parent = str(path.parent).replace("\\", "/")
        if parent != first_dir:
            first_dir = parent
            if not label:
                try:
                    pdir = path.parent.relative_to(CEX_ROOT)
                    print(f"cex_wave_validator scanning {str(pdir).replace(chr(92), '/')}/")
                except ValueError:
                    pass

        errors = validate_file(path)
        if errors:
            fail_count += 1
            print(f"  [FAIL] {path.name}")
            for e in errors:
                print(f"    - {e}")
        else:
            pass_count += 1
            print(f"  [PASS] {path.name}")

    total = pass_count + fail_count
    print(f"\nSummary: {pass_count}/{total} PASS, {fail_count}/{total} FAIL")
    if fail_count:
        print(f"Exit code: 1 ({fail_count} file(s) failed validation)")
        return 1
    print("Exit code: 0 (all files passed)")
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="cex_wave_validator",
        description="Validate builder ISOs before commit (7 systemic checks).",
    )
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--scope", type=str,
                     help="Path to a single builder directory (e.g. archetypes/builders/voice-pipeline-builder/)")
    src.add_argument("--all", dest="all_path", type=str,
                     help="Path to a parent dir; scan ALL bld_*.md under it")
    src.add_argument("--staged", action="store_true",
                     help="Validate only staged archetypes/builders/*/bld_*.md files")
    p.add_argument("--fix", action="store_true",
                   help="(reserved) auto-fix trivial issues; currently a no-op")
    p.add_argument("--strict", action="store_true",
                   help="Treat all check categories as hard failures")
    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    if args.fix:
        print("cex_wave_validator: --fix is reserved for future use (no-op)")

    if args.staged:
        files = get_staged_builder_files()
        return run_validation(files, label="staged files")

    scope_arg = args.scope or args.all_path
    scope = Path(scope_arg)
    if not scope.is_absolute():
        scope = (CEX_ROOT / scope_arg).resolve()

    if not scope.exists():
        print(f"cex_wave_validator: scope not found: {scope}")
        return 2

    files = list(iter_builder_files(scope))
    try:
        label = str(scope.relative_to(CEX_ROOT)).replace("\\", "/") + "/"
    except ValueError:
        label = str(scope)
    return run_validation(files, label=label)


if __name__ == "__main__":
    sys.exit(main())
