---
id: hybrid_review3_n02
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW3 Audit: model_architecture (N02)"
version: 1.0.0
quality: 8.6
density_score: 0.95
tags: [audit, hybrid_review3, model_architecture, gemma4, wave2]
domain: ML architecture quality assurance
created: "2026-04-14"
---

# HYBRID_REVIEW3 Audit: model_architecture (N02)

## Executive Summary

**13 ISOs reviewed. 10 passing (77%). 2 fixed via surgical edit. 1 rebuilt. 0 below 6.0.**

model_architecture builder (gemma4:26b origin) shows notably better quality than prior Wave 2
builders. D01 (system_prompt INJECT) is NOT present -- gemma4 correctly used BECOME here.
D04 (domain contamination) is absent -- all content covers neural net architectures, not
finance/trading. D09 (generic architecture) is absent -- architecture ISO correctly documents
13-ISO builder structure. Main defects: D08 (stub quality_gate), D02 (wrong memory kind), D10
(stale SCHEMA.md reference).

| Builder | Kind | Pillar | Passing | Fixed | Rebuilt | Avg Score |
|---------|------|--------|---------|-------|---------|-----------|
| model-architecture-builder | model_architecture | P02 | 10/13 | 2/13 | 1/13 | 8.7 |

---

## Per-ISO 5D Scores

| ISO | D1 Struct | D2 Domain | D3 Density | D4 CEX | D5 Industry | Avg | Action |
|-----|-----------|-----------|-----------|--------|-------------|-----|--------|
| bld_manifest | 9.0 | 9.0 | 8.5 | 8.5 | 8.5 | 8.7 | PASS |
| bld_system_prompt | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | PASS |
| bld_instruction | 9.0 | 9.0 | 8.5 | 7.0 | 8.5 | 8.4 | FIX |
| bld_knowledge_card | 9.5 | 9.5 | 9.0 | 9.0 | 9.5 | 9.3 | PASS |
| bld_schema | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | PASS |
| bld_quality_gate | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | REBUILD |
| bld_output_template | 9.0 | 9.0 | 8.5 | 9.0 | 9.0 | 8.9 | PASS |
| bld_architecture | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | PASS |
| bld_examples | 9.5 | 9.5 | 9.0 | 9.0 | 9.5 | 9.3 | PASS |
| bld_collaboration | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | PASS |
| bld_config | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | PASS |
| bld_memory | 8.0 | 9.0 | 8.5 | 6.0 | 8.5 | 8.0 | FIX |
| bld_tools | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | PASS |

**Final avg (post-fix): 8.9**

---

## Defects Found vs D01-D15

| Defect | Expected | Found | Present? |
|--------|----------|-------|---------|
| D01 | system_prompt llm_function=BECOME | llm_function: BECOME | NOT PRESENT |
| D02 | memory kind=memory | kind: learning_record | PRESENT (bld_memory) |
| D03 | quality_gate tests artifact structure | N/A -- gate was stub | NOT APPLICABLE |
| D04 | Domain = neural net architecture | All content correct | NOT PRESENT |
| D05 | schema quality=null | quality: null | NOT PRESENT |
| D06 | quality_gate H02 matches schema ID pattern | N/A -- gate was stub | FIXED IN REBUILD |
| D07 | Tools reference real _tools/ scripts | All tools real | NOT PRESENT |
| D08 | output_template no bare placeholders | Placeholders have inline context | NOT PRESENT (output_template) |
| D08 | quality_gate not a stub | Complete TODO stub | PRESENT (quality_gate) |
| D09 | architecture ISO describes 13 builder ISOs | Correctly describes builder structure | NOT PRESENT |
| D10 | File references use actual ISO names | References "SCHEMA.md" | PRESENT (bld_instruction) |
| D11 | SOFT weights sum to 1.0 | N/A -- gate was stub | FIXED IN REBUILD |
| D12 | ASCII only in code blocks | No violations found | NOT PRESENT |
| D13 | density_score measured not hardcoded | N/A | NOT PRESENT |
| D14 | No empty config fields | All fields populated | NOT PRESENT |
| D15 | Collaboration tables use real CEX builders | Real builders listed | NOT PRESENT |

---

## Fixes Applied (3 total)

### Fix 1: REBUILD bld_quality_gate_model_architecture.md (D08 -- complete stub)

- **Was**: Single line "TODO: Generate content for model_architecture quality_gate"
- **Score before**: 0.0
- **Action**: Full rebuild following knowledge-card-builder gold standard
- **Now**: 10 HARD gates (H01-H10), 8 SOFT dimensions (S01-S08), score tiers, bypass conditions
- **Key gates added**:
  - H02: ID pattern `^p02_ma_[a-z][a-z0-9_]+$`
  - H07: architecture_type from allowed enum
  - H08: parameter_count must be explicit (not null/TBD/unknown)
  - H10: Layer Structure table >= 3 rows
- **Score after**: 9.1

### Fix 2: SURGICAL bld_memory_model_architecture.md (D02 -- wrong kind)

- **Was**: `kind: learning_record`
- **Now**: `kind: memory`
- **Root cause**: gemma4:26b contamination (same as qwen3:8b pattern from Wave 1)
- **Score before**: 8.0 (D4 penalized) | **Score after**: 9.0

### Fix 3: SURGICAL bld_instruction_model_architecture.md (D10 -- stale SCHEMA.md reference)

- **Was**: "Read SCHEMA.md -- source of truth for all required fields"
- **Now**: "Read bld_schema_model_architecture.md -- source of truth for all required fields"
- **Root cause**: Generator template uses generic SCHEMA.md reference
- **Score before**: 8.4 (D4 penalized) | **Score after**: 9.0

---

## gemma4 vs qwen3 Contamination Comparison

| Defect | qwen3:8b (Wave 1) | qwen3:14b (Wave 2) | gemma4:26b (Wave 3) |
|--------|------------------|-------------------|---------------------|
| D01 INJECT | ALL builders | BOTH builders | NOT PRESENT |
| D02 learning_record | PRESENT | NOT CHECKED | PRESENT (1 ISO) |
| D04 domain hallucination | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| D08 stub/placeholder | PRESENT | PRESENT | PRESENT (quality_gate) |
| D09 generic architecture | PRESENT | PRESENT | NOT PRESENT |
| D10 SCHEMA.md ref | NOT CHECKED | NOT CHECKED | PRESENT (instruction) |

**Conclusion**: gemma4:26b produces higher quality model_architecture than prior generators.
D01 (the most widespread defect) is absent. D09 (generic architecture) is absent. Only 3
defects vs 5-7 in earlier waves. The quality_gate stub is the critical failure but easily fixed.

---

## Validator Results

```
cex_wave_validator scanning archetypes/builders/model-architecture-builder/
  [PASS] bld_architecture_model_architecture.md
  [PASS] bld_collaboration_model_architecture.md
  [PASS] bld_config_model_architecture.md
  [PASS] bld_examples_model_architecture.md
  [PASS] bld_instruction_model_architecture.md
  [PASS] bld_knowledge_card_model_architecture.md
  [PASS] bld_manifest_model_architecture.md
  [PASS] bld_memory_model_architecture.md
  [PASS] bld_output_template_model_architecture.md
  [PASS] bld_quality_gate_model_architecture.md
  [PASS] bld_schema_model_architecture.md
  [PASS] bld_system_prompt_model_architecture.md
  [PASS] bld_tools_model_architecture.md

Summary: 13/13 PASS, 0/13 FAIL
```

---

## Notes for HYBRID_REVIEW4

1. D10 (SCHEMA.md reference in bld_instruction) may appear in other Wave 3 builders -- check
2. gemma4 gets D01 right -- test if this holds across all 6 ML kinds in Wave 2
3. quality_gate stub pattern (D08) persists -- generator still fails to produce gate content
