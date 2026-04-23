---
kind: tools
id: bld_tools_knowledge_card
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for knowledge_card production
quality: 9.1
title: "Tools Knowledge Card"
version: "1.0.0"
author: n03_builder
tags: [knowledge_card, builder, examples]
tldr: "Golden and anti-examples for knowledge card construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_validation_schema
  - bld_tools_retriever_config
  - bld_tools_quality_gate
  - bld_tools_scoring_rubric
  - bld_tools_chunk_strategy
  - bld_tools_golden_test
  - bld_tools_path_config
  - bld_tools_memory_scope
  - bld_tools_validator
  - bld_tools_cli_tool
---

# Tools: knowledge-card-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| validate_kc.py | Validate KC: 10 HARD + 20 SOFT gates | Phase 3 | CONDITIONAL |
| brain_query [MCP] | Search existing KCs in pool | Phase 1 | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | — | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alt compose | [PLANNED] |
## validate_kc.py Usage
```bash
# Single file
python _tools/validate_kc.py path/to/p01_kc_topic.md
# Directory (batch)
python _tools/validate_kc.py P01_knowledge/examples/ --summary
# JSON output (machine-readable)
python _tools/validate_kc.py path/to/file.md --json
```
Output: HARD pass/fail + SOFT score 0-10 + verdict.
Fix suggestions provided for failed gates.
## brain_query Usage
```python
brain_query("knowledge card about {topic}")
# Returns: existing KCs matching topic
# Purpose: avoid duplicates, find linked_artifacts
```
## Data Sources
| Source | Path | Data |
|--------|------|------|
| CEX Schema | P01_knowledge/_schema.yaml | KC field definitions |
| CEX Examples | P01_knowledge/examples/ | 63+ real KCs |
| CEX Template | P01_knowledge/templates/tpl_knowledge_card.md | Fillable template |
| CEX Pool | records/pool/ (source repository) | 1957+ published artifacts |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
validate_kc.py is ACTIVE — always run before committing.
No manual gate-checking needed (unlike model-card-builder).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_validation_schema]] | sibling | 0.53 |
| [[bld_tools_retriever_config]] | sibling | 0.48 |
| [[bld_tools_quality_gate]] | sibling | 0.47 |
| [[bld_tools_scoring_rubric]] | sibling | 0.46 |
| [[bld_tools_chunk_strategy]] | sibling | 0.45 |
| [[bld_tools_golden_test]] | sibling | 0.45 |
| [[bld_tools_path_config]] | sibling | 0.44 |
| [[bld_tools_memory_scope]] | sibling | 0.43 |
| [[bld_tools_validator]] | sibling | 0.43 |
| [[bld_tools_cli_tool]] | sibling | 0.43 |
