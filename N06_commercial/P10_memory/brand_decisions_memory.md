---
id: brand_decisions_memory
kind: memory_summary
pillar: P10
title: "Brand Decisions Memory — N06 Commercial"
nucleus: N06
version: 1.0.0
created: 2026-04-07
author: n06_commercial
domain: brand_decisions
quality: 9.0
tags: [memory, brand, decisions, N06, GDP, strategy]
tldr: "Persistent log of brand decisions made via GDP — prevents re-asking, ensures consistency across sessions."
scope: brand_decision_tracking
density_score: 1.0
---

# Brand Decisions Memory

## Purpose

Track every brand/commercial decision made via GDP so future sessions inherit context. No decision should be asked twice. Cost of re-asking: user friction + lost trust. Cost of tracking: zero.

---

## Decision Log Template

```yaml
decision_id: "YYYY-MM-DD_topic"
date: "2026-MM-DD"
category: "brand | pricing | funnel | positioning | identity"
question: "What was asked?"
answer: "What the user decided"
rationale: "Why this choice (if given)"
impact: "What this affects downstream"
reversible: true | false
```

---

## Active Decisions

### D-2026-04-06-001: NotebookLM Scope
- **Category**: content_distribution
- **Question**: 1 notebook per mission or per domain?
- **Answer**: Per domain (reusable)
- **Rationale**: Speed + reusability. Domain notebooks accumulate knowledge.
- **Impact**: All content pipelines use domain-scoped notebooks
- **Reversible**: Yes

### D-2026-04-06-002: Default NotebookLM Outputs
- **Category**: content_distribution
- **Question**: Which output types by default?
- **Answer**: Flashcards, audio_summary, quiz (subset for speed)
- **Rationale**: Full set too slow; these 3 cover learning + engagement
- **Impact**: `cex_notebooklm.py` default output config
- **Reversible**: Yes

### D-2026-04-06-003: Publish Mode
- **Category**: content_distribution
- **Question**: Auto-publish or manual approval?
- **Answer**: Auto-publish
- **Rationale**: Speed > manual approval for internal content
- **Impact**: No human gate before publishing
- **Reversible**: Yes

### D-2026-04-06-004: Browser Engine
- **Category**: infrastructure
- **Question**: Which browser for NotebookLM automation?
- **Answer**: Chrome local (free, validated in PoC)
- **Rationale**: Zero cost, already working
- **Impact**: No Playwright/Puppeteer cloud costs
- **Reversible**: Yes

### D-2026-04-06-005: Google Account
- **Category**: infrastructure
- **Question**: Which Google account for NotebookLM?
- **Answer**: {{BRAND_EMAIL}} (already PRO)
- **Rationale**: Existing PRO account, no new subscription needed
- **Impact**: All NotebookLM operations use this account
- **Reversible**: Yes

---

## Superseded Decisions

_None yet. When a decision is overridden, move it here with superseded_by reference._

---

## Decision Metrics

| Category | Active | Superseded | Total |
|----------|--------|-----------|-------|
| brand | 0 | 0 | 0 |
| pricing | 0 | 0 | 0 |
| content_distribution | 3 | 0 | 3 |
| infrastructure | 2 | 0 | 2 |
| **Total** | **5** | **0** | **5** |

---

## Usage Rules

1. **Before asking a GDP question** → search this file first
2. **After every GDP session** → append new decisions here
3. **On contradiction** → flag to user, don't silently override
4. **Quarterly review** → prune stale decisions, confirm active ones still hold
