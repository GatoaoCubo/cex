---
kind: schema
id: bld_schema_repo_map
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for repo_map
quality: 9.1
title: "Schema Repo Map"
version: "1.0.0"
author: wave1_builder_gen
tags: [repo_map, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for repo_map"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field      | Type   | Required | Default | Notes                          |  
|------------|--------|----------|---------|--------------------------------|  
| id         | string | yes      | -       | Unique identifier              |  
| kind       | string | yes      | "repo_map" | CEX kind type               |  
| pillar     | string | yes      | "P01"   | Pillar classification          |  
| title      | string | yes      | -       | Repository name                |  
| version    | string | yes      | "1.0"   | Schema version                 |  
| created    | date   | yes      | -       | Creation timestamp             |  
| updated    | date   | yes      | -       | Last update timestamp          |  
| author     | string | yes      | -       | Owner/creator                  |  
| domain     | string | yes      | -       | Repository domain (e.g., GitHub) |  
| quality    | string | yes      | "draft" | Quality status                 |  
| tags       | list   | yes      | []      | Keywords                       |  
| tldr       | string | yes      | -       | Summary                        |  
| token_budget | int | yes | 1024 | Max tokens for this map |
| symbol_count | int | yes | - | Total symbols extracted |
| file_count | int | yes | - | Files included in map |
| extraction_method | string | yes | "tree-sitter" | tree-sitter \| ctags \| hybrid |  

### Recommended  
| Field         | Type   | Notes                  |  
|---------------|--------|------------------------|  
| license_type  | string | License information    |  
| contributor_count | int  | Number of contributors |  

## ID Pattern  
^p01_rm_[a-zA-Z0-9_]+\.md$  

## Body Structure  
1. **Repository Overview**  
   - Description, purpose, and scope.  
2. **Mapping Details**  
   - Key-value pairs linking repository components.  
3. **Quality Assessment**  
   - Evaluation criteria and scores.  
4. **Domain-Specific Metadata**  
   - Additional fields for repository context.  
5. **Version History**  
   - Changes and updates over time.  

## Constraints  
- ID must follow `p01_rm_{{name}}.md` regex.  
- Required fields must be present and valid.  
- File size must not exceed 5120 bytes.  
- `repository_url` must be a valid URI.  
- `version` must use semantic versioning (e.g., "1.2.3").  
- `tags` must be unique and lowercase.
