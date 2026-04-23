---
kind: quality_gate
id: p11_qg_workflow_primitive
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of workflow_primitive artifacts
pattern: few-shot learning for atomic orchestration building blocks
quality: 9.0
title: 'Gate: Workflow Primitive'
version: 1.0.0
author: builder
tags:
- eval
- P11
- quality_gate
- examples
tldr: Gates ensuring workflow primitives define typed I/O, enforce composition rules
  (parallel-merge, loop max_iter, gate threshold), and contain no full workflow graphs
  or DAG edges.
domain: workflow_primitive
created: '2026-04-06'
updated: '2026-04-06'
density_score: 0.85
related:
  - p03_ins_workflow_primitive_builder
  - bld_knowledge_card_workflow_primitive
  - bld_examples_workflow_primitive
  - bld_memory_workflow_primitive
  - p03_sp_workflow_primitive_builder
  - bld_config_workflow_primitive
  - bld_schema_workflow_primitive
  - bld_output_template_workflow_primitive
  - workflow-primitive-builder
  - bld_collaboration_workflow_primitive
---

## Quality Gate

## Definition
A workflow_primitive is an atomic orchestration building block — one of seven types (step, condition, loop, parallel, router, gate, merge) with typed inputs and outputs. It passes this gate when its type is valid, inputs and outputs are typed, type-specific guards are present (max_iter for loops, threshold for gates, merge_ref for parallel), and the primitive contains no full workflow graphs or DAG edges.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches pattern `p12_wp_{type}` or `p12_wp_{type}_{name}` | Mismatched IDs cause routing failures |
| H03 | `kind` is exactly `workflow_primitive` (literal match) | Kind drives the loader; wrong literal silently misroutes |
| H04 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H05 | `type` is one of: step, condition, loop, parallel, router, gate, merge | Unknown types break primitive resolution |
| H06 | `inputs` is a non-empty list with typed entries (name + type + required) | Untyped inputs break composition |
| H07 | `outputs` is a non-empty list with typed entries (name + type) | Untyped outputs break downstream consumption |
| H08 | Loop primitives have `max_iter` in range 1-100 | Unbounded loops are system killers |
| H09 | Parallel primitives have `merge_ref` pointing to a merge primitive | Fan-out without fan-in loses data |
| H10 | Gate primitives have numeric `threshold` | Thresholdless gates always pass — useless |
| H11 | Router primitives have `default_route` | Unmatched routes silently drop work |
| H12 | Total YAML size <= 4096 bytes | Oversized primitives exceed token budget |
| H13 | Primitive is atomic: one type, one operation, no workflow graphs | Compound primitives defeat the purpose of composition |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler | Mostly substantive | No filler; every line carries information |
| 2 | I/O typing precision (types match domain expectations, descriptions present) | 1.5 | Types are all "string" | Most types correct | Every type precisely matches the data it carries |
| 3 | Guard clause completeness (type-specific guards present and reasonable) | 1.5 | Missing required guards | Guards present but values questionable | Guards present with well-justified values |
| 4 | Composition metadata (composable_after/before lists match type semantics) | 1.0 | No composition metadata | Partial metadata | Complete composition rules for this type |
| 5 | Description clarity (one-line, actionable, matches what the primitive does) | 0.5 | Vague or missing | Present but generic | Precise one-line description of the operation |
| 6 | Error handling (on_error or retry_count defined where apownte) | 0.5 | No error handling | retry_count set | on_error with fallback primitive reference |
| 7 | Tags include `workflow_primitive` | 0.5 | Missing | Present but misspelled | Exactly `workflow_primitive` in tags list |
| 8 | Cross-primitive type compatibility (output types match expected input types of successor) | 1.0 | Types incompatible | Most compatible | All outputs type-match expected downstream inputs |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
