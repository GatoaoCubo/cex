---
id: p01_kc_task
kind: knowledge_card
type: kind
pillar: P01
title: "Task — Structured Workflow for execution"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: task
quality: 9.1
tags: [task, p01, reusable, kind-kc]
tldr: "Structured workflow with defined phases, triggers, and lifecycle management for repeatable execution"
when_to_use: "Planning, executing, or reasoning about task artifacts"
keywords: [task, phases, trigger, reusable, workflow, lifecycle]
feeds_kinds: [task]
density_score: null
---

# Task

## Spec
```yaml
kind: task
pillar: P01
llm_function: TOOL
max_bytes: 4096
naming: p01_task_{{name}}.md + .yaml
core: true
