---
id: p11_tools_revision_loop_policy
kind: toolkit
pillar: P04
llm_function: CALL
purpose: P04 tools available to the revision-loop-policy-builder
quality: 8.1
title: "Tools: Revision Loop Policy Builder"
version: "1.0.0"
author: n03_hermes_w1_6
tags: [tools, revision_loop_policy, builder, p04, p11]
domain: "revision_loop_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.86
related:
  - bld_tools_kind
  - bld_tools_model_architecture
  - bld_tools_training_method
  - p11_qg_knowledge
  - p11_qg_artifact
  - bld_tools_hitl_config
  - bld_tools_knowledge_graph
  - bld_tools_validation_schema
  - kind-builder
  - bld_tools_builder
---

## Available Tools (F5 CALL)

### Core Build Tools

| Tool | Command | Purpose |
|------|---------|---------|
| Compile | `python _tools/cex_compile.py {path}` | Convert .md -> .yaml |
| Doctor | `python _tools/cex_doctor.py` | Health check all artifacts |
| Sanitize | `python _tools/cex_sanitize.py --check` | Verify ASCII compliance |
| Score | `python _tools/cex_score.py --apply {path}` | Peer-review scoring |

### Validation Tools

| Tool | Command | Purpose |
|------|---------|---------|
| JSON validate | `python -m json.tool .cex/kinds_meta.json` | Verify kinds_meta is valid JSON |
| YAML validate | `python -c "import yaml; yaml.safe_load(open('{path}'))"` | Verify frontmatter parses |

### Discovery Tools

| Tool | Command | Purpose |
|------|---------|---------|
| Query | `python _tools/cex_query.py revision_loop_policy` | Find similar artifacts |
| Retriever | `python _tools/cex_retriever.py "revision loop"` | TF-IDF similarity search |
| Kind meta | `python -c "import json; d=json.load(open('.cex/kinds_meta.json')); print(d.get('revision_loop_policy'))"` | Check kind registration |

### Reference Files (read before building)

| File | Purpose |
|------|---------|
| `archetypes/builders/revision-loop-policy-builder/bld_schema_revision_loop_policy.md` | HARD gates + schema |
| `N00_genesis/P11_feedback/tpl_revision_loop_policy.md` | Canonical template |
| `N00_genesis/P01_knowledge/library/kind/kc_revision_loop_policy.md` | Domain KC |
| `archetypes/builders/revision-loop-policy-builder/bld_examples_revision_loop_policy.md` | 3 golden + 3 anti-examples |

### File Operations

| Operation | Tool |
|-----------|------|
| Read files | Read (not cat) |
| Write new artifact | Write |
| Edit existing | Edit |
| Find similar | Glob + Grep |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_kind]] | related | 0.40 |
| [[bld_tools_model_architecture]] | related | 0.33 |
| [[bld_tools_training_method]] | related | 0.31 |
| [[p11_qg_knowledge]] | downstream | 0.30 |
| [[p11_qg_artifact]] | downstream | 0.30 |
| [[bld_tools_hitl_config]] | related | 0.30 |
| [[bld_tools_knowledge_graph]] | related | 0.29 |
| [[bld_tools_validation_schema]] | related | 0.28 |
| [[kind-builder]] | downstream | 0.28 |
| [[bld_tools_builder]] | related | 0.26 |
