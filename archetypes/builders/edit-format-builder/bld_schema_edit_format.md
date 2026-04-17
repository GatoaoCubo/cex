---
kind: schema
id: bld_schema_edit_format
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for edit_format
quality: 9.2
title: "Schema Edit Format"
version: "1.1.0"
author: n04_hybrid_review2
tags: [edit_format, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for edit_format"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Frontmatter Fields

This ISO specifies an edit format: how diffs or patches are expressed and applied.

### Required

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | yes | - | Matches `^p06_ef_[a-z0-9_]+$` |
| kind | string | yes | "edit_format" | CEX kind |
| pillar | string | yes | "P06" | Pillar classification |
| title | string | yes | - | Max 256 chars |
| version | string | yes | "1.0.0" | Semantic versioning |
| created | datetime | yes | - | ISO 8601 format |
| updated | datetime | yes | - | ISO 8601 format |
| author | string | yes | - | Author or nucleus ID |
| domain | string | yes | - | Use case domain (e.g., "code_agent", "config_mgmt") |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Max 10 lowercase alphanumeric tags |
| tldr | string | yes | - | Max 256 chars |
| format_type | enum | yes | - | See format_type enum below |
| edit_scope | enum | yes | - | See edit_scope enum below |

### Recommended

| Field | Type | Notes |
|-------|------|-------|
| description | string | Detailed purpose and tradeoffs |
| examples | list | 1-3 minimal usage examples |
| compatible_tools | list | Tools that can apply this format (e.g., "aider", "cursor", "git apply") |

## format_type Enum

```
format_type: whole_file | unified_diff | udiff_simple | search_replace | json_patch | lsp_textedit
```

| Value | Description |
|-------|-------------|
| whole_file | Full file replacement; LLM returns complete content |
| unified_diff | Standard `-u` format with `---`/`+++`/`@@ -n,m @@` headers |
| udiff_simple | Unified diff without context lines or `@@` headers |
| search_replace | SEARCH/REPLACE block pair anchored by exact content match |
| json_patch | RFC 6902 JSON Patch operations array |
| lsp_textedit | LSP v3.17 TextEdit with range + newText |

## edit_scope Enum

```
edit_scope: whole_file | partial_hunk | targeted_replace | multi_hunk
```

| Value | Description |
|-------|-------------|
| whole_file | Replaces entire file content |
| partial_hunk | Single contiguous block of changes |
| targeted_replace | Single search-replace pair |
| multi_hunk | Multiple non-contiguous change blocks in one response |

## ID Pattern

```
^p06_ef_[a-z0-9_]+$
```

Examples: `p06_ef_aider_whole`, `p06_ef_search_replace`, `p06_ef_unified_diff`

## Body Structure

1. **Overview**: Purpose, format family, primary use cases
2. **Format Specification**: Exact syntax with marked example, field definitions
3. **Application Rules**: How host tool MUST apply this format (exact match, fuzzy, line-number)
4. **Compatibility**: Which tools/editors can apply this format natively
5. **Validation Rules**: How to verify a response is valid for this format
6. **Examples**: One valid and one invalid example with explanation

## Constraints

- `quality` MUST be null
- `format_type` MUST be from the enum above
- `edit_scope` MUST be from the enum above
- ID MUST match naming pattern
- Tags MUST be lowercase alphanumeric
- Max file size: 4096 bytes
- Encoding: UTF-8 (no BOM for .md files)
