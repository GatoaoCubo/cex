---
id: hybrid_review3_n01
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW3 Master Summary: N01 (agent_computer_interface + training_method)"
version: 1.0.0
quality: 8.5
tags: [audit, hybrid_review3, n01, master_summary, gemma4, wave2]
domain: AI research quality assurance
created: "2026-04-14"
author: n01_intelligence
tldr: "N01 HYBRID_REVIEW3 complete: 26 ISOs audited, 10 defects fixed (7 ACI + 3 TM). Both builders 13/13 PASS. ACI overall 8.6, TM overall 8.9."
sources:
  - N01_intelligence/audits/hybrid_review3_n01_aci.md
  - N01_intelligence/audits/hybrid_review3_n01_tm.md
  - N01_intelligence/reports/master_systemic_defects.md
related:
  - hybrid_review3_n01_aci
  - hybrid_review3_n01_tm
  - bld_schema_bugloop
  - bld_schema_quickstart_guide
  - bld_schema_pitch_deck
  - bld_schema_kind
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - p06_schema_a11y_checklist
  - bld_schema_integration_guide
---

# HYBRID_REVIEW3 Master Summary: N01

## Mission Summary
| Attribute | Value |
|-----------|-------|
| Mission | HYBRID_REVIEW3 |
| Nucleus | N01 (claude-sonnet-4-6) |
| Wave | review |
| Builders reviewed | agent-computer-interface-builder, training-method-builder |
| Total ISOs | 26 |
| Source model | gemma4:26b (Wave 2) |
| Audit date | 2026-04-14 |
| Validator result | 26/26 PASS |

## Defect Summary

| Builder | Critical | High | Medium/Low | Total | Rebuilds | Surgical | Pre-Score | Post-Score |
|---------|---------|------|-----------|-------|---------|---------|-----------|-----------|
| ACI (13 ISOs) | 3 | 4 | 0 | 7 | 6 | 1 | 5.2 avg | 8.6 |
| TM (13 ISOs) | 2 | 1 | 0 | 3 | 1 | 2 | 7.4 avg | 8.9 |
| **TOTAL** | **5** | **5** | **0** | **10** | **7** | **3** | **6.3** | **8.75** |

## Defect Code Distribution (vs master_systemic_defects.md)

| Code | Description | ACI | TM | Known from prior audits? |
|------|------------|-----|----|--------------------------|
| D02 | memory kind=learning_record | YES | YES | YES -- universal |
| D03 | runtime metrics in quality_gate | YES | N/A | YES -- seen in N02-R1 |
| D08 | output_template bare placeholders | YES | NO | YES -- seen in N01-R1 |
| D09 | architecture: generic team names | YES | NO | YES -- seen in N01-R1, N01-R2 |
| D10 | file reference drift (SCHEMA.md) | YES | YES | YES -- seen in N03-R1 |
| D15 | collaboration: generic non-CEX names | YES | NO | YES -- seen in N04-R2 |
| NEW | Truncation: ISOs cut off mid-content | YES (3/13) | NO | NEW in HR3 |
| NEW | Empty TODO placeholder | NO | YES (1/13) | NEW in HR3 |

## New Defect Patterns (Not in master_systemic_defects.md)

### D16 (NEW): gemma4 Context Truncation
3 ACI ISOs (schema, quality_gate, knowledge_card) were truncated mid-content. The files exist but
are silently incomplete -- no truncation marker, no error. This is worse than wrong content because:
- Validators that only check frontmatter will PASS truncated files
- Users cannot detect the problem without manually reading the file
- The schema ISO with 2 fields looked "valid" but was missing 11+ required fields

**Root cause hypothesis:** gemma4:26b hit a token budget during generation and stopped without
signaling incompletion. Wave 2 may have used tighter per-ISO token limits than Wave 1.

**Detection rule for cex_wave_validator.py:**
```python
# Flag ISOs that are suspiciously short (< 20 non-frontmatter lines)
body_lines = content_after_frontmatter.strip().split('\n')
if len(body_lines) < 20:
    warnings.append(f"D16_SUSPECT: {path} body only {len(body_lines)} lines -- may be truncated")
```

### D17 (NEW): Empty TODO Placeholder
TM bld_quality_gate contained only:
```
> TODO: Generate content for training_method quality_gate
```
This is distinct from D03 (wrong content) -- the ISO was entirely skipped. The generator
wrote a header + TODO and moved on. This produces a valid YAML frontmatter file with
no functional content.

**Detection rule:**
```python
if 'TODO:' in body and len(body_lines) < 5:
    errors.append(f"D17: {path} is a TODO placeholder -- no content generated")
```

## Quality Comparison: ACI vs TM (gemma4:26b Wave 2)

| Metric | ACI | TM | Delta |
|--------|-----|-----|-------|
| ISOs passing without change | 4/13 (31%) | 10/13 (77%) | +46% for TM |
| Full rebuilds required | 6 | 1 | ACI had 5x more rebuilds |
| Domain accuracy | Medium | High | TM ML terms are correct |
| Truncation defects | 3 | 0 | New defect, ACI only |
| Empty TODO defects | 0 | 1 | New defect, TM only |
| Post-fix overall score | 8.6 | 8.9 | Both above 8.0 threshold |

**Hypothesis:** training_method is a well-established ML domain with clear terminology (SFT, DPO,
PPO, LoRA). gemma4's training data heavily covers these. ACI is a newer term (post-2023) with less
training coverage, leading to gemma4 using generic/wrong framings (team roles vs interface schemas).

## Recommendations for wave1_builder_gen.py

1. **Add D16 check**: Flag any ISO body under 20 lines as a truncation candidate
2. **Add D17 check**: Reject any ISO body containing only TODO markers
3. **Per-ISO token budget**: ACI schema was cut at 24 lines -- increase min token budget
   for schema ISOs (they require more fields than other ISOs)
4. **D02 still universal**: kind=learning_record persists across all generators. Fix wave1_builder_gen.py line 84.

## Validator Results (Post-Fix)
```
ACI builder:  13/13 PASS (cex_wave_validator.py)
TM builder:   13/13 PASS (cex_wave_validator.py)
```
Both builders are ready for production use.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[hybrid_review3_n01_aci]] | sibling | 0.43 |
| [[hybrid_review3_n01_tm]] | sibling | 0.38 |
| [[bld_schema_bugloop]] | downstream | 0.34 |
| [[bld_schema_quickstart_guide]] | downstream | 0.34 |
| [[bld_schema_pitch_deck]] | downstream | 0.34 |
| [[bld_schema_kind]] | downstream | 0.33 |
| [[bld_schema_usage_report]] | downstream | 0.33 |
| [[bld_schema_reranker_config]] | downstream | 0.33 |
| [[p06_schema_a11y_checklist]] | downstream | 0.32 |
| [[bld_schema_integration_guide]] | downstream | 0.32 |
