---
quality: 8.3
quality: 7.9
id: bld_rules_deployment_manifest
kind: knowledge_card
pillar: P08
title: "Rules: deployment_manifest Builder Constraints"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: deployment_manifest
tags: [rules, deployment_manifest, P09]
llm_function: COLLABORATE
tldr: "Hard constraints and edge case handling for deployment_manifest builder."
density_score: null
related:
  - bld_norms
  - p03_sp__builder_builder
  - p03_sp_system-prompt-builder
  - p03_sp_n03_creation_nucleus
  - p03_sp_quickstart_guide_builder
  - spec_n07_operational_intelligence
  - p03_sp_few_shot_example_builder
  - p03_sp_golden_test_builder
  - p03_sp_env_config_builder
  - p03_sp_path_config_builder
---

# Rules: deployment_manifest Builder

## Hard Constraints
1. NEVER inline secret values -- vault path or k8s secret ref only
2. NEVER use "latest" or mutable tags -- always pin to semver or SHA
3. ALWAYS include rollback_to -- no manifest ships without a recovery path
4. artifacts_count MUST equal len(artifacts list) -- gate H06
5. id MUST match filename stem -- naming compliance
6. quality MUST be null -- never self-score

## Edge Cases

| Situation | Resolution |
|-----------|-----------|
| User has only 1 artifact | Valid; artifacts_count: 1 |
| User doesn't know rollback revision | Block: ask for prior stable version before proceeding |
| User wants to deploy to multiple regions | Create 1 manifest per region OR add regions list field |
| User wants canary split in this manifest | Redirect to canary_config; deployment_manifest handles artifact spec only |
| User wants test environment | Redirect to sandbox_spec |
| Artifact has no registry (local build) | Use filesystem path as source; note "local" in source field |
| No health check endpoint exists | Use startup probe instead; document as readiness_probe |

## Naming Rules
- File: `p09_dm_{name_slug}.md` where name_slug is kebab-to-snake: `cex-api-v2` -> `cex_api_v2`
- ID: `p09_dm_{name_slug}`
- Tags: MUST include "deployment_manifest" + domain + target_env

## Boundary Enforcement
- deployment_manifest DEFINES the spec; the deployment runner EXECUTES it
- If user asks to "run the deployment": out of scope -- this builder produces the spec only
- If user asks to "monitor the deployment": redirect to workflow or trace_config

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_norms]] | related | 0.19 |
| [[p03_sp__builder_builder]] | upstream | 0.19 |
| [[p03_sp_system-prompt-builder]] | upstream | 0.18 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.17 |
| [[p03_sp_quickstart_guide_builder]] | upstream | 0.17 |
| [[spec_n07_operational_intelligence]] | upstream | 0.17 |
| [[p03_sp_few_shot_example_builder]] | upstream | 0.17 |
| [[p03_sp_golden_test_builder]] | upstream | 0.17 |
| [[p03_sp_env_config_builder]] | upstream | 0.17 |
| [[p03_sp_path_config_builder]] | upstream | 0.16 |
