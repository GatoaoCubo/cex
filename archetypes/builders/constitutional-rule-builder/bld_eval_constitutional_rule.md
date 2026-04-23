---
id: bld_quality_gate_constitutional_rule
kind: quality_gate
pillar: P11
title: "Constitutional Rule Builder -- Quality Gate"
version: 1.0.0
quality: 8.3
tags: [builder, constitutional_rule, quality_gate]
llm_function: GOVERN
density_score: 1.0
updated: "2026-04-17"
related:
  - p11_qg_guardrail
  - p11_qg_chunk_strategy
  - p03_sp_guardrail_builder
  - bld_instruction_guardrail
  - p11_qg_quality_gate
  - p11_qg_validator
  - p11_qg_constraint_spec
  - p11_qg_creation_artifacts
  - bld_architecture_guardrail
  - p11_qg_builder
---

## Quality Gate

# Gate: constitutional_rule
## Threshold
>= 8.0 to publish (higher threshold because these are core safety rules); >= 9.5 for golden
## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Syntax error |
| H02 | id matches `^p11_cr_[a-z][a-z0-9_]+$` | Wrong pattern |
| H03 | id equals filename stem | Mismatch |
| H04 | kind == `constitutional_rule` | Any other value |
| H05 | quality == null | Non-null |
| H06 | bypass_policy == `none` | Any other value -- ABSOLUTE FAIL |
| H07 | core == true | Missing or false |
| H08 | constitutional_basis is valid enum | Unlisted value |
| H09 | principle is a single concrete prohibition | Vague or compound |
| H10 | severity == critical | Any other severity |
## SOFT Scoring
| Dim | Check | Weight |
|-----|-------|--------|
| S01 | Principle is concrete and testable (not abstract value) | 0.30 |
| S02 | At least 2 concrete violation examples | 0.20 |
| S03 | Detection method specified | 0.15 |
| S04 | Rationale explains why no exceptions exist | 0.15 |
| S05 | Boundary section distinguishes from guardrail and safety_policy | 0.10 |
| S06 | cai_reference or equivalent ethical grounding cited | 0.10 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN -- reference constitutional rule |
| >= 8.0 | PUBLISH |
| >= 7.0 | REVIEW -- principle or detection unclear |
| < 7.0 | REJECT -- likely has bypass or vague principle |

## Examples

# Examples: constitutional_rule
## Golden Example: AI Identity Honesty
```yaml
id: p11_cr_ai_identity_disclosure
kind: constitutional_rule
constitutional_basis: honesty
principle: "Never deny being an AI when a user sincerely asks whether they are talking to a human or an AI"
bypass_policy: none
core: true
severity: critical
detection_method: semantic_classifier
cai_reference: "CAI honesty principle 1"
tldr: "Absolute prohibition: never deny AI identity to a sincere human query. No bypass. Honesty basis."
```
## Golden Example: CSAM Prevention
```yaml
id: p11_cr_no_csam
kind: constitutional_rule
constitutional_basis: harm_prevention
principle: "Never generate, describe, or assist with creating sexual content involving minors under any circumstances"
bypass_policy: none
core: true
severity: critical
detection_method: keyword_filter + semantic_classifier
cai_reference: "CAI harm prevention principle 1"
```
## Anti-Pattern: Constitutional Rule with Bypass
```yaml
# WRONG -- bypass_policy present means this is a guardrail, not a constitutional rule
kind: constitutional_rule
bypass_policy: "Security lead may override with written approval"
# CORRECT: remove bypass entirely, or change kind to guardrail
kind: guardrail
bypass_policy: "Security lead; written sign-off required"
```
## Anti-Pattern: Vague Principle
```yaml
# WRONG -- not concrete, not testable
principle: "Be safe and helpful at all times"
# CORRECT: single concrete prohibition
principle: "Never provide step-by-step instructions for synthesizing biological agents capable of mass casualties"
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
