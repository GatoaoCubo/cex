---
id: p08_arch_builder_constructor
kind: agent_card
pillar: P08
title: "Architecture — N03 Builder Component Map"
version: 2.0.0
created: 2026-04-07
updated: 2026-04-07
author: builder_agent
domain: construction
quality: null
tags: [architecture, builder, N03, component-map, 8F]
tldr: "Component architecture map for N03 Builder — shows data flow from intent through 8F pipeline to compiled artifact."
density_score: 0.93
linked_artifacts:
  primary: "N03_builder/agents/agent_builder.md"
  related:
    - N03_builder/prompts/system_prompt_builder.md
    - N03_builder/orchestration/workflow_builder.md
---

# N03 Builder — Architecture Component Map

## Overview

N03 Builder receives construction tasks from N07 Orchestrator via handoff files.
Each task flows through the 8F pipeline, loading builder ISOs, injecting context,
producing artifacts, and compiling to YAML. The system is deterministic: same
intent + same ISOs + same context = same artifact structure.

## Data Flow

```
┌─────────────────────────────────────────────────────────┐
│                    N07 Orchestrator                      │
│         .cex/runtime/handoffs/n03_task.md                │
└──────────────────────┬──────────────────────────────────┘
                       │ handoff
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  F1 CONSTRAIN                           │
│  Intent → .cex/kinds_meta.json → kind + pillar + schema │
│  cex_query.py resolves intent to builder                 │
└──────────────────────┬──────────────────────────────────┘
                       │ kind, pillar
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  F2 BECOME                              │
│  archetypes/builders/{kind}-builder/ → 13 ISOs loaded   │
│  cex_skill_loader.py merges shared + kind-specific      │
└──────────────────────┬──────────────────────────────────┘
                       │ persona + constraints
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  F3 INJECT                              │
│  brand_inject.py → brand context                        │
│  cex_memory_select.py → relevant memory                 │
│  linked_artifacts → cross-references                    │
└──────────────────────┬──────────────────────────────────┘
                       │ full context
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  F4 REASON                              │
│  Plan artifact structure                                │
│  GDP gate if subjective decisions needed                │
│  cex_gdp.py → decision_manifest.yaml                   │
└──────────────────────┬──────────────────────────────────┘
                       │ plan
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  F5 CALL                                │
│  cex_retriever.py → similar artifacts                   │
│  cex_prompt_layers.py → pillar context                  │
│  External tool enrichment                               │
└──────────────────────┬──────────────────────────────────┘
                       │ enriched data
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  F6 PRODUCE                             │
│  Generate artifact with YAML frontmatter                │
│  Body under max_bytes                                   │
│  quality: null always                                   │
└──────────────────────┬──────────────────────────────────┘
                       │ artifact.md
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  F7 GOVERN                              │
│  cex_hooks.py → pre-validation                          │
│  Schema check against P{pillar}_*/_schema.yaml          │
│  Frontmatter YAML parse check                           │
└──────────────────────┬──────────────────────────────────┘
                       │ validated
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  F8 COLLABORATE                         │
│  cex_compile.py → .yaml output                          │
│  git commit -m "[N03] ..."                              │
│  signal_writer.py → .cex/runtime/signals/               │
└─────────────────────────────────────────────────────────┘
```

## Component Registry

| Component | Path | Role |
|-----------|------|------|
| Kind Registry | `.cex/kinds_meta.json` | Maps 123 kinds to pillars |
| Builder ISOs | `archetypes/builders/{kind}-builder/` | 13 ISOs per kind |
| Shared Skills | `archetypes/builders/_shared/` | Cross-kind skills (GDP, etc) |
| Pillar Schemas | `P{01-12}_*/_schema.yaml` | Validation constraints |
| Brand Config | `.cex/brand/brand_config.yaml` | Brand context injection |
| Memory Store | `.cex/learning_records/` | Historical learnings |
| Signal Path | `.cex/runtime/signals/` | Inter-nucleus signals |
| Handoff Path | `.cex/runtime/handoffs/` | Task assignments |
| Compiled Output | `N03_builder/compiled/` | Compiled YAML artifacts |

## Dependencies

```
N07 → handoff → N03 → signal → N07
                 │
                 ├── archetypes/builders/ (ISOs)
                 ├── .cex/kinds_meta.json (registry)
                 ├── P{01-12}_*/_schema.yaml (validation)
                 ├── .cex/brand/brand_config.yaml (brand)
                 └── .cex/learning_records/ (memory)
```

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Kind not found | cex_query.py returns empty | Ask N07 to clarify intent |
| ISO missing | cex_skill_loader.py warns | Use shared ISOs + schema only |
| Schema violation | cex_hooks.py FAIL | Rebuild with corrected frontmatter |
| Compile error | cex_compile.py exit 1 | Fix YAML syntax, re-compile |
| Quality < 8.0 | Peer review score | Rebuild from F4 with feedback |
