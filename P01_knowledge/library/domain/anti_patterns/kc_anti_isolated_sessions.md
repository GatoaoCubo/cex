---
id: p01_kc_anti_isolated_sessions
kind: knowledge_card
type: domain
pillar: P01
title: "Anti-Pattern: Isolated Sessions"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: anti_patterns
quality: null
tags: [anti-pattern, isolated, sessions, continuity, handoff]
tldr: "Sessions that don't share state. Each starts from zero. No learning carries over. Fix: shared filesystem, signals, handoffs."
when_to_use: "Designing multi-session or multi-agent workflows"
keywords: [anti-pattern, isolation, continuity, shared-state, handoff]
density_score: 0.91
---

# Anti-Pattern: Isolated Sessions

## The Problem
Each session/agent starts from scratch. No memory of previous sessions. No shared state between agents. Work is repeated.

## Symptoms
- Agent re-discovers what was already known
- Parallel agents produce contradictory output
- No improvement over time
- User repeats context every session

## Fix
1. Shared filesystem as state (`.cex/runtime/`, `P01_knowledge/`)
2. Signals between agents (`signal_writer.py`)
3. Handoff documents (`.cex/runtime/handoffs/`)
4. Decision manifests (`.cex/runtime/decisions/`)
5. Learning records (`.cex/learning_records/`)
6. Brand config as shared identity (`.cex/brand/brand_config.yaml`)
