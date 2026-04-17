---
kind: examples
id: bld_examples_role_assignment
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of role_assignment artifacts
quality: 9.0
title: "Examples Role Assignment"
version: "1.0.0"
author: n03_wave8_builder
tags: [role_assignment, builder, examples, composable, crewai]
tldr: "Golden and anti-examples of role_assignment artifacts"
domain: "role_assignment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---

## Golden Example
```markdown
---
id: p02_ra_domain_researcher.md
kind: role_assignment
pillar: P02
role_name: domain_researcher
agent_id: .claude/agents/research-pipeline-builder.md
goal: Produce 8-12 citable sources per brief with confidence score >= 0.75 avg.
backstory: You are a senior market intelligence analyst with 10y in AI/SaaS competitive research. You triangulate primary sources (SEC filings, GitHub, product docs) before citing any claim.
crewai_equivalent: "Agent(role='Domain Researcher', goal=..., backstory=...)"
quality: null
---

## Responsibilities
1. Accept research brief (topic, scope, deadline); return 8-12 sources.
2. Validate each source against freshness (<= 12 months) and authority heuristics.
3. Output citation objects with url, confidence, snippet, fetched_at.
4. Surface gaps/contradictions in a `caveats` block.

## Tools Allowed
- WebSearch
- WebFetch
- cex_retriever
- -cex_compile  <!-- writer, not editor -->

## Delegation Policy
can_delegate_to: [peer_reviewer]
conditions:
  on_source_count_below: 6
```

## Anti-Example 1: Inline Agent Identity
```markdown
---
kind: role_assignment
role_name: writer
agent_id: "You are a helpful writer agent with tools..."
---
```
## Why it fails:
`agent_id` inlines identity instead of pointing to an agent artifact. Fails H04 (broken ref). Breaks reuse -- every crew referencing this role duplicates the inline identity. Must be `.claude/agents/{slug}.md` or `N0x/agents/{slug}.md`.

## Anti-Example 2: Delegation by agent_id (portability break)
```markdown
---
role_name: manager
agent_id: .claude/agents/supervisor-builder.md
---
## Delegation Policy
can_delegate_to:
  - .claude/agents/research-pipeline-builder.md   # agent_id, not role_name
  - .claude/agents/changelog-builder.md
```
## Why it fails:
`can_delegate_to` leaks agent_ids instead of role_names. Fails H07. Breaks crew portability -- swapping the underlying agent requires rewriting every role that delegates to it. Always name roles (e.g., `researcher`, `editor`), not agents.
