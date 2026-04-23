---
kind: tools
id: bld_tools_agentic_rag
pillar: P04
llm_function: CALL
purpose: Tools available for agentic_rag production
quality: 8.9
title: "Tools Agentic Rag"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [agentic_rag, builder, tools]
tldr: "Tools available for agentic_rag production"
domain: "agentic_rag construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_agentic_rag
  - bld_tools_graph_rag_config
  - bld_tools_reranker_config
  - bld_tools_rbac_policy
  - bld_tools_usage_quota
  - bld_instruction_agentic_rag
  - bld_tools_github_issue_template
  - bld_tools_playground_config
  - bld_tools_integration_guide
  - bld_tools_white_label_config
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile agentic_rag artifact to .yaml | After authoring |
| cex_score.py | Peer-review score via 5D rubric | After compile |
| cex_retriever.py | Find similar existing agentic_rag artifacts | During F3 INJECT |
| cex_doctor.py | Validate builder ISO health | Pre-dispatch |
| cex_wave_validator.py | Validate all ISOs in builder directory | Post-build |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_hooks.py | Pre-commit quality gate enforcement | Before git commit |
| cex_sanitize.py | Check ASCII compliance in code files | Pre-commit |
| cex_hygiene.py | Artifact CRUD rules (frontmatter, naming) | Periodic cleanup |

## External References
- Self-RAG (Asai et al. 2023: self-reflection tokens for retrieval decisions)
- CRAG -- Corrective RAG (Yan et al. 2024: retrieval evaluator + web search fallback)
- RAG-Fusion (Rackauckas 2024: multi-query generation + RRF reranking)
- Adaptive RAG (Jeong et al. 2024: query complexity classifier)
- LangGraph agentic RAG (retrieve->grade->re-query loop via StateGraph)
- LlamaIndex AgentRunner (tool-calling + retrieval planning)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_agentic_rag]] | upstream | 0.50 |
| [[bld_tools_graph_rag_config]] | sibling | 0.40 |
| [[bld_tools_reranker_config]] | sibling | 0.37 |
| [[bld_tools_rbac_policy]] | sibling | 0.36 |
| [[bld_tools_usage_quota]] | sibling | 0.35 |
| [[bld_instruction_agentic_rag]] | upstream | 0.35 |
| [[bld_tools_github_issue_template]] | sibling | 0.34 |
| [[bld_tools_playground_config]] | sibling | 0.34 |
| [[bld_tools_integration_guide]] | sibling | 0.33 |
| [[bld_tools_white_label_config]] | sibling | 0.33 |
