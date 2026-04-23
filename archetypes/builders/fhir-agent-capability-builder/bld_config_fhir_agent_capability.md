---
kind: config
id: bld_config_fhir_agent_capability
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for fhir_agent_capability production
quality: 8.8
title: "Config FHIR Agent Capability"
version: "1.0.0"
author: n06_wave7
tags: [fhir_agent_capability, builder, config, fhir, hl7]
tldr: "Naming, paths, limits for fhir_agent_capability production"
domain: "fhir_agent_capability construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_model_registry
  - bld_config_transport_config
  - bld_config_usage_quota
  - bld_config_ab_test_config
  - bld_config_healthcare_vertical
  - bld_config_search_strategy
  - bld_config_sales_playbook
  - bld_config_visual_workflow
  - bld_config_data_residency
  - bld_config_prompt_technique
---

## Naming Convention
Pattern: `p08_fhir_{{capability_slug}}.md`
Examples: `p08_fhir_cds_sepsis_alert.md`, `p08_fhir_summarization_discharge.md`, `p08_fhir_coding_icd10_auto.md`

## Paths
Artifacts stored in: `P08_architecture/fhir_capabilities/{{capability_category}}/{{id}}.md`

## Limits
max_bytes: 5120
max_turns: 6
effort_level: 4

## Hooks
pre_build: validate FHIR version (R5 or R4B only)
post_build: register in fhir_capability_registry.yaml
on_error: null
on_quality_fail: escalate to healthcare compliance team

## Registry
Capabilities register in `.cex/registry/fhir_capabilities.yaml` on F8 completion.
Registry entry format:
```yaml
id: p08_fhir_{{capability_slug}}
capability_category: {{capability_category}}
fhir_version: {{fhir_version}}
phi_handling: {{phi_handling}}
smart_scopes: [{{scope_list}}]
cds_hooks: [{{hook_list}}]
created: {{date}}
compliance_reviewed: false
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_model_registry]] | sibling | 0.40 |
| [[bld_config_transport_config]] | sibling | 0.37 |
| [[bld_config_usage_quota]] | sibling | 0.35 |
| [[bld_config_ab_test_config]] | sibling | 0.34 |
| [[bld_config_healthcare_vertical]] | sibling | 0.34 |
| [[bld_config_search_strategy]] | sibling | 0.34 |
| [[bld_config_sales_playbook]] | sibling | 0.33 |
| [[bld_config_visual_workflow]] | sibling | 0.33 |
| [[bld_config_data_residency]] | sibling | 0.33 |
| [[bld_config_prompt_technique]] | sibling | 0.32 |
