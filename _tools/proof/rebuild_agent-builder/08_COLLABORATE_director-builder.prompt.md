# CEX Crew Runner -- Builder Execution
**Builder**: `director-builder`
**Function**: COLLABORATE
**Intent**: reconstroi agent-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:20.363810

## Intent Context
- **Verb**: reconstroi
- **Object**: agent-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_director.md
---
id: satellite-spec-builder
kind: type_builder
pillar: P08
parent: null
domain: satellite_spec
llm_function: BECOME
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: EDISON
tags: [kind-builder, satellite-spec, P08, specialist, architecture]
---

# satellite-spec-builder
## Identity
Especialista em construir satellite_specs — especificacoes completas de satelites autonomos.
Sabe tudo sobre arquitetura de satelites: roles, modelos LLM, MCPs, boot sequences,
constraints, dispatch rules, scaling, e a fronteira entre satellite_spec (P08, satelite inteiro),
agent (P02, agente individual), e boot_config (P02, por provider).
## Capabilities
- Especificar satelites com role, model, MCPs e domain completos
- Produzir satellite_spec artifacts com frontmatter completo (24+ campos)
- Definir boot sequences, constraints, e dispatch rules
- Mapear dependencias, scaling rules, e monitoring
- Validar artifact contra quality gates (10 HARD + 10 SOFT)
- Documentar tool availability e MCP server configurations
## Routing
keywords: [satellite, spec, architecture, role, model, mcp, boot, dispatch, scaling, monitoring]
triggers: "define a new satellite", "spec this satellite", "document satellite architecture"
## Crew Role
In a crew, I handle SATELLITE ARCHITECTURE SPECIFICATION.
I answer: "what is this satellite's role, model, tools, and constraints?"
I do NOT handle: agent identity (P02 agent), boot configuration per provider (P02 boot_config), pattern documentation (P08 pattern).

### bld_instruction_director.md
---
id: p03_ins_satellite_spec_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Satellite Spec Builder Instructions
target: satellite-spec-builder agent
phases_count: 4
prerequisites:
  - Satellite name is defined (non-empty string, kebab-case)
  - Primary domain or responsibility is stated
  - At least one tool or MCP server is identified
  - Target LLM model family is known (e.g. opus, sonnet, haiku)
validation_method: checklist
domain: satellite_spec
quality: null
tags: [instruction, satellite-spec, architecture, P08]
idempotent: true
atomic: false
rollback: Delete generated satellite_spec file and restart from Phase 1
dependencies: []
logging: true
tldr: Build a complete satellite_spec covering role, model, MCPs, boot sequence, constraints, dispatch rules, and scaling.
density_score: 0.91
---

## Context
The satellite-spec-builder produces `satellite_spec` artifacts — complete architectural
specifications for an autonomous agent satellite. A satellite_spec defines everything needed
to instantiate, operate, and monitor a satellite: its role, model, MCP servers, boot sequence,
constraints, dispatch rules, and scaling configuration.
**Input contract**:
- `{{satellite_name}}`: kebab-case identifier (e.g. `research-sat`, `build-sat`)
- `{{domain}}`: primary operational domain (e.g. `web_research`, `code_generation`)
- `{{model}}`: LLM model identifier (e.g. `claude-opus-4`, `claude-sonnet-4`)
- `{{tools_list}}`: comma-separated list of MCP servers or built-in tools
- `{{constraints_raw}}`: free-text description of operational boundaries
**Output contract**: A single `satellite_spec` YAML file with 24+ frontmatter fields,
a narrative identity section, and structured subsections for boot sequence, dispatch rules,
constraints, and monitoring.
**Boundaries**:
- Handles full satellite architecture only.
- Individual agent identity belongs in a separate agent artifact.
- Per-provider boot configuration belongs in a boot_config artifact.
- Reusable operation patterns belong in pattern artifacts.
## Phases
### Phase 1: Analyze Role and Boundary
**Primary action**: Define the satellite's operational role and establish what it does
versus what it explicitly does not do.
```
INPUT: satellite_name, domain, constraints_raw
1. Express the satellite's single primary function:
   role_statement = "{{satellite_name}} is responsible for [ONE THING]"
   Reject vague roles like "general purpose" or "multi-domain"
2. Map the NOT-domain boundary:
   for each adjacent domain in [research, build, execute, monitor, orchestrate, store]:
     if domain != satellite's primary domain:
       add to NOT_HANDLES list with brief reason
   Minimum 2 entries required.
3. Determine LLM function type:
   if satellite makes decisions     -> BECOME
   if satellite calls external tools -> CALL
   if satellite coordinates others  -> COLLABORATE
   if satellite injects context     -> INJECT
4. Extract capability_keywords (5-10 terms) from domain description.
OUTPUT: role_statement, not_handles[], llm_function, capability_keywords[]
```
Verification: `role_statement` is one sentence. `not_handles` has >= 2 entries.
### Phase 2: Specify Model and Tools
**Primary action**: Select and document the model configuration and MCP server bindings.
```
INPUT: model, tools_list, role_statement
1. Model specification:
   model_config = {
     id: {{model}},
     context_window: lookup by family (opus=200k, sonnet=200k, haiku=200k),
     temperature: 0.3 for deterministic tasks | 0.7 for creative tasks,
     max_tokens: sized to expected output
   }
2. MCP server binding for each tool in tools_list:
   mcp_entry = {
     name: tool_name,
     transport: "stdio" | "http",
     required: true | false,
     fallback: null | alternative_tool
   }
3. Boot sequence (ordered list):
   boot_steps = [
     "load system prompt",
     "initialize MCP connections",
     "verify tool availability",
     "load domain context",
     "ready"
   ]
   Add satellite-specific steps between generic ones.
   Assign estimated duration in seconds to each step.
4. boot_time_seconds = sum(step durations)
OUTPUT: model_config{}, mcp_bindings[], boot_sequence[], boot_time_seconds
```
Verification: each MCP entry has `transport` and `required` fields.
`boot_sequence` has >= 4 steps.
### Phase 3: Define Dispatch and Constraints
**Primary action**: Specify how the satellite receives work, what it accepts or rejects,
and its operational limits.
```
INPUT: constraints_raw, capability_keywords[], role_statement
1. Dispatch rules:
   dispatch = {
     triggers: [keywords that route tasks here],  # >= 3 required
     input_format: "handoff_file" | "inline_prompt" | "both",
     max_prompt_chars: 200 if inline else null,
     priority: "normal" | "high" | "low"
   }
2. Constraint extraction from constraints_raw:
   hard_constraints = []   # things the satellite MUST NEVER do
   soft_constraints = []   # things the satellite SHOULD prefer
   for each sentence in constraints_raw:
     if NEVER/MUST NOT/FORBIDDEN -> hard_constraint
     if PREFER/AVOID/MINIMIZE    -> soft_constraint
3. Scaling configuration:
   scaling = {
     max_parallel_instances: 1 | 2 | 3,
     shared_resources: [resources that conflict if parallel],
     cooldown_seconds: wait time between sequential runs
   }
4. Monitoring spec:
   monitoring = {
     signal_on_complete: true,
     signal_on_error: true,
     heartbeat_interval_seconds: null | integer,
     log_level: "info" | "debug" | "error"
   }
OUTPUT: dispatch{}, hard_constraints[], soft_constraints[], scaling{}, monitoring{}
```
Verification: `dispatch.triggers` has >= 3 keywords. `hard_constraints` is non-empty.
### Phase 4: Assemble and Validate Artifact
**Primary action**: Combine all phase outputs into the final satellite_spec YAML and run
quality gates.
```
INPUT: all outputs from Phases 1-3
1. Assemble frontmatter with 24+ required fields (id, kind, pillar, version,
   created, domain, model, llm_function, boot_time_seconds, context_window,

### bld_knowledge_card_director.md
---
kind: knowledge_card
id: bld_knowledge_card_director
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for satellite_spec production — atomic searchable facts
sources: satellite-spec-builder MANIFEST.md + SCHEMA.md, microservices architecture, multi-agent systems
---

# Domain Knowledge: satellite_spec
## Executive Summary
Satellite specs define autonomous processing units in multi-agent architectures — each spec declares one satellite's domain, LLM model, MCP servers, boot sequence, constraints, and dispatch keywords. Each satellite owns ONE domain with no cross-domain responsibilities. They differ from agents (individual entities inside a satellite), boot configs (how to start a provider), patterns (abstract reusable solutions), and spawn configs (runtime launch parameters) by being the complete architectural specification of what a satellite IS and what it does.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P08 (architecture) |
| Kind | `satellite_spec` (exact literal) |
| ID pattern | `p08_sat_{slug}` |
| Required frontmatter | 24+ fields |
| Quality gates | 10 HARD + 10 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Key fields | role, model, mcps, domain, boot_sequence, dispatch_keywords |
| Scaling limit | Max 3 concurrent + orchestrator (BSOD at >4) |
## Patterns
| Pattern | Application |
|---------|-------------|
| Single domain ownership | Each satellite owns ONE domain; no cross-domain responsibilities |
| Model-to-task matching | opus for reasoning-heavy; sonnet for speed/volume |
| MCP as tool interface | MCP servers are the satellite's external tool access |
| Ordered boot sequence | Idempotent, ordered initialization steps |
| Constraints as boundaries | Define what satellite CANNOT do, not aspirations |
| Dispatch keywords as contract | Routing contract with orchestrator; concrete nouns/verbs |
| Explicit dependencies | No hidden couplings between satellites |
| Signal-based monitoring | Signal on complete/failure enables autonomous recovery |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Cross-domain responsibilities | Violates single-domain principle; creates coupling |
| Missing boot sequence | Cannot reliably start or recover the satellite |
| No dispatch keywords | Orchestrator cannot route tasks to this satellite |
| Constraints section empty | No boundaries = scope creep inevitable |
| > 4 concurrent satellites | Resource exhaustion; system instability |
| Hidden dependencies | Undeclared coupling causes cascade failures |
| No monitoring/signal config | Cannot detect completion or failure |
## Application
1. Define satellite role and domain (ONE domain only)
2. Select LLM model matching task complexity
3. List MCP servers with config file path
4. Define ordered, idempotent boot sequence
5. Set constraints (what satellite CANNOT do)
6. Define dispatch keywords (routing contract)
7. Specify scaling limits and monitoring config
8. Document dependencies explicitly
9. Validate: 10 HARD + 10 SOFT gates, body <= 4096 bytes
## References
- satellite-spec-builder SCHEMA.md v1.0.0
- Newman, Sam. Building Microservices (2015)
- Wooldridge, Michael. Introduction to MultiAgent Systems (2009)
- Kubernetes Pod Specification (resource limits, health checks)

### bld_quality_gate_director.md
---
id: p11_qg_satellite-spec
kind: quality_gate
pillar: P11
title: "Gate: Satellite Spec"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: EDISON
domain: satellite_spec
quality: null
density_score: 0.85
tags:
  - quality-gate
  - satellite-spec
  - autonomous-agent
  - p11
tldr: "Gates ensuring satellite spec files define a fully autonomous agent with role, model, tools, boot sequence, and dispatch rules."
---

## Definition
A satellite spec describes a fully autonomous agent: its identity, the LLM it runs on, the external tools it can call, how it starts up, how it receives work, and how it shuts down. A spec passes this gate when any operator could launch and operate the satellite from the document alone, without consulting the author.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`satellite-spec-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `satellite_spec` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains a **Role** definition (one-paragraph description of what the satellite does and does not do) | Without role boundary, operators cannot determine if a task is in scope |
| H08 | Spec contains a **Model** assignment: LLM provider and model name (e.g., `provider: anthropic`, `model: claude-opus-4-6`) | Satellite cannot be launched without knowing which model to request |
| H09 | Spec contains an **MCP server list** (may be empty list `[]`, but must be explicitly declared) | Tool availability determines what the satellite can execute |
| H10 | Spec contains a **Boot sequence**: ordered steps to bring the satellite from cold to ready state | Without boot sequence, launch is non-reproducible |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Constraints documented (what the satellite must never do) | 1.0 | No constraints listed | Partial list, vague | Explicit NEVER list with rationale per constraint |
| 3 | Dispatch rules present (how the satellite receives and accepts tasks) | 1.0 | No dispatch described | Dispatch channel named, no detail | Full dispatch protocol: channel, format, acceptance criteria |
| 4 | Scaling rules defined (concurrency limits, queue behavior, overflow handling) | 0.5 | No mention | Single-instance only documented | Concurrency limits, queue behavior, and overflow all defined |
| 5 | Monitoring configuration (signals emitted, health check, alerting thresholds) | 1.0 | No monitoring | Logs only | Structured signals + health check + alerting thresholds |
| 6 | Tags include `satellite-spec` | 0.5 | Missing | Present but misspelled | Exactly `satellite-spec` in tags list |
| 7 | Domain boundaries explicit (data and systems the satellite may and may not access) | 1.0 | No boundaries | Implicit in examples | Explicit allowed-access list and forbidden-access list |
| 8 | Tool availability listed with version or source per MCP server | 1.0 | None listed | Names only | Names + source/version + fallback if unavailable |

### bld_schema_director.md
---
kind: schema
id: bld_schema_director
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for satellite_spec
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: satellite_spec
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p08_sat_{name}) | YES | - | Namespace compliance |
| kind | literal "satellite_spec" | YES | - | Type integrity |
| pillar | literal "P08" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Satellite name (uppercase) |
| role | string | YES | - | Primary function description |
| model | string | YES | - | LLM model used (opus, sonnet, haiku) |
| mcps | list[string] | YES | - | MCP servers available |
| domain_area | string | YES | - | Domain this satellite covers |
| boot_sequence | list[string] | REC | [] | Ordered boot steps |
| constraints | list[string] | REC | [] | Operational limitations |
| dispatch_keywords | list[string] | REC | [] | Keywords that route tasks here |
| tools | list[string] | REC | [] | Tools available to this satellite |
| dependencies | list[string] | REC | [] | Other satellites/services required |
| scaling | object or null | REC | null | Scaling rules (max_concurrent, timeout) |
| monitoring | object or null | REC | null | Health check and alerting config |
| runtime | string | REC | "claude" | Runtime engine (claude, codex) |
| mcp_config_file | string or null | REC | null | Path to .mcp-{sat}.json |
| flags | list[string] | REC | [] | CLI flags for spawn |
| domain | string | YES | - | Domain this artifact belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "satellite" |
| tldr | string <= 160ch | YES | - | Dense summary |
## Complex Objects
```yaml
scaling:
  max_concurrent: integer    # max parallel instances
  timeout_minutes: integer   # max execution time
  memory_limit_mb: integer   # RAM ceiling
monitoring:
  health_check: string       # command or URL
  signal_on_complete: boolean # emit signal when done
  alert_on_failure: boolean  # notify on error
```
## ID Pattern
Regex: `^p08_sat_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Role` — what the satellite does and its primary function
2. `## Model & MCPs` — LLM model details and MCP server specs
3. `## Boot Sequence` — ordered initialization steps
4. `## Dispatch` — keywords and routing rules
5. `## Constraints` — operational limits and prohibitions
6. `## Dependencies` — external services and sibling satellites
7. `## Scaling & Monitoring` — concurrency, timeouts, health checks
## Constraints
- max_bytes: 4096 (body only)
- naming: p08_sat_{name_lower}.yaml
- machine_format: yaml
- id == filename stem
- name MUST be non-empty (uppercase convention)
- role MUST describe primary function
- model MUST be a valid LLM identifier
- mcps MUST list available MCP servers (empty list if none)
- quality: null always

### bld_examples_director.md
---
kind: examples
id: bld_examples_director
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of satellite_spec artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: satellite-spec-builder
## Golden Example
INPUT: "Especifica o satelite researcher para pesquisa de mercado"
OUTPUT:
```yaml
id: p08_sat_shaka
kind: satellite_spec
pillar: P08
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
name: "researcher"
role: "Research satellite — market intelligence, competitor analysis, web scraping"
model: "sonnet"
mcps: [firecrawl, brain]
domain_area: "research"
boot_sequence:
  - "Load prime_researcher.md"
  - "Initialize firecrawl MCP"
  - "Initialize brain MCP"
  - "Check dispatch queue"
constraints:
  - "Read-only: never modify production data"
  - "Max 10 credits per research session (firecrawl budget)"
  - "No code generation — delegate to builder"
  - "Results must include source URLs"
dispatch_keywords: [pesquisar, mercado, concorrente, scrape, analise, research]
tools: [firecrawl_scrape, firecrawl_extract, brain_query, web_search]
dependencies: [brain_mcp, firecrawl_api]
scaling:
  max_concurrent: 1
  timeout_minutes: 30
  memory_limit_mb: 2048
monitoring:
  health_check: "brain_query('shaka status')"
  signal_on_complete: true
  alert_on_failure: true
runtime: "claude"
mcp_config_file: ".mcp-shaka.json"
flags: ["--no-chrome", "-p"]
domain: "research-intelligence"
quality: null
tags: [satellite, research, shaka, market-intelligence, scraping]
tldr: "researcher satellite spec — research domain, sonnet model, firecrawl+brain MCPs, market intelligence."
```
## Role
Research satellite focused on market intelligence, competitor analysis, and web data extraction.
Primary function: gather, structure, and deliver research findings as knowledge cards or reports.
Does not generate code or modify production systems.
## Model & MCPs
- **Model**: sonnet (balanced cost/quality for research tasks)
- **firecrawl**: web scraping and structured data extraction (3000 credits/month)
- **brain**: knowledge search and deduplication check
## Boot Sequence
1. Load prime_researcher.md (identity, constraints, dispatch protocol)
2. Initialize firecrawl MCP (verify API key, check credit balance)
3. Initialize brain MCP (verify Ollama running, index freshness)
4. Check dispatch queue (.claude/handoffs/shaka_*.md)
## Dispatch
Keywords: pesquisar, mercado, concorrente, scrape, analise, research
Routing: orchestrator matches keywords against dispatch_keywords list.
Priority: research tasks routed to researcher before any other satellite.
## Constraints
- Read-only: never modify production data or commit to main
- Budget: max 10 firecrawl credits per research session
- Boundary: no code generation (delegate to builder)
- Quality: all findings must include source URLs
## Dependencies
- brain MCP server (Ollama + FAISS index)
- firecrawl API ($19/month tier)
- No sibling satellite dependencies (fully independent)
## Scaling & Monitoring
- Max 1 concurrent instance (avoid firecrawl rate limits)
- 30-minute timeout per session
- Signal on complete: emits p12_sig_shaka_complete.json
- Alert on failure: logs error + notifies orchestrator
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p08_sat_ pattern (H02 pass)
- kind: satellite_spec (H04 pass)
- 26 frontmatter fields present (H06 pass)
- name non-empty "researcher" (H07 pass)
- model is valid "sonnet" (H08 pass)
- mcps is list (H09 pass)
- role non-empty (H10 pass)
- YAML parses cleanly (H01 pass)
- id == filename stem (H03 pass)
- tldr <= 160 chars (S01 pass)
- tags list len >= 3 (S02 pass)
- All 7 body sections present (S03-S09 pass)
## Anti-Example
INPUT: "Define researcher satellite"
BAD OUTPUT:
```yaml
id: shaka_satellite
kind: satellite
pillar: Architecture
name: Shaka
model: Claude Sonnet 4
mcps: firecrawl
role: This satellite is responsible for doing various types of research including market research, competitor analysis, web scraping, and many other research-related activities
quality: 9.0

### bld_config_director.md
---
kind: config
id: bld_config_director
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: satellite_spec Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p08_sat_{name_lower}.yaml` | `p08_sat_shaka.yaml` |
| Builder directory | kebab-case | `satellite-spec-builder/` |
| Frontmatter fields | snake_case | `domain_area`, `boot_sequence` |
| Satellite names | UPPERCASE in name field | `researcher`, `builder`, `marketer` |
| Name slugs | lowercase in id | `shaka`, `edison`, `lily` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P08_architecture/examples/p08_sat_{name_lower}.yaml`
- Compiled: `cex/P08_architecture/compiled/p08_sat_{name_lower}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total: ~6000 bytes including frontmatter
- Density: >= 0.80
## Model Enum
| Model | When to use |
|-------|-------------|
| opus | Complex reasoning, code generation, architecture |
| sonnet | Balanced cost/quality, research, marketing |
| haiku | Simple tasks, classification, formatting |
## MCP Convention
- List all MCPs even if empty: `mcps: []`
- Use short names: `brain`, `firecrawl`, `railway`, `pg`
- MCP config path follows: `.mcp-{sat_lower}.json`
## Scaling Defaults
| Field | Default | Max |
|-------|---------|-----|
| max_concurrent | 1 | 3 (BSOD prevention) |
| timeout_minutes | 30 | 120 |
| memory_limit_mb | 2048 | 8192 |

### bld_output_template_director.md
---
kind: output_template
id: bld_output_template_director
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a satellite_spec
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: satellite_spec
```yaml
id: p08_sat_{{name_lower}}
kind: satellite_spec
pillar: P08
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{SATELLITE_NAME}}"
role: "{{primary_function_description}}"
model: "{{llm_model}}"
mcps: [{{mcp_1}}, {{mcp_2}}]
domain_area: "{{domain_this_satellite_covers}}"
boot_sequence:
  - "{{boot_step_1}}"
  - "{{boot_step_2}}"
constraints:
  - "{{constraint_1}}"
  - "{{constraint_2}}"
dispatch_keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]
tools: [{{tool_1}}, {{tool_2}}]
dependencies: [{{dependency_1}}]
scaling:
  max_concurrent: {{integer}}
  timeout_minutes: {{integer}}
  memory_limit_mb: {{integer}}
monitoring:
  health_check: "{{command_or_url}}"
  signal_on_complete: {{boolean}}
  alert_on_failure: {{boolean}}
runtime: "{{claude_or_codex}}"
mcp_config_file: "{{path_to_mcp_json_or_null}}"
flags: [{{flag_1}}, {{flag_2}}]
domain: "{{domain_value}}"
quality: null
tags: [satellite, {{domain_tag}}, {{name_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```
## Role
{{what_the_satellite_does_and_primary_function}}
## Model & MCPs
{{llm_model_details_and_mcp_server_specs}}
## Boot Sequence
{{ordered_initialization_steps}}
## Dispatch
{{keywords_and_routing_rules}}
## Constraints
{{operational_limits_and_prohibitions}}
## Dependencies
{{external_services_and_sibling_satellites}}
## Scaling & Monitoring
{{concurrency_timeouts_health_checks}}
## References
- {{reference_1}}
- {{reference_2}}

### bld_architecture_director.md
---
kind: architecture
id: bld_architecture_director
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of satellite_spec — inventory, dependencies, and architectural position
---

# Architecture: satellite_spec in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 24-field metadata header (id, kind, pillar, domain, model, mcps, etc.) | satellite-spec-builder | active |
| role_definition | Primary domain and responsibility of the satellite | author | active |
| model_config | LLM model selection with provider and parameters | author | active |
| mcp_servers | List of MCP servers the satellite connects to at boot | author | active |
| boot_sequence | Ordered steps for satellite initialization | author | active |
| constraints | Resource limits, domain boundaries, and prohibited actions | author | active |
| dispatch_rules | How tasks are routed to this satellite based on keywords | author | active |
| monitoring | Health checks, signal emission, and observability configuration | author | active |
## Dependency Graph
```
router          --dispatches_to-->  satellite_spec  --configures-->  agent
spawn_config    --launches-->       satellite_spec  --depends-->     mcp_server
satellite_spec  --signals-->        health_status
```
| From | To | Type | Data |
|------|----|------|------|
| router (P02) | satellite_spec | data_flow | task dispatched to satellite based on routing rules |
| spawn_config (P12) | satellite_spec | dependency | launch configuration for terminal spawn |
| satellite_spec | agent (P02) | produces | satellite instantiates agents within its domain |
| satellite_spec | mcp_server (P04) | dependency | satellite requires specific MCP servers at runtime |
| satellite_spec | health_status (P12) | signals | periodic health and availability signals |
| model_card (P02) | satellite_spec | dependency | model specifications inform model_config selection |
## Boundary Table
| satellite_spec IS | satellite_spec IS NOT |
|-------------------|----------------------|
| A complete specification of an autonomous satellite | An individual agent identity (agent P02) |
| Defines model, MCPs, boot sequence, and constraints | A boot configuration for one provider (boot_config P02) |
| Scoped to a domain with dispatch rules and monitoring | A reusable architecture solution (pattern P08) |
| Includes resource limits and prohibited actions | An inviolable operational rule (law P08) |
| Configures observability with health checks and signals | A visual architecture representation (diagram P08) |
| Documents the full satellite as a deployable unit | An inventory of generic system components (component_map P08) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Identity | frontmatter, role_definition | Satellite name, domain, and primary responsibility |
| Configuration | model_config, mcp_servers, boot_sequence | Model, tools, and initialization procedure |
| Governance | constraints, dispatch_rules | Domain boundaries and task routing criteria |
| Operations | monitoring, health_status | Health checks and observability |
| Integration | router, spawn_config, agent | How the satellite is launched and receives work |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `director-builder` for pipeline function `COLLABORATE`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
