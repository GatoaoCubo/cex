---
id: p01_kc_aws_bedrock_patterns
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: 'AWS Bedrock Patterns: Agents, Knowledge Bases, Guardrails, Orchestration'
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: aws_bedrock
origin: src_provider_taxonomy
quality: 9.1
tags:
- aws
- bedrock
- agents
- knowledge-bases
- guardrails
- rag
- knowledge
tldr: AWS Bedrock patterns covering agents (action_groups + orchestration), knowledge bases (RAG + vector stores + chunking),
  guardrails (safety), and managed memory/sessions.
when_to_use: When building with AWS Bedrock agents, implementing RAG knowledge bases, or comparing AWS orchestration patterns
  vs MCP/Anthropic.
keywords:
- bedrock
- agents
- knowledge_bases
- guardrails
- rag
- orchestration
long_tails:
- aws bedrock agent action group knowledge base orchestration
- bedrock knowledge base chunking strategy vector store rag
axioms:
- Bedrock agents are server-managed (orchestration on AWS); Anthropic agentic loop is client-managed
feeds_kinds:
- agent
- knowledge_card
- guardrail
- function_def
- retriever_config
- env_config
linked_artifacts:
  adw: null
  agent: null
  hop: null
density_score: 0.87
related:
  - atom_03_openai_agents_sdk
  - agent_card_n04
  - cex_llm_vocabulary_whitepaper
  - n04_kc_knowledge_management
  - bld_collaboration_agent
  - atom_07_llamaindex
  - p01_kc_agent
  - p01_kc_terminology_rosetta_stone
  - p03_sp_agentic_rag_builder
  - bld_instruction_agentic_rag
---

# KC-Domain: AWS Bedrock Patterns

## Quick Reference
```yaml
topic: AWS Bedrock (docs.aws.amazon.com)
scope: Agents, knowledge bases, guardrails, orchestration
owner: builder_agent
criticality: medium
```

## Agents

| Term | Role | Key Detail |
|------|------|------------|
| `agent` | Core entity | Autonomous system orchestrating FMs, data sources, apps, and conversations |
| `action_group` | Component | Defines actions an agent can perform; maps to an API schema (OpenAPI) |
| `knowledge_base` | Component | Database of private data queried for augmented responses |
| `agent_alias` | Deployment | Pointer to specific agent version for production API calls |
| `foundation_model` (FM) | Core entity | Underlying LLM the agent orchestrates |
| `orchestration` | Process | FM coordinates interactions between all components |
| `trace` | Monitoring | Step-by-step reasoning record for troubleshooting |
| `memory` | Capability | Managed by Bedrock; maintains context across sessions |
| `guardrail` | Safety | Policy layer filtering harmful content + enforcing topic boundaries |
| `session` | Context | Conversation container for a single agent interaction |

**Architecture**: Agent = FM + action_groups + knowledge_bases + guardrails + memory. The FM does the orchestration (decides which action_group to call, when to query knowledge_base).

## Knowledge Bases (RAG)

| Term | Role | Key Detail |
|------|------|------------|
| `knowledge_base` | Resource | Integrates proprietary info into generative AI apps |
| `data_source` | Component | Underlying repository (unstructured or structured) |
| `vector_store` | Storage | Indexes embeddings; auto-created (OpenSearch Serverless) or user-managed |
| `embedding_model` | Component | Converts text to vectors for semantic search |
| `chunking_strategy` | Config | How documents split during ingestion (fixed, semantic, hierarchical) |
| `ingestion_job` | Operation | Processes data source documents into vector store |
| `sync` | Operation | Updates knowledge base index from data source |
| `retrieval` | Process | Searches data sources for relevant information |
| `RAG` | Technique | Retrieval Augmented Generation -- improves FM accuracy with real data |

**Pipeline**: Data source -> ingestion_job (chunking + embedding) -> vector_store -> retrieval query -> FM augmented response.

## Cross-Provider Alignment

| Concept | AWS Bedrock | Anthropic | MCP |
|---------|-------------|-----------|-----|
| Tool def | `action_group` (OpenAPI schema) | `tool` (input_schema) | `tool` (inputSchema) |
| Orchestration | Server-managed (FM orchestrates) | Client-managed (agentic loop) | Client-managed (MCP Host) |
| Knowledge | `knowledge_base` + RAG | No native (use MCP resources) | `resource` primitive |
| Safety | `guardrail` (managed) | System prompt instructions | No native |
| Memory | Managed `memory` (cross-session) | `cache_control` (ephemeral) | Stateful session |
| Conversation | `session` | Messages array | MCP session |

## Golden Rules
- Bedrock agents are fully server-managed -- you don't implement the orchestration loop
- Action groups require OpenAPI schema (not JSON Schema like tool definitions)
- Knowledge base vector stores can be auto-created (OpenSearch Serverless) but cost scales with data
- Guardrails are applied at the agent level, not per-tool
- `agent_alias` is required for production -- never call agent versions directly
- Trace logs are essential for debugging orchestration decisions

## Flow
```text
[User query] -> [Agent receives] -> [FM orchestrates] -> [action_group API call OR knowledge_base retrieval] -> [Guardrail filter] -> [Response]
```

## References
- Origin: src_provider_taxonomy.md (Provider Official Taxonomy)
- Agents: /bedrock/latest/userguide/agents.html
- Knowledge Bases: /bedrock/latest/userguide/knowledge-base.html

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[atom_03_openai_agents_sdk]] | sibling | 0.27 |
| [[agent_card_n04]] | related | 0.26 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.25 |
| [[n04_kc_knowledge_management]] | sibling | 0.24 |
| [[bld_collaboration_agent]] | downstream | 0.23 |
| [[atom_07_llamaindex]] | sibling | 0.23 |
| [[p01_kc_agent]] | sibling | 0.23 |
| [[p01_kc_terminology_rosetta_stone]] | sibling | 0.23 |
| [[p03_sp_agentic_rag_builder]] | downstream | 0.23 |
| [[bld_instruction_agentic_rag]] | downstream | 0.22 |
