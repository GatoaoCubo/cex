---
id: p01_kc_claude_md_patterns
kind: knowledge_card
type: domain
pillar: P01
title: "CLAUDE.md Patterns — System Prompt as File"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: meta
quality: 9.0
tags: [claude-md, system-prompt, meta, project-context, memory]
tldr: "CLAUDE.md is the system prompt that persists. Patterns: identity section, pointers table, rules count, brand injection, status dashboard."
when_to_use: "Designing or maintaining CLAUDE.md for any Claude Code project"
keywords: [claude-md, system-prompt, project-memory, configuration, identity]
density_score: 0.93
updated: "2026-04-07"
related:
  - ctx_cex_new_dev_guide
  - p01_kc_input_hydration
  - spec_cex_system_map
  - p01_kc_qa_validation
  - p03_sp_brand_nucleus
  - p01_kc_cex_project_overview
  - p01_kc_context_scoping
  - bld_knowledge_card_system_prompt
  - p03_sp_system-prompt-builder
  - p01_kc_cex_as_digital_asset
---

# CLAUDE.md Patterns

## Core Concept
CLAUDE.md is read by Claude Code at every session start. It's a persistent system prompt — the project's identity, rules, and state.

## Sections (best practice order)

| Section | Purpose | Example |
|---------|---------|---------|
| Brand Identity | WHO this project serves | Bootstrapped brand name + archetype |
| Who Am I | WHAT role this instance plays | "N07 = Orchestrator" |
| Pointers | WHERE things are | Table of paths to key files |
| Rules | WHAT must always be true | "8F mandatory", "GDP before dispatch" |
| Commands | WHAT the user can do | /plan, /guide, /spec, /grid |
| Tools | WHAT scripts exist | Python tool table |

## Anti-Patterns
- CLAUDE.md >5000 lines → too long, LLM skims. Keep <200 lines, link to details.
- No pointers → LLM can't find files. Always include path table.
- No rules → LLM makes up its own. Be explicit about constraints.
- Static → never updated. Inject brand, update status dynamically.

## CEX Implementation
- Top: Brand Identity (auto-injected by bootstrap)
- Middle: Pointers + Rules + Commands (stable structure)
- Bottom: Tools + Quick Dispatch (reference)
- Total: ~120 lines (dense, every line matters)

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_claude_md_patterns`
- **Tags**: [claude-md, system-prompt, meta, project-context, memory]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[ctx_cex_new_dev_guide]] | related | 0.29 |
| [[p01_kc_input_hydration]] | sibling | 0.26 |
| [[spec_cex_system_map]] | related | 0.26 |
| [[p01_kc_qa_validation]] | sibling | 0.26 |
| [[p03_sp_brand_nucleus]] | downstream | 0.25 |
| [[p01_kc_cex_project_overview]] | sibling | 0.25 |
| [[p01_kc_context_scoping]] | sibling | 0.23 |
| [[bld_knowledge_card_system_prompt]] | sibling | 0.23 |
| [[p03_sp_system-prompt-builder]] | downstream | 0.23 |
| [[p01_kc_cex_as_digital_asset]] | sibling | 0.22 |
