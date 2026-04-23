---
kind: schema
id: bld_schema_safety_policy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for safety_policy
quality: 9.1
title: "Schema Safety Policy"
version: "1.0.0"
author: wave1_builder_gen
tags: [safety_policy, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for safety_policy"
domain: "safety_policy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_sandbox_config
  - bld_schema_rbac_policy
  - bld_schema_reranker_config
  - bld_schema_pitch_deck
  - bld_schema_search_strategy
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
  - bld_schema_compliance_framework
---

## Frontmatter Fields
### Required
| Field         | Type       | Required | Default | Notes                              |
|---------------|------------|----------|---------|------------------------------------|
| id            | string     | yes      |         | Unique identifier                  |
| kind          | string     | yes      |         | "safety_policy"                    |
| pillar        | string     | yes      |         | "P11"                              |
| title         | string     | yes      |         | Policy name                        |
| version       | string     | yes      | "1.0.0" | Semantic versioning                |
| created       | datetime   | yes      |         | ISO 8601                           |
| updated       | datetime   | yes      |         | ISO 8601                           |
| author        | string     | yes      |         | Author name                        |
| domain        | string     | yes      |         | "CEX"                              |
| quality       | string     | yes      | "draft" | "draft", "review", "approved"      |
| tags          | list       | yes      | []      | Keywords                           |
| tldr          | string     | yes      |         | Summary                            |
| risk_level    | string     | yes      |         | "Low", "Medium", "High", "Critical"|
| compliance_framework | string | yes |         | Reference standard                 |
| enforcement_mechanisms | list | yes | []      | Actions for policy enforcement     |

### Recommended
| Field               | Type   | Notes                          |
|---------------------|--------|--------------------------------|
| last_reviewed       | date   | Last review date               |
| policy_owner        | string | Responsible team/individual    |
| related_policies    | list   | Linked policy IDs              |
| audit_frequency     | string | "Quarterly", "Annual", etc.    |

## ID Pattern
^p11_sp_[a-zA-Z0-9_]+\.md$

## Body Structure
1. **Policy Scope**
   Define the policy's applicability and boundaries.

2. **Risk Management Framework**
   Outline risk identification, assessment, and mitigation strategies.

3. **Compliance Requirements**
   Specify mandatory standards, regulations, and internal guidelines.

4. **Enforcement Mechanisms**
   Detail procedures for monitoring, reporting, and addressing violations.

5. **Incident Response Protocol**
   Describe steps for handling breaches, incidents, or non-compliance.

6. **Review and Update Process**
   Define frequency, triggers, and stakeholders for policy revisions.

## Constraints
- All required fields must be present and non-empty.
- Version must follow semantic versioning

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.69 |
| [[bld_schema_dataset_card]] | sibling | 0.69 |
| [[bld_schema_sandbox_config]] | sibling | 0.69 |
| [[bld_schema_rbac_policy]] | sibling | 0.69 |
| [[bld_schema_reranker_config]] | sibling | 0.68 |
| [[bld_schema_pitch_deck]] | sibling | 0.68 |
| [[bld_schema_search_strategy]] | sibling | 0.68 |
| [[bld_schema_quickstart_guide]] | sibling | 0.67 |
| [[bld_schema_benchmark_suite]] | sibling | 0.67 |
| [[bld_schema_compliance_framework]] | sibling | 0.66 |
