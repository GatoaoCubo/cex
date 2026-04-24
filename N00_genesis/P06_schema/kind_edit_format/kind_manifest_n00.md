---
id: n00_edit_format_manifest
kind: knowledge_card
8f: F3_inject
pillar: P06
nucleus: n00
title: "Edit Format -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, edit_format, p06, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_edit_format
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_examples_edit_format
  - bld_schema_benchmark_suite
  - bld_schema_sandbox_spec
  - bld_schema_contributor_guide
  - bld_schema_thinking_config
  - bld_schema_usage_report
  - bld_schema_pitch_deck
---

<!-- 8F: F1=knowledge_card P06 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Edit format defines the structured specification for how an LLM communicates file changes to a host environment. It constrains the syntax, semantics, and validation rules for diff-like change representations including search-replace blocks, unified diff format, whole-file replacement, and structured JSON patch. Used in agentic coding environments (Aider, Claude Code, Cursor) to ensure reliable, parseable file modifications.

## Pillar
P06 -- Schema

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `edit_format` |
| pillar | string | yes | Always `P06` |
| title | string | yes | Format name (e.g., "CEX Search-Replace Edit Format") |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| format_type | enum | yes | search_replace / unified_diff / whole_file / json_patch |
| file_path_convention | string | yes | How file paths are specified in the format |
| change_block_syntax | string | yes | Exact syntax for a single change block |
| validation_rules | list | yes | Rules for accepting/rejecting an edit block |
| conflict_policy | enum | yes | reject / warn / force |

## When to use
- Defining the edit protocol for a custom agentic coding environment
- Specifying how a multi-agent pipeline communicates file changes between roles
- Documenting the accepted change format for a pre-commit validation hook

## Builder
`archetypes/builders/edit_format-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind edit_format --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N03 engineering + N05 operations define edit formats
- `{{SIN_LENS}}` -- Inventive Pride: unambiguous, machine-parseable format
- `{{TARGET_AUDIENCE}}` -- LLM agents and host-side parsers consuming the edit blocks
- `{{DOMAIN_CONTEXT}}` -- coding environment, file types, conflict resolution policy

## Example (minimal)
```yaml
---
id: edit_format_cex_search_replace
kind: edit_format
pillar: P06
nucleus: n03
title: "CEX Search-Replace Edit Format"
version: 1.0
quality: null
---
format_type: search_replace
conflict_policy: reject
change_block_syntax: |
  <<<<<<< SEARCH
  {old_content}
  =======
  {new_content}
  >>>>>>> REPLACE
```

## Related kinds
- `validator` (P06) -- validates edit blocks against this format spec
- `input_schema` (P06) -- schema for the structured input to the edit operation
- `output_validator` (P05) -- post-application check that the edit was applied correctly

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_edit_format]] | related | 0.42 |
| [[bld_schema_reranker_config]] | related | 0.42 |
| [[bld_schema_integration_guide]] | related | 0.41 |
| [[bld_examples_edit_format]] | downstream | 0.40 |
| [[bld_schema_benchmark_suite]] | related | 0.40 |
| [[bld_schema_sandbox_spec]] | related | 0.39 |
| [[bld_schema_contributor_guide]] | related | 0.39 |
| [[bld_schema_thinking_config]] | related | 0.39 |
| [[bld_schema_usage_report]] | related | 0.39 |
| [[bld_schema_pitch_deck]] | related | 0.39 |
