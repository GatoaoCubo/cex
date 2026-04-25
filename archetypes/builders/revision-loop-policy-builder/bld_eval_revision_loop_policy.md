---
id: p11_qg_revision_loop_policy
kind: quality_gate
pillar: P11
llm_function: GOVERN
purpose: F7 GOVERN quality gates for revision_loop_policy artifacts
quality: 8.6
title: "Quality Gate: Revision Loop Policy Builder"
version: "1.0.0"
author: n03_hermes_w1_6
tags: [quality_gate, revision_loop_policy, builder, p11, governance, f7]
domain: "revision_loop_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
tldr: "F7 GOVERN quality gates for revision_loop_policy artifacts"
density_score: 0.91
target_kind: revision_loop_policy
delivery_threshold: 0.85
bypass_policy: owner
related:
  - p03_sp_quality_gate_builder
  - p11_qg_creation_artifacts
  - bld_collaboration_quality_gate
  - quality-gate-builder
  - p03_ins_quality_gate
  - p11_qg_engineering_artifacts
  - bld_knowledge_card_quality_gate
  - p11_qg_quality_gate
  - bld_memory_quality_gate
  - p01_kc_artifact_quality_evaluation_methods
---

## Quality Gate

## HARD Gates (all must pass)

| ID | Criterion | Failure Action |
|----|-----------|---------------|
| H01 | `kind == "revision_loop_policy"` | block |
| H02 | `max_iterations` is a positive integer (>= 1) | block |
| H03 | `priority_order == [security, quality, implementation]` (exact order, all 3) | block |
| H04 | `escalation_target` in `{user, senior_nucleus, freeze}` | block |
| H05 | `escalation_message_template` contains `{{max_iterations}}` AND `{{failing_gates}}` | block |
| H06 | `quality == null` (never self-score) | block |

## SOFT Gates (weighted, sum = 1.0)

| ID | Criterion | Weight | Scoring Method |
|----|-----------|--------|---------------|
| S01 | Boundaries section present with all 4 NOT-items | 0.25 | binary |
| S02 | `per_scenario_overrides` includes `security_critical` and `documentation` | 0.25 | binary |
| S03 | Usage in `pipeline_template` code block present in body | 0.25 | binary |
| S04 | `tags` includes `hermes_origin` | 0.25 | binary |

## Scoring Formula

```
aggregate_score = S01*0.25 + S02*0.25 + S03*0.25 + S04*0.25
PASS: all H gates pass AND aggregate_score >= 0.85
FAIL: any H gate fails OR aggregate_score < 0.85
```

## Actions

| Outcome | Consequence |
|---------|-------------|
| PASS | Artifact proceeds to F8 COLLABORATE (compile + commit + signal) |
| H-FAIL | Artifact returned with specific HARD gate failure detail; fix and retry |
| S-FAIL | Artifact returned with soft gate breakdown; improve and retry (max 2 retries) |

## Bypass Policy

- Who may override: `owner` (N03 builder or N05 operations nucleus)
- Conditions: only H06 (quality: null) may be bypassed in peer-review mode (peer sets actual score)
- All other HARD gates: no bypass permitted
- Audit: log bypass with actor, timestamp, and justification

## Examples

## Golden Example 1: Standard Policy (HERMES Default)

```yaml
---
id: rlp_standard
kind: revision_loop_policy
pillar: P11
title: "Revision Policy: Standard"
max_iterations: 3
iteration_on_quality_floor: 8.5
priority_order: [security, quality, implementation]
escalation_target: user
escalation_message_template: "Reached {{max_iterations}} revisions without passing gates: {{failing_gates}}"
per_scenario_overrides:
  security_critical: 5
  documentation: 2
version: 1.0.0
quality: null
tags: [hermes_origin, revision, escalation, policy, standard]
upstream_source: "1ilkhamov/opencode-hermes-multiagent"
---

## Policy: Standard

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

1. Evaluate all quality gates for iteration N
2. IF all gates pass OR score >= 8.5: ACCEPT, stop loop
3. IF attempt < 3: increment attempt, regenerate with gate context
4. IF attempt == 3: emit escalation message, route to user

### Boundaries

- NOT `retry_policy` (P09): retry_policy handles transient failures (network, timeout)
- NOT `quality_gate` (P11): quality_gate is a single check; this orchestrates N of them
- NOT `regression_check` (P11): regression_check diffs against a baseline
- NOT `bugloop` (P11): bugloop is code-bug auto-correction, not content quality iteration

### Usage in pipeline_template

```yaml
revision_loop:
  policy_ref: rlp_standard
  max_iterations: 3
  escalation_target: user
```
```

## Golden Example 2: Security-Critical Override

```yaml
---
id: rlp_security_critical
kind: revision_loop_policy
pillar: P11
title: "Revision Policy: Security Critical"
max_iterations: 5
iteration_on_quality_floor: 9.0
priority_order: [security, quality, implementation]
escalation_target: senior_nucleus
escalation_message_template: "Security artifact reached {{max_iterations}} revisions without passing: {{failing_gates}}"
per_scenario_overrides:
  security_critical: 5
  standard: 3
  documentation: 2
version: 1.0.0
quality: null
tags: [hermes_origin, revision, escalation, policy, security_critical]
---
```
**Why it works:** max_iterations elevated to 5 for security sensitivity. Quality floor raised to 9.0
(tighter than standard). Escalation routes to senior_nucleus (automated) rather than user (manual).
Overrides cover all three canonical scenarios.

## Golden Example 3: Freeze Policy (Fully Automated Pipeline)

```yaml
---
id: rlp_freeze_on_fail
kind: revision_loop_policy
pillar: P11
title: "Revision Policy: Freeze on Exhaustion"
max_iterations: 3
iteration_on_quality_floor: 8.5
priority_order: [security, quality, implementation]
escalation_target: freeze
escalation_message_template: "Pipeline frozen after {{max_iterations}} revisions. Gates still failing: {{failing_gates}}"
per_scenario_overrides:
  security_critical: 5
  documentation: 2
version: 1.0.0
quality: null
tags: [hermes_origin, revision, escalation, policy, freeze, headless]
---
```
**Why it works:** `escalation_target: freeze` is appropriate for overnight headless pipelines where
there is no user to route to. The pipeline freezes and logs; a human reviews the next morning.

## Anti-Example 1: Missing escalation_message_template placeholders

```yaml
---
id: rlp_bad_template
kind: revision_loop_policy
max_iterations: 3
escalation_message_template: "Too many attempts"
---
```
**Why it fails (H05):** `escalation_message_template` must contain `{{max_iterations}}` AND
`{{failing_gates}}` to provide actionable context to the escalation target.
"Too many attempts" gives the recipient no information about what failed or how many cycles ran.

## Anti-Example 2: Invalid priority_order

```yaml
---
id: rlp_bad_priority
kind: revision_loop_policy
max_iterations: 3
priority_order: [quality, security]
escalation_target: user
---
```
**Why it fails (H03):** `priority_order` must contain all three tiers: `[security, quality, implementation]`.
Omitting `implementation` means implementation-gate conflicts have no defined resolution order.
Reordering security below quality violates the HERMES canonical order (security is always first).

## Anti-Example 3: Confusing with retry_policy

```yaml
---
id: rlp_confused
kind: revision_loop_policy
max_iterations: 5
trigger: "network_timeout OR rate_limit_exceeded"
---
```
**Why it fails:** This describes transient infrastructure retries -- route to `retry-policy-builder`.
`revision_loop_policy` handles content-quality iteration, not network/timeout retries.
The `trigger` field is not part of the revision_loop_policy schema.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
