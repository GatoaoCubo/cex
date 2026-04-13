---
kind: schema
id: bld_schema_bias_audit
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for bias_audit
quality: null
title: "Schema Bias Audit"
version: "1.0.0"
author: wave1_builder_gen
tags: [bias_audit, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for bias_audit"
domain: "bias_audit construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field      | Type   | Required | Default | Notes |  
|------------|--------|----------|---------|-------|  
| id         | string | yes      | -       | Unique identifier |  
| kind       | string | yes      | "bias_audit" | CEX type |  
| pillar     | string | yes      | "P07"    | Pillar classification |  
| title      | string | yes      | -       | Audit title |  
| version    | string | yes      | "1.0"   | Schema version |  
| created    | date   | yes      | -       | ISO 8601 format |  
| updated    | date   | yes      | -       | ISO 8601 format |  
| author     | string | yes      | -       | Responsible party |  
| domain     | string | yes      | -       | Application domain |  
| quality    | string | yes      | "draft" | Quality status |  
| tags       | list   | yes      | []      | Keywords |  
| tldr       | string | yes      | -       | Summary |  
| bias_type  | string | yes      | -       | Type of bias (e.g., algorithmic, data) |  
| affected_groups | list | yes | [] | Populations impacted |  

### Recommended  
| Field              | Type   | Notes |  
|--------------------|--------|-------|  
| mitigation_steps   | list   | Actions to address bias |  
| audit_date         | date   | Audit execution date |  

## ID Pattern  
^p07_ba_[a-zA-Z0-9_]+\.md$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and context of the audit.  
2. **Methodology**  
   - Tools, data sources, and evaluation criteria used.  
3. **Findings**  
   - Detailed results, including bias metrics and examples.  
4. **Recommendations**  
   - Mitigation strategies and corrective actions.  
5. **Stakeholder Impact**  
   - Effects on users, systems, and organizational policies.  

## Constraints  
- All required fields must be present and valid.  
- ID must match regex pattern.  
- Version must follow semantic versioning (e.g., "1.0.0").  
- Audit_date must be in ISO 8601 format.  
- File size must not exceed 5120 bytes.  
- Tags must be lowercase and separated by commas.
