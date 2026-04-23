---
id: p11_qg_knowledge
kind: quality_gate
pillar: P11
title: "N04 Quality Gate — Knowledge Card Validation"
version: 4.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.1
tags: [quality_gate, n04, knowledge, density, freshness, taxonomy]
tldr: "10 checks for KCs: frontmatter complete, density >= 0.85, taxonomy valid, no duplicates, export-ready."
density_score: 0.93
related:
  - p11_qg_artifact
  - p11_qg_admin_orchestration
  - p04_tool_kc_validator
  - doctor
  - p04_skill_verify
  - bld_tools_kind
  - p07_rubric_knowledge
  - bld_tools_model_architecture
  - p03_sp_verification_agent
  - validate
---

# N04 Quality Gate

## Hard Gates

| ID | Check | Rationale |
|----|-------|-----------|
| H01 | All required frontmatter fields present | Incomplete KC breaks indexing |
| H02 | kind exists in kinds_meta.json | Invalid kind = unroutable |
| H03 | density_score >= 0.85 | Low density = wasted tokens |
| H04 | No duplicate KC (same id or >90% content overlap) | Duplicates pollute search |
| H05 | Compiles successfully (cex_compile.py) | Invalid YAML = broken pipeline |

## Soft Scoring

| # | Dimension | Weight | 1 (Poor) | 10 (Excellent) |
|---|-----------|--------|----------|----------------|
| 1 | Density (signal per token) | 1.0 | Filler prose | Every sentence carries info |
| 2 | Taxonomy accuracy | 0.8 | Wrong kind/pillar | Perfect classification |
| 3 | Freshness (<90 days) | 0.8 | >1 year old | <30 days |
| 4 | Export-readiness (JSONL/SQL/YAML) | 0.6 | Only .md | Triple-export ready |
| 5 | Cross-references (linked_artifacts) | 0.4 | No links | 3+ related KCs linked |

## Validation Workflow

**Step 1: Pre-validation**
```bash
# Check file exists and is readable
ls -la path/to/kc.md
# Verify in correct directory
pwd | grep -E "(P01_knowledge|library)"
```

**Step 2: Hard Gate Validation**
```bash
# H01-H05 automated check
python _tools/cex_doctor.py --check-kc path/to/kc.md
# Manual frontmatter review
head -20 path/to/kc.md | grep -E "^(id|kind|title|when_to_use):"
```

**Step 3: Compilation Test**
```bash
# H05 verification
python _tools/cex_compile.py path/to/kc.md
# Check output exists
ls compiled/ | grep $(basename path/to/kc.md .md).yaml
```

**Step 4: Duplicate Detection**
```bash
# H04 verification
python _tools/cex_query.py --find-duplicates --threshold 0.9
python _tools/cex_retriever.py --similar path/to/kc.md --top 3
```

**Step 5: Soft Scoring**
- Manually review density (tables vs prose ratio)
- Check taxonomy against `.cex/kinds_meta.json`
- Verify freshness in frontmatter `created` field
- Test export with `cex_compile.py --format all`

## Usage Guidelines

**When to apply:**
- Before committing any knowledge card to P01_knowledge/library/
- During batch KC validation with `/validate all`
- After major KC updates or taxonomy changes
- Pre-deployment to ensure indexing won't break

**Implementation:**
```bash
python _tools/cex_doctor.py --check-kc path/to/kc.md
python _tools/cex_compile.py path/to/kc.md
python _tools/cex_query.py --find-duplicates
```

**Common failures:**
- Missing `when_to_use` field (H01 violation)
- Generic titles like "Best Practices" (taxonomy fail)
- Verbose prose instead of tables (density <0.85)
- Outdated tech references (freshness fail)

**Pass/Fail examples:**
- ✅ PASS: `kc_react_hooks.md` — specific, dense, 3 code examples
- ❌ FAIL: `kc_general_tips.md` — vague kind, 0.72 density

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_artifact]] | sibling | 0.33 |
| [[p11_qg_admin_orchestration]] | sibling | 0.29 |
| [[p04_tool_kc_validator]] | upstream | 0.28 |
| [[doctor]] | upstream | 0.26 |
| [[p04_skill_verify]] | upstream | 0.25 |
| [[bld_tools_kind]] | upstream | 0.24 |
| [[p07_rubric_knowledge]] | upstream | 0.24 |
| [[bld_tools_model_architecture]] | upstream | 0.24 |
| [[p03_sp_verification_agent]] | upstream | 0.24 |
| [[validate]] | upstream | 0.23 |
