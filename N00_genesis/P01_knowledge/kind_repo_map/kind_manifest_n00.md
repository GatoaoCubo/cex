---
id: n00_repo_map_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Repo Map -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, repo_map, p01, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_repo_map
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_contributor_guide
  - bld_schema_benchmark_suite
  - bld_schema_quickstart_guide
  - bld_schema_multimodal_prompt
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Repo Map defines a codebase context extraction strategy that produces a structured summary of a software repository for use in LLM coding agents. It specifies which directories to index, how to represent file structure, and what code symbols to extract (functions, classes, APIs). Used by N05 and N03 to give coding agents navigable codebase context without consuming the full token budget.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `repo_map` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Repository name and scope |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| root_path | string | yes | Repository root directory path |
| include_patterns | list | yes | Glob patterns to include |
| exclude_patterns | list | no | Glob patterns to exclude |
| symbol_extraction | enum | yes | none\|functions\|classes\|full -- code symbol depth |
| output_format | enum | yes | tree\|json\|markdown\|ctags |
| max_depth | int | no | Maximum directory traversal depth |

## When to use
- When onboarding a coding agent to a new repository
- When building a RAG source from a codebase
- When creating context for code review or architecture analysis

## Builder
`archetypes/builders/repo_map-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind repo_map --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N05 or N03)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- coding agents and code review tools
- `{{DOMAIN_CONTEXT}}` -- programming language and project type

## Example (minimal)
```yaml
---
id: repo_map_cex_tools
kind: repo_map
pillar: P01
nucleus: n05
title: "CEX _tools/ Repo Map"
version: 1.0
quality: null
---
root_path: "C:/Users/CEX/Documents/GitHub/cex/_tools"
include_patterns: ["**/*.py"]
exclude_patterns: ["**/__pycache__/**"]
symbol_extraction: functions
output_format: markdown
max_depth: 3
```

## Related kinds
- `rag_source` (P01) -- the indexed result of a repo map
- `software_project` (P02) -- the project this map describes
- `context_doc` (P01) -- higher-level project documentation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_repo_map]] | downstream | 0.50 |
| [[bld_schema_reranker_config]] | downstream | 0.44 |
| [[bld_schema_integration_guide]] | downstream | 0.43 |
| [[bld_schema_dataset_card]] | downstream | 0.43 |
| [[bld_schema_usage_report]] | downstream | 0.42 |
| [[bld_schema_search_strategy]] | downstream | 0.41 |
| [[bld_schema_contributor_guide]] | downstream | 0.41 |
| [[bld_schema_benchmark_suite]] | downstream | 0.41 |
| [[bld_schema_quickstart_guide]] | downstream | 0.41 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.40 |
