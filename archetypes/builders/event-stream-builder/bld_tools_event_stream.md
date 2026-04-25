---
quality: 7.6
quality: 7.5
id: bld_tools_event_stream
kind: knowledge_card
pillar: P04
title: "Event Stream Builder -- Tools"
version: 1.0.0
llm_function: CALL
tags: [builder, event_stream, tools]
author: builder
tldr: "Event Stream tools: tool integrations, CLI commands, and external capabilities"
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_tools_kind
  - skill
  - validate
  - bld_architecture_kind
  - kind-builder
  - bld_collaboration_kind
  - bld_tools_model_architecture
  - bld_tools_builder
  - p03_sp_n03_creation_nucleus
  - p11_qg_knowledge
---

# Event Stream Builder -- Tools

Builder domain: streaming infrastructure. Primary nucleus: N05.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar event_stream artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_event_stream.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `event_stream`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/event-stream-builder/bld_examples_event_stream.md` | Reference examples | F3 INJECT |
| `archetypes/builders/event-stream-builder/bld_schema_event_stream.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing event_stream artifacts
python _tools/cex_retriever.py --query "Real-time ordered event sequence configuration"

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
| [[bld_tools_kind]] | related | 0.39 |
| [[skill]] | downstream | 0.31 |
| [[validate]] | downstream | 0.29 |
| [[bld_architecture_kind]] | downstream | 0.29 |
| [[kind-builder]] | downstream | 0.29 |
| [[bld_collaboration_kind]] | downstream | 0.27 |
| [[bld_tools_model_architecture]] | related | 0.27 |
| [[bld_tools_builder]] | related | 0.26 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.25 |
| [[p11_qg_knowledge]] | downstream | 0.25 |
