---
id: bld_tools_tagline
kind: tools
pillar: P04
builder: tagline-builder
version: 1.0.0
quality: 9.0
title: "Tools Tagline"
author: n03_builder
tags: [tagline, builder, examples]
tldr: "Golden and anti-examples for tagline construction, demonstrating ideal structure and common pitfalls."
domain: "tagline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: CALL
related:
  - bld_memory_tagline
  - bld_collaboration_tagline
  - bld_architecture_tagline
  - bld_tools_landing_page
  - bld_config_tagline
  - tagline-builder
  - bld_instruction_tagline
  - bld_quality_gate_tagline
  - bld_schema_tagline
  - bld_system_prompt_tagline
---
# Tools: Tagline Builder

## Required Tools
1. `brand_config_reader`: Read .cex/brand/brand_config.yaml for brand context
2. `cex_query.py`: Find competitor builders and existing brand artifacts
3. `cex_retriever.py`: Search existing taglines in the knowledge base

## Optional Tools
1. `browser_web_scraping`: Scrape competitor websites for their taglines
2. `cex_memory_select.py`: Recall previous tagline decisions and preferences

## No External Dependencies
Tagline creation is pure LLM reasoning -- no APIs, no code execution.
All tools are for context gathering, not generation.

## Tool Permissions
1. READ: brand config, existing artifacts, competitor taglines, memory records
2. WRITE: output files only (tagline YAML + compiled artifacts)
3. EXECUTE: none (pure reasoning, no code execution)
4. DENY: no database writes, no API calls, no deployment actions

## Metadata

```yaml
id: bld_tools_tagline
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-tagline.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `tools` |
| Pillar | P04 |
| Domain | tagline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_tagline]] | downstream | 0.45 |
| [[bld_collaboration_tagline]] | downstream | 0.43 |
| [[bld_architecture_tagline]] | downstream | 0.40 |
| [[bld_tools_landing_page]] | sibling | 0.38 |
| [[bld_config_tagline]] | downstream | 0.37 |
| [[tagline-builder]] | upstream | 0.36 |
| [[bld_instruction_tagline]] | upstream | 0.34 |
| [[bld_quality_gate_tagline]] | downstream | 0.33 |
| [[bld_schema_tagline]] | downstream | 0.33 |
| [[bld_system_prompt_tagline]] | upstream | 0.32 |
