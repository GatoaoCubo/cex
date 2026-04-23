---
kind: knowledge_card
id: bld_knowledge_card_safety_hazard_taxonomy
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for safety_hazard_taxonomy production
quality: 9.2
title: "Knowledge Card Safety Hazard Taxonomy"
version: "1.0.0"
author: n01_wave7
tags: [safety_hazard_taxonomy, builder, knowledge_card, MLCommons, AILuminate, Llama-Guard, hazard-category, CBRN, severity-level, response-template, taxonomy]
tldr: "Domain knowledge for safety_hazard_taxonomy production"
domain: "safety_hazard_taxonomy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_safety_hazard_taxonomy
  - p03_sp_safety_hazard_taxonomy_builder
  - bld_output_template_safety_hazard_taxonomy
  - safety-hazard-taxonomy-builder
  - bld_schema_safety_hazard_taxonomy
  - p11_qg_safety_hazard_taxonomy
  - bld_collaboration_safety_hazard_taxonomy
  - bld_examples_safety_hazard_taxonomy
  - bld_tools_safety_hazard_taxonomy
  - p10_lr_safety_hazard_taxonomy_builder
---

## Domain Overview
MLCommons AILuminate v1.0 (December 2024) is the industry-standard AI safety benchmarking system comprising 24,000+ expert-written test prompts across 12 hazard categories. Powered by Llama Guard 4 (12B multimodal, Meta 2025), which provides automatic hazard classification aligned to the same taxonomy. Over 35 AI companies participated in AILuminate v1.0 evaluation at launch. The taxonomy has become the de-facto reference for AI safety classification, referenced by NIST AI 600-1 and integrated into enterprise safety systems.

A safety_hazard_taxonomy artifact formally codifies this classification structure for use in content moderation pipelines, red team operations, and safety policy design. It is a DEFINITION document -- not a filtering configuration or enforcement rule.

## Key Concepts
| Concept | Definition | Source |
|---------|-----------|--------|
| hazard-category | One of 12 top-level safety hazard types from MLCommons AILuminate taxonomy | MLCommons AILuminate v1.0 |
| severity-level | 4-level risk classification per category variant: low/medium/high/critical | AILuminate evaluation rubric |
| response-template | Structured response pattern for each severity level: refusal / safe-completion / warning / escalation | AI safety best practice |
| Llama Guard 4 | Meta's 12B multimodal safety classifier; output labels map 1:1 to AILuminate categories | Meta, 2025 |
| CBRN | Chemical, Biological, Radiological, Nuclear weapons -- the highest-priority hazard category | AILuminate S9 |
| AILuminate v1.0 | MLCommons safety benchmark: 24K+ prompts, 12 categories, 35+ model evaluations | MLCommons Dec 2024 |
| boundary condition | Explicit rule distinguishing one hazard category from an adjacent/overlapping category | Taxonomy design practice |
| taxonomy-scope | Declaration of which categories are covered: full-12 or subset with justification | This artifact's required field |

## The 12 AILuminate Hazard Categories
| # | Category | Llama Guard Label | Priority |
|---|---------|-----------------|---------|
| 1 | Violent Crimes | S1 | Critical |
| 2 | Non-Violent Crimes | S2 | High |
| 3 | Sex Crimes | S3 | Critical |
| 4 | Child Sexual Abuse Material (CSAM) | S4 | Critical |
| 5 | Specialized Advice (medical/legal/financial) | S5 | High |
| 6 | Privacy (PII / personal data) | S6 | High |
| 7 | Intellectual Property | S7 | Moderate |
| 8 | Indiscriminate Weapons (CBRN) | S8 | Critical |
| 9 | Hate Speech / Discrimination | S9 | High |
| 10 | Self-Harm / Suicide | S10 | High |
| 11 | Sexual Content (adult, non-consensual) | S11 | High |
| 12 | Elections / Civic Integrity | S12 | High |

## Severity Level Definitions
| Level | Definition | Default Response |
|-------|-----------|-----------------|
| low | Informational query with educational framing; no direct harm pathway | Safe completion with disclaimer |
| medium | Borderline request; harm pathway exists but indirect or requires additional steps | Warning + partial refusal |
| high | Explicit harm request; direct harmful content would result from compliance | Refusal + explanation |
| critical | Imminent or mass-casualty harm pathway (CBRN, CSAM, targeted violence) | Hard refusal + escalation |

## Response Template Patterns
| Template Type | When to Use | Structure |
|--------------|------------|---------|
| SAFE_COMPLETE | low severity | Provide answer with appropriate disclaimer |
| WARN_PARTIAL | medium severity | Partial answer + explicit warning about harm pathway |
| REFUSE_EXPLAIN | high severity | Refusal + educational explanation of why |
| HARD_REFUSE | critical severity | Terse refusal + escalation flag (no elaboration) |

## Industry Standards
- MLCommons AILuminate v1.0 (mlcommons.org/benchmarks/ailuminate, December 2024)
- Meta Llama Guard 4 (ai.meta.com/research/llama-guard, 2025)
- NIST AI 600-1 GenAI Profile (CBRN category cross-reference)
- EU AI Act Article 5 (prohibited AI practices -- CSAM, subliminal manipulation)
- Anthropic Responsible Scaling Policy (ASL-3 CBRN threshold reference)

## Common Patterns
1. Taxonomy is the REFERENCE LAYER -- build content_filter and guardrail artifacts ON TOP of it.
2. CBRN always requires hard-refuse at all severity levels -- no exceptions in AILuminate.
3. Boundary conditions between Sex Crimes and Sexual Content are critical to avoid over-refusal.
4. False-positive risk notes prevent over-aggressive filtering of legitimate queries.

## Pitfalls
- Treating taxonomy as a pipeline config -- it defines categories, not filtering logic.
- Missing boundary conditions between adjacent categories (e.g., Hate Speech vs. Elections).
- Incomplete CBRN sub-categorization -- Chemical/Biological/Radiological/Nuclear must be individually addressed.
- Omitting false-positive risk notes -- leads to over-refusal of benign educational queries.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_safety_hazard_taxonomy]] | downstream | 0.67 |
| [[p03_sp_safety_hazard_taxonomy_builder]] | downstream | 0.63 |
| [[bld_output_template_safety_hazard_taxonomy]] | downstream | 0.60 |
| [[safety-hazard-taxonomy-builder]] | downstream | 0.59 |
| [[bld_schema_safety_hazard_taxonomy]] | downstream | 0.47 |
| [[p11_qg_safety_hazard_taxonomy]] | downstream | 0.44 |
| [[bld_collaboration_safety_hazard_taxonomy]] | downstream | 0.43 |
| [[bld_examples_safety_hazard_taxonomy]] | downstream | 0.42 |
| [[bld_tools_safety_hazard_taxonomy]] | downstream | 0.40 |
| [[p10_lr_safety_hazard_taxonomy_builder]] | downstream | 0.37 |
