---
id: p01_kc_hook_config
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P04
title: "Hook Config — Deep Knowledge for hook_config"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: builder_agent
domain: hook_config
quality: 9.1
tags: [hook_config, P04, CONSTRAIN, kind-kc, hooks, lifecycle]
tldr: "Declarative manifest that lists WHICH hooks fire at WHICH lifecycle events — the registry, not the implementation. Hook artifacts implement; hook_config declares when they activate."
when_to_use: "Building, reviewing, or reasoning about hook_config artifacts"
keywords: [hook_config, lifecycle, pre_save, post_save, pre_commit, validation]
feeds_kinds: [hook_config]
density_score: null
related:
  - bld_examples_hook_config
  - p10_lr_hook_config_builder
  - bld_knowledge_card_hook_config
  - hook-config-builder
  - p03_sp_hook_builder
  - bld_collaboration_hook
  - bld_collaboration_hook_config
  - bld_architecture_hook_config
  - p03_sp_hook_config_builder
  - bld_instruction_hook_config
---

# Hook Config

## Spec
```yaml
kind: hook_config
pillar: P04
llm_function: CONSTRAIN
max_bytes: 4096
naming: p04_hook_config_{{topic}}.md + .yaml
core: false
```

## What It Is
A hook_config is a declarative manifest that registers which hooks fire at which lifecycle events during builder execution. It is the DECLARATION layer — listing event names, hook references, execution order, and conditions. It is NOT a hook (which is the IMPLEMENTATION of the actual logic) nor an env_config (which sets environment variables). The hook_config answers "which hooks are active and when do they fire?" — the hook artifact answers "what does this hook actually do?".

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| Git | .git/hooks/ + core.hooksPath config | Config points to hook scripts |
| Claude Code | settings.json hooks array | Event + command + pattern matching |
| GitHub Actions | workflow YAML on: triggers | Declarative event-to-action mapping |
| Kubernetes | Admission webhooks config | ValidatingWebhookConfiguration |
| Webpack | plugin.apply(compiler.hooks) | Tap into named lifecycle hooks |
| pytest | conftest.py + pytest_plugins | Hook registration via convention |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| events | list[str] | required | pre_save, post_save, pre_commit, post_compile, on_error |
| hooks | list[ref] | required | References to hook artifact IDs |
| execution_order | str | sequential | sequential vs parallel; safety vs speed |
| fail_strategy | str | abort | abort / warn / skip; strictness vs resilience |
| conditions | list[expr] | null | Filter by kind, pillar, or file pattern |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Pre-save validation chain | Catch errors before write | lint_frontmatter -> check_density -> validate_schema |
| Post-compile indexer | Keep search index current | After .yaml compile, update index.db |
| On-error recovery | Self-healing pipeline | On validation fail, trigger auto-fix hook |
| Kind-scoped hooks | Different rules per artifact | agent hooks != knowledge_card hooks |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Hooks in code, not config | Invisible; cannot audit or toggle | Extract to hook_config; reference by ID |
| No execution order | Race conditions on shared state | Set explicit sequential or priority ordering |
| fail_strategy: skip everywhere | Silent failures accumulate | Use abort for HARD gates; warn for SOFT only |

## Integration Graph
```
[lifecycle_event] --> [hook_config] --> [hook_1, hook_2, hook_3]
                          |                    |
                   [conditions]          [execution_order]
                          |                    |
                   [kind/pillar filter]  [sequential/parallel]
```

## Decision Tree
- IF need to implement hook logic THEN use hook (P04)
- IF need environment variables THEN use env_config (P09)
- IF need runtime execution rules THEN use runtime_rule (P09)
- IF need to declare which hooks fire when THEN hook_config
- DEFAULT: hook_config when registering lifecycle hooks for a builder or pipeline

## Quality Criteria
- GOOD: At least 2 events defined; hooks referenced by ID; fail_strategy set
- GREAT: Full lifecycle coverage (pre+post for save, compile, commit); kind-scoped conditions; execution_order explicit; tested with cex_hooks.py
- FAIL: No event mapping; hooks referenced by path instead of ID; no fail_strategy

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_hook_config]] | downstream | 0.56 |
| [[p10_lr_hook_config_builder]] | downstream | 0.53 |
| [[bld_knowledge_card_hook_config]] | sibling | 0.52 |
| [[hook-config-builder]] | related | 0.49 |
| [[p03_sp_hook_builder]] | upstream | 0.48 |
| [[bld_collaboration_hook]] | downstream | 0.47 |
| [[bld_collaboration_hook_config]] | downstream | 0.47 |
| [[bld_architecture_hook_config]] | downstream | 0.46 |
| [[p03_sp_hook_config_builder]] | related | 0.46 |
| [[bld_instruction_hook_config]] | upstream | 0.45 |
