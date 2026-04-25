---
id: spec_n07_bootstrap_context
kind: context_doc
title: CEX Architecture -- Theory vs Practice Gap Analysis
version: 2.0.0
quality: 9.0
created: 2026-04-07
updated: 2026-04-07
purpose: Give a fresh N07 instance full understanding of what was designed vs what exists
density_score: null
domain: "system specification"
author: n07_admin
---

# CEX Architecture: Theory vs Practice

## What CEX Is

| Attribute | Value |
|-----------|-------|
| Purpose | Universal categorized dictionary for LLMs |
| Format | Structured artifacts (.md with YAML frontmatter) |
| Language | LLM-to-LLM (tables, lists, code blocks -- zero prose filler) |
| Test | Would Llama-7B understand this term without explanation? |
| Value | Context does the work, not the model's intelligence |

## Structural Layers

### Base Layer (read-only molds)

| Component | Path | Count | Purpose |
|-----------|------|-------|---------|
| Pillar schemas | P{01-12}_*/_schema.yaml | 12 | Structure contracts per category |
| Builder archetypes | archetypes/builders/{kind}-builder/ | 121 | 13 components per kind (instruction, examples, quality gate, output template, schema, etc) |
| Knowledge library | P01_knowledge/library/ | 270+ KCs | Domain knowledge in structured form |
| Templates | P{01-12}_*/templates/tpl_*.md | 67+ | Output patterns with {{variable}} slots |
| Kind registry | .cex/kinds_meta.json | 300 kinds | Every artifact type CEX understands |
| Rules | .claude/rules/*.md | 16 | Behavioral constraints (incl. technical-authority, input-transmutation) |
| Terminology | _docs/specs/spec_metaphor_dictionary.md | 40+ terms | Metaphor → Industry term translation |
| Rosetta Stone | P01_knowledge/library/domain/_reference/kc_terminology_rosetta_stone.md | 4 providers | Cross-provider canonical naming |

### Instance Layer (filled per agent)

| Component | Path | Count per nucleus | Purpose |
|-----------|------|-------------------|---------|
| Nucleus directory | N{01-06}_*/ | ~40 artifacts | Domain-specific filled molds |
| Subdirectories | agents/, prompts/, knowledge/, schemas/, output/, orchestration/, quality/, ... | 9-14 subdirs | Mirrors 12 pillar categories |
| Agent card manifest | N{0X}_*/agent_card_n0X.md | 1 | Self-discovery: what this agent has |

### Runtime Layer (assembled per task)

| Component | Path | Purpose |
|-----------|------|---------|
| Handoffs | .cex/runtime/handoffs/ | Task + artifact references |
| Decisions | .cex/runtime/decisions/ | User preferences (GDP) |
| Signals | .cex/runtime/signals/ | Completion signals |
| Plans | .cex/runtime/plans/ | Mission decomposition |
| PIDs | .cex/runtime/pids/ | Process tracking |

## Context Assembly (the theory)

### Phase 1: Boot (agent self-assembles)

When a nucleus starts, it should ALREADY know its capabilities:

| What loads | How | Status |
|-----------|-----|--------|
| CLAUDE.md | Claude Code reads automatically on startup | WIRED |
| agent_card_n0X.md | --append-system-prompt in boot .cmd | WIRED (Apr 7) |
| .claude/rules/n0X*.md | Claude Code reads automatically | WIRED |
| Sin identity | --append-system-prompt in boot .cmd | WIRED |
| Slash commands (/build, /mission, /status) | .claude/commands/ (native) | WIRED |

### Phase 2: Task (orchestrator assembles)

When N07 dispatches, the handoff should include everything the nucleus needs:

| What to include | How | Status |
|----------------|-----|--------|
| Task description | Handoff .md | WIRED |
| Builder path (13 components) | ## Relevant artifacts section | RULE EXISTS (dispatch-depth.md), NOT ENFORCED IN CODE |
| Relevant KCs | Listed in handoff | RULE EXISTS, NOT ENFORCED IN CODE |
| Output template | Listed in handoff | RULE EXISTS, NOT ENFORCED IN CODE |
| Brand config | Auto-loaded if /init was run | WIRED (brand_inject.py) |
| Decision manifest | Auto-included if GDP ran | WIRED (spawn_solo.ps1) |

### Phase 3: Pipeline (8F execution)

During task execution, the 8F pipeline enriches further:

| Step | What happens | Status |
|------|-------------|--------|
| F1 CONSTRAIN | Resolve kind, pillar from intent | WIRED (cex_8f_runner.py) |
| F2 BECOME | Load builder 13 components | WIRED (cex_skill_loader.py) |
| F3 INJECT | Assemble KCs + examples + memory + brand | CODE EXISTS but BROKEN -- needs LLM subprocess, should be pure Python |
| F4 REASON | Plan approach | WIRED |
| F5 CALL | Tool enrichment (retriever, query, providers) | WIRED |
| F6 PRODUCE | Generate with all context | WIRED (but depends on F3 working) |
| F7 GOVERN | Quality gate check | WIRED |
| F8 COLLABORATE | Save, compile, commit, signal | WIRED |

## Gaps Between Theory and Practice

### GAP G3: 22% of artifacts are prose-heavy (was 37%, improved)

| Metric | Value |
|--------|-------|
| Total artifacts | 3008 with frontmatter |
| Prose-heavy (>50% prose lines) | 654 (22%) |
| False positives | ~460 (bld_instruction_*.md = numbered lists, correct format) |
| True offenders | ~190 (config, output, KC files with narrative paragraphs) |
| Target | < 15% |
| Fix | Overnight evolve sweep on true offenders |
| Tool | cex_evolve.py agent <file> --target 9.0 |

### GAP G4: F3 INJECT is broken → N05 FIXING

| Metric | Value |
|--------|-------|
| Current F3 | Calls execute_prompt() which needs LLM subprocess |
| Problem | execute_prompt() can't reach LLM (no API key, nested pi fails) |
| Fix | Refactor F3 to use Python code only: cex_retriever + cex_prompt_layers |
| Impact | Pipeline works on ANY model, even offline/free |
| File | _tools/cex_8f_runner.py (1385 lines, F3 at ~line 200) |
| Status | **N05 dispatched 3x (killed twice by spawn_stop bug). Active.** |

### GAP G5: Template variables not systematic

| Metric | Value |
|--------|-------|
| Builder files with {{variables}} | 320 |
| Template files with {{variables}} | 67 |
| Templates WITHOUT {{BRAND_*}} slots | Unknown -- needs audit |
| Fix | Audit all bld_output_template_*.md, add missing {{BRAND_*}} and contextual slots |
| Status | **SCHEDULED for wave 3** |

### GAP G6: Stale docs → RESOLVED

| Doc | Action | Commit |
|-----|--------|--------|
| All stale runtime docs | Archived by N04 | `24d172da` |
| Status | **DONE** | 2026-04-07 |

### GAP G7: Handoff artifact selection not automated

| Metric | Value |
|--------|-------|
| Theory | N07 selects relevant builders, KCs, templates per task |
| Practice | N07 writes text descriptions, nucleus discovers on its own |
| Fix | Build a handoff composer that reads kinds_meta.json, finds builder path, finds KC, lists in handoff |
| Impact | Nucleus starts producing on turn 1 instead of spending 5 turns discovering files |
| Status | **SCHEDULED for wave 3** |

### GAP G8: Nucleus doesn't self-select context during task

| Metric | Value |
|--------|-------|
| Theory | Nucleus reads handoff references + autonomously pulls more relevant artifacts |
| Practice | Nucleus follows handoff literally, doesn't explore library |
| Fix | Nucleus boot prompt should instruct: "After reading handoff, scan P01_knowledge/library/ for relevant KCs before producing" |
| Impact | Richer context = better output |
| Status | **SCHEDULED for wave 4** |

### GAP G9 (NEW): Schemas were in Portuguese → RESOLVED

| Metric | Value |
|--------|-------|
| Problem | All 12 _schema.yaml descriptions in PT-BR |
| Impact | Fails Llama-7B test. Non-PT models lose context. |
| Fix | Translated all descriptions to English |
| Status | **DONE** (N03 + N01, commit in wave 2) |

### GAP G10 (NEW): 5 kinds with non-industry names → IN PROGRESS

| Old name | New name | Industry source | Status |
|----------|----------|----------------|--------|
| vector_store | vector_store | LangChain, LlamaIndex, Pinecone | 🔄 N03 renaming |
| knowledge_index | knowledge_index | LlamaIndex | 🔄 N03 renaming |
| director | supervisor | LangGraph | 🔄 N03 renaming |
| law | invariant | Software engineering | 🔄 N03 renaming |
| content_monetization | (move P04→P11) | Misplaced pillar | 🔄 N03 moving |

### GAP G11 (NEW): 4 missing kinds → IN PROGRESS

| Kind | Pillar | Industry source | Status |
|------|--------|----------------|--------|
| prompt_cache | P09 | Anthropic, Google | 🔄 N04 creating builders |
| citation | P01 | Anthropic, Google grounding | 🔄 N04 creating builders |
| context_window_config | P09 | All providers | 🔄 N04 creating builders |
| multi_modal_config | P09 | OpenAI, Anthropic, Google | 🔄 N04 creating builders |

### GAP G12 (NEW): 139 builder ISOs in Portuguese

| Metric | Value |
|--------|-------|
| Files with Portuguese | 139 / 1578 (9%) |
| Most common pattern | "Especialista em construir" (102 manifests) |
| Other patterns | Validar (92), Domina (69), Produzir (57) |
| Fix | Batch find-replace: PT patterns → EN equivalents |
| Status | **SCHEDULED for overnight run** |

### GAP G13 (CLOSED): satellite/agent_node renamed to agent_group

| Metric | Value |
|--------|-------|
| Files modified | 648 |
| Insertions | 2,078 |
| Deletions | 2,003 |
| Residual old terms | 0 |
| Fix | Renamed satellite + agent_node to `agent_group` |
| Status | **DONE** (2026-04-07, N03) |

### GAP G14 (NEW): 4 kinds missing llm_function

| Kind | Should be | Rationale |
|------|-----------|-----------|
| instruction (P03) | REASON | Instructions guide reasoning |
| hook_config (P04) | GOVERN | Lifecycle hook config = governance |
| director (P08) | REASON | Routing decisions (being renamed to supervisor) |
| effort_profile (P09) | CONSTRAIN | Effort estimation constrains scope |

### GAP G15 (NEW): spawn_stop -Nucleus bug

| Metric | Value |
|--------|-------|
| Problem | `bash _spawn/dispatch.sh stop n0X` kills ALL nuclei, not just the specified one |
| Impact | Killed N05 twice during this session, lost work |
| Fix | Fix `-Nucleus` filter in `_spawn/spawn_stop.ps1` |
| Workaround | Never use `stop n0X`. Let nuclei finish naturally or use `stop --all`. |
| Status | **SCHEDULED for N05 wave 3** |

## Runtime Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| N07 runtime | Claude Code (this process) | Orchestration, dispatch, monitoring |
| N01-N06 runtime | Claude Code (spawned via CMD) | Nucleus execution |
| Slash commands | .claude/commands/ (native) | /build, /mission, /status, /grid |
| Sub-agents | .claude/agents/ (native) | 125 builder sub-agents |
| Rules | .claude/rules/ (auto-loaded) | 8F, nucleus-specific, dispatch |
| Process management | _spawn/*.ps1 | Spawn, monitor, kill, grid layout |
| Quality | _tools/cex_doctor.py + cex_flywheel_audit.py | Health checks |
| Evolution | _tools/cex_evolve.py + boot/overnight_h1.cmd | Autonomous improvement |

## Spec Reference

| Spec | Path | What it defines |
|------|------|----------------|
| Context assembly | _docs/specs/spec_context_assembly.md | Two-phase loading, fractal structure |
| NotebookLM pipeline | _docs/specs/spec_notebooklm_pipeline.md | KC -> human content |
| Content factory | _docs/specs/spec_content_factory_v1.md | Multi-format content production |
| AutoResearch | _docs/specs/spec_autoresearch_assimilation.md | Karpathy pattern for CEX |

## Industry Validation (2026-04-07)

### 8F Pipeline = Universal LLM Agent Execution Cycle

| 8F | Industry pattern | Provider mapping |
|----|-----------------|-----------------|
| F1 CONSTRAIN | Schema validation | JSON Schema (OpenAI), Pydantic (LangChain), Guardrails |
| F2 BECOME | Agent initialization | System prompt (all), Agent config (CrewAI), Role (LangGraph) |
| F3 INJECT | RAG / context injection | RAG (all), Context stuffing, Few-shot injection |
| F4 REASON | Planning / chain-of-thought | Extended thinking (Anthropic), Reasoning (OpenAI o1/o3) |
| F5 CALL | Tool use / function calling | Tool use (Anthropic), Function calling (OpenAI/Google) |
| F6 PRODUCE | Generation / inference | Completion (all), Inference (MLOps) |
| F7 GOVERN | Evaluation / quality gating | Evals (OpenAI), LLM-as-judge, Quality gates (CI/CD) |
| F8 COLLABORATE | Artifact management / handoff | Handoff (Swarm), Observation (LangChain), Event (POSIX) |

### 12 Pillars = Superset of All Frameworks

| Framework | Pillars covered | Out of 12 |
|-----------|----------------|-----------|
| LangChain | P01, P02, P03, P04, P05, P06, P10, P12 | 8/12 |
| OpenAI Agents | P02, P03, P04, P05, P06, P07, P10, P11, P12 | 9/12 |
| Google A2A | P01, P02, P03, P04, P08, P12 | 6/12 |
| CrewAI | P02, P03, P04, P10, P12 | 5/12 |
| MCP | P01, P03, P04, P08 | 4/12 |
| **CEX** | **All** | **12/12** |

No framework covers P07 (Evals), P08 (Architecture), P09 (Config) as first-class citizens. CEX is the only system that treats all 12 as equal pillars.

### Sin System = Persona Engineering (validated)

Industry pattern: persona-driven behavioral differentiation through system prompt injection. The 7 sins create 7 orthogonal behavioral dimensions that make the same model (opus-4-6) produce meaningfully different outputs per nucleus. This is CEX's brand differentiator — keep as-is.

### 13 Builder ISOs = Agent Construction Pattern (validated)

Each ISO maps to a recognized industry concept: Agent Card, System Prompt, JSON Schema, Few-Shot Examples, Quality Gate, Output Schema, Architecture Doc, Context Document, Memory Config, Tool Config, Handoff Protocol.

## Memory (N07 persistent across sessions)

| File | Purpose |
|------|---------|
| cex_core_purpose.md | INVIOLABLE: universal taxonomy, zero jargon, LLM-to-LLM |
| roadmap_cex.md | 3 horizons, 10 principles, current state |
| operational_lessons.md | 7 hard-learned lessons (permanent) |
| terminology_standardization.md | Metaphor → industry term mapping + rename status |
| user_directive_technical_authority.md | User delegated tech lead to N07. Terms taught. |
| industry_terminology_audit.md | 300 kinds vs 4 providers |
| deep_architecture_audit.md | 8F, sins, pillars, ISOs, tools validated |
| project_cex_product_context.md | CEX ships as unconfigured instance |
| project_notebooklm_pipeline.md | NotebookLM integration |

## Infinite Bootstrap Loop (spec: spec_infinite_bootstrap_loop.md)

| Component | Status | Purpose |
|-----------|--------|---------|
| cex_mission_state.py | BUILDING | Checkpoint that survives N07 restart |
| cex_lock.py | BUILDING | Atomic file locking for shared resources |
| overnight_infinite.cmd | BUILDING | Auto-restart loop for N07 |
| --continuous mode | BUILDING | Continuous batching in mission_runner |
| pi subagent extension | BUILDING | 4 concurrent sub-agents per nucleus |
| 6 CEX agent definitions | BUILDING | scout, builder-iso, kc-writer, formatter, test-runner, researcher |
| Shared-file proposal pattern | BUILDING | Nuclei propose, N07 applies (git conflict prevention) |
| Task queue spec | BUILDING | Prioritized task queue for continuous dispatch |

Peak throughput: 24 parallel LLM streams, 864 artifacts/hour, full CEX from zero in ~3 hours.

## Terminology Reference (permanent)

| Source | Path |
|--------|------|
| Metaphor dictionary | _docs/specs/spec_metaphor_dictionary.md |
| Rosetta Stone | P01_knowledge/library/domain/_reference/kc_terminology_rosetta_stone.md |
| Anthropic canonical | P01_knowledge/library/domain/_reference/kc_terminology_anthropic_canonical.md |
| OpenAI canonical | P01_knowledge/library/domain/_reference/kc_terminology_openai_canonical.md |
| Google/MCP canonical | P01_knowledge/library/domain/_reference/kc_terminology_google_mcp_canonical.md |
| Decision manifest | .cex/runtime/decisions/decision_terminology_standardization.yaml |

## Cross-References

- **Pillar**:  (System)
- **Kind**: `context doc`
- **Artifact ID**: `spec_n07_bootstrap_context`
- **Tags**: []

## Integration Points

| Component | Role |
|-----------|------|
| Pillar  | System domain |
| Kind `context doc` | Artifact type |
| Pipeline | 8F (F1→F8) |
