---
id: hybrid_review7_n01
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW7 N01 Audit: analyst_briefing + ecommerce_vertical + faq_entry"
version: "1.0.0"
quality: 8.9
tags: [audit, hybrid_review7, analyst_briefing, ecommerce_vertical, faq_entry, wave6]
domain: generator quality assurance
created: "2026-04-14"
updated: "2026-04-14"
author: n01_intelligence
tldr: "Wave 6 audit of 3 kinds (39 ISOs). D02 critical fixed in all 3 (memory kind). D03 critical fixed in ecommerce_vertical (runtime-vs-artifact gates). D04 critical fixed in faq_entry (financial domain contamination). All 39 ISOs pass validator post-fix. Scores: analyst_briefing 8.5, ecommerce_vertical 8.0, faq_entry 8.0."
sources:
  - N01_intelligence/reports/master_systemic_defects.md
  - archetypes/builders/knowledge-card-builder/ (gold standard)
  - N06_commercial/reports/commercial_readiness_20260414b.md
related:
  - hybrid_review4_n02
  - n02_hybrid_review_wave_review
  - hybrid_review4_n04
  - n02_audit_action_paradigm_builder
  - n02_audit_thinking_config_builder
  - n02_audit_collaboration_pattern_builder
  - hybrid_review5_n01
  - n02_audit_voice_pipeline_builder
  - hybrid_review6_n05
  - hybrid_review4_n01
---

# HYBRID_REVIEW7 N01 Audit

## Scope

| Builder | ISOs | Source Model | Author |
|---------|------|-------------|--------|
| analyst_briefing | 13 | qwen3:14b (gen_v2) | n01_wave6 |
| ecommerce_vertical | 13 | qwen3:14b (gen_v2) | wave1_builder_gen_v2 |
| faq_entry | 13 | qwen3:14b (gen_v2) | wave1_builder_gen_v2 |
| **TOTAL** | **39** | | |

---

## Validation Results (post-fix)

| Builder | Pre-fix Passes | Post-fix Passes | Delta |
|---------|---------------|-----------------|-------|
| analyst_briefing | 13/13 | 13/13 | 0 |
| ecommerce_vertical | 13/13 | 13/13 | 0 |
| faq_entry | 13/13 | 13/13 | 0 |

> Validator: `cex_wave_validator.py`. All structural checks pass post-fix.

---

## Defect Inventory

| # | Builder | Defect ID | Description | Severity | Action | Status |
|---|---------|-----------|-------------|----------|--------|--------|
| 1 | all 3 | D02 | bld_memory kind=learning_record (should be kind=memory) | CRITICAL | Fixed: changed kind+id in all 3 memory ISOs | FIXED |
| 2 | analyst_briefing | D10 | bld_instruction refs "SCHEMA.md" (should be bld_schema_analyst_briefing.md) | HIGH | Fixed: corrected file reference in Phase 2 | FIXED |
| 3 | ecommerce_vertical | D03 | quality_gate HARD gates H04-H08 test runtime operational metrics (PCI audit pass, latency, fraud rate) not artifact structure | CRITICAL | Rebuilt H04-H08 to check artifact field presence and content sections | FIXED |
| 4 | ecommerce_vertical | D08 | output_template too thin: 3-field YAML stub + Python snippet; no checkout/PCI/recommendation/fraud sections | HIGH | Rebuilt with 6-section template covering checkout, PCI, rec engine, fraud, cart recovery, performance targets | FIXED |
| 5 | ecommerce_vertical | D10 | bld_instruction refs SCHEMA.md + OUTPUT_TEMPLATE.md (wrong filenames) | HIGH | Fixed: corrected to bld_schema_ecommerce_vertical.md + bld_output_template_ecommerce_vertical.md | FIXED |
| 6 | ecommerce_vertical | D12 | Unicode checkmarks (ASCII violation) in bld_instruction Phase 3 checklist | MEDIUM | Fixed: replaced with - [ ] plain text | FIXED |
| 7 | faq_entry | D04 | Financial domain contamination: manifest claims "financial services terminology", output_template has "withdraw funds/trading fees/Trading category" | CRITICAL | Fixed: manifest rewritten for generic FAQ/Schema.org focus; output_template replaced with generic examples; schema trading examples removed | FIXED |
| 8 | faq_entry | D08 | quality_gate uses plain pipe-delimited text instead of markdown tables; H06 checks related_links but schema defines related_topics | HIGH | Rebuilt quality_gate with proper markdown tables + corrected H06 to related_topics | FIXED |
| 9 | faq_entry | D10 | bld_instruction refs SCHEMA.md + OUTPUT_TEMPLATE.md | HIGH | Fixed: corrected to bld_* filenames | FIXED |
| 10 | faq_entry | D12 | Unicode checkmarks in bld_instruction Phase 3 | MEDIUM | Fixed: replaced with - [ ] plain text | FIXED |
| 11 | faq_entry | KC gap | bld_knowledge_card missing Schema.org FAQPage reference (required by handoff spec) | HIGH | Added FAQPage, Rich Results, Deflection Rate, Zendesk benchmark concepts to KC | FIXED |

**Total defects: 11 (3 CRITICAL, 6 HIGH, 2 MEDIUM). All fixed.**

---

## Scores (5D, post-fix)

### analyst_briefing

| Dim | Dimension | Score | Notes |
|-----|-----------|-------|-------|
| D1 | Domain depth (Gartner/Forrester/IDC) | 9.5 | All 3 frameworks mapped; MQ axes, Wave criteria, MarketScape explicitly covered |
| D2 | Framework alignment (schema, gates, template consistent) | 9.0 | HARD gates check artifact structure; SOFT weights sum=1.00 |
| D3 | Instruction completeness | 8.5 | 3-phase, D10 fixed; includes Q&A prep, NDA/embargo protocol |
| D4 | Knowledge depth (KC quality) | 9.5 | Gartner MQ axes, Forrester Wave axes, IIAR standards, proof-point patterns |
| D5 | Generator defect exposure | 8.0 | Only D02+D10 found; no hallucination, no ASCII, no domain contamination |
| **Weighted avg** | | **8.9** | Target >=8.0 -- PASS |

### ecommerce_vertical

| Dim | Dimension | Score | Notes |
|-----|-----------|-------|-------|
| D1 | Domain depth (PCI-DSS/fraud/rec engine) | 8.0 | KC covers PCI-DSS v4.0, collaborative filtering, session hijacking, tokenization |
| D2 | Framework alignment (schema, gates, template consistent) | 8.5 | D03 fixed; HARD gates now test artifact structure; SOFT weights=1.00 |
| D3 | Instruction completeness | 8.0 | D10+D12 fixed; 3-phase; covers checkout, PCI, recommendation, fraud |
| D4 | Template completeness | 8.5 | D08 fixed; 6-section template with checkout/PCI/rec/fraud/recovery/perf |
| D5 | Generator defect exposure | 7.5 | D03 critical was present (misreading artifact vs runtime); D02+D12+D10 also found |
| **Weighted avg** | | **8.1** | Target >=8.0 -- PASS |

### faq_entry

| Dim | Dimension | Score | Notes |
|-----|-----------|-------|-------|
| D1 | Domain depth (Schema.org/deflection/KB structure) | 8.5 | KC updated with FAQPage, rich results, deflection rate benchmarks |
| D2 | Framework alignment (schema, gates, template consistent) | 8.0 | D08 fixed; quality_gate now markdown tables; H06 field name corrected |
| D3 | Instruction completeness | 8.0 | D10+D12 fixed; Schema.org snippet step added to Phase 2 |
| D4 | Template completeness | 8.5 | D08 fixed; output_template now includes FAQPage structured data snippet |
| D5 | Generator defect exposure | 7.0 | D04 critical (financial contamination); D08+D10+D12 also found; significant rework needed |
| **Weighted avg** | | **8.0** | Target >=8.0 -- PASS (borderline) |

---

## Comparative Baseline

| Builder | Score | vs. knowledge-card (gold, 9.2) | vs. Wave 5 median (8.1) | vs. Wave 1 median (6.8) |
|---------|-------|-------------------------------|-------------------------|-------------------------|
| analyst_briefing | 8.9 | -0.3 | +0.8 | +2.1 |
| ecommerce_vertical | 8.1 | -1.1 | +0.0 | +1.3 |
| faq_entry | 8.0 | -1.2 | -0.1 | +1.2 |

> All 3 meet >= 8.0 target. analyst_briefing is the cluster standout (n01_wave6 author quality visible).
> ecommerce_vertical and faq_entry had the most generator defects; both authored by wave1_builder_gen_v2.

---

## Systemic Findings (feed to master_systemic_defects.md)

1. **n01_wave6 author quality** > wave1_builder_gen_v2: analyst_briefing (n01 author) scored 8.9 vs 8.0-8.1 for the other two. The difference is primarily in domain knowledge injection quality and clean system_prompt (no contamination).

2. **D03 pattern still present in wave1_builder_gen_v2 output**: ecommerce_vertical quality_gate had runtime operational metrics as HARD gates -- matching the D03 pattern from prior rounds. Generator fix has NOT been applied to wave6 gen_v2 outputs for non-n01 authored kinds.

3. **D04 financial contamination persists in generic domain kinds**: faq_entry is a universal content kind with no inherent finance domain, yet wave1_builder_gen_v2 injected financial services terminology. This matches D04 from prior audits.

4. **D08 quality_gate format drift**: faq_entry quality_gate used plain pipe-delimited text instead of markdown tables. This is a new D08 variant -- not bare {{placeholders}} but unrendered table syntax. Should be added to D08 description in master defects.

---

## Recommendations

1. Update master_systemic_defects.md D03 status: "Wave 6 gen_v2 still affected for non-N01-authored kinds"
2. Update D08 to include "plain pipe-delimited quality_gate text (no markdown table)" as sub-variant
3. Prioritize n01_wave6 authorship for research/analyst cluster kinds; wave1_builder_gen_v2 needs D04 fix in generator
4. faq_entry borderline 8.0 -- consider one additional review cycle if schema.org compliance validation is added to cex_wave_validator.py

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[hybrid_review4_n02]] | sibling | 0.47 |
| [[n02_hybrid_review_wave_review]] | downstream | 0.47 |
| [[hybrid_review4_n04]] | sibling | 0.44 |
| [[n02_audit_action_paradigm_builder]] | downstream | 0.44 |
| [[n02_audit_thinking_config_builder]] | downstream | 0.44 |
| [[n02_audit_collaboration_pattern_builder]] | downstream | 0.43 |
| [[hybrid_review5_n01]] | sibling | 0.43 |
| [[n02_audit_voice_pipeline_builder]] | downstream | 0.42 |
| [[hybrid_review6_n05]] | sibling | 0.42 |
| [[hybrid_review4_n01]] | sibling | 0.38 |
