---
kind: schema
id: bld_schema_edit_format
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for edit_format
quality: null
title: "Schema Edit Format"
version: "1.0.0"
author: wave1_builder_gen
tags: [edit_format, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for edit_format"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
Field | Type | Required | Default | Notes  
--- | --- | --- | --- | ---  
id | string | yes | - | Regex: ^p06_ef_[a-zA-Z0-9_]+\.md$  
kind | string | yes | "edit_format" | -  
pillar | string | yes | "P06" | -  
title | string | yes | - | Max 256 chars  
version | string | yes | "1.0.0" | Semantic versioning  
created | datetime | yes | - | ISO 8601 format  
updated | datetime | yes | - | ISO 8601 format  
author | string | yes | - | Max 128 chars  
domain | string | yes | - | E.g., "content", "metadata"  
quality | string | yes | "draft" | Values: draft, review, final  
tags | list | yes | [] | Max 10 tags  
tldr | string | yes | - | Max 256 chars  
format_type | string | yes | - | E.g., "markdown", "json"  
edit_scope | string | yes | - | E.g., "structure", "style"  

### Recommended  
Field | Type | Notes  
--- | --- | ---  
description | string | Max 1024 chars  
examples | list | Example usage  
dependencies | list | Required tools/formats  

## ID Pattern  
^p06_ef_[a-zA-Z0-9_]+\.md$  

## Body Structure  
1. **Overview**  
   - Purpose and scope of the edit format  
2. **Format Specifications**  
   - Required syntax and structure  
3. **Usage Guidelines**  
   - Best practices and limitations  
4. **Validation Rules**  
   - Schema or regex for validation  
5. **Examples**  
   - Valid and invalid format samples  
6. **Version History**  
   - Changes per version  

## Constraints  
- All required fields must be present and non-empty  
- Format_type must align with supported editors  
- Edit_scope must be one of: structure, style, metadata  
- Tags must be lowercase and alphanumeric  
- File size must not exceed 4096 bytes  
- Encoding must be UTF-8 without BOM
