---
kind: tools
id: bld_tools_retriever
pillar: P08
llm_function: CALL
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.0
tags: [tools, retriever, P08, RAG, vector-search]
density_score: 1.0
title: Tools ISO - retriever
related:
  - bld_instruction_retriever
  - tools_prompt_template_builder
  - bld_tools_retriever_config
  - p11_qg_retriever
  - bld_tools_quality_gate
  - bld_tools_voice_pipeline
  - bld_tools_golden_test
  - bld_tools_notifier
  - bld_tools_validation_schema
  - bld_tools_action_paradigm
---
# Tools: retriever-builder

## Production Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| brain_query("retriever {store_type}") | Find existing retriever artifacts and patterns | Before creating — check for duplicates |
| brain_query("embedding model {use_case}") | Discover embedding model recommendations | When model not specified by user |
| validate_artifact.py | Run HARD gate checks against schema | After composing, before delivery |
| cex_forge.py | Scaffold artifact from template | When starting from scratch |
| glob("p04_retr_*.md") | List all existing retriever artifacts | Dedup check |
| grep("store_type: {type}") | Find retrievers using a specific backend | Pattern reference |

## Data Sources

| Source | Content | Usage |
|--------|---------|-------|
| bld_schema_retriever.md | Field definitions, enums, constraints | REQUIRED — read before composing |
| bld_output_template_retriever.md | Fillable template | REQUIRED — fill `{{vars}}` |
| bld_quality_gate_retriever.md | HARD + SOFT gate definitions | REQUIRED — validate before deliver |
| bld_knowledge_card_retriever.md | Domain patterns, metric guide, store comparison | Reference for recommendations |
| bld_examples_retriever.md | Golden + anti-example with gate annotations | Reference when uncertain |
| records/pool/ (p04_retr_*.md) | Existing production artifacts | Dedup + pattern mining |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation (manual gate checks without tooling)

```
H01: paste frontmatter into yaml.org/parser — should parse cleanly
H02: confirm id starts with p04_retr_ and matches filename stem
H03: kind field == "retriever" (exact, lowercase)
H04: quality field == null (not a number, not missing)
H05: check required fields: id, name, store_type, embedding_model, similarity_metric, top_k
H06: store_type in [chroma, pinecone, faiss, qdrant, weaviate, milvus, elasticsearch, costm]
H07: embedding_model is non-empty string with provider identifiable
H08: similarity_metric in [cosine, dot_product, euclidean, manhattan]
H09: top_k is integer >= 1
H10: wc -c body_only.md <= 2048
```

## Tool Invocation Order
1. brain_query — dedup + context
2. bld_schema_retriever.md — read constraints
3. bld_output_template_retriever.md — fill template
4. bld_quality_gate_retriever.md — validate
5. validate_artifact.py — automated gate run
6. Deliver if all HARD pass and score >= 7.0

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_retriever]] | upstream | 0.40 |
| [[tools_prompt_template_builder]] | sibling | 0.38 |
| [[bld_tools_retriever_config]] | sibling | 0.37 |
| [[p11_qg_retriever]] | downstream | 0.37 |
| [[bld_tools_quality_gate]] | sibling | 0.37 |
| [[bld_tools_voice_pipeline]] | sibling | 0.36 |
| [[bld_tools_golden_test]] | sibling | 0.35 |
| [[bld_tools_notifier]] | sibling | 0.35 |
| [[bld_tools_validation_schema]] | sibling | 0.34 |
| [[bld_tools_action_paradigm]] | sibling | 0.34 |
