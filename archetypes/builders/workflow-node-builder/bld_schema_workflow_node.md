---
kind: schema
id: bld_schema_workflow_node
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for workflow_node
quality: null
title: "Schema Workflow Node"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [workflow_node, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for workflow_node"
domain: "workflow_node construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field     | Type   | Required | Default | Notes                              |  
|-----------|--------|----------|---------|------------------------------------|  
| id        | string | yes      | null    | Unique identifier                  |  
| kind      | string | yes      | null    | Must be 'workflow_node'            |  
| pillar    | string | yes      | null    | Must be 'P12'                      |  
| title     | string | yes      | null    | Descriptive name                   |  
| version   | string | yes      | null    | Semantic version (e.g., 1.0.0)     |  
| created   | date   | yes      | null    | ISO 8601 timestamp                 |  
| updated   | date   | yes      | null    | ISO 8601 timestamp                 |  
| author    | string | yes      | null    | Creator                            |  
| domain    | string | yes      | null    | Workflow domain (e.g., 'data')     |  
| quality   | null   | yes      | null    | Never self-score; peer review assigns |  
| tags      | array  | yes      | null    | Keywords for categorization        |  
| tldr      | string | yes      | null    | One-sentence summary               |  
| input_type | string | yes      | null    | Expected input format              |  
| output_type | string | yes      | null    | Expected output format             |  

### Recommended  
| Field         | Type   | Notes                  |  
|---------------|--------|------------------------|  
| dependencies  | array  | Required workflow nodes |  
| status        | string | Active/Deprecated      |  

## ID Pattern  
^p12_wn_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and context of the workflow node.  

2. **Inputs/Outputs**  
   - Detailed description of input_type and output_type.  

3. **Execution**  
   - Steps, tools, or systems involved in processing.  

4. **Dependencies**  
   - List of required workflow nodes or external resources.  

5. **Status**  
   - Current lifecycle state (e.g., active, deprecated).  

6. **Metadata**  
   - Additional technical or operational details.  

## Constraints  
- Input_type and output_type must conform to standardized formats.  
- Dependencies must reference valid workflow_node IDs.  
- Status transitions require approval from the domain owner.  
- Versioning follows semantic versioning (SemVer) rules.  
- Quality must be assigned by at least two peer reviewers.  
- File size must not exceed 4096 bytes.
