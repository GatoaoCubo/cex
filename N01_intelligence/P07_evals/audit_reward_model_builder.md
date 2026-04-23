---
id: n01_audit_reward_model_builder
kind: audit_report
nucleus: n01
mission: HYBRID_REVIEW
wave: review
created: 2026-04-13
builder: reward-model-builder
kind_reviewed: reward_model
pillar: P07
iso_count: 13
quality: 8.8
related:
  - n01_audit_rl_algorithm_builder
  - n01_audit_reasoning_strategy_builder
  - n01_audit_search_strategy_builder
  - n01_hybrid_review_wave1
  - n01_audit_voice_pipeline_builder
  - hybrid_review7_n04
  - n02_audit_action_paradigm_builder
  - hybrid_review7_n05
  - n02_audit_collaboration_pattern_builder
  - hybrid_review3_n04
---

# Audit: reward-model-builder (13 ISOs)

## ISO Score Table

| ISO | D1 Structural | D2 Density | D3 Alignment | D4 Complete | D5 Integration | Score | Action |
|-----|--------------|------------|--------------|-------------|----------------|-------|--------|
| bld_manifest | 9 | 8 | 8 | 8 | 8 | 8.2 | PASS |
| bld_system_prompt | 8 | 7 | 5 | 8 | 7 | 7.0 | FIXED: INJECT->BECOME |
| bld_instruction | 9 | 8 | 8 | 8 | 8 | 8.2 | PASS |
| bld_knowledge_card | 9 | 8 | 8 | 9 | 8 | 8.4 | PASS -- RLHF + ISO 23894 citations |
| bld_architecture | 6 | 6 | 5 | 7 | 6 | 6.0 | FIXED: staking/trading ref + ISO inventory |
| bld_output_template | 5 | 4 | 6 | 5 | 5 | 5.0 | FIXED: {{placeholder}} literal -> schema-guided |
| bld_examples | 9 | 8 | 8 | 8 | 8 | 8.2 | PASS -- Dialogue Quality RM golden example |
| bld_schema | 8 | 8 | 6 | 8 | 8 | 7.6 | FIXED: quality field said "draft" |
| bld_quality_gate | 8 | 7 | 3 | 8 | 7 | 6.6 | FIXED: H02 ^[A-Z]{3}-[0-9]{4}$ -> ^p07_rwm_* |
| bld_collaboration | 9 | 8 | 8 | 8 | 8 | 8.2 | PASS |
| bld_config | 7 | 6 | 7 | 7 | 6 | 6.6 | NOTE: timestamp in naming is non-standard |
| bld_memory | 8 | 7 | 7 | 8 | 7 | 7.5 | PASS |
| bld_tools | 8 | 7 | 8 | 8 | 8 | 7.9 | PASS -- bias_checker, HuggingFace evaluate |

## Quality Distribution

| Tier | Count | ISOs |
|------|-------|------|
| >= 8.0 (PASS) | 6 | manifest, instruction, knowledge_card, examples, collaboration, memory |
| 6-8 (SURGICAL FIX) | 7 | system_prompt, architecture, schema, quality_gate, config, tools, memory |
| < 6 (REBUILD) | 0 | - |

## Fixes Applied

| File | Defect | Fix |
|------|--------|-----|
| bld_system_prompt | llm_function: INJECT | Changed to BECOME (F2 identity function) |
| bld_quality_gate | H02 pattern: ^[A-Z]{3}-[0-9]{4}$ | Changed to ^p07_rwm_[a-zA-Z0-9]+$ per schema |
| bld_schema | quality field: string/"draft" | Changed to null with CEX null rule |
| bld_architecture | "trading and staking activities" | Replaced with ISO inventory + P07 pillar position |
| bld_output_template | {{placeholder}} literal text in body | Replaced with schema-required fields + structured sections |

## Notable Observations

- output_template was the weakest ISO (5.0) -- body sections had literal "{{placeholder}} content for..." text
- H02 pattern (^[A-Z]{3}-[0-9]{4}$) was the most incorrect of all 4 builders -- format completely wrong
- Config uses timestamp in naming convention (p07_rwm_<name>_<timestamp>) -- non-standard, may cause collision issues in high-frequency builds
- bld_tools includes human_evaluator tool -- appropriate for RLHF domain, validates domain expertise

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n01_audit_rl_algorithm_builder]] | sibling | 0.59 |
| [[n01_audit_reasoning_strategy_builder]] | sibling | 0.58 |
| [[n01_audit_search_strategy_builder]] | sibling | 0.55 |
| [[n01_hybrid_review_wave1]] | sibling | 0.46 |
| [[n01_audit_voice_pipeline_builder]] | sibling | 0.44 |
| [[hybrid_review7_n04]] | upstream | 0.38 |
| [[n02_audit_action_paradigm_builder]] | sibling | 0.36 |
| [[hybrid_review7_n05]] | upstream | 0.36 |
| [[n02_audit_collaboration_pattern_builder]] | sibling | 0.36 |
| [[hybrid_review3_n04]] | upstream | 0.35 |
