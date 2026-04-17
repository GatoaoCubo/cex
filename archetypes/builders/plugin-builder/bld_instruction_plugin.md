---
id: p01_kc_skill
kind: knowledge_card
type: kind
pillar: P04
title: "Skill — Deep Knowledge for skill"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: skill
quality: 9.1
tags: [skill, p04, reusable, kind-kc]
tldr: "Reusable capability with structured phases, triggers, and lifecycle management for repeatable workflows"
when_to_use: "Building, reviewing, or reasoning about skill artifacts"
keywords: [skill, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [skill]
density_score: null
llm_function: REASON
---
# Skill

This ISO defines a plugin contract: the extension surface a host uses to load, register, and invoke external capability.

## Spec
```yaml
kind: skill
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_skill_{{name}}.md + .yaml
core: true
