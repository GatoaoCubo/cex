---
id: n00_action_prompt_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Action Prompt -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, action_prompt, p03, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An action_prompt is a task prompt sent by a human or orchestrator to an agent, triggering a specific operation or sequence of operations. It carries the user's intent, required parameters, and contextual constraints needed for the agent to execute correctly. The output is a structured invocation that maps cleanly to a builder pipeline step or tool call.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `action_prompt` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| intent | string | yes | The action the prompt triggers (verb + object) |
| target_nucleus | string | yes | Receiving nucleus (n01-n07) |
| parameters | map | no | Named parameters passed to the agent |
| llm_function | string | no | 8F function this activates (INJECT, CALL, etc.) |

## When to use
- When a human or orchestrator needs to send a structured task to an agent nucleus
- When the action has specific parameters that must be declared and validated before execution
- When the prompt needs to be version-controlled and reusable across multiple dispatches

## Builder
`archetypes/builders/action_prompt-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind action_prompt --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ap_research_competitor_pricing
kind: action_prompt
pillar: P03
nucleus: n01
title: "Research Competitor Pricing"
version: 1.0
quality: null
---
intent: "research competitor pricing in EdTech SaaS"
target_nucleus: n01
parameters:
  domain: edtech
  depth: 6_competitors
```

## Related kinds
- `system_prompt` (P03) -- sets the agent identity before action_prompt fires
- `instruction` (P03) -- step-by-step execution instructions the action activates
- `chain` (P03) -- sequences multiple action_prompts into a pipeline
- `function_def` (P04) -- the tool definition the action_prompt may invoke
