---
kind: memory
id: bld_memory_skill
pillar: P09
llm_function: INJECT
purpose: Persistent learnings for skill-builder across sessions
pattern: what worked, what failed, key insights from building skills
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Skill"
version: "1.0.0"
author: n03_builder
tags: [skill, builder, examples]
tldr: "Golden and anti-examples for skill construction, demonstrating ideal structure and common pitfalls."
domain: "skill construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Memory: skill-builder

## Learnings
1. Skills are NOT agents — they have no identity, only behavior
2. Skills are NOT workflows — they are reusable across workflows
3. The boundary between skill and workflow: a skill is invokable, a workflow is sequential
4. Universal term: Alexa Skills, Semantic Kernel Skills, AgentSkills.io

## What Worked
1. Defining trigger conditions clearly prevents misuse
2. Phases (setup → execute → validate → cleanup) give consistent structure
3. Anti-patterns section is high-value — prevents common mistakes

## What Failed
1. Over-scoping: trying to make one skill do too much → split into focused skills
2. Missing boundary: skill that overlaps with agent identity → strip identity, keep behavior

## Metadata

```yaml
id: bld_memory_skill
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-skill.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P09 |
| Domain | skill construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
