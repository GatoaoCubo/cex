---
kind: knowledge_card
id: bld_knowledge_card_gpai_technical_doc
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for gpai_technical_doc production
quality: 9.2
title: "Knowledge Card GPAI Technical Doc"
version: "1.0.0"
author: n01_wave7
tags: [gpai_technical_doc, builder, knowledge_card, GPAI, EU-AI-Act, Annex-IV, Article-53, training-data, compute-budget, downstream-limit, technical-documentation]
tldr: "Domain knowledge for gpai_technical_doc production"
domain: "gpai_technical_doc construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_gpai_technical_doc_builder
  - gpai-technical-doc-builder
  - bld_knowledge_card_conformity_assessment
  - bld_manifest_conformity_assessment
  - bld_instruction_conformity_assessment
  - bld_output_template_gpai_technical_doc
  - bld_schema_gpai_technical_doc
  - bld_output_template_conformity_assessment
  - bld_system_prompt_conformity_assessment
  - bld_collaboration_gpai_technical_doc
---

## Domain Overview
The EU Artificial Intelligence Act (Regulation (EU) 2024/1689) entered into force August 1, 2024. GPAI (General Purpose AI) model obligations under Article 53 became active August 2, 2025. GPAI providers must submit technical documentation to the EU AI Office covering training procedures, model capabilities, evaluation results, and intended use. Annex IV (formerly Annex XI in committee drafts) specifies the required fields.

GPAI models are distinguished from high-risk AI systems -- they are general-purpose foundation models (e.g., large language models, multimodal models). Models trained with >= 10^25 FLOP face additional obligations including systemic risk assessments. GPAI technical documentation is distinct from model cards (informal) and from conformity assessments for high-risk AI systems.

## Key Concepts
| Concept | Definition | Source |
|---------|-----------|--------|
| GPAI model | General purpose AI model with broad applicability across tasks and domains | EU AI Act Article 3(63) |
| Article 53 | Obligation for GPAI providers: technical doc, usage policies, copyright compliance, incident reporting | EU AI Act Art. 53 |
| Annex IV | List of required technical documentation fields for GPAI providers | EU AI Act Annex IV |
| training-data | Datasets used for pretraining and fine-tuning including sources, volumes, preprocessing methods | EU AI Act Annex IV(1)(b) |
| compute-budget | Total computational resources consumed during training, expressed in FLOP or GPU/TPU-hours | EU AI Act Annex IV(1)(c) |
| downstream-limit | Restrictions on use cases permitted for API integrators; defines prohibited downstream applications | EU AI Act Art. 53(1)(d) |
| EU AI Office | EU body responsible for GPAI oversight, receiving technical documentation submissions | EU AI Act Art. 64 |
| systemic risk | Additional obligations for GPAI models trained >= 10^25 FLOP (adversarial testing, incident reporting) | EU AI Act Art. 51 |
| energy consumption | MWh consumed during training + CO2-equivalent, required field in Annex IV | EU AI Act Annex IV(1)(c) |
| intended purpose | Primary use cases, target user groups, and deployment contexts declared by the provider | EU AI Act Annex IV(1)(a) |

## Annex IV Required Fields
| Field | Article Reference | Required Content |
|-------|-----------------|----------------|
| Model identity | Annex IV(1)(a) | Name, version, architecture type, release date, provider legal entity |
| Training procedures | Annex IV(1)(b) | Pretraining + fine-tuning objectives, data sources, volume (tokens/samples) |
| Compute budget | Annex IV(1)(c) | FLOP estimate or GPU-hours, hardware type, training location |
| Energy consumption | Annex IV(1)(c) | MWh total, CO2-eq, PUE, reporting methodology |
| Evaluation results | Annex IV(1)(d) | Benchmark names, scores, evaluation methodology, known performance gaps |
| Intended purpose | Annex IV(1)(e) | Primary use cases, prohibited uses, target user populations |
| Data governance | Annex IV(1)(f) | Filtering procedures, de-duplication, copyright compliance measures |
| Downstream limits | Article 53(1)(d) | API terms restricting prohibited use cases for integrators |
| EU representative | Art. 53 / GDPR analog | Required if provider is non-EU legal entity |

## Compliance Timeline
| Date | Obligation |
|------|-----------|
| Aug 2, 2024 | EU AI Act entered into force |
| Feb 2, 2025 | Prohibited AI practices banned |
| Aug 2, 2025 | GPAI obligations active (Article 53) |
| Aug 2, 2026 | High-risk AI system obligations active |
| Aug 2, 2027 | General-purpose AI systems with older regulation covered |

## Industry Standards
- EU AI Act Regulation (EU) 2024/1689 (Official Journal, July 2024)
- EU AI Office Guidelines for GPAI Technical Documentation (2025)
- GHG Protocol Corporate Standard (energy consumption methodology)
- ISO/IEC 42001:2023 (AIMS -- complementary framework)
- Model Cards for Model Reporting (Mitchell et al., 2019 -- informal reference)

## Common Patterns
1. GPAI technical doc is a LEGAL document, not a technical README -- tone and precision matter.
2. Downstream-limit clauses must be specific -- "no harmful use" is insufficient; enumerate prohibited cases.
3. Compute budget in FLOP is preferred; GPU-hours acceptable if hardware specs are included.
4. Energy data should reference GHG Protocol methodology for credibility.

## Pitfalls
- Conflating GPAI technical doc with model cards -- different audience, different legal standing.
- Omitting EU representative for non-EU providers -- enforcement risk.
- Vague downstream-limit clauses that don't enumerate specific prohibited uses.
- Missing evaluation methodology -- benchmark scores without methodology are unverifiable.
- Treating the document as static -- requires update on model version changes.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_gpai_technical_doc_builder]] | downstream | 0.67 |
| [[gpai-technical-doc-builder]] | downstream | 0.64 |
| [[bld_knowledge_card_conformity_assessment]] | sibling | 0.50 |
| [[bld_manifest_conformity_assessment]] | downstream | 0.46 |
| [[bld_instruction_conformity_assessment]] | downstream | 0.45 |
| [[bld_output_template_gpai_technical_doc]] | downstream | 0.45 |
| [[bld_schema_gpai_technical_doc]] | downstream | 0.43 |
| [[bld_output_template_conformity_assessment]] | downstream | 0.43 |
| [[bld_system_prompt_conformity_assessment]] | downstream | 0.43 |
| [[bld_collaboration_gpai_technical_doc]] | downstream | 0.43 |
