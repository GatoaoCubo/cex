---
kind: quality_gate
id: p11_qg_memory_scope
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of memory_scope artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: memory_scope"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, memory-scope, P02]
tldr: "Pass/fail gate for memory_scope artifacts: required fields, id pattern, body sections, parameter completeness."
domain: "agent memory configuration and scope"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - bld_examples_memory_scope
  - p11_qg_retriever_config
  - p11_qg_chunk_strategy
  - p11_qg_handoff_protocol
  - p11_qg_output_validator
  - bld_instruction_memory_scope
  - p11_qg_constraint_spec
  - memory-scope-builder
  - p11_qg_prompt_version
  - p03_sp_memory_scope_builder
---

## Quality Gate

# Gate: memory_scope
## Definition
| Field | Value |
|---|---|
| metric | memory_scope artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: memory_scope` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p02_memscope_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | id field != filename without extension |
| H04 | Kind equals literal `memory_scope` | Any other kind value |
| H05 | Quality field is null | Any non-null value |
| H06 | All required fields present | Missing quality, tags, tldr or other required fields |
| H07 | All required body sections present | Missing ## Overview or ## Memory Types or ## Backend Config or ## Lifecycle |
| H08 | Body <= 2048 bytes | Body exceeds size limit |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Parameter completeness | 1.0 | All parameters have concrete values (no placeholders) |
| Rationale quality | 1.0 | Each parameter value has clear rationale |
| Pattern selection | 1.0 | Correct pattern chosen for the use case |
| Boundary clarity | 1.0 | Explicitly states what this IS and IS NOT |
| Integration mapping | 0.5 | Upstream and downstream connections documented |
| Density | 1.0 | Information density >= 0.8, no filler content |
| Tags quality | 0.5 | Tags >= 3, includes "memory_scope", relevant to content |
| Tldr quality | 0.5 | Tldr <= 160 chars, dense, accurate summary |
| Domain specificity | 1.0 | Parameters and values specific to declared domain |
| Testability | 0.5 | Configuration can be validated with known inputs |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
