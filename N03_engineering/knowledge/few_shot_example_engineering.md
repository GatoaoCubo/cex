---
id: p01_fse_builder_golden
kind: few_shot_example
pillar: P01
title: Few-Shot Examples -- Golden Artifacts
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [few-shot, builder, N03, golden]
tldr: 3 golden artifact patterns the builder learns from -- agent, KC, workflow.
density_score: 0.85
---

# Golden Examples for Builder

## Pattern 1: Agent (quality 9.5)

**Why golden**: Complete frontmatter, all sections filled, boundaries table, immediately usable.

Frontmatter pattern: id=p02_agent_{{name}}, kind=agent, pillar=P02
capabilities_count and tools_count are ACTUAL counts, never placeholders.
tldr is one sentence telling exactly what this agent does.

Body: Identity > Capabilities (numbered) > Tools (table) > Routing > Boundaries (Does/NOT table) > Crew Role

## Pattern 2: Knowledge Card (quality 9.3)

**Why golden**: Dense, searchable, no filler, spec block with actual constraints.

Frontmatter: when_to_use and keywords fields are critical for discoverability.
feeds_kinds lists which artifact kinds consume this KC.

Body: Spec (yaml) > Definition > When to Use > Boundaries > Relations > Anti-Patterns

## Pattern 3: Workflow (quality 9.1)

**Why golden**: Every step has agent, input, output, signal, depends_on.

steps_count is actual count. execution is sequential/parallel/mixed.
signals lists ALL signals emitted across all steps.

Body: Purpose > Steps (Agent/Input/Output/Signal/Depends each) > Quality Gates > Signals

## What Makes Golden

1. ZERO placeholder values in frontmatter (no null, no TBD)
2. Every section has 3+ lines of substantive content
3. Tables have real data, not example rows
4. Density >= 0.90
5. Compiles to valid YAML without warnings