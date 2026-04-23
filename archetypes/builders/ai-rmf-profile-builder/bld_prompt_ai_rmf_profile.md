---
kind: instruction
id: bld_instruction_ai_rmf_profile
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for ai_rmf_profile
quality: 8.9
title: "Instruction AI RMF Profile"
version: "1.0.0"
author: n01_wave7
tags: [ai_rmf_profile, builder, instruction, NIST, AI-RMF, GOVERN, MAP, MEASURE, MANAGE]
tldr: "Step-by-step production process for ai_rmf_profile"
domain: "ai_rmf_profile construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_ai_rmf_profile_builder
  - p11_qg_ai_rmf_profile
  - ai-rmf-profile-builder
  - bld_knowledge_card_ai_rmf_profile
  - bld_examples_ai_rmf_profile
  - kc_ai_rmf_profile
  - bld_schema_ai_rmf_profile
  - p10_lr_ai_rmf_profile_builder
  - bld_output_template_ai_rmf_profile
  - bld_collaboration_ai_rmf_profile
---

## Phase 1: RESEARCH
1. Identify the AI system or domain being profiled (e.g., GenAI chatbot, automated decision system, recommendation engine).
2. Determine applicable AI 600-1 GenAI risk categories relevant to the system.
3. Map organizational context to NIST AI-RMF functions (GOVERN/MAP/MEASURE/MANAGE).
4. Gather existing governance policies, risk registers, and audit findings.
5. Identify action-IDs from the NIST AI-RMF Playbook applicable to identified risks.
6. Cross-reference with ISO/IEC 42001 controls and EU AI Act obligations for crosswalk table.

## Phase 2: COMPOSE
1. Reference SCHEMA for required fields (profile scope, function coverage, risk categories, action-IDs).
2. For each of 4 functions (GOVERN/MAP/MEASURE/MANAGE), list applicable action-IDs and implementation status.
3. For each of 12 GenAI risk categories, assign severity level and map to controlling action-IDs.
4. Populate crosswalk table linking AI-RMF actions to ISO 42001 controls (where applicable).
5. Document risk response approach per category (Accept / Mitigate / Transfer / Avoid).
6. Include profile scope declaration: system name, deployment context, profiler identity, review date.
7. Flag gaps where action-IDs have no implementation assigned.
8. Add evidence pointers (policy docs, test results, audit logs) per action-ID where available.
9. Proofread for action-ID format consistency (e.g., GV-1.1 not "Govern 1.1").

## Phase 3: VALIDATE
- [ ] All 4 functions (GOVERN/MAP/MEASURE/MANAGE) addressed with at least 1 action-ID each.
- [ ] All 12 GenAI risk-categories from AI 600-1 listed with severity assignments.
- [ ] Action-IDs follow NIST format (GV/MP/MS/MG prefix + numeric suffix).
- [ ] Profile scope field present (system name, context, review date).
- [ ] Crosswalk table has at least ISO 42001 column populated.
- [ ] No action-ID referenced that does not exist in NIST AI-RMF Playbook v1.0.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_ai_rmf_profile_builder]] | related | 0.62 |
| [[p11_qg_ai_rmf_profile]] | downstream | 0.52 |
| [[ai-rmf-profile-builder]] | downstream | 0.50 |
| [[bld_knowledge_card_ai_rmf_profile]] | upstream | 0.44 |
| [[bld_examples_ai_rmf_profile]] | downstream | 0.42 |
| [[kc_ai_rmf_profile]] | upstream | 0.42 |
| [[bld_schema_ai_rmf_profile]] | downstream | 0.38 |
| [[p10_lr_ai_rmf_profile_builder]] | downstream | 0.34 |
| [[bld_output_template_ai_rmf_profile]] | downstream | 0.33 |
| [[bld_collaboration_ai_rmf_profile]] | downstream | 0.31 |
