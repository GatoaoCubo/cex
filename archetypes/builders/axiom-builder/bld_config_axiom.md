---
kind: config
id: bld_config_axiom
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Axiom"
version: "1.0.0"
author: n03_builder
tags: [axiom, builder, examples]
tldr: "Golden and anti-examples for axiom construction, demonstrating ideal structure and common pitfalls."
domain: "axiom construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_retriever_config
  - bld_config_memory_scope
  - bld_config_prompt_version
  - p03_sp_axiom_builder
  - bld_output_template_axiom
  - bld_architecture_axiom
  - bld_config_output_validator
  - bld_config_quality_gate
  - p11_qg_axiom
  - bld_config_handoff_protocol
---
# Config: axiom Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_ax_{slug}.md` | `p10_ax_quality_never_self_scored.md` |
| Builder directory | kebab-case | `axiom-builder/` |
| Frontmatter fields | snake_case | `linked_artifacts`, `density_score` |
| Slug | lowercase + underscores | `quality_never_self_scored` |
Rule: id MUST equal filename stem.
## File Paths
1. Output: `cex/P10_memory/examples/p10_ax_{slug}.md`
2. Compiled: `cex/P10_memory/compiled/p10_ax_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 3072 bytes
2. Total: ~4000 bytes (frontmatter + body)
3. Density: >= 0.80
## Axiom-Specific Constraints
1. Rule atomicity: ONE sentence, no conjunctions ("and", "or", "but")
2. Immutability test: if the rule could change in 5 years, it is a law, not an axiom
3. Scope precision: must name domain boundary (e.g., "all CEX artifacts" not "the system")
4. No operational details: axiom states WHAT, never HOW
5. Dependencies: only reference other axioms (never laws, guardrails, or instructions)

## Metadata

```yaml
id: bld_config_axiom
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-axiom.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | axiom construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_retriever_config]] | sibling | 0.47 |
| [[bld_config_memory_scope]] | sibling | 0.45 |
| [[bld_config_prompt_version]] | sibling | 0.43 |
| [[p03_sp_axiom_builder]] | upstream | 0.43 |
| [[bld_output_template_axiom]] | upstream | 0.43 |
| [[bld_architecture_axiom]] | upstream | 0.42 |
| [[bld_config_output_validator]] | sibling | 0.42 |
| [[bld_config_quality_gate]] | sibling | 0.42 |
| [[p11_qg_axiom]] | downstream | 0.42 |
| [[bld_config_handoff_protocol]] | sibling | 0.41 |
