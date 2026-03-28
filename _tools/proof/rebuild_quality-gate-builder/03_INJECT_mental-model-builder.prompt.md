# CEX Crew Runner -- Builder Execution
**Builder**: `mental-model-builder`
**Function**: INJECT
**Intent**: reconstroi quality-gate-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:18.995810

## Intent Context
- **Verb**: reconstroi
- **Object**: quality-gate-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_mental_model.md
---
id: mental-model-builder
kind: type_builder
pillar: P02
parent: null
domain: mental_model
llm_function: BECOME
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: EDISON
tags: [kind-builder, mental-model, P02, specialist, routing, decision-tree, cognitive-map]
---

# mental-model-builder
## Identity
Especialista em construir `mental_model` (P02) artifacts — mapas cognitivos de design-time
que definem routing rules, decision trees, priorities, heuristics, e domain maps de um agente.
Domina routing rule composition, decision tree branching, priority ordering, heuristic
formulation, domain boundary scoping, and personality trait definition.
Produz mental models densos com routing/decisions completos e boundaries claros.
## Capabilities
- Produzir mental_model (P02) com frontmatter completo (14 required + 9 recommended)
- Compor routing rules com keywords, actions, e confidence thresholds
- Estruturar decision trees com if/then/else branching
- Definir priorities, heuristics, e domain maps
- Validar artifact contra quality gates (9 HARD + 12 SOFT)
- Detectar boundary violations (P02 mental_model vs P10 mental_model vs agent vs router)
## Routing
keywords: [mental-model, routing, decision-tree, cognitive-map, heuristics, priorities, domain-map, agent-blueprint]
triggers: "create mental model for agent", "define routing rules and decisions", "build cognitive map for agent"
## Crew Role
In a crew, I handle AGENT COGNITIVE DESIGN.
I answer: "how does this agent route tasks, make decisions, and prioritize work?"
I do NOT handle: agent definition (agent-builder), task routing rules (router-builder [PLANNED]), runtime state (P10 mental-model [PLANNED]).

### bld_instruction_mental_model.md
---
id: p03_ins_mental_model
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Mental Model Builder Execution Protocol
target: mental-model-builder agent
phases_count: 4
prerequisites:
  - Target agent name and domain are identified
  - Primary routing patterns (what triggers what) are describable
  - Agent's key decision points during operation are known
validation_method: checklist
domain: mental_model
quality: null
tags: [instruction, mental-model, routing, P02, decision-tree, cognitive-map]
idempotent: true
atomic: false
rollback: "Discard generated artifact; agent behavior is unchanged"
dependencies: []
logging: true
tldr: Build a cognitive map for an agent defining routing rules, decision trees, priorities, heuristics, domain boundaries, and fallback behavior.
density_score: 0.91
---

## Context
The mental-model-builder produces `mental_model` artifacts (P02) — design-time cognitive maps that define how an agent routes tasks, makes decisions, and prioritizes work. Mental models differ from agent definitions (identity and capabilities), runtime state (P10, ephemeral), and router artifacts (pure task dispatchers): a mental model encodes the thinking patterns an agent uses during execution.
**Inputs:**
- `$agent_name (required) - string - "The agent this mental model belongs to (e.g. 'scout-agent', 'law-builder')"`
- `$agent_slug (required) - string - "snake_case version of agent name for use in id field"`
- `$domain (required) - string - "Primary domain the agent operates in"`
- `$routing_triggers (required) - list[string] - "Keywords or signal types that trigger this agent's activation"`
- `$decisions (optional) - list[string] - "Key binary or multi-path decisions the agent makes during operation"`
- `$domain_map (optional) - object - "What the agent covers vs what it delegates; keys: covers, routes_to"`
**Output:** A single `mental_model` artifact (P02), body <= 2048 bytes, with 14 required + 9 recommended frontmatter fields and body sections covering agent reference, routing rules, decision tree, priorities, heuristics, domain map, and fallback.
**Boundary check before proceeding:**
- Need to define the agent's identity and capabilities → route to agent-builder
- Need to define runtime state → do not use mental_model (P02), use P10 runtime state
- Need a pure task dispatcher with no domain logic → route to router-builder (planned)
- Need to encode how an agent thinks, routes, and decides → proceed
## Phases
### Phase 1: Analyze
**Action:** Gather and organize the cognitive parameters of the target agent.
1. Identify the **target agent** by name and domain.
2. Determine primary **routing patterns**: what input signals trigger what agent behaviors.
3. List **key decisions** the agent makes — binary or multi-path choices at decision points.
4. Identify **priority ordering**: what takes precedence when multiple tasks or signals compete.
5. Collect **heuristics**: actionable rules of thumb derived from the agent's operational patterns.
6. Map **domain boundaries**:
   - `covers`: what this agent handles directly
   - `routes_to`: what this agent delegates, and to which other agents
7. Check for existing mental_models for the same agent — avoid duplicates.
8. Confirm this is P02 (design-time cognitive map), NOT P10 (runtime state).
9. Define `fallback`: what the agent does when no routing rule matches.
**Verification:** You can describe the agent's routing in one sentence: "When [signal type], this agent does [action]; when [other signal], it routes to [other agent]."
### Phase 2: Compose
**Action:** Write all frontmatter fields and body sections within the 2048-byte body limit.
1. Read `SCHEMA.md` — source of truth for all 14 required + 9 recommended fields.
2. Read `OUTPUT_TEMPLATE.md` — fill every `{{var}}` following SCHEMA constraints.
3. Generate `agent_slug` in snake_case from the agent name.
4. Fill frontmatter: all 14 required fields (`quality: null`).
5. Build `routing_rules`: list of >= 3 rules, each with: `keywords` (list), `action` (string), `confidence` (float 0.0–1.0).
6. Build `decision_tree`: list of >= 2 conditions, each with: `condition` (string), `then` (string), `else` (string).
7. Set `priorities`: ordered list, highest priority first.
8. Set `heuristics`: list of actionable rules of thumb (not observations — each must guide a choice).
9. Set `domain_map`: object with `covers` (list) and `routes_to` (dict: domain → agent).
10. Set `personality`: object with `tone`, `verbosity`, `risk_tolerance`.
11. Set `constraints`: list of hard behavioral limits the agent must never violate.
12. Set `fallback`: object with `action` (what to do) and `escalate_to` (who to ask).
13. Write `## Agent Reference` — one-line identity: who this agent is and its primary function.
14. Write `## Routing Rules` — table with columns: Keywords | Action | Confidence.
15. Write `## Decision Tree` — numbered if/then/else list.
16. Write `## Priorities` — ordered list, highest first.
17. Write `## Heuristics` — actionable rules of thumb.
18. Write `## Domain Map` — what this agent covers vs routes to others.
Byte budget pseudocode:
```
body_bytes = len(encode_utf8(body_content))
# if body_bytes > 2048: compress heuristics, merge similar routing rules
```
**Verification:** `routing_rules` has >= 3 rules. `decision_tree` has >= 2 conditions, each with `condition`, `then`, and `else`. Body <= 2048 bytes. Keywords in routing rules are specific (not "general" or "anything").
### Phase 3: Validate
**Action:** Run all 9 HARD gates from `QUALITY_GATES.md`. Fix any failure before output.
| Gate | Check |
|------|-------|
| H01 | YAML frontmatter parses without error |
| H02 | `id` matches pattern `^p02_mm_[a-z][a-z0-9_]+$` |
| H03 | `kind` is literal string `mental_model` |
| H04 | `pillar` is `P02` (NOT P10) |
| H05 | `quality` is `null` |
| H06 | `routing_rules` has >= 3 rules each with keywords + action |
| H07 | `decision_tree` has >= 2 conditions each with condition + then |

### bld_knowledge_card_mental_model.md
---
kind: knowledge_card
id: bld_knowledge_card_mental_model
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for mental_model production — atomic searchable facts
sources: mental-model-builder MANIFEST.md + SCHEMA.md, cognitive science, BDI architecture
---

# Domain Knowledge: mental_model
## Executive Summary
Mental models are design-time cognitive blueprints for agents — structured YAML artifacts encoding routing rules, decision trees, priorities, heuristics, and domain boundaries. Each mental model belongs to exactly ONE agent and defines how that agent thinks, not what it does. They differ from agents (which have capabilities and tools), routers (which route tasks between components), system prompts (which define persona), and P10 runtime state (which is ephemeral) by being static, versioned cognitive maps loaded at agent boot.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 (design-time spec) |
| Kind | `mental_model` (exact literal) |
| ID pattern | `p02_mm_{agent_slug}` |
| Machine format | YAML |
| Required frontmatter | 14 fields |
| Recommended frontmatter | 9 fields (personality, fallback, etc.) |
| Quality gates | 9 HARD + 12 SOFT |
| Max body | 2048 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Min routing rules | 3 |
| Min decision tree conditions | 2 |
## Patterns
| Pattern | Application |
|---------|-------------|
| Routing specificity | Keywords must be concrete nouns/verbs, never vague categories |
| Confidence thresholds | 0.8+ direct routing, 0.5-0.8 tentative, <0.5 fallback |
| Decision tree depth | Max 3 levels to avoid reasoning complexity |
| Priority ordering | Highest first, max 5-7 priorities (Miller's law) |
| Heuristic formulation | "when X, prefer Y because Z" — actionable, not philosophical |
| Domain map scoping | Explicit covers/routes_to prevents boundary drift |
| Personality coherence | tone + verbosity + risk_tolerance must be internally consistent |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| `pillar: P10` on a mental_model | P10 is runtime state; mental_model is design-time P02 |
| Fewer than 3 routing rules | Fails HARD gate — insufficient routing coverage |
| Single-branch decision tree | Minimum 2 conditions required |
| Self-assigned quality score | `quality` must be null at creation |
| Generic heuristics | Must reflect actual agent edge cases, not platitudes |
| Mixing agent identity into mental_model | agent-builder owns identity; mental_model owns cognition |
| Vague keywords ("stuff", "things") | No routing signal; use domain-specific terms |
## Application
1. Identify target agent slug (e.g., `research_agent` -> `p02_mm_research_agent`)
2. Write frontmatter: all 14 required fields; set `quality: null`, `pillar: P02`
3. Define `routing_rules`: minimum 3 entries with keywords, action, confidence
4. Define `decision_tree`: minimum 2 if/then/else branches
5. Order `priorities` list highest-first (max 7 items)
6. Write `heuristics` as concise rules for domain-specific edge cases
7. Define `domain_map`: explicit scope IN and OUT boundaries
8. Validate: body <= 2048 bytes, id == filename stem, 9 HARD + 12 SOFT gates
## References
- mental-model-builder SCHEMA.md v1.0.0
- Johnson-Laird 1983 — Mental Models
- BDI architecture — Belief-Desire-Intention agent model

### bld_quality_gate_mental_model.md
---
id: p11_qg_mental_model
kind: quality_gate
pillar: P11
title: "Gate: Mental Model"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: EDISON
domain: mental_model
quality: null
tags: [quality-gate, mental-model, routing, P02, cognitive-map]
tldr: "Quality gate for mental_model artifacts: enforces routing rules, decision tree, domain map, and design-time-only scope."
density_score: 0.85
---

# Gate: Mental Model
## Definition
A `mental_model` is a design-time cognitive map that tells an agent how to route, prioritize, and decide. It carries no runtime state and executes no logic. Gates here enforce that routing rules have confidence thresholds, decisions have if/then/else structure, and the artifact never encodes live session data — which belongs in runtime state artifacts.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p02_mm_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"mental_model"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | All required fields present and non-empty (`id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `agent`, `domain`, `routing_rules`, `decision_tree`, `tags`, `tldr`) | Incomplete artifact |
| H07 | `Routing Rules` section present in body | Model has no routing — central purpose missing |
| H08 | `Decision Tree` or `Priorities` section present in body | No decision structure — model cannot guide choices |
| H09 | `Domain Map` section present in body | Domain boundaries undefined — routing leaks |
| H10 | `routing_rules` list has >= 3 entries, each with `keywords` and `action` | Routing table too sparse to be useful |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, names the agent and its primary routing concern |
| S02 | Routing rules have confidence thresholds | 1.0 | Each rule specifies a match confidence or keyword specificity level |
| S03 | Decisions have if/then/else structure | 1.0 | Decision tree entries follow: condition → then action → else action |
| S04 | Priorities ordered with rationale | 1.0 | `priorities` list is ranked and each rank has a one-line justification |
| S05 | Heuristics testable | 0.5 | Each heuristic can be verified with a specific input example |
| S06 | Domain boundaries explicit | 1.0 | Domain Map states what the agent covers AND what it routes away |
| S07 | Personality traits defined | 0.5 | `personality` object with `tone`, `verbosity`, `risk_tolerance` |
| S08 | `tags` includes `"mental-model"` | 0.5 | Minimum tag for routing |
| S09 | Conflict resolution rules present | 1.0 | Documents what happens when two routing rules match simultaneously |
| S10 | No runtime state encoded | 1.0 | No session counters, active task lists, or live flags in body |
| S11 | Fallback action defined | 0.5 | `fallback` specifies action and escalation target when no rule matches |
| S12 | Density >= 0.80 | 0.5 | No filler: "this model helps", "generally speaking", "in most cases" |
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool + record in memory |
| >= 8.0 | PUBLISH | Commit to pool |
| >= 7.0 | REVIEW | Acceptable with documented improvement items |
| < 7.0 | REJECT | Revise and resubmit — do not publish |
| 0 (HARD fail) | REJECTED | Fix failing HARD gate(s) first |
## Bypass
Bypasses are logged and expire automatically.
| Field | Value |
|-------|-------|
| condition | New agent bootstrapping — routing rules are provisional and under observation from live sessions |

### bld_schema_mental_model.md
---
kind: schema
id: bld_schema_mental_model
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for mental_model (P02)
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: mental_model
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p02_mm_{agent_slug}) | YES | - | Namespace compliance |
| kind | literal "mental_model" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment — NOT P10 |
| version | semver string | YES | "1.0.0" | Semantic versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| agent | string | YES | - | Target agent this model belongs to |
| routing_rules | object | YES | - | Keyword-to-action mappings |
| decision_tree | object | YES | - | If-then branching logic |
| domain | string | YES | - | Agent primary domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "mental-model" |
| tldr | string <= 160ch | YES | - | Dense one-liner |
| priorities | list[string] | REC | - | Ordered priority list (highest first) |
| heuristics | list[string] | REC | - | Rules of thumb for edge cases |
| domain_map | object | REC | - | Scope of knowledge domains with boundaries |
| tools_available | list[string] | REC | - | Tools this agent can invoke |
| personality | object | REC | - | Behavioral traits (tone, verbosity, risk) |
| constraints | list[string] | REC | - | Hard limits on behavior |
| fallback | object | REC | - | What to do when routing fails |
| llm_function | literal "BECOME" | REC | "BECOME" | Identity artifact |
| density_score | float 0.80-1.00 | OPT | - | Content density |
## Routing Rules Object
```yaml
routing_rules:
  - keywords: [list, of, trigger, words]
    action: "what to do"
    confidence: float  # 0.0-1.0 threshold
  - keywords: [...]
    action: "..."
```
## Decision Tree Object
```yaml
decision_tree:
  - condition: "if X"
    then: "action A"
    else: "action B"
  - condition: "if Y"
    then: "action C"
```
## ID Pattern
Regex: `^p02_mm_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Agent Reference` — which agent, one-line identity
2. `## Routing Rules` — table of keyword-to-action mappings with confidence
3. `## Decision Tree` — if-then branching logic as structured list
4. `## Priorities` — ordered priority list (highest first)
5. `## Heuristics` — rules of thumb for ambiguous cases
6. `## Domain Map` — scope boundaries (what agent covers vs routes away)
## Constraints
- max_bytes: 2048 (body only)
- naming: p02_mm_{agent_slug}.yaml
- machine_format: yaml
- id == filename stem
- quality: null always
- pillar: P02 (NOT P10 — P02 is design-time, P10 is runtime)
- routing_rules: minimum 3 rules
- decision_tree: minimum 2 conditions
- llm_function: BECOME (identity artifact)

### bld_examples_mental_model.md
---
kind: examples
id: bld_examples_mental_model
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of mental_model (P02) artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: mental-model-builder
## Golden Example
INPUT: "Create mental model for a content-reviewer agent"
OUTPUT:
```yaml
id: p02_mm_content_reviewer
kind: mental_model
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
agent: "content-reviewer"
routing_rules:
  - keywords: [review, audit, check, validate]
    action: "execute quality review pipeline"
    confidence: 0.9
  - keywords: [grammar, spelling, typo, language]
    action: "run language quality checks"
    confidence: 0.85
  - keywords: [compliance, legal, policy, brand]
    action: "apply compliance ruleset"
    confidence: 0.8
  - keywords: [improve, rewrite, enhance, optimize]
    action: "route to content-writer agent"
    confidence: 0.7
decision_tree:
  - condition: "content has compliance flags"
    then: "prioritize compliance review before style"
    else: "start with language quality"
  - condition: "quality score < 7.0"
    then: "reject with specific gate failures"
    else: "approve with score annotation"
  - condition: "content exceeds 5000 words"
    then: "split into sections and review each"
priorities:
  - "compliance (legal/brand violations block publish)"
  - "factual accuracy (wrong data is worse than bad grammar)"
  - "density (no filler, >= 0.80)"
  - "language quality (grammar, clarity, tone)"
  - "formatting (tables, headers, structure)"
heuristics:
  - "when unsure about compliance, flag for human review rather than approve"
  - "when density < 0.70, reject immediately — no amount of editing fixes filler"
  - "when content mixes domains, review each domain section against its own rubric"
domain_map:
  covers: [content_quality, compliance, language, density]
  routes_to:
    content_creation: "content-writer"
    research: "research-agent"
    translation: "translator-agent"
tools_available: [brain_query, grep, read, glob]
personality:
  tone: "direct"
  verbosity: "concise"
  risk_tolerance: "low"
constraints:
  - "never approve content with compliance violations"
  - "never self-score quality (annotate, do not judge)"
  - "never rewrite content — flag issues, let writer fix"
fallback:
  action: "log unroutable request and return to sender"
  escalate_to: "orchestrator"
domain: "content_review"
llm_function: BECOME
quality: null
tags: [mental-model, content-review, quality, routing, P02]
tldr: "Design-time cognitive map for content-reviewer: 4 routing rules, 3-branch decision tree, compliance-first priority"
density_score: 0.91
```
## Agent Reference
content-reviewer: reviews content for compliance, accuracy, density, and language quality.
## Routing Rules
| Keywords | Action | Confidence |
|----------|--------|------------|
| review, audit, check, validate | execute quality review pipeline | 0.9 |
| grammar, spelling, typo, language | run language quality checks | 0.85 |
| compliance, legal, policy, brand | apply compliance ruleset | 0.8 |
| improve, rewrite, enhance, optimize | route to content-writer agent | 0.7 |
## Decision Tree
1. IF content has compliance flags THEN prioritize compliance ELSE start with language
2. IF quality score < 7.0 THEN reject with failures ELSE approve with annotation
3. IF content > 5000 words THEN split and review each section
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p02_mm_ pattern (H02 pass) | kind: mental_model (H04 pass)
- pillar: P02 (H07 pass) | 23 fields (H06 pass) | 4 routing rules (H08 pass)
- 3 decision conditions (H09 pass) | priorities: 5 items (S03 pass)
- heuristics: 3 items (S04 pass) | domain_map with covers+routes_to (S05 pass)
- personality complete (S06 pass) | tools: 4 items (S07 pass) | constraints: 3 (S08 pass)
- fallback with action+escalate_to (S09 pass) | density: 0.91 (S10 pass)
- keywords are specific nouns/verbs (S12 pass) | no filler (S11 pass)
## Anti-Example
INPUT: "Make a mental model for my agent"

### bld_config_mental_model.md
---
kind: config
id: bld_config_mental_model
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: mental_model Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_mm_{agent_slug}.yaml` | `p02_mm_scout_agent.yaml` |
| Builder directory | kebab-case | `mental-model-builder/` |
| Frontmatter fields | snake_case | `routing_rules`, `decision_tree` |
| Agent slug | snake_case, lowercase | `scout_agent`, `research_lead` |
Rule: id MUST equal filename stem.
Rule: file extension is .yaml (pure YAML artifact).
## File Paths
- Output: `cex/P02_model/examples/p02_mm_{agent_slug}.yaml`
- Compiled: `cex/P02_model/compiled/p02_mm_{agent_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total: ~3000 bytes
- Density: >= 0.80
## Routing Rules Requirements
- Minimum 3 routing rules
- Each rule: keywords (list), action (string), confidence (float 0.0-1.0)
- Keywords must be specific (not "everything", "anything", "general")
- Actions must be concrete verbs ("route to X", "execute Y", "defer to Z")
## Decision Tree Requirements
- Minimum 2 conditions
- Each condition: if/then structure, optional else
- Conditions must be evaluable (not vague)
- No circular references between conditions
## Personality Enum Values
| Field | Allowed Values |
|-------|---------------|
| tone | professional, casual, technical, empathetic, direct |
| verbosity | concise, moderate, verbose |
| risk_tolerance | low, medium, high |
## Pillar Disambiguation
This builder produces P02 mental_model (design-time blueprint).
P10 mental_model (runtime session state) is a DIFFERENT kind.
Never set pillar to P10 — that requires a different builder.

### bld_output_template_mental_model.md
---
kind: output_template
id: bld_output_template_mental_model
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a mental_model artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: mental_model
```yaml
id: p02_mm_{{agent_slug}}
kind: mental_model
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
agent: "{{agent_name}}"
routing_rules:
  - keywords: [{{kw_1a}}, {{kw_1b}}, {{kw_1c}}]
    action: "{{action_1}}"
    confidence: {{0.0-1.0}}
  - keywords: [{{kw_2a}}, {{kw_2b}}]
    action: "{{action_2}}"
    confidence: {{0.0-1.0}}
  - keywords: [{{kw_3a}}, {{kw_3b}}]
    action: "{{action_3}}"
    confidence: {{0.0-1.0}}
decision_tree:
  - condition: "{{if_condition_1}}"
    then: "{{action_a}}"
    else: "{{action_b}}"
  - condition: "{{if_condition_2}}"
    then: "{{action_c}}"
priorities: [{{priority_1}}, {{priority_2}}, {{priority_3}}]
heuristics:
  - "{{heuristic_1}}"
  - "{{heuristic_2}}"
domain_map:
  covers: [{{domain_1}}, {{domain_2}}]
  routes_to: [{{routed_domain_1}}: {{target_agent}}]
tools_available: [{{tool_1}}, {{tool_2}}]
personality:
  tone: "{{tone_descriptor}}"
  verbosity: "{{concise|moderate|verbose}}"
  risk_tolerance: "{{low|medium|high}}"
constraints:
  - "{{constraint_1}}"
  - "{{constraint_2}}"
fallback:
  action: "{{fallback_action}}"
  escalate_to: "{{escalation_target}}"
domain: "{{primary_domain}}"
llm_function: BECOME
quality: null
tags: [mental-model, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```
## Agent Reference
{{agent_name}}: {{one_line_agent_identity}}
## Routing Rules
| Keywords | Action | Confidence |
|----------|--------|------------|
| {{kw_set_1}} | {{action_1}} | {{conf_1}} |
| {{kw_set_2}} | {{action_2}} | {{conf_2}} |
| {{kw_set_3}} | {{action_3}} | {{conf_3}} |
## Decision Tree
1. IF {{condition_1}} THEN {{action_a}} ELSE {{action_b}}
2. IF {{condition_2}} THEN {{action_c}}
## Priorities
1. {{priority_1}} (highest)
2. {{priority_2}}
3. {{priority_3}} (lowest)
## Heuristics
- {{heuristic_1}}
- {{heuristic_2}}
## Domain Map
Covers: {{domain_list}}
Routes away: {{routed_domains_with_targets}}
## References
- Source agent: {{agent_definition_path}}
- Builder: mental-model-builder v1.0.0

### bld_architecture_mental_model.md
---
kind: architecture
id: bld_architecture_mental_model
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of mental_model — inventory, dependencies, and architectural position
---

# Architecture: mental_model in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 23-field metadata header (id, kind, pillar, domain, target_agent, etc.) | mental-model-builder | active |
| routing_rules | Keyword-to-action mappings with confidence thresholds | author | active |
| decision_trees | If/then/else branching logic for complex routing decisions | author | active |
| priorities | Ordered list of objectives the agent optimizes for | author | active |
| heuristics | Rules of thumb for ambiguous situations without clear routing | author | active |
| domain_map | Boundaries defining what the agent knows and does not know | author | active |
| personality_traits | Behavioral tendencies that shape tone and approach | author | active |
## Dependency Graph
```
knowledge_card  --produces-->  mental_model  --consumed_by-->  agent
domain_context  --produces-->  mental_model  --referenced_by-> router
mental_model    --signals-->   routing_decision
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card (P01) | mental_model | data_flow | domain facts informing routing rules and heuristics |
| context_doc (P01) | mental_model | data_flow | domain context shaping boundary definitions |
| mental_model | agent (P02) | consumes | agent loads mental model as cognitive operating system |
| mental_model | router (P02) | data_flow | routing rules referenced by dispatch logic |
| mental_model | routing_decision | produces | specific route selected for incoming task |
| system_prompt (P03) | mental_model | dependency | system prompt identity constrains mental model scope |
## Boundary Table
| mental_model IS | mental_model IS NOT |
|-----------------|---------------------|
| A design-time cognitive map with routing and decisions | A runtime-accumulated state (runtime_state P10) |
| Defines how an agent routes, prioritizes, and decides | An agent identity with capabilities (agent P02) |
| Static until explicitly updated by author | A task-routing dispatch table (router P02) |
| Composed of rules, trees, heuristics, and domain maps | An evaluation framework with scoring (scoring_rubric P07) |
| Scoped to one agent or one domain | A universal routing system for all agents |
| Declared personality traits, not emergent behavior | A learned behavioral pattern (learning_record P10) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Context | knowledge_card, context_doc, system_prompt | Supply domain knowledge and identity constraints |
| Routing | routing_rules, decision_trees | Define how tasks are classified and directed |
| Judgment | priorities, heuristics | Guide decisions when routing rules are ambiguous |
| Identity | domain_map, personality_traits | Scope boundaries and behavioral tendencies |
| Output | routing_decision, agent | Produce routing decisions consumed by the agent |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `mental-model-builder` for pipeline function `INJECT`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
