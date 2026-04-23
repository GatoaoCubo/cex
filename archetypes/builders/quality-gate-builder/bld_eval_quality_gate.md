---
kind: quality_gate
id: p11_qg_quality_gate
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of quality_gate artifacts
quality: 9.0
title: 'Gate: Quality Gate'
version: 1.0.0
author: builder
tags:
- eval
- P11
- quality_gate
- examples
tldr: 'Recursive quality gate for quality_gate artifacts: verifies HARD/SOFT structure,
  weight math, and bypass rules.'
domain: quality_gate
created: '2026-03-27'
updated: '2026-03-27'
density_score: 0.85
related:
  - bld_knowledge_card_quality_gate
  - bld_examples_quality_gate
  - p11_qg_response_format
  - p11_qg_creation_artifacts
  - p11_qg_orchestration_artifacts
  - p11_qg_marketing_artifacts
  - p11_qg_prompt_template
  - p11_qg_intelligence_artifact
  - p11_qg_runtime_state
  - p11_qg_chunk_strategy
---

## Quality Gate

## Definition
A quality gate artifact defines the acceptance criteria for one artifact kind. It contains blocking HARD gates (binary pass/fail), a weighted SOFT scoring table, a four-tier action map, and a bypass policy. This gate is self-applicable: it evaluates other quality gate files, including itself.
Scope: files with `kind: quality_gate`. Does not apply to scoring rubrics (P08), validators (P07), or benchmark suites (P13).
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p11_qg_*` | `id.startswith("p11_qg_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `quality_gate` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 | HARD gates section present with >= 6 gates | count rows in HARD Gates table >= 6 |
| H08 | SOFT scoring table present with weights that sum to 100% when normalized | sum(weight_i / total_weight) == 1.0 within float tolerance |
| H09 | Actions section present with all four tiers: GOLDEN, PUBLISH, REVIEW, REJECT | all four tier names present in Actions table |
| H10 | Bypass section present with condition, approver, audit_log, and expiry fields | all four fields non-empty in Bypass table |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Universal HARD gates H01-H06 (YAML, id namespace, id=filename, kind, quality null, required fields) are all present | 1.0 |
| 3  | SOFT weights use only values 0.5 or 1.0 (no fractional intermediates) | 0.5 |
| 4  | Scoring formula is documented inline (not just assumed) | 1.0 |
| 5  | Bypass section explicitly states H01 and H05 cannot be bypassed | 1.0 |
| 6  | Tags list includes `quality-gate` | 0.5 |
| 7  | Tier thresholds match standard: GOLDEN >= 9.5, PUBLISH >= 8.0, REVIEW >= 7.0, REJECT < 7.0 | 1.0 |
| 8  | Every gate predicate is testsble (binary outcome, no subjective language) | 1.0 |
| 9  | Gate set is domain-adapted, not a copy-paste of a generic template | 1.0 |
| 10 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 8.5. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; use as reference for new gate authors |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Gate covers an experimental artifact kind in active design (schema not yet stable) |
| approver | Pillar owner must approve in writing before bypass takes effect |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, and reason |
| expiry | 14 days from bypass grant; gate must reach full compliance before expiry |

## Examples

# Examples: quality-gate-builder
## Golden Example
INPUT: "Define gate for knowledge_cards antes de publicar no pool"
OUTPUT:
```yaml
id: p11_qg_kc_publish
kind: quality_gate
pillar: P11
title: "Gate: KC Publish"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "system"
domain: "knowledge_card"
quality: null
tags: [quality-gate, knowledge-card, pre-publish]
tldr: "Pre-publish gate for KCs: 10 HARD checks + 5-dimension scoring >= 8.0"
density_score: 0.92
## Definition
| Property | Value |
|----------|-------|
| Metric | combined_score |
| Threshold | 8.0 |
| Operator | >= |
| Scope | All knowledge_card artifacts before pool merge |
## Checklist (HARD)
- [ ] YAML parses without error
- [ ] id starts with p01_kc_
- [ ] id == filename stem
- [ ] kind == knowledge_card
- [ ] quality == null
- [ ] body >= 3 bullet points
- [ ] size <= 5120 bytes
## Scoring (SOFT)
| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Density | 25% | >= 0.80 |
| Completeness | 25% | All required fields present |
| Actionability | 20% | Concrete examples or commands |
| Boundary | 15% | IS/IS NOT section |
| References | 15% | >= 1 source URL |
## Actions
| Result | Action | Escalation |
|--------|--------|------------|
| Pass >= 8.0 | Merge to pool | None |
| Fail < 8.0 | Return with report | Retry required |
## Bypass
- Conditions: SOFT 7.0-7.9 with architect approval
- Approver: p01-chief [PLANNED]
- Audit: bypass in commit message
```
## Anti-Example
```yaml
id: quality_check
kind: quality_gate
title: "Make sure it's good"
quality: 9.0
Check that the artifact is high quality. If good enough, approve.
```
FAILURES:
1. id: no p11_qg_ prefix
2. lp: missing
3. quality: self-scored
4. "good enough": subjective, not measurable
5. No Definition table, no scoring, no bypass

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
