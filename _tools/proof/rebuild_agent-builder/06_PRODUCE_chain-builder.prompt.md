# CEX Crew Runner -- Builder Execution
**Builder**: `chain-builder`
**Function**: PRODUCE
**Intent**: reconstroi agent-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:20.339812

## Intent Context
- **Verb**: reconstroi
- **Object**: agent-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_chain.md
---
id: chain-builder
kind: type_builder
pillar: P03
parent: null
domain: chain
llm_function: BECOME
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [kind-builder, chain, P03, specialist, pipeline, sequential]
---

# chain-builder
## Identity
Especialista em construir `chain` — sequencias de prompts encadeados onde output A
eh input B. Domina prompt chaining, composicao sequencial, data flow tipado entre
steps, branching logic, e error handling strategies across LangChain SequentialChain,
DSPy Module composition, e manual pipeline patterns.
## Capabilities
- Decompor tarefas complexas em steps atomicos de prompt (1 step = 1 LLM call)
- Produzir chain com frontmatter completo (19 campos)
- Definir data flow e context passing entre steps com tipos explicitos
- Especificar error handling strategy (fail_fast, skip, retry, fallback)
- Mapear boundaries: chains sao PROMPTS, nao workflows (P12)
- Validar artifact contra quality gates (8 HARD + 10 SOFT)
## Routing
keywords: [chain, pipeline, sequential, prompt-chain, multi-step, composition, LLMChain]
triggers: "create prompt chain for pipeline", "build sequential prompt flow", "design multi-step prompt chain"
## Crew Role
In a crew, I handle PROMPT PIPELINE DESIGN.
I answer: "what prompts run in what order, and how does data flow between them?"
I do NOT handle: runtime orchestration (workflow), agent coordination (crew), task routing (dispatch_rule).

### bld_instruction_chain.md
---
kind: instruction
id: bld_instruction_chain
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for chain
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a chain
## Phase 1: RESEARCH
1. Identify the complex task to decompose: state the input and the final output in concrete terms
2. List atomic steps: each step must be exactly one LLM call with one purpose — split any step that requires two decisions into two steps
3. Define data flow between steps: for each connection, specify the exact type (string, list, JSON object, markdown block) of data passed from one step to the next
4. Determine error handling strategy per step: fail_fast for steps where downstream steps cannot proceed without the output, skip for enrichment steps, retry for transient failures, fallback for steps with an acceptable degraded alternative
5. Map branching logic: if any step produces a conditional output, define the condition and both paths explicitly
6. Search for existing chains that perform the same transformation (avoid duplicates)
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Fill frontmatter: all 19 fields (quality: null, never self-score)
4. Set quality: null
5. Write Steps section: for each step, provide name, the prompt reference it uses, input type, and output type — all four fields required per step
6. Write Data Flow section: connections between steps with typed inputs and outputs shown explicitly
7. Write Error Handling section: strategy for each step and the global fallback policy
8. Write Branching section: conditions for each path selection, or state "no branching" if the chain is strictly linear
9. Write Context Passing section: specify which data accumulates across steps and which resets at each step boundary
10. Verify steps_count in frontmatter matches the actual number of steps written
11. Keep body <= 8192 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. HARD gate: id matches `p03_ch_` pattern
3. HARD gate: kind == chain
4. HARD gate: quality == null
5. HARD gate: every step has input type and output type specified
6. HARD gate: error handling strategy is specified (at minimum at the global level)
7. HARD gate: each step represents exactly one LLM call — reject any step that describes multiple calls or includes routing logic
8. Cross-check: do the steps reference prompts (not workflows)? Chains belong to P03, workflows belong to P12
9. Cross-check: is there any runtime orchestration logic embedded in the steps? Runtime orchestration is not part of a chain definition
10. Cross-check: are all data types between steps explicit, not implied?
11. If score < 8.0: revise before outputting

### bld_knowledge_card_chain.md
---
kind: knowledge_card
id: bld_knowledge_card_chain
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for chain production — sequential prompt pipelines
sources: LangChain SequentialChain, DSPy Module composition, Anthropic prompt chaining guide
---

# Domain Knowledge: chain
## Executive Summary
Chains are sequential prompt pipelines where output A feeds input B across multiple LLM calls. Each step performs one atomic task with typed I/O, enabling reliable composition without agent overhead. Chains differ from workflows (runtime orchestration with agents), DAGs (dependency graphs without execution), and instructions (step-by-step recipes for one agent).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 (prompts) |
| Frontmatter fields | 19 |
| Quality gates | 8 HARD + 10 SOFT |
| Flow types | sequential, branching, parallel, mixed |
| Error strategies | fail_fast, skip, retry, fallback |
| Context passing | full, filtered, summary |
| Step constraint | 1 step = 1 LLM call |
## Patterns
- **Atomic steps**: each step has one clear purpose and one LLM call — compound steps are split into separate chain links
- **Typed I/O contracts**: explicit input/output types per step prevent data mismatches between chain links
- **Context passing strategies**: full (all prior output), filtered (relevant subset), summary (compressed) — choose based on context window budget
- **Error propagation**: fail_fast for critical paths; skip for optional enrichment steps; retry for transient failures
- **Narrowing funnel**: early steps gather broadly, later steps filter and refine — most efficient information flow
| Source | Concept | Application |
|--------|---------|-------------|
| LangChain SequentialChain | Chained LLMChains with variable passing | Direct: steps with typed I/O |
| DSPy Module composition | Composable modules with typed signatures | Typed contracts per step |
| Anthropic prompt chaining | Multi-step prompt best practices | Step atomicity, error strategy |
| LangGraph | Stateful graph-based chains | Branching and parallel flows |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Multi-purpose steps | Step does too much; hard to debug and test in isolation |
| Untyped I/O between steps | Data format mismatches cause silent failures |
| Full context passing always | Context window overflows on long chains |
| No error strategy defined | One step failure crashes entire chain silently |
| Missing data flow diagram | Hidden dependencies between steps go unnoticed |
| Chain used for agent coordination | That is a workflow (P12), not a prompt chain |
## Application
1. Decompose task into atomic steps: each step = 1 LLM call with 1 purpose
2. Define typed I/O for each step: input type, output type, format
3. Choose context passing: full, filtered, or summary per step transition
4. Set error strategy: fail_fast for critical, skip for enrichment, retry for transient
5. Draw data flow: visualize which output feeds which input
6. Validate: each step independently testable, total steps <= 10 for maintainability
## References
- LangChain: SequentialChain, LCEL documentation
- DSPy: Module composition and typed signatures
- Anthropic: prompt chaining best practices guide
- LangGraph: stateful graph-based chain execution

### bld_quality_gate_chain.md
---
id: p11_qg_chain
kind: quality_gate
pillar: P11
title: "Gate: chain"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: "prompt pipeline design — sequential LLM call chains with typed data flow between steps"
quality: null
tags: [quality-gate, chain, P03, prompt-pipeline, sequential, data-flow]
tldr: "Pass/fail gate for chain artifacts: step atomicity, typed data flow, error handling strategy, and pipeline completeness."
density_score: 0.91
---

# Gate: chain
## Definition
| Field | Value |
|---|---|
| metric | chain artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: chain` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | `id: my_chain` but file is `other_chain.md` |
| H04 | Kind equals literal `chain` | `kind: workflow` or `kind: pipeline` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `steps`, `input_schema`, or `output_schema` |
| H07 | Chain has at least two steps | Single-step chain is a prompt, not a chain |
| H08 | Each step has an explicit output type | Step output typed as `any` or unspecified |
| H09 | Error handling strategy declared | `error_handling` field absent; must be one of: fail_fast, skip, retry, fallback |
| H10 | No step references a runtime executor | Step contains orchestration logic (loops, parallelism) — chain is prompts only |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Step atomicity | 1.0 | Each step is one LLM call; no compound logic bundled in a single step |
| Data flow explicitness | 1.0 | Each step declares which prior step's output it consumes |
| Type coverage | 1.0 | All input/output types are concrete (string, number, list[string], not `any`) |
| Error handling granularity | 1.0 | Error strategy defined per-step or with justified global default |
| Context passing efficiency | 0.5 | Passes only required fields to each step, not entire prior context |
| Step naming clarity | 0.5 | Step names describe the LLM task (extract_entities not step_2) |
| Branching documentation | 1.0 | Conditional branches have explicit conditions and merge points documented |
| Prompt boundaries | 1.0 | No step bleeds workflow logic (loops, state management) into prompt text |
| Input schema completeness | 0.5 | Input schema covers all fields consumed by first step |
| Output schema alignment | 0.5 | Output schema matches the final step's declared output type |
| Domain specificity | 1.0 | Step prompts and transforms specific to the declared domain problem |
| Testability | 1.0 | Each step can be unit-tested with mock input/output independently |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Proof-of-concept chain during active research spike, not intended for production use |
| approver | Lead author acknowledgment in artifact comment block |
| audit_trail | Bypass reason and spike ticket ID recorded in frontmatter comment |
| expiry | 48h — spike chains must either reach >= 7.0 or be deleted |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics) |

### bld_schema_chain.md
---
kind: schema
id: bld_schema_chain
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for chain
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: chain
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p03_ch_{pipeline_slug}) | YES | - | Namespace compliance |
| kind | literal "chain" | YES | - | Type integrity |
| pillar | literal "P03" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| title | string | YES | - | Human-readable chain name |
| steps_count | integer | YES | - | Number of steps in body (must match) |
| flow | enum: sequential, branching, parallel, mixed | YES | "sequential" | Step arrangement |
| input_format | string | YES | - | What the first step receives |
| output_format | string | YES | - | What the last step produces |
| context_passing | enum: full, filtered, summary | REC | "full" | Inter-step context strategy |
| error_strategy | enum: fail_fast, skip, retry, fallback | REC | "fail_fast" | Chain-level error handling |
| domain | string | YES | - | Domain this chain belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "chain" |
| tldr | string <= 160ch | YES | - | Dense summary |
| density_score | float 0.80-1.00 | REC | - | Content density |
## ID Pattern
Regex: `^p03_ch_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Purpose` — why this chain exists, what transformation it performs
2. `## Steps` — numbered steps, each with Input/Prompt/Output subsections
3. `## Data Flow` — ASCII diagram showing step connections + context strategy
4. `## Error Handling` — strategy, failure behavior, retry policy
## Constraints
- max_bytes: 6144 (body only)
- naming: p03_ch_{pipeline_slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- steps_count MUST match actual count of numbered steps in body
- Each step MUST define Input, Prompt, and Output
- Steps are TEXT transformations only — no agent spawns or tool calls
- quality: null always

### bld_examples_chain.md
---
kind: examples
id: bld_examples_chain
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of chain artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: chain-builder
## Golden Example
INPUT: "Create a prompt chain for research-to-knowledge-card pipeline"
OUTPUT:
```yaml
id: p03_ch_research_to_kc
kind: chain
pillar: P03
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
title: "Research to Knowledge Card Pipeline"
steps_count: 3
flow: sequential
input_format: "topic name + domain string"
output_format: "knowledge_card markdown artifact"
context_passing: filtered
error_strategy: fail_fast
domain: "knowledge"
quality: null
tags: [chain, knowledge, research, distillation]
tldr: "3-step chain: gather sources, extract facts, compose KC with density >= 0.80"
density_score: 0.88
```
## Purpose
Transforms a raw topic into a production-ready knowledge_card by chaining three
prompt steps: source gathering, fact extraction, and KC composition. Each step
narrows scope — from broad research to atomic distilled facts.
## Steps
### Step 1: Gather Sources
- **Input**: topic name (string), domain (string)
- **Prompt**: Search for authoritative sources on {{topic}} in {{domain}}. Return 3-5 URLs with one-line summaries.
- **Output**: list of {url, summary} objects (JSON)
### Step 2: Extract Facts
- **Input**: list of {url, summary} from Step 1
- **Prompt**: For each source, extract 5-10 atomic facts as bullets <= 80 chars. Remove opinions and filler.
- **Output**: deduplicated fact list (markdown bullets)
### Step 3: Compose KC
- **Input**: fact list from Step 2, original topic/domain
- **Prompt**: Compose a knowledge_card following P01 schema. Fill all required fields. density >= 0.80.
- **Output**: complete knowledge_card artifact (YAML frontmatter + markdown body)
## Data Flow
```text
[topic, domain] --string--> Gather --JSON--> Extract --bullets--> Compose --KC.md-->
```
Context passing: filtered — each step receives only its direct input, not full history.
## Error Handling
- **Strategy**: fail_fast
- **On failure at step N**: halt chain, return partial output with error context
- **Retry policy**: none (source quality issues require human intervention)
## References
- P01_knowledge/_schema.yaml (KC field definitions)
- archetypes/builders/knowledge-card-builder/ (downstream consumer)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p03_ch_ pattern (H02 pass)
- kind: chain (H04 pass)
- 19 required fields present (H06 pass)
- body has Purpose + Steps + Data Flow + Error Handling (H07 pass)
- steps_count: 3 matches actual 3 steps (H08 pass)
- Each step has Input/Prompt/Output (S03 pass)
- Data flow diagram present and matches steps (S04 pass)
- No runtime orchestration in body (S08 pass)
- No filler phrases (S10 pass)
## Anti-Example
INPUT: "Create a chain for content processing"
BAD OUTPUT:
```yaml
id: content_chain
kind: prompt
pillar: prompt
title: Content Chain
steps_count: 5
quality: 9.0
tags: [content]
```
This chain processes content through multiple steps. First, we gather the content.
Then we process it. Finally, we output the result.
## Steps
1. Get content
2. Process content
3. Output result
FAILURES:
1. id: no `p03_ch_` prefix -> H02 FAIL
2. kind: "prompt" not "chain" -> H04 FAIL
3. pillar: "prompt" not "P03" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. Missing fields: version, created, updated, author, flow, input_format, output_format, domain -> H06 FAIL
6. tags: only 1 item, missing "chain" -> S02 FAIL
7. Steps lack Input/Prompt/Output structure -> S03 FAIL
8. No Data Flow diagram -> S04 FAIL
9. No Error Handling section -> S06 FAIL
10. Body is filler prose ("This chain processes...") -> S10 FAIL

### bld_config_chain.md
---
kind: config
id: bld_config_chain
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: chain Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p03_ch_{pipeline_slug}.md` | `p03_ch_research_to_kc.md` |
| Builder directory | kebab-case | `chain-builder/` |
| Frontmatter fields | snake_case | `steps_count`, `error_strategy` |
| Pipeline slug | snake_case, lowercase | `research_to_kc`, `content_enrichment` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P03_prompt/examples/p03_ch_{pipeline_slug}.md`
- Compiled: `cex/P03_prompt/compiled/p03_ch_{pipeline_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 6144 bytes
- Total (frontmatter + body): ~8000 bytes
- Density: >= 0.80
## Flow Type Enum
| Value | When to use | Example |
|-------|-------------|---------|
| sequential | Steps run in order A->B->C | Most pipelines |
| branching | Steps branch based on condition | Intent-based routing |
| parallel | Steps run simultaneously, merge results | Multi-perspective analysis |
| mixed | Combination of above patterns | Complex pipelines |
## Error Strategy Enum
| Value | When to use | Example |
|-------|-------------|---------|
| fail_fast | Stop chain on first failure | Critical data paths |
| skip | Skip failed step, continue with partial data | Enrichment/optional steps |
| retry | Retry failed step N times before failing | Transient API errors |
| fallback | Use alternative step on failure | Graceful degradation |
## Body Requirements
- Purpose: 2-4 sentences, must explain the transformation
- Steps: numbered, each with Input/Prompt/Output subsections
- Data Flow: ASCII diagram showing step connections
- Error Handling: strategy + failure behavior

### bld_output_template_chain.md
---
kind: output_template
id: bld_output_template_chain
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a chain
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: chain
```yaml
id: p03_ch_{{pipeline_slug}}
kind: chain
pillar: P03
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
title: "{{human_readable_title}}"
steps_count: {{integer_matching_body}}
flow: {{sequential|branching|parallel|mixed}}
input_format: "{{what_first_step_receives}}"
output_format: "{{what_last_step_produces}}"
context_passing: {{full|filtered|summary}}
error_strategy: {{fail_fast|skip|retry|fallback}}
domain: "{{domain_value}}"
quality: null
tags: [chain, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```
## Purpose
{{why_this_chain_exists_2_to_4_sentences}}
## Steps
### Step 1: {{step_name}}
- **Input**: {{input_type_and_description}}
- **Prompt**: {{what_this_step_does}}
- **Output**: {{output_type_and_description}}
### Step 2: {{step_name}}
- **Input**: {{receives_from_step_1}}
- **Prompt**: {{what_this_step_does}}
- **Output**: {{output_type_and_description}}
{{...repeat for steps_count steps}}
## Data Flow
```text
{{step_1}} --{{data_type}}--> {{step_2}} --{{data_type}}--> {{step_N}}
```
Context passing: {{context_passing_strategy_description}}
## Error Handling
- **Strategy**: {{error_strategy}}
- **On failure at step N**: {{failure_behavior}}
- **Retry policy**: {{retry_details_if_applicable}}
## References
- {{reference_1}}
- {{reference_2}}

### bld_architecture_chain.md
---
kind: architecture
id: bld_architecture_chain
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of chain — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| step | Single LLM call unit — one prompt in, one output out | chain | required |
| data_flow | Typed binding that passes output of step N to input of step N+1 | chain | required |
| error_handling | Strategy applied when a step fails (fail_fast, skip, retry, fallback) | chain | required |
| context_pass | Mechanism for carrying shared context across all steps | chain | required |
| branching_logic | Conditional routing — directs flow to different step paths | chain | optional |
| system_prompt | Agent persona injected into step prompts | P03 | external |
| output_schema | Typed contract defining step output shape | P05/P06 | external |
| knowledge_card | Domain facts injected into one or more steps | P01 | external |
| workflow | Runtime orchestrator that may embed this chain as a substep | P12 | consumer |
## Dependency Graph
```
knowledge_card  --produces--> step
system_prompt   --produces--> step
output_schema   --produces--> step
step            --produces--> data_flow
data_flow       --produces--> step
step            --depends-->  error_handling
context_pass    --produces--> step
branching_logic --depends-->  data_flow
workflow        --depends-->  chain
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card | step | produces | domain facts for prompt hydration |
| system_prompt | step | produces | persona and operational rules |
| output_schema | step | produces | typed output contract |
| step | data_flow | produces | step output (text or structured) |
| data_flow | step | produces | input for next step |
| step | error_handling | depends | failure signal triggering strategy |
| context_pass | step | produces | shared context available to all steps |
| branching_logic | data_flow | depends | conditional routing decision |
| workflow | chain | depends | embeds chain as a prompt substep |
## Boundary Table
| chain IS | chain IS NOT |
|----------|-------------|
| Sequential prompt pipeline — output A feeds input B | A runtime orchestrator managing agents and tools (that is workflow) |
| Text-to-text transformations only | A task dependency graph without execution semantics (that is dag) |
| One LLM call per step | An intra-prompt reasoning technique (that is chain_of_thought) |
| Defined data flow with typed bindings between steps | A single-task action prompt (that is action_prompt) |
| Error handling strategy at step level | A step-by-step agent execution protocol (that is instruction) |
| Composable — consumed by workflows as a substep | Contains agents, tools, or signals |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| knowledge | knowledge_card, system_prompt | Provide domain context and persona for step prompts |
| composition | step, context_pass, branching_logic | Define the individual LLM calls and conditional routing |
| data | data_flow, output_schema | Type and route data between steps |
| resilience | error_handling | Define behavior when a step fails |
| integration | workflow (consumer) | Runtime orchestration that embeds chains |

### bld_collaboration_chain.md
---
kind: collaboration
id: bld_collaboration_chain
pillar: P12
llm_function: COLLABORATE
purpose: How chain-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: chain-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what prompts run in what order, and how does data flow between them?"
I do not orchestrate agents. I do not define individual task prompts.
I compose prompt pipelines so multi-step LLM tasks execute in correct sequence with typed data flow.
## Crew Compositions
### Crew: "Prompt Pipeline"
```
  1. action-prompt-builder -> "individual task prompts (steps)"
  2. chain-builder -> "sequential composition with data flow"
  3. input-schema-builder -> "typed contracts between chain steps"
```
### Crew: "Complex Task Decomposition"
```
  1. instruction-builder -> "step-by-step recipe for task"
  2. chain-builder -> "prompt chain that implements the recipe"
  3. e2e-eval-builder -> "end-to-end test of the full chain"
```
## Handoff Protocol
### I Receive
- seeds: task decomposition (list of steps), data flow description
- optional: error handling strategy, branching conditions, context passing rules
### I Produce
- chain artifact (.md + .yaml frontmatter)
- committed to: `cex/P03/examples/p03_chain_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- action-prompt-builder: provides individual step prompts composed into the chain
- input-schema-builder: provides typed contracts for inter-step data flow
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| e2e-eval-builder | Tests the full chain from input to final output |
| dag-builder | May model chain dependencies in execution graphs |

### bld_memory_chain.md
---
id: p10_lr_chain_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Chains that attempted to pack multiple transformations into a single step produced outputs that were difficult to debug and impossible to partially retry. Enforcing 1 step = 1 LLM call with explicit typed input/output reduced debugging time by ~60% and enabled partial retry at the step level."
pattern: "Each chain step must have exactly one purpose, one LLM call, and explicitly typed input and output. Data flows between steps via named output references. Error handling is declared per step, not per chain."
evidence: "5 pipeline patterns validated across research, data processing, and intent routing domains. Step granularity discipline eliminated 'which step broke?' ambiguity in all cases where it was applied."
confidence: 0.7
outcome: SUCCESS
domain: chain
tags: [chain, prompt-decomposition, data-flow, step-granularity, error-handling]
tldr: "One step, one purpose, one LLM call. Typed inputs and outputs at every boundary. Handle errors per step, not per chain."
impact_score: 7.5
decay_rate: 0.05
satellite: edison
keywords: [prompt chain, step decomposition, data flow, typed output, partial retry, error handling, atomic step]
---

## Summary
Complex tasks decomposed into prompt chains fail in one of two ways: steps that are too coarse (multiple transformations packed together, hard to debug) or steps that are too fine (one sentence per step, creating orchestration overhead without benefit). The effective middle ground is 1 step = 1 transformation with a single LLM call, explicit typed input, and explicit typed output.
The key insight: a chain is not a script. It has no mutable state between steps except what is explicitly passed. This constraint, enforced strictly, makes each step independently testable and retryable.
## Pattern
**Atomic step discipline.**
1. Define the chain's goal as a single sentence. Every step must serve that goal directly.
2. Assign each step a single purpose: classify, extract, summarize, format, validate, route, or generate. No compound purposes.
3. Declare typed input and output for each step before writing the prompt. Input type drives what the step receives; output type drives what the next step can consume.
4. Data flow: each step references prior step outputs by name (e.g., `step_1.output.entities`). No implicit global state.
5. Error handling per step: define what happens when that step's LLM call fails or returns unexpected type. Options: retry, skip, abort chain, return partial.
6. Steps_count in frontmatter must equal the actual count of numbered steps in the body (validator catches mismatch).
Common pipeline shapes:
- Extract-Transform-Load (3 steps, sequential): data processing
- Research-Synthesize-Format (3 steps, sequential): knowledge production
- Classify-Route-Execute (3 steps, branching): intent-based handling
- Parallel-Merge (2+ steps, parallel then merge): multi-perspective analysis
- Gather-Filter-Compose (3 steps, sequential): content curation
## Anti-Pattern
- Packing two transformations into one step to reduce step count (saves nothing; costs debuggability).
- Implicit data passing (step 3 "knows" what step 1 produced without explicit reference).
- Per-chain error handling only (when step 2 fails, which step do you retry?).
- Steps without typed output (the next step has no contract to code against).
- Confusing chain with chain-of-thought: chain = separate LLM calls between prompts; CoT = reasoning within one prompt.
- Including orchestration logic (spawns, signals, agent routing) in a chain — that belongs in a workflow.
## Context
The chain-vs-workflow boundary is the most common confusion point. A chain is purely data transformation across LLM calls with no side effects and no external system calls. The moment a step writes to a database, sends a signal, or spawns another process, it has crossed into workflow territory.


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `chain-builder` for pipeline function `PRODUCE`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
