---
id: p01_kc_anti_patterns_general
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "LLM Agent Anti-Patterns — General Catalog"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: anti_patterns
quality: 9.0
tags: [anti-pattern, catalog, llm, agent, pitfalls]
tldr: "Catalog of common LLM agent mistakes: over-autonomy, prompt bloat, jargon dependency, self-scoring, single-point-of-failure."
when_to_use: "Reviewing agent system design for common pitfalls"
keywords: [anti-pattern, catalog, pitfalls, design-review]
density_score: 0.92
updated: "2026-04-07"
related:
  - bld_collaboration_system_prompt
  - p01_kc_agent
  - bld_collaboration_agent
  - p01_kc_spawn_patterns
  - bld_knowledge_card_agent
  - p01_kc_context_scoping
  - agent-builder
  - p01_kc_input_hydration
  - spec_context_assembly
  - bld_architecture_agent
---

# LLM Agent Anti-Patterns

## Catalog

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| **Self-scoring** | LLM rates own output highly | Peer-review (different LLM or human scores) |
| **Prompt bloat** | System prompt >10K tokens | Layer: core identity (short) + injected context (on demand) |
| **Over-autonomy** | Agent makes decisions user should make | GDP: guided decisions before autonomous execution |
| **Jargon lock-in** | System requires learning custom vocabulary | Use industry-standard terms (spec not PSPEC) |
| **God agent** | One agent does everything | Nucleus separation: each agent has bounded scope |
| **API key dependency** | System breaks without paid API | Subscription CLI as primary (`claude -p`), API as fallback |
| **Hallucination trust** | Accepting LLM output without validation | F7 GOVERN: always validate before F8 COLLABORATE |
| **Template rigidity** | All output forced into one format | Multiple output templates per nucleus |
| **Sequential bottleneck** | Everything waits for one agent | Fan-out/fan-in via `/grid` |
| **Knowledge amnesia** | Learnings not persisted | Learning records + memory files + KCs |

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_anti_patterns_general`
- **Tags**: [anti-pattern, catalog, llm, agent, pitfalls]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_system_prompt]] | downstream | 0.31 |
| [[p01_kc_agent]] | sibling | 0.30 |
| [[bld_collaboration_agent]] | downstream | 0.29 |
| [[p01_kc_spawn_patterns]] | sibling | 0.28 |
| [[bld_knowledge_card_agent]] | sibling | 0.27 |
| [[p01_kc_context_scoping]] | sibling | 0.26 |
| [[agent-builder]] | downstream | 0.26 |
| [[p01_kc_input_hydration]] | sibling | 0.25 |
| [[spec_context_assembly]] | related | 0.25 |
| [[bld_architecture_agent]] | downstream | 0.25 |
