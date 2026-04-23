---
kind: collaboration
id: bld_collaboration_nucleus_def
pillar: P12
llm_function: COLLABORATE
purpose: How nucleus_def-builder works in crews with other builders
quality: 9.1
title: "Collaboration Nucleus Def"
version: "1.0.0"
author: n05_wave8
tags: [nucleus_def, builder, collaboration]
tldr: "How nucleus_def-builder works in crews with other builders"
domain: "nucleus_def construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - nucleus-def-builder
  - bld_knowledge_card_nucleus_def
  - bld_system_prompt_nucleus_def
  - bld_collaboration_capability_registry
  - p08_pat_nucleus_fractal
  - bld_tools_nucleus_def
  - bld_collaboration_kind
  - bld_collaboration_model_provider
  - p02_nd_n03.md
  - bld_examples_nucleus_def
---

## Crew Role
Produces formal nucleus_def contracts that make the CEX 8-nucleus fractal architecture
machine-readable and orchestration-ready. Acts as the fractal cartographer that maps
each nucleus's identity, boundaries, and composability contracts.

## Receives From

| Source | What | Format |
|--------|------|--------|
| nucleus_models.yaml | CLI + model bindings per nucleus | YAML |
| N0{X} agent cards | Domain agents, kinds_owned, capabilities | Markdown |
| .claude/rules/n0{X}-*.md | Sin lens, routing rules, domain | Markdown |
| N00_genesis/README.md | Fractal structure, pillar map | Markdown |
| .cex/kinds_meta.json | Pillar assignments, kind boundaries | JSON |
| boot/n0{X}.ps1 | Boot script paths for contract | PowerShell |

## Produces For

| Consumer | What | Format |
|----------|------|--------|
| N07 Orchestrator | Dispatch contracts (role, boot_script, cli_binding) | Markdown |
| cex_router.py | CLI selection input (cli_binding, fallback_chain) | Markdown |
| N04 Knowledge | Indexed nucleus registry for retrieval | Markdown |
| spawn_grid.ps1 | Boot configuration (nucleus_id, boot_script) | Markdown |
| cex_retriever.py | Semantic search target for nucleus queries | Markdown |

## Boundary
Does NOT handle individual agent definitions (handled by agent-builder).
Does NOT handle model provider configuration (handled by model-provider-builder).
Does NOT handle crew assembly logic (handled by collaboration-pattern-builder).
Legal boundaries between nuclei (routing rules) are defined in .claude/rules/ files,
not within nucleus_def artifacts.

## Crew Patterns

### Pattern 1: Nucleus Registry Build
```
nucleus-def-builder (x7, one per N01-N07)
  --> produces: p02_nd_n01.md through p02_nd_n07.md
  --> N04 indexes all 7 artifacts
  --> N07 reads registry for dispatch routing
```

### Pattern 2: New Nucleus Registration
```
N03 builder-architect (designs new nucleus)
  --> nucleus-def-builder (formalizes the definition)
  --> N05 operations (validates boot contract)
  --> N07 orchestrator (integrates into dispatch)
```

### Pattern 3: Nucleus Audit
```
N01 intelligence (scans actual nucleus directories)
  --> nucleus-def-builder (updates nucleus_def artifacts)
  --> cex_doctor.py (verifies alignment between def + reality)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[nucleus-def-builder]] | upstream | 0.54 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.49 |
| [[bld_system_prompt_nucleus_def]] | upstream | 0.45 |
| [[bld_collaboration_capability_registry]] | sibling | 0.38 |
| [[p08_pat_nucleus_fractal]] | upstream | 0.34 |
| [[bld_tools_nucleus_def]] | upstream | 0.34 |
| [[bld_collaboration_kind]] | sibling | 0.33 |
| [[bld_collaboration_model_provider]] | sibling | 0.33 |
| [[p02_nd_n03.md]] | upstream | 0.33 |
| [[bld_examples_nucleus_def]] | upstream | 0.33 |
