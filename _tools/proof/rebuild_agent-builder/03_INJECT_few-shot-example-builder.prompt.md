# CEX Crew Runner -- Builder Execution
**Builder**: `few-shot-example-builder`
**Function**: INJECT
**Intent**: reconstroi agent-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:20.318811

## Intent Context
- **Verb**: reconstroi
- **Object**: agent-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_few_shot_example.md
---
id: few-shot-example-builder
kind: type_builder
pillar: P01
parent: null
domain: few_shot_example
llm_function: BECOME
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: EDISON
tags: [kind-builder, few-shot-example, P01, specialist, prompt]
---

# few-shot-example-builder
## Identity
Especialista em construir few_shot_example — pares input/output para few-shot learning em prompts.
Knows prompt engineering, example selection, edge case coverage, difficulty calibration,
and the boundary between few_shot_example (format exemplification) and golden_test (quality evaluation).
## Capabilities
- Craft realistic input/output pairs that teach format, not evaluate quality
- Calibrate difficulty (easy/medium/hard) and cover edge cases
- Produce few_shot_example with complete frontmatter (5+ required fields)
- Validate artifacts against quality gates (7 HARD + 7 SOFT)
- Keep artifacts under 1024 bytes and always show FORMAT not just content
## Routing
keywords: [few-shot, example, input-output, prompt, learning, calibration, training]
triggers: "create few-shot example", "show input output pair", "exemplify format", "prompt example"
## Crew Role
In a crew, I handle FEW-SHOT EXAMPLE CRAFTING.
I answer: "what input/output pair best teaches this format?"
I do NOT handle: golden test scoring (P07), unit eval assertions (P07), prompt template authoring (P03).

### bld_instruction_few_shot_example.md
---
kind: instruction
id: bld_instruction_few_shot_example
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for few_shot_example
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a few_shot_example
## Phase 1: RESEARCH
1. Identify the target format to exemplify — which artifact kind or output structure are you teaching?
2. Determine difficulty level: easy (canonical happy path), medium (realistic variation), hard (edge case or boundary input)
3. Select realistic input data — concrete, specific, the kind of request a real user would send
4. Craft the expected output matching the exact target format — no abbreviations, no abstractions
5. Identify edge cases to cover — what unusual input or boundary condition does this example exercise?
6. Check existing examples for the same format — avoid producing a duplicate that teaches the same lesson
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all required fields and constraints
2. Read OUTPUT_TEMPLATE.md — use exact template structure
3. Fill frontmatter:
   - id: `p01_fse_{topic_slug}` (must match filename stem)
   - kind: `few_shot_example`
   - quality: null (never self-score)
   - difficulty: easy | medium | hard
4. Write Input section: realistic data matching the target schema — not "write something", but a fully specified request
5. Write Output section: correctly formatted result demonstrating the target format without deviation
6. Write Difficulty section: calibration level with one-line justification
7. Write Edge Cases section: which unusual inputs this example covers and how
8. Write Format Notes section: which structural element or rule this example is specifically teaching
9. Check body size — must stay at or below 1024 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — run all HARD gates manually before outputting
2. HARD gates:
   - [ ] id matches `p01_fse_[a-z][a-z0-9_]+`
   - [ ] kind == `few_shot_example`
   - [ ] quality == null
   - [ ] input field is non-empty
   - [ ] output field is non-empty
   - [ ] difficulty is labeled
   - [ ] body <= 1024 bytes
3. SOFT gates: tldr <= 160 chars, tags >= 3, Format Notes present, input is realistic, output demonstrates format clearly
4. Cross-check: teaches FORMAT not evaluates quality (that is golden_test)? Not assertion-based (that is unit_eval)? No `{{vars}}` placeholders (that is prompt_template)?
5. If score < 8.0: revise in the same pass before outputting

### bld_knowledge_card_few_shot_example.md
---
kind: knowledge_card
id: bld_knowledge_card_few_shot_example
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for few_shot_example production — format-teaching I/O pairs
sources: Brown et al. 2020 (GPT-3), Anthropic prompt engineering, in-context learning research
---

# Domain Knowledge: few_shot_example
## Executive Summary
Few-shot examples are input/output pairs that teach LLMs format and quality through in-context demonstration. 1-3 examples dramatically improve task performance (Brown et al. 2020) — the LLM pattern-matches example structure. A mediocre prompt with a golden example outperforms an excellent prompt with no example. Few-shot examples differ from golden tests (quality evaluation with scoring) and unit evals (assertion-based correctness testing).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge) |
| Max size | 1024 bytes per example |
| Quality gates | 7 HARD + 7 SOFT |
| Quantity rule | 1 golden + 1 anti per builder (sufficient) |
| Max examples | 3 golden + 3 anti (context budget limit) |
| Purpose | Teach FORMAT, not evaluate QUALITY |
## Patterns
- **Golden example structure**: three layers
| Layer | Content | Rule |
|-------|---------|------|
| Frontmatter | Every schema field with realistic value | Missing field = LLM learns to omit it |
| Dense body | Concrete domain content, no filler | Every sentence carries information |
| WHY GOLDEN | Maps each quality gate to example | Bridge between example and schema |
- **Anti-example structure**: deliberately violates schema to teach what NOT to produce
| Layer | Content | Rule |
|-------|---------|------|
| Wrong frontmatter | Missing fields, wrong prefix, self-scored quality | Shows specific violations |
| Generic body | Filler language, no domain content | "You are a helpful assistant" |
| FAILURES | Numbered list of violated gates | Gate code + FAIL for each |
- **Bridge pattern**: SCHEMA defines fields → EXAMPLE demonstrates them → GATES validate them
- **Density test**: if replacing a sentence with "blah blah" and example seems complete, that sentence is filler
- **Input specificity**: golden input names concrete artifacts; anti input is vague and generic
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Abstract output ("good response") | LLM learns vagueness, not format |
| Vague input ("write something") | No domain anchor; any output seems valid |
| Self-scored quality field | Must be null; self-scoring teaches wrong pattern |
| Body > 1024 bytes | Exceeds context budget; compress |
| Missing gate references in WHY | Bridge between example and schema is broken |
| >3 golden examples | Diminishing returns; wastes context window |
## Application
1. Read target type's SCHEMA.md: know every required field and gate
2. Write golden: specific input + fully-formatted output + WHY GOLDEN mapping all gates
3. Write anti: vague input + deliberately wrong output + FAILURES listing violated gates
4. Verify bridge: every schema field appears in golden; every HARD gate referenced
5. Density check: every sentence in body carries information; no filler
6. Validate: <= 1024 bytes per example, quality: null, realistic domain values
## References
- Brown et al. 2020: "Language Models are Few-Shot Learners" (GPT-3)
- Anthropic: prompt engineering — in-context example design
- Min et al. 2022: "Rethinking the Role of Demonstrations in In-Context Learning"
- Liu et al. 2022: few-shot example selection and ordering effects

### bld_quality_gate_few_shot_example.md
---
id: p11_qg_few_shot_example
kind: quality_gate
pillar: P11
title: "Gate: few_shot_example"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: "few_shot_example — input/output pairs that teach format to LLMs via in-context prompt engineering"
quality: null
tags: [quality-gate, few-shot-example, prompt-engineering, format-teaching, P11]
tldr: "Validates few_shot_example artifacts: input/output completeness, format demonstration clarity, and byte-size constraint."
density_score: 0.90
---

# Gate: few_shot_example
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: few_shot_example` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p01_fse_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `few_shot_example` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | `input` field present and non-empty string | Missing or empty input |
| H07 | `output` field present and non-empty string | Missing or empty output |
| H08 | Artifact body size <= 1024 bytes | Exceeds byte limit (bloats prompt context) |
| H09 | No scoring rubric present anywhere in the artifact | Rubric found (conflates with golden_test) |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` <= 160 chars, names the format being taught | 0.10 | Accurate=1.0, vague=0.4, absent=0.0 |
| S02 | Tags list len >= 3, includes `few-shot` | 0.05 | Met=1.0, partial=0.5 |
| S03 | Output demonstrates FORMAT visibly (structure present, not just content) | 0.18 | Clear structure=1.0, content-only=0.2 |
| S04 | Input is a realistic task request (not abstract or contrived) | 0.14 | Realistic=1.0, contrived=0.3 |
| S05 | Explanation section present and explains why the output format is correct | 0.12 | Present+explains=1.0, missing=0.0 |
| S06 | Example is self-contained (no external reference required to understand it) | 0.10 | Self-contained=1.0, requires context=0.2 |
| S07 | Example covers a non-trivial pattern (edge case or formatting nuance) | 0.10 | Non-trivial=1.0, trivial happy-path=0.4 |
| S08 | `density_score` >= 0.80 | 0.08 | Met=1.0, below=0.0 |
| S09 | No filler in output ("as you can see", "this example shows") | 0.07 | Clean=1.0, filler present=0.0 |
| S10 | Difficulty level (`easy`/`medium`/`hard`) matches actual complexity | 0.06 | Accurate=1.0, mislabeled=0.2 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — reference artifact for few_shot_example calibration |
| >= 8.0 | PUBLISH — pool-eligible; format clearly demonstrated in output |
| >= 7.0 | REVIEW — usable but output may be content-heavy, not format-focused |
| < 7.0  | REJECT — redo; likely missing format structure or oversized body |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Domain so narrow that no realistic input exists; synthetic input approved in writing |
| approver | Prompt engineer who owns the target prompt template |
| audit trail | Required: target prompt ID, justification for synthetic input, approver name |
| expiry | Permanent until a realistic example is available to replace it |
| never bypass | H01 (corrupt YAML), H05 (self-scored quality is invalid), H08 (byte limit protects prompt context budgets — non-negotiable) |

### bld_schema_few_shot_example.md
---
kind: schema
id: bld_schema_few_shot_example
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for few_shot_example
pattern: TEMPLATE derives from this. CONFIG restricts this.
version: "2.0.0"
---

# Schema: few_shot_example
SOURCE OF TRUTH. OUTPUT_TEMPLATE derives from here. CONFIG restricts from here.
## Required Fields (12)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | YES | — | Pattern: `^p01_fse_[a-z][a-z0-9_]+$`, must equal filename stem |
| kind | literal "few_shot_example" | YES | — | Type integrity |
| pillar | literal "P01" | YES | — | Pillar assignment |
| title | string | YES | — | Human-readable label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| input | string | YES | — | Non-empty task/prompt being demonstrated |
| output | string | YES | — | Non-empty ideal response showing format |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3, includes "few-shot" | YES | — | Classification |
| tldr | string <= 160ch | YES | — | Dense summary |
## Recommended Fields (7)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| author | string | REC | — | Who produced this example |
| domain | string | REC | — | Artifact kind being exemplified |
| difficulty | enum: easy, medium, hard | REC | — | Complexity tier |
| edge_case | boolean | REC | false | True if tests boundary condition |
| format | string | REC | — | What format this exemplifies |
| explanation | string | REC | — | Why this pair teaches the format |
| keywords | list[string], len >= 3 | REC | — | Search terms |
## Example Counts
| Metric | Type | Constraint | Rationale |
|--------|------|------------|-----------|
| golden_count | integer | >= 1 required | Minimum 1 golden example per builder |
| anti_count | integer | >= 1 required | Minimum 1 anti-example per builder |
| max_golden | integer | <= 3 | Context budget: never exceed 3 golden |
| max_anti | integer | <= 3 | Context budget: never exceed 3 anti |
## Body Structure (3 required sections)
1. **Golden Example** — 3 layers:
   - Frontmatter: every schema field with realistic value
   - Dense Body: concrete domain content, no filler
   - WHY GOLDEN: maps each quality gate to example (`- quality: null (H05 pass)`)
2. **Anti-Example** — 3 layers:
   - Wrong Frontmatter: deliberately violates schema (wrong prefix, missing fields, self-scored quality)
   - Generic Body: filler language, no domain content
   - FAILURES: numbered list of violated gates (`1. id: no p03_sp_ prefix -> H02 FAIL`)
3. **Bridge Table** — gate coverage matrix:
   - Every schema field appears in golden example
   - Every HARD gate referenced in golden (pass) or anti (fail)
   - >= 80% of SOFT gates referenced across both examples
## Gate References
Anti-examples MUST reference gate codes for each failure:
```
1. id: missing p01_fse_ prefix -> H02 FAIL
2. quality: 8.5 (self-scored) -> H05 FAIL
3. tags: only 1 tag -> H06 FAIL (len >= 3)
```
## Constraints
- max_bytes: 5120 (body only) — builder EXAMPLES.md avg 3985B, max 6918B; old 1024 limit was insufficient
- naming: p01_fse_{topic}.md + p01_fse_{topic}.yaml
- id MUST equal filename stem
- input AND output MUST both be non-empty strings
- NO scoring rubric (that is golden_test P07)
- quality MUST be null
- Golden input: specific, names concrete artifact
- Anti input: vague, generic (demonstrates what NOT to do)
- Density test: if replacing a sentence with "blah blah" and example seems complete, it is filler — remove it
## Boundary Rule
few_shot_example SHOWS format. golden_test (P07) EVALUATES quality with scoring rubric.
If your artifact has a rubric or scores, it is NOT a few_shot_example.
## ID Pattern
Regex: `^p01_fse_[a-z][a-z0-9_]+$`
Examples: `p01_fse_kc_frontmatter`, `p01_fse_validator_conditions`, `p01_fse_rag_source_yaml`

### bld_architecture_few_shot_example.md
---
kind: architecture
id: bld_architecture_few_shot_example
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of few_shot_example — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| input_text | Realistic task request that mimics a real user or system prompt | few_shot_example | required |
| output_text | Ideal response demonstrating the target format exactly | few_shot_example | required |
| domain | Subject area the example belongs to; scopes the learning signal | few_shot_example | required |
| difficulty | Calibration level: easy, medium, or hard | few_shot_example | required |
| format_target | The specific format being taught (JSON, YAML, Markdown, table, etc.) | few_shot_example | required |
| edge_case_flag | Whether this example covers a boundary or unusual condition | few_shot_example | optional |
| byte_budget | Size constraint (max 1024 bytes); keeps context injection cost low | few_shot_example | required |
## Dependency Graph
```
knowledge_card (P01) --produces--> few_shot_example
schema (P06)         --depends-->  few_shot_example
few_shot_example     --produces--> system_prompt (P03)
few_shot_example     --produces--> action_prompt (P03)
golden_test (P07)    --depends-->  few_shot_example
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card (P01) | few_shot_example | produces | domain facts and concepts to exemplify |
| schema (P06) | few_shot_example | depends | format constraints the output must conform to |
| few_shot_example | system_prompt (P03) | produces | injected input/output pair for format teaching |
| few_shot_example | action_prompt (P03) | produces | task demonstration injected into action context |
| golden_test (P07) | few_shot_example | depends | uses exemplary pairs as quality reference anchors |
## Boundary Table
| few_shot_example IS | few_shot_example IS NOT |
|---------------------|-------------------------|
| An input/output pair that teaches format by demonstration | An artifact with a scoring rubric or quality grade (that is golden_test) |
| Evaluated externally; quality is null in the artifact itself | A prompt template with {{variables}} for reuse |
| Subject to a byte budget (max 1024 bytes) | Background domain knowledge without an input/output pair |
| A teaching unit — shows HOW to format a response | A test assertion that checks correctness (that is unit_eval) |
| Domain-scoped and difficulty-calibrated | An orchestration step or workflow instruction |
| Stateless — no execution context, just a static pair | A context document explaining system background |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| Source | knowledge_card (P01), schema (P06) | Provide domain facts and format constraints to exemplify |
| Content | input_text, output_text | The core teaching pair — request and ideal response |
| Metadata | domain, difficulty, format_target, edge_case_flag | Classify the example for selection and calibration |
| Budget | byte_budget | Enforce size constraint for cost-effective context injection |
| Injection | system_prompt (P03), action_prompt (P03) | Consume the pair as format-teaching context |
| Evaluation | golden_test (P07) | Use exemplary pairs as quality calibration anchors (external) |

### bld_collaboration_few_shot_example.md
---
kind: collaboration
id: bld_collaboration_few_shot_example
pillar: P12
llm_function: COLLABORATE
purpose: How few-shot-example-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: few-shot-example-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what input/output pair best teaches this format?"
I do not evaluate quality. I do not test correctness.
I craft format-exemplifying pairs so prompts can teach LLMs the expected output shape.
## Crew Compositions
### Crew: "Prompt Quality Stack"
```
  1. context-doc-builder -> "domain context"
  2. action-prompt-builder -> "task-focused prompt"
  3. few-shot-example-builder -> "input/output examples for the prompt"
  4. golden-test-builder -> "quality reference for evaluation"
```
### Crew: "Format Teaching"
```
  1. input-schema-builder -> "input contract definition"
  2. few-shot-example-builder -> "examples that demonstrate the format"
  3. formatter-builder -> "output formatting rules"
```
## Handoff Protocol
### I Receive
- seeds: target format/artifact type, difficulty level (easy/medium/hard)
- optional: edge cases to cover, domain context, output schema
### I Produce
- few_shot_example artifact (.md + .yaml, max 1024 bytes)
- committed to: `cex/P01/examples/p01_fewshot_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- input-schema-builder: provides the format contract that examples must demonstrate
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| action-prompt-builder | Embeds few-shot examples in task prompts |
| chain-builder | Uses examples to calibrate chain step outputs |
| golden-test-builder | References examples as starting point for quality refs |

### bld_config_few_shot_example.md
---
kind: config
id: bld_config_few_shot_example
pillar: P09
llm_function: CONSTRAIN
purpose: File system and operational configuration for few_shot_example artifacts
---

# Config: few_shot_example
## File Naming
| Component | Rule | Example |
|-----------|------|---------|
| Prefix | p01_fse_ (fixed) | p01_fse_ |
| Topic slug | lowercase, underscores, no hyphens | kc_frontmatter |
| Extension | .md (primary) + .yaml (machine) | p01_fse_kc_frontmatter.md |
| Full name | p01_fse_{topic_slug}.md | p01_fse_kc_frontmatter.md |
## File Paths
| File type | Path |
|-----------|------|
| Primary (md) | `cex/P01_knowledge/examples/p01_fse_{topic}.md` |
| Machine (yaml) | `cex/P01_knowledge/examples/p01_fse_{topic}.yaml` |
| Builder | `cex/archetypes/builders/few-shot-example-builder/` |
## Size Constraints
| Constraint | Value | Scope |
|------------|-------|-------|
| max_bytes | 1024 | Body only (not frontmatter) |
| tldr max | 160 chars | tldr field |
| tags min | 3 items | tags list |
| input min | 1 char | input field (non-empty) |
| output min | 1 char | output field (non-empty) |
## Difficulty Enum
| Value | Meaning | When to use |
|-------|---------|-------------|
| easy | Canonical happy-path | First example for a format |
| medium | Realistic variation | Second example, different domain |
| hard | Edge case or ambiguous | Third example, boundary testing |
## Input/Output Constraints
- input: string — the task request a real user would send
- output: string — the complete ideal response (may be multiline with YAML block scalar)
- Both fields MUST be non-empty
- Output MUST demonstrate format, not describe it
## ID Constraint
```
id == filename stem
p01_fse_kc_frontmatter.md -> id: p01_fse_kc_frontmatter
```

### bld_examples_few_shot_example.md
---
kind: examples
id: bld_examples_few_shot_example
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of few_shot_example artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: few-shot-example-builder
## Golden Example
INPUT: "Cria um few_shot_example mostrando o formato de frontmatter YAML de um knowledge_card"
OUTPUT:
```yaml
id: p01_fse_kc_frontmatter
kind: few_shot_example
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
input: "Create a knowledge card about Docker networking basics"
output: |
  id: kc_docker_networking
  kind: knowledge_card
  pillar: P01
  version: "1.0.0"
  created: "2026-03-26"
  updated: "2026-03-26"
  author: "knowledge-engine"
  quality: null
  tags: [docker, networking, devops]
  tldr: "Docker networking: bridge, host, overlay modes and use cases."
domain: knowledge_card
difficulty: easy
edge_case: false
format: "knowledge_card YAML frontmatter"
quality: null
tags: [few-shot, knowledge-card, frontmatter, yaml]
tldr: "Input/output pair teaching knowledge_card YAML frontmatter format."
keywords: [knowledge-card, frontmatter, yaml, format]
```
## Explanation
Teaches the exact YAML frontmatter structure for knowledge_card.
LLM learns: required fields, field order, quality: null rule, tags as list.
## Variations
- **Variation 1**: "Create a KC about Python async/await" — same format, different domain
- **Variation 2**: "Create a KC about React hooks best practices" — tests tag selection
## Edge Cases
- **Edge**: input requests a KC with quality: 9.0
  **Expected**: output shows quality: null — self-scoring is forbidden
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p01_fse_ pattern (H02 pass)
- id == filename stem p01_fse_kc_frontmatter (H03 pass)
- kind: few_shot_example (H04 pass)
- input field non-empty, realistic task (H06 pass)
- output field non-empty, shows complete format (H07 pass)
- YAML parses cleanly (H01 pass)
- tldr <= 160 chars (S01 pass)
- tags list has 4 items >= 3 (S02 pass)
- Explanation section present (S03 pass)
- No scoring rubric (S07 pass)
## Anti-Example
INPUT: "Faz um exemplo de knowledge card"
BAD OUTPUT:
```yaml
id: kc_example
kind: example
pillar: knowledge
input: write a knowledge card
output: a good knowledge card with all fields
quality: 8.5
scoring:
  criteria: completeness
  weight: 0.5
tags: example
This document shows how to make knowledge cards. Basically you fill in the fields.
```
FAILURES:
1. id: no `p01_fse_` prefix -> H02 FAIL
2. kind: "example" not "few_shot_example" -> H04 FAIL
3. quality: 8.5 (not null) -> H05 FAIL
4. input: "write a knowledge card" — not a realistic task request -> S04 FAIL
5. output: abstract description, not format demonstration -> S05 FAIL
6. scoring rubric included: golden_test drift -> S07 FAIL
7. tags: string not list, len < 3 -> S02 FAIL
8. body: filler prose ("basically you fill in the fields") -> S07 FAIL
9. pillar: "knowledge" not "P01" -> H01 schema violation
10. Explanation section missing -> S03 FAIL

### bld_memory_few_shot_example.md
---
id: p10_lr_few_shot_example_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Few-shot examples that demonstrate format teach more reliably than examples that demonstrate content. Output fields that contain prose descriptions ('a good response would include...') rather than actual format demonstrations fail to transfer format patterns. Body exceeding 1024 bytes — the tightest limit in P01 — forces cuts to explanation rather than examples. Input prompts that are vague ('write something about X') produce outputs that cannot be reused as format templates. Difficulty calibration absent from a set means all examples are easy, leaving edge cases untaught."
pattern: "The output field must show the actual format, not describe it. Input must be specific and realistic. Sequence examples easy -> medium -> hard across a set. Each pair includes an Explanation section stating exactly which format rule the output demonstrates. Body cap is 1024 bytes — trim Variations and Edge Cases before trimming the output demonstration. Never include scoring rubric or quality assessment; that belongs in golden_test (P07)."
evidence: "12 few-shot example artifacts reviewed. Output fields containing descriptions instead of demonstrations required rework in 8 of 12 cases. Vague inputs produced non-reusable format templates in 5 cases. Sets with difficulty calibration (easy+medium+hard) showed 40% better format transfer in downstream evaluations vs easy-only sets."
confidence: 0.70
outcome: SUCCESS
domain: few_shot_example
tags: [few_shot_example, format_teaching, difficulty_calibration, input_output_pairs, format_demonstration]
tldr: "Show format in output, not describe it. Calibrate easy->medium->hard. Stay under 1024 bytes body."
impact_score: 7.5
decay_rate: 0.04
satellite: edison
keywords: [few_shot, format_teaching, difficulty_calibration, output_demonstration, input_specificity, edge_case, explanation]
---

## Summary
Few-shot examples teach a model what format to produce, not what content to generate. The output field must be an actual demonstration of the target format. Difficulty must be calibrated across a set — easy examples establish the baseline, medium ones show variation, hard ones handle edge cases. The body limit is 1024 bytes, the tightest in the P01 pillar.
## Pattern
1. The `output` field must contain the actual formatted artifact, not a description of what it should contain.
2. The `input` field must be specific and realistic — a real task someone would submit, not a placeholder.
3. Sequence examples across a set: easy (canonical request) -> medium (realistic variation) -> hard (edge case or boundary condition).
4. Every example includes an `## Explanation` section stating which specific format rule the output demonstrates and why.
5. Body cap is 1024 bytes. Trim `## Variations` and `## Edge Cases` prose sections before trimming the output itself.
6. `quality` must be null — self-scoring is rejected. Scoring belongs in golden_test (P07).
7. The `id` field value must match the filename stem exactly.
8. Tags must be a YAML list, not a string.
## Anti-Pattern
- Output field containing prose: "a good response would have a tldr, then three bullet points..." — this teaches nothing about format.
- Input so vague it cannot produce a consistent format demonstration: "write something about quality gates."
- Including a scoring rubric or quality threshold — that is golden_test (P07), not few_shot_example.
- All examples set to easy difficulty — edge cases go untaught and the model fails on boundary inputs.
- Body over 1024 bytes — the fix is trimming prose sections, never truncating the output demonstration with "...".
- Recursive drift: producing a few_shot_example about few_shot_examples that evaluates quality (crosses into P07).
## Context
Applies when: teaching format for any artifact type by showing concrete input/output pairs.


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `few-shot-example-builder` for pipeline function `INJECT`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
