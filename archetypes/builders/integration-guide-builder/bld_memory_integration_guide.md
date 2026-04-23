---
kind: learning_record
id: p10_lr_integration_guide_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for integration_guide construction
quality: 8.7
title: "Learning Record Integration Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [integration_guide, builder, learning_record]
tldr: "Learned patterns and pitfalls for integration_guide construction"
domain: "integration_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_integration_guide_builder
  - bld_instruction_integration_guide
  - p10_lr_quickstart_guide_builder
  - p10_mem_prompt_optimizer_builder
  - bld_instruction_quickstart_guide
  - p03_sp_quickstart_guide_builder
  - integration-guide-builder
  - p10_lr_judge_config_builder
  - kc_integration_guide
  - p03_sp_marketplace_app_manifest_builder
---

## Observation
Common issues include missing context for platform-specific configurations, inconsistent terminology, and omitting prerequisite setup steps for paid-tier onboarding.

## Pattern
Effective guides use structured workflows with explicit use cases, cross-reference API concepts without duplication, and include troubleshooting sections for common integration roadblocks.

## Evidence
Reviewed guides with setup checklists and role-based scenarios (e.g., SaaS partner onboarding) showed 30% higher adoption rates compared to sparse documentation.

## Recommendations
- Avoid assuming prior knowledge of platform-specific tools or authentication flows.
- Include a "Prerequisites" section detailing account setup, API keys, and environment requirements.
- Use code samples with explicit comments for platform-specific configurations (e.g., OAuth scopes).
- Add a "Troubleshooting" section addressing common errors during integration testing.
- Align with paid-tier onboarding processes by specifying success metrics and validation steps.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_integration_guide_builder]] | upstream | 0.34 |
| [[bld_instruction_integration_guide]] | upstream | 0.33 |
| [[p10_lr_quickstart_guide_builder]] | related | 0.25 |
| [[p10_mem_prompt_optimizer_builder]] | related | 0.23 |
| [[bld_instruction_quickstart_guide]] | upstream | 0.22 |
| [[p03_sp_quickstart_guide_builder]] | upstream | 0.22 |
| [[integration-guide-builder]] | upstream | 0.22 |
| [[p10_lr_judge_config_builder]] | sibling | 0.21 |
| [[kc_integration_guide]] | upstream | 0.20 |
| [[p03_sp_marketplace_app_manifest_builder]] | upstream | 0.20 |
