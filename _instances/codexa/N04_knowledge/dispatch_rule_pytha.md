---
id: p12_dr_pytha_knowledge
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2023-10-05
updated: 2023-10-05
author: dispatch-rule-specialist
domain: knowledge_management
quality: null
tags: [dispatch, knowledge_management, pytha]
tldr: Route tasks related to knowledge management to the Pytha knowledge nucleus
scope: knowledge
keywords: [conhecimento, knowledge, gestão, management, indexação, indexing, embedder, embbedder, pesquisa, research]
satellite: pytha
model: sonnet
priority: 8
confidence_threshold: 0.70
fallback: default_gateway
conditions: {}
load_balance: false
routing_strategy: hybrid
---
# Knowledge Management Dispatch Rule
## Purpose
Routes tasks related to knowledge management, indexing, and embedding to the Pytha knowledge nucleus satellite. This ensures that knowledge-centric tasks are handled efficiently by a dedicated system.
## Keyword Rationale
The selected keywords include bilingual coverage and variations of terms related to knowledge management to ensure broad recognition of relevant tasks.
## Fallback Logic
Fallback to a general-purpose gateway ensures tasks are processed even if the Pytha nucleus is unavailable, maximizing task completion reliability.
---
