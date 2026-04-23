---
kind: tools
id: bld_tools_edtech_vertical
pillar: P04
llm_function: CALL
purpose: Tools available for edtech_vertical production
quality: 8.8
title: "Tools Edtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [edtech_vertical, builder, tools]
tldr: "Tools available for edtech_vertical production"
domain: "edtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - edtech-vertical-builder
  - p10_mem_edtech_vertical_builder
  - p03_sp_edtech_vertical_builder
  - bld_examples_edtech_vertical
  - bld_instruction_edtech_vertical
  - bld_knowledge_card_edtech_vertical
  - p01_qg_edtech_vertical
  - bld_output_template_edtech_vertical
  - bld_architecture_edtech_vertical
  - hybrid_review7_n06
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile edtech_vertical YAML/MD artifacts to registry | After artifact generation |
| cex_score.py | Score artifact quality (5D rubric) against quality gate | Post-generation quality check |
| cex_retriever.py | Fetch similar edtech artifacts for reference | During F3 INJECT phase |
| cex_doctor.py | Diagnose schema compliance and frontmatter issues | Pre-validation checks |
| cex_wave_validator.py | Validate builder ISO set completeness and D01-D15 defects | Builder audit cycle |

## External References
- IMS Global LTI 1.3 specification (imsglobal.org/spec/lti/v1p3): LMS integration standard
- 1EdTech xAPI (Experience API) specification: learning activity tracking
- FERPA guidance (studentprivacy.ed.gov): educational record privacy
- COPPA FTC guidelines (ftc.gov/coppa): under-13 data collection rules
- Canvas LTI Developer Keys + Moodle External Tool documentation: LMS integration guides

## Domain Scope
These tools support edtech vertical artifact production, including LMS integration testing, accessibility compliance checks, and student data anonymization workflows specific to edtech use cases.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[edtech-vertical-builder]] | upstream | 0.45 |
| [[p10_mem_edtech_vertical_builder]] | downstream | 0.45 |
| [[p03_sp_edtech_vertical_builder]] | upstream | 0.43 |
| [[bld_examples_edtech_vertical]] | downstream | 0.42 |
| [[bld_instruction_edtech_vertical]] | upstream | 0.40 |
| [[bld_knowledge_card_edtech_vertical]] | upstream | 0.36 |
| [[p01_qg_edtech_vertical]] | downstream | 0.33 |
| [[bld_output_template_edtech_vertical]] | downstream | 0.32 |
| [[bld_architecture_edtech_vertical]] | downstream | 0.32 |
| [[hybrid_review7_n06]] | upstream | 0.32 |
