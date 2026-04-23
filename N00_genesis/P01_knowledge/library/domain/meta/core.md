---
id: p01_kc_core
kind: knowledge_card
type: kind
pillar: P04
title: "Core — Foundation for pattern"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: core
quality: 9.1
tags: [core, p04, reusable, kind-kc]
tldr: "Reusable foundation with structured phases, triggers, and lifecycle management for repeatable workflows"
when_to_use: "Building, reviewing, or reasoning about core artifacts"
keywords: [core, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [core]
density_score: null
related:
  - p04_kc_core
  - p01_kc_skill
  - bld_config_ab_test_config
  - bld_instruction_kind
  - p01_kc_naming_rule
---

# Core

## Spec
```yaml
kind: core
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_core_{{name}}.md + .yaml
core: true

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_kc_core]] | sibling | 0.26 |
| [[p01_kc_skill]] | sibling | 0.23 |
| [[bld_config_ab_test_config]] | downstream | 0.15 |
| [[bld_instruction_kind]] | upstream | 0.15 |
| [[p01_kc_naming_rule]] | sibling | 0.15 |
