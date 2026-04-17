---
kind: output_template
id: bld_output_template_memory_architecture
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for memory_architecture production
quality: 9.2
title: "Output Template: memory_architecture"
version: "2.0.0"
author: n06_commercial
tags: [memory_architecture, builder, output_template]
tldr: "Template for LLM agent memory architecture artifacts: layer table, storage backends, pipelines, tier matrix"
domain: "LLM agent memory systems"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

```yaml
---
id: p10_marc_{{agent_slug}}
kind: memory_architecture
pillar: P10
title: "Memory Architecture: {{agent_name}}"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{agent_domain}}"
quality: null
tags: [memory_architecture, {{agent_slug}}, {{tier}}]
tldr: "{{one_sentence_summary}}"
layers: [{{active_layers}}]
tier: "{{tier}}"
system_ref: "{{reference_system}}"
retention_days: {{episodic_retention_days}}
consolidation_enabled: {{true_or_false}}
---
```

<!-- id: Unique identifier following ^p10_marc_[a-z][a-z0-9_]+ -->
<!-- agent_slug: snake_case agent name (e.g., customer_support_v2) -->
<!-- agent_name: Human-readable name (e.g., "Customer Support Agent v2") -->
<!-- active_layers: subset of [working, episodic, semantic, procedural] -->
<!-- tier: free | pro | enterprise -->
<!-- reference_system: memgpt | zep | mem0 | cognee | langmem | custom -->
<!-- episodic_retention_days: integer, or null if no episodic layer -->

## Overview

{{agent_name}} memory architecture for {{agent_domain}}. Active layers: {{active_layers}}.
Commercial tier: {{tier}}. Reference design: {{reference_system}}.

## Memory Layer Definitions

| Layer | Backend | Retention | Tier Required | Notes |
|-------|---------|-----------|---------------|-------|
| Working | In-context ({{context_window_size}} tokens) | Session only | Free | Always active |
| Episodic | {{episodic_backend}} | {{episodic_retention_days}} days | Pro | {{episodic_notes}} |
| Semantic | {{semantic_backend}} | Persistent | Pro | {{semantic_notes}} |
| Procedural | {{procedural_backend}} | Persistent | Pro | {{procedural_notes}} |

<!-- Remove rows for inactive layers. Add justification note in Overview if excluded. -->

## Storage Backends

### Working Memory
- Type: In-context (native LLM context window)
- Capacity: {{context_window_size}} tokens
- Management: {{context_management_strategy}} (e.g., sliding window, summarization)

### Episodic Memory
- Backend: {{episodic_backend}} (e.g., pgvector, Pinecone, Weaviate)
- Embedding model: {{embedding_model}}
- Retrieval: semantic search, top-{{episodic_top_k}} results
- TTL: {{episodic_retention_days}} days

### Semantic Memory
- Backend: {{semantic_backend}} (e.g., Neo4j, ArangoDB, Redis JSON)
- Schema: entity-relation triples with temporal metadata
- Retrieval: entity lookup + graph traversal

### Procedural Memory
- Backend: {{procedural_backend}} (e.g., Redis KV, PostgreSQL, filesystem)
- Format: versioned skill definitions (YAML/JSON)
- Retrieval: exact key match + fuzzy name search

## Read Pipeline

1. Parse query intent and extract memory retrieval signals.
2. Query episodic memory: semantic search over recent interactions.
3. Query semantic memory: entity lookups for referenced entities.
4. Query procedural memory: skill lookup if task matches known procedure.
5. Rank results by: recency (0.4) + relevance (0.4) + importance (0.2).
6. Inject top-{{total_top_k}} memories into system prompt under `## Context` section.

## Write Pipeline

1. After generation, extract memory-worthy content via LLM extraction prompt.
2. Classify extracted content: fact (-> semantic), event (-> episodic), skill (-> procedural).
3. Deduplicate against existing memories (embedding similarity > 0.92 = merge).
4. Write to appropriate backend with timestamp and importance score.
5. Append to episodic log with session ID.
6. Trigger consolidation if episodic buffer > {{consolidation_threshold}} entries.

## Eviction Policy

| Layer | Strategy | Trigger | Action |
|-------|----------|---------|--------|
| Working | FIFO + summarization | Token budget > 80% | Summarize oldest 20% |
| Episodic | TTL + importance | Age > {{episodic_retention_days}}d OR importance < 0.3 | Archive or delete |
| Semantic | LRU + staleness | Last accessed > 180d AND no entity links | Soft-delete + audit log |
| Procedural | Version-based | New version > old | Archive old, activate new |

## Commercial Tier Matrix

| Feature | Free | Pro | Enterprise |
|---------|------|-----|------------|
| Working memory | {{free_context_tokens}} tokens | {{pro_context_tokens}} tokens | {{enterprise_context_tokens}} tokens |
| Episodic memory | None | Last {{pro_episodic_sessions}} sessions | Unlimited + searchable |
| Semantic memory | None | Auto-extraction | Full knowledge graph |
| Procedural memory | None | Shared skill library | Versioned + team-scoped |
| Consolidation | None | Basic TTL | Sleep-time + compliance |
| Retention | N/A | {{pro_retention_days}} days | Custom + data residency |
| Audit logs | None | Read | Write + export + GDPR |

## Integration Points

- Consolidation rules: see `consolidation_policy` kind (P10) for promotion logic.
- Skill storage: see `procedural_memory` kind (P10) for skill schema and versioning.
- Retrieval config: see `retriever_config` kind (P01) for embedding and ranking config.
