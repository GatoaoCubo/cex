---
id: bld_tools_type_def
kind: tools
pillar: P04
llm_function: CALL
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [tools, type-def, P04, tooling]
quality: 9.1
title: "Tools Type Def"
tldr: "Golden and anti-examples for type def construction, demonstrating ideal structure and common pitfalls."
domain: "type def construction"
density_score: 0.90
related:
  - tools_prompt_template_builder
  - bld_tools_voice_pipeline
  - bld_tools_naming_rule
  - bld_tools_optimizer
  - bld_tools_component_map
  - bld_tools_collaboration_pattern
  - bld_tools_context_doc
  - bld_tools_action_paradigm
  - bld_tools_validation_schema
  - bld_tools_dispatch_rule
---

## Production Tools
| Tool | Status | Tag | Purpose |
|---|---|---|---|
| `brain_query` | CONDITIONAL | [MCP] | Surface existing type_def artifacts, related schemas, domain context |
| `validate_artifact` | CONDITIONAL | [PLANNED] | Run SCHEMA.md hard gates against produced artifact |
| `cex_forge` | CONDITIONAL | [PLANNED] | Register type_def into CEX artifact registry |
| `glob` | ACTIVE | [LOCAL] | Find existing type_def files under `archetypes/` for collision check |
| `read` | ACTIVE | [LOCAL] | Read sibling type_def artifacts to check inheritance targets |
## Data Sources
| Source | What to Extract |
|---|---|
| `P06_schema/_schema.yaml` | max_bytes, naming pattern, llm_function for type_def |
| `archetypes/builders/*/SCHEMA.md` | Sibling schemas to verify no kind collision |
| Brain index (via `brain_query`) | Existing type_defs by domain, related constraints |
| Domain KNOWLEDGE.md files | Base type vocabulary for the target domain |
## brain_query Usage [IF MCP]
```
brain_query "type_def {type_name}"          # Find existing definitions for this type
brain_query "base_type constraints {domain}" # Find constraint patterns in domain
brain_query "composition union {type_name}"  # Find union/intersection patterns
```
Always run before composing — prevents duplicate type_def creation.
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation Checklist
Run these checks before finalizing output (no tool required):
- [ ] `id` matches `^p06_td_[a-z][a-z0-9_]*$`
- [ ] `kind: type_def` present
- [ ] `pillar: P06` present
- [ ] `base_type` is non-null and from controlled vocabulary
- [ ] `constraints` is a structured object (not free text)
- [ ] `quality: null` on draft
- [ ] Artifact byte count <= 3072
- [ ] At least one example in body
- [ ] `tldr` is a single sentence

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tools_prompt_template_builder]] | sibling | 0.42 |
| [[bld_tools_voice_pipeline]] | sibling | 0.41 |
| [[bld_tools_naming_rule]] | sibling | 0.40 |
| [[bld_tools_optimizer]] | sibling | 0.40 |
| [[bld_tools_component_map]] | sibling | 0.40 |
| [[bld_tools_collaboration_pattern]] | sibling | 0.39 |
| [[bld_tools_context_doc]] | sibling | 0.39 |
| [[bld_tools_action_paradigm]] | sibling | 0.39 |
| [[bld_tools_validation_schema]] | sibling | 0.39 |
| [[bld_tools_dispatch_rule]] | sibling | 0.38 |
