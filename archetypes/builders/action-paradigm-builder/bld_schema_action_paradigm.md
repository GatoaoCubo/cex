---
kind: schema
id: bld_schema_action_paradigm
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for action_paradigm
quality: 9.2
title: "Schema Action Paradigm"
version: "1.0.0"
author: wave1_builder_gen
tags: [action_paradigm, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for action_paradigm"
domain: "action_paradigm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field      | Type   | Required | Default | Notes |  
|------------|--------|----------|---------|-------|  
| id         | string | yes      | -       | Unique identifier |  
| kind       | string | yes      | "action_paradigm" | CEX kind |  
| pillar     | string | yes      | "P04"    | Pillar reference |  
| title      | string | yes      | -       | Descriptive name |  
| version    | string | yes      | "1.0"    | Schema version |  
| created    | date   | yes      | -       | Creation timestamp |  
| updated    | date   | yes      | -       | Last update timestamp |  
| author     | string | yes      | -       | Owner/creator |  
| domain     | string | yes      | -       | Application domain |  
| quality    | null   | yes      | null     | Always null at authoring time; peer review assigns score |  
| tags       | list   | yes      | []       | Keywords |  
| tldr       | string | yes      | -       | Summary |  
| action_type | string | yes      | -       | Action classification |  
| scope      | string | yes      | -       | Operational scope |  
| impact_area | string | yes      | -       | Affected domain |  

### Recommended  
| Field              | Type   | Notes |  
|--------------------|--------|-------|  
| related_actions    | list   | Linked actions |  
| dependencies       | list   | Prerequisites |  
| risk_assessment    | string | Risk profile |  

## ID Pattern  
^p04_act_[a-zA-Z0-9_]+\.md$  

## Body Structure  
1. **Overview**  
   - Purpose, context, and scope of the action paradigm.  
2. **Key Principles**  
   - Core rules, values, or methodologies guiding implementation.  
3. **Implementation Steps**  
   - Phased approach, roles, and required resources.  
4. **Success Metrics**  
   - KPIs, benchmarks, and evaluation criteria.  
5. **Domain-Specific Considerations**  
   - Tailored adaptations for the target domain.  

## Constraints  
- Must align with organizational goals and regulatory frameworks.  
- Requires stakeholder validation before deployment.  
- All actions must be traceable to a defined impact area.  
- Versioning enforced for iterative updates.  
- Tags must include at least one domain-specific keyword.  
- TLDR must be under 256 characters.

## Properties

| Property | Value |
|----------|-------|
| Kind | `schema` |
| Pillar | P06 |
| Domain | action_paradigm construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
