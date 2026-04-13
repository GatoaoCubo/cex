---
id: n06_task
kind: task
type: kind
pillar: P06
title: "Task — Vector Store Builder"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: task
quality: 8.9
tags: [task, p06, vector-store, builder, kind]
tldr: "Structured workflow for creating and managing vector stores with metadata, indexing, and query capabilities"
when_to_use: "Building, reviewing, or reasoning about vector store artifacts"
keywords: [task, vector-store, metadata, indexing, query, builder, artifact]
feeds_kinds: [task]
density_score: 0.92
---

# Task

## Spec
```yaml
kind: task
pillar: P06
llm_function: TOOL
max_bytes: 4096
naming: p06_task_{{name}}.md + .yaml
core: true
