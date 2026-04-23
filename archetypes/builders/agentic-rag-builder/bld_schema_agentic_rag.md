---
kind: schema
id: bld_schema_agentic_rag
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for agentic_rag
quality: 9.1
title: "Schema Agentic Rag"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [agentic_rag, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for agentic_rag"
domain: "agentic_rag construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_prompt_technique
  - bld_schema_multimodal_prompt
  - bld_schema_roi_calculator
  - bld_schema_contributor_guide
  - bld_schema_eval_metric
  - bld_schema_onboarding_flow
  - bld_schema_pitch_deck
---

## Frontmatter Fields  
### Required  
| Field | Type | Required | Default | Notes |  
|---|---|---|---|---|  
| id | string | yes | null | Must match ID Pattern |  
| kind | string | yes | "agentic_rag" | CEX type |  
| pillar | string | yes | "P01" | Strategic focus area |  
| title | string | yes | null | Descriptive name |  
| version | string | yes | "1.0" | Schema version |  
| created | datetime | yes | null | ISO 8601 format |  
| updated | datetime | yes | null | ISO 8601 format |  
| author | string | yes | null | Responsible party |  
| domain | string | yes | "agentic_rag" | Application domain |  
| quality | null | yes | null | Peer-reviewed score |  
| tags | list | yes | [] | Metadata keywords |  
| tldr | string | yes | null | Summary (≤200 chars) |  
| agent_type | string | yes | null | Agent specialization |  
| knowledge_source | string | yes | null | Data origin |  

### Recommended  
| Field | Type | Notes |  
|---|---|---|  
| last_reviewed | datetime | Last peer review date |  
| reviewers | list | Peer reviewers |  

## ID Pattern  
^p01_ar_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and use case for agentic_rag.  
2. **Agent Configuration**  
   - Parameters, capabilities, and constraints.  
3. **Knowledge Sources**  
   - Integration details and data provenance.  
4. **Execution Workflow**  
   - Step-by-step operational logic.  
5. **Compliance**  
   - Regulatory and ethical considerations.  

## Constraints  
- File name must match ID Pattern exactly.  
- Total size must not exceed 5120 bytes.  
- Quality field must be assigned by peer review only.  
- Domain-specific fields (agent_type, knowledge_source) are mandatory.  
- Version must follow semantic versioning (e.g., 1.0.0).  
- All datetime fields must use ISO 8601 format.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | sibling | 0.77 |
| [[bld_schema_reranker_config]] | sibling | 0.74 |
| [[bld_schema_benchmark_suite]] | sibling | 0.72 |
| [[bld_schema_prompt_technique]] | sibling | 0.71 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.69 |
| [[bld_schema_roi_calculator]] | sibling | 0.69 |
| [[bld_schema_contributor_guide]] | sibling | 0.68 |
| [[bld_schema_eval_metric]] | sibling | 0.68 |
| [[bld_schema_onboarding_flow]] | sibling | 0.68 |
| [[bld_schema_pitch_deck]] | sibling | 0.68 |
