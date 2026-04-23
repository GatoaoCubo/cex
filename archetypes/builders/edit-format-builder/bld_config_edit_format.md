---
kind: config
id: bld_config_edit_format
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for edit_format production
quality: 8.6
title: "Config Edit Format"
version: "1.1.0"
author: n04_hybrid_review2
tags: [edit_format, builder, config]
tldr: "Naming, paths, limits for edit_format production"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_bugloop
  - bld_schema_sandbox_spec
  - bld_schema_edit_format
  - bld_schema_contributor_guide
  - bld_schema_benchmark_suite
  - bld_schema_prompt_technique
  - bld_schema_quickstart_guide
  - bld_schema_onboarding_flow
---

## Naming Convention
This ISO specifies an edit format: how diffs or patches are expressed and applied.

Pattern: `p06_ef_{{name}}.md`

Examples:
- `p06_ef_search_replace.md`
- `p06_ef_unified_diff.md`
- `p06_ef_whole_file.md`
- `p06_ef_json_patch.md`

## Paths
Storage: `P06_schema/edit_formats/p06_ef_{{name}}.md`

## Limits
- `max_bytes`: 4096
- `max_turns`: 3
- `effort_level`: 2

## Hooks
- `pre_build`: null
- `post_build`: `python _tools/cex_compile.py {path}`
- `on_error`: null
- `on_quality_fail`: null

## Edit Format Matrix
| Format | Granularity | Reversible | Use Case |
|--------|------------|-----------|----------|
| search_replace | line-level | Yes | LLM code edits |
| unified_diff | hunk-level | Yes | Git patches |
| whole_file | file-level | Yes | Complete rewrites |
| json_patch | key-level | Yes | JSON/YAML updates |
| xml_diff | element-level | Yes | Structured docs |
| inline_comment | token-level | Partial | Annotation |
| semantic_diff | node-level | Yes | AST-based refactors |
| binary_delta | byte-level | Yes | Binary files |
| block_edit | block-level | Yes | Large sections |
| minimal_diff | optimal | Yes | Minimal changes |

## Quality Gates
| Gate | Check |
|------|-------|
| format_type required | From allowed enum |
| encoding documented | How format is encoded |
| example provided | At least 1 apply example |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | upstream | 0.39 |
| [[bld_schema_reranker_config]] | upstream | 0.39 |
| [[bld_schema_bugloop]] | downstream | 0.38 |
| [[bld_schema_sandbox_spec]] | upstream | 0.38 |
| [[bld_schema_edit_format]] | upstream | 0.37 |
| [[bld_schema_contributor_guide]] | upstream | 0.37 |
| [[bld_schema_benchmark_suite]] | upstream | 0.36 |
| [[bld_schema_prompt_technique]] | upstream | 0.36 |
| [[bld_schema_quickstart_guide]] | upstream | 0.35 |
| [[bld_schema_onboarding_flow]] | upstream | 0.35 |
