---
kind: instruction
id: bld_instruction_sdk_example
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for sdk_example
quality: 8.9
title: "Instruction Sdk Example"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sdk_example, builder, instruction]
tldr: "Step-by-step production process for sdk_example"
domain: "sdk_example construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_sdk_example_builder
  - sdk-example-builder
  - bld_instruction_tts_provider
  - bld_instruction_stt_provider
  - p10_lr_sdk_example_builder
  - p04_qg_sdk_example
  - bld_instruction_search_strategy
  - p07_sr_engineering_quality
  - bld_instruction_integration_guide
  - bld_instruction_edit_format
---

## Phase 1: RESEARCH  
1. Identify target programming languages for SDK examples (e.g., Python, Java, JS).  
2. Analyze existing SDKs for canonical integration patterns (authentication, API calls, error handling).  
3. Gather use cases from P04 domain (e.g., payment processing, user management).  
4. Map use cases to language-specific implementation requirements.  
5. Research language-specific best practices (e.g., Python’s async, Java’s exceptions).  
6. Document research findings into a requirements matrix.  

## Phase 2: COMPOSE  
1. Create project structure per bld_schema_sdk_example.md (e.g., `examples/`, `tests/`, `docs/`).  
2. Write code examples for each language, aligning with mapped use cases.  
3. Implement authentication flow using P04-standard tokens (refer to bld_schema_sdk_example.md).  
4. Use bld_output_template_sdk_example.md for code formatting (indentation, comments, variable names).  
5. Add error handling per language conventions (e.g., Python’s `try/except`, JS’s `try/catch`).  
6. Write unit tests for each example (e.g., mock API responses, validate edge cases).  
7. Generate documentation stubs in `docs/` (API references, usage examples).  
8. Conduct code review against bld_schema_sdk_example.md compliance and P04 domain rules.  
9. Package artifact with versioning (e.g., `sdk_example-v1.0.0.tar.gz`).  

## Phase 3: VALIDATE  
- [ ] All code examples conform to bld_schema_sdk_example.md structure and P04 function specs.  
- [ ] Unit tests pass for all languages (coverage >=90%).  
- [ ] Error handling matches language-specific best practices.  
- [ ] Documentation in `docs/` aligns with bld_output_template_sdk_example.md.  
- [ ] Artifact builds successfully across target languages (CI/CD pipeline).


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_sdk_example_builder]] | related | 0.29 |
| [[sdk-example-builder]] | downstream | 0.27 |
| [[bld_instruction_tts_provider]] | sibling | 0.27 |
| [[bld_instruction_stt_provider]] | sibling | 0.26 |
| [[p10_lr_sdk_example_builder]] | downstream | 0.24 |
| [[p04_qg_sdk_example]] | downstream | 0.23 |
| [[bld_instruction_search_strategy]] | sibling | 0.21 |
| [[p07_sr_engineering_quality]] | downstream | 0.20 |
| [[bld_instruction_integration_guide]] | sibling | 0.20 |
| [[bld_instruction_edit_format]] | sibling | 0.19 |
