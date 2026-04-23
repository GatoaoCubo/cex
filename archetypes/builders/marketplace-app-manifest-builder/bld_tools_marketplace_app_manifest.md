---
kind: tools
id: bld_tools_marketplace_app_manifest
pillar: P04
llm_function: CALL
purpose: Tools available for marketplace_app_manifest production
quality: 8.9
title: "Tools Marketplace App Manifest"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [marketplace_app_manifest, builder, tools]
tldr: "Tools available for marketplace_app_manifest production"
domain: "marketplace_app_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_marketplace_app_manifest
  - bld_tools_vad_config
  - bld_tools_api_reference
  - bld_tools_faq_entry
  - bld_tools_quickstart_guide
  - bld_manifest_memory_type
  - bld_tools_sdk_example
  - bld_tools_prosody_config
  - bld_tools_edit_format
  - p02_agent_software_project_manifest
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles app manifest from source files | During build process |
| cex_score.py | Evaluates manifest compliance with marketplace rules | Pre-deployment validation |
| cex_retriever.py | Fetches external dependencies for manifest | When resolving third-party assets |
| cex_doctor.py | Diagnoses manifest errors and suggests fixes | Post-validation troubleshooting |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| validate_manifest.py | Checks manifest syntax and structure | Pre-submission |
| schema_checker.py | Ensures adherence to marketplace schema | During development |
| linter_manifest.py | Enforces coding standards in manifest files | Continuous integration |

## External References
- JSON Schema (for manifest structure validation)
- PyYAML (for parsing manifest metadata)
- Marketplace API v2.1 (for runtime compliance checks)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_marketplace_app_manifest]] | downstream | 0.35 |
| [[bld_tools_vad_config]] | sibling | 0.31 |
| [[bld_tools_api_reference]] | sibling | 0.31 |
| [[bld_tools_faq_entry]] | sibling | 0.27 |
| [[bld_tools_quickstart_guide]] | sibling | 0.27 |
| [[bld_manifest_memory_type]] | upstream | 0.27 |
| [[bld_tools_sdk_example]] | sibling | 0.25 |
| [[bld_tools_prosody_config]] | sibling | 0.25 |
| [[bld_tools_edit_format]] | sibling | 0.25 |
| [[p02_agent_software_project_manifest]] | upstream | 0.24 |
