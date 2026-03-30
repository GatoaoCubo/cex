---
id: p10_lr_prompt_version_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
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
agent_node: edison
keywords: [prompt version, sequential, branching, optimized, rollback]
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
- No version tracking: Cannot reproduce results or rollback on regression
- Mutable versions: Changing a 'version' in place breaks reproducibility
- No metrics: Cannot compare versions objectively
- No parent lineage: Cannot trace how a prompt evolved or why changes were made
## Context
The 2048-byte body limit keeps prompt_version artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.
