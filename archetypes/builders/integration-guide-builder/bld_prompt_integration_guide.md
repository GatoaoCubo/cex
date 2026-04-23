---
kind: instruction
id: bld_instruction_integration_guide
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for integration_guide
quality: 8.9
title: "Instruction Integration Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [integration_guide, builder, instruction]
tldr: "Step-by-step production process for integration_guide"
domain: "integration_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_integration_guide_builder
  - bld_instruction_api_reference
  - p10_lr_integration_guide_builder
  - bld_instruction_tts_provider
  - bld_instruction_quickstart_guide
  - integration-guide-builder
  - kc_integration_guide
  - bld_instruction_sdk_example
  - bld_instruction_playground_config
  - bld_instruction_judge_config
---

## Phase 1: RESEARCH  
1. Gather API specifications, SDKs, and authentication protocols from platform partners.  
2. Interview paid-tier customers to identify onboarding pain points and integration requirements.  
3. Analyze existing documentation for gaps in workflow diagrams, error codes, and rate-limiting rules.  
4. Map integration patterns (e.g., OAuth 2.0, webhook subscriptions) used across partner ecosystems.  
5. Document platform-specific constraints (e.g., data formats, latency thresholds, compliance rules).  
6. Compile a list of use cases for core features (e.g., user provisioning, payment processing).  

## Phase 2: COMPOSE  
1. Structure the guide using SCHEMA.md’s hierarchy: overview, prerequisites, API references, code samples.  
2. Write an introduction explaining the platform’s integration philosophy and partner benefits.  
3. Detail API endpoints with HTTP methods, parameters, and response formats (reference SCHEMA.md).  
4. Include code samples in multiple languages (Python, JavaScript, cURL) per OUTPUT_TEMPLATE.md.  
5. Explain authentication flows (API keys, OAuth, SSO) with step-by-step configuration guides.  
6. Add troubleshooting sections for common errors (4xx/5xx codes, timeout scenarios).  
7. Embed workflow diagrams for end-to-end onboarding processes (e.g., from registration to production).  
8. Reference OUTPUT_TEMPLATE.md to ensure consistency in terminology and formatting.  
9. Finalize with a checklist for partners to validate integration completeness.  

## Phase 3: VALIDATE  
- [ ] Confirm alignment with SCHEMA.md’s structure and OUTPUT_TEMPLATE.md’s formatting rules.  
- [ ] Verify code samples execute without errors in sandbox environments.  
- [ ] Ensure all API endpoints and authentication methods are accurately described.  
- [ ] Validate that onboarding workflows match partner feedback from Phase 1.  
- [ ] Obtain stakeholder approval for final content and technical accuracy.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_integration_guide_builder]] | related | 0.38 |
| [[bld_instruction_api_reference]] | sibling | 0.33 |
| [[p10_lr_integration_guide_builder]] | downstream | 0.32 |
| [[bld_instruction_tts_provider]] | sibling | 0.30 |
| [[bld_instruction_quickstart_guide]] | sibling | 0.29 |
| [[integration-guide-builder]] | downstream | 0.26 |
| [[kc_integration_guide]] | upstream | 0.25 |
| [[bld_instruction_sdk_example]] | sibling | 0.25 |
| [[bld_instruction_playground_config]] | sibling | 0.24 |
| [[bld_instruction_judge_config]] | sibling | 0.24 |
