# CEX Crew Runner -- Builder Execution
**Builder**: `input-schema-builder`
**Function**: CONSTRAIN
**Intent**: reconstroi signal-builder
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:29:34.522518

## Intent Context
- **Verb**: reconstroi
- **Object**: signal-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_input_schema.md
---
id: input-schema-builder
kind: type_builder
pillar: P06
parent: null
domain: input_schema
llm_function: BECOME
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: EDISON
tags: [kind-builder, input-schema, P06, specialist, contract]
---

# input-schema-builder
## Identity
Especialista em construir input_schemas — contratos unilaterais de entrada.
Sabe tudo sobre field definitions, type constraints, required/optional fields,
default values, coercion rules, validation patterns,
and the boundary between input_schemas (P06), interfaces (P06 bilateral), and type_defs (P06 abstract).
## Capabilities
- Definir contratos de entrada com fields tipados e constraints
- Produzir input_schemas com frontmatter completo (20+ campos)
- Especificar defaults, coercion rules e error messages por field
- Compor examples para documentacao e testing
- Validar artifact contra quality gates (8 HARD + 10 SOFT)
## Routing
keywords: [input-schema, input, contract, entry, fields, required, defaults, coercion]
triggers: "define input contract for this agent", "what data does X need", "create entry schema"
## Crew Role
In a crew, I handle INPUT CONTRACTS.
I answer: "what data must be provided to this agent/operation?"
I do NOT handle: bilateral contracts (P06 interface), validation rules (P06 validator), abstract type definitions (P06 type_def).

### bld_instruction_input_schema.md
---
kind: instruction
id: bld_instruction_input_schema
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for input_schema
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an input_schema
## Phase 1: RESEARCH
1. Identify the operation or agent that needs this input contract — name it explicitly
2. List every piece of data the caller must provide; one field per line
3. Classify each field as required or optional; required fields have no fallback
4. Assign a type to each field: string, integer, float, boolean, list, or object
5. Define default values for every optional field (null is a valid default)
6. Specify coercion rules: what happens when a string arrives where an integer is expected, how nulls are treated, what triggers a type cast failure
7. Identify validation patterns per field: regex for strings, min/max for numbers, enum for fixed sets
8. Check existing input_schemas via brain_query [IF MCP] for the same operation — avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all frontmatter fields and constraints
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints exactly
3. Fill frontmatter: all 17 fields (null is acceptable for recommended fields)
4. Set quality: null — never self-score
5. Write the Fields section: one row per field with columns name / type / required / default / description
6. Write the Validation Rules section: per-field rules (regex pattern, numeric range, allowed enum values, custom constraints)
7. Write the Coercion Rules section: document every type conversion and null-handling behavior
8. Write the Error Messages section: one failure message per field that can fail validation
9. Write the Examples section: at least one complete, valid input object in YAML or JSON
10. Write the Constraints section: maximum field count, nesting depth limit, total payload size ceiling
11. Verify body is within 3072 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — apply each gate manually
2. HARD gates (all must pass):
   - YAML frontmatter parses without errors
   - id matches pattern `p06_is_[a-z][a-z0-9_]+`
   - kind == input_schema
   - fields list has at least one entry
   - every field entry has name and type
   - quality == null
3. SOFT gates (score each against QUALITY_GATES.md):
   - all required fields are explicitly marked
   - optional fields each have a default value specified
   - at least one complete example present
   - error messages cover all required fields
   - coercion behavior documented for any mixed-type field
4. Cross-check scope boundaries:
   - unilateral input contract (one receiver), not a bilateral interface?
   - not validation logic that belongs in a validator?
   - not an abstract type definition (type_def)?
   - defaults specified for all optional fields?
5. If score < 8.0: revise in the same pass before outputting

### bld_knowledge_card_input_schema.md
---
kind: knowledge_card
id: bld_knowledge_card_input_schema
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for input_schema production — unilateral entry contracts
sources: JSON Schema (draft-07), OpenAPI requestBody, Pydantic BaseModel, TypeScript params
---

# Domain Knowledge: input_schema
## Executive Summary
Input schemas are unilateral entry contracts — the receiving system declares what data it requires with types, constraints, defaults, and coercion rules. Rooted in JSON Schema and OpenAPI requestBody patterns. Input schemas differ from interfaces (bilateral contracts), validators (pass/fail rule checks), and type definitions (abstract reusable types).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P06 (contracts/schema) |
| Frontmatter fields | 20+ |
| Quality gates | 8 HARD + 10 SOFT |
| Direction | Unilateral (receiver defines) |
| Required per field | name, type, required/optional, description |
| Optional per field | default, coercion, error_message, examples |
## Patterns
- **Field type system**: every field has an explicit type with validation
| Source | Concept | Application |
|--------|---------|-------------|
| JSON Schema | Properties, required, types, defaults | Field definitions with types |
| OpenAPI | requestBody validation | Unilateral API input contracts |
| Pydantic | Data validation with defaults | Fields + coercion + defaults |
| TypeScript | Typed function parameters | Field-level type constraints |
| GraphQL | Input types for mutations | Structured input with defaults |
- **Required vs optional**: required fields block execution if missing; optional fields MUST have defaults
- **Coercion rules**: "123" → 123 when type is integer — handle LLM-generated mixed-type data gracefully
- **Field-level error messages**: each required field has its own error text for clear LLM-friendly feedback
- **Examples mandatory**: at least one valid payload example for testing and documentation
- **Versioning**: semver for schema evolution — breaking changes require major version bump
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Optional field without default | Undefined behavior when field missing |
| No type constraints | Any value accepted; runtime type errors |
| No coercion rules | LLM sends "42" as string; integer field rejects it |
| Missing error messages | Generic "validation failed" with no field context |
| No examples | Cannot test or document expected input format |
| Bilateral contract in input_schema | That is an interface, not an input_schema |
## Application
1. Identify scope: what operation/agent receives this input?
2. Define fields: name, type, required/optional, description per field
3. Set defaults: every optional field gets a default value
4. Add coercion: rules for type conversion (string→int, string→bool)
5. Write error messages: field-level, actionable text
6. Provide examples: at least one valid payload
## References
- JSON Schema: json-schema.org (draft-07+)
- OpenAPI: requestBody specification (spec.openapis.org)
- Pydantic: data validation for Python (docs.pydantic.dev)
- GraphQL: input type specification

### bld_quality_gate_input_schema.md
---
id: p11_qg_input_schema
kind: quality_gate
pillar: P11
title: "Gate: Input Schema"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: "input_schema — unilateral entry contracts defining required fields, types, and coercion rules"
quality: null
tags: [quality-gate, input-schema, contract, fields, validation, coercion]
tldr: "Gates ensuring input_schema artifacts define complete, typed, unambiguous entry contracts with defaults, coercion rules, and at least one example."
density_score: 0.89
---

# Gate: Input Schema
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: input_schema` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | Uppercase, spaces, or leading digit |
| H03 | ID equals filename stem | `id: create_input` in file `edit_input.md` |
| H04 | Kind equals literal `input_schema` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All required fields present | Missing: fields, required, version, or owner |
| H07 | Every field entry has `type` and `description` | Any field missing type or description |
| H08 | All fields listed in `required` exist in `fields` | Required list names a field not defined in fields |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Type precision | 1.0 | Types use constrained vocabulary (string, integer, float, boolean, list, object, enum) | Types present but use freeform labels | Types missing or `any` used |
| S02 | Default coverage | 1.0 | All optional fields have explicit `default` values | Most optionals have defaults | No defaults on optional fields |
| S03 | Coercion rules | 1.0 | Fields that accept coercion list source types and target type explicitly | Coercion mentioned but unspecified | No coercion documentation |
| S04 | Constraint documentation | 1.0 | Fields with constraints (min, max, pattern, enum values) fully documented | Some constraints documented | Constraints implied but not stated |
| S05 | Error messages | 0.5 | Per-field error message or error code defined | Generic error messages only | No error documentation |
| S06 | Examples | 1.0 | At least 2 complete examples (one valid, one invalid input) | One example present | No examples |
| S07 | Required vs optional clarity | 0.5 | All fields unambiguously classified in `required` list | Mostly clear with minor gaps | Mixed required/optional with no list |
| S08 | Unilaterality enforced | 1.0 | Schema defines input only; no output fields included | Mostly unilateral; minor output leakage | Bilateral — mixes input and output |
| S09 | Naming convention | 0.5 | All field names are snake_case | Mostly snake_case with exceptions | camelCase or mixed throughout |
| S10 | Owner linkage | 0.5 | `owner` field references a specific agent or service | Owner field present but generic | No owner |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to pool as golden input contract |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Rapidly evolving API where field set is not yet stable; schema explicitly marked `draft` |
| Approver | Owner agent lead |
| Audit trail | `bypass_reason` + `draft: true` both required in frontmatter |
| Expiry | Draft status expires after 14 days; must reach H-gate compliance or be deprecated |

### bld_architecture_input_schema.md
---
kind: architecture
id: bld_architecture_input_schema
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of input_schema — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| field_definitions | Typed entries the caller must or may provide | author | required |
| required_flags | Which fields are mandatory vs optional | author | required |
| type_constraints | Primitive or structured type per field (string, int, enum, object) | author | required |
| default_values | Fallback values applied when optional fields are absent | author | optional |
| coercion_rules | Type casting applied silently before validation | author | optional |
| error_messages | Human-readable feedback per validation failure | author | optional |
| examples | Concrete valid input objects for documentation and testing | author | recommended |
| schema_version | Version identifier for backward compatibility tracking | author | required |
## Dependency Graph
```
interface     --references--> input_schema
input_schema  --validates_via--> validator
input_schema  --informs--> action_prompt
system_prompt --documents--> input_schema
```
| From | To | Type | Data |
|------|----|------|------|
| interface | input_schema | data_flow | method signature requiring typed input shape |
| input_schema | validator | data_flow | field definitions and constraints to check |
| input_schema | action_prompt | data_flow | input format reference for prompt construction |
| system_prompt | input_schema | data_flow | documentation of required caller data |
## Boundary Table
| input_schema IS | input_schema IS NOT |
|-----------------|---------------------|
| Unilateral contract: defines what the callee needs | Bilateral contract defining both sides |
| Design-time artifact specifying required data shape | Runtime validation execution engine |
| Concrete field-level contract for one operation | Abstract reusable type definition |
| Documents required vs optional with defaults | Output shape specification |
| Applies coercion before validation | Integration contract between two agents |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Contract declaration | field_definitions, required_flags, schema_version | Define the shape of valid input |
| Type system | type_constraints, coercion_rules | Enforce and normalize data types |
| Defaults | default_values | Handle absent optional fields gracefully |
| Feedback | error_messages, examples | Enable caller self-correction and testing |
| Consumers | validator, action_prompt, interface | Enforce and reference the schema at use time |

### bld_collaboration_input_schema.md
---
kind: collaboration
id: bld_collaboration_input_schema
pillar: P12
llm_function: COLLABORATE
purpose: How input-schema-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: input-schema-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what data must be provided to this agent/operation?"
I do not define bilateral contracts. I do not validate output.
I specify unilateral input contracts so producers know exactly what data consumers require.
## Crew Compositions
### Crew: "Contract Stack"
```
  1. input-schema-builder -> "unilateral input contract (fields, types, defaults)"
  2. interface-builder -> "bilateral integration contract"
  3. formatter-builder -> "output format specification"
```
### Crew: "Prompt Engineering"
```
  1. input-schema-builder -> "input contract for the prompt"
  2. action-prompt-builder -> "task prompt respecting input schema"
  3. few-shot-example-builder -> "examples conforming to schema"
```
## Handoff Protocol
### I Receive
- seeds: consumer name, required fields with types
- optional: defaults, coercion rules, validation patterns, error messages
### I Produce
- input_schema artifact (.md + .yaml frontmatter)
- committed to: `cex/P06/examples/p06_input_{consumer}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Input schemas are defined from consumer requirements.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| action-prompt-builder | Prompts must respect input contract |
| chain-builder | Chain steps pass data conforming to input schemas |
| few-shot-example-builder | Examples must match input format |
| formatter-builder | Formatters transform data described by input schemas |
| interface-builder | Bilateral contracts compose from input schemas |

### bld_config_input_schema.md
---
kind: config
id: bld_config_input_schema
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: input_schema Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p06_is_{scope_slug}.yaml` | `p06_is_brain_query.yaml` |
| Builder directory | kebab-case | `input-schema-builder/` |
| Frontmatter fields | snake_case | `error_message`, `default` |
| Scope slugs | snake_case, lowercase | `brain_query`, `research_input` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P06_schema/examples/p06_is_{scope_slug}.yaml`
- Compiled: `cex/P06_schema/compiled/p06_is_{scope_slug}.json`
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total: ~4000 bytes including frontmatter
- Density: >= 0.80
## Field Type Enum
| Type | JSON equivalent | Example |
|------|----------------|---------|
| string | string | "hello" |
| integer | number (int) | 42 |
| float | number (float) | 3.14 |
| boolean | boolean | true |
| list | array | [1, 2, 3] |
| object | object | {key: value} |
## Required vs Optional Policy
- Required fields: MUST be provided by caller, error_message SHOULD be set
- Optional fields: MUST have default value, caller can omit
- No field can be both required AND have a default (required means caller provides)

### bld_examples_input_schema.md
---
kind: examples
id: bld_examples_input_schema
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of input_schema artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: input-schema-builder
## Golden Example
INPUT: "Define o input schema para o brain_query — o que precisa receber para buscar"
OUTPUT:
```yaml
id: p06_is_brain_query
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
scope: "brain_query search operation"
fields:
  - name: "query"
    type: "string"
    required: true
    default: null
    description: "Natural language search query"
    error_message: "query is required — provide a search string"
  - name: "max_results"
    type: "integer"
    required: false
    default: 10
    description: "Maximum number of results to return"
    error_message: null
  - name: "filters"
    type: "object"
    required: false
    default: null
    description: "Optional filters: {pillar, kind, domain, min_quality}"
    error_message: null
coercion:
  - from: "string"
    to: "integer"
    rule: "Parse max_results from string if numeric"
examples:
  - {query: "agent for research", max_results: 5}
  - {query: "P06 validators", filters: {pillar: "P06", kind: "validator"}}
domain: "brain-search"
quality: null
tags: [input-schema, brain-query, search, P10]
tldr: "Input contract for brain_query: requires query string, optional max_results and filters."
density_score: 0.90
```
## Contract Definition
brain_query receives search requests from any agent/satellite. Callers provide a natural
language query string, optional result limit, and optional filters by pillar/kind/domain.
## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | query | string | YES | - | Natural language search query |
| 2 | max_results | integer | NO | 10 | Max results to return |
| 3 | filters | object | NO | null | Filter by pillar, kind, domain, min_quality |
## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | integer | Parse max_results from string if numeric |
## Examples
```json
{"query": "agent for research", "max_results": 5}
```
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p06_is_ pattern (H02 pass)
- kind: input_schema (H04 pass)
- 13+ required fields present (H06 pass)
- fields has 3 entries with name/type/required (H07 pass)
- optional fields have defaults (H08 pass)
- scope is descriptive (S05 pass)
- tldr <= 160 chars, dense (S01 pass)
- tags list len >= 3, includes "input-schema" (S02 pass)
- YAML parses cleanly (H01 pass)
## Anti-Example
INPUT: "Input para brain query"
BAD OUTPUT:
```yaml
id: brain_input
kind: schema
pillar: Schema
scope: brain
fields: "query string and results count"
quality: 8.0
tags: input
```
Takes a query and returns results.
FAILURES:
1. id: no `p06_is_` prefix -> H02 FAIL
2. kind: "schema" not "input_schema" -> H04 FAIL
3. pillar: "Schema" not "P06" -> H03 FAIL
4. quality: 8.0 (not null) -> H05 FAIL
5. fields: string instead of list[object] -> H07 FAIL
6. scope: "brain" not descriptive -> S05 FAIL
7. tags: string not list, len < 3 -> S02 FAIL
8. body: filler prose ("Takes a query and returns results") -> S07 FAIL
9. no examples section -> S08 FAIL
10. no coercion section -> S06 FAIL

### bld_memory_input_schema.md
---
id: p10_lr_input_schema_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Input schemas with required fields that have default values create caller confusion — callers provide the default and the system rejects it as unnecessary. Optional fields without defaults force callers to handle None unexpectedly. Using 'any' or 'object' as a type without coercion rules causes silent data corruption downstream. Informative error messages that name the failing field and expected type reduce debug time by ~60% compared to generic 'validation error' messages."
pattern: "Every field must have: type (specific, not 'any'), required (boolean), and if optional then a default value. Required fields never have defaults. Optional fields always have defaults. Coercion rules must be declared explicitly when the input type differs from the processing type (e.g., string->int). Error messages must name the field and the expected type, not just say 'invalid input'."
evidence: "8 input schema reviews: 5 of 8 had required fields with defaults (caller confusion). 6 of 8 had at least one optional field without a default (None propagation bug). 3 of 8 used 'any' type on at least one field (silent coercion failure in 2 cases). Error messages with field names reduced caller debug time from avg 12min to avg 5min."
confidence: 0.70
outcome: SUCCESS
domain: input_schema
tags: [input-schema, validation, coercion, typed-fields, error-messages, contracts]
tldr: "Required fields never have defaults. Optional fields always have defaults. Every field needs a specific type. Error messages must name the failing field."
impact_score: 7.0
decay_rate: 0.05
satellite: edison
keywords: [input_schema, validation, required, optional, default, coercion, type, error_message, contract]
---

## Summary
Input schemas define the contract between a caller and a component. The most common failure mode is semantic confusion between required and optional: a required field with a default is a contradiction, and an optional field without a default creates None propagation bugs. Getting these two rules right eliminates the majority of runtime validation failures.
## Pattern
Field definition rules (all three must hold):
1. **Type specificity** - Use `string`, `integer`, `boolean`, `list`, `object`. Never `any` or `mixed`. If the raw input type differs from the processing type, declare a coercion rule.
2. **Required/optional semantics** - `required: true` means caller must provide it, no default. `required: false` means caller may omit it, default must be declared.
3. **Error message quality** - Each field's error message must include: field name, expected type/format, and what was received. Generic messages ("validation failed") are prohibited.
Coercion rule format: `coerce: "string -> integer via int()"` — explicit source type, target type, and conversion function. Declare coercion whenever accepting loose input (e.g., form data, CLI args, LLM output).
Input schemas cover only what goes in. Do not add response shapes or output fields — that is an interface contract (different artifact type).
## Anti-Pattern
- `required: true` with a `default` value — contradictory, creates caller confusion.
- `required: false` with no `default` — causes None to propagate silently through processing.
- `type: "any"` — disables type checking, causes silent coercion failures downstream.
- Generic error message ("invalid input") — forces callers to read source code to debug.
- Adding response/output shapes to the input schema — scope creep into interface territory.
- Fields list as a flat string instead of structured objects — unparseable by validators.
## Context

### bld_output_template_input_schema.md
---
kind: output_template
id: bld_output_template_input_schema
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an input_schema
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: input_schema
```yaml
id: p06_is_{{scope_slug}}
kind: input_schema
pillar: P06
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
scope: "{{what_operation_or_agent_this_serves}}"
fields:
  - name: "{{field_name}}"
    type: "{{string|integer|float|boolean|list|object}}"
    required: {{true|false}}
    default: {{default_value_or_null}}
    description: "{{what_this_field_is}}"
    error_message: "{{message_if_missing_or_invalid}}"
  - name: "{{field_name_2}}"
    type: "{{type}}"
    required: {{true|false}}
    default: {{default_value_or_null}}
    description: "{{description}}"
    error_message: "{{error_message_or_null}}"
coercion:
  - from: "{{source_type}}"
    to: "{{target_type}}"
    rule: "{{how_to_convert}}"
examples:
  - {{example_valid_payload_1}}
domain: "{{schema_domain}}"
quality: null
tags: [input-schema, {{scope_tag}}, {{domain_tag}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
```
## Contract Definition
{{what_operation_this_input_serves_and_who_provides_data}}
## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | {{name}} | {{type}} | {{Y/N}} | {{default}} | {{desc}} |
| 2 | {{name}} | {{type}} | {{Y/N}} | {{default}} | {{desc}} |
## Coercion Rules
| From | To | Rule |
|------|----|------|
| {{source}} | {{target}} | {{conversion}} |
## Examples
```json
{{valid_example_payload}}
```
## References
- {{reference_1}}
- {{reference_2}}

### bld_schema_input_schema.md
---
kind: schema
id: bld_schema_input_schema
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for input_schema
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: input_schema
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p06_is_{scope}) | YES | - | Namespace compliance |
| kind | literal "input_schema" | YES | - | Type integrity |
| pillar | literal "P06" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| scope | string | YES | - | What operation/agent this input serves |
| fields | list[object] | YES | - | Field definitions (min 1) |
| coercion | list[object] | REC | null | Type conversion rules |
| examples | list[object] | REC | - | Valid payload examples |
| domain | string | YES | - | Schema domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "input-schema" |
| tldr | string <= 160ch | YES | - | Dense summary |
| keywords | list[string] | REC | - | Brain search terms |
| density_score | float 0.80-1.00 | REC | - | Content density |
## Fields Object
```yaml
fields:
  - name: "topic"
    type: "string"
    required: true
    default: null
    description: "Research topic"
    error_message: "topic is required"
```
Each field MUST have: name, type, required. Optional: default, description, error_message.
Type: string, integer, float, boolean, list, object.
## Coercion Object
```yaml
coercion:
  - from: "string"
    to: "integer"
    rule: "Parse numeric string to int, fail if non-numeric"
```
## ID Pattern
Regex: `^p06_is_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Contract Definition` — what operation this input serves
2. `## Fields` — table with name/type/required/default/description
3. `## Coercion Rules` — type conversion rules (if any)
4. `## Examples` — at least one valid payload
## Constraints
- max_bytes: 3072 (body only)
- naming: p06_is_{scope}.yaml
- machine_format: json (compiled form)
- id == filename stem
- fields MUST have at least 1 entry
- each field MUST have name and type
- optional fields SHOULD have default values
- quality: null always
- input_schema is unilateral — defines what ONE receiver needs


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `input-schema-builder` for pipeline function `CONSTRAIN`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
