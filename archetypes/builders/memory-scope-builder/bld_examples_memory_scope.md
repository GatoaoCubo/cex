---
kind: examples
id: bld_examples_memory_scope
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of memory_scope artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Memory Scope"
version: "1.0.0"
author: n03_builder
tags: [memory_scope, builder, examples]
tldr: "Golden and anti-examples for memory scope construction, demonstrating ideal structure and common pitfalls."
domain: "memory scope construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: memory-scope-builder
## Golden Example
INPUT: "Create memory scope for a research agent with long-term learning"
OUTPUT:
```yaml
id: p02_memscope_research_agent
kind: memory_scope
pillar: P02
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Research Agent Memory Scope"
quality: null
tags: [memory_scope, P02, memory]
tldr: "Research Agent Memory Scope — production-ready memory_scope configuration"
```
## Overview
Memory scope for research agents that learn across sessions.
Combines ephemeral conversation buffer with persistent fact storage and learned patterns.

## Memory Types
| Type | Purpose | TTL | Backend |
|------|---------|-----|---------|
| episodic | Current session conversation context | session | in-memory |
| semantic | Distilled facts and findings | 30d | sqlite |
| procedural | Learned research patterns and shortcuts | 90d | sqlite |

## Backend Config
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| backend | sqlite | Local, zero-dependency, ACID compliant |
| db_path | .cex/memory/{agent_id}.db | Per-agent isolation |
| max_entries | 1000 | Bounded growth with LRU eviction |
| eviction_policy | score-weighted LRU | High-confidence entries persist longer |
| encryption | none | Local-only, no PII stored |

## Lifecycle
- Session start: load semantic + procedural from sqlite, init episodic buffer
- During session: append to episodic, promote high-confidence findings to semantic
- Session end: consolidate episodic -> extract patterns -> store procedural
- Eviction: score-weighted LRU when max_entries reached (confidence * recency)
- TTL sweep: daily cron removes expired entries
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p02_memscope_ pattern (H02 pass)
- kind: memory_scope (H04 pass)
- All required fields present (H06 pass)
- Body has all 4 sections: Overview, Memory Types, Backend Config, Lifecycle (H07 pass)
- Parameters table with value and rationale (S03 pass)
- tldr under 160 chars (S01 pass)
- tags >= 3 items, includes "memory_scope" (S02 pass)
## Anti-Example
INPUT: "Create memory config for chatbot"
BAD OUTPUT:
```yaml
id: chatbot-memory
kind: memory
quality: 9.0
tags: [memory]
```
FAILURES:
1. id has hyphens and no p02_memscope_ prefix -> H02 FAIL
2. kind: 'memory' not 'memory_scope' -> H04 FAIL
3. Missing fields: memory_types, backend, ttl -> H06 FAIL
4. quality: 7.5 (not null) -> H05 FAIL
5. No ## Memory Types section -> H07 FAIL
6. No backend config table -> S03 FAIL
