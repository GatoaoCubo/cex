# CEX Crew Runner -- Builder Execution
**Builder**: `handoff-builder`
**Function**: COLLABORATE
**Intent**: reconstroi quality-gate-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:19.037811

## Intent Context
- **Verb**: reconstroi
- **Object**: quality-gate-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_handoff.md
---
id: handoff-builder
kind: type_builder
pillar: P12
domain: handoff
llm_function: COLLABORATE
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: CODEX
parent: null
tags: [kind-builder, handoff, P12, orchestration, specialist]
---

# handoff-builder
## Identity
Especialista em construir `handoff` de P12: instrucoes completas de delegacao
que empacotam tarefa, contexto, escopo e regras de commit para satelites executarem.
## Capabilities
- Produzir handoff markdown com campos obrigatorios e naming P12 corretos
- Distinguir handoff de action_prompt, signal e dispatch_rule sem sobreposicao
- Modelar scope fence com paths permitidos e proibidos
- Validar handoffs contra gates duros de completude, escopo e tamanho
## Routing
keywords: [handoff, delegation, dispatch, task, context, scope_fence, commit]
triggers: "delega tarefa para satelite", "cria instrucao de handoff", "prepara execucao remota"
## Crew Role
In a crew, I handle TASK DELEGATION PACKAGING.
I answer: "what should the satellite do, with what context, and how should it commit?"
I do NOT handle: status reporting, dependency graphs, routing policy, execution runtime.

### bld_instruction_handoff.md
---
kind: instruction
id: bld_instruction_handoff
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for handoff
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a handoff
## Phase 1: RESEARCH
1. Identify the task to delegate — what work needs to be done and what is the concrete deliverable?
2. Determine the target executor — which satellite or agent will carry out this work?
3. Define required context — what background does the executor need to understand why this task matters?
4. Scope the deliverable — what exactly should be produced, to what quality threshold, by when?
5. Identify scope fence — which file paths and directories are allowed, and which are strictly forbidden?
6. Determine commit convention — what git add pattern and commit message format should the executor use?
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all required fields
2. Read OUTPUT_TEMPLATE.md — use exact template structure
3. Set filename as `p12_ho_{task_slug}.md`
4. Fill frontmatter: all required fields, quality: null (never self-score)
5. Write Context section: background and motivation — why this task exists and what it unblocks
6. Write Task section: clear deliverable description with acceptance criteria — specific enough for autonomous execution without clarification
7. Write Seeds section: 5 to 10 domain keywords the executor can use for context retrieval
8. Write Scope Fence section: allowed paths (SOMENTE) and forbidden paths (NAO TOQUE) as explicit lists
9. Write Commit Convention section: exact git add pattern and commit message format
10. Write Signal section: the completion notification mechanism the executor must trigger when done
11. Check body size — must stay at or below 3072 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — run all HARD gates manually
2. HARD gates:
   - [ ] id matches `p12_ho_[a-z][a-z0-9_]+`
   - [ ] kind == `handoff`
   - [ ] quality == null
   - [ ] context section present
   - [ ] task has acceptance criteria
   - [ ] scope fence has both allowed and forbidden paths
   - [ ] body <= 3072 bytes
3. SOFT gates: seeds list has 5+ keywords, commit convention specified, signal mechanism defined
4. Cross-check: delegation package not execution recipe (that is instruction)? Not a status event (that is signal)? Not a routing policy (that is dispatch_rule)? Task is clear enough for autonomous execution without back-and-forth?
5. If score < 8.0: revise in the same pass before outputting

### bld_knowledge_card_handoff.md
---
kind: knowledge_card
id: bld_knowledge_card_handoff
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for handoff production — task delegation packaging
sources: orchestration patterns, delegation protocols, mission briefing design
---

# Domain Knowledge: handoff
## Executive Summary
Handoffs are self-contained delegation packages that tell a satellite WHAT to do, with what context, within what scope, and how to commit and signal completion. They are instructions consumed by execution engines — not events (signals), not routing policies (dispatch rules), and not runtime orchestration (workflows). A handoff must be self-contained: the satellite needs no external context.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P12 (orchestration) |
| llm_function | COLLABORATE |
| Max size | 4096 bytes |
| Naming | p12_ho_{task}.md |
| Required body sections | Context, Tasks, Scope Fence, Commit, Signal |
| Autonomy levels | full, supervised, assisted |
| Key fields | satellite, mission, autonomy, quality_target |
## Patterns
- **Autonomy levels**: define how independently the satellite operates
| Level | Behavior | Use case |
|-------|----------|----------|
| full | Satellite decides all implementation details | Trusted, well-defined tasks |
| supervised | Checks back on key decisions | Complex tasks with trade-offs |
| assisted | Follows precise instructions, minimal deviation | Critical or risky tasks |
- **Five body sections**: each serves a specific purpose
| Section | Content | Rule |
|---------|---------|------|
| Context | WHY this work is needed | 2-4 sentences, motivation only |
| Tasks | WHAT to do | Numbered steps, action verbs |
| Scope Fence | WHERE allowed/forbidden | SOMENTE + NAO TOQUE paths |
| Commit | HOW to save work | Exact git add + commit commands |
| Signal | HOW to report completion | Signal writer call or file |
- **Self-contained**: satellite needs no external context — everything is in the handoff
- **Scope fence**: explicitly lists allowed paths AND forbidden paths — prevents satellite from touching wrong files
- **Action verb tasks**: every task starts with an action verb (create, read, validate, write)
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague tasks ("do your best") | Satellite has no clear objective |
| Missing scope fence | Satellite modifies wrong files |
| External context required | Satellite fails when context unavailable |
| No commit section | Work done but not saved; lost on session end |
| No signal section | Orchestrator cannot detect completion |
| Over 4096 bytes | Too complex; split into multiple handoffs |
## Application
1. Define mission and satellite assignment
2. Write context: 2-4 sentences on WHY this work is needed
3. List tasks: numbered, action-verb-first, specific deliverables
4. Set scope fence: SOMENTE (allowed) + NAO TOQUE (forbidden) paths
5. Write commit: exact git commands for saving work
6. Write signal: completion notification mechanism
## References
- Military briefing: OPORD (Operations Order) structure
- Agile: user story + acceptance criteria delegation pattern
- Orchestration: task delegation and completion signaling protocols
- CI/CD: pipeline stage handoff and artifact passing

### bld_quality_gate_handoff.md
---
id: p11_qg_handoff
kind: quality_gate
pillar: P11
title: "Gate: Handoff"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: "handoff — task delegation packages for satellite execution"
quality: null
tags: [quality-gate, handoff, delegation, orchestration, scope-fence]
tldr: "Gates ensuring handoff artifacts carry complete delegation context: task, scope fence, commit instructions, and size discipline."
density_score: 0.88
---

# Gate: Handoff
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: handoff` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | Uppercase, spaces, or leading digit |
| H03 | ID equals filename stem | `id: deploy_api` in file `setup.md` |
| H04 | Kind equals literal `handoff` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All required fields present | Missing: task, context, scope_fence, commit, or signal |
| H07 | `scope_fence` contains both `allowed` and `prohibited` keys | Missing either key or both empty |
| H08 | `task` section has at least one numbered step | Narrative blob with no steps |
| H09 | `commit` section contains a valid git command | Section present but no `git commit` instruction |
| H10 | Body size <= 4096 bytes | Exceeds limit — handoff too verbose |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Task decomposition | 1.0 | Steps are atomic and independently verifiable | Steps exist but some are compound | Single block of instructions |
| S02 | Context completeness | 1.0 | Background, motivation, and prior state all present | Partial context (2/3) | Context absent |
| S03 | Scope fence precision | 1.0 | Exact paths listed in both allowed and prohibited | Paths listed for one side only | Vague scope description |
| S04 | Commit instruction quality | 0.5 | Stage command + message template + signal command present | Only commit message present | No commit guidance |
| S05 | Signal instruction | 0.5 | Signal call with satellite, status, and score specified | Signal mentioned without params | Signal absent |
| S06 | Step ordering | 1.0 | Dependencies between steps are explicit | Steps ordered but implicit deps | Steps unordered |
| S07 | Open variable marking | 0.5 | All decision points marked `[OPEN_VARIABLE]` | Some decision points unmarked | No open variables marked |
| S08 | Size discipline | 1.0 | Body 1000-3000 bytes (dense, complete) | Body 3001-4096 bytes (verbose) | Body < 500 bytes (too sparse) |
| S09 | Autonomy framing | 0.5 | Explicit autonomy flag + quality target stated | Quality target stated without autonomy flag | Neither present |
| S10 | Retry/resilience guidance | 0.5 | Error handling or retry instructions included | Partial guidance | None |
| S11 | Naming convention | 0.5 | Filename follows `{MISSION}_{sat}.md` pattern | Filename partially correct | Arbitrary filename |
| S12 | No internal jargon leaked | 0.5 | No framework internals or unexplained acronyms | Minor internal refs | Heavy framework coupling |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to pool as golden handoff template |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Time-critical incident response where full context is not yet known |
| Approver | Senior orchestrator (human) only |

### bld_schema_handoff.md
---
kind: schema
id: bld_schema_handoff
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for handoff - SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
---

# Schema: handoff
## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P12` |
| Type | literal `handoff` |
| Machine format | `yaml` (frontmatter) + `md` (body) |
| Naming | `p12_ho_{task}.md` |
| Max bytes | 4096 |
## Required Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (`p12_ho_{slug}`) | YES | - | Unique handoff identifier |
| kind | literal "handoff" | YES | - | Type integrity |
| lp | literal "P12" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| satellite | string | YES | - | Target executor (lowercase slug) |
| mission | string | YES | - | Mission or project name |
| autonomy | enum (`full`, `supervised`, `assisted`) | YES | - | Execution autonomy level |
| quality_target | number 0.0-10.0 | YES | - | Minimum quality threshold |
| domain | string | YES | - | Domain this artifact belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Searchability |
| tldr | string <= 160ch | YES | - | Dense summary |
## Optional Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| dependencies | list[string] | NO | omitted | Handoffs or artifacts that must complete first |
| seeds | list[string] | NO | omitted | Seed words for context hydration |
| agent | string | NO | omitted | Specific agent to load before execution |
| skill | string | NO | omitted | Specific skill to follow during execution |
| batch | string | NO | omitted | Batch identifier for continuous batching |
| wave | integer | NO | omitted | Wave number in multi-wave execution |
| keywords | list[string] | NO | omitted | Brain search terms |
| linked_artifacts | object {primary, related} | NO | omitted | Cross-references |
## Body Structure (required sections)
1. `## Context` — why this work is needed and relevant background
2. `## Tasks` — numbered list of specific actions to perform
3. `## Scope Fence` — paths allowed (SOMENTE) and forbidden (NAO TOQUE)
4. `## Commit` — exact git commands for committing deliverables
5. `## Signal` — how to signal completion (signal_writer or file)
## Semantic Rules
1. One handoff delegates one coherent unit of work to one satellite
2. Tasks must be specific and actionable, not vague
3. Scope fence must explicitly list allowed and forbidden paths
4. Commit section must include exact git add and commit commands
5. Signal section must reference signal_writer or a completion file
6. Autonomy level governs how much the satellite can decide independently
## Boundary Rules
`handoff` IS:
- complete delegation instruction for a satellite
- packaged context + tasks + scope + commit rules
- one-shot execution brief
`handoff` IS NOT:
- `action_prompt`: no persona, no system rules, no response format constraints
- `signal`: no status event, no quality score, no timestamp-only data
- `dispatch_rule`: no keyword routing table, no satellite selection policy
- `workflow`: no step graph, no error handling, no runtime state
- `dag`: no dependency graph structure, no topological ordering
- `crew`: no multi-agent coordination protocol
## ID Pattern
Regex: `^p12_ho_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Constraints
- max_bytes: 4096
- naming: `p12_ho_{task}.md`
- id == filename stem
- Must have all 5 body sections
- Scope fence must list both SOMENTE and NAO TOQUE

### bld_examples_handoff.md
---
kind: examples
id: bld_examples_handoff
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of handoff artifacts
pattern: few-shot learning for delegation instruction packaging
---

# Examples: handoff-builder
## Golden Example
INPUT: "Create handoff for edison to build 3 archetype builders in wave 19"
OUTPUT (`p12_ho_wave19_builders.md`):
```yaml
id: p12_ho_wave19_builders
kind: handoff
lp: P12
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "stella"
satellite: "edison"
mission: "wave19"
autonomy: "full"
quality_target: 9.0
domain: "orchestration"
quality: null
tags: [handoff, edison, wave19, builders, archetype]
tldr: "Edison builds 3 archetype builders (session-state, dag, handoff) with 13 ISO each"
dependencies: []
seeds: [builder, archetype, session_state, dag, handoff, P10, P12]
agent: "builder-builder"
batch: "batch_06"
wave: 19
keywords: [wave19, builders, archetype, edison]
linked_artifacts:
  primary: "archetypes/builders/"
  related: ["archetypes/builders/_builder-builder/", "archetypes/SEED_BANK.yaml"]
```
# EDISON — WAVE19: Build 3 Builders
**Full Autonomy** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**
## Context
Wave 19 requires 3 new archetype builders for types session_state (P10),
dag (P12), and handoff (P12). Each builder follows the 13-ISO pattern
established by _builder-builder. Reference builders: signal-builder, workflow-builder.
## Tasks
### Step 1: Read References
Read _builder-builder/BUILDER_NORMS.md, signal-builder/, and workflow-builder/.
### Step 2: Build session-state-builder
Create 13 ISO files in archetypes/builders/session-state-builder/.
### Step 3: Commit session-state-builder
Run: git add archetypes/builders/session-state-builder/ && git commit
### Step 4: Build dag-builder
Create 13 ISO files in archetypes/builders/dag-builder/.
### Step 5: Commit dag-builder
Run: git add archetypes/builders/dag-builder/ && git commit
### Step 6: Build handoff-builder
Create 13 ISO files in archetypes/builders/handoff-builder/.
### Step 7: Commit handoff-builder
Run: git add archetypes/builders/handoff-builder/ && git commit
## Scope Fence
- SOMENTE: archetypes/builders/session-state-builder/, archetypes/builders/dag-builder/, archetypes/builders/handoff-builder/
- NAO TOQUE: archetypes/builders/_builder-builder/, archetypes/builders/signal-builder/, P12_orchestration/_schema.yaml
## Commit
```bash
git add archetypes/builders/session-state-builder/
git commit -m "archetype: session-state-builder -- 13 ISO (P10, Wave 19)"
git add archetypes/builders/dag-builder/
git commit -m "archetype: dag-builder -- 13 ISO (P12, Wave 19)"
git add archetypes/builders/handoff-builder/
git commit -m "archetype: handoff-builder -- 13 ISO (P12, Wave 19)"
```
## Signal
```bash
python -c "from records.core.python.signal_writer import write_signal; write_signal('edison', 'complete', 9.0)"
```
WHY GOLDEN: filename `p12_ho_*`, 19+ frontmatter fields, all 5 body sections, specific tasks, SOMENTE+NAO TOQUE, exact git commands, signal mechanism, no prompt/event/routing drift.
## Anti-Example
BAD OUTPUT (`p03_ap_build_stuff.md`):
```yaml
id: p03_ap_build_stuff
kind: action_prompt
lp: P03
persona: "You are a helpful builder"
response_format: "markdown"
Build some archetype builders. Use your best judgment.
Make sure they are good quality. Commit when done.
Try to finish everything today if possible.
```
FAILURES:
1. wrong kind: `action_prompt` instead of `handoff` (H02)
2. wrong pillar: `P03` instead of `P12` (H01)
3. wrong id prefix: `p03_ap_` instead of `p12_ho_` (H01)
4. contains `persona`: prompt engineering -> action_prompt drift (H08)
5. contains `response_format`: prompt constraint -> action_prompt drift (H08)
6. missing required fields: `satellite`, `mission`, `autonomy`, `quality_target`, `quality`, `tags`, `tldr` (H03)
7. vague tasks: "Build some archetype builders" is not specific (H09)
8. no scope fence section: missing SOMENTE/NAO TOQUE (H10)
9. no commit section: missing exact git commands (H10)

### bld_config_handoff.md
---
kind: config
id: bld_config_handoff
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: handoff Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p12_ho_{task}.md` | `p12_ho_wave19_builders.md` |
| Builder directory | kebab-case | `handoff-builder/` |
| Frontmatter fields | snake_case | `quality_target`, `scope_fence` |
| Autonomy values | lowercase enum | `full`, `supervised`, `assisted` |
| Satellite values | lowercase slug | `edison`, `atlas`, `shaka` |
Rule: use `.md` (YAML frontmatter + markdown body) for handoff artifacts.
## File Paths
- Primary output: `.claude/handoffs/p12_ho_{task}.md`
- Compiled output: `P12_orchestration/compiled/p12_ho_{task}.md`
- Human reference: `P12_orchestration/examples/p12_ho_{task}.md`
## Size Limits
- Preferred handoff size: <= 3072 bytes
- Absolute max: 4096 bytes
- Tasks should be concise and specific
## Content Restrictions
- Each task step must be one specific action (no compound steps)
- Scope fence must list both SOMENTE and NAO TOQUE
- Commit section must have exact git add and commit commands
- Signal section must reference a concrete completion mechanism
## Boundary Restrictions
- No prompt persona or response format constraints (belongs in action_prompt)
- No status events or quality scores (belongs in signal)
- No keyword routing tables (belongs in dispatch_rule)
- No step graphs with error handling (belongs in workflow)
- No dependency graph structure (belongs in dag)
- No multi-agent coordination protocol (belongs in crew)

### bld_output_template_handoff.md
---
kind: output_template
id: bld_output_template_handoff
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a handoff
pattern: every field here exists in SCHEMA.md; template derives, never invents
---

# Output Template: handoff
Naming pattern: `p12_ho_{task}.md`
Filename: `p12_ho_{{task_slug}}.md`
```yaml
id: p12_ho_{{task_slug}}
kind: handoff
lp: P12
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
satellite: "{{target_satellite}}"
mission: "{{mission_name}}"
autonomy: "{{full|supervised|assisted}}"
quality_target: {{7.0_to_10.0}}
domain: "{{domain_value}}"
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
dependencies: [{{dep_handoff_ids_or_omit}}]
seeds: [{{seed_1}}, {{seed_2}}, {{seed_3}}]
agent: "{{agent_name_or_omit}}"
skill: "{{skill_name_or_omit}}"
batch: "{{batch_id_or_omit}}"
wave: {{wave_number_or_omit}}
keywords: [{{keyword_1}}, {{keyword_2}}]
linked_artifacts:
  primary: "{{primary_ref_or_omit}}"
  related: [{{related_refs_or_omit}}]
```
# {{SATELLITE}} — {{MISSION}}: {{Title}}
**{{Autonomy}} Autonomy** | **Quality {{quality_target}}+**
**REGRA: Commit e signal ANTES de qualquer pausa.**
## Context
{{why_this_work_is_needed}}
{{relevant_background}}
## Tasks
### Step 1: {{ACTION_VERB}}
{{specific_actionable_instruction}}
### Step 2: {{ACTION_VERB}}
{{specific_actionable_instruction}}
## Scope Fence
- SOMENTE: {{allowed_paths}}
- NAO TOQUE: {{forbidden_paths}}
## Commit
```bash
git add {{paths}}
git commit -m "{{satellite}}[{{mission}}]: {{description}}"
```
## Signal
```bash
python -c "from records.core.python.signal_writer import write_signal; write_signal('{{satellite}}', 'complete', {{quality_score}})"
```
## Derivation Notes
- Frontmatter fields are the machine-readable contract from SCHEMA.md
- Body sections are the human-readable execution brief
- Omit absent optional frontmatter fields instead of using placeholders
- Tasks must be specific: each step = one action verb

### bld_architecture_handoff.md
---
kind: architecture
id: bld_architecture_handoff
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of handoff — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| task_description | Core body of work the receiver must complete | author | required |
| context_block | Background information the receiver needs to act | author | required |
| scope_fence | Explicit allowed/forbidden paths and operations | author | required |
| commit_rules | How and when to commit work before stopping | author | required |
| signal_instruction | How to emit completion status after finishing | author | required |
| seed_keywords | Domain terms guiding retrieval and search | author | optional |
| dependency_refs | Upstream artifacts this handoff depends on | author | optional |
| naming_convention | File naming pattern (`{MISSION}_{sat}.md`) | system | required |
## Dependency Graph
```
dispatch_rule --produces--> handoff
dag           --produces--> handoff
handoff       --> execution
execution     --produces--> signal
handoff       --referenced_by--> spawn_config
handoff       --referenced_by--> workflow
```
| From | To | Type | Data |
|------|----|------|------|
| dispatch_rule | handoff | data_flow | satellite selection, mission name |
| dag | handoff | data_flow | task node context, dependency order |
| handoff | execution | data_flow | task, context, scope fence, commit rules |
| execution | signal | data_flow | status (complete/error), score |
| handoff | spawn_config | data_flow | satellite id, model params |
| handoff | workflow | data_flow | step instructions within larger orchestration |
## Boundary Table
| handoff IS | handoff IS NOT |
|------------|----------------|
| Complete delegation package for one receiver | Conversational prompt with persona |
| Carries task + context + scope + commit rules | Status or event report |
| One handoff per satellite per mission | Routing policy (who receives what type) |
| Pre-execution artifact (written before spawn) | Dependency graph of tasks |
| Scoped to a single execution unit | Multi-agent orchestration runtime |
| Source of truth for what to do and how to commit | Boot configuration (model, flags, MCPs) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Routing | dispatch_rule, dag | Decide which satellite and in what order |
| Delegation | task_description, context_block, seed_keywords | Define the work and its background |
| Boundary | scope_fence, dependency_refs | Constrain what may be touched |
| Commit | commit_rules, signal_instruction | Enforce artifact persistence and status reporting |
| Instantiation | spawn_config, workflow | Consume handoff to launch or sequence execution |

### bld_collaboration_handoff.md
---
kind: collaboration
id: bld_collaboration_handoff
pillar: P12
llm_function: COLLABORATE
purpose: How handoff-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: handoff-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what should the target do, with what context, and how should it commit?"
I do not define routing rules. I do not model dependencies.
I package delegation instructions so remote executors have everything needed to complete a task.
## Crew Compositions
### Crew: "Full Dispatch Setup"
```
  1. dispatch-rule-builder -> "routing rules (who receives)"
  2. dag-builder -> "execution order (when to execute)"
  3. handoff-builder -> "delegation instructions (what to do)"
```
### Crew: "Task Delegation"
```
  1. context-doc-builder -> "domain context for the executor"
  2. instruction-builder -> "step-by-step recipe"
  3. handoff-builder -> "packaged delegation with scope fence and commit rules"
```
## Handoff Protocol
### I Receive
- seeds: target executor, task description, scope fence (allowed/forbidden paths)
- optional: context documents, seed keywords, commit template, quality threshold
### I Produce
- handoff artifact (.md with context, tasks, scope fence, commit, signal sections)
- committed to: `cex/P12/examples/p12_handoff_{mission}_{target}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- dispatch-rule-builder: provides routing decision that determines handoff target
- context-doc-builder: provides domain context embedded in the handoff
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| dag-builder | Models handoff dependencies in execution graphs |
| e2e-eval-builder | Tests that handoff execution produces correct results |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `handoff-builder` for pipeline function `COLLABORATE`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
