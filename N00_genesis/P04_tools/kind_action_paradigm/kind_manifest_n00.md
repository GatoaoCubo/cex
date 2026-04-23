---
id: n00_action_paradigm_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Action Paradigm -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, action_paradigm, p04, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_action_paradigm
  - bld_schema_search_strategy
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_audit_log
  - bld_schema_dual_loop_architecture
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_multimodal_prompt
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An action_paradigm defines how agents execute actions in their environments, specifying the action space, observation model, reward structure, and execution loop. It codifies whether the agent uses ReAct (Reason+Act), Plan-Execute, or event-driven paradigms, and how tool calls are sequenced relative to reasoning steps. The output is a reusable execution contract that governs how nuclei interact with tools and environments.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `action_paradigm` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| paradigm_type | string | yes | ReAct, plan-execute, event-driven, or reflexion |
| action_space | list | yes | Available action types: tool_call, message, file_write, signal |
| observation_format | string | yes | How environment feedback is structured for LLM consumption |
| retry_policy | map | no | Error type -> retry limit and backoff strategy |

## When to use
- When defining how a new nucleus or agent loop interacts with its tool environment
- When the F5 CALL step needs a defined action protocol beyond simple tool invocation
- When designing agentic pipelines that require specific action/observation loop structures

## Builder
`archetypes/builders/action_paradigm-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind action_paradigm --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ap_react_nucleus_loop
kind: action_paradigm
pillar: P04
nucleus: n03
title: "ReAct Nucleus Execution Loop"
version: 1.0
quality: null
---
paradigm_type: ReAct
action_space: [tool_call, file_write, git_commit, signal]
observation_format: "JSON with {tool, result, error, timestamp}"
retry_policy:
  tool_error: {max: 3, backoff: exponential}
```

## Related kinds
- `function_def` (P04) -- tool definitions that populate the action_space
- `planning_strategy` (P03) -- planning approach that drives action selection
- `hook` (P04) -- pre/post hooks that wrap action execution
- `workflow` (P12) -- orchestration layer that sequences action_paradigm invocations

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_action_paradigm]] | downstream | 0.46 |
| [[bld_schema_search_strategy]] | downstream | 0.38 |
| [[bld_schema_reranker_config]] | downstream | 0.38 |
| [[bld_schema_benchmark_suite]] | downstream | 0.38 |
| [[bld_schema_integration_guide]] | downstream | 0.37 |
| [[bld_schema_audit_log]] | downstream | 0.37 |
| [[bld_schema_dual_loop_architecture]] | downstream | 0.37 |
| [[bld_schema_usage_report]] | downstream | 0.37 |
| [[bld_schema_dataset_card]] | downstream | 0.37 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.37 |
