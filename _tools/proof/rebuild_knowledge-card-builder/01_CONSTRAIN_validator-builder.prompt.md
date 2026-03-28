# CEX Crew Runner -- Builder Execution
**Builder**: `validator-builder`
**Function**: CONSTRAIN
**Intent**: reconstroi knowledge-card-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:19.310813

## Intent Context
- **Verb**: reconstroi
- **Object**: knowledge-card-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_validator.md
---
id: validator-builder
kind: type_builder
pillar: P06
parent: null
domain: validator
llm_function: BECOME
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder
tags: [kind-builder, validator, P06, specialist, governance]
---

# validator-builder
## Identity
Especialista em construir validators — regras de validacao tecnica pass/fail.
Sabe tudo sobre pre-commit hooks, field validation, regex constraints,
severity levels, auto-fix policies, and the boundary between validators (P06),
quality gates (P11), and scoring rubrics (P07).
## Capabilities
- Definir regras de validacao com conditions estruturadas (field/operator/value)
- Produzir validators com frontmatter completo (22 campos)
- Classificar severity (error/warning/info) e determinar auto_fix viabilidade
- Compor bypass policies com audit trail
- Validar artifact contra quality gates (9 HARD + 10 SOFT)
## Routing
keywords: [validator, validation, pre-commit, rule, check, constraint, pass-fail]
triggers: "define validation rule", "what should be checked before commit", "create pre-commit validator"
## Crew Role
In a crew, I handle VALIDATION RULES.
I answer: "what technical check must pass before this artifact is accepted?"
I do NOT handle: quality gates with scoring (P11), scoring rubric criteria (P07), input schema contracts (P06 input_schema).

### bld_instruction_validator.md
---
id: p03_ins_validator
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Validator Builder Instructions
target: "validator-builder agent"
phases_count: 4
prerequisites:
  - "Target artifact kind is identified"
  - "The specific field or property to check is named"
  - "Severity level is determined: error, warning, or info"
  - "The check is binary pass/fail (not a score or range)"
validation_method: checklist
domain: validator
quality: null
tags: [instruction, validator, pre-commit, pass-fail, P06]
idempotent: true
atomic: true
rollback: "Delete generated validator YAML file"
dependencies: []
logging: true
tldr: "Build a validator YAML that encodes one binary pass/fail rule with structured conditions, severity, auto-fix policy, and bypass audit trail."
density_score: 0.93
---

## Context
The validator-builder produces a `validator` artifact -- a structured YAML that encodes a single binary pass/fail technical check. Validators run at defined pipeline checkpoints (pre-commit, post-generation, or on-demand) and either block, warn, or inform based on severity.
**Critical distinction**: a `validator` is a single binary rule. It is NOT a collection of field rules in a schema (`validation_schema` -- system applies multiple rules together), NOT a quality score with thresholds (`quality_gate` -- P11, produces a score), and NOT an input contract (`input_schema` -- governs what inputs are accepted). Confusing these produces checks at the wrong granularity.
**Input contract**:
- `rule_name`: string -- kebab-case rule identifier (e.g. `require-quality-null`, `id-matches-pattern`)
- `target_kind`: string -- the artifact kind this rule applies to
- `scope`: enum -- `pre_commit` | `post_generation` | `on_demand`
- `severity`: enum -- `error` | `warning` | `info`
- `conditions`: list of condition objects (see Phase 2)
- `auto_fix`: boolean -- whether the system can automatically correct violations
- `auto_fix_action`: string or null -- description of the correction applied if auto_fix is true
- `bypass_policy`: object or null -- conditions under which the rule can be bypassed
- `error_message`: string -- actionable message shown when the rule fails
- `remediation`: string -- steps the author can take to fix the violation
**Output contract**: a single `validator` YAML with all required fields, stored at `records/validators/{rule_name}.yaml`.
**Variables**:
- `{{rule_name}}` -- kebab-case rule identifier
- `{{target_kind}}` -- artifact kind the rule targets
- `{{condition_N}}` -- Nth condition object
- `{{error_message}}` -- violation message
- `{{remediation}}` -- fix instructions
## Phases
### Phase 1: Define the Rule and Determine Severity
**Action**: Translate the check requirement into a single focused rule with a severity assignment.
```
A valid validator encodes EXACTLY ONE check. If you have two checks, build two validators.
rule_name must describe the check, not the target:
  good: "require-quality-null"
  bad:  "system-prompt-validator"
severity assignment:
  error   -> failure blocks the pipeline; artifact is rejected
  warning -> failure logged; pipeline continues; author notified
  info    -> failure logged silently; no author notification
auto_fix eligibility:
  YES: string casing, whitespace, enum normalization, date format
  NO:  missing required fields, logic errors, structural violations,
       any change that alters semantic meaning
```
Verifiable exit: rule_name describes the check; severity is assigned; auto_fix eligibility is determined.
### Phase 2: Define Conditions
**Action**: Encode the check logic as a list of structured condition objects.
Condition object schema:
```
{
  field: string -- dot-notation path to the field being checked (e.g. "frontmatter.quality")
  operator: enum [equals, not_equals, exists, not_exists, matches, not_matches,
                  greater_than, less_than, contains, not_contains, in, not_in]
  value: the expected value or pattern
  negate: boolean -- if true, the condition passes when the check fails (logical NOT)
}
```
Composition rules:
- Multiple conditions default to AND (all must pass for the rule to pass)
- To express OR: use separate validators and a dispatch rule
- `matches` / `not_matches` require a valid regex in `value`
- `in` / `not_in` require a list in `value`
```
ASSERT len(conditions) >= 1
FOR each condition:
    ASSERT condition.field is a dot-notation path
    ASSERT condition.operator is a valid enum value
    ASSERT condition.value is defined (unless operator is exists/not_exists)
```
Verifiable exit: conditions list is non-empty; each condition has field, operator, and value where required.
### Phase 3: Define Error Handling and Bypass Policy
**Action**: Write the user-facing error message and optional bypass rules.
```
error_message format:
  "[field] [violation description]. Expected: [expected]. Got: [actual]."
  example: "frontmatter.quality must be null. Expected: null. Got: 8.5."
remediation format:
  Numbered steps the author takes to fix the violation.
  Max 3 steps. First step is always the most direct fix.
bypass_policy (optional):
  {
    allowed: boolean
    conditions: string -- when bypass is permitted
    approver: string -- who can approve a bypass
    audit_required: boolean -- whether bypass must be logged
  }
IF bypass_policy is null:
    the rule has no bypass -- all violations must be fixed
```
Verifiable exit: error_message names the field and states the expectation; remediation has >= 1 step.
### Phase 4: Validate Against Quality Gates
**Action**: Run 9 HARD gates before emitting; log 10 SOFT gates as warnings.
```
HARD gates (all must pass):
  H1: rule_name is kebab-case and describes the check (not the target)
  H2: target_kind is non-empty
  H3: scope is one of pre_commit, post_generation, on_demand
  H4: severity is one of error, warning, info
  H5: conditions list has >= 1 entry, each with field and operator
  H6: error_message names the field and states the expectation
  H7: auto_fix is false for any semantic/structural change
  H8: quality is null

### bld_knowledge_card_validator.md
---
kind: knowledge_card
id: bld_knowledge_card_validator
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for validator production — atomic searchable facts
sources: validator-builder MANIFEST.md + SCHEMA.md
---

# Domain Knowledge: validator
## Executive Summary
A `validator` (P06) is a deterministic, binary (pass/fail) technical check applied to an artifact before acceptance. It differs from `quality_gate` (weighted scoring 0–10), `scoring_rubric` (subjective evaluation), and `validation_schema` (silent post-generation contract) by being an explicit named rule with structured conditions, severity, and optional bypass policy. Validators enforce contracts; they do not measure quality.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P06 |
| Kind | `validator` |
| ID pattern | `^p06_val_[a-z][a-z0-9_]+$` |
| Naming | `p06_val_{rule}.yaml` |
| Max body | 3072 bytes |
| Machine format | yaml |
| Required frontmatter fields | 14 |
| Recommended fields | 4 |
| `severity` values | `error`, `warning`, `info` |
| `quality` field | always `null` |
| Result | pass/fail — no weighted scoring |
## Patterns
| Pattern | Rule |
|---------|------|
| Deterministic | Same input always produces same result — no randomness |
| Binary result | Pass or fail only — never a score, never a percentage |
| Composable | Multiple validators chain; all must pass for acceptance |
| Actionable error messages | Tell what to fix, not just what failed |
| Conditions as triples | Each condition: `(field, operator, value)` + optional `target` |
| `pre_commit: true` | Validator fires before git commit for that artifact kind |
| `auto_fix: true` | Only for safe, lossless repairs (casing, formatting, whitespace) |
| Bypass requires audit | `bypass.audit: true` always; `approver` names the authorizing role |
**Condition operators**:
| Operator | Use case |
|----------|----------|
| `eq` / `ne` | Exact match / mismatch |
| `gt` / `lt` / `gte` / `lte` | Numeric thresholds |
| `regex` | Pattern matching (IDs, naming) |
| `in` / `not_in` | Enum membership |
| `exists` | Field presence check |
| `type_check` | Type conformance |
**Condition targets**: `frontmatter` (default), `body`, `filename`
**Boundary — what validator is NOT**:
| kind | Why NOT validator |
|------|-----------------|
| `quality_gate` | Weighted scoring 0–10; validators are binary |
| `scoring_rubric` | Subjective criteria; validators are objective |
| `validation_schema` | Silent system contract; validators are explicit named rules |
| `input_schema` | Defines input shape; validators check rule conformance |
| `guardrail` | Behavioral safety limits; validators check data fields |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Numeric score in result | Validators are binary — scoring belongs in `quality_gate` |
| Empty `conditions` list | Schema HARD gate: at least 1 condition required |
| Vague `error_message` ("invalid") | Not actionable; user cannot fix without knowing what failed |
| `auto_fix: true` on lossy changes | Data loss is unsafe; auto-fix only for lossless repairs |
| `bypass` without `audit: true` | No governance trail; exception is untracked |
| `quality` set to a score | Never self-score; governance assigns |
| `id` not matching filename stem | Schema constraint violated; indexing breaks |
## Application
1. Name the rule in `rule` field (human-readable, e.g. `"id_namespace_compliance"`)
2. Set `id` = `p06_val_{rule_snake}`, must equal filename stem
3. Set `domain` to the artifact kind this validator governs
4. Set `severity`: `error` blocks, `warning` flags, `info` logs only
5. Set `pre_commit: true` if this fires before commit; `false` if post-acceptance
6. Write `conditions` list: at least 1 triple of `(field, operator, value)` with optional `target`
7. Write `error_message`: actionable — what to fix, not just what failed
8. Decide `auto_fix`: only `true` if repair is lossless and safe
9. If bypass is needed: define `bypass.conditions`, `bypass.approver`, `bypass.audit: true`

### bld_quality_gate_validator.md
---
id: p11_qg_validator
kind: quality_gate
pillar: P06
title: "Gate: Validator"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: validator
quality: null
density_score: 0.85
tags:
  - quality-gate
  - validator
  - rules
  - P06
tldr: "Validates technical pass/fail rules for artifact checking: condition structure, severity, and target kind."
---

## Definition
A validator defines one or more pass/fail rules applied to an artifact. Each rule has a condition (field, operator, value), a severity (error, warning, or info), and a target artifact kind. Validators do not score — they pass or fail. This gate ensures every validator is structurally sound, has actionable error messages, and is safe to run automatically.
## HARD Gates
Failure on any HARD gate causes immediate REJECT. No score is computed.
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid and complete with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p06_val_[a-z][a-z0-9_]+$` |
| H03 | ID equals filename | `id` slug matches the parent directory or filename stem |
| H04 | Kind matches literal | `kind` is exactly `validator` |
| H05 | Quality is null | `quality` field is `null` (not yet scored) |
| H06 | Required fields present | `target_kind`, `conditions`, `severity` all defined and non-empty |
| H07 | Condition structure valid | Each condition has `field`, `operator`, and `value` keys |
| H08 | Severity is valid enum | `severity` is one of: `error`, `warning`, `info` |
| H09 | Target artifact kind identified | `target_kind` names a specific artifact kind, not a generic scope |
| H10 | No scoring logic | Validator body contains no weighted scores, rubrics, or 0-10 scales |
## SOFT Scoring
Score each dimension 0 or 10. Multiply by weight. Divide total by sum of weights, scale to 0-10.
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Density >= 0.80 | 1.0 | No prose restating what the condition table shows |
| Standard operators only | 1.0 | Operators from: `eq`, `neq`, `gt`, `lt`, `gte`, `lte`, `regex`, `in`, `not_in` |
| Severity justification present | 0.5 | Each severity level has a brief reason |
| Auto_fix feasibility noted | 0.5 | `auto_fix: true` conditions describe what the fix does |
| Bypass policy present | 0.5 | Body includes a bypass section, even if `bypass: null` |
| Tags include validator | 0.5 | `tags` contains `"validator"` |
| Pipeline position documented | 1.0 | Body states when this runs (pre-commit, post-generate, pre-publish) |
| Error messages are actionable | 1.0 | Each message tells the developer what to fix, not just what is wrong |
| Performance impact minimal | 0.5 | Conditions require no external calls, file reads, or LLM inference |
| No scoring in validator | 1.0 | Pass/fail outcomes only; no weighted scores or rubrics |
Sum of weights: 7.5. `soft_score = sum(weight * gate_score) / 7.5 * 10`
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — archive to pool as reference validator |
| >= 8.0 | PUBLISH — safe to run in automated pipelines |
| >= 7.0 | REVIEW — runnable but error messages or pipeline placement needs clarification |
| < 7.0 | REJECT — do not run; conditions are ambiguous or severity is unjustified |
## Bypass
| Field | Value |
|-------|-------|
| condition | Validator targets a new artifact kind whose field structure is still being finalized; conditions may be temporarily incomplete |
| approver | Engineer who owns the target artifact kind |
| audit_log | Entry required in `.claude/bypasses/validator_{date}.md` listing which conditions are not yet enforced |
| expiry | Until target kind's QUALITY_GATES.md reaches PUBLISH score; validator must be updated at that point |
H01 (frontmatter parses) and H05 (quality is null) cannot be bypassed under any condition.

### bld_schema_validator.md
---
kind: schema
id: bld_schema_validator
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for validator
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: validator
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p06_val_{rule}) | YES | - | Namespace compliance |
| kind | literal "validator" | YES | - | Type integrity |
| pillar | literal "P06" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| rule | string | YES | - | Human-readable rule name |
| conditions | list[object] | YES | - | When this validator fires |
| error_message | string | YES | - | Message on failure |
| severity | enum: error, warning, info | YES | "error" | Failure severity |
| auto_fix | boolean | YES | false | Can system auto-remediate? |
| pre_commit | boolean | YES | false | Runs before commit? |
| threshold | number or null | REC | null | Numeric threshold if applicable |
| bypass | object {conditions, approver} | REC | null | Bypass policy |
| logging | boolean | REC | true | Log validation results? |
| domain | string | YES | - | What artifact kind this validates |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "validator" |
| tldr | string <= 160ch | YES | - | Dense summary |
| density_score | float 0.80-1.00 | REC | - | Content density |
## Conditions Object
```yaml
conditions:
  - field: "{{field_name}}"
    operator: "{{eq|ne|gt|lt|gte|lte|regex|in|not_in|exists|type_check}}"
    value: "{{expected_value}}"
    target: "{{frontmatter|body|filename}}"
```
Operators: eq, ne, gt, lt, gte, lte, regex, in, not_in, exists, type_check.
Target: frontmatter (default), body, filename.
## Bypass Object
```yaml
bypass:
  conditions: ["{{when_bypass_allowed}}"]
  approver: "{{role_or_name}}"
  audit: true
```
## ID Pattern
Regex: `^p06_val_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Rule Definition` — what is checked, in plain language
2. `## Conditions` — structured conditions table (field, operator, value)
3. `## Error Handling` — error_message, severity, remediation steps
4. `## Bypass Policy` — when bypass is allowed, who approves
## Constraints
- max_bytes: 3072 (body only)
- naming: p06_val_{rule}.yaml
- machine_format: yaml
- id == filename stem
- severity MUST be one of: error, warning, info
- conditions MUST have at least 1 entry
- quality: null always
- validator is pass/fail — no weighted scoring (that is quality_gate P11)

### bld_examples_validator.md
---
kind: examples
id: bld_examples_validator
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of validator artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: validator-builder
## Golden Example
INPUT: "Cria um validator que garante que todo knowledge_card tem quality null"
OUTPUT:
```yaml
id: p06_val_kc_quality_null
kind: validator
pillar: P06
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
rule: "Knowledge card quality must be null"
conditions:
  - field: "quality"
    operator: "eq"
    value: null
    target: "frontmatter"
  - field: "kind"
    operator: "eq"
    value: "knowledge_card"
    target: "frontmatter"
error_message: "quality must be null — never self-score. Remove the numeric value and set quality: null."
severity: "error"
auto_fix: true
pre_commit: true
threshold: null
bypass:
  conditions: ["calibration run with known golden artifacts"]
  approver: "p06-chief"
  audit: true
logging: true
domain: "knowledge_card"
quality: null
tags: [validator, knowledge-card, quality-null, pre-commit]
tldr: "Blocks knowledge_cards with non-null quality — self-scoring is forbidden."
density_score: 0.92
```
## Rule Definition
Every knowledge_card artifact MUST have `quality: null` in frontmatter.
Self-assigned quality scores corrupt the evaluation pipeline.
## Conditions
| # | Field | Operator | Value | Target |
|---|-------|----------|-------|--------|
| 1 | quality | eq | null | frontmatter |
| 2 | kind | eq | knowledge_card | frontmatter |
## Error Handling
- **Message**: quality must be null — never self-score. Remove the numeric value and set quality: null.
- **Severity**: error (blocks commit)
- **Auto-fix**: yes — set quality: null
- **Remediation**: Open file, find `quality:` line, replace value with `null`
## Bypass Policy
- **Conditions**: calibration run with known golden artifacts
- **Approver**: p06-chief
- **Audit**: always logged
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p06_val_ pattern (H02 pass)
- kind: validator (H04 pass)
- 22 required fields present (H06 pass)
- severity is valid enum "error" (H07 pass)
- conditions has 2 entries (H08 pass)
- error_message is actionable — tells HOW to fix (S05 pass)
- tldr <= 160 chars, dense (S01 pass)
- tags list len >= 3, includes "validator" (S02 pass)
- YAML parses cleanly (H01 pass)
## Anti-Example
INPUT: "Valida knowledge cards"
BAD OUTPUT:
```yaml
id: kc_validator
kind: validation
pillar: Schema
rule: check KC
conditions: "quality should be null"
error_message: Invalid
severity: critical
auto_fix: maybe
quality: 8.5
tags: validator
```
Quality check for KCs. Makes sure things are good.
FAILURES:
1. id: no `p06_val_` prefix -> H02 FAIL
2. kind: "validation" not "validator" -> H04 FAIL
3. pillar: "Schema" not "P06" -> H03 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. conditions: string instead of list[object] -> H08 FAIL
6. severity: "critical" not in enum -> H07 FAIL
7. auto_fix: "maybe" not boolean -> H09 FAIL
8. tags: string not list, len < 3 -> S02 FAIL
9. error_message: "Invalid" — not actionable -> S05 FAIL
10. body: filler prose ("makes sure things are good") -> S07 FAIL

### bld_config_validator.md
---
kind: config
id: bld_config_validator
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: validator Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p06_val_{rule_slug}.yaml` | `p06_val_kc_quality_null.yaml` |
| Builder directory | kebab-case | `validator-builder/` |
| Frontmatter fields | snake_case | `error_message`, `auto_fix` |
| Rule slugs | snake_case, lowercase | `kc_quality_null`, `id_prefix_check` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P06_schema/examples/p06_val_{rule_slug}.yaml`
- Compiled: `cex/P06_schema/compiled/p06_val_{rule_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total: ~4000 bytes including frontmatter
- Density: >= 0.80
## Severity Enum
| Value | Meaning | Effect |
|-------|---------|--------|
| error | Blocks acceptance | Artifact cannot be committed/published |
| warning | Flags issue | Artifact accepted but flagged for review |
| info | Informational | Logged only, no blocking |
## Operator Enum
| Operator | Meaning | Example |
|----------|---------|---------|
| eq | Equals | `quality eq null` |
| ne | Not equals | `kind ne ""` |
| gt / lt | Greater/less than | `density_score gt 0.80` |
| gte / lte | Greater/less or equal | `version gte "1.0.0"` |
| regex | Regex match | `id regex "^p06_val_"` |
| in | Value in list | `severity in [error, warning, info]` |
| not_in | Value not in list | `author not_in [orchestrator]` |
| exists | Field exists | `tldr exists true` |
| type_check | Type assertion | `conditions type_check list` |
## Auto-Fix Policy
- auto_fix: true ONLY for deterministic, safe repairs (formatting, casing, null insertion)
- auto_fix: false for anything requiring semantic judgment
- When auto_fix: true, the fix MUST be documented in Error Handling section

### bld_output_template_validator.md
---
kind: output_template
id: bld_output_template_validator
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a validator
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: validator
```yaml
id: p06_val_{{rule_slug}}
kind: validator
pillar: P06
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
rule: "{{human_readable_rule_name}}"
conditions:
  - field: "{{field_name}}"
    operator: "{{operator}}"
    value: "{{expected_value}}"
    target: "{{frontmatter|body|filename}}"
error_message: "{{actionable_error_text}}"
severity: "{{error|warning|info}}"
auto_fix: {{true|false}}
pre_commit: {{true|false}}
threshold: {{number_or_null}}
bypass:
  conditions: ["{{bypass_condition}}"]
  approver: "{{approver_role}}"
  audit: true
logging: {{true|false}}
domain: "{{artifact_kind_this_validates}}"
quality: null
tags: [validator, {{domain_tag}}, {{rule_tag}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
```
## Rule Definition
{{plain_language_description_of_what_is_checked}}
## Conditions
| # | Field | Operator | Value | Target |
|---|-------|----------|-------|--------|
| 1 | {{field}} | {{op}} | {{val}} | {{target}} |
| 2 | {{field}} | {{op}} | {{val}} | {{target}} |
## Error Handling
- **Message**: {{error_message}}
- **Severity**: {{severity}}
- **Auto-fix**: {{yes_no_and_how}}
- **Remediation**: {{steps_to_fix_manually}}
## Bypass Policy
- **Conditions**: {{when_bypass_is_allowed}}
- **Approver**: {{who_can_approve}}
- **Audit**: always logged
## References
- {{reference_1}}
- {{reference_2}}

### bld_architecture_validator.md
---
kind: architecture
id: bld_architecture_validator
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of validator — inventory, dependencies, and architectural position
---

# Architecture: validator in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 22-field metadata header (id, kind, pillar, domain, target_kind, severity, etc.) | validator-builder | active |
| conditions | Structured check rules (field, operator, value) that define pass/fail | author | active |
| severity_level | Classification of violation impact: error, warning, or info | author | active |
| auto_fix_policy | Whether violations can be automatically repaired and how | author | active |
| bypass_policy | Conditions under which the validator can be skipped with audit | author | active |
| audit_trail | Logging requirements for validation runs and bypass events | author | active |
## Dependency Graph
```
artifact (any)  --checked_by-->  validator  --produces-->    pass_fail_result
quality_gate    --depends-->     validator  --signals-->     validation_event
validator       --depends-->     type_def
```
| From | To | Type | Data |
|------|----|------|------|
| artifact (any) | validator | data_flow | artifact submitted for validation check |
| validator | pass_fail_result | produces | boolean pass/fail with severity and message |
| quality_gate (P11) | validator | dependency | gates compose validators as hard check components |
| type_def (P06) | validator | dependency | type definitions inform field and constraint checks |
| validator | validation_event (P12) | signals | emitted on pass, fail, or bypass |
| law (P08) | validator | dependency | laws may mandate specific validation rules |
## Boundary Table
| validator IS | validator IS NOT |
|--------------|-----------------|
| A technical pass/fail check with structured conditions | A multi-dimensional scoring framework (scoring_rubric P07) |
| Classified by severity (error/warning/info) | A quality barrier with scoring formula (quality_gate P11) |
| Supports auto_fix for recoverable violations | A post-generation schema contract (validation_schema P06) |
| Includes bypass policy with audit trail | An input contract for operations (input_schema P06) |
| Applied to individual rules — atomic checks | A reusable type declaration (type_def P06) |
| Runs at pre-commit or pre-promotion checkpoints | A response format instruction for the LLM (response_format P05) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Input | artifact, type_def | Artifact under check and type constraints |
| Rules | frontmatter, conditions, severity_level | Define what is checked and how severe violations are |
| Remediation | auto_fix_policy, bypass_policy | Handle violations via fix or approved skip |
| Audit | audit_trail | Log validation runs and bypass events |
| Output | pass_fail_result, validation_event, quality_gate | Deliver result and feed into quality gates |

### bld_collaboration_validator.md
---
kind: collaboration
id: bld_collaboration_validator
pillar: P06
llm_function: COLLABORATE
purpose: How validator-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: validator-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what technical check must pass before this artifact is accepted?"
I define individual pass/fail rules with structured conditions (field/operator/value), severity levels (error/warning/info), and auto-fix policies. I do NOT produce quality gates with scoring (quality-gate-builder), scoring rubric criteria (scoring-rubric-builder), or input schema contracts (input-schema-builder).
## Crew Compositions
### Crew: "Artifact Governance Pipeline"
```
  1. type-def-builder -> "establishes field types and constraints that validators reference"
  2. validation-schema-builder -> "defines the structural output contract at schema level"
  3. validator-builder -> "adds individual pre-commit rules: field checks, regex, severity, bypass"
```
### Crew: "Pre-Commit Quality Gate"
```
  1. validator-builder -> "defines pass/fail rules that run before the artifact is accepted"
  2. quality-gate-builder -> "applies weighted scoring after all validators pass"
  3. unit-eval-builder -> "verifies the artifact passes both validators and functional tests"
```
## Handoff Protocol
### I Receive
- seeds: artifact kind to validate, field list with constraints, severity requirements
- optional: regex patterns, enum constraints, auto_fix candidates, bypass policy, audit trail requirements
### I Produce
- validator artifact (YAML, frontmatter 22 fields, structured conditions, max 100 lines)
- committed to: `cex/P06_schema/examples/p06_val_{rule_slug}.yaml`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- type-def-builder: field type definitions inform the operator and value choices in rule conditions
- validation-schema-builder: schema-level contracts reveal which fields need individual validator coverage
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| quality-gate-builder | uses validators as the HARD gate checklist source before scoring |
| workflow-builder | workflow steps run validators as acceptance gates before advancing |
| unit-eval-builder | test assertions may verify that validators correctly catch invalid inputs |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `validator-builder` for pipeline function `CONSTRAIN`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
