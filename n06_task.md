---
id: n06_task_quality_gate_security
kind: knowledge_card
type: kind
pillar: P04
title: "Quality Gate Security — Structured Security Validation for skill"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: security
quality: 9.1
tags: [security, p04, reusable, kind-kc]
tldr: "Structured security validation framework with phase-based checks, trigger conditions, and lifecycle management for repeatable security workflows"
when_to_use: "Building, reviewing, or reasoning about security artifacts"
keywords: [security, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [security]
density_score: 85
---

# Quality Gate Security

## Spec
```yaml
kind: security_gate
pillar: P04
llm_function: TOOL
max_bytes: 4064
naming: p04_security_gate_{{name}}.md + .yaml
core: true
