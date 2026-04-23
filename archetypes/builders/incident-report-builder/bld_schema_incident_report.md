---
kind: schema
id: bld_schema_incident_report
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for incident_report
quality: 9.1
title: "Schema Incident Report"
version: "1.0.0"
author: wave1_builder_gen
tags: [incident_report, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for incident_report"
domain: "incident_report construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_sandbox_config
  - bld_schema_pitch_deck
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_safety_policy
  - bld_schema_agent_profile
  - bld_schema_benchmark_suite
  - bld_schema_prompt_technique
  - bld_schema_quickstart_guide
---

## Frontmatter Fields  
### Required  
| Field          | Type       | Required | Default | Notes                              |  
|----------------|------------|----------|---------|------------------------------------|  
| id             | string     | yes      | -       | Unique identifier                  |  
| kind           | string     | yes      | "incident_report" | CEX document type         |  
| pillar         | string     | yes      | "P11"    | Pillar classification              |  
| title          | string     | yes      | -       | Concise summary of incident        |  
| version        | string     | yes      | "1.0"    | Document version                   |  
| created        | datetime   | yes      | -       | ISO 8601 format                    |  
| updated        | datetime   | yes      | -       | ISO 8601 format                    |  
| author         | string     | yes      | -       | Responsible party                  |  
| domain         | string     | yes      | -       | Affected system/service            |  
| quality        | string     | yes      | "draft"  | "draft", "reviewed", "final"       |  
| tags           | list       | yes      | []      | Keywords (e.g., "security", "outage") |  
| tldr           | string     | yes      | -       | One-sentence incident summary      |  
| incident_date  | datetime   | yes      | -       | Date of incident                   |  
| impact_summary | string     | yes      | -       | Brief impact description           |  

### Recommended  
| Field              | Type   | Notes                          |  
|--------------------|--------|--------------------------------|  
| resolution_status  | string | "open", "closed", "investigating" |  
| root_cause_analysis| string | Analysis of incident cause     |  

## ID Pattern  
^p11_ir_[a-zA-Z0-9_]+\.md$  

## Body Structure  
1. **Overview**  
   - Incident summary, scope, and context.  
2. **Timeline**  
   - Chronological sequence of events.  
3. **Impact**  
   - Systems affected, user impact, and financial/operational consequences.  
4. **Resolution**  
   - Actions taken to mitigate and resolve the incident.  
5. **Root Cause Analysis**  
   - Detailed technical and procedural analysis.  
6. **Lessons Learned**  
   - Improvements to prevent recurrence.  

## Constraints  
- All required fields must be present and non-empty.  
- `created` and `updated` must use ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ).  
- `id` must match the regex pattern and be unique.  
- `tags` must be a list of lowercase alphanumeric strings separated by commas.  
- `version` must follow semantic versioning (e.g., "1.0.0").

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_sandbox_config]] | sibling | 0.69 |
| [[bld_schema_pitch_deck]] | sibling | 0.68 |
| [[bld_schema_reranker_config]] | sibling | 0.68 |
| [[bld_schema_usage_report]] | sibling | 0.67 |
| [[bld_schema_dataset_card]] | sibling | 0.67 |
| [[bld_schema_safety_policy]] | sibling | 0.66 |
| [[bld_schema_agent_profile]] | sibling | 0.66 |
| [[bld_schema_benchmark_suite]] | sibling | 0.66 |
| [[bld_schema_prompt_technique]] | sibling | 0.64 |
| [[bld_schema_quickstart_guide]] | sibling | 0.64 |
