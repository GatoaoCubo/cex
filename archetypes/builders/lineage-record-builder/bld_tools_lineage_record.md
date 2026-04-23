---
quality: 7.6
quality: 7.5
id: bld_tools_lineage_record
kind: knowledge_card
pillar: P01
title: "Lineage Record Builder -- Tools"
version: 1.0.0
llm_function: CALL
tags: [builder, lineage_record, tools]
author: builder
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
  - bld_tools_knowledge_graph
  - bld_tools_builder
  - p03_sp_n03_creation_nucleus
---

# Lineage Record Builder -- Tools

Builder domain: data lineage. Primary nucleus: N04.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar lineage_record artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_lineage_record.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `lineage_record`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/lineage-record-builder/bld_examples_lineage_record.md` | Reference examples | F3 INJECT |
| `archetypes/builders/lineage-record-builder/bld_schema_lineage_record.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing lineage_record artifacts
python _tools/cex_retriever.py --query "Provenance chain of a knowledge artifact derivation"

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
| [[bld_tools_kind]] | downstream | 0.39 |
| [[skill]] | downstream | 0.31 |
| [[validate]] | downstream | 0.29 |
| [[bld_architecture_kind]] | downstream | 0.29 |
| [[kind-builder]] | downstream | 0.29 |
| [[bld_collaboration_kind]] | downstream | 0.27 |
| [[bld_tools_model_architecture]] | downstream | 0.26 |
| [[bld_tools_knowledge_graph]] | downstream | 0.25 |
| [[bld_tools_builder]] | downstream | 0.25 |
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.25 |
