---
id: bld_tools_deployment_manifest
kind: knowledge_card
pillar: P09
title: "Deployment Manifest Builder -- Tools"
version: 1.0.0
quality: 6.5
llm_function: CALL
tags: [builder, deployment_manifest, tools]
density_score: 1.0
updated: "2026-04-17"
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
