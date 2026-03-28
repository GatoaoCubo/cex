# CEX Crew Runner -- Builder Execution
**Builder**: `response-format-builder`
**Function**: PRODUCE
**Intent**: reconstroi signal-builder
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:29:34.584519

## Intent Context
- **Verb**: reconstroi
- **Object**: signal-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_response_format.md
---
id: response-format-builder
kind: type_builder
pillar: P05
parent: null
domain: response_format
llm_function: BECOME
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [kind-builder, response-format, P05, specialist, spec, output]
---

# response-format-builder
## Identity
Especialista em construir response_formats — formatos de resposta injetados no prompt do LLM para guiar como o agente estrutura seu output.
Conhece structured output patterns (JSON mode, YAML frontmatter, markdown sections), injection points (system_prompt, user_message), e a diferenca critica entre response_format (P05, LLM ve), validation_schema (P06, sistema aplica pos-geracao), parser (P05, extrai dados), e formatter (P05, transforma formato).
## Capabilities
- Projetar formatos de resposta com sections, fields, e examples
- Produzir response_format com frontmatter completo (19 campos)
- Definir injection_point adequado (system_prompt vs user_message)
- Especificar format_type (json, yaml, markdown, csv, plaintext)
- Validar artifact contra quality gates (10 HARD + 9 SOFT)
- Manter boundary clara: LLM ve este formato durante geracao
## Routing
keywords: [response-format, output-format, structured-output, json-mode, how-to-respond, output-structure]
triggers: "how should the LLM format its response", "define output structure", "create response format"
## Crew Role
In a crew, I handle RESPONSE STRUCTURE DESIGN.
I answer: "how should the LLM structure its output for this task?"
I do NOT handle: post-generation validation (validation-schema-builder), data extraction (parser-builder), format transformation (formatter-builder).

### bld_instruction_response_format.md
---
id: p03_ins_response_format
kind: instruction
pillar: P05
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Response Format Builder Instructions
target: "response-format-builder agent"
phases_count: 4
prerequisites:
  - "Caller has identified the task the LLM will perform (e.g. entity extraction, summarization, classification)"
  - "The desired output structure is known at a high level (e.g. JSON object, markdown report, CSV rows)"
  - "Injection point is known or inferable: system_prompt (persistent) or user_message (per-request)"
validation_method: checklist
domain: response_format
quality: null
tags: [instruction, response-format, P05, structured-output, output-design, injection]
idempotent: true
atomic: false
rollback: "Delete the produced format file. No LLM behavior changes until the format is injected into a prompt."
dependencies: []
logging: true
tldr: "Design how the LLM structures its output — sections, fields, examples — and produce a response_format artifact ready for prompt injection."
density_score: 0.92
---

## Context
A **response_format** is a prompt-injected specification that tells the LLM how to structure its output. It is placed into the prompt (system or user turn) so the model sees the format during generation. It governs the shape of every response the agent produces for a given task. The LLM reads this artifact; the system does not execute it.
**Inputs**
| Field | Type | Description |
|---|---|---|
| `task` | string | What the LLM will do (e.g. `extract entities`, `summarize document`, `classify intent`) |
| `format_type` | enum | `json` \| `yaml` \| `markdown` \| `csv` \| `plaintext` |
| `injection_point` | enum | `system_prompt` \| `user_message` |
| `sections` | list | Named output sections or fields the format must contain (ordered) |
| `target_kind` | string | The artifact or task type this format serves (for discovery and routing) |
**Output**
A single `.md` file with YAML frontmatter (17 required fields) + 4 mandatory body sections: Format Overview, Sections, Example Output, Injection Instructions. The format specification must be written exactly as it will appear when injected into the prompt.
**Critical boundary**
- response_format = what the LLM sees during generation and uses to shape output (this builder)
- validation_schema = what the system checks *after* generation (different builder)
- parser = code that extracts structured data from LLM output (different builder)
- formatter = code that converts one format to another (different builder)
## Phases
### Phase 1: Research — Output Structure Design
Determine the exact structure the LLM must produce and how it will be consumed.
```
FOR each section in sections:
  classify:
    required:  LLM must always emit this section
    optional:  LLM emits only when relevant data is present
    repeated:  LLM emits one instance per item (array/list pattern)
  FOR json/yaml format:
    field_name (snake_case), value_type, nullable (bool)
  FOR markdown format:
    heading_level (##, ###), content_type (prose, list, table, code block)
  FOR csv format:
    column_name, data_type, column_order (integer)
  FOR plaintext format:
    structural constraints described as prose rules
injection_point selection:
  system_prompt:  format is a standing instruction (best for consistent output shape across sessions)
  user_message:   format is per-request (best for task-specific variation)
consumption context:
  WHO reads the output: human | parser | validation_schema | another LLM
  This affects how strict the format must be.
Check brain_query [IF MCP] for existing response_formats in same domain to avoid duplicates.
```
Deliverable: ordered section list with types, optionality, and injection strategy.
### Phase 2: Classify — Boundary Check
Confirm the artifact belongs to `response_format` and not a sibling kind.
```
IF caller wants code that parses the LLM's output into structured data:
  RETURN "Route to parser-builder — parsers extract data post-generation."
IF caller wants a schema to validate the LLM's output after generation:
  RETURN "Route to validation-schema-builder."
IF caller wants to transform the LLM's output from one format to another:
  RETURN "Route to formatter-builder."
IF caller wants to define a standing instruction the LLM follows:
  CHECK: is it about OUTPUT SHAPE (proceed here) or AGENT BEHAVIOR (route to system-prompt-builder)?
IF the format will be injected into the prompt so the LLM sees it during generation:
  PROCEED as response_format
```
Deliverable: confirmed `kind: response_format` with one-line justification.
### Phase 3: Compose — Build the Format Artifact
Assemble frontmatter and all 4 required body sections, following SCHEMA.md.
```
ID generation:
  id = "p05_rf_" + task_slug + "_" + format_type
  task_slug: snake_case, describes the task
  must conform to valid response_format id pattern
Frontmatter (all 17 required fields from SCHEMA.md):
  id, kind (= response_format), pillar (= P05), title, version,
  created, updated, author, task, format_type, injection_point,
  target_kind, sections (ordered list), sections_count (integer),
  quality (= null), tags, domain
Body sections (in this order):
  ## Format Overview
  One paragraph: what structure this format defines and for what task.
  State whether strict mode applies (LLM must follow exactly) or
  approximate mode (LLM uses format as a guide).
  ## Sections
  Ordered list of sections with per-section constraints:
    - Section name, heading level (for markdown), field names (for json/yaml)
    - Required vs optional for each section
    - Content type: prose | list | table | code block | key-value pairs
    - Cardinality for repeated sections (min/max items if known)
  ## Example Output
  At least one complete, realistic example.
  Must be valid for the declared format_type:
    json/yaml: parseable, no placeholder strings like "value1" or "string"
    markdown:  rendered section headers with realistic content
    csv:       header row + minimum 2 data rows
  Variables in example must match the sections list.

### bld_knowledge_card_response_format.md
---
kind: knowledge_card
id: bld_knowledge_card_response_format
pillar: P05
llm_function: INJECT
purpose: Domain knowledge for response_format production — atomic searchable facts
sources: response-format-builder MANIFEST.md + SCHEMA.md
---

# Domain Knowledge: response_format
## Executive Summary
A response_format is a template injected into the LLM prompt that specifies how the model must structure its output during generation — it is a pre-generation contract the LLM sees. Post-generation validation belongs to validation_schema (P06). Data extraction belongs to parser (P05). Format transformation belongs to formatter (P05). The response_format is guidance, not enforcement; clarity and a concrete example output are what drive compliance.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P05 (IO) |
| ID pattern | `^p05_rf_[a-z][a-z0-9_]+$` |
| Required frontmatter fields | 12 (includes `format_type` and `domain`) |
| Recommended fields | 4 (target_kind, example_output, variable_syntax, sections) |
| Max body | 4096 bytes |
| Body sections | 4 (Format Specification, Variables Table, Template Body, Example Output) |
| Section count constraint | 4–7 sections; consolidate if > 7 |
| Naming | `p05_rf_{format_slug}.yaml` |
## Patterns
| Pattern | Rule |
|---------|------|
| Format compliance hierarchy | JSON (95%) > YAML (90%) > Markdown tables (88%) > Numbered lists (85%) > Prose (70%) |
| Consumer-driven format_type | Machine consumer = `json`; config = `yaml`; human = `markdown` |
| Variable syntax tier 1 | `{{VARIABLE_NAME}}` — mustache, required; must have type + example in variables table |
| Variable syntax tier 2 | `[VARIABLE_NAME]` — bracket, optional; clearly marked as optional |
| Variables table completeness | Every variable requires: name, type, constraints, required/optional, example |
| Example Output section | Must be fully filled — no placeholders remaining in the example |
| Injection point selection | `system_prompt` for persistent structure; `user_message` for per-request context |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Untyped `{{value}}` variable | Forbidden — schema rejects variables without type + example |
| > 7 sections | Exceeds section limit; must consolidate |
| Prose-only template body | 70% LLM compliance — lowest tier; use structured format |
| `quality` non-null | Self-scoring forbidden; always `null` |
| Example Output section missing | LLM cannot verify output shape without a filled reference |
| Mixing mustache and bracket for same tier | Ambiguous variable precedence |
| response_format containing validation rules | Wrong artifact — post-generation validation belongs in validation_schema (P06) |
| Vague section names (`## Details`) | Use action-oriented names: `## Remediation Steps`, `## Score Breakdown` |
## Application
1. Identify the target artifact kind and consumer type (machine / config / human)
2. Select `format_type` based on consumer: machine = `json`, config = `yaml`, human = `markdown`
3. Write frontmatter: 12 required fields; `quality: null`; add `target_kind` and `sections` list
4. Write `## Format Specification` — output structure, format_type rationale, compliance notes
5. Write `## Variables Table` — every variable with type, constraints, required/optional, example
6. Write `## Template Body` — actual template using `{{REQUIRED}}` and `[OPTIONAL]` placeholders
7. Write `## Example Output` — fully filled; zero remaining placeholders
8. Verify body <= 4096 bytes; sections count 4–7; `id` matches filename stem
## References
- response-format-builder MANIFEST.md v1.0.0
- response_format SCHEMA.md v2.0.0
- Boundary: response_format (LLM sees, pre-gen) vs validation_schema (P06, system applies post-gen) vs parser (P05, extracts data) vs formatter (P05, transforms format)

### bld_quality_gate_response_format.md
---
id: p11_qg_response_format
kind: quality_gate
pillar: P11
title: "Gate: Response Format"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: response_format
quality: null
density_score: 0.85
tags:
  - quality-gate
  - response-format
  - p11
  - output-structure
  - llm
tldr: "Quality gate for LLM output structure specs: verifies format type, injection point, section definitions, and downstream parseability."
---

## Definition
A response format artifact specifies the exact output structure an LLM must produce. It declares a format type (json, yaml, markdown, csv, or plaintext), an injection point where the spec is delivered to the model (system prompt or user message), and a section structure with field-level definitions. The artifact is consumed by the LLM at generation time — it is not a post-generation validator.
Scope: files with `kind: response_format`. Does not apply to validation schemas (P06), which check outputs after generation.
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p05_rf_*` | `id.startswith("p05_rf_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `response_format` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 | `format_type` is one of: json, yaml, markdown, csv, plaintext | enum membership check |
| H08 | `injection_point` is one of: system_prompt, user_message | enum membership check |
| H09 | Section structure defined with at least one named section | sections table or list has >= 1 entry |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Each section has explicit field definitions (name, type, required/optional) | 1.0 |
| 3  | At least one complete example output present for the declared format | 1.0 |
| 4  | Injection point matches the use case (system for persistent structure, user for per-request) | 1.0 |
| 5  | Format is parseable by a downstream consumer without ambiguity | 1.0 |
| 6  | Tags list includes `response-format` | 0.5 |
| 7  | Scope note confirms this is for LLM generation time, not post-generation validation | 1.0 |
| 8  | Field constraints documented (max length, allowed values, nullable) | 1.0 |
| 9  | Fallback format described for partial or truncated LLM output | 0.5 |
| 10 | Format is compatible with the target model's context window and output style | 0.5 |
| 11 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 9.0. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; use as reference for format design |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Format is under active negotiation with a new model provider whose output style is not yet finalized |
| approver | Domain lead must approve in writing before bypass takes effect |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, and reason |
| expiry | 14 days from bypass grant; format must reach full compliance once model behavior is confirmed |

### bld_schema_response_format.md
---
kind: schema
id: bld_schema_response_format
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for response_format
pattern: TEMPLATE derives from this. CONFIG restricts this.
version: 2.0.0
---

# Schema: response_format
## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P05` |
| Type | literal `response_format` |
| Machine format | `yaml` (frontmatter yaml + md body) |
| Naming | `p05_rf_{format_slug}.yaml` |
| Max bytes | 4096 |
## Required Fields (12)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string, matches `^p05_rf_[a-z][a-z0-9_]+$` | YES | — | id == filename stem |
| kind | literal "response_format" | YES | — | Type discriminator |
| pillar | literal "P05" | YES | — | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update date |
| author | string | YES | — | Producer identity |
| format_type | enum: json, yaml, markdown, text, structured | YES | — | Output format; compliance: JSON 95% > YAML 90% > tables 88% > lists 85% > prose 70% |
| domain | string | YES | — | Domain this format covers |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Must include "response-format" |
| tldr | string <= 160ch | YES | — | Dense summary |
## Recommended Fields (4)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| target_kind | string | REC | Artifact kind that uses this format |
| example_output | string | REC | Concrete example of expected output |
| variable_syntax | enum: mustache, bracket | REC | tier1={{MUSTACHE}} for primary, tier2=[BRACKET] for secondary |
| sections | list[string] | REC | Ordered output section names |
## ID Pattern
```
^p05_rf_[a-z][a-z0-9_]+$
```
Rule: id MUST equal filename stem.
## Variable Syntax
| Tier | Syntax | Use |
|------|--------|-----|
| Primary (required vars) | `{{VARIABLE_NAME}}` | Mustache — always typed in variables table |
| Secondary (optional vars) | `[VARIABLE_NAME]` | Bracket — clearly marked optional |
Every variable MUST have type + example in the variables table. Untyped variables are forbidden.
## Body Structure (4 sections)
1. `## Format Specification` — what output structure this defines, format_type, compliance notes
2. `## Variables Table` — all variables with name, type, constraints, required/optional, example
3. `## Template Body` — the actual template with placeholders showing expected shape
4. `## Example Output` — complete filled example demonstrating correct output
## Compliance Note
Format preference hierarchy (by LLM compliance rate):
`JSON (95%) > YAML (90%) > Markdown tables (88%) > Numbered lists (85%) > Prose (70%)`
Choose format_type based on consumer: machine = json, config = yaml, human = markdown.
## Constraints
| Constraint | Value |
|-----------|-------|
| max_bytes | 4096 (body only) |
| naming | p05_rf_{format_slug}.yaml |
| id == filename stem | enforced |
| format_type | one of: json, yaml, markdown, text, structured |
| quality | ALWAYS null |
| sections | 4-7 per format (consolidate if >7) |
| variables | every variable typed + exampled |

### bld_examples_response_format.md
---
kind: examples
id: bld_examples_response_format
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of response_format artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: response-format-builder
## Golden Example
INPUT: "Cria response_format para knowledge_card output em YAML frontmatter + markdown"
OUTPUT:
```yaml
id: p05_rf_knowledge_card
kind: response_format
pillar: P05
title: "Response Format: Knowledge Card"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
target_kind: "knowledge_card"
format_type: "yaml"
injection_point: "system_prompt"
sections: [frontmatter, tldr, core_concepts, patterns, anti_patterns, quick_reference, references]
sections_count: 7
domain: "knowledge"
quality: null
tags: [response-format, knowledge-card, yaml-frontmatter, structured-output]
tldr: "KC output format: YAML frontmatter (id, kind, pillar, tags, tldr) + 6 markdown sections, injected in system_prompt"
example_output: "see body"
composable: false
density_score: 0.91
linked_artifacts:
  primary: "knowledge-card-builder"
  related: [p06_vs_knowledge_card, p01_kc_prompt_caching]
## Format Overview
Defines how the LLM should structure knowledge_card output: YAML frontmatter with required fields followed by 6 ordered markdown sections.
Injected in system_prompt so every KC production follows the same structure.
## Sections
| # | Section | Description | Required | Constraints |
|---|---------|-------------|----------|-------------|
| 1 | frontmatter | YAML block with id, kind, pillar, quality: null, tags, tldr | yes | all required fields per P01 schema |
| 2 | TL;DR | 1-2 sentence dense summary | yes | <= 160 chars, no filler |
| 3 | Core Concepts | Key facts as bullet list | yes | >= 3 bullets, <= 80 chars each |
| 4 | Patterns | Proven approaches | yes | >= 2 bullets with context |
| 5 | Anti-Patterns | What to avoid | yes | >= 1 bullet with why |
| 6 | Quick Reference | Commands, snippets, tables | yes | Actionable, copy-paste ready |
| 7 | References | Source URLs with dates | yes | >= 1 URL, verifiable |
## Example Output
```yaml
id: p01_kc_example_topic
kind: knowledge_card
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
domain: "example"
quality: null
tags: [example, knowledge-card, template]
tldr: "Example KC showing expected output structure with all 7 sections"
## TL;DR
Example knowledge card demonstrating the response format structure.
## Core Concepts
- First key concept with concrete data
- Second key concept with specific reference
- Third key concept with actionable detail
## Patterns
- Pattern 1: when X, do Y (proven in context Z)
- Pattern 2: use A instead of B (measured 30% improvement)
## Anti-Patterns
- Anti-pattern 1: avoid X because Y (causes Z failure)
## Quick Reference
| Command | Purpose |
|---------|---------|
| `example_cmd` | Does specific thing |
## References
- Source: https://example.com (2026-03-26)
```
## Injection Instructions
- **Point**: system_prompt
- **Position**: after identity rules, before task instructions
- **Template**: "When producing a knowledge_card, use the following output format:"
- **Composable**: false — KC format is self-contained
## References
- P01_knowledge/_schema.yaml: field definitions
- knowledge-card-builder SCHEMA.md: authoritative field reference
```
WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p05_rf_ pattern (H02 pass)
- kind: response_format (H04 pass)
- 17 required fields present (H07 pass)
- sections_count 7 >= 1 (H08 pass)
- format_type "yaml" in valid enum (H09 pass)
- injection_point "system_prompt" in valid enum (H10 pass)
- target_kind non-empty (H11 pass)
- Sections table with all 7 sections, ordered (S03 pass)
- Example Output complete and matches sections (S04 pass)
- Injection Instructions with point, position, template (S05 pass)
- tldr <= 160 chars, dense (S01 pass)
## Anti-Example
INPUT: "Format para output"
BAD OUTPUT:
```yaml
id: output_format
kind: format
pillar: Output
format_type: text
sections_count: 0

### bld_config_response_format.md
---
kind: config
id: bld_config_response_format
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for response_format production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: response_format Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p05_rf_{format_slug}.yaml | p05_rf_knowledge_card.yaml |
| Builder dir | kebab-case | response-format-builder/ |
| Fields | snake_case | format_type, injection_point, sections_count |
| Format slugs | lowercase_underscores | knowledge_card, model_card, signal_json |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P05_output/examples/p05_rf_{format_slug}.yaml
- Compiled: cex/P05_output/compiled/p05_rf_{format_slug}.json
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80
- Sections: >= 1 (recommend 3-7; LLMs struggle above 10)
## Format Policy
- format_type determines output structure the LLM follows
- json: highest compliance rate, best for machine consumption
- yaml: good for config-like output with frontmatter
- markdown: best for human-readable docs, supports headers/tables
- csv: tabular data only, simple extraction
- plaintext: unstructured, use only when no structure needed

### bld_output_template_response_format.md
---
kind: output_template
id: bld_output_template_response_format
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for response_format production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: response_format
```yaml
id: p05_rf_{{format_slug}}
kind: response_format
pillar: P05
title: "Response Format: {{format_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
target_kind: "{{artifact_kind_or_task}}"
format_type: "{{json_or_yaml_or_markdown_or_csv_or_plaintext}}"
injection_point: "{{system_prompt_or_user_message}}"
sections: [{{section_1}}, {{section_2}}, {{section_3}}]
sections_count: {{integer_gte_1}}
domain: "{{domain_value}}"
quality: null
tags: [response-format, {{target_kind}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
example_output: "see body"
composable: {{true_or_false}}
density_score: {{0.80_to_1.00}}
linked_artifacts:
  primary: "{{target_kind_builder}}"
  related: [{{related_artifact_refs}}]
## Format Overview
{{what_structure_this_defines_and_for_what_task}}
## Sections
| # | Section | Description | Required | Constraints |
|---|---------|-------------|----------|-------------|
| 1 | {{section_1}} | {{description}} | {{yes/no}} | {{constraints}} |
| 2 | {{section_2}} | {{description}} | {{yes/no}} | {{constraints}} |
| 3 | {{section_3}} | {{description}} | {{yes/no}} | {{constraints}} |
## Example Output
```{{format_type}}
{{complete_example_showing_expected_shape}}
```
## Injection Instructions
- **Point**: {{system_prompt_or_user_message}}
- **Position**: {{where_in_the_prompt}}
- **Template**: "Respond using the following format: {{format_description}}"
- **Composable**: {{true/false}} — {{explanation}}
## References
- {{reference_1}}
- {{reference_2}}
```

### bld_architecture_response_format.md
---
kind: architecture
id: bld_architecture_response_format
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of response_format — inventory, dependencies, and architectural position
---

# Architecture: response_format in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 19-field metadata header (id, kind, pillar, domain, format_type, etc.) | response-format-builder | active |
| format_type | Output structure type (json, yaml, markdown, csv, plaintext) | author | active |
| sections | Ordered sections the LLM must include in its response | author | active |
| field_definitions | Named fields with types and descriptions within each section | author | active |
| injection_point | Where the format is placed (system_prompt or user_message) | author | active |
| example_output | Concrete example showing a correctly formatted response | author | active |
## Dependency Graph
```
system_prompt   --injects-->    response_format  --consumed_by-->  LLM
response_format --produces-->   formatted_output  --validated_by--> validation_schema
response_format --signals-->    format_deviation
```
| From | To | Type | Data |
|------|----|------|------|
| system_prompt (P03) | response_format | data_flow | format injected into system prompt for LLM guidance |
| response_format | LLM | consumes | LLM reads format instructions during generation |
| response_format | formatted_output | produces | response structured according to format spec |
| formatted_output | validation_schema (P06) | data_flow | post-generation contract validates the output |
| formatted_output | parser (P05) | data_flow | parser extracts structured data from formatted output |
| response_format | format_deviation (P12) | signals | emitted when LLM output deviates from format |
## Boundary Table
| response_format IS | response_format IS NOT |
|--------------------|------------------------|
| An instruction injected into the prompt that the LLM sees | A post-generation contract the system enforces (validation_schema P06) |
| Guides how the LLM structures its output during generation | A data extractor applied after generation (parser P05) |
| Specifies sections, fields, and format type | A format converter between representations (formatter P05) |
| Placed at a specific injection point in the prompt | A naming convention for files or artifacts (naming_rule P05) |
| Defines what the response looks like, not what it contains | A task instruction defining what to accomplish (action_prompt P03) |
| Format type: json, yaml, markdown, csv, or plaintext | A binary or image output specification |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Injection | system_prompt, injection_point | Where and how the format enters the prompt |
| Definition | frontmatter, format_type, sections, field_definitions | Specify the structure the LLM must follow |
| Example | example_output | Concrete reference for the expected format |
| Generation | LLM, formatted_output | LLM produces output following the format |
| Validation | validation_schema, parser, format_deviation | Post-generation checking and data extraction |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `response-format-builder` for pipeline function `PRODUCE`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
