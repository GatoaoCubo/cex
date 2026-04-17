"""
Wave 1-3: Generate 13 ISOs per kind using Ollama.
V2: Hardened generator with 7 systemic fixes + ISO body validation.

Fixes from HYBRID_REVIEW + HYBRID_REVIEW2 audits:
  1. system_prompt llm_function: BECOME (not INJECT) -- enforced in frontmatter + prompt
  2. schema quality field: type=null, default=null, examples=[null]
  3. quality_gate H02: references actual schema ID pattern (not generic regex)
  4. domain keyword validation: reject ISO body missing kind-domain terms
  5. output_template placeholders: reject bare {{field}} without schema-backed context
  6. architecture domain check: reject blockchain keywords for non-blockchain kinds
  7. compiled yaml integrity: auto-compile .md after save via cex_compile.py

Backward compat: same CLI flags as v1. Wave 2 (running) uses v1; v2 targets Wave 3 + regen.

Usage:
  python _tools/wave1_builder_gen_v2.py                     # Wave 1 (16 kinds)
  python _tools/wave1_builder_gen_v2.py --wave 2            # Wave 2 (18 kinds)
  python _tools/wave1_builder_gen_v2.py --wave 3            # Wave 3 (18 kinds)
  python _tools/wave1_builder_gen_v2.py --wave all          # All 52 kinds
  python _tools/wave1_builder_gen_v2.py --kind threat_model # Single kind
  python _tools/wave1_builder_gen_v2.py --validate-only     # Validate existing ISOs only
"""
import json, os, sys, re, time, argparse, subprocess, requests
from datetime import date
from pathlib import Path
from typing import Any

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:14b"           # v2 default: qwen3:14b (better than gemma4:26b for domain fidelity)
META_PATH = ".cex/kinds_meta.json"
BUILDERS_DIR = "archetypes/builders"
COMPILE_TOOL = "_tools/cex_compile.py"
TODAY = date.today().isoformat()

# ============================================================
# Wave definitions (same as v1 -- backward compat)
# ============================================================
WAVE1_KINDS = [
    "threat_model", "safety_policy", "content_filter",
    "bias_audit", "compliance_framework", "incident_report",
    "reasoning_strategy", "rl_algorithm", "reward_model",
    "search_strategy", "thinking_config",
    "agent_profile", "planning_strategy", "action_paradigm",
    "collaboration_pattern", "dual_loop_architecture",
]

WAVE2_KINDS = [
    "voice_pipeline", "realtime_session", "vad_config",
    "tts_provider", "stt_provider", "prosody_config", "transport_config",
    "edit_format", "sandbox_config", "repo_map",
    "diff_strategy", "agent_computer_interface",
    "training_method", "model_architecture", "dataset_card",
    "model_registry", "experiment_tracker", "quantization_config",
]

WAVE3_KINDS = [
    "benchmark_suite", "judge_config", "eval_metric",
    "eval_framework", "trajectory_eval",
    "reranker_config", "graph_rag_config", "agentic_rag",
    "memory_architecture", "procedural_memory",
    "consolidation_policy", "memory_benchmark",
    "prompt_technique", "prompt_optimizer", "multimodal_prompt",
    "workflow_node", "visual_workflow",
    "self_improvement_loop",
]

WAVE4_KINDS = [
    "ab_test_config", "course_module", "subscription_tier",
    "user_journey", "compliance_checklist", "usage_report",
    "rbac_policy", "audit_log", "onboarding_flow",
    "pricing_page", "cohort_analysis", "referral_program",
    "enterprise_sla", "data_residency", "sso_config",
    "white_label_config", "usage_quota", "customer_segment",
]

WAVE5_KINDS = [
    "quickstart_guide", "api_reference", "pitch_deck",
    "roi_calculator", "case_study", "playground_config",
    "sdk_example", "competitive_matrix", "interactive_demo",
    "integration_guide", "sales_playbook", "changelog",
    "sandbox_spec", "discovery_questions",
    "healthcare_vertical", "fintech_vertical", "legal_vertical",
    "product_tour",
]

WAVE6_KINDS = [
    "ecommerce_vertical", "govtech_vertical", "edtech_vertical",
    "partner_listing", "marketplace_app_manifest", "oauth_app_config",
    "app_directory_entry", "contributor_guide", "code_of_conduct",
    "github_issue_template", "faq_entry", "nps_survey",
    "churn_prevention_playbook", "expansion_play", "renewal_workflow",
    "analyst_briefing", "press_release", "webinar_script",
]

WAVE_MAP = {
    "1": WAVE1_KINDS,
    "2": WAVE2_KINDS,
    "3": WAVE3_KINDS,
    "4": WAVE4_KINDS,
    "5": WAVE5_KINDS,
    "6": WAVE6_KINDS,
    "all": WAVE1_KINDS + WAVE2_KINDS + WAVE3_KINDS + WAVE4_KINDS + WAVE5_KINDS + WAVE6_KINDS,
}

# ============================================================
# ISO specs (FIX 1: system_prompt llm_function=BECOME enforced)
# ============================================================
ISO_SPECS = [
    ("bld_manifest_{k}.md",        "type_builder",  "{pillar}", "BECOME",    "Builder identity, capabilities, routing for {kind}"),
    ("bld_instruction_{k}.md",     "instruction",   "P03",      "REASON",    "Step-by-step production process for {kind}"),
    ("bld_system_prompt_{k}.md",   "system_prompt", "P03",      "BECOME",    "System prompt defining {kind}-builder persona and rules"),  # BECOME not INJECT
    ("bld_schema_{k}.md",          "schema",        "P06",      "CONSTRAIN", "Formal schema -- SINGLE SOURCE OF TRUTH for {kind}"),
    ("bld_quality_gate_{k}.md",    "quality_gate",  "P11",      "GOVERN",    "Quality gate with HARD and SOFT scoring for {kind}"),
    ("bld_output_template_{k}.md", "output_template","P05",     "PRODUCE",   "Template with vars for {kind} production"),
    ("bld_examples_{k}.md",        "examples",      "P07",      "GOVERN",    "Golden and anti-examples of {kind} artifacts"),
    ("bld_knowledge_card_{k}.md",  "knowledge_card","P01",      "INJECT",    "Domain knowledge for {kind} production"),
    ("bld_architecture_{k}.md",    "architecture",  "P08",      "CONSTRAIN", "Component map of {kind} -- inventory, dependencies"),
    ("bld_collaboration_{k}.md",   "collaboration", "P12",      "COLLABORATE","How {kind}-builder works in crews with other builders"),
    ("bld_config_{k}.md",          "config",        "P09",      "CONSTRAIN", "Naming, paths, limits for {kind} production"),
    ("bld_memory_{k}.md",          "learning_record","P10",     "INJECT",    "Learned patterns and pitfalls for {kind} construction"),
    ("bld_tools_{k}.md",           "tools",         "P04",      "CALL",      "Tools available for {kind} production"),
]

# ============================================================
# FIX 4 + 6: Domain validation config
# ============================================================

# Per-kind regex: body MUST match at least one of these terms
DOMAIN_KEYWORDS = {
    # Voice / audio stack
    "voice_pipeline":           r"audio|stream|latency|VAD|TTS|STT|WebRTC|RTP|codec",
    "realtime_session":         r"audio|stream|VAD|barge.in|ephemeral|WebRTC|WebSocket|bidirectional",
    "vad_config":               r"voice.activity|VAD|silence|threshold|detection|frame",
    "tts_provider":             r"text.to.speech|synthesis|voice|neural|ElevenLabs|Polly|WaveNet",
    "stt_provider":             r"speech.to.text|transcription|recognition|ASR|Deepgram|Whisper",
    "prosody_config":           r"pitch|rate|volume|prosody|SSML|intonation|cadence",
    "transport_config":         r"transport|protocol|WebRTC|WebSocket|latency|gRPC|stream",
    # Reasoning / RL
    "reasoning_strategy":       r"reasoning|inference|chain.of.thought|decompose|strategy",
    "thinking_config":          r"thinking|reasoning|budget|tokens|scratchpad|chain",
    "rl_algorithm":             r"reward|policy|agent|reinforcement|Q.learning|gradient|episode",
    "reward_model":             r"reward|signal|preference|RLHF|feedback|scalar|human",
    "search_strategy":          r"search|retrieval|query|index|ranking|BM25|vector|recall",
    # Agent architecture
    "agent_profile":            r"agent|capability|role|task|autonomy|tool|skill",
    "planning_strategy":        r"plan|goal|decompose|strategy|step|action|horizon",
    "action_paradigm":          r"action|paradigm|agent|execute|state|tool|loop",
    "collaboration_pattern":    r"collaboration|multi.agent|crew|coordination|handoff|protocol",
    "dual_loop_architecture":   r"loop|architecture|agent|feedback|iteration|outer|inner|cycle",
    # Safety
    "threat_model":             r"threat|attack|vulnerability|risk|adversar|mitigation",
    "safety_policy":            r"safety|policy|harm|guardrail|restrict|prohibit|red.line",
    "content_filter":           r"content|filter|block|detect|classify|moderat|toxic",
    "bias_audit":               r"bias|fairness|equity|stereotype|representation|audit|disparity",
    "compliance_framework":     r"compliance|regulation|GDPR|ISO|audit|governance|control|SOC",
    "incident_report":          r"incident|report|root.cause|postmortem|severity|timeline|RCA",
    # ML lifecycle
    "training_method":          r"training|fine.tun|dataset|loss|gradient|epoch|batch|LoRA|PEFT",
    "model_architecture":       r"model|architecture|layer|attention|transformer|parameter|head",
    "dataset_card":             r"dataset|split|annotation|license|schema|bias|provenance",
    "model_registry":           r"registry|model|version|artifact|lineage|deploy|stage",
    "experiment_tracker":       r"experiment|tracking|metric|run|artifact|MLflow|wandb|neptune",
    "quantization_config":      r"quantization|precision|int8|int4|weight|inference|GPTQ|AWQ",
    # Code agents
    "edit_format":              r"edit|diff|patch|format|code|unified|apply|hunk",
    "sandbox_config":           r"sandbox|container|isolat|execute|secur|docker|nsjail|firejail",
    "repo_map":                 r"repository|codebase|index|symbol|graph|tree|function|AST",
    "diff_strategy":            r"diff|patch|merge|conflict|change|hunk|delta|three.way",
    "agent_computer_interface": r"computer|interface|action|screenshot|click|keyboard|GUI|cursor",
    # Eval
    "benchmark_suite":          r"benchmark|eval|suite|score|metric|dataset|baseline|harness",
    "judge_config":             r"judge|eval|criteria|score|LLM|rubric|dimension|prompt",
    "eval_metric":              r"metric|eval|score|measure|threshold|precision|recall|F1",
    "eval_framework":           r"evaluation|framework|pipeline|metric|dataset|harness|runner",
    "trajectory_eval":          r"trajectory|eval|step|action|rollout|episode|sequence|trace",
    # RAG
    "reranker_config":          r"rerank|cross.encoder|score|retrieval|relevance|biencoder|ColBERT",
    "graph_rag_config":         r"graph|RAG|entity|relation|knowledge|triple|node|edge|Neo4j",
    "agentic_rag":              r"agentic|RAG|retrieval|agent|tool|query|generation|plan|reflect",
    # Memory
    "memory_architecture":      r"memory|architecture|scope|storage|retrieval|episodic|semantic",
    "procedural_memory":        r"procedural|memory|sequence|skill|action|routine|habit",
    "consolidation_policy":     r"consolidation|memory|compress|prune|policy|decay|retention",
    "memory_benchmark":         r"memory|benchmark|eval|capacity|recall|retention|task",
    # Prompt
    "prompt_technique":         r"prompt|technique|chain.of.thought|few.shot|template|CoT|self.consistency",
    "prompt_optimizer":         r"prompt|optimizer|DSPy|compile|improve|metric|bootstrap|teleprompter",
    "multimodal_prompt":        r"multimodal|prompt|image|vision|audio|modality|interleav|pixel",
    # Workflow
    "workflow_node":            r"workflow|node|step|state|transition|input|output|trigger",
    "visual_workflow":          r"workflow|visual|diagram|flow|node|edge|DAG|Mermaid|canvas",
    # Self improvement
    "self_improvement_loop":    r"self.improv|loop|feedback|iterate|evolve|score|cycle|reward",
}

# FIX 6: Keywords that must NOT appear in architecture ISOs of non-blockchain kinds
WRONG_DOMAIN_PATTERN = re.compile(
    r"\b(trading|staking|DeFi|Solana|Ethereum|blockchain|crypto\b|NFT|market.cap|wallet.address)\b",
    re.IGNORECASE
)

# Kinds that legitimately discuss blockchain (none in current set -- future-proof)
BLOCKCHAIN_KINDS = set()

# The 13 ISO component names that should appear in architecture ISOs
ISO_COMPONENT_NAMES = [
    "bld_manifest", "bld_instruction", "bld_system_prompt", "bld_schema",
    "bld_quality_gate", "bld_output_template", "bld_examples", "bld_knowledge_card",
    "bld_architecture", "bld_collaboration", "bld_config", "bld_memory", "bld_tools",
]


# ============================================================
# FIX 4 + 5 + 6: Pre-commit ISO body validator
# ============================================================

def validate_iso_body(iso_type: str, kind: str, body: str) -> tuple[bool, list[str]]:
    """
    Pre-commit validation of generated ISO body content.
    Returns (passed: bool, errors: list[str]).

    Checks applied:
      1. Domain keywords: body must match at least one kind-specific term
      2. Wrong-domain keywords: architecture ISO must not contain blockchain terms
      3. Output template: reject bare {{field}} placeholders without schema context
      4. Quality gate: H02 pattern must not be a known bad generic regex
    """
    errors = []

    # Check 1: Domain keyword presence (any ISO type)
    if kind in DOMAIN_KEYWORDS:
        pattern = DOMAIN_KEYWORDS[kind]
        if not re.search(pattern, body, re.IGNORECASE):
            errors.append(
                "Domain check FAIL: body missing kind-specific terms. "
                "Expected pattern: " + pattern[:60]
            )

    # Check 2: Wrong-domain keywords in architecture ISO
    if iso_type == "architecture" and kind not in BLOCKCHAIN_KINDS:
        match = WRONG_DOMAIN_PATTERN.search(body)
        if match:
            errors.append(
                "Wrong-domain keyword in architecture ISO: '" + match.group() + "'. "
                "Architecture must list the 13 builder ISOs, not a business/blockchain tech stack."
            )

    # Check 3: Bare placeholders in output_template without schema context
    if iso_type == "output_template":
        bare = re.findall(r"\{\{[a-zA-Z_]+\}\}", body)
        has_comment = bool(re.search(r"<!--.*?-->", body, re.DOTALL))
        has_schema_ref = "schema" in body.lower() or "frontmatter" in body.lower()
        if bare and not has_comment and not has_schema_ref:
            short = [b for b in bare[:3]]
            errors.append(
                "Bare placeholders without schema context: " + str(short) + ". "
                "Add <!-- comment --> guidance or reference schema fields."
            )

    # Check 4: Quality gate H02 must not use known bad generic patterns
    if iso_type == "quality_gate":
        bad_patterns = [
            r"PXX-YYYY",
            r"rl_\[a-z0-9\]",
            r"\[A-Z\]\{3\}-\[0-9\]\{4\}",
            r"P04-\[A-Z\]\{3\}",
        ]
        for bp in bad_patterns:
            if bp in body:
                errors.append(
                    "quality_gate H02 uses generic pattern '" + bp + "'. "
                    "Replace with exact ID pattern from bld_schema (e.g. ^p04_vp_[a-z][a-z0-9_]+$)."
                )
                break

    return (len(errors) == 0, errors)


# ============================================================
# Helper: derive ID regex from naming convention
# ============================================================

def derive_id_pattern(naming: str, kind: str) -> str:
    """
    Derive regex ID pattern from naming convention template.
    Example: 'p04_vp_{{name}}' -> '^p04_vp_[a-z][a-z0-9_]+$'
    """
    base = naming.replace("{{name}}", "[a-z][a-z0-9_]+")
    base = base.replace("{{timestamp}}", "[0-9]+")
    # Remove any remaining unfilled templates gracefully
    base = re.sub(r"\{\{[^}]+\}\}", "[a-z][a-z0-9_]+", base)
    return "^" + base + "$"


# ============================================================
# Ollama call (same as v1 with model override)
# ============================================================

def ollama_generate(prompt: str, max_tokens: int = 2048, model: str | None = None) -> str | None:
    """Call Ollama with /no_think for fast structured output."""
    use_model = model or MODEL
    for attempt in range(3):
        try:
            resp = requests.post(OLLAMA_URL, json={
                "model": use_model,
                "prompt": prompt + "\n/no_think",
                "stream": False,
                "options": {"num_predict": max_tokens, "temperature": 0.3}
            }, timeout=600)
            resp.raise_for_status()
            text = resp.json().get("response", "").strip()
            # Strip thinking tags if present
            if "<think>" in text:
                text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
            if len(text) > 50:
                return text
            print("  [WARN] Short response (" + str(len(text)) + " chars), retry " + str(attempt + 1))
        except Exception as e:
            print("  [WARN] Ollama error (attempt " + str(attempt + 1) + "): " + str(e))
            time.sleep(2)
    return None


def load_kind_meta(kind: str) -> dict[str, Any]:
    with open(META_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get(kind, {})


# ============================================================
# Prompt generators (updated with systemic fixes)
# ============================================================

def build_manifest_prompt(kind: str, meta: dict[str, Any]) -> str:
    return (
        "You are generating a builder manifest for CEX kind '" + kind + "'.\n"
        "The kind belongs to pillar " + meta["pillar"] + " with llm_function " + meta["llm_function"] + ".\n"
        "Description: " + meta["description"] + "\n"
        "Boundary: " + meta["boundary"] + "\n\n"
        "Generate the body content (NO frontmatter, just markdown) for a builder manifest with these sections:\n"
        "## Identity\n"
        "(2-3 sentences: what this builder specializes in, what domain knowledge it has)\n"
        "## Capabilities\n"
        "(5 numbered capabilities this builder has)\n"
        "## Routing\n"
        "(keywords and triggers for when to invoke this builder)\n"
        "## Crew Role\n"
        "(1 paragraph: role in a team, what it answers, what it does NOT handle)\n\n"
        "Be specific to " + kind + ". Use industry terminology. ASCII only. Under 60 lines."
    )


def build_instruction_prompt(kind: str, meta: dict[str, Any]) -> str:
    return (
        "Generate production instructions for building a '" + kind + "' artifact.\n"
        "Kind: " + kind + ", Pillar: " + meta["pillar"] + ", Function: " + meta["llm_function"] + "\n"
        "Description: " + meta["description"] + "\n\n"
        "Generate markdown body (NO frontmatter) with:\n"
        "## Phase 1: RESEARCH\n"
        "(6 numbered steps specific to " + kind + ")\n"
        "## Phase 2: COMPOSE\n"
        "(9 numbered steps for writing the artifact, referencing SCHEMA.md and OUTPUT_TEMPLATE.md)\n"
        "## Phase 3: VALIDATE\n"
        "(5 numbered validation steps with checkbox format)\n\n"
        "Be domain-specific. ASCII only. Under 70 lines."
    )


def build_system_prompt_prompt(kind: str, meta: dict[str, Any]) -> str:
    # FIX 1: Explicitly instruct BECOME, not INJECT
    return (
        "Generate a system prompt for the " + kind + "-builder agent.\n"
        "Kind: " + kind + ", Pillar: " + meta["pillar"] + "\n"
        "CRITICAL: This system prompt operates at the F2 BECOME stage (builder persona loading).\n"
        "llm_function MUST be BECOME -- NOT INJECT, NOT REASON, NOT CALL.\n"
        "Description: " + meta["description"] + "\n"
        "Boundary: " + meta["boundary"] + "\n\n"
        "Generate markdown body (NO frontmatter) with:\n"
        "## Identity\n"
        "(1 paragraph defining who this agent is and what it produces)\n"
        "## Rules\n"
        "### Scope\n"
        "(3 rules about what it produces and what it does NOT)\n"
        "### Quality\n"
        "(5 rules about quality requirements specific to " + kind + ")\n"
        "### ALWAYS / NEVER\n"
        "(2 ALWAYS + 2 NEVER rules using ALL CAPS format)\n\n"
        "Be specific. Use industry terms. ASCII only. Under 60 lines."
    )


def build_schema_prompt(kind: str, meta: dict[str, Any]) -> str:
    naming = meta.get("naming", "p00_x_{{name}}")
    id_pattern = derive_id_pattern(naming, kind)
    # FIX 2: Explicit quality field spec; FIX 3: pass derived ID pattern
    return (
        "Generate a formal schema for CEX kind '" + kind + "'.\n"
        "Pillar: " + meta["pillar"] + ", Naming: " + naming + ", Max bytes: " + str(meta.get("max_bytes", 5120)) + "\n"
        "ID pattern (use this exact regex in the ## ID Pattern section): " + id_pattern + "\n\n"
        "Generate markdown body (NO frontmatter) with:\n"
        "## Frontmatter Fields\n"
        "### Required\n"
        "(Table: Field | Type | Required | Default | Notes -- at least 10 fields)\n"
        "CRITICAL quality field row (copy exactly):\n"
        "| quality | null | yes | null | Never self-score; peer review assigns |\n"
        "Include: id, kind, pillar, title, version, created, updated, author, domain, quality, tags, tldr\n"
        "Plus 2-4 domain-specific fields for " + kind + "\n"
        "### Recommended\n"
        "(Table: 3-4 optional fields)\n"
        "## ID Pattern\n"
        "(Use this exact pattern: " + id_pattern + ")\n"
        "## Body Structure (required sections)\n"
        "(4-6 numbered sections specific to " + kind + ")\n"
        "## Constraints\n"
        "(5-6 bullet constraints)\n\n"
        "ASCII only. Under 80 lines."
    )


def build_quality_gate_prompt(kind: str, meta: dict[str, Any]) -> str:
    naming = meta.get("naming", "p00_x_{{name}}")
    id_pattern = derive_id_pattern(naming, kind)
    # FIX 3: Pass actual ID pattern for H02
    return (
        "Generate a quality gate for CEX kind '" + kind + "'.\n"
        "Pillar: " + meta["pillar"] + ", Description: " + meta["description"] + "\n"
        "Schema ID pattern (use this in H02): " + id_pattern + "\n\n"
        "Generate markdown body (NO frontmatter) with:\n"
        "## Definition\n"
        "(Table: metric, threshold, operator, scope)\n"
        "## HARD Gates\n"
        "(Table: ID | Check | Fail Condition -- 7-10 gates)\n"
        "CRITICAL: H02 MUST use this exact pattern from the schema: " + id_pattern + "\n"
        "H01: YAML frontmatter valid\n"
        "H02: ID matches pattern " + id_pattern + "\n"
        "H03: kind field matches '" + kind + "'\n"
        "Add 4-7 more HARD gates specific to " + kind + "\n"
        "## SOFT Scoring\n"
        "(Table: Dim | Dimension | Weight | Scoring Guide -- 8-11 dimensions summing to 1.00)\n"
        "## Actions\n"
        "(Table: Score | Action -- 4 tiers: GOLDEN >=9.5, PUBLISH >=8.0, REVIEW >=7.0, REJECT <7.0)\n"
        "## Bypass\n"
        "(Table: conditions, approver, audit trail)\n\n"
        "ASCII only. Under 80 lines."
    )


def build_output_template_prompt(kind: str, meta: dict[str, Any]) -> str:
    naming = meta.get("naming", "p00_x_{{name}}")
    id_pattern = derive_id_pattern(naming, kind)
    # FIX 5: Require schema-backed context, not bare placeholders
    return (
        "Generate an output template for CEX kind '" + kind + "'.\n"
        "Pillar: " + meta["pillar"] + ", Naming: " + naming + "\n\n"
        "RULES:\n"
        "1. Every placeholder MUST have a <!-- comment --> explaining what goes there.\n"
        "2. Include complete frontmatter with ALL required schema fields.\n"
        "3. Include at least one table or code block in the body.\n"
        "4. ID field must follow pattern: " + id_pattern + "\n"
        "5. quality field MUST be: null (never a number or string)\n\n"
        "Generate markdown body (NO frontmatter) with a YAML code block showing:\n"
        "- All required frontmatter fields with {{variable}} placeholders\n"
        "- Each placeholder followed by <!-- what to put here --> comment\n"
        "- Body sections with structured examples (tables, code blocks)\n\n"
        "ASCII only. Under 70 lines."
    )


def build_examples_prompt(kind: str, meta: dict[str, Any]) -> str:
    return (
        "Generate golden and anti-examples for CEX kind '" + kind + "'.\n"
        "Description: " + meta["description"] + "\n"
        "Boundary: " + meta["boundary"] + "\n\n"
        "Generate markdown body (NO frontmatter) with:\n"
        "## Golden Example\n"
        "(A complete, high-quality example of a " + kind + " artifact with frontmatter and body)\n"
        "Use REAL names: no 'ProviderA', 'SomeVendor', 'ExampleModel'. Use actual tools/vendors.\n"
        "## Anti-Example 1: {common mistake}\n"
        "(BAD example with ## Why it fails explanation)\n"
        "## Anti-Example 2: {another mistake}\n"
        "(Another BAD example with ## Why it fails explanation)\n\n"
        "ASCII only. Under 120 lines."
    )


def build_knowledge_card_prompt(kind: str, meta: dict[str, Any]) -> str:
    return (
        "Generate domain knowledge for building '" + kind + "' artifacts.\n"
        "Description: " + meta["description"] + "\n"
        "Boundary: " + meta["boundary"] + "\n\n"
        "Generate markdown body (NO frontmatter) with:\n"
        "## Domain Overview\n"
        "(2-3 paragraphs of industry context for " + kind + ")\n"
        "## Key Concepts\n"
        "(Table: Concept | Definition | Source -- 8-12 rows with REAL standards/papers)\n"
        "## Industry Standards\n"
        "(List relevant standards, frameworks, RFCs, or papers with actual names)\n"
        "## Common Patterns\n"
        "(4-6 numbered patterns with 1-line descriptions)\n"
        "## Pitfalls\n"
        "(4-5 common mistakes to avoid)\n\n"
        "Use REAL industry terminology and references. ASCII only. Under 90 lines."
    )


def build_architecture_prompt(kind: str, meta: dict[str, Any]) -> str:
    # FIX 6: Explicitly list 13 ISOs as components; forbid wrong-domain content
    iso_list = ", ".join(ISO_COMPONENT_NAMES)
    return (
        "Generate an architecture document for the " + kind + "-builder.\n"
        "Kind: " + kind + ", Pillar: " + meta["pillar"] + "\n\n"
        "CRITICAL RULES:\n"
        "1. Component Inventory MUST list the 13 builder ISOs as components:\n"
        "   " + iso_list + "\n"
        "2. Do NOT include generic business/tech components (no trading, no blockchain, no video conferencing).\n"
        "3. Architectural Position must describe " + kind + "'s role in the CEX pillar taxonomy.\n\n"
        "Generate markdown body (NO frontmatter) with:\n"
        "## Component Inventory\n"
        "(Table: ISO Name | Role | Pillar | Status -- list all 13 ISOs from the list above)\n"
        "## Dependencies\n"
        "(Table: From | To | Type -- 4-6 dependencies between ISOs or external tools)\n"
        "## Architectural Position\n"
        "(1 paragraph placing " + kind + " in the CEX pillar " + meta["pillar"] + " ecosystem)\n\n"
        "ASCII only. Under 60 lines."
    )


def build_collaboration_prompt(kind: str, meta: dict[str, Any]) -> str:
    return (
        "Generate a collaboration spec for " + kind + "-builder.\n"
        "Kind: " + kind + ", Boundary: " + meta["boundary"] + "\n\n"
        "Generate markdown body (NO frontmatter) with:\n"
        "## Crew Role\n"
        "(What this builder does in a team)\n"
        "## Receives From\n"
        "(Table: Builder | What | Format -- 3-4 rows)\n"
        "## Produces For\n"
        "(Table: Builder | What | Format -- 3-4 rows)\n"
        "## Boundary\n"
        "(What this builder does NOT do and who handles it instead)\n\n"
        "ASCII only. Under 45 lines."
    )


def build_config_prompt(kind: str, meta: dict[str, Any]) -> str:
    return (
        "Generate a config for " + kind + "-builder.\n"
        "Naming: " + meta.get("naming", "") + ", Max bytes: " + str(meta.get("max_bytes", 5120)) + ", Pillar: " + meta["pillar"] + "\n\n"
        "Generate markdown body (NO frontmatter) with:\n"
        "## Naming Convention\n"
        "(Pattern and examples)\n"
        "## Paths\n"
        "(Where artifacts are stored -- use actual CEX directory structure)\n"
        "## Limits\n"
        "(max_bytes, max_turns, effort level)\n"
        "## Hooks\n"
        "(pre_build, post_build, on_error, on_quality_fail -- all null for now)\n\n"
        "ASCII only. Under 40 lines."
    )


def build_memory_prompt(kind: str, meta: dict[str, Any]) -> str:
    return (
        "Generate a learning record (memory) for " + kind + "-builder.\n"
        "Description: " + meta["description"] + "\n"
        "Boundary: " + meta["boundary"] + "\n\n"
        "Generate markdown body (NO frontmatter) with:\n"
        "## Observation\n"
        "(2-3 sentences about common issues when building " + kind + " artifacts)\n"
        "## Pattern\n"
        "(2-3 sentences about what works well)\n"
        "## Evidence\n"
        "(1-2 sentences referencing reviewed artifacts)\n"
        "## Recommendations\n"
        "(4-5 bullet points)\n\n"
        "ASCII only. Under 40 lines."
    )


def build_tools_prompt(kind: str, meta: dict[str, Any]) -> str:
    return (
        "Generate a tools inventory for " + kind + "-builder.\n"
        "Kind: " + kind + "\n\n"
        "Generate markdown body (NO frontmatter) with:\n"
        "## Production Tools\n"
        "(Table: Tool | Purpose | When -- 4-6 CEX tools like cex_compile.py, cex_score.py, cex_retriever.py, cex_doctor.py)\n"
        "## Validation Tools\n"
        "(Table: Tool | Purpose | When -- 3-4 tools)\n"
        "## External References\n"
        "(2-3 relevant external tools or frameworks specific to " + kind + ")\n\n"
        "ASCII only. Under 40 lines."
    )


PROMPT_GENERATORS = [
    build_manifest_prompt,
    build_instruction_prompt,
    build_system_prompt_prompt,
    build_schema_prompt,
    build_quality_gate_prompt,
    build_output_template_prompt,
    build_examples_prompt,
    build_knowledge_card_prompt,
    build_architecture_prompt,
    build_collaboration_prompt,
    build_config_prompt,
    build_memory_prompt,
    build_tools_prompt,
]


# ============================================================
# Frontmatter generator (same logic as v1, verify BECOME on sp)
# ============================================================

def generate_frontmatter(
    iso_spec: tuple[str, str, str, str, str], kind: str, meta: dict[str, Any]
) -> str:
    """Generate YAML frontmatter for an ISO file."""
    fname_pattern, iso_kind, pillar_tpl, llm_func, purpose_tpl = iso_spec
    pillar = pillar_tpl.format(pillar=meta["pillar"])
    purpose = purpose_tpl.format(kind=kind)

    if iso_kind == "type_builder":
        iso_id = kind.replace("_", "-") + "-builder"
    elif iso_kind == "quality_gate":
        iso_id = meta["pillar"].lower() + "_qg_" + kind
    elif iso_kind == "system_prompt":
        iso_id = "p03_sp_" + kind + "_builder"
    elif iso_kind == "learning_record":
        iso_id = "p10_lr_" + kind + "_builder"
    else:
        iso_id = "bld_" + iso_kind + "_" + kind

    title_kind = kind.replace("_", " ").title()

    # FIX 2: quality is always null in frontmatter
    fm = (
        "---\n"
        "kind: " + iso_kind + "\n"
        "id: " + iso_id + "\n"
        "pillar: " + pillar + "\n"
        "llm_function: " + llm_func + "\n"   # FIX 1: llm_func from ISO_SPECS (BECOME for system_prompt)
        "purpose: " + purpose + "\n"
        "quality: null\n"                      # FIX 2: always null -- never self-score
        'title: "' + iso_kind.replace("_", " ").title() + " " + title_kind + '"\n'
        'version: "1.0.0"\n'
        "author: wave1_builder_gen_v2\n"
        "tags: [" + kind + ", builder, " + iso_kind + "]\n"
        'tldr: "' + purpose + '"\n'
        'domain: "' + kind + ' construction"\n'
        'created: "' + TODAY + '"\n'
        'updated: "' + TODAY + '"\n'
        "density_score: 0.85\n"
        "---"
    )
    return fm


# ============================================================
# FIX 7: Compile after save
# ============================================================

def compile_iso(fpath: str) -> bool:
    """Run cex_compile.py on a saved ISO to create matching .yaml."""
    try:
        result = subprocess.run(
            [sys.executable, COMPILE_TOOL, fpath],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            return True
        print("  [WARN] compile failed for " + fpath + ": " + result.stderr[:100])
        return False
    except Exception as e:
        print("  [WARN] compile error for " + fpath + ": " + str(e))
        return False


# ============================================================
# Core generate function (updated with validation + compile)
# ============================================================

def generate_iso(
    kind: str,
    meta: dict[str, Any],
    iso_idx: int,
    dry_run: bool = False,
    max_retries: int = 2,
) -> str | None:
    """
    Generate a single ISO file for a kind.
    v2 additions:
      - validate_iso_body() pre-commit check (retries up to max_retries)
      - compile_iso() post-save for FIX 7
    Returns: "OK" | "SKIP" | "DRY" | "REJECT" | None
    """
    iso_spec = ISO_SPECS[iso_idx]
    fname = iso_spec[0].format(k=kind)
    iso_type = iso_spec[1]
    builder_dir = os.path.join(BUILDERS_DIR, kind.replace("_", "-") + "-builder")
    fpath = os.path.join(builder_dir, fname)

    if os.path.exists(fpath) and not dry_run:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        if "> TODO:" not in content:
            return "SKIP"

    frontmatter = generate_frontmatter(iso_spec, kind, meta)
    prompt_fn = PROMPT_GENERATORS[iso_idx]
    prompt = prompt_fn(kind, meta)

    if dry_run:
        print("  [DRY] " + fname)
        return "DRY"

    body = None
    last_errors = []
    for attempt in range(1, max_retries + 2):   # 1 initial + max_retries retries
        raw = ollama_generate(prompt)
        if not raw:
            continue
        passed, errors = validate_iso_body(iso_type, kind, raw)
        if passed:
            body = raw
            break
        last_errors = errors
        print("  [RETRY " + str(attempt) + "] " + fname + " -- " + "; ".join(errors[:2]))

    if not body:
        if last_errors:
            print("  [REJECT] " + fname + " -- validation failed after " + str(max_retries + 1) + " attempts")
            print("           Errors: " + "; ".join(last_errors))
            return "REJECT"
        # No response from Ollama at all
        body = (
            "# " + iso_spec[1].replace("_", " ").title() + ": " + kind + "\n\n"
            "> TODO: Generate content for " + kind + " " + iso_spec[1] + "\n"
        )

    content = frontmatter + "\n\n" + body + "\n"
    os.makedirs(builder_dir, exist_ok=True)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    # FIX 7: Auto-compile after save
    if os.path.exists(COMPILE_TOOL):
        compile_iso(fpath)

    return "OK"


# ============================================================
# Validate-only mode: scan existing ISOs
# ============================================================

def validate_existing(kinds: list[str]) -> None:
    """Scan existing ISO files and report validation issues without regenerating."""
    print("[VALIDATE-ONLY] Scanning existing ISOs...\n")
    total = 0
    issues = 0
    for kind in kinds:
        builder_dir = os.path.join(BUILDERS_DIR, kind.replace("_", "-") + "-builder")
        if not os.path.isdir(builder_dir):
            continue
        for iso_idx, iso_spec in enumerate(ISO_SPECS):
            fname = iso_spec[0].format(k=kind)
            fpath = os.path.join(builder_dir, fname)
            if not os.path.exists(fpath):
                continue
            total += 1
            iso_type = iso_spec[1]
            with open(fpath, "r", encoding="utf-8") as f:
                raw = f.read()
            # Strip frontmatter for body validation
            parts = raw.split("---", 2)
            body = parts[2].strip() if len(parts) >= 3 else raw
            passed, errors = validate_iso_body(iso_type, kind, body)
            if not passed:
                issues += 1
                print("[ISSUE] " + fpath)
                for e in errors:
                    print("  - " + e)
    print("\n" + "="*60)
    print("Scanned: " + str(total) + " | Issues: " + str(issues))
    print("="*60)


# ============================================================
# Main
# ============================================================

def main() -> None:
    parser = argparse.ArgumentParser(description="CEX ISO generator v2 -- hardened with 7 fixes")
    parser.add_argument("--kind", help="Generate for specific kind only")
    parser.add_argument("--wave", default="1", help="Wave number: 1, 2, 3, or all")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--fix", action="store_true", help="Regenerate ISOs with TODO placeholders")
    parser.add_argument("--iso", type=int, help="Generate specific ISO index only (0-12)")
    parser.add_argument("--model", default=MODEL, help="Ollama model to use (default: qwen3:14b)")
    parser.add_argument("--max-retries", type=int, default=2, help="Max validation retries per ISO")
    parser.add_argument("--validate-only", action="store_true", help="Validate existing ISOs without regenerating")
    args = parser.parse_args()

    # Apply model override
    if args.model != MODEL:
        globals()["MODEL"] = args.model

    if args.kind:
        kinds = [args.kind]
    else:
        kinds = WAVE_MAP.get(args.wave, WAVE1_KINDS)
        print("[INFO] Wave " + args.wave + ": " + str(len(kinds)) + " kinds | model=" + MODEL)

    if args.validate_only:
        validate_existing(kinds)
        return

    total = 0
    created = 0
    skipped = 0
    rejected = 0
    failed = 0

    for kind in kinds:
        meta = load_kind_meta(kind)
        if not meta:
            print("[SKIP] " + kind + " not in kinds_meta.json")
            continue

        print("\n=== " + kind + " (" + meta["pillar"] + "/" + meta["llm_function"] + ") ===")

        iso_range = [args.iso] if args.iso is not None else range(13)

        for i in iso_range:
            total += 1
            fname = ISO_SPECS[i][0].format(k=kind)
            result = generate_iso(kind, meta, i, args.dry_run, args.max_retries)

            if result == "OK":
                created += 1
                print("  [OK] " + fname)
            elif result == "SKIP":
                skipped += 1
                print("  [SKIP] " + fname + " (exists)")
            elif result == "REJECT":
                rejected += 1
                # message already printed in generate_iso
            elif result == "DRY":
                pass
            else:
                failed += 1
                print("  [FAIL] " + fname)

    print("\n" + "="*60)
    print(
        "Total: " + str(total) +
        " | Created: " + str(created) +
        " | Skipped: " + str(skipped) +
        " | Rejected: " + str(rejected) +
        " | Failed: " + str(failed)
    )
    print("="*60)


if __name__ == "__main__":
    main()
