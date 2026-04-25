---
quality: 7.6
quality: 7.5
id: bld_tools_value_object
kind: knowledge_card
pillar: P06
title: "Value Object Builder -- Tools"
version: 1.0.0
llm_function: CALL
tags: [builder, value_object, tools]
author: builder
tldr: "Value Object schema: tool integrations, CLI commands, and external capabilities"
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_tools_kind
  - skill
  - validate
  - kind-builder
  - bld_architecture_kind
  - bld_collaboration_kind
  - bld_tools_model_architecture
  - p03_sp_n03_creation_nucleus
  - bld_tools_builder
  - doctor
---

# Value Object Builder -- Tools

Builder domain: domain model type. Primary nucleus: N03.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar value_object artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_value_object.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `value_object`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/value-object-builder/bld_examples_value_object.md` | Reference examples | F3 INJECT |
| `archetypes/builders/value-object-builder/bld_schema_value_object.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing value_object artifacts
python _tools/cex_retriever.py --query "Immutable typed value defined by attributes alone"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```

## Tool Integration Checklist

- Verify tool name follows snake_case convention
- Validate input/output schema matches interface contract
- Cross-reference with capability_registry for discoverability
- Test tool invocation in sandbox before production use

## Invocation Pattern

```yaml
# Tool invocation contract
name: tool_name
input_schema: validated
output_schema: validated
error_handling: defined
timeout: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_kind]] | upstream | 0.39 |
| [[skill]] | downstream | 0.32 |
| [[validate]] | downstream | 0.30 |
| [[kind-builder]] | downstream | 0.29 |
| [[bld_architecture_kind]] | downstream | 0.29 |
| [[bld_collaboration_kind]] | downstream | 0.27 |
| [[bld_tools_model_architecture]] | upstream | 0.27 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.26 |
| [[bld_tools_builder]] | upstream | 0.25 |
| [[doctor]] | downstream | 0.25 |
