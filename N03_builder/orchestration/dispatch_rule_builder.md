---
id: p12_dr_builder_construction
kind: dispatch_rule
pillar: P12
title: "Dispatch Rule — N03 Builder"
version: 2.0.0
created: 2026-04-07
updated: 2026-04-07
author: builder_agent
domain: construction
quality: 9.0
tags: [dispatch-rule, builder, N03, routing, construction, 8F]
tldr: "Routes build/create/scaffold/artifact tasks to N03 Builder nucleus — keyword match with 0.70 confidence threshold."
scope: builder_construction
keywords: [build, create, construct, scaffold, generate, forge, artifact, kind, 8F, pipeline, template, bootstrap, construir]
agent_group: builder
model: opus-4-6
priority: 9
confidence_threshold: 0.70
fallback: n07
conditions:
  quality_min: 8.0
  signal_required: true
routing_strategy: keyword_match
density_score: 0.96
---

# Builder Construction Dispatch Rules

## Purpose

Routing rules that N07 Orchestrator uses to dispatch artifact construction tasks
to N03 Builder. Tasks matching construction keywords above 0.70 confidence get
routed to N03 in a new terminal via `bash _spawn/dispatch.sh solo n03`.

## Primary Rule: Build / Create → N03

| Property | Value |
|----------|-------|
| Keywords | build, create, construct, scaffold, generate, forge, artifact, kind, 8F, pipeline, template, bootstrap, construir |
| Target | N03 (Builder) |
| CLI | pi (claude opus-4-6) |
| Context | 1M tokens |
| Priority | 9 (highest among builders) |
| Mode | solo (default), grid if > 3 artifacts in batch |

## Keyword Categories

### Action Verbs (EN)
build, create, construct, scaffold, generate, forge, produce, compose, assemble

### Action Verbs (PT)
construir, criar, gerar, montar, produzir, compor

### Domain Nouns
artifact, kind, builder, ISO, template, frontmatter, schema, pipeline, 8F

### Compound Triggers
"build artifact", "create kind", "scaffold template", "8F pipeline", "generate builder",
"bootstrap fractal", "construct agent card", "forge knowledge card"

## Confidence Scoring

- **Match strategy**: keyword_match with bilingual stemming (PT + EN)
- **Threshold**: 0.70 (7 of 10 keywords or equivalent weight)
- **Below threshold**: Return to N07 for clarification
- **Multiple matches**: Highest priority wins. N03 has priority 9.

## Anti-Routing (NOT N03)

| Task Pattern | Correct Nucleus |
|--------------|-----------------|
| "research competitor X" | N01 (Research) |
| "write ad copy for Y" | N02 (Marketing) |
| "index knowledge about Z" | N04 (Knowledge) |
| "deploy to production" | N05 (Operations) |
| "price the course at $X" | N06 (Commercial) |
| "dispatch tasks to builders" | N07 (Orchestrator) |

## Dispatch Command

```bash
# Solo — single artifact
bash _spawn/dispatch.sh solo n03 "Leia .cex/runtime/handoffs/n03_task.md e execute."

# Grid — batch of artifacts
bash _spawn/dispatch.sh grid MISSION_NAME
```

## References

- N07 master dispatch: N07_admin/orchestration/dispatch_rule_admin.md
- Workflow: N03_builder/orchestration/workflow_builder.md
- Spawn config: N03_builder/orchestration/spawn_config_builder.md
