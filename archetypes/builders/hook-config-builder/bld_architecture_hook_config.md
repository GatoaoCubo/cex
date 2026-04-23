---
kind: architecture
id: bld_architecture_hook_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of hook_config — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Hook Config"
version: "1.0.0"
author: n03_builder
tags: [hook_config, builder, examples]
tldr: "Golden and anti-examples for hook config construction, demonstrating ideal structure and common pitfalls."
domain: "hook config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - hook-config-builder
  - p03_sp_hook_config_builder
  - p10_lr_hook_config_builder
  - p01_kc_hook_config
  - bld_examples_hook_config
  - bld_knowledge_card_hook_config
  - bld_instruction_hook_config
  - p11_qg_hook_config
  - bld_collaboration_hook_config
  - bld_tools_hook_config
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| phases | 8F pipeline phases where hooks can bind | hook_config | required |
| events | Event types (pre-build, post-build, on-error, quality-fail) | hook_config | required |
| actions | What each hook triggers (script, signal, validator) | hook_config | required |
| conditions | When a hook fires (always, on-fail, on-score-below) | hook_config | required |
| priority | Execution order when multiple hooks bind same event | hook_config | optional |
| hook | Implementation code that runs when event fires | P04 | consumer |
| lifecycle_rule | Archive/promote policy triggered by hooks | P04 | consumer |
## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| phases | hook_config | produces | 8F pipeline phase declarations |
| events | hook_config | produces | Event type bindings |
| actions | hook_config | produces | Action declarations per hook |
| conditions | hook_config | produces | Conditional firing rules |
| priority | hook_config | produces | Execution order for same-event hooks |
| hook | P04 | depends | Implementation code bound to events |
| lifecycle_rule | P04 | depends | Policy triggered by hook events |
## Boundary Table
| hook_config IS | hook_config IS NOT |
|----------------|-------------------|
| Declaration of which hooks fire and when | hook (implementation code) |
| Event binding configuration per build phase | lifecycle_rule (archive/promote policy) |
| Conditional firing rules for pipeline events | plugin (extension module) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| spec | phases, events, actions, conditions | Define the artifact's core declarations |
| optional | priority | Extend with execution ordering |
| external | hook, lifecycle_rule | Downstream consumers of declarations |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_architecture_hook_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-architecture-hook-config.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[hook-config-builder]] | upstream | 0.67 |
| [[p03_sp_hook_config_builder]] | upstream | 0.59 |
| [[p10_lr_hook_config_builder]] | downstream | 0.57 |
| [[p01_kc_hook_config]] | upstream | 0.56 |
| [[bld_examples_hook_config]] | upstream | 0.55 |
| [[bld_knowledge_card_hook_config]] | upstream | 0.55 |
| [[bld_instruction_hook_config]] | upstream | 0.53 |
| [[p11_qg_hook_config]] | downstream | 0.50 |
| [[bld_collaboration_hook_config]] | downstream | 0.47 |
| [[bld_tools_hook_config]] | upstream | 0.41 |
