---
kind: tools
id: bld_tools_reranker_config
pillar: P04
llm_function: CALL
purpose: Tools available for reranker_config production
quality: 8.9
title: "Tools Reranker Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [reranker_config, builder, tools]
tldr: "Tools available for reranker_config production"
domain: "reranker_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile reranker_config artifact to .yaml | After authoring |
| cex_score.py | Peer-review score via 5D rubric | After compile |
| cex_retriever.py | Find similar existing reranker_config artifacts | During F3 INJECT |
| cex_doctor.py | Validate builder ISO health | Pre-dispatch |
| cex_wave_validator.py | Validate all ISOs in builder directory | Post-build |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_hooks.py | Pre-commit quality gate enforcement | Before git commit |
| cex_sanitize.py | Check ASCII compliance in code files | Pre-commit |
| cex_hygiene.py | Artifact CRUD rules (frontmatter, naming) | Periodic cleanup |

## External References
- Cohere Rerank v3 (cross-encoder reranking API)
- BGE reranker (BAAI/bge-reranker-large via HuggingFace)
- ColBERT v2 (late-interaction neural ranking, Stanford NLP)
- ms-marco cross-encoders (ms-marco-MiniLM-L-6-v2, msmarco-distilbert)
- RankGPT (GPT-4 listwise reranking, Sun et al. 2023)
- FAISS (vector similarity search, Facebook AI)
