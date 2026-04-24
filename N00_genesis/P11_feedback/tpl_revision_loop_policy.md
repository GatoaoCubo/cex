---
id: rlp_{{name}}
kind: revision_loop_policy
8f: F7_govern
pillar: P11
title: "Revision Policy: {{name}}"
max_iterations: 3
iteration_on_quality_floor: 8.5
priority_order: [security, quality, implementation]
escalation_target: user
escalation_message_template: "Reached {{max_iterations}} revisions without passing gates: {{failing_gates}}"
per_scenario_overrides:
  security_critical: 5
  documentation: 2
version: 1.0.0
quality: 8.1
tags: [hermes_origin, revision, escalation, policy]
upstream_source: "1ilkhamov/opencode-hermes-multiagent"
related:
  - bld_collaboration_quality_gate
  - p03_sp_bugloop_builder
  - hitl-config-builder
density_score: 1.0
updated: "2026-04-22"
---

## Policy: {{name}}

### Revision Loop Behavior

| Parameter | Value | Notes |
|-----------|-------|-------|
| Max iterations | 3 | HERMES proven default |
| Quality floor | 8.5 | Trigger revision if score below this |
| Priority | security > quality > implementation | Conflict resolution order |
| Escalation | user | After max_iterations exhausted |

### Scenario Overrides

| Scenario | Max Iterations | Rationale |
|----------|---------------|-----------|
| security_critical | 5 | Extra cycles for security-sensitive artifacts |
| documentation | 2 | Docs rarely need >2 revision cycles |

### Escalation Protocol

When `max_iterations` is reached without all gates passing:
1. Emit escalation message: `Reached {{max_iterations}} revisions without passing gates: {{failing_gates}}`
2. Route to `escalation_target` (user / senior_nucleus / freeze)
3. Log revision trace for post-escalation review

### Boundaries

- NOT `retry_policy` (P09) -- retry_policy handles transient failures (network, timeout); this handles content quality cycles
- NOT `quality_gate` (P11) -- quality_gate is a single pass/fail check; revision_loop_policy orchestrates N of them
- NOT `regression_check` (P11) -- regression_check diffs against a baseline; this iterates toward a quality floor

### Usage in pipeline_template

```yaml
revision_loop:
  policy_ref: rlp_{{name}}
  max_iterations: 3
  escalation_target: user
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_quality_gate]] | related | 0.16 |
| [[p03_sp_bugloop_builder]] | related | 0.16 |
| [[hitl-config-builder]] | related | 0.15 |
