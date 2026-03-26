---
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
---
id: p06_val_kc_quality_null
kind: validator
pillar: P06
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
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
---
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

---

## Anti-Example

INPUT: "Valida knowledge cards"

BAD OUTPUT:

```yaml
---
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
---
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
