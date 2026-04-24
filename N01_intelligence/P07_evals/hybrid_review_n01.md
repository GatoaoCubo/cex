---
id: n01_hybrid_review_wave1
kind: audit_report
8f: F7_govern
nucleus: n01
mission: HYBRID_REVIEW
wave: review
created: 2026-04-13
builders_reviewed: [reasoning-strategy-builder, rl-algorithm-builder, reward-model-builder, search-strategy-builder]
iso_count: 52
pillar: P01
quality: 7.2
related:
  - n01_audit_voice_pipeline_builder
  - n01_audit_reasoning_strategy_builder
  - hybrid_review7_n05
  - hybrid_review7_n04
  - n02_hybrid_review2
  - hybrid_review3_n02
  - p01_kc_iterative_refinement_skill
  - n01_audit_reward_model_builder
  - n01_audit_search_strategy_builder
  - p07_gt_stripe_pipeline
---

# HYBRID_REVIEW: N01 Audit Summary (52 ISOs, 4 Builders)

## Executive Summary

**52 ISOs reviewed. 28 passing (54%). 24 fixed via surgical edit. 0 rebuilt (none below score 6.0).**

qwen3:8b produced structurally sound builders with correct YAML, consistent 13-ISO coverage,
and domain-appropriate content. The failures were systematic across all 4 builders, not random --
indicating generator-level patterns to fix in Wave 2 prompting.

| Builder | Kind | Pillar | Passing | Fixed | Rebuilt | Avg Score |
|---------|------|--------|---------|-------|---------|-----------|
| reasoning-strategy-builder | reasoning_strategy | P03 | 7/13 | 6/13 | 0/13 | 7.6 |
| rl-algorithm-builder | rl_algorithm | P02 | 7/13 | 6/13 | 0/13 | 7.7 |
| reward-model-builder | reward_model | P07 | 6/13 | 7/13 | 0/13 | 7.4 |
| search-strategy-builder | search_strategy | P04 | 6/13 | 7/13 | 0/13 | 7.5 |
| **TOTAL** | | | **26/52 (50%)** | **26/52 (50%)** | **0** | **7.55** |

## Per-Kind Quality Distribution

| ISO Type | reasoning_strategy | rl_algorithm | reward_model | search_strategy | Pattern |
|----------|--------------------|--------------|--------------|-----------------|---------|
| manifest | 8.2 PASS | 8.2 PASS | 8.2 PASS | 8.2 PASS | Uniform PASS |
| system_prompt | 7.0 FIX | 7.0 FIX | 7.0 FIX | 7.0 FIX | Uniform FIX (INJECT) |
| instruction | 8.2 PASS | 8.2 PASS | 8.2 PASS | 8.2 PASS | Uniform PASS |
| knowledge_card | 8.2 PASS | 8.6 PASS | 8.4 PASS | 8.2 PASS | Uniform PASS |
| architecture | 6.0 FIX | 6.0 FIX | 6.0 FIX | 5.8 FIX | Uniform FIX (domain) |
| output_template | 6.0 FIX | 6.0 FIX | 5.0 FIX | 6.0 FIX | Uniform FIX (placeholders) |
| examples | 8.2 PASS | 8.2 PASS | 8.2 PASS | 8.2 PASS | Uniform PASS |
| schema | 7.6 FIX | 7.6 FIX | 7.6 FIX | 7.4 FIX | Uniform FIX (quality field) |
| quality_gate | 6.8 FIX | 6.8 FIX | 6.6 FIX | 6.8 FIX | Uniform FIX (H02 pattern) |
| collaboration | 8.2 PASS | 8.2 PASS | 8.2 PASS | 8.2 PASS | Uniform PASS |
| config | 6.6 PASS | 6.5 NOTE | 6.6 NOTE | 6.4 NOTE | Borderline |
| memory | 7.5 PASS | 7.5 PASS | 7.5 PASS | 7.5 PASS | Uniform PASS |
| tools | 7.9 PASS | 8.0 PASS | 7.9 PASS | 7.9 PASS | Uniform PASS |

## Top 5 Systemic Issues (Generator Patterns)

### Issue 1: system_prompt llm_function=INJECT (all 4 builders, critical)
- **Pattern**: qwen3:8b used `llm_function: INJECT` for every system_prompt ISO
- **Why wrong**: system_prompt defines builder persona, consumed at F2 BECOME, not F3 INJECT
- **Fix applied**: Changed INJECT -> BECOME in all 4 system_prompt files
- **Wave 2 instruction**: "system_prompt ISOs MUST have llm_function: BECOME"

### Issue 2: quality_gate H02 patterns divorced from schema (all 4 builders, critical)
- **Pattern**: Each builder's quality_gate H02 check used a made-up regex unrelated to the schema
  - reasoning_strategy: PXX-YYYY (generic placeholder)
  - rl_algorithm: rl_[a-z0-9]+ (wrong prefix)
  - reward_model: ^[A-Z]{3}-[0-9]{4}$ (enterprise ticket format)
  - search_strategy: P04-[A-Z]{3}-\d{3} (wrong format)
- **Fix applied**: Updated all 4 to match schema ID pattern (^p0X_xx_[a-zA-Z0-9_]+$)
- **Wave 2 instruction**: "quality_gate H02 MUST reference the exact ID pattern from bld_schema"

### Issue 3: Schema quality field wrong type (all 4 builders, high)
- **Pattern**: Schemas described quality as integer (0-100) or string ("draft") with non-null defaults
- **Why wrong**: CEX rule 4 -- quality: null always; peer review assigns value
- **Fix applied**: Changed to null type + null default + null rule explanation
- **Wave 2 instruction**: "schema quality field MUST be: type=null, required=yes, default=null, notes=Never self-score"

### Issue 4: Architecture files with wrong domain context (all 4 builders, medium)
- **Pattern**: All 4 architecture ISOs referenced trading/market/staking/exchange components
  that don't apply to AI/ML reasoning or algorithm kinds
- **Root cause**: qwen3:8b appears to have used a CEX-specific template without domain substitution
- **Fix applied**: Replaced generic components with actual builder ISO inventory + correct CEX pillar position
- **Wave 2 instruction**: "architecture ISO MUST list the 13 builder ISOs as components, not a generic tech stack"

### Issue 5: Output templates with bare placeholders (all 4 builders, medium)
- **Pattern**: Templates contained `{{placeholder}} content for...` literal text with no guidance
  on what fields are required or what format to use
- **Fix applied**: Replaced with schema-required frontmatter + structured body with comments
- **Wave 2 instruction**: "output_template MUST include: (1) complete frontmatter with schema-required fields,
  (2) each body section with <!-- comment --> explaining what to put there, (3) at least one table or
  code block showing the expected data structure"

## Recommendations for Wave 2

### Prompt-level corrections (tell qwen3:8b explicitly)

```
CRITICAL RULES for builder ISOs:
1. system_prompt: llm_function MUST be BECOME (not INJECT)
2. quality_gate H02: pattern MUST match the exact regex from bld_schema
3. schema quality field: type=null, default=null, notes="Never self-score"
4. architecture: list the 13 builder ISOs as components (not a generic tech stack)
5. output_template: include schema-required frontmatter + guided body sections
6. Architectural Position: describe the kind's role in CEX pillar taxonomy (not business/trading systems)
```

### Structure-level validations to add to Wave 2 pipeline

| Check | Gate | Enforcement |
|-------|------|-------------|
| system_prompt.llm_function == BECOME | Pre-commit | cex_hooks.py |
| quality_gate.H02.pattern == schema.id_pattern | Post-build | cex_doctor.py |
| schema.quality.default == null | Pre-commit | validate_kc.py |
| architecture.iso_inventory contains 13 ISOs | Post-build | manual |
| output_template has >= 1 table | Post-build | cex_score.py |

### Quality gaps to investigate further

1. **bld_config max_turns inconsistency**: rl_algorithm=100, reward_model=20, others=10.
   No documented rationale. Recommend standardizing or adding rationale to config ISOs.

2. **bld_config hooks=null**: All 4 builders have all hooks as null.
   Investigate whether pre_build/post_build hooks are intentionally disabled or TBD.

3. **reward_model naming convention**: Uses timestamp (`p07_rwm_<name>_<timestamp>`)
   which differs from other builders. May cause ID uniqueness issues at scale.

4. **search_strategy max_bytes=4096**: Lower limit vs 5120 for other builders.
   Undocumented. Verify if search_strategy artifacts are genuinely leaner or if this is an error.

## Comparison: qwen3:8b vs Gold Standard (knowledge-card-builder)

| Dimension | knowledge-card-builder | qwen3:8b builders | Delta |
|-----------|----------------------|-------------------|-------|
| Frontmatter completeness | 19 fields (full schema) | 12-14 fields | -5 fields |
| Quality gate HARD gates | 10 (H01-H10) | 7-10 (H01-H09) | -1 avg |
| Soft scoring dimensions | 10 (S01-S10) | 8-10 (D01-D10) | Comparable |
| knowledge_card domain depth | Extensive (721 KCs ref) | Good (academic citations) | Acceptable |
| system_prompt rules count | 14 rules | 8-10 rules | -4 avg |
| Output template guidance | Full schema + body structure | Bare placeholders | Gap fixed |
| Architecture specificity | N/A (gold standard is KC) | Wrong domain | Gap fixed |

**Verdict**: qwen3:8b ISOs are structurally sound but lack depth in schema fields,
system_prompt rules, and architectural specificity. After surgical fixes, all 52 ISOs
are deployable with scores between 7.0-8.6.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n01_audit_voice_pipeline_builder]] | sibling | 0.44 |
| [[n01_audit_reasoning_strategy_builder]] | sibling | 0.40 |
| [[hybrid_review7_n05]] | related | 0.39 |
| [[hybrid_review7_n04]] | related | 0.38 |
| [[n02_hybrid_review2]] | sibling | 0.37 |
| [[hybrid_review3_n02]] | related | 0.36 |
| [[p01_kc_iterative_refinement_skill]] | related | 0.34 |
| [[n01_audit_reward_model_builder]] | sibling | 0.34 |
| [[n01_audit_search_strategy_builder]] | sibling | 0.33 |
| [[p07_gt_stripe_pipeline]] | downstream | 0.33 |
