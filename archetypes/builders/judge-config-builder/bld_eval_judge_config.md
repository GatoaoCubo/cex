---
kind: quality_gate
id: p07_qg_judge_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate for judge_config ARTIFACTS (structure/fields, not runtime judgment accuracy)
quality: 9.0
title: "Quality Gate Judge Config"
version: "1.1.0"
author: n03_hybrid_review4
tags: [judge_config, builder, quality_gate]
tldr: "Tests the judge_config artifact structure. Judgment calibration accuracy is measured by eval runs, not by this gate."
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_examples_judge_config
  - bld_schema_judge_config
  - p07_qg_eval_framework
  - bld_knowledge_card_judge_config
  - p11_qg_llm_judge
  - bld_knowledge_card_llm_judge
  - scoring-rubric-builder
  - bld_collaboration_scoring_rubric
  - p12_qg_workflow_node
  - p01_kc_scoring_rubric
---

## Quality Gate

## Definition

| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| ID pattern match | ^p07_jc_[a-z][a-z0-9_]+\.md$ | matches | frontmatter.id |
| Max bytes | 4096 | <= | file size |
| Required sections | 5 | >= | body |
| Rubric levels defined | 1 | >= | body: Rubric |

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Valid YAML frontmatter | YAML parse error or missing frontmatter |
| H02 | ID matches ^p07_jc_[a-z][a-z0-9_]+\.md$ | ID does not match pattern |
| H03 | kind == "judge_config" | kind field missing or != "judge_config" |
| H04 | pillar == "P07" | pillar != "P07" |
| H05 | quality == null | quality self-scored (must be null) |
| H06 | judge_type in enum | judge_type not in [pairwise, rubric, reference_based, direct] |
| H07 | judge_model declared | judge_model field missing (provider + model required) |
| H08 | scoring_scale declared | scoring_scale missing (e.g., 1-5, 1-10, binary, pairwise) |
| H09 | judgment_criteria non-empty | criteria array missing or [] |
| H10 | Position bias mitigation noted (for pairwise) | judge_type==pairwise but no swap_order/randomize declared |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Schema compliance | 0.25 | All required frontmatter fields present, correct types |
| D2 | Rubric specificity | 0.20 | Each scale level has a descriptor (Prometheus-style anchored rubric) |
| D3 | Bias mitigation | 0.20 | Position bias, length bias, self-enhancement bias addressed |
| D4 | Reference grounding | 0.20 | Reference answer provided (for reference_based) or calibration examples listed |
| D5 | Industry alignment | 0.15 | Uses MT-Bench / G-Eval / Prometheus / Chatbot-Arena terminology correctly |

Weight check: 0.25 + 0.20 + 0.20 + 0.20 + 0.15 = 1.00

## Actions

| Score | Action |
|-------|--------|
| GOLDEN (>= 9.5) | Auto-approve, promote to examples library |
| PUBLISH (>= 8.0) | Approve as-is |
| REVIEW (>= 7.0) | Peer review required before publish |
| REJECT (< 7.0) | Rework; fix all HARD failures and re-submit |

## Bypass

| Conditions | Approver | Audit Trail |
|------------|----------|-------------|
| Exploratory judge (research-only, not for production eval) | Pillar owner (P07) | Log bypass with research context + expected deprecation date |

## Examples

## Golden Example
```markdown
---
kind: judge_config
name: llm_judge_automated_eval
---
model: "gpt-4o"
criteria:
  - relevance
  - coherence
  - factual_accuracy
scoring:
  threshold: 0.75
  scale: 1-5
api:
  endpoint: "https://api.openai.com/v1/engines/gpt-4o/completions"
  auth: "Bearer <API_KEY>"
  timeout: 30
```

## Anti-Example 1: Missing Essential Parameters
```markdown
---
kind: judge_config
name: incomplete_judge
---
model: "gpt-4o"
criteria: []
scoring:
  threshold: 0.75
```
## Why it fails
Lacks required evaluation criteria and API configuration, making the judge non-functional. Empty criteria list prevents any meaningful evaluation.

## Anti-Example 2: Human Rubric Contamination
```markdown
---
kind: judge_config
name: hybrid_judge
---
model: "gpt-4o"
criteria:
  - "Use 3-point rubric for grammar"
  - "Apply human-style feedback"
scoring:
  threshold: 0.5
  scale: "A-F"
```
## Why it fails
Mixes automated judge config with human rubric elements (letter grades, explicit feedback instructions). Contradicts boundary requirement to exclude scoring_rubric content.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
