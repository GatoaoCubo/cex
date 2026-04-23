---
id: p03_ins_smoke_eval_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Smoke Eval Builder Instructions
target: smoke-eval-builder agent
phases_count: 3
prerequisites:
  - Scope to test is identified (agent, service, pipeline, or component name)
  - At least one critical-path check can be described
  - Execution environment prerequisites are known (services, configs, env vars)
  - Total expected runtime is under 30 seconds
validation_method: checklist
domain: smoke_eval
quality: 9.0
tags: [instruction, smoke-eval, testing, sanity-check, P07]
idempotent: true
atomic: true
rollback: Delete generated smoke_eval file and restart from Phase 1
dependencies: []
logging: true
tldr: Build a smoke_eval with a critical-path check sequence, binary assertions, 30s timeout, and fast-fail — does the component work at all?
density_score: 0.85
llm_function: REASON
related:
  - bld_knowledge_card_smoke_eval
  - p03_sp_smoke_eval_builder
  - bld_collaboration_smoke_eval
  - p11_qg_smoke-eval
  - p01_kc_smoke_eval
  - bld_architecture_smoke_eval
  - p11_qg_unit_eval
  - bld_examples_smoke_eval
  - bld_instruction_e2e_eval
  - bld_knowledge_card_unit_eval
---
## Context
The smoke-eval-builder produces `smoke_eval` artifacts — fast sanity tests that verify
whether a component's critical path is functional. A smoke_eval answers one question:
"does this component work at all?" It is not a correctness test (unit_eval), not a
pipeline test (e2e_eval), and not a performance measurement (benchmark). It fails fast
on the first broken check, keeping total runtime under 30 seconds.
**Input contract**:
- `{{scope}}`: what is being tested (e.g. `research-agent`, `ingest-pipeline`, `auth-service`)
- `{{critical_path_raw}}`: free-text description of the minimum viable check sequence
- `{{prerequisites_raw}}`: comma-separated environment requirements before running
- `{{frequency}}`: how often this smoke runs (e.g. `on_deploy`, `hourly`, `pre_merge`)
**Output contract**: A single `smoke_eval` YAML/Markdown file with frontmatter, a
`critical_path` ordered check list, binary assertions with expected values, strict
timeout (<= 30 seconds), `fast_fail: true`, and a prerequisites list.
**Boundaries**:
- Smoke_eval verifies "does it work at all" — not "is it correct in all cases".
- Deep correctness checks belong in unit_eval artifacts.
- Multi-component pipeline validation belongs in e2e_eval artifacts.
- Throughput and latency measurement belongs in benchmark artifacts.
- Total runtime must be < 30 seconds — any check exceeding this is out of scope.
## Phases
### Phase 1: Identify Critical Path
**Primary action**: Determine the shortest sequence of checks that proves the component
is alive and functional, discarding everything non-essential.
```
INPUT: scope, critical_path_raw, prerequisites_raw
1. Characterize the scope:
   scope_profile = {
     name: {{scope}},
     type: "agent" | "service" | "pipeline" | "component",
     entry_point: how the component is invoked or reached,
     observable_output: what a healthy response looks like
   }
2. Extract critical path from critical_path_raw:
   Parse into ordered check steps.
   For each step candidate:
     - Is it verifiable in < 5 seconds?           -> include
     - Does it prove a fundamental capability?     -> include
     - Is it a nice-to-have or edge case?          -> exclude
     - Does it depend on external network calls?   -> flag as "external" (may be fragile)
   critical_path = ordered list of included steps (aim for 3-7 steps)
3. Assign runtime estimate per step:
   step_time_s = estimated seconds to execute
   ASSERT sum(step_time_s) < 30
   If sum >= 30: remove the slowest non-critical step until sum < 30.
4. Parse prerequisites_raw:
   prerequisites = [
     {name: requirement_name, type: "env_var" | "service" | "file" | "config",
      check: how to verify it exists}
   ]
OUTPUT: scope_profile{}, critical_path[] (3-7 steps, sum < 30s), prerequisites[]
```
Verification: `critical_path` has 3-7 steps. Estimated total runtime < 30 seconds.
### Phase 2: Define Assertions
**Primary action**: For each critical path step, write a binary assertion with an
expected value that can be evaluated as pass or fail with no ambiguity.
```
INPUT: critical_path[], scope_profile
1. Assertion rules (all assertions must follow these):
   - Binary: result is either PASS or FAIL — no partial credit
   - Observable: the check examines a concrete output, not a subjective quality
   - Specific: expected value is a concrete string, integer, boolean, or status code
   - Fast: each assertion evaluates in <= 5 seconds
2. For each step in critical_path:
   assertion = {
     step_id: "check_{N}",
     description: what is being checked (imperative sentence),
     command_or_action: how to execute the check,
     expected: concrete expected value (string, int, bool, or status pattern),
     actual_field: where to read the actual value from,
     pass_condition: "actual == expected" | "actual contains expected" | "actual > 0"
   }
3. Determine failure behavior:
   fast_fail: true  # abort on first FAIL — do not continue to remaining checks
   on_fail_message: "{step_id}: expected {{expected}}, got {{actual}}"
4. Assign severity to each check:
   "critical":  failure here means the component cannot function at all
   "warning":   failure here means degraded but not completely broken
OUTPUT: assertions[] (one per critical_path step), fast_fail=true,
        failure_message_template
```
Verification: every step has exactly one binary assertion. Every expected value is
concrete (not "should be non-null" — use a specific value). `fast_fail` is `true`.
### Phase 3: Assemble Artifact and Validate
**Primary action**: Combine all phase outputs into the final smoke_eval file and run
quality gates.
```
INPUT: scope_profile, critical_path, prerequisites, assertions, frequency
1. Assemble frontmatter:
   id: smoke-eval-`{{scope_slug}}`  # scope_slug = scope.lower().replace(" ", "-")
   kind: smoke_eval
   pillar: P07
   version: 1.0.0
   scope: `{{scope}}`
   timeout_seconds: sum(step_time_s) + 5  # buffer, hard cap at 30
   fast_fail: true
   frequency: `{{frequency}}`
   checks_count: len(critical_path)
   quality: null
   ASSERT timeout_seconds <= 30
2. Write body sections:
   ## Prerequisites  — list of environment requirements with check methods


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_smoke_eval]] | downstream | 0.43 |
| [[p03_sp_smoke_eval_builder]] | related | 0.39 |
| [[bld_collaboration_smoke_eval]] | downstream | 0.31 |
| [[p11_qg_smoke-eval]] | downstream | 0.31 |
| [[p01_kc_smoke_eval]] | downstream | 0.29 |
| [[bld_architecture_smoke_eval]] | downstream | 0.29 |
| [[p11_qg_unit_eval]] | downstream | 0.29 |
| [[bld_examples_smoke_eval]] | downstream | 0.29 |
| [[bld_instruction_e2e_eval]] | sibling | 0.28 |
| [[bld_knowledge_card_unit_eval]] | upstream | 0.28 |
