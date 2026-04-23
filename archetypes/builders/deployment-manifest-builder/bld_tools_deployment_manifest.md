---
quality: 7.6
quality: 7.5
id: bld_tools_deployment_manifest
kind: knowledge_card
pillar: P09
title: "Deployment Manifest Builder -- Tools"
version: 1.0.0
llm_function: CALL
tags: [builder, deployment_manifest, tools]
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_tools_kind
  - skill
  - bld_architecture_kind
  - kind-builder
  - validate
  - bld_collaboration_kind
  - p03_sp_n03_creation_nucleus
  - bld_tools_model_architecture
  - p11_qg_knowledge
  - bld_tools_builder
---

# Deployment Manifest Builder -- Tools

Builder domain: release management. Primary nucleus: N05.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar deployment_manifest artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_deployment_manifest.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `deployment_manifest`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/deployment-manifest-builder/bld_examples_deployment_manifest.md` | Reference examples | F3 INJECT |
| `archetypes/builders/deployment-manifest-builder/bld_schema_deployment_manifest.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing deployment_manifest artifacts
python _tools/cex_retriever.py --query "Artifact deploy specification for an environment"

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
| [[skill]] | upstream | 0.32 |
| [[bld_architecture_kind]] | upstream | 0.30 |
| [[kind-builder]] | upstream | 0.30 |
| [[validate]] | upstream | 0.29 |
| [[bld_collaboration_kind]] | downstream | 0.27 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.27 |
| [[bld_tools_model_architecture]] | upstream | 0.27 |
| [[p11_qg_knowledge]] | downstream | 0.26 |
| [[bld_tools_builder]] | upstream | 0.26 |
