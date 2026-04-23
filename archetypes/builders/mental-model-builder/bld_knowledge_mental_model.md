---
kind: knowledge_card
id: bld_knowledge_card_mental_model
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for mental_model production — atomic searchable facts
sources: mental-model-builder MANIFEST.md + SCHEMA.md, cognitive science, BDI architecture
quality: 9.1
title: "Knowledge Card Mental Model"
version: "1.0.0"
author: n03_builder
tags: [mental_model, builder, examples]
tldr: "Golden and anti-examples for mental model construction, demonstrating ideal structure and common pitfalls."
domain: "mental model construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_mental_model
  - mental-model-builder
  - p03_sp_mental_model_builder
  - bld_collaboration_mental_model
  - p11_qg_mental_model
  - bld_memory_mental_model
  - bld_architecture_mental_model
  - p01_kc_mental_model
  - bld_config_mental_model
  - p03_ins_runtime_state
---

# Domain Knowledge: mental_model

This ISO operationalizes a mental model -- a compact analogy or abstraction that guides reasoning.
## Executive Summary
Mental models are design-time cognitive blueprints for agents — structured YAML artifacts encoding routing rules, decision trees, priorities, heuristics, and domain boundaries. Each mental model belongs to exactly ONE agent and defines how that agent thinks, not what it does. They differ from agents (which have capabilities and tools), routers (which route tasks between components), system prompts (which define persona), and P10 runtime state (which is ephemeral) by being static, versioned cognitive maps loaded at agent boot.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 (design-time spec) |
| Kind | `mental_model` (exact literal) |
| ID pattern | `p02_mm_{agent_slug}` |
| Machine format | YAML |
| Required frontmatter | 14 fields |
| Recommended frontmatter | 9 fields (personality, fallback, etc.) |
| Quality gates | 9 HARD + 12 SOFT |
| Max body | 2048 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Min routing rules | 3 |
| Min decision tree conditions | 2 |
## Patterns
| Pattern | Application |
|---------|-------------|
| Routing specificity | Keywords must be concrete nouns/verbs, never vague categories |
| Confidence thresholds | 0.8+ direct routing, 0.5-0.8 tentative, <0.5 fallback |
| Decision tree depth | Max 3 levels to avoid reasoning complexity |
| Priority ordering | Highest first, max 5-7 priorities (Miller's law) |
| Heuristic formulation | "when X, prefer Y because Z" — actionable, not philosophical |
| Domain map scoping | Explicit covers/routes_to prevents boundary drift |
| Personality coherence | tone + verbosity + risk_tolerance must be internally consistent |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| `pillar: P10` on a mental_model | P10 is runtime state; mental_model is design-time P02 |
| Fewer than 3 routing rules | Fails HARD gate — insufficient routing coverage |
| Single-branch decision tree | Minimum 2 conditions required |
| Self-assigned quality score | `quality` must be null at creation |
| Generic heuristics | Must reflect actual agent edge cases, not platitudes |
| Mixing agent identity into mental_model | agent-builder owns identity; mental_model owns cognition |
| Vague keywords ("stuff", "things") | No routing signal; use domain-specific terms |
## Application
1. Identify target agent slug (e.g., `research_agent` -> `p02_mm_research_agent`)
2. Write frontmatter: all 14 required fields; set `quality: null`, `pillar: P02`
3. Define `routing_rules`: minimum 3 entries with keywords, action, confidence
4. Define `decision_tree`: minimum 2 if/then/else branches
5. Order `priorities` list highest-first (max 7 items)
6. Write `heuristics` as concise rules for domain-specific edge cases
7. Define `domain_map`: explicit scope IN and OUT boundaries
8. Validate: body <= 2048 bytes, id == filename stem, 9 HARD + 12 SOFT gates
## References
- mental-model-builder SCHEMA.md v1.0.0
- Johnson-Laird 1983 — Mental Models
- BDI architecture — Belief-Desire-Intention agent model

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_mental_model]] | downstream | 0.55 |
| [[mental-model-builder]] | downstream | 0.54 |
| [[p03_sp_mental_model_builder]] | downstream | 0.50 |
| [[bld_collaboration_mental_model]] | downstream | 0.49 |
| [[p11_qg_mental_model]] | downstream | 0.47 |
| [[bld_memory_mental_model]] | downstream | 0.45 |
| [[bld_architecture_mental_model]] | downstream | 0.44 |
| [[p01_kc_mental_model]] | sibling | 0.42 |
| [[bld_config_mental_model]] | downstream | 0.40 |
| [[p03_ins_runtime_state]] | downstream | 0.38 |
