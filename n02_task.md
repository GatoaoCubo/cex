---
id: n02_task
kind: task
type: translation
pillar: P04
title: "Translate Embedder Provider Output Template"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: translation
quality: 9.1
tags: [translation, p04, reusable, kind-task]
tldr: "Reusable template for translating output from embedder providers with structured phases, triggers, and lifecycle management for repeatable workflows"
when_to_use: "Building, reviewing, or reasoning about translation artifacts"
keywords: [translation, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [translation]
density_score: null
---

# Translate Embedder Provider Output Template

## Spec
```yaml
kind: translation
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_translation_{{name}}.md + .yaml
core: true
