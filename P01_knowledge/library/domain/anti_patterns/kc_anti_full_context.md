---
id: p01_kc_anti_full_context
kind: knowledge_card
type: domain
pillar: P01
title: "Anti-Pattern: Full Context Dependency"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: anti_patterns
quality: null
tags: [anti-pattern, context-window, memory, session]
tldr: "Don't rely on conversation history as the only state. Context windows overflow, sessions end, models change. Persist state to files."
when_to_use: "Designing agent memory and state management"
keywords: [anti-pattern, context-dependency, state-persistence, session-loss]
density_score: 0.91
---

# Anti-Pattern: Full Context Dependency

## The Problem
Assuming the entire conversation history is always available. Context windows have limits (200K tokens max). Sessions end. Models switch. History is lost.

## Symptoms
- "It forgot what we discussed earlier"
- Breaking when context exceeds window
- Can't resume work across sessions
- Agent quality degrades over long conversations

## Fix
1. Write state to files (manifests, handoffs, plans)
2. Use `.cex/runtime/` for persistent state
3. Write learning records after important discoveries
4. Design for session-less operation: any session can pick up from files
5. `wf_auto_handoff.md` saves state before session ends
