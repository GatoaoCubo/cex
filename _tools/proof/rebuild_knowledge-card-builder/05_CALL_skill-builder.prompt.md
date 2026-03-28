# CEX Crew Runner -- Builder Execution
**Builder**: `skill-builder`
**Function**: CALL
**Intent**: reconstroi knowledge-card-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:19.363811

## Intent Context
- **Verb**: reconstroi
- **Object**: knowledge-card-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_skill.md
---
id: skill-builder
kind: type_builder
pillar: P04
parent: null
domain: skill
llm_function: BECOME
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [kind-builder, skill, P04, specialist, phases, trigger, reusable]
---

# skill-builder
## Identity
Especialista em construir `skill` — habilidades reutilizaveis com fases estruturadas e
trigger definido. Domina lifecycle design (discover/configure/execute/validate), trigger
engineering, phase decomposition, e a fronteira exata entre skill (P04), agent (P02), e
action_prompt (P03). Produz skills densas com frontmatter completo e fases atomicas.
## Capabilities
- Analisar dominio da habilidade para decompor em fases executaveis
- Produzir skill com frontmatter completo (12 campos required + 4 optional)
- Definir trigger preciso: slash command, keyword, event, ou agent-invoked
- Distinguir user_invocable (slash command) de agent-only (programmatic call)
- Estruturar phases com input/output claros por fase
- Validar artifact contra quality gates (7 HARD + 10 SOFT)
## Routing
keywords: [skill, phases, trigger, reusable, capability, slash-command, workflow, lifecycle]
triggers: "create skill for", "build reusable capability", "define phases for", "add slash command"
## Crew Role
In a crew, I handle REUSABLE CAPABILITY DEFINITION.
I answer: "what phases does this capability execute, and when is it triggered?"
I do NOT handle: agent identity (system-prompt-builder), task prompts (action-prompt-builder),
MCP servers (mcp-server-builder), hooks (hook is P04 but event-driven, not phase-based).

### bld_instruction_skill.md
---
id: p03_ins_skill_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Skill Builder Instructions
target: skill-builder agent
phases_count: 4
prerequisites:
  - Capability name is defined (non-empty string, kebab-case)
  - Invocation pattern is known (slash command, keyword, event, or agent-invoked)
  - At least two distinct execution phases can be identified
  - Input and output for the skill are described
validation_method: checklist
domain: skill
quality: null
tags: [instruction, skill, phases, reusable, P04]
idempotent: true
atomic: false
rollback: Delete generated skill artifact and restart from Phase 1
dependencies: []
logging: true
tldr: Build a reusable skill artifact with a precise trigger, 2-6 atomic phases each with explicit input/output, and when-to-use contrast.
density_score: 0.90
---

## Context
The skill-builder produces `skill` artifacts — reusable capabilities defined as ordered
phases with a trigger that activates them. A skill encapsulates a repeatable process:
it has a clear entry point (trigger), a structured execution path (phases), and a defined
output. Skills are distinct from agents (which have identity) and action prompts (which are
single-turn instructions).
**Input contract**:
- `{{skill_name}}`: kebab-case capability name (e.g. `web-search`, `code-review`)
- `{{trigger_type}}`: one of `slash_command`, `keyword`, `event`, `agent-invoked`
- `{{trigger_value}}`: the exact trigger string (e.g. `/search`, `"review this"`, `on_deploy`)
- `{{user_invocable}}`: boolean — can a human trigger this directly?
- `{{phases_raw}}`: comma-separated phase names or free-text describing the process
- `{{input_description}}`: what the skill receives
- `{{output_description}}`: what the skill produces
**Output contract**: A single `skill` Markdown file with YAML frontmatter, 2-6 atomic
phases each with Input/Action/Output blocks, when_to_use and when_not_to_use lists,
concrete invocation examples, anti-patterns section, and metrics section.
**Boundaries**:
- Skill handles reusable phase-based capabilities only.
- Agent identity (who the agent IS) belongs in a system-prompt artifact.
- Single-turn task instructions belong in an action_prompt artifact.
- Event-driven hooks (triggered by file/tool events) are a separate hook artifact.
- MCP server tool exposure belongs in an mcp_server artifact.
## Phases
### Phase 1: Analyze Capability and Trigger
**Primary action**: Understand the capability's domain, decompose it into executable
phases, and define the precise trigger.
```
INPUT: skill_name, trigger_type, trigger_value, user_invocable, phases_raw
1. Validate skill_name:
   Must be kebab-case, lowercase: ^[a-z][a-z0-9-]+$
   Derive id: p04_skill_{{skill_name_with_underscores}}
2. Classify the capability domain:
   domain_type = "data" | "code" | "communication" | "analysis" | "orchestration"
3. Trigger specification:
   trigger = {
     type: {{trigger_type}},
     value: {{trigger_value}},
     user_invocable: {{user_invocable}},
     description: one sentence — "Activates when [condition]"
   }
   Trigger precision rules:
     slash_command: must start with "/" and be unique in the system
     keyword:       must be specific enough to not trigger accidentally
     event:         must be an observable system event (not a vague condition)
     agent-invoked: must name the calling agent and the invocation condition
4. Phase decomposition from phases_raw:
   phase_list = parse phases_raw into named phases (2-6 required)
   for each phase:
     phase_entry = {
       name: short verb phrase (e.g. "Discover", "Configure", "Execute", "Validate"),
       position: integer (1-based),
       atomic: true  # each phase does ONE primary action
     }
   Validate atomicity: if a phase does two distinct things, split it.
   Validate sequence: phases must be ordered (each builds on previous output).
OUTPUT: validated_id, domain_type, trigger{}, phase_list[] (2-6 phases, atomic)
```
Verification: `phase_list` has 2-6 entries. Each phase has a single primary action.
Trigger value is specific and unambiguous.
### Phase 2: Define Phase Input/Output
**Primary action**: For each phase, write explicit Input, Action, and Output blocks
that make the data flow unambiguous.
```
INPUT: phase_list[], input_description, output_description
1. Map data flow across phases:
   Phase 1 Input  = skill's overall {{input_description}}
   Phase N Output = Phase N+1 Input (chaining)
   Last Phase Output = skill's overall {{output_description}}
2. For each phase in phase_list:
   phase_spec = {
     name: phase.name,
     input: what data this phase receives (concrete, not vague),
     action: the single primary action (imperative verb phrase),
     output: what data this phase produces (concrete, not vague),
     tools: list of tools/commands used (empty list if none)
   }
   Action verb rules:
     Use active imperative: "Search for...", "Parse...", "Write..."
     Do NOT use: "Handle", "Process", "Deal with" (too vague)
3. Validate phase chain continuity:
   for each consecutive pair (phase_N, phase_N+1):
     if phase_N.output does not match phase_N+1.input:
       add an explicit transformation note between phases
4. Identify sub-skills this skill may delegate to:
   sub_skills = [] (list any existing skills this skill calls)
OUTPUT: phase_specs[] with input/action/output for each, sub_skills[]
```
Verification: every phase has non-empty input, action, and output. Output of phase N
is compatible with input of phase N+1.
### Phase 3: Write Usage Guidance and Examples
**Primary action**: Produce the when_to_use and when_not_to_use lists, at least 3
concrete invocation examples, anti-patterns, and metrics.
```
INPUT: trigger{}, phase_specs[], domain_type, skill_name
1. when_to_use (list of conditions, parallel grammatical structure):
   - At least 3 concrete conditions
   - Each condition is observable (not "when you feel like it")
   - Pattern: "When [observable condition]..."
2. when_not_to_use (list of exclusions, same abstraction level):
   - At least 3 exclusions

### bld_knowledge_card_skill.md
---
kind: knowledge_card
id: bld_knowledge_card_skill
pillar: P04
llm_function: INJECT
purpose: Domain knowledge for skill production — atomic searchable facts
sources: skill-builder MANIFEST.md + SCHEMA.md
---

# Domain Knowledge: skill
## Executive Summary
Skills are reusable, phase-structured capabilities with a defined trigger — the bridge between a raw LLM and a repeatable workflow. Each skill has an ordered phase list (discover/configure/execute/validate) and a precise invocation pattern. Unlike agents (which carry identity/persona) or action_prompts (single-shot task text), skills are stateless capability definitions with no "You are" language and no task instructions.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 |
| Format | YAML (frontmatter) + Markdown (body) |
| Naming | `p04_skill_{name}.md` + `.yaml` |
| ID regex | `^p04_skill_[a-z][a-z0-9_]+$` |
| Max body bytes | 5120 |
| Required frontmatter fields | 16 |
| Optional frontmatter fields | 4: references_dir, sub_skills, platforms, stack_default |
| Quality gates | 7 HARD + 10 SOFT |
| description max | 120 characters |
| Minimum phases | 2 |
| Maximum phases | 6 |
| quality field | null always — invariant |
## Patterns
| Pattern | Rule |
|---------|------|
| Phase alignment | `phases` list in frontmatter MUST match `## Workflow Phases` subsections in body (1:1) |
| Slash command trigger | `user_invocable: true` REQUIRES trigger to start with `/` |
| Agent-invoked trigger | `user_invocable: false` + keyword or event trigger (no slash) |
| No persona | Skills NEVER contain "You are" — capability only, not identity |
| Parallel lists | `when_to_use` and `when_not_to_use` MUST be at the same abstraction level |
| id == filename stem | `p04_skill_deploy.md` → `id: p04_skill_deploy` |
| Sub-skills | Delegate to other skill IDs via `sub_skills` list; never re-implement inline |
| Canonical phases | discover → configure → execute → validate |
- **Body sections**: Purpose → Workflow Phases → Anti-Patterns → Metrics
- **Per-phase structure**: input / action / output clearly named
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| "You are an expert…" in skill body | Skills have no persona; identity belongs in system_prompt |
| phases list mismatched to body subsections | Hard gate failure; names must be 1:1 with body |
| `user_invocable: true` with non-slash trigger | Schema violation; slash command required for user-invocable |
| Single monolithic phase | Loses phase contract; minimum 2 distinct phases with named boundaries |
| Missing `when_not_to_use` | Routing ambiguity; consumers cannot exclude skill correctly |
| Task instructions embedded in skill | Skill defines capability shape, not execution content |
| God skill (8+ unrelated actions) | Split into focused sub_skills |
## Application
1. Define the single reusable capability domain
2. Decompose into 2–6 ordered phases (minimum: execute + validate)
3. Write frontmatter: all 16 required fields, set `user_invocable` and `trigger` correctly
4. If `user_invocable: true`, set trigger to `/skill-name` slash command
5. Write body: Purpose → one `###` subsection per phase (input/action/output) → Anti-Patterns → Metrics
6. Verify `phases` list matches body subsection names exactly
7. Set `quality: null`
8. Check body ≤ 5120 bytes
## References
- Schema: skill SCHEMA.md (P06)
- Pillar: P04 (skills + hooks)
- Boundary: system_prompt (identity), action_prompt (single-shot task), hook (event-driven, not phase-based)

### bld_quality_gate_skill.md
---
id: p11_qg_skill
kind: quality_gate
pillar: P11
title: "Gate: Skill"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: skill
quality: null
density_score: 0.85
tags:
  - quality-gate
  - skill
  - reusable-capability
  - p11
tldr: "Gates ensuring skill files define a specific trigger, two or more typed workflow phases, and phase-level error handling without claiming agent identity."
---

## Definition
A skill is a reusable capability: a named sequence of phases that can be invoked by a trigger and composed with other skills. A skill passes this gate when the trigger is specific enough to avoid false activations, each phase has typed input and output, error handling is defined at the phase level (not just globally), and the skill makes no claims about being an agent — it is a procedure, not an identity.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`skill-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `skill` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains a **Trigger definition** (slash command name, keyword pattern, or event type that activates the skill) | Without a trigger, the skill cannot be invoked programmatically or by convention |
| H08 | Spec contains >= 2 **Workflow Phases** (each phase is a named step in the execution sequence) | A single-phase skill is a function, not a skill; phased structure enables partial retry and composition |
| H09 | Spec contains **Input and Output** per phase (field names and types, not just prose descriptions) | Typed per-phase I/O is the contract that enables composition with other skills |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Trigger is specific not generic (trigger will not fire on unrelated inputs) | 1.0 | Generic keyword like "do" or "run" | Moderately specific | Exact slash command or narrow keyword pattern with exclusion rules |
| 3 | Phases have clear boundaries (entry condition, exit condition, and handoff artifact per phase) | 1.0 | Phases blend together | Start/end noted | Explicit entry condition, exit condition, and handoff artifact per phase |
| 4 | Input/output typed per phase (not just final output typed) | 1.0 | Only final output typed | Partial typing | Every phase has named fields with types for both input and output |
| 5 | user_invocable flag correct (`true` if user can trigger it, `false` if internal-only) | 0.5 | Missing | Present but unchecked | Present and verified against trigger type |
| 6 | Tags include `skill` | 0.5 | Missing | Present but misspelled | Exactly `skill` in tags list |
| 7 | Error handling per phase (each phase has its own error class, retry rule, and fallback) | 1.0 | No error handling | Global handler only | Each phase has error class, retry rule, and fallback |
| 8 | Phase dependencies documented (which phases must complete before the next; parallel-eligible phases noted) | 1.0 | No dependencies stated | Sequential assumed | Explicit dependency graph including any parallel-eligible phases |

### bld_schema_skill.md
---
kind: schema
id: bld_schema_skill
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for skill
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: skill
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_skill_{name}) | YES | - | Namespace compliance |
| kind | literal "skill" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable skill name |
| description | string <= 120ch | YES | - | One-line capability summary |
| user_invocable | boolean | YES | false | True = slash command available |
| trigger | string | YES | - | Exact invocation pattern |
| phases | list[string] | YES | - | Ordered phase names |
| when_to_use | list[string] | YES | - | Conditions favoring this skill |
| when_not_to_use | list[string] | YES | - | Conditions excluding this skill |
| examples | list[string] | YES | - | 2+ concrete invocation examples |
| quality | null | YES | null | Never self-score |
| references_dir | string | NO | - | Path to related artifacts |
| sub_skills | list[string] | NO | - | Skill IDs this skill delegates to |
| platforms | list[string] | NO | - | OS/runtime constraints |
| stack_default | string | NO | - | Default stack/runtime |
## ID Pattern
Regex: `^p04_skill_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Purpose` — what capability this skill provides and why it exists
2. `## Workflow Phases` — one subsection per phase with input/output/action
3. `## Anti-Patterns` — named failures and how to avoid them
4. `## Metrics` — measurable success criteria for this skill
## Constraints
- max_bytes: 5120 (body only)
- naming: p04_skill_{name}.md + .yaml
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- phases list MUST match ## Workflow Phases subsections in body
- user_invocable: true REQUIRES trigger to be a slash command pattern (/name)
- quality: null always
- skill has NO identity/persona — capability only, no "You are" statements
- when_to_use and when_not_to_use MUST be parallel (same abstraction level)

### bld_examples_skill.md
---
kind: examples
id: bld_examples_skill
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of skill artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: skill-builder
## Golden Example
INPUT: "Create skill for committing and pushing git changes"
OUTPUT:
```yaml
id: p04_skill_git_commit
kind: skill
pillar: P04
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
name: "Git Commit and Push"
description: "Stage, commit, and push changes with message validation and branch safety"
user_invocable: true
trigger: "/commit"
phases:
  - "discover"
  - "configure"
  - "execute"
  - "validate"
when_to_use:
  - "Changes are ready and tests pass"
  - "Agent has completed a task and must persist output"
  - "User explicitly requests a commit"
when_not_to_use:
  - "Changes are untested or partial"
  - "Branch is main/master and force-push would be required"
  - "No meaningful changes exist (empty diff)"
examples:
  - "/commit"
  - "/commit -m 'feat: add deploy skill'"
  - "agent invokes after completing build task"
quality: null
references_dir: "records/skills/git_commit/"
sub_skills: []
platforms: ["linux", "macos", "windows"]
stack_default: "git"
```
## Purpose
Provides a safe, validated git commit-and-push workflow reusable across agents and users.
Exists as a skill (not action_prompt) because it has multi-phase lifecycle with validation
and is invoked in dozens of different agent contexts.
## Workflow Phases
### Phase 1: discover
**Input**: working directory, optional commit message flag
**Action**: run `git status` and `git diff` to inspect staged/unstaged changes
**Output**: change summary, list of modified files, current branch name
### Phase 2: configure
**Input**: change summary, branch name, optional -m flag
**Action**: validate branch not protected, draft commit message if not provided, check for secrets in diff
**Output**: validated commit message, confirmed safe branch, staged file list
### Phase 3: execute
**Input**: validated commit message, staged file list
**Action**: run `git add` for specific files, run `git commit -m`, run `git push`
**Output**: commit SHA, push confirmation, remote URL
### Phase 4: validate
**Input**: commit SHA, push output
**Action**: verify commit appears in `git log`, verify remote reflects push
**Output**: success signal with SHA, or error signal with failure reason
## Anti-Patterns
- **Blanket add**: `git add -A` or `git add .` without reviewing files — may include secrets or binaries
- **Force push to main**: never use `--force` on protected branches — check branch name first
- **Silent failure**: swallowing push errors without signaling — always emit error signal on failure
## Metrics
- Commit success rate: >= 98% of invocations result in committed SHA
- Secret leak rate: 0% (configure phase must detect secrets before execute)
- Phase duration: discover < 2s, configure < 1s, execute < 5s, validate < 2s
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_skill_ pattern (H02 pass)
- kind: skill (H04 pass)
- 19 required+optional fields present (H06 pass)
- body has Purpose + Workflow Phases + Anti-Patterns + Metrics (H07 pass)
- phases list matches 4 body subsections exactly (H08 pass)
- user_invocable: true with trigger "/commit" (S03 pass)
- when_to_use and when_not_to_use parallel structure (S04 pass)
- No identity language in body (S05 pass)
- 3 anti-patterns named with avoidance (S06 pass)
- 3 metrics with measurable targets (S07 pass)
- description <= 120 chars (S01 pass)
## Anti-Example
INPUT: "Create skill for deploying code"
BAD OUTPUT:
```yaml
id: deploy_skill
kind: tool
pillar: tools
name: Deploy
trigger: deploy
quality: 8.0
```
You are a deploy specialist. You deploy code to production.
Run the deploy command when asked.
FAILURES:
1. id: no `p04_skill_` prefix, uses hyphen — H02 FAIL
2. kind: "tool" not "skill" — H04 FAIL
3. pillar: "tools" not "P04" — H06 FAIL
4. quality: 8.0 (not null) — H05 FAIL

### bld_config_skill.md
---
kind: config
id: bld_config_skill
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: skill Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_skill_{name}.md` | `p04_skill_git_commit.md` |
| Compiled YAML | `p04_skill_{name}.yaml` | `p04_skill_git_commit.yaml` |
| Builder directory | kebab-case | `skill-builder/` |
| Frontmatter fields | snake_case | `user_invocable`, `when_to_use` |
| Skill name slug | snake_case, lowercase | `git_commit`, `deploy_railway` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P04_tools/examples/p04_skill_{name}.md`
- Compiled: `cex/P04_tools/compiled/p04_skill_{name}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 5120 bytes
- Total (frontmatter + body): ~6500 bytes
- Density: >= 0.80
## Phase Count
| Count | Status | Notes |
|-------|--------|-------|
| 1 | INVALID | Single-phase is an action_prompt, not a skill |
| 2-3 | MINIMAL | Acceptable for simple capabilities |
| 4 | CANONICAL | discover + configure + execute + validate |
| 5-6 | EXTENDED | Valid for complex skills with sub-phases |
| 7+ | REJECT | Split into sub_skills |
## Trigger Convention
| Type | Format | user_invocable |
|------|--------|---------------|
| Slash command | `/verb` or `/verb-noun` | true |
| Keyword | `"keyword phrase"` | false |
| Event | `on_{event_name}` | false |
| Agent call | `skill:{id}` | false |
## Boolean Fields
- user_invocable: true ONLY when trigger is a slash command starting with `/`
- user_invocable: false for all agent-only, event-driven, or keyword triggers
## Body Section Requirements
- Purpose: 2-4 sentences, must state WHY skill exists vs action_prompt
- Workflow Phases: one ### subsection per phase, each with Input/Action/Output
- Anti-Patterns: >= 3 named failures with avoidance strategy
- Metrics: >= 2 measurable success criteria with target values

### bld_output_template_skill.md
---
kind: output_template
id: bld_output_template_skill
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a skill
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: skill
```yaml
id: p04_skill_{{name}}
kind: skill
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_name}}"
description: "{{one_line_capability_max_120ch}}"
user_invocable: {{true|false}}
trigger: "{{slash_command_or_keyword_or_event}}"
phases:
  - "{{phase_1_name}}"
  - "{{phase_2_name}}"
  - "{{phase_3_name}}"
when_to_use:
  - "{{condition_1}}"
  - "{{condition_2}}"
when_not_to_use:
  - "{{exclusion_1}}"
  - "{{exclusion_2}}"
examples:
  - "{{invocation_example_1}}"
  - "{{invocation_example_2}}"
quality: null
references_dir: "{{optional_path_or_omit}}"
sub_skills: ["{{optional_skill_id_or_omit}}"]
platforms: ["{{optional_platform_or_omit}}"]
stack_default: "{{optional_stack_or_omit}}"
```
## Purpose
{{what_capability_this_provides}}
{{why_it_exists_as_a_skill_not_agent_or_prompt}}
## Workflow Phases
### Phase 1: {{phase_1_name}}
**Input**: {{what_phase_1_receives}}
**Action**: {{what_phase_1_does}}
**Output**: {{what_phase_1_produces}}
### Phase 2: {{phase_2_name}}
**Input**: {{what_phase_2_receives}}
**Action**: {{what_phase_2_does}}
**Output**: {{what_phase_2_produces}}
### Phase 3: {{phase_3_name}}
**Input**: {{what_phase_3_receives}}
**Action**: {{what_phase_3_does}}
**Output**: {{what_phase_3_produces}}
## Anti-Patterns
- **{{anti_pattern_1_name}}**: {{what_goes_wrong}} — {{how_to_avoid}}
- **{{anti_pattern_2_name}}**: {{what_goes_wrong}} — {{how_to_avoid}}
- **{{anti_pattern_3_name}}**: {{what_goes_wrong}} — {{how_to_avoid}}
## Metrics
- {{metric_1}}: {{target_value}}
- {{metric_2}}: {{target_value}}
- {{metric_3}}: {{target_value}}

### bld_architecture_skill.md
---
kind: architecture
id: bld_architecture_skill
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of skill — inventory, dependencies, and architectural position
---

# Architecture: skill in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, trigger, phases_count, etc.) | skill-builder | active |
| trigger_definition | What activates the skill (slash command, keyword, event, or programmatic call) | author | active |
| phase_list | Ordered execution phases with input/output per phase | author | active |
| input_contract | Typed specification of what the skill receives at invocation | author | active |
| output_contract | Typed specification of what the skill produces on completion | author | active |
| user_invocable_flag | Whether the skill is triggered by user (slash command) or agent-only | author | active |
## Dependency Graph
```
agent           --invokes-->    skill  --produces-->     skill_output
trigger_event   --activates-->  skill  --signals-->      completion_signal
skill           --depends-->    knowledge_card
```
| From | To | Type | Data |
|------|----|------|------|
| agent (P02) | skill | consumes | agent invokes skill for reusable capability |
| trigger_event | skill | data_flow | event or command that activates the skill |
| skill | skill_output | produces | structured result from phase execution |
| skill | completion_signal (P12) | signals | emitted when all phases complete |
| knowledge_card (P01) | skill | dependency | domain knowledge injected into skill phases |
| action_prompt (P03) | skill | dependency | individual phases may use action prompts |
## Boundary Table
| skill IS | skill IS NOT |
|----------|--------------|
| A reusable capability with structured phases and trigger | An agent identity with persona and rules (system_prompt P03) |
| Triggered by slash command, keyword, event, or API call | A one-time task prompt (action_prompt P03) |
| Multi-phase with defined input/output per phase | An event interceptor without phases (hook P04) |
| User-invocable or agent-only based on flag | A protocol server exposing tools (mcp_server P04) |
| Produces structured output on completion | A pluggable extension with lifecycle hooks (plugin P04) |
| Scoped to one capability domain | A multi-satellite orchestration (workflow P12) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Trigger | trigger_definition, user_invocable_flag | Define how and by whom the skill is activated |
| Contract | frontmatter, input_contract, output_contract | Specify typed I/O for the skill |
| Execution | phase_list, action_prompt | Ordered phases with per-phase input/output |
| Context | knowledge_card | Domain knowledge supporting phase execution |
| Output | skill_output, completion_signal | Deliver result and signal completion |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `skill-builder` for pipeline function `CALL`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
