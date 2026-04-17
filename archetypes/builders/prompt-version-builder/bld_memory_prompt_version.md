---
id: p10_lr_prompt_version_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "prompt_version artifacts require concrete parameter values with rationale. Placeholder values cause downstream failures."
pattern: "Define all parameters with concrete values and rationale. Validate against SCHEMA.md. Keep body under 2048 bytes."
evidence: "Pattern extracted from PromptLayer version tracking, DSPy optimized prompts, LangChain Hub versioning, Humanloop prompt management, Braintrust prompt registry documentation and production usage."
confidence: 0.7
outcome: SUCCESS
domain: prompt_version
tags: [prompt-version, P03, type-builder]
tldr: "Concrete values with rationale. Validate against schema. Stay under 2048 bytes."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [prompt version, sequential, branching, optimized, rollback]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.1
title: "Memory Prompt Version"
density_score: 0.90
llm_function: INJECT
---
## Summary
Prompt version — immutable snapshot of a prompt at a point in time with metrics and lineage. The difference between a useful prompt_version and a useless one is concrete values
with rationale versus placeholder text.
## Pattern
**Concrete parameters with rationale.**
Every parameter must have: name, value, and why that value was chosen.
Required body sections: Overview, Prompt Snapshot, Metrics, Lineage.
Body budget: 2048 bytes max.
## Anti-Pattern
1. No version tracking: Cannot reproduce results or rollback on regression
2. Mutable versions: Changing a 'version' in place breaks reproducibility
3. No metrics: Cannot compare versions objectively
4. No parent lineage: Cannot trace how a prompt evolved or why changes were made
## Context
The 2048-byte body limit keeps prompt_version artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.

## Metadata

```yaml
id: p10_lr_prompt_version_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-prompt-version-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | prompt_version |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
