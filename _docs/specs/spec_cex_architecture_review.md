---
id: spec_cex_architecture_review
kind: decision_record
pillar: P08
nucleus: N03
title: "CEX Architecture Review -- Internal Technical Reference"
version: 1.0.0
quality: 8.6
created: 2026-04-19
updated: 2026-04-19
author: n03_builder
tags: [architecture, review, internals, adoption, reference]
tldr: "Deep technical walkthrough of CEX internals: fractal layout, boot sequence, 8F pipeline, ISO loading, inter-nucleus signals, SDK layer, and end-to-end data flow."
density_score: 0.92
---

# CEX Architecture Review

Technical reference for senior AI engineers evaluating CEX for adoption.
Covers the seven subsystems that make CEX work: directory convention, boot sequence,
reasoning pipeline, taxonomy, inter-nucleus communication, SDK layer, and data flow.

---

## 1. Convention over Configuration (CoC)

### 1.1 The Fractal Structure

CEX enforces structure through directory naming. No registry files, no DI containers,
no config-driven wiring. The filesystem IS the configuration.

```
repo root
  |-- N00_genesis/         archetype (template nucleus)
  |-- N01_intelligence/    intelligence nucleus
  |-- N02_marketing/       marketing nucleus
  |-- N03_engineering/     engineering nucleus
  |-- N04_knowledge/       knowledge nucleus
  |-- N05_operations/      operations nucleus
  |-- N06_commercial/      commercial nucleus
  |-- N07_admin/           orchestrator nucleus
  |-- archetypes/builders/ builder ISOs (13 files per kind)
  |-- _tools/              Python toolchain (150 tools)
  |-- _spawn/              dispatch scripts (solo/grid/swarm)
  |-- cex_sdk/             runtime SDK (78 .py, 4504 lines)
  |-- boot/                PowerShell boot scripts (1 per nucleus + shared)
  |-- .cex/                runtime state (signals, handoffs, pids, decisions)
  |-- .claude/             Claude Code config (rules, commands, agents, skills)
```

### 1.2 Fractal Identity: Every Nucleus Mirrors N00

Each nucleus (N00-N07) contains the same 12 pillar subdirectories. This is not optional;
it is the structural invariant that enables tool discovery, compilation, and cross-nucleus
queries without configuration.

**Proof -- N03 vs N04 directory listing (actual):**

| N03_engineering/ | N04_knowledge/ | N00_genesis/ |
|-----------------|----------------|--------------|
| P01_knowledge/ | P01_knowledge/ | P01_knowledge/ |
| P02_model/ | P02_model/ | P02_model/ |
| P03_prompt/ | P03_prompt/ | P03_prompt/ |
| P04_tools/ | P04_tools/ | P04_tools/ |
| P05_output/ | P05_output/ | P05_output/ |
| P06_schema/ | P06_schema/ | P06_schema/ |
| P07_evals/ | P07_evals/ | P07_evals/ |
| P07_evaluation/ | P07_evaluation/ | -- |
| P08_architecture/ | P08_architecture/ | P08_architecture/ |
| P09_config/ | P09_config/ | P09_config/ |
| P10_memory/ | P10_memory/ | P10_memory/ |
| P11_feedback/ | P11_feedback/ | P11_feedback/ |
| P12_orchestration/ | P12_orchestration/ | P12_orchestration/ |
| compiled/ | compiled/ | compiled/ |
| rules/ | rules/ | rules/ |

All three are structurally identical. N00 is the archetype; N01-N07 are instances.

### 1.3 What the Layout Enforces

| Convention | Enforced By | Config File Needed |
|-----------|------------|-------------------|
| Artifact placement (pillar) | Directory name `P{01-12}_*` | None |
| Nucleus identity | Directory name `N{00-07}_*` | None |
| Builder discovery | `archetypes/builders/{kind}-builder/` | None |
| ISO file naming | `bld_{component}_{kind}.md` (13 patterns) | None |
| Schema loading | `P{xx}/_schema.yaml` per pillar | Schema file exists by convention |
| Signal routing | `.cex/runtime/signals/signal_{nucleus}_*.json` | None |
| Handoff discovery | `.cex/runtime/handoffs/{nucleus}_task.md` | None |
| Kind registry | `.cex/kinds_meta.json` | Single registry, not per-nucleus |

Tools like `cex_skill_loader.py` (line 247-274) discover builders by globbing
`archetypes/builders/{kind}-builder/bld_*.md` -- no manifest, no import map.

---

## 2. Boot Sequence

### 2.1 Boot Script Architecture

Every nucleus has a PowerShell boot script at `boot/n{0X}.ps1`. These are generated
by `cex_boot_gen.py` from two YAML sources:

| Source | Path | Purpose |
|--------|------|---------|
| Model config | `.cex/P09_config/nucleus_models.yaml` | CLI, model, context window |
| Sin config | `.cex/P09_config/nucleus_sins.yaml` | Sin name, personality text |

### 2.2 Boot Sequence (step by step)

**N07 Orchestrator (`boot/cex.ps1`, 109 lines):**

| Step | Line | Action |
|------|------|--------|
| 1 | 12 | Source `_shared/vt_enable.ps1` (ANSI terminal support) |
| 2 | 13 | Resolve `$cexRoot` from script location (worktree-agnostic) |
| 3 | 14-15 | Source `_shared/theme.ps1` (per-nucleus background color) |
| 4 | 20-29 | Read handoff file for mission name (window title) |
| 5 | 50 | Set window title: `N07 Sin | repo@branch [mission] -- BOOTING` |
| 6 | 77-81 | Set env: `CEX_NUCLEUS=N07`, `CEX_ROOT`, `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` |
| 7 | 84 | Source `load_dotenv.ps1` (secrets for MCP/providers) |
| 8 | 88-90 | Build system prompt with sin identity |
| 9 | 98-104 | Construct CLI args: `--model claude-opus-4-6`, `--append-system-prompt agent_card_n07.md` |
| 10 | 108 | Launch: `& claude @cliArgs` |

**N03 Builder (`boot/n03.ps1`, 108 lines):**

Same sequence with three differences:

| Difference | N07 (cex.ps1) | N03 (n03.ps1) |
|-----------|---------------|---------------|
| Model | `claude-opus-4-6` | `claude-sonnet-4-6` |
| System prompt | "You NEVER build directly. You dispatch." | "Every artifact must be worthy of your signature." |
| Initial message | "Ready. What do you need?" | "Read n03_task.md and execute. If no handoff, report ready." |
| Background color | Black | DarkBlue |
| MCP config | None | `.mcp-n03.json` |

### 2.3 CEX_NUCLEUS Routing

The `CEX_NUCLEUS` env var controls identity loading at the LLM level:

| Value | Behavior | Rules Loaded |
|-------|----------|-------------|
| `N07` | Orchestrator mode | `.claude/rules/n07-*.md` only |
| `N01`-`N06` | Builder mode | `N{0X}_*/rules/n{0X}-*.md` |
| Not set | Auto-detect from context | Reads CLAUDE.md, decides |

Key design: N07 never pre-loads other nuclei's rules. Each nucleus lazy-loads
its own identity on boot. This keeps the orchestrator context lean.

### 2.4 Handoff-Driven Startup

Nuclei never receive tasks via CLI arguments. The boot script reads from:
```
.cex/runtime/handoffs/{nucleus}_task.md
```

This avoids nested-quote escaping in CMD/PowerShell and enables multi-line
structured task descriptions with frontmatter.

---

## 3. 8F Pipeline

### 3.1 The 8 Functions

| Function | Name | Purpose | Builder ISO Loaded | Primary Tool |
|----------|------|---------|-------------------|-------------|
| F1 | CONSTRAIN | Resolve kind, pillar, schema | `bld_manifest_{kind}.md`, `bld_schema_{kind}.md` | `kinds_meta.json` |
| F2 | BECOME | Load builder identity | `bld_system_prompt_{kind}.md`, `bld_instruction_{kind}.md` | `cex_skill_loader.py` |
| F3 | INJECT | Assemble context | `bld_knowledge_card_{kind}.md`, `bld_memory_{kind}.md`, `bld_examples_{kind}.md` | `cex_retriever.py` |
| F3b | PERSIST | Declare knowledge to persist | -- | `cex_memory_update.py` |
| F3c | GROUND | Record source provenance | -- | -- |
| F4 | REASON | Plan approach | -- | GDP gate (`cex_gdp.py`) |
| F5 | CALL | Execute tools, fetch refs | `bld_tools_{kind}.md` | Various `_tools/*.py` |
| F6 | PRODUCE | Generate artifact | `bld_output_template_{kind}.md`, `bld_config_{kind}.md` | `chat()` |
| F7 | GOVERN | Quality gate | `bld_quality_gate_{kind}.md` | `cex_score.py` |
| F7b | LEARN | Capture feedback signals | -- | `cex_feedback.py` |
| F8 | COLLABORATE | Save, compile, commit, signal | `bld_collaboration_{kind}.md` | `signal_writer.py`, `cex_compile.py` |

### 3.2 8F-to-ISO Mapping in Code

`_tools/cex_skill_loader.py` (lines 62-91) defines the exact mapping:

```python
STAGE_ISO_MAP = {
    "manifest": ["manifest"],
    "constraint": ["schema", "manifest"],
    "system_prompt": ["system_prompt"],
    "instruction": ["instruction"],
    "memory": ["memory"],
    "knowledge_card": ["knowledge_card", "context"],
    "few_shot": ["examples"],
    "template": ["template", "output_template"],
    "quality_gate": ["quality", "scoring"],
    "tools": ["tools"],
    "collaboration": ["collaboration"],
    "architecture": ["architecture"],
    "config": ["config"],
}

F_STAGE_ALIASES = {
    "F1": ["manifest", "constraint"],
    "F2": ["system_prompt", "instruction"],
    "F3": ["memory", "knowledge_card", "few_shot"],
    "F6": ["instruction", "template", "format"],
    "F7": ["quality_gate", "scoring_rubric"],
}
```

This enables selective loading: `loader.load_builder("agent", stages=["F1", "F7"])`
loads only 4-5 ISOs instead of 13, saving ~60% context tokens.

### 3.3 How 8F Varies by Nucleus

The protocol is identical. The content differs:

| Nucleus | F1 CONSTRAIN resolves | F6 PRODUCE generates | F7 GOVERN validates |
|---------|----------------------|---------------------|-------------------|
| N01 | kind=knowledge_card, domain=research | Intelligence brief | Sources cited? Density >= 0.85? |
| N02 | kind=prompt_template, domain=copy | Ad variants, taglines | Brand voice? CTA present? |
| N03 | kind=agent/workflow/etc, domain=build | Structured artifact | Frontmatter? Quality >= 9.0? |
| N04 | kind=knowledge_card, domain=docs | KC, glossary, RAG config | Completeness? Cross-refs? |
| N05 | kind=cli_tool/benchmark, domain=ops | Code, tests, configs | Tests pass? ASCII-only? |
| N06 | kind=content_monetization, domain=sales | Pricing models, funnels | Margins positive? Tiers clear? |
| N07 | scope=mission, waves=N | Handoffs, wave plans | All handoffs valid? All nuclei bootable? |

### 3.4 Quality Gate (F7)

Three-layer scoring:

| Layer | Weight | Method | Tool |
|-------|--------|--------|------|
| Structural | 30% | Automated: frontmatter fields, section count, byte size | `cex_hooks.py` |
| Rubric | 30% | Dimension scoring (D1-D5) against builder's quality gate ISO | `cex_score.py` |
| Semantic | 40% | LLM evaluation (only when L1+L2 >= 8.5) | `cex_score.py --apply` |

Floor: 8.0 (reject). Target: 9.0. Self-scoring prohibited (`quality: null` in all produced artifacts).

---

## 4. Pillars x Kinds x Crews

### 4.1 The 12 Pillars

| Pillar | Domain | Schema Location | Example Kinds |
|--------|--------|----------------|---------------|
| P01 | Knowledge | `N00_genesis/P01_knowledge/_schema.yaml` | knowledge_card, chunk_strategy, embedding_config |
| P02 | Model | `N00_genesis/P02_model/_schema.yaml` | agent, model_provider, fallback_chain |
| P03 | Prompt | `N00_genesis/P03_prompt/_schema.yaml` | prompt_template, system_prompt, chain |
| P04 | Tools | `N00_genesis/P04_tools/_schema.yaml` | cli_tool, browser_tool, mcp_server |
| P05 | Output | `N00_genesis/P05_output/_schema.yaml` | landing_page, formatter, parser |
| P06 | Schema | `N00_genesis/P06_schema/_schema.yaml` | input_schema, type_def, interface |
| P07 | Evaluation | `N00_genesis/P07_evals/_schema.yaml` | quality_gate, scoring_rubric, benchmark |
| P08 | Architecture | `N00_genesis/P08_architecture/_schema.yaml` | agent_card, component_map, decision_record |
| P09 | Config | `N00_genesis/P09_config/_schema.yaml` | env_config, rate_limit_config, feature_flag |
| P10 | Memory | `N00_genesis/P10_memory/_schema.yaml` | entity_memory, knowledge_index, memory_summary |
| P11 | Feedback | `N00_genesis/P11_feedback/_schema.yaml` | bugloop, learning_record, guardrail |
| P12 | Orchestration | `N00_genesis/P12_orchestration/_schema.yaml` | workflow, dispatch_rule, schedule |

### 4.2 Kinds (293)

A kind is an atomic artifact type. Each kind has:

| Component | Location | Count |
|-----------|----------|-------|
| Registry entry | `.cex/kinds_meta.json` | 293 |
| Knowledge card | `N00_genesis/P01_knowledge/library/kind/kc_{kind}.md` | 424 |
| Builder (12 ISOs) | `archetypes/builders/{kind}-builder/` | 301 builders |
| Sub-agent | `.claude/agents/{kind}-builder.md` | 294 |

Kinds are the type system. A `knowledge_card` is not a `context_doc`. A `prompt_template`
is not a `system_prompt`. The taxonomy prevents synonyms and ensures machine-addressable artifacts.

### 4.3 Dispatch Modes

| Mode | Concurrency | Coherence | Use Case |
|------|------------|-----------|----------|
| **Solo** | 1 | N/A | Single artifact, single kind |
| **Crew** | Intra-crew (sequential/hierarchical/consensus) | High (handoffs between roles) | Multi-role package (launch kit, RFP) |
| **Grid** | Up to 6 parallel nuclei | Low (independent) | Multi-nucleus parallel production |
| **Grid-of-crews** | N crews in parallel | High within crew, parallel across | N simultaneous packages |
| **Swarm** | N builders of same kind | None (isolated worktrees) | Coverage/variant exploration |

### 4.4 Crew Primitives (WAVE8)

| Primitive | Kind | Pillar | Role |
|-----------|------|--------|------|
| `crew_template` | P12 | Recipe: roles table + process topology + handoff protocol |
| `role_assignment` | P02 | Binds role_name to agent_id with goal/backstory/tools |
| `capability_registry` | P08 | Index of all spawnable agents (282) |
| `nucleus_def` | P02 | Machine-readable nucleus identity (1 per nucleus) |
| `team_charter` | P12 | Mission contract: budget, deadline, quality gate |

Crew topologies: `sequential` (pipeline), `hierarchical` (manager-worker), `consensus` (parallel vote).

---

## 5. Inter-Nucleus Communication

### 5.1 Signal Protocol

`_tools/signal_writer.py` (55 lines) writes JSON signals to `.cex/runtime/signals/`.

**Signal schema:**

```json
{
  "nucleus": "n03",
  "status": "complete",
  "quality_score": 9.0,
  "mission": "BRAND_LAUNCH",
  "timestamp": "2026-04-19T12:00:00+00:00",
  "wave": 1
}
```

**Filename pattern:**
- Standard: `signal_{nucleus}_{YYYYMMDD_HHMMSS}.json`
- Mission-scoped: `signal_{nucleus}_{mission}_w{wave}_{YYYYMMDD_HHMMSS}.json`

**Validation (line 13-19):**
- Nucleus must be `n01`-`n07` or mission phase pattern `w\d+`
- Quality score must be 0-10 float
- Status must be lowercase alpha/underscore only

### 5.2 Handoff Files

N07 writes structured handoff files before dispatching:

| File | Purpose | Reader |
|------|---------|--------|
| `.cex/runtime/handoffs/{MISSION}_{nucleus}.md` | Mission-scoped task | Grid spawn |
| `.cex/runtime/handoffs/{nucleus}_task.md` | Boot task (also `n0X_task.md` root copy) | Boot script initial message |
| `.cex/runtime/decisions/decision_manifest.yaml` | GDP decisions (subjective choices) | All dispatched nuclei |

Handoffs contain YAML frontmatter (mission, nucleus, kind, pillar) plus structured markdown
body with context references, expected output, and artifact paths.

### 5.3 Dispatch Broker (`_spawn/dispatch.sh`)

`dispatch.sh` (244 lines) is a bash router that translates mode + arguments into
PowerShell spawn calls:

| Mode | Downstream Script | Process |
|------|------------------|---------|
| `solo` | `spawn_solo.ps1` | 1 window, 1 nucleus |
| `grid` | `spawn_grid.ps1` | 3x2 tiled windows, up to 6 nuclei |
| `swarm` | `spawn_swarm.sh` | N worktrees, N builders of same kind |
| `status` | `spawn_monitor.ps1` | Poll PIDs + signals |
| `stop` | `spawn_stop.ps1` | Session-aware process kill |

Multi-runtime variants: `grid-gemini`, `grid-codex`, `grid-ollama`, `grid-litellm`,
`solo-ollama`, `solo-codex`, `solo-gemini`, `solo-litellm`, `ollama` (headless),
`ollama-grid` (headless parallel).

### 5.4 Session-Aware PID Tracking

Multiple N07 orchestrators can run simultaneously. Each dispatch records a session ID:

```
{wrapper_pid} {nucleus} {cli} {session_id} {timestamp} {worker_pids}
```

- `stop` kills only the current session's nuclei (safe for multi-N07)
- `stop n03` kills that specific nucleus regardless of session
- `stop --all` kills everything (requires explicit flag)

PID file: `.cex/runtime/pids/spawn_pids.txt`
Session file: `.cex/runtime/pids/.my_session`

Session IDs are generated from timestamp (`s{epoch}`) and persist via the session file.

### 5.5 Process Tree Concern (Windows)

`Start-Process -PassThru` returns the PowerShell wrapper PID, not the LLM CLI PID.
The actual process tree is:

```
powershell.exe (wrapper -- returned by -PassThru)
  +-- boot/n0X.ps1
        +-- claude.exe (actual worker)
              +-- node.exe (MCP servers)
              +-- uvx, python (sub-tools)
```

`taskkill /F /PID <pid> /T` (tree-kill) is the only reliable cleanup method.
`Stop-Process` orphans child processes.

---

## 6. SDK Layer

### 6.1 Architecture

`cex_sdk/` (version 10.2.0, 78 .py files) is a Python runtime absorbed from
Agno (github.com/agno-agi/agno) and adapted to CEX's type system.

```
cex_sdk/
  |-- __init__.py         barrel exports: chat, Claude, Workflow, CEXAgent, etc.
  |-- models/
  |     |-- chat.py       thin synchronous LLM call (103 lines)
  |     |-- providers/
  |           |-- anthropic.py
  |           |-- openai.py
  |           |-- ollama.py
  |           |-- google.py
  |           |-- litellm.py
  |           |-- openrouter.py
  |-- agent/
  |     |-- cex_agent.py  8F-aware build layer (185 lines)
  |     |-- context_loader.py
  |     |-- signal_emitter.py
  |     |-- f8_pipeline.py
  |-- schema/             InputSchema, DataContract, Validator
  |-- workflow/           Workflow, Step, Parallel
  |-- tools/              Toolkit, cex_tool decorator
  |-- memory/             Memory management
  |-- knowledge/          KC loading
  |-- vectordb/           Embedding stores
  |-- guardrails/         PIIDetectionGuardrail, etc.
  |-- reasoning/          Chain-of-thought modules
  |-- eval/               Evaluation harness
  |-- tracing/            Observability
  |-- session/            Session persistence
```

### 6.2 Provider Abstraction (`chat()`)

`cex_sdk/models/chat.py` (lines 11-29) provides a single function:

```python
def chat(prompt, *, model="claude-sonnet-4-6", provider="auto",
         max_tokens=4096, system="", **kwargs) -> str:
```

Provider resolution (line 32-39):

| Model prefix | Resolved provider | Backend |
|-------------|-------------------|---------|
| `claude-*` | `anthropic` | `anthropic.Anthropic()` |
| `gpt-*`, `o1-*`, `o3-*` | `openai` | `openai.OpenAI()` |
| Everything else | `ollama` | HTTP POST to `localhost:11434` |

All three paths return plain `str`. No streaming, no async -- synchronous by design.
Environment variables: `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `OLLAMA_URL`.

### 6.3 CEXAgent (8F in Code)

`cex_sdk/agent/cex_agent.py` (lines 83-185) wraps `chat()` with the 8F pipeline:

| Method | 8F Stages | What It Does |
|--------|-----------|-------------|
| `__init__()` | -- | Set nucleus, kind, model, min_score; init ContextLoader + SignalEmitter |
| `build(intent)` | F1-F8 | Full pipeline: resolve kind -> load context -> build prompt -> call LLM -> validate -> signal |
| `validate(payload)` | F7 | Standalone quality gate |
| `signal(score)` | F8 | Standalone signal emission |

`build()` returns `BuildResult` (dataclass): artifact text, kind, pillar, score,
pass/fail, trace string, errors, signal path, context chars.

### 6.4 Relationship: SDK vs File-Based Architecture

| Concern | File-based (tools + builders) | SDK (`cex_sdk/`) |
|---------|------------------------------|-----------------|
| Builder ISOs | `archetypes/builders/` (markdown) | Not used -- SDK uses `ContextLoader` |
| LLM calls | CLI tools (`claude`, `gemini`, etc.) | `chat()` function |
| Signals | `_tools/signal_writer.py` | `SignalEmitter` class |
| Validation | `_tools/cex_score.py` | `Validator.for_kind()` |
| Orchestration | `_spawn/dispatch.sh` + boot scripts | Not covered (SDK is per-agent) |
| Intent resolution | `_tools/cex_intent_resolver.py` | `_guess_kind()` heuristic |

The SDK is the programmatic API for external consumers (`pip install -e .`).
The file-based architecture is the operational system for multi-nucleus dispatch.
They share the `.cex/runtime/signals/` directory and `kinds_meta.json` registry.

---

## 7. Data Flow (End-to-End)

### 7.1 Full Path: User Input to Compiled Artifact

```
User: "create an agent for customer support"
  |
  |  [1] Intent Resolution
  |  Tool: _tools/cex_intent_resolver.py (Python, 0 tokens)
  |  Fallback: N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md
  |  Output: {kind: "agent", pillar: "P02", nucleus: "N03", verb: "create"}
  |
  |  [2] GDP Check
  |  Tool: _tools/cex_gdp.py
  |  File: .cex/runtime/decisions/decision_manifest.yaml
  |  Question: Is this subjective? (agent persona = yes -> ask user)
  |
  |  [3] F1 CONSTRAIN
  |  File: .cex/kinds_meta.json (resolve kind -> pillar mapping)
  |  File: N00_genesis/P02_model/_schema.yaml (load schema)
  |
  |  [4] F2 BECOME
  |  Tool: _tools/cex_skill_loader.py
  |  Dir: archetypes/builders/agent-builder/ (12 ISOs)
  |  Files loaded:
  |    bld_manifest_agent.md      (identity, capabilities, triggers)
  |    bld_instruction_agent.md   (build instructions)
  |    bld_system_prompt_agent.md (LLM system prompt)
  |    bld_schema_agent.md        (frontmatter requirements)
  |    bld_output_template_agent.md (output structure)
  |    bld_examples_agent.md      (golden + anti-examples)
  |    bld_memory_agent.md        (cross-session memory)
  |    bld_tools_agent.md         (available tools)
  |    bld_quality_gate_agent.md  (F7 validation rules)
  |    bld_knowledge_card_agent.md (domain KC)
  |    bld_architecture_agent.md  (structural constraints)
  |    bld_collaboration_agent.md (crew role definition)
  |    bld_config_agent.md        (runtime config)
  |
  |  [5] F3 INJECT
  |  File: N00_genesis/P01_knowledge/library/kind/kc_agent.md
  |  Tool: _tools/cex_retriever.py (TF-IDF, 2184 docs, 12K vocab)
  |  Tool: _tools/cex_memory_select.py (relevant memory injection)
  |  File: .cex/brand/brand_config.yaml (brand voice, if bootstrapped)
  |
  |  [6] F4 REASON
  |  Plan: sections, approach (template-first if match >= 60%), density target
  |
  |  [7] F5 CALL
  |  Scan existing agents for reuse patterns
  |  Tool: _tools/cex_query.py (TF-IDF builder discovery)
  |
  |  [8] F6 PRODUCE
  |  Generate: complete artifact with YAML frontmatter + structured body
  |  Constraint: density >= 0.85, all required frontmatter fields present
  |
  |  [9] F7 GOVERN
  |  Tool: _tools/cex_score.py
  |  Gates: 7 HARD gates (reject if any fail) + 10 SOFT gates
  |  Score: 3-layer (structural 30% + rubric 30% + semantic 40%)
  |  If < 8.0: retry (max 2 retries, return to F6)
  |
  |  [10] F8 COLLABORATE
  |  Write: N03_engineering/P02_model/agent_customer_support.md
  |  Compile: python _tools/cex_compile.py <path> (md -> yaml)
  |  Commit: git add + git commit
  |  Signal: python -c "from _tools.signal_writer import write_signal;
  |          write_signal('n03', 'complete', 9.0)"
  |  Output: .cex/runtime/signals/signal_n03_20260419_120000.json
```

### 7.2 ISO Source Priority (Override Chain)

`cex_skill_loader.py` (lines 35-41) defines 5 priority levels:

| Priority | Source | Path | Purpose |
|----------|--------|------|---------|
| 0 (lowest) | genesis | `N00_genesis/archetypes/builders/{kind}-builder/` | Base templates |
| 1 | shared | `archetypes/builders/_shared/skill_*.md` | Cross-builder skills |
| 2 | builder | `archetypes/builders/{kind}-builder/bld_*.md` | Kind-specific (primary) |
| 3 | nucleus | `N{xx}_*/builders/{kind}-builder/bld_*.md` | Nucleus-specific overrides |
| 4 (highest) | brand | `.cex/brand/overrides/{kind}-builder/bld_*.md` | Brand customization |

Higher priority overrides lower. Deduplication by canonical path prevents double-loading.

### 7.3 Multi-Runtime Dispatch Path

```
N07 writes handoff -> .cex/runtime/handoffs/MISSION_n03.md
N07 copies to      -> n03_task.md (repo root, boot scripts read this)
N07 calls          -> bash _spawn/dispatch.sh solo n03
dispatch.sh        -> powershell spawn_solo.ps1 -nucleus n03
spawn_solo.ps1     -> Start-Process boot/n03.ps1
boot/n03.ps1       -> & claude --model claude-sonnet-4-6 ...
claude (N03)       -> reads n03_task.md -> executes 8F -> commits -> signals
N07 detects        -> git log --since + ls .cex/runtime/signals/
N07 consolidates   -> verify deliverables, kill process, archive signal
```

For alternative runtimes, `dispatch.sh` substitutes the spawn mode:

| dispatch.sh mode | Boot script suffix | CLI binary |
|------------------|--------------------|-----------|
| `solo` / `grid` | `n0X.ps1` | `claude` |
| `solo-gemini` / `grid-gemini` | `n0X_gemini.ps1` | `gemini` |
| `solo-codex` / `grid-codex` | `n0X_codex.ps1` | `codex` |
| `solo-ollama` / `grid-ollama` | `n0X_ollama.ps1` | `ollama_nucleus.py` |
| `solo-litellm` / `grid-litellm` | `n0X_litellm.ps1` | LiteLLM proxy |
| `ollama` (headless) | -- | `cex_8f_runner.py --execute` |

### 7.4 Compilation Pipeline

After artifact creation (F8), `cex_compile.py` converts markdown to YAML:

```
Source: N03_engineering/P02_model/agent_customer_support.md
Output: N03_engineering/compiled/agent_customer_support.yaml
```

Compiled YAML is machine-queryable, enabling cross-artifact indexing by
`cex_retriever.py` (2184 docs, 12K vocab TF-IDF index).

---

## Appendix A: Key File Reference

| File | Lines | Purpose |
|------|-------|---------|
| `CLAUDE.md` | 283 | Top-level system prompt, pointers table, commands |
| `.claude/rules/8f-reasoning.md` | 238 | 8F protocol specification |
| `.claude/rules/composable-crew.md` | 140 | Crew composition protocol |
| `.claude/rules/n07-orchestrator.md` | ~130 | Orchestrator rules |
| `.claude/rules/guided-decisions.md` | ~90 | GDP protocol |
| `boot/cex.ps1` | 109 | N07 boot script |
| `boot/n03.ps1` | 108 | N03 boot script |
| `_tools/cex_skill_loader.py` | 427 | ISO loader with 5-source priority |
| `_tools/signal_writer.py` | 55 | Signal protocol |
| `_spawn/dispatch.sh` | 244 | Dispatch broker (14 modes) |
| `cex_sdk/__init__.py` | 43 | SDK barrel exports |
| `cex_sdk/models/chat.py` | 103 | Provider-agnostic LLM call |
| `cex_sdk/agent/cex_agent.py` | 185 | 8F pipeline in code |
| `.cex/kinds_meta.json` | -- | 293 kind registry |
| `archetypes/builders/agent-builder/` | 12 files | Reference builder (12 ISOs) |

## Appendix B: System Counts (as of 2026-04-19)

| Metric | Count |
|--------|-------|
| Kinds | 293 |
| Builders | 295 |
| ISOs | 3835 |
| Pillars | 12 |
| Nuclei | 8 (N00-N07) |
| Tools | 158 |
| Sub-agents | 259 |
| Knowledge cards | 424 |
| SDK Python files | 78 |
| SDK lines | 4504 |
| Runtimes | 4 (Claude, Codex, Gemini, Ollama) |
| Dispatch modes | 14 |
