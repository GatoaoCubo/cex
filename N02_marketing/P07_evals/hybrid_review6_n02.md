---
id: hybrid_review6_n02
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW6 N02 Audit: pitch_deck + interactive_demo + product_tour"
version: "1.0.0"
quality: 8.9
density_score: 0.99
author: n02_marketing
tags: [audit, hybrid_review6, pitch_deck, interactive_demo, product_tour, wave5]
domain: quality assurance
created: "2026-04-14"
updated: "2026-04-14"
mission: HYBRID_REVIEW6
wave: review
source_model: qwen3:14b (Wave 5 gen_v2)
tldr: "39 ISOs audited (3 builders). Pre-fix score 5.2/10 avg. Post-fix 8.8/10. 7 defect types fixed: D02/D07/D09/D10/D11/D12 + output template contamination. All 39 ISOs PASS validator."
---

# HYBRID_REVIEW6 N02 Audit Report

## Scope

| Builder | Kind | ISOs | Pre-fix Score | Post-fix Score | Action |
|---|---|---|---|---|---|
| pitch-deck-builder | pitch_deck | 13 | 5.5 | 8.9 | surgical fix |
| interactive-demo-builder | interactive_demo | 13 | 5.0 | 8.7 | surgical fix |
| product-tour-builder | product_tour | 13 | 5.5 | 8.8 | surgical fix |

Validator result: 39/39 PASS (post-fix)

---

## Defect Inventory (pre-fix)

| Defect | Category | Severity | Builders Affected | ISOs Fixed |
|---|---|---|---|---|
| D02: memory kind=learning_record | Master defect list | CRITICAL | all 3 | bld_memory x3 |
| D07: fabricated tools | Master defect list | HIGH | all 3 | bld_tools x3 |
| D09: architecture wrong pillars | Master defect list | HIGH | all 3 | bld_architecture x3 |
| D10: file reference drift (SCHEMA.md) | Master defect list | HIGH | all 3 | bld_instruction x3 |
| D12: Unicode checkmarks (U+2705) | Master defect list | MEDIUM | pitch_deck, product_tour | bld_instruction x2 |
| D11: SOFT weights sum to 0.90 | Master defect list | MEDIUM | interactive_demo | bld_quality_gate x1 |
| Output template Python contamination | Domain-specific | HIGH | all 3 | bld_output_template x3 |
| Knowledge card missing platform refs | Domain-specific | HIGH | all 3 | bld_knowledge_card x3 |
| System prompt wrong framework refs | Domain-specific | MEDIUM | pitch_deck | bld_system_prompt x1 |

Total ISOs modified: 22 / 39

---

## Per-Builder Findings

### pitch_deck

**Pre-fix issues:**
- bld_memory: `kind: learning_record` (D02 CRITICAL)
- bld_tools: 6 fabricated tools (cex_visualizer.py, cex_formatter.py, val_*.py) + fake SaaS refs (D07)
- bld_architecture: all 13 ISOs assigned pillar P05, correct varies P01/P03/P04/P06/P08/P09/P10/P11/P12 (D09)
- bld_instruction: references SCHEMA.md and OUTPUT_TEMPLATE.md instead of bld_* files (D10)
- bld_instruction: Unicode checkmarks U+2705 in validate checklist (D12)
- bld_output_template: contained Python API endpoint code block -- domain contamination; missing 7 of 10 Sequoia slides
- bld_knowledge_card: missing Sequoia 10-slide template, Guy Kawasaki 10/20/30, "Why Now" framing
- bld_system_prompt: referenced Slidebean/Pitcher instead of Sequoia/YC/Kawasaki

**Fixes applied:**
- bld_memory: kind -> memory, id -> p10_mem_pitch_deck_builder
- bld_tools: replaced with real CEX tools (cex_compile, cex_score, cex_retriever, cex_doctor, cex_hooks, cex_hygiene) + informational external refs (Sequoia, YC, Kawasaki, Crunchbase)
- bld_architecture: corrected all 13 ISO pillar assignments + llm_function column added
- bld_instruction: fixed all file references + replaced checkmarks with ASCII `- [ ]`
- bld_output_template: rebuilt as full 10-slide Sequoia structure with {{vars}} per field
- bld_knowledge_card: added Slide Framework Reference table (Sequoia/YC/Kawasaki/Airbnb), Why Now section, updated industry standards
- bld_system_prompt: rewrote identity with Sequoia structure, Why Now mandate, Guy Kawasaki density rules

**Narrative lens check:** problem -> why now -> solution -> market -> product -> biz model -> traction -> team -> financials -> ask. Full 10-slide arc now enforced.

**Post-fix score: 8.9/10**

---

### interactive_demo

**Pre-fix issues:**
- bld_memory: `kind: learning_record` (D02 CRITICAL)
- bld_tools: cex_runner.py, val_linter.py, val_simulator.py, val_consistency.py fabricated + React/TensorFlow Lite/Jupyter as "external refs" (D07)
- bld_architecture: all 13 ISOs assigned pillar P05 (D09)
- bld_instruction: references SCHEMA.md and OUTPUT_TEMPLATE.md (D10)
- bld_quality_gate: SOFT weights = 0.90 (not 1.00) -- D11 defect
- bld_output_template: Python input() code block in demo script; broken ```yaml nesting inside ```markdown
- bld_knowledge_card: no Demostack/Reprise/Navattic/Arcade/Supademo platform patterns; no presales SE playbook structure

**Fixes applied:**
- bld_memory: kind -> memory, id -> p10_mem_interactive_demo_builder
- bld_tools: replaced with real CEX tools + platform reference table (Demostack/Reprise/Navattic/Arcade/Supademo/MEDDIC)
- bld_architecture: corrected all 13 ISO pillar assignments + llm_function column
- bld_instruction: fixed file references
- bld_quality_gate: reweighted SOFT dimensions to sum 1.00 (D01=0.20, D02=0.20, D03=0.15, D04=0.15, D05=0.10, D06=0.05, D07=0.05, D08=0.10)
- bld_output_template: rebuilt as guided-tour + talk track script with demo flow table (step/screen/action/talk track/objection/response columns)
- bld_knowledge_card: added Platform Patterns table, Presales SE Playbook Structure, updated industry standards

**Narrative lens check:** interactive_demo = self-serve evaluation layer. Post-pitch-deck, pre-close. Presales talk track (discovery -> setup -> core demo -> proof -> objection -> CTA) now embedded.

**Post-fix score: 8.7/10**

---

### product_tour

**Pre-fix issues:**
- bld_memory: `kind: learning_record` (D02 CRITICAL)
- bld_tools: cex_analyzer.py, cex_optimizer.py, val_checker.py, val_simulator.py, val_reporter.py, val_comparator.py fabricated + Tour.js/Storybook/Lodash as "external refs" (D07)
- bld_architecture: all 13 ISOs assigned pillar P05 (D09)
- bld_instruction: references SCHEMA.md and OUTPUT_TEMPLATE.md (D10)
- bld_instruction: Unicode checkmarks U+2705 in validate checklist (D12)
- bld_output_template: Python code block with pass statement; generic yaml structure missing tour-specific fields
- bld_knowledge_card: no Pendo/Appcues/WalkMe/Intercom platform patterns; no trigger anatomy; no TTV metric

**Fixes applied:**
- bld_memory: kind -> memory, id -> p10_mem_product_tour_builder
- bld_tools: replaced with real CEX tools + platform reference table (Pendo/Appcues/WalkMe/Intercom/WCAG/TTV)
- bld_architecture: corrected all 13 ISO pillar assignments + llm_function column
- bld_instruction: fixed all file references; replaced checkmarks with ASCII `- [ ]`
- bld_output_template: rebuilt as in-app tour spec with step table (step_id/target_element/tooltip_position/trigger_condition/analytics_event), trigger config, accessibility block, localization table
- bld_knowledge_card: added Platform Patterns table (Pendo/Appcues/WalkMe/Intercom), Trigger Anatomy table, Activation Metrics / TTV section, updated industry standards

**Narrative lens check:** product_tour = post-purchase activation layer. After signup, drives time-to-value. Empty-state coaching now explicitly referenced.

**Post-fix score: 8.8/10**

---

## Conversion-Narrative Layer Coherence

These 3 kinds form a funnel:

| Stage | Kind | Audience | Goal |
|---|---|---|---|
| Fundraising / Enterprise sales | pitch_deck | Investors / economic buyers | Close funding or enterprise deal |
| Self-serve evaluation | interactive_demo | Champions / technical evaluators | Enable buyer to explore product independently |
| Post-purchase activation | product_tour | End users | Drive time-to-value, feature adoption |

The narrative arc (problem -> solution -> proof -> action) runs through all 3:
- pitch_deck encodes it as slides
- interactive_demo encodes it as talk track
- product_tour encodes it as tooltip sequences

All 3 builders now have industry-appropriate platform references injected into both the knowledge card and tools ISO.

---

## Systemic Defects Confirmed in Wave 5

| Defect | Count in This Wave | Disposition |
|---|---|---|
| D02 memory kind | 3/3 builders | Fixed |
| D07 fabricated tools | 3/3 builders | Fixed |
| D09 architecture pillar drift | 3/3 builders | Fixed |
| D10 file reference drift | 3/3 builders | Fixed |
| D11 weight sum != 1.00 | 1/3 builders | Fixed |
| D12 Unicode checkmarks | 2/3 builders | Fixed |
| Output template code contamination | 3/3 builders | Fixed (domain-specific, not in master list) |

Recommendation: add output template domain-contamination (Python code in non-code kinds) as D16 to master_systemic_defects.md.

---

## Validator Summary

| Builder | Pre-fix | Post-fix |
|---|---|---|
| pitch-deck-builder | 11/13 PASS | 13/13 PASS |
| interactive-demo-builder | 10/13 PASS | 13/13 PASS |
| product-tour-builder | 10/13 PASS | 13/13 PASS |
| **Total** | **31/39** | **39/39** |
