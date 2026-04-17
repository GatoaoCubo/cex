---
kind: examples
id: bld_examples_capability_registry
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of capability_registry artifacts
quality: 9.1
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
| Build dashboards | .claude/P02_model/dashboard-builder.md | ...
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

## Anti-Example 4: Flat List Without Layer Separation

```markdown
| capability_name | provider_agent | availability |
|----------------|----------------|--------------|
| Build landing page | .claude/P02_model/landing-page-builder.md | active |
| Knowledge management | N04_knowledge/P02_model/agent_knowledge.md | active |
| Orchestration | N07_admin/agent_card_n07.md | active |
```

### Why it fails:
All three agent layers mixed in one flat table. Builder sub-agents, nucleus domain agents, and nucleus cards have different invocation paths: sub-agents are invoked as Claude Code sub-agents; domain agents via dispatch.sh; nucleus cards describe the nucleus itself. Mixing them causes routing errors where N07 attempts to dispatch a builder sub-agent path as a nucleus boot.

## Key Distinctions
| Aspect | Good Registry Entry | Bad Registry Entry |
|--------|--------------------|--------------------|
| provider_agent | Validated path to existing file | Path to non-existent file |
| quality_baseline | "unscored" when source is null | Invented numeric score |
| keyword_index | >= 5 domain-derived terms | 1-2 generic terms |
| availability | "active" / "deprecated" / "experimental" | Missing or free-text |
| layer | Entries in correct section (builder / nucleus / card) | Mixed flat list |
