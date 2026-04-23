---
id: n00_diff_strategy_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Diff Strategy -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, diff_strategy, p04, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_schema_diff_strategy
  - bld_schema_search_strategy
  - bld_schema_reranker_config
  - bld_schema_rl_algorithm
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
  - bld_schema_voice_pipeline
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A diff_strategy defines the change application and matching algorithm used when agents modify existing files, specifying how to locate the target section, apply the change, and validate the result. It governs whether the agent uses unified diff format, search-and-replace blocks, AST-level edits, or full-file overwrites. The output is a reusable change protocol that minimizes destructive edits and maximizes merge safety.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `diff_strategy` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| algorithm | string | yes | unified_diff, search_replace, ast_edit, full_rewrite |
| match_method | string | yes | exact, fuzzy, line_number, regex |
| conflict_resolution | string | yes | abort, prefer_new, prefer_existing, manual |
| validation_step | boolean | yes | Whether to verify the applied change before committing |

## When to use
- When an agent is modifying existing code or documentation files and must do so safely
- When the build pipeline uses an Edit tool that needs a specified matching strategy
- When N05 handles code review and patch application with conflict detection

## Builder
`archetypes/builders/diff_strategy-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind diff_strategy --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ds_search_replace_safe
kind: diff_strategy
pillar: P04
nucleus: n05
title: "Search-Replace Safe Diff Strategy"
version: 1.0
quality: null
---
algorithm: search_replace
match_method: exact
conflict_resolution: abort
validation_step: true
```

## Related kinds
- `code_executor` (P04) -- executor that validates the applied diff by running tests
- `hook` (P04) -- pre-commit hook that enforces diff_strategy before changes are saved
- `bugloop` (P11) -- iterative fix loop that applies diffs repeatedly until tests pass
- `cli_tool` (P04) -- git cli_tool that applies the final validated diff

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_diff_strategy]] | downstream | 0.48 |
| [[bld_schema_search_strategy]] | downstream | 0.46 |
| [[bld_schema_reranker_config]] | downstream | 0.46 |
| [[bld_schema_rl_algorithm]] | downstream | 0.45 |
| [[bld_schema_benchmark_suite]] | downstream | 0.44 |
| [[bld_schema_usage_report]] | downstream | 0.44 |
| [[bld_schema_integration_guide]] | downstream | 0.43 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.43 |
| [[bld_schema_dataset_card]] | downstream | 0.43 |
| [[bld_schema_voice_pipeline]] | downstream | 0.43 |
