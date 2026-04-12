---
id: phases
kind: concept
type: workflow
pillar: N05
title: "Phases — Structured Workflow Execution for AI Artifacts"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_n05
domain: ai_workflow
quality: 8.6
tags: [ai, n05, phases, workflow, lifecycle]
tldr: "Structured execution framework with defined phases, trigger conditions, and lifecycle management for repeatable AI workflows"
when_to_use: "Designing, reviewing, or reasoning about phase-based AI workflows"
keywords: [phases, workflow, lifecycle, trigger, execution, ai, validation]
feeds_kinds: [phase]
density_score: 8.4
---

# Phases

## Spec
```yaml
kind: phase
pillar: N05
llm_function: TOOL
max_bytes: 4096
naming: n05_phase_{{name}}.md + .yaml
core: true
