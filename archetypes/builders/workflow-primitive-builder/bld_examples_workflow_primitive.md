---
kind: examples
id: bld_examples_workflow_primitive
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of workflow_primitive artifacts
pattern: few-shot learning for atomic orchestration building blocks
quality: 9.0
title: "Examples Workflow Primitive"
version: "1.0.0"
author: n03_builder
tags: [workflow_primitive, builder, examples]
tldr: "Golden and anti-examples for workflow primitive construction, demonstrating ideal structure and common pitfalls."
domain: "workflow primitive construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: workflow-primitive-builder
## Golden Example: Step
INPUT: "Create a research step primitive that takes a query and returns findings"
OUTPUT (`p12_wp_step.yaml`):
```yaml
type: step
description: Execute research query against knowledge base and return ranked findings
inputs:
  - name: query
    type: string
    required: true
    description: Natural language research question
  - name: max_results
    type: integer
    required: false
    description: Maximum findings to return (default 10)
outputs:
  - name: findings
    type: list
    required: true
    description: Ranked list of relevant knowledge artifacts
  - name: confidence
    type: float
    required: true
    description: Overall retrieval confidence score (0.0-1.0)
retry_count: 2
on_error: p12_wp_step.fallback_search
composable_after: [condition, gate, merge]
composable_before: [condition, gate, parallel, router]
```
WHY THIS IS GOLDEN:
- filename follows `p12_wp_{type}.yaml`
- type is valid enum value
- inputs and outputs are fully typed with names, types, required flags
- descriptions are concise one-liners
- error handling present (retry_count + on_error)
- composition metadata specifies what can precede/follow
## Golden Example: Loop with Guard
OUTPUT (`p12_wp_loop_retry_build.yaml`):
```yaml
type: loop
description: Retry artifact build with quality feedback until passing score or max attempts
inputs:
  - name: build_intent
    type: string
    required: true
    description: Original build instruction
  - name: feedback
    type: string
    required: false
    description: Quality gate feedback from previous iteration
outputs:
  - name: artifact_path
    type: string
    required: true
    description: Path to the built artifact
  - name: quality_score
    type: float
    required: true
    description: Final quality gate score (0.0-10.0)
max_iter: 3
break_condition: "quality_score >= 8.0"
feedback_input: feedback
composable_after: [step, condition, merge]
composable_before: [gate, step]
```
WHY THIS PASSES:
- max_iter = 3 (within 1-100 range) — loop has termination guard
- break_condition provides early exit when quality is sufficient
- feedback_input connects loop iterations to quality gate output
- typed I/O enables composition with upstream step and downstream gate
## Golden Example: Parallel + Merge Pair
OUTPUT (`p12_wp_parallel_research.yaml`):
```yaml
type: parallel
description: Fan out research to N01 and N04 simultaneously
inputs:
  - name: research_query
    type: string
    required: true
outputs:
  - name: branch_results
    type: list
    required: true
branches:
  - p12_wp_step.n01_research
  - p12_wp_step.n04_knowledge
merge_ref: p12_wp_merge.research_collect
timeout_s: 300
```
OUTPUT (`p12_wp_merge_research_collect.yaml`):
```yaml
type: merge
description: Collect and deduplicate parallel research results from N01 and N04
inputs:
  - name: branch_results
    type: list
    required: true
    description: Results from parallel research branches
outputs:
  - name: merged_findings
    type: list
    required: true
    description: Deduplicated combined findings
  - name: coverage_score
    type: float
    required: true
    description: How much of the query space was covered (0.0-1.0)
strategy: all
source_refs:
  - p12_wp_parallel.research
```
WHY THIS PAIR PASSES:
- parallel has `merge_ref` pointing to the merge primitive
- merge has `source_refs` pointing back to the parallel
- parallel has `timeout_s` to kill stalled branches
- merge `strategy: all` waits for both branches
- types are consistent across the pair
## Golden Example: Gate
OUTPUT (`p12_wp_gate_quality_check.yaml`):
```yaml
type: gate
description: Block pipeline until quality threshold is met by upstream builders
inputs:
  - name: quality_scores
    type: list
    required: true
    description: Quality scores from upstream build steps
outputs:
  - name: gate_passed
    type: boolean
    required: true
    description: Whether the threshold was met
  - name: failing_items
    type: list
    required: false
    description: Items that did not meet threshold
threshold: 0.8
wait_for:
  - p12_wp_step.build_kc
  - p12_wp_step.build_agent
timeout_s: 600
```
WHY THIS PASSES:
- threshold is numeric (0.8 = 80% must pass)
- wait_for lists specific upstream primitives
- timeout_s prevents infinite blocking
- output includes both pass/fail and details of failures
## Anti-Example
BAD OUTPUT (`p12_wp_full_pipeline.yaml`):
```yaml
type: workflow
description: Complete research-build-validate pipeline
steps:
  - name: research
    action: query knowledge base
  - name: build
    action: construct artifact
  - name: validate
    action: run quality gates
  - name: deploy
    action: commit and signal
```
FAILURES:
1. `type: workflow` is not in the 7-value enum — this is not a primitive
2. contains multiple steps — primitives are atomic (one operation)
3. no typed inputs or outputs — composition is impossible
4. no guard clauses — no max_iter, no threshold, no timeout
5. this is a workflow (multi-step graph), not a primitive — use workflow-builder
## Anti-Example: Loop Without Guard
BAD OUTPUT (`p12_wp_loop.yaml`):
```yaml
type: loop
description: Keep retrying until it works
inputs:
  - name: task
    type: string
    required: true
outputs:
  - name: result
    type: string
    required: true
```
FAILURES:
1. no `max_iter` — unbounded loop will run forever (HARD gate H08 failure)
2. no `break_condition` — no way to exit early
3. description "keep retrying until it works" is vague and implies no termination
4. no `feedback_input` — loop iterations have no way to improve
