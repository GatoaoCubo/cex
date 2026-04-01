---
id: p01_kc_knowledge_distillation
kind: knowledge_card
type: domain
pillar: P01
title: "Knowledge Distillation — Compressing Expertise into KCs"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: patterns
quality: null
tags: [distillation, knowledge, compression, kc, expertise]
tldr: "Transform verbose sources (docs, conversations, code) into dense, structured KCs. Keep signal, remove noise. Target: 1-2KB that replaces 10KB+ of raw source."
keywords: [distillation, compression, knowledge-card, signal-to-noise, density]
density_score: 0.92
---

# Knowledge Distillation

## Process
```
RAW SOURCE (10KB+ docs, conversations, code)
  → EXTRACT signal (concepts, patterns, decisions)
  → STRUCTURE (frontmatter + sections + tables)
  → COMPRESS (remove redundancy, increase density)
  → VALIDATE (does 1KB KC replace 10KB source?)
  → OUTPUT: knowledge_card (1-2KB, density >= 0.85)
```

## Distillation Heuristics
| Keep | Remove |
|------|--------|
| Definitions, boundaries | Verbose explanations |
| Decision criteria (when/when-not) | Historical context |
| Tables, structured data | Prose paragraphs |
| Anti-patterns | Obvious best practices |
| Provider-specific differences | Generic advice |
