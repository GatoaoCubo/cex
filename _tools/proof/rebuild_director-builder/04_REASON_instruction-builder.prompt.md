# CEX Crew Runner -- Builder Execution
**Builder**: `instruction-builder`
**Function**: REASON
**Intent**: reconstroi director-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:21.023811

## Intent Context
- **Verb**: reconstroi
- **Object**: director-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_instruction.md
---
id: instruction-builder
kind: type_builder
pillar: P03
parent: null
domain: instruction
llm_function: BECOME
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: EDISON
tags: [kind-builder, instruction, P03, specialist, steps, recipe]
---

# instruction-builder
## Identity
Especialista em construir instructions — receitas operacionais passo-a-passo para
execucao de tarefas por agentes. Domina decomposicao de tarefas, prerequisitos,
validacao de conclusao, rollback strategies, e a distincao entre instructions (P03),
action_prompts (P03), e workflows (P12).
## Capabilities
- Decompor tarefas complexas em steps atomicos e sequenciais
- Produzir instruction com frontmatter completo (20 campos)
- Definir prerequisites, validation criteria, e rollback procedures
- Classificar idempotencia e atomicidade de cada instruction
- Especificar dependencies e ordem de execucao
- Validar artifact contra quality gates (8 HARD + 11 SOFT)
## Routing
keywords: [instruction, steps, recipe, how-to, procedure, runbook, execution, prerequisites]
triggers: "create step-by-step instruction", "write execution recipe for task", "build operational runbook"
## Crew Role
In a crew, I handle OPERATIONAL RECIPES.
I answer: "what are the exact steps to execute this task?"
I do NOT handle: agent identity (system_prompt), task prompts with I/O (action_prompt), multi-agent orchestration (workflow P12).

### bld_architecture_instruction.md
---
kind: architecture
id: bld_architecture_instruction
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of instruction — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| prerequisites | Conditions and resources that must exist before execution begins | author | required |
| steps | Ordered atomic actions the executor follows sequentially | author | required |
| validation_criteria | Observable outcomes that confirm each step succeeded | author | required |
| rollback_procedure | Reversal actions if execution fails midway | author | required |
| idempotency_flag | Whether repeated execution produces the same result safely | author | required |
| dependencies | Other instructions or artifacts this instruction relies on | author | optional |
| timeout_guidance | Expected duration and when to escalate | author | optional |
| scope_note | Explicit boundaries on what this instruction modifies | author | optional |
## Dependency Graph
```
action_prompt  --provides_context_to--> instruction
knowledge_card --informs--> instruction
instruction    --consumed_by--> agent
instruction    --referenced_by--> skill
skill          --depends_on--> instruction
```
| From | To | Type | Data |
|------|----|------|------|
| action_prompt | instruction | data_flow | task context, goal, and constraints |
| knowledge_card | instruction | data_flow | domain facts required for step accuracy |
| instruction | agent | data_flow | ordered steps, prerequisites, rollback |
| instruction | skill | data_flow | sub-procedure referenced by skill phases |
| skill | instruction | depends | skill phase delegates to instruction for execution |
## Boundary Table
| instruction IS | instruction IS NOT |
|----------------|-------------------|
| Step-by-step recipe for a single executor | Conversational prompt with response format |
| Specifies exact actions, not goals | Agent identity or persona definition |
| Includes rollback for failure recovery | Multi-agent orchestration across satellites |
| One-shot execution without lifecycle phases | Structured workflow with branching logic |
| Single-agent scope | Task delegation package to a remote receiver |
| Verifiable: each step has validation criteria | Event-triggered side-effect handler |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Entry gate | prerequisites, dependencies | Ensure conditions are met before starting |
| Execution | steps, scope_note, timeout_guidance | Provide the ordered recipe to follow |
| Verification | validation_criteria | Confirm each step completed correctly |
| Recovery | rollback_procedure, idempotency_flag | Handle failure without data corruption |
| Integration | action_prompt, knowledge_card | Supply context and domain knowledge to steps |

### bld_collaboration_instruction.md
---
kind: collaboration
id: bld_collaboration_instruction
pillar: P12
llm_function: COLLABORATE
purpose: How instruction-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: instruction-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the exact steps to execute this task?"
I do not define agent identity. I do not write task prompts with I/O.
I compose step-by-step recipes so agents can execute tasks in correct order with validation.
## Crew Compositions
### Crew: "New Agent End-to-End"
```
  1. knowledge-card-builder -> "domain knowledge"
  2. agent-builder -> "agent definition"
  3. instruction-builder -> "execution steps for agent tasks"
  4. boot-config-builder -> "provider configuration"
  5. iso-package-builder -> "deployable package"
```
### Crew: "Task Recipe Design"
```
  1. context-doc-builder -> "domain context for grounding"
  2. instruction-builder -> "step-by-step operational recipe"
  3. action-prompt-builder -> "task prompt that follows the recipe"
  4. e2e-eval-builder -> "end-to-end test of recipe execution"
```
## Handoff Protocol
### I Receive
- seeds: task name, high-level goal, execution environment
- optional: prerequisites, rollback procedures, validation criteria, dependencies
### I Produce
- instruction artifact (.md + .yaml frontmatter)
- committed to: `cex/P03/examples/p03_instruction_{task}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- context-doc-builder: provides domain background that grounds recipe steps
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| action-prompt-builder | Prompts may implement instruction steps |
| chain-builder | Chains may encode instruction sequences as prompt pipelines |
| handoff-builder | Embeds instruction steps in delegation packages |
| iso-package-builder | Includes instructions in agent packages |

### bld_config_instruction.md
---
kind: config
id: bld_config_instruction
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: instruction Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p03_ins_{task_slug}.md` | `p03_ins_rebuild_brain_faiss.md` |
| Builder directory | kebab-case | `instruction-builder/` |
| Frontmatter fields | snake_case | `steps_count`, `validation_method` |
| Task slug | snake_case, lowercase | `rebuild_brain_faiss`, `deploy_api` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P03_prompt/examples/p03_ins_{task_slug}.md`
- Compiled: `cex/P03_prompt/compiled/p03_ins_{task_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80
## Validation Method Enum
| Value | When to use |
|-------|-------------|
| checklist | Manual verification via checkbox list (most common) |
| automated | Script or test validates outcome |
| manual | Human judgment required (subjective) |
| none | Fire-and-forget (rare, discouraged) |
## Step Writing Rules
- One action per step (verb + object + expected outcome)
- Steps numbered sequentially (1, 2, 3...)
- Include concrete commands where applicable (not "run the script" but `python build.py --all`)
- Expected outcome after dash: "1. Run build — output shows 0 errors"
- If step has conditional: split into sub-steps (1a, 1b) or separate steps

### bld_examples_instruction.md
---
kind: examples
id: bld_examples_instruction
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of instruction artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: instruction-builder
## Golden Example
INPUT: "Create instruction for rebuilding the Brain FAISS index"
OUTPUT:
```yaml
id: p03_ins_rebuild_brain_faiss
kind: instruction
pillar: P03
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
title: "Rebuild Brain FAISS Index"
target: "knowledge-engine satellite or human operator"
steps_count: 6
prerequisites:
  - "Ollama running locally with nomic-embed-text model"
  - "Python 3.10+ with faiss-cpu installed"
  - "At least 2GB free disk space"
validation_method: checklist
idempotent: true
atomic: false
rollback: "Delete generated .faiss files and revert to previous index backup"
dependencies:
  - "ollama"
  - "faiss-cpu"
  - "build_indexes_ollama.py"
logging: true
domain: "knowledge"
quality: null
tags: [instruction, brain, faiss, index, rebuild]
tldr: "6-step procedure to rebuild Brain FAISS+BM25 index from pool artifacts using Ollama embeddings"
density_score: 0.90
```
## Prerequisites
- Ollama running: `ollama list` shows `nomic-embed-text`
- Python deps: `python -c "import faiss; print(faiss.__version__)"`
- Disk space: `df -h .` shows >= 2GB free
## Steps
1. Backup current index — `cp records/core/brain/*.faiss records/core/brain/backup/`
2. Verify Ollama health — `ollama list | grep nomic-embed-text`
3. Run index builder — `cd records/core/brain/mcp-codexa-brain && python build_indexes_ollama.py --scope all`
4. Wait for completion — process takes ~20 minutes, outputs progress to stdout
5. Verify index size — `ls -la records/core/brain/*.faiss` (expect ~140MB)
6. Test query — `python -c "from brain_search import search; print(search('test query')[:1])"`
## Validation
- [ ] New .faiss files exist and are > 100MB
- [ ] brain_query returns results for known terms
- [ ] No error output in build log
- [ ] Index timestamp matches current date
## Rollback
Restore backup: `cp records/core/brain/backup/*.faiss records/core/brain/`
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p03_ins_ pattern (H02 pass)
- kind: instruction (H04 pass)
- 20 required fields present (H06 pass)
- body has Steps with 6 numbered items (H07 pass)
- rollback defined and atomic: false (H08 pass)
- steps_count: 6 matches actual 6 steps (S03 pass)
- Each step has one action (S04 pass)
- Prerequisites are verifiable commands (S05 pass)
- No persona/identity content (S09 pass)
## Anti-Example
INPUT: "Create instruction for deploying the API"
BAD OUTPUT:
```yaml
id: deploy-api
kind: procedure
pillar: prompt
title: Deploy
steps_count: 1
quality: 9.0
tags: [deploy]
```
You are a deployment expert. Follow these steps:
1. Deploy the API to production by running the deployment script and checking that everything works and then verifying the logs and restarting if needed.
FAILURES:
1. id: no `p03_ins_` prefix, uses hyphens -> H02 FAIL
2. kind: "procedure" not "instruction" -> H04 FAIL
3. pillar: "prompt" not "P03" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. Missing fields: version, created, updated, author, target, prerequisites, validation_method, idempotent, atomic, domain -> H06 FAIL
6. tags: only 1 item -> S02 FAIL
7. Step 1 has 4 compound actions -> S04 FAIL
8. Contains persona ("You are a deployment expert") -> S09 FAIL
9. No ## Prerequisites, ## Validation, ## Rollback sections -> S06, S07, S08 FAIL
10. steps_count: 1 but step contains multiple actions -> S03 FAIL

### bld_instruction_instruction.md
---
kind: instruction
id: bld_instruction_instruction
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for instruction
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an instruction
## Phase 1: RESEARCH
1. Identify the task: state exactly what must happen, who executes it, and in what context
2. Determine the executor: name the agent or role that will follow this recipe
3. List prerequisites — each must be verifiable ("Python 3.10+ installed" not "environment ready")
4. Define the input contract: every variable the executor receives, with type and required/optional status
5. Define the output contract: what the executor produces and in what format
6. Assess complexity to choose phase count: 3 phases for simple tasks, 4-5 for multi-stage operations
7. Check existing instructions via brain_query [IF MCP] for the same task — avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all frontmatter fields and body constraints
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints exactly
3. Fill frontmatter: 15 required fields + 7 recommended fields (null is acceptable for recommended)
4. Set quality: null — never self-score
5. Write the Context section (15-20% of doc): background, input/output contracts, every $variable defined with type and required/optional status
6. Write the Phases section (40-50% of doc): 3-5 phases following the Analyze -> Generate -> Validate pattern; each phase is atomic with one primary action; include pseudocode for complex logic
7. Write the Output Contract section (5-10% of doc): a literal template using {{variable}} placeholders — not a prose description
8. Write the Validation section (8-12% of doc): quality gates with numeric thresholds, formatted as a checklist
9. Write the Metacognition section (recommended): a Does / Does NOT block plus chaining notation showing upstream -> THIS -> downstream
10. Verify phases_count in frontmatter matches the actual number of Phase sections in the body
11. Verify body is within 8192 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — apply each gate manually
2. HARD gates (all must pass):
   - YAML frontmatter parses without errors
   - id matches pattern `p03_ins_[a-z][a-z0-9_]+`
   - kind == instruction
   - phases_count matches actual Phase section count in body
   - prerequisites are verifiable statements, not vague conditions
   - every $variable is defined with type and required/optional
   - output uses a literal {{variable}} template, not prose
   - quality == null
3. SOFT gates (score each against QUALITY_GATES.md):
   - each phase contains exactly one primary action
   - pseudocode present for any complex logic step
   - Context section is 15-20% of total doc
   - Phases section is 40-50% of total doc
   - Metacognition section present with Does / Does NOT block
4. Cross-check scope boundaries:
   - operational recipe, not an agent identity document (system_prompt)?
   - not a one-shot task prompt (action_prompt)?
   - not an orchestration plan (workflow, P12)?
   - no persona or identity content leaked into the body?
5. If score < 8.0: revise in the same pass before outputting

### bld_knowledge_card_instruction.md
---
kind: knowledge_card
id: bld_knowledge_card_instruction
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for instruction production — operational step-by-step recipes
sources: SRE runbooks, IEC 62443 SOPs, operational procedure design, 5 production instructions
---

# Domain Knowledge: instruction
## Executive Summary
Instructions are operational recipes that transform a defined start state into an end state through atomic, verifiable, reversible steps. From SRE runbooks and SOPs. Each step performs one action, has verifiable completion criteria, and supports rollback. Instructions differ from action prompts (concise task with I/O), system prompts (identity/persona), and workflows (multi-agent orchestration).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 (prompts) |
| Frontmatter fields | 20 |
| Quality gates | 8 HARD + 11 SOFT |
| Phases | 3-5 (analyze → generate → validate) |
| Max body bytes | 4096 |
| Sweet spot | 200-350 lines, 3000-3500 tokens |
| Input vars | 3-6 with type hints |
## Patterns
- **7-section structure**: allocation by importance
| Section | Purpose | % of doc |
|---------|---------|----------|
| Title + Audience | Who + what | 2-3% |
| Context | Background, I/O contracts | 15-20% |
| Task | Objective, success criteria | 8-12% |
| Approach | Phased execution + pseudocode | 40-50% |
| Constraints | Quality gates, limits | 8-12% |
| Examples | Complete I/O demo | 10-15% |
| Output Template | Exact deliverable format | 5-10% |
- **Input/output contracts**: every variable has type hint + required/optional + default — without contracts, LLM guesses formats inconsistently
- **Phase structure** (3-5 phases): universal pattern is Analyze → Generate → Validate
- **Pseudocode guidance**: descriptive function names, clear conditions — guides LLM reasoning, not execution
- **Atomic steps**: one action per step — compound steps cause ambiguous failures
- **Verifiable prerequisites**: "Python 3.10+" not "environment ready"
- **Idempotent when possible**: explicit rollback procedure when not
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No input contract | LLM guesses variable types; inconsistent output |
| Compound steps | Two actions in one step; ambiguous failure point |
| Prose output description | Use literal template with {{variables}} instead |
| Missing validation phase | No quality check; output quality unverified |
| No examples | At least 1 complete I/O example required |
| Identity mixed with task | Identity = system_prompt; task = instruction |
| Qualitative gates ("ensure quality") | Unenforceable; use numeric thresholds |
## Application
1. Define audience and prerequisites (verifiable, specific)
2. Write input/output contracts: every var with type, required/optional, default
3. Design 3-5 phases: Analyze → Generate → Validate pattern
4. Write approach section (40-50%): pseudocode with descriptive names
5. Add constraints: numeric quality gates, not aspirational
6. Include >= 1 complete I/O example and output template
## References
- Google SRE: runbook design and operational procedures
- IEC 62443: industrial automation procedure standards
- Prompt engineering: structured instruction design for LLMs
- Operational excellence: atomic, verifiable, reversible step patterns

### bld_memory_instruction.md
---
id: p10_lr_instruction_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Compound steps with multiple action verbs ('deploy and verify and restart') cause partial execution — agents complete the first verb and mark the step done. Vague prerequisites ('environment ready') cannot be verified and are silently skipped. Steps marked atomic:false without a rollback procedure leave systems in partially modified states. Steps_count mismatches with actual step count cause validator rejection. Including persona text in instructions ('You are an expert') misplaces content that belongs in system prompts."
pattern: "Each instruction step contains exactly one action verb and one verifiable expected output. Prerequisites are stated as machine-checkable conditions (e.g., 'Python 3.10+ installed: verify with python --version'). Steps marked atomic:false must declare a rollback procedure. Steps_count in frontmatter must match the exact count of numbered steps in the body. Idempotence classification (idempotent/non-idempotent) is required for every step."
evidence: "10 instruction reviews: 7 of 10 had at least one compound step. 8 of 10 had vague prerequisites. 4 of 10 had atomic:false steps without rollback. Steps_count mismatch found in 3 of 10 (caught by validator). Idempotence classification missing in 6 of 10 early productions."
confidence: 0.75
outcome: SUCCESS
domain: instruction
tags: [instruction, atomic-steps, idempotence, rollback, prerequisites, decomposition]
tldr: "One step = one verb + one verifiable output. Vague prerequisites are skipped. atomic:false requires rollback. steps_count must match exactly."
impact_score: 7.5
decay_rate: 0.05
satellite: edison
keywords: [instruction, atomic, idempotent, rollback, prerequisite, decomposition, step, verification, procedure]
---

## Summary
Instructions describe how to execute a procedure step by step. The primary failure mode is compound steps: packaging multiple actions into one step causes partial execution that appears complete. The secondary failure is unverifiable prerequisites that agents skip silently. Both are fixed at authoring time with simple structural rules.
## Pattern
Step anatomy (all four elements required):
```
### Step N: [Single action verb] [object]
**Prerequisite**: [Machine-checkable condition with verify command]
**Idempotent**: yes | no
[Action description — one verb, one target, one expected output]
**Verify**: [Command or check that confirms step success]
**Rollback**: [Required only if idempotent:no — how to undo this step]
```
Decomposition rules:
- One verb per step: create, edit, run, verify, wait, delete — never "and"
- If a step has a conditional branch, split into two steps with explicit IF noted
- Long-running steps must include monitoring command and expected completion indicator
- Verification steps are their own numbered steps, not sub-bullets of action steps
Idempotence classification:
- `idempotent: yes` — running the step twice produces the same result as running once
- `idempotent: no` — running twice causes side effects; rollback procedure required
Steps_count in frontmatter must be updated manually after adding or removing steps. Validator rejects mismatches.
## Anti-Pattern
- Compound step: "Deploy the app and verify health and restart workers" — split into 3 steps.
- Vague prerequisite: "Environment is ready" — not machine-checkable, silently skipped.
- `atomic: false` without rollback — leaves system in partial state on failure.
- `steps_count: 5` when body has 7 steps — validator rejects, causes production failure.
- Persona text in instructions ("You are an expert deployer") — belongs in system_prompt, not here.
- Verification buried as sub-bullet inside action step — easy to skip, hard to audit.
## Context

### bld_output_template_instruction.md
---
kind: output_template
id: bld_output_template_instruction
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an instruction
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: instruction
```yaml
id: p03_ins_{{task_slug}}
kind: instruction
pillar: P03
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
title: "{{human_readable_title}}"
target: "{{who_executes}}"
steps_count: {{integer_matching_body}}
prerequisites:
  - "{{prerequisite_1}}"
  - "{{prerequisite_2}}"
validation_method: {{checklist|automated|manual|none}}
idempotent: {{true|false}}
atomic: {{true|false}}
rollback: "{{undo_procedure_or_null}}"
dependencies:
  - "{{dependency_1}}"
logging: {{true|false}}
domain: "{{domain_value}}"
quality: null
tags: [instruction, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```
## Prerequisites
- {{prerequisite_1_verifiable_condition}}
- {{prerequisite_2_verifiable_condition}}
## Steps
1. {{action_1}} — {{expected_outcome_1}}
2. {{action_2}} — {{expected_outcome_2}}
3. {{action_3}} — {{expected_outcome_3}}
{{...one action per step, repeat for steps_count}}
## Validation
- [ ] {{check_1_verifiable}}
- [ ] {{check_2_verifiable}}
- [ ] Final outcome: {{expected_final_state}}
## Rollback
{{rollback_procedure_or_na_if_idempotent}}
## References
- {{reference_1}}
- {{reference_2}}

### bld_quality_gate_instruction.md
---
id: p11_qg_instruction
kind: quality_gate
pillar: P11
title: "Gate: Instruction"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: "instruction — step-by-step operational recipes for agent task execution"
quality: null
tags: [quality-gate, instruction, steps, recipe, procedure, idempotency]
tldr: "Gates ensuring instruction artifacts decompose tasks into atomic verifiable steps with prerequisites, completion criteria, and rollback procedures."
density_score: 0.90
---

# Gate: Instruction
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: instruction` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | Uppercase, spaces, or leading digit |
| H03 | ID equals filename stem | `id: deploy_service` in file `restart_service.md` |
| H04 | Kind equals literal `instruction` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All required fields present | Missing: steps, prerequisites, or completion_criteria |
| H07 | Steps are numbered and count >= 2 | Single undivided step or unnumbered list |
| H08 | `idempotent` field is a boolean | Missing field or non-boolean value |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Step atomicity | 1.0 | Every step performs exactly one action and is independently verifiable | Most steps atomic; some compound | Steps are multi-action paragraphs |
| S02 | Prerequisites completeness | 1.0 | All tools, permissions, files, and env vars listed | Some prerequisites listed | No prerequisites section |
| S03 | Completion criteria | 1.0 | Each step has explicit success signal (exit code, file exists, output pattern) | Overall completion defined but not per-step | No success criteria |
| S04 | Rollback procedures | 1.0 | Undo steps defined for each destructive action | Partial rollback notes present | No rollback |
| S05 | Idempotency declaration | 0.5 | `idempotent: true/false` with explanation of why | Field present, no rationale | Field absent |
| S06 | Dependency ordering | 1.0 | Steps reference their predecessors explicitly when order matters | Steps ordered but dependencies implicit | Unordered; any sequence implied |
| S07 | Atomicity classification | 0.5 | `atomic` field classifies instruction as atomic or composable | Classification present but unexplained | Field missing |
| S08 | Error handling per step | 1.0 | Each step lists what to do on failure | Some steps have error notes | No error handling |
| S09 | Tool list | 0.5 | `tools_required` lists every CLI, SDK, or API the steps invoke | Partial tool list | No tool list |
| S10 | Distinction from action_prompt | 0.5 | No I/O prompt framing — pure procedural steps | Minimal prompt framing leakage | Reads as a prompt, not a recipe |
| S11 | Example run | 0.5 | At least one example showing input values substituted into steps | Example mentioned but sparse | No example |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to pool as golden operational runbook |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Novel procedure being executed for the first time; rollback path not yet known |
| Approver | Task owner + one peer reviewer |
| Audit trail | `bypass_reason` required; note which gates are bypassed and why |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `instruction-builder` for pipeline function `REASON`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
