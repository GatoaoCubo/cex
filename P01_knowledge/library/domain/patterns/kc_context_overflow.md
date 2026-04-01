---
id: p01_kc_context_overflow
kind: knowledge_card
type: domain
pillar: P01
title: "Context Overflow Management"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: patterns
quality: 8.4
tags: [pattern, skill, llm]
tldr: "Detect early, compress at 50%, offload at 70%, handoff at 80%. All state persists in files."
keywords: [context-overflow, window-limit, compression, handoff]
density_score: 0.91
---

# Context Overflow Management

| At | Strategy |
|----|----------|
| 50% | Summarize history |
| 70% | Write state to files |
| 80% | Full handoff, new session |
| Always | Token budgeting |
