---
quality: 7.6
quality: 7.5
id: bld_tools_domain_event
kind: knowledge_card
pillar: P12
title: "Domain Event Builder -- Tools"
version: 1.0.0
llm_function: CALL
tags: [builder, domain_event, tools]
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_tools_kind
  - skill
  - bld_architecture_kind
  - validate
  - kind-builder
  - bld_tools_model_architecture
  - bld_collaboration_kind
  - p03_sp_n03_creation_nucleus
  - bld_tools_builder
  - bld_tools_knowledge_graph
---

# Domain Event Builder -- Tools

Builder domain: event-driven architecture. Primary nucleus: N03.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar domain_event artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_domain_event.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `domain_event`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/domain-event-builder/bld_examples_domain_event.md` | Reference examples | F3 INJECT |
| `archetypes/builders/domain-event-builder/bld_schema_domain_event.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing domain_event artifacts
python _tools/cex_retriever.py --query "Immutable record of a significant domain occurrence"

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
| [[bld_tools_kind]] | upstream | 0.38 |
| [[skill]] | upstream | 0.30 |
| [[bld_architecture_kind]] | upstream | 0.29 |
| [[validate]] | upstream | 0.29 |
| [[kind-builder]] | upstream | 0.28 |
| [[bld_tools_model_architecture]] | upstream | 0.27 |
| [[bld_collaboration_kind]] | related | 0.27 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.25 |
| [[bld_tools_builder]] | upstream | 0.24 |
| [[bld_tools_knowledge_graph]] | upstream | 0.24 |
