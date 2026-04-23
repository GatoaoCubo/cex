---
kind: collaboration
id: bld_collaboration_ai_rmf_profile
pillar: P12
llm_function: COLLABORATE
purpose: How ai_rmf_profile-builder works in crews with other builders
quality: 8.9
title: "Collaboration AI RMF Profile"
version: "1.0.0"
author: n01_wave7
tags: [ai_rmf_profile, builder, collaboration, NIST, AI-RMF, GOVERN, MAP, MEASURE, MANAGE]
tldr: "How ai_rmf_profile-builder works in crews with other builders"
domain: "ai_rmf_profile construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_safety_hazard_taxonomy
  - bld_collaboration_gpai_technical_doc
  - ai-rmf-profile-builder
  - bld_collaboration_llm_evaluation_scenario
  - bld_architecture_kind
  - bld_collaboration_builder
  - p03_sp_ai_rmf_profile_builder
  - bld_collaboration_code_of_conduct
  - bld_collaboration_safety_policy
  - kind-builder
---

## Crew Role
Produces structured NIST AI-RMF profile artifacts mapping organizational AI risks to AI-RMF functions and action-IDs per AI 600-1 GenAI categories.

## Receives From
| Builder | What | Format |
|---------|------|--------|
| compliance_framework-builder | Existing regulatory mapping context | Markdown |
| threat_model-builder | Risk inventory and severity assessments | Markdown |
| safety_policy-builder | Organizational safety policies for evidence pointers | Markdown |
| N01 Intelligence | NIST Playbook action-ID references and crosswalk data | Knowledge Card |

## Produces For
| Builder | What | Format |
|---------|------|--------|
| compliance_framework-builder | AI-RMF profile as input to broader compliance mapping | Markdown |
| safety_policy-builder | Action-ID gaps informing new policy requirements | Markdown |
| guardrail-builder | Risk category controls informing runtime guardrails | Markdown |
| N05 Operations | Profile evidence pointers triggering evaluation tasks | Markdown |

## Boundary
Does NOT handle EU AI Act documentation (use gpai_technical_doc-builder), runtime safety enforcement (use guardrail-builder), or safety hazard classification (use safety_hazard_taxonomy-builder). Legal sign-off and final audit evidence are managed by compliance/legal teams, not this builder.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_safety_hazard_taxonomy]] | sibling | 0.43 |
| [[bld_collaboration_gpai_technical_doc]] | sibling | 0.43 |
| [[ai-rmf-profile-builder]] | upstream | 0.37 |
| [[bld_collaboration_llm_evaluation_scenario]] | sibling | 0.33 |
| [[bld_architecture_kind]] | upstream | 0.32 |
| [[bld_collaboration_builder]] | sibling | 0.30 |
| [[p03_sp_ai_rmf_profile_builder]] | upstream | 0.30 |
| [[bld_collaboration_code_of_conduct]] | sibling | 0.30 |
| [[bld_collaboration_safety_policy]] | sibling | 0.29 |
| [[kind-builder]] | upstream | 0.29 |
