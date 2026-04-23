---
id: skill_memory_update
kind: instruction
scope: shared
purpose: Teach builders to reflect and record learnings after execution
quality: 9.0
title: "Skill Memory Update"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_memory_learning_record
  - bld_knowledge_card_learning_record
  - bld_norms
  - skill
  - bld_collaboration_memory_type
  - doctor
  - bld_manifest_memory_type
  - bld_instruction_memory_type
  - bld_meta_memory_builder
  - bld_system_prompt_memory_type
---
# Skill: Memory Update After Execution

## When to Use
After EVERY build session, before signaling complete.

## What to Record
One structured observation per session. Focus on **reusable patterns**, not obvious facts.

### Good Observations
1. "Splitting handler into validate+process+respond reduced errors 40%"
2. "Builders with >3 tools need explicit tool-selection criteria"
3. "ISO files >4KB overflow small model context — split into sections"

### Bad Observations (DO NOT record)
1. "The schema was followed" (obvious)
2. "The file was saved" (mechanical)
3. "Quality was high" (vague)

## How to Record

```bash
python _tools/cex_memory_update.py \
  --builder <your-builder-id> \
  --type feedback \
  --observation "what you learned" \
  --pattern "generalizable rule" \
  --evidence "data that supports it" \
  --confidence 0.8 \
  --outcome SUCCESS
```

## Observation Types
| Type | Decay | When to Use |
|------|-------|-------------|
| user | 0.02/day | User preference or style |
| feedback | 0.00 | Quality feedback (NEVER decays) |
| project | 0.05/day | Project-specific context |
| reference | 0.03/day | External knowledge or docs |

## Rules
1. ONE observation per session (quality > quantity)
2. Confidence 0.0-1.0 (be honest, 0.6-0.8 is normal)
3. Pattern must be ACTIONABLE (someone else can apply it)
4. Evidence must be MEASURABLE when possible
5. If nothing was learned, don't force an observation

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar |  |
| Domain | CEX system |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_learning_record]] | related | 0.35 |
| [[bld_knowledge_card_learning_record]] | related | 0.33 |
| [[bld_norms]] | related | 0.24 |
| [[skill]] | sibling | 0.22 |
| [[bld_collaboration_memory_type]] | related | 0.21 |
| [[doctor]] | sibling | 0.21 |
| [[bld_manifest_memory_type]] | related | 0.21 |
| [[bld_instruction_memory_type]] | sibling | 0.20 |
| [[bld_meta_memory_builder]] | related | 0.20 |
| [[bld_system_prompt_memory_type]] | related | 0.20 |
