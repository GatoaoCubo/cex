---
id: p10_lr_context_doc_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Context documents with vague scope statements ('this covers the payment system') required 2-4 clarification rounds before downstream consumers could use them. Documents with explicit insidand/ortside boundary declarations ('covers Stripe checkout flow; excludes subscription management, refund processing, and fraud detection') were used without clarification in all cases."
pattern: "Write the scope boundary as two lists: what is explicitly inside and what is explicitly outside. Both lists are required. Ambiguity in the outside list is the primary cause of scope creep in downstream work."
evidence: "11 context documents reviewed: 7 with vague scope required 2-4 clarification rounds; 4 with explicit..."
confidence: 0.7
outcome: SUCCESS
domain: context_doc
tags: [context-doc, scope-boundary, domain-scoping, stakeholders, constraints]
tldr: "Scope requires two explicit lists: inside and outside. The outside list prevents downstream scope creep. Both are required."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [context document, scope boundary, domain scoping, stakeholders, constraints, assumptions, inside outside, clarification]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Context Doc"
density_score: 0.90
llm_function: INJECT
---
## Summary
A context document's job is eliminating ambiguity about what a piece of work covers. The outside list in the scope section is more valuable than the inside list: consumers know what the work covers from the title; what they need — and almost never get explicitly — is what it does not cover. A missing or vague outside list causes downstream consumers to fill the gap with assumptions that diverge into scope creep, rework, or integration failures.
## Pattern
**Two-list scope declaration: inside and outside.**
Scope section structure:
```
## Scope
Inside:
- [specific item 1]
- [specific item 2]
- [specific item 3]
Outside:
- [excluded item 1 — why excluded if non-obvious]
- [excluded item 2]
- [excluded item 3]
```
Frontmatter scope (single sentence): name the bounded domain, actor type, and time horizon. Examples: "Stripe checkout flow for server-side integration, v3 API" / "Onboarding process for new engineers, first 30 days" / "LGPD data retention for SaaS products, 2023 cycle".
Stakeholders: list by role, not name. Constraints: hard non-negotiable limits (budget, legal, contract) — distinct from assumptions (beliefs that could be wrong). Assumptions: each must include a verification method ("verify by: calling /rate-limit endpoint").
## Anti-Pattern
- Scope without an outside list (leaves exclusions to assumption).
- Scope too broad ("covers the entire payment system") — split per bounded context.
- Scope too narrow (single fact belongs in a knowledge card).
- Stakeholders as names instead of roles.
- Mixing constraints (hard limits) with assumptions (beliefs that could be wrong).
- Filler prose ("This document describes...", "Basically...") — delete on sight.
- Body over 2048 bytes: trim References first, Background second; scope and constraints must survive.
- Atomic single-fact structure in body — that is a knowledge card, not a context_doc.
## Context
Context_doc vs. knowledge_card: a context document allows narrative prose and covers a bounded domain holistically. A knowledge card is atomic (one fact, one card). If content has a scope section and multiple interdependent sections, it is a context document. If it is a single extractable fact, it is a knowledge card.
Write the outside list before any other section. This forces explicit exclusion decisions before elaborating on inclusions — the only reliable way to prevent scope creep. Assumption verification discipline: every assumption must have a falsifiability condition ("assumed: rate limit is 1000 req/min; verify by: calling /rate-limit endpoint"), converting hidden risks into testsble hypotheses.
## Impact
