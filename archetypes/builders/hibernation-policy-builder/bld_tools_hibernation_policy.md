---
kind: toolkit
id: bld_tools_hibernation_policy
pillar: P04
llm_function: CALL
purpose: P04 tools used by hibernation_policy builder
quality: 8.0
title: "Tools: hibernation_policy Builder"
version: "1.0.0"
author: n03_engineering
tags: [hibernation_policy, builder, tools]
tldr: "P04 tools used by hibernation_policy builder"
domain: "hibernation_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_tools_white_label_config
  - n06_api_access_pricing
  - bld_tools_pricing_page
  - bld_tools_api_reference
  - bld_tools_kind
  - bld_tools_skill
  - bld_tools_vad_config
  - bld_tools_onboarding_flow
  - bld_tools_legal_vertical
  - bld_tools_multimodal_prompt
---

## Tools Used in F5 CALL

| Tool | Purpose | When |
|------|---------|------|
| `cex_compile.py` | Compile .md -> .yaml | F8 COLLABORATE -- after save |
| `cex_doctor.py` | Health check artifact structure | F7 GOVERN -- validate before commit |
| `python -m json.tool` | Validate kinds_meta.json | F8 -- after patching kinds_meta |
| `cex_retriever.py` | Find similar existing hibernation_policy artifacts | F3 INJECT -- avoid duplication |
| `cex_8f_runner.py` | Execute full 8F pipeline for this kind | F1 entry point |

## External APIs (optional -- for validation only)

| API | Purpose | Required |
|-----|---------|----------|
| Daytona API | Validate workspace pause/resume endpoint exists | No -- design-time only |
| Modal API | Validate container scaling-to-zero config | No -- design-time only |

## No External Calls During Build
hibernation_policy is a pure config artifact. The builder does NOT make live API calls to backends during construction. Configuration is validated syntactically (schema + gates), not by hitting live endpoints.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_white_label_config]] | related | 0.26 |
| [[n06_api_access_pricing]] | downstream | 0.23 |
| [[bld_tools_pricing_page]] | related | 0.22 |
| [[bld_tools_api_reference]] | related | 0.22 |
| [[bld_tools_kind]] | related | 0.21 |
| [[bld_tools_skill]] | related | 0.21 |
| [[bld_tools_vad_config]] | related | 0.21 |
| [[bld_tools_onboarding_flow]] | related | 0.21 |
| [[bld_tools_legal_vertical]] | related | 0.20 |
| [[bld_tools_multimodal_prompt]] | related | 0.20 |
