---
id: bld_tools_domain_vocabulary
kind: knowledge_card
pillar: P01
title: "Domain Vocabulary Builder -- Tools"
version: 1.0.0
quality: 6.5
llm_function: CALL
tags: [builder, domain_vocabulary, tools]
density_score: 1.0
updated: "2026-04-17"
---

# Domain Vocabulary Builder -- Tools

Builder domain: ubiquitous language. Primary nucleus: N04.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar domain_vocabulary artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_domain_vocabulary.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `domain_vocabulary`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/domain-vocabulary-builder/bld_examples_domain_vocabulary.md` | Reference examples | F3 INJECT |
| `archetypes/builders/domain-vocabulary-builder/bld_schema_domain_vocabulary.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing domain_vocabulary artifacts
python _tools/cex_retriever.py --query "Governed canonical term registry for a bounded context"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```
