---
kind: learning_record
id: p10_lr_threat_model_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for threat_model construction
quality: 8.8
title: "Learning Record Threat Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [threat_model, builder, learning_record]
tldr: "Learned patterns and pitfalls for threat_model construction"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - p03_sp_threat_model_builder
  - bld_collaboration_threat_model
  - p11_qg_threat_model
  - threat-model-builder
  - bld_knowledge_card_threat_model
  - bld_architecture_threat_model
  - bld_instruction_threat_model
  - bld_tools_threat_model
  - bld_examples_threat_model
  - bld_schema_threat_model
---

## Observation

This ISO records a threat model: the assets worth protecting and the attacker profiles that target them.
Common issues include incomplete threat scenarios, siloed input from narrow stakeholders, and over-reliance on generic templates that ignore AI-specific attack vectors (e.g., data poisoning, model inversion).

## Pattern
Effective models use structured frameworks (e.g., STRIDE, MITRE ATT&CK) tailored to AI systems, integrate cross-functional input (security, engineering, domain experts), and emphasize iterative refinement through scenario-based validation.

## Evidence
Reviewed artifacts from healthcare and finance domains showed improved coverage when threat models explicitly addressed adversarial training data and inference-time evasion techniques.

## Recommendations
- Prioritize AI-specific threat categories (e.g., data integrity, model robustness) over generic templates.
- Involve diverse stakeholders early to identify non-technical risks (e.g., reputational, legal).
- Use iterative workshops to refine scenarios and validate assumptions with red-team exercises.
- Link threats directly to mitigation strategies (e.g., differential privacy, input validation).
- Document assumptions and limitations to enable model evolution as AI systems mature.
| Common: missing STRIDE coverage | Address all 6 STRIDE categories or justify omissions |
| Common: no mitigation for each threat | Every threat entry must have a mitigation strategy |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_threat_model_builder]] | upstream | 0.43 |
| [[bld_collaboration_threat_model]] | downstream | 0.41 |
| [[p11_qg_threat_model]] | downstream | 0.41 |
| [[threat-model-builder]] | downstream | 0.40 |
| [[bld_knowledge_card_threat_model]] | upstream | 0.40 |
| [[bld_architecture_threat_model]] | upstream | 0.38 |
| [[bld_instruction_threat_model]] | upstream | 0.37 |
| [[bld_tools_threat_model]] | upstream | 0.37 |
| [[bld_examples_threat_model]] | upstream | 0.36 |
| [[bld_schema_threat_model]] | upstream | 0.35 |
