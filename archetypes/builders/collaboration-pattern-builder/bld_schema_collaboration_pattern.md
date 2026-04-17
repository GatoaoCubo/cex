---
kind: schema
id: bld_schema_collaboration_pattern
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for collaboration_pattern
quality: 9.2
title: "Schema Collaboration Pattern"
version: "1.0.0"
author: wave1_builder_gen
tags: [collaboration_pattern, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for collaboration_pattern"
domain: "collaboration_pattern construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field        | Type   | Required | Default | Notes                          |
|--------------|--------|----------|---------|--------------------------------|
| id           | string | yes      | -       | Unique identifier              |
| kind         | string | yes      | -       | "collaboration_pattern"        |
| pillar       | string | yes      | -       | "P12"                          |
| title        | string | yes      | -       | Human-readable name            |
| version      | string | yes      | "1.0"   | Schema version                 |
| created      | date   | yes      | -       | ISO 8601                       |
| updated      | date   | yes      | -       | ISO 8601                       |
| author       | string | yes      | -       | Owner                          |
| domain       | string | yes      | -       | Application domain             |
| quality      | null   | yes      | null    | Always null at authoring time; peer review assigns score |
| tags         | list   | yes      | []      | Keywords                       |
| tldr         | string | yes      | -       | Summary                        |
| collaboration_type | string | yes | - | "cross-functional", "external", etc. |
| stakeholders | list   | yes      | []      | Involved parties               |
| success_metrics | list | yes | []      | KPIs                           |
| governance_model | string | yes | - | "decentralized", "hierarchical" |

### Recommended
| Field              | Type   | Notes                          |
|--------------------|--------|--------------------------------|
| risk_assessment    | string | Potential risks                |
| communication_protocols | string | Channels and rules           |
| conflict_resolution | string | Dispute handling mechanism   |

## ID Pattern
^p12_collab_[a-zA-Z0-9_]+\.md$

## Body Structure
1. **Overview**
   Describe the collaboration's purpose, scope, and objectives.

2. **Key Components**
   List core elements (e.g., workflows, tools, roles).

3. **Stakeholders**
   Detail roles, responsibilities, and engagement levels.

4. **Success Metrics**
   Define quantifiable outcomes and KPIs.

5. **Governance Model**
   Explain decision-making structure and accountability.

6. **Challenges**
   Identify potential barriers and mitigation strategies.

## Constraints
- Collaboration_type must be one of: "cross-functional", "external", "internal", "hybrid".
- Stakeholders list must include at least 2 distinct entities.
- Success_metrics must align with domain-specific KPIs.
- Governance_model must specify authority hierarchy.
- Created and updated dates must be within 1 year of each other.
- File size must not exceed 5120 bytes.

## Properties

| Property | Value |
|----------|-------|
| Kind | `schema` |
| Pillar | P06 |
| Domain | collaboration_pattern construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
