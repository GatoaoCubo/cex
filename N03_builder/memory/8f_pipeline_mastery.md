---
id: p10_mem_builder_8f_mastery
kind: memory
pillar: P10
title: "8F Pipeline Mastery — Builder Learning Record"
version: 2.0.0
created: 2026-04-07
updated: 2026-04-07
author: builder_agent
domain: construction
quality: null
tags: [memory, builder, N03, 8F, pipeline, learning, mastery]
tldr: "Accumulated learnings from 8F pipeline execution — patterns that produce 9.0+ artifacts consistently."
memory_type: convention
freshness: current
decay_days: 365
density_score: 0.94
linked_artifacts:
  primary: "N03_builder/agents/agent_builder.md"
  related:
    - N03_builder/quality/quality_gate_builder.md
    - N03_builder/knowledge/knowledge_card_builder.md
---

# 8F Pipeline Mastery — Builder Learning Record

## F1 CONSTRAIN Lessons

### Pattern: Resolve Before Build
Always run `cex_query.py` to resolve intent to kind before loading ISOs.
Free-text intent can map to unexpected kinds — the query tool uses TF-IDF
to find the best match across 123 kinds.

### Anti-pattern: Assuming Kind
Never assume the kind from the task description alone. "Build an agent card"
could be `agent_card`, `agent`, or `architecture` depending on context.
Always verify against `.cex/kinds_meta.json`.

## F2 BECOME Lessons

### Pattern: Load All 13 ISOs
Even if the task seems simple, load all 13 ISOs. ISOs 05 (anti-patterns) and
06 (linked kinds) often contain critical constraints that prevent rework.

### Anti-pattern: Partial ISO Loading
Skipping ISOs 09 (memory) or 10 (brand) leads to context-poor artifacts
that fail peer review. Load everything, even if not all ISOs are populated.

## F3 INJECT Lessons

### Pattern: Brand First, Memory Second
Inject brand context before memory. Brand config establishes the tone and
audience context that memory entries need to be interpreted against.

### Pattern: Check Linked Artifacts
If the kind's ISO 06 lists linked kinds, check whether those artifacts exist.
If they do, inject them as cross-references. This dramatically improves density.

## F4 REASON Lessons

### Pattern: Structure Before Content
Plan the heading structure and frontmatter fields before writing any body
content. This prevents the "rewrite the frontmatter after the body" trap
that wastes tokens and introduces inconsistencies.

### Pattern: GDP Gate Check
At F4, always check if the decision manifest exists and covers the current
task. Subjective decisions (tone, audience, style) must come from the manifest,
not from builder assumptions.

## F5 CALL Lessons

### Pattern: Retriever for Similar Artifacts
Before producing, run `cex_retriever.py` to find similar existing artifacts.
They serve as golden examples and prevent duplicate or contradictory content.

## F6 PRODUCE Lessons

### Pattern: Frontmatter Template
Always start from the universal frontmatter template (11 required fields).
Then add kind-specific extensions. Never freeform the frontmatter.

### Pattern: density_score Estimation
Estimate density_score based on: unique concepts per section, cross-references,
actionable content vs filler. Range 0.80-1.00 for well-crafted artifacts.

## F7 GOVERN Lessons

### Pattern: YAML Parse Test
Before saving, mentally parse the frontmatter YAML. Common errors:
- Missing quotes around strings with colons
- Incorrect list indentation
- `quality: 9.0` instead of `quality: null`

## F8 COLLABORATE Lessons

### Pattern: Commit Batch Size
Commit every 3-4 files during batch builds. This provides recovery points
without creating excessive commit noise. Each commit should be a logical unit.

### Pattern: Signal After Commit
Always commit BEFORE signaling. A signal implies the work is committed and
available. Signaling before committing leads to N07 reading incomplete state.

## Meta

- **Source**: Direct experience from fractal bootstrap, grid missions, solo builds
- **Confidence**: High (validated across 100+ artifact builds)
- **Decay**: Review in 365 days for relevance
