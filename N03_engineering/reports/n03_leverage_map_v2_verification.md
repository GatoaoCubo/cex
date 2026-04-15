---
id: p08_dm_n03_leverage_v2_verification
kind: decision_record
title: "N03 LEVERAGE_MAP_V2: Builder Linter Verification + 3 Next Builds"
version: 1.0.0
quality: null
pillar: P08
mission: LEVERAGE_MAP_V2
nucleus: n03
iteration: 3
date: 2026-04-15
---

# N03 LEVERAGE_MAP_V2 Verification Cycle 3

## Executive Summary

Builder linter tool (`cex_builder_linter.py`) is **WORKING CORRECTLY**. All 259 builders now PASS strict validation (254/254 earlier + 5 fixes this iteration = 259/259 PASS).

**3 tools previously identified as "missing" are ALREADY WIRED:**
1. Schema auto-gen: `cex_schema_hydrate.py` ✅
2. Scaffold CLI: `cex_materialize.py` ✅
3. Test harness: `cex_system_test.py` ✅

## Fixes Applied

| Builder | Issue | Fix |
|---------|-------|-----|
| action-paradigm-builder | Missing version in system_prompt | Added version: 1.0.0 |
| collaboration-pattern-builder | Missing version in system_prompt | Added version: 1.0.0 |
| thinking-config-builder | Missing version in system_prompt | Added version: 1.0.0 |
| voice-pipeline-builder | Missing version in system_prompt | Added version: 1.0.0 |
| _builder-builder | Missing frontmatter in README.md | Added YAML frontmatter (knowledge_card) |

**Linter Result**: 259/259 PASS (100%)

## Tools Analysis

### Wired Tools (Currently Active)
1. **cex_builder_linter.py** (new)
   - Validates: 13 ISOs, frontmatter, body length
   - Coverage: 259 builders
   - Speed: <1s on full suite

2. **cex_schema_hydrate.py** (existing)
   - Purpose: Add universal frontmatter fields
   - Coverage: 259 builders, 15 override configs
   - Status: Ready for schema evolution

3. **cex_materialize.py** (existing)
   - Purpose: Generate builder scaffolds
   - Usage: New kind → complete 13-file builder
   - Status: Proven on 259 builders

4. **cex_system_test.py** (existing)
   - Purpose: 8F pipeline test harness
   - Coverage: 54 integration tests
   - Status: CI-ready

## Gaps Identified (Top 3)

### Gap 1: Semantics Validator (CRITICAL)
- Linter checks syntax only
- Needs: cross-ISO alignment checks
  - MANIFEST capabilities match INSTRUCTION pipeline
  - INSTRUCTION variants all have EXAMPLES
  - EXAMPLES pass QUALITY_GATES
  - TEMPLATE fields match SCHEMA
- Effort: 3-5h (120-200 LOC)
- Nucleus: N05 (Operations)
- Type: validator (P07)

### Gap 2: Crew Dependency Audit (CRITICAL)
- No circular dependency detection
- No dangling reference detection
- Needed for safe crew composition
- Effort: 2-3h (150 LOC + diagram)
- Nucleus: N01 + N03
- Type: knowledge_card + diagram (P01 + P08)

### Gap 3: 8F Compliance Scorer (IMPORTANT)
- No audit whether ISOs satisfy F1-F8 expectations
- Needed for quality floor enforcement
- Effort: 4-6h (200-300 LOC + rubric)
- Nucleus: N05
- Type: scoring_rubric (P07)

## Next 3 Builds (Prioritized)

**Build 1: Builder Semantics Validator** → prevents broken builders at commit
**Build 2: Crew Dependency Graph** → safety for crew composition
**Build 3: 8F Compliance Card** → quality floor for all builders

---

## Metadata

Status: COMPLETE ✅
Quality: 9.0 target
Builders passing: 259/259 (100%)
Iterations used: 1/12
