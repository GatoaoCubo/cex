---
kind: schema
id: bld_schema_ai_rmf_profile
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for ai_rmf_profile
quality: 9.1
title: "Schema AI RMF Profile"
version: "1.0.0"
author: n01_wave7
tags: [ai_rmf_profile, builder, schema, NIST, AI-RMF, GOVERN, MAP, MEASURE, MANAGE, GenAI-profile, 600-1, action-ID, risk-category]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for ai_rmf_profile"
domain: "ai_rmf_profile construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_agent_profile
  - bld_schema_search_strategy
  - bld_schema_pitch_deck
  - bld_schema_sandbox_config
  - bld_schema_reranker_config
  - bld_schema_action_paradigm
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
  - bld_schema_safety_policy
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | yes | | Pattern: p11_rmf_{{profile}}.md |
| kind | string | yes | | Must be: ai_rmf_profile |
| pillar | string | yes | | Must be: P11 |
| title | string | yes | | Include "AI RMF GenAI Profile" in title |
| version | string | yes | | Semantic version of profile |
| created | date | yes | | ISO 8601 |
| updated | date | yes | | ISO 8601 |
| author | string | yes | | Profile author / team |
| domain | string | yes | | AI system domain being profiled |
| quality | null | yes | null | Never self-score |
| tags | array | yes | | Include: NIST, AI-RMF, 600-1 minimum |
| tldr | string | yes | | One-line profile summary |
| profile_scope | string | yes | | System name + deployment context |
| review_date | date | yes | | Next scheduled review date |
| profiler | string | yes | | Team / individual responsible |

### Recommended
| Field | Type | Notes |
|-------|------|-------|
| system_type | string | GenAI, recommendation, classification, etc. |
| deployment_context | string | Cloud/on-prem, B2B/B2C, sector |
| nist_version | string | AI-RMF 1.0, AI 600-1 |

## ID Pattern
^p11_rmf_[a-z][a-z0-9_]+\.md$

## Body Structure
1. **Function Coverage** -- Table: Function | Action-IDs | Implementation Status
2. **Risk Category Severity Matrix** -- Table: Category | Severity | Controlling Action-IDs | Response
3. **Crosswalk Table** -- Columns: AI-RMF Action-ID | Description | ISO 42001 Control | EU AI Act Ref
4. **Gap Analysis** -- Action-IDs with no implementation assigned + remediation plan
5. **Evidence Pointers** -- Per action-ID: link to policy doc, test result, audit log

## Constraints
- All 4 functions must appear in Function Coverage table.
- All 12 GenAI risk categories from AI 600-1 must appear in Risk Category Severity Matrix.
- Action-ID format: {prefix}-{digit}.{digit} where prefix in [GV, MP, MS, MG].
- implementation_status must be one of: Implemented / Partial / Planned / Not Applicable.
- severity must be one of: Low / Moderate / High / Critical.
- review_date must be in ISO 8601 format and within 12 months of created date.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.63 |
| [[bld_schema_agent_profile]] | sibling | 0.62 |
| [[bld_schema_search_strategy]] | sibling | 0.62 |
| [[bld_schema_pitch_deck]] | sibling | 0.61 |
| [[bld_schema_sandbox_config]] | sibling | 0.60 |
| [[bld_schema_reranker_config]] | sibling | 0.60 |
| [[bld_schema_action_paradigm]] | sibling | 0.60 |
| [[bld_schema_quickstart_guide]] | sibling | 0.60 |
| [[bld_schema_benchmark_suite]] | sibling | 0.60 |
| [[bld_schema_safety_policy]] | sibling | 0.60 |
