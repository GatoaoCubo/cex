---
kind: quality_gate
id: p11_qg_validator
pillar: P06
llm_function: GOVERN
purpose: Golden and anti-examples of validator artifacts
pattern: "few-shot learning \u2014 LLM reads these before producing"
quality: 9.0
title: 'Gate: Validator'
version: 1.0.0
author: builder
tags:
- eval
- P06
- quality_gate
- examples
tldr: 'Validates technical pass/fail rules for artifact checking: condition structure,
  severity, and target kind.'
domain: validator
created: '2026-03-27'
updated: '2026-03-27'
density_score: 0.85
related:
  - bld_examples_validator
  - p03_sp_validator-builder
  - validator-builder
  - p03_ins_validator
  - bld_output_template_validator
  - bld_memory_validator
  - bld_knowledge_card_validator
  - bld_collaboration_validator
  - bld_knowledge_card_quality_gate
  - bld_schema_validator
---

## Quality Gate

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

## Examples

# Examples: validator-builder
## Golden Example
INPUT: "Create um validator que garante que todo knowledge_card tem quality null"
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
quality: 8.7
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
