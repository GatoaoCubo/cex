---
kind: examples
id: bld_examples_capability_registry
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of capability_registry artifacts
quality: null
title: "Examples Capability Registry"
version: "1.0.0"
author: n04_wave8
tags: [capability_registry, builder, examples, agent-discovery]
tldr: "Golden and anti-examples of capability_registry artifacts"
domain: "capability_registry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example

```markdown
---
id: p08_cr_builder_sub_agents.md
kind: capability_registry
pillar: P08
title: "CEX Builder Sub-Agent Registry"
registry_scope: builder_sub_agents
entry_count: 3
index_date: "2026-04-14"
quality: null
---

## Builder Sub-Agent Index
| capability_name | provider_agent | input_schema | output_schema | cost_tokens | quality_baseline | availability | keyword_index |
|----------------|----------------|--------------|---------------|-------------|-----------------|--------------|---------------|
| Build landing page | .claude/agents/landing-page-builder.md | intent string, brand_config | landing_page (P05 .md) | medium | unscored | active | landing page, html, conversion, marketing, P05 |
| Build knowledge card | .claude/agents/knowledge-card-builder.md | topic, domain, sources | knowledge_card (P01 .md) | low | unscored | active | knowledge card, KC, P01, documentation, RAG |
| Build agent card | .claude/agents/agent-card-builder.md | nucleus id, capabilities list | agent_card (P08 .md) | low | unscored | active | agent card, A2A, capability declaration, P08 |

## Query Examples
| Query | Top Candidate | Why |
|-------|--------------|-----|
| "who can build conversion pages?" | landing-page-builder | keyword: conversion, marketing |
| "who documents domain knowledge?" | knowledge-card-builder | keyword: knowledge card, KC, documentation |
```

## Anti-Example 1: Missing Required Fields

```markdown
| capability_name | provider_agent |
|----------------|----------------|
| Build reports  | some-builder   |
```

### Why it fails:
Missing input_schema, output_schema, cost_tokens, quality_baseline, availability, and keyword_index. Unusable for ranked candidate selection -- N07 cannot determine if the agent is appropriate for a given query.

## Anti-Example 2: Phantom Agent Reference

```markdown
| capability_name | provider_agent | ...
|----------------|----------------|
| Build dashboards | .claude/agents/dashboard-builder.md | ...
```

### Why it fails:
`dashboard-builder.md` does not exist in `.claude/agents/`. Registry entries with phantom paths corrupt the discovery index and cause dispatch failures. Every `provider_agent` must be validated as an existing file.

## Anti-Example 3: Invented Quality Scores

```markdown
| capability_name | quality_baseline |
|----------------|-----------------|
| Build landing page | 8.5 |
```

### Why it fails:
The landing-page-builder has `quality: null` (unscored). Inventing a score of 8.5 misleads N07 into preferring this builder over genuinely scored alternatives. Use "unscored" when source has null.
