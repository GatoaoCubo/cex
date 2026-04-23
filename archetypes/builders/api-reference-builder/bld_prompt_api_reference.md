---
kind: instruction
id: bld_instruction_api_reference
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for api_reference
quality: 8.8
title: "Instruction Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, instruction]
tldr: "Step-by-step production process for api_reference"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_api_reference_builder
  - p10_lr_api_reference_builder
  - api-reference-builder
  - bld_instruction_integration_guide
  - kc_api_reference
  - p06_qg_api_reference
  - bld_knowledge_card_api_reference
  - p11_qg_client
  - bld_examples_api_reference
  - bld_output_template_api_reference
---

## Phase 1: RESEARCH  
1. Collect all endpoints from API spec (POST, GET, PUT, DELETE).  
2. Document authentication methods (OAuth2, API keys, Bearer tokens).  
3. Extract parameters (query, path, body) with data types and constraints.  
4. Define response formats (JSON, XML) and error codes (4xx, 5xx).  
5. Gather example requests/responses for each endpoint.  
6. Validate against bld_schema_api_reference.md for structure and constraint compliance.  

## Phase 2: COMPOSE  
1. Create table of contents with grouped endpoints (e.g., /v1/resources).  
2. Write endpoint descriptions with HTTP method, path, and summary.  
3. Add authentication section (scopes, token flow, headers).  
4. Detail parameters (name, type, required, example) per endpoint.  
5. Specify response codes, schemas, and example payloads.  
6. Insert example requests/responses with cURL and JSON samples.  
7. Cross-reference bld_schema_api_reference.md to ensure parameter/response alignment.  
8. Use bld_output_template_api_reference.md for consistent formatting (tables, code blocks).  
9. Finalize with versioning, changelog, and API lifecycle notes.  

## Phase 3: VALIDATE  
[ ] All endpoints listed with correct methods/paths  
[ ] Authentication details match bld_schema_api_reference.md and spec  
[ ] Example requests/responses pass constraint validation  
[ ] Formatting adheres to bld_output_template_api_reference.md rules  
[ ] Peer review confirms clarity and completeness


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_api_reference_builder]] | related | 0.35 |
| [[p10_lr_api_reference_builder]] | downstream | 0.34 |
| [[api-reference-builder]] | downstream | 0.34 |
| [[bld_instruction_integration_guide]] | sibling | 0.27 |
| [[kc_api_reference]] | upstream | 0.27 |
| [[p06_qg_api_reference]] | downstream | 0.26 |
| [[bld_knowledge_card_api_reference]] | upstream | 0.26 |
| [[p11_qg_client]] | downstream | 0.25 |
| [[bld_examples_api_reference]] | downstream | 0.24 |
| [[bld_output_template_api_reference]] | downstream | 0.23 |
