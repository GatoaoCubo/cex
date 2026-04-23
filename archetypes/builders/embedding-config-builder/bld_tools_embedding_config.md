---
kind: tools
id: bld_tools_embedding_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for embedding_config production
quality: 9.0
title: "Tools Embedding Config"
version: "1.0.0"
author: n03_builder
tags: [embedding_config, builder, examples]
tldr: "Golden and anti-examples for embedding config construction, demonstrating ideal structure and common pitfalls."
domain: "embedding config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_retriever_config
  - bld_tools_function_def
  - bld_tools_input_schema
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_validator
  - bld_tools_chunk_strategy
  - bld_tools_path_config
  - bld_tools_prompt_version
  - bld_tools_output_validator
---

# Tools: embedding-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing embedding_configs in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P01_knowledge/_schema.yaml | Field definitions for embedding_config |
| CEX Examples | P01_knowledge/examples/ | Real embedding_config artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P01_embedding_config seeds |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| MTEB Leaderboard | huggingface.co/spaces/mteb/leaderboard | Model quality comparison |
| Ollama Library | ollama.com/library | Local model specs |
| OpenAI Embeddings | platform.openai.com/docs/guides/embeddings | API model specs |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet for embedding_configs.
Manually check each QUALITY_GATES.md gate against produced artifact:
- [ ] YAML parses without error
- [ ] id matches p01_emb_ prefix
- [ ] dimensions is positive integer
- [ ] chunk_size is positive integer
- [ ] quality is null
- [ ] model_name is specific identifier

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_retriever_config]] | sibling | 0.63 |
| [[bld_tools_function_def]] | sibling | 0.60 |
| [[bld_tools_input_schema]] | sibling | 0.60 |
| [[bld_tools_memory_scope]] | sibling | 0.59 |
| [[bld_tools_cli_tool]] | sibling | 0.59 |
| [[bld_tools_validator]] | sibling | 0.59 |
| [[bld_tools_chunk_strategy]] | sibling | 0.59 |
| [[bld_tools_path_config]] | sibling | 0.58 |
| [[bld_tools_prompt_version]] | sibling | 0.58 |
| [[bld_tools_output_validator]] | sibling | 0.58 |
