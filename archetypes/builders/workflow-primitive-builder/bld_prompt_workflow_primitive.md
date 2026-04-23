---
id: p03_ins_workflow_primitive_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: instruction-builder
title: Workflow Primitive Builder Instructions
target: workflow-primitive-builder agent
phases_count: 3
prerequisites:
  - Primitive type is known (step, condition, loop, parallel, router, gate, or merge)
  - Input data types are identified
  - Output data types are identified
  - Guard clauses are defined (max_iter for loops, threshold for gates)
validation_method: checklist
domain: workflow_primitive
quality: 9.0
tags: [instruction, workflow_primitive, orchestration, P12]
idempotent: true
atomic: true
rollback: "Discard primitive and regenerate — primitives are stateless definitions"
dependencies: []
logging: true
tldr: Produce a YAML workflow primitive with typed inputs, typed outputs, composition constraints, and guard clauses — under 4096 bytes, one type per file, no full workflow graphs included.
density_score: 0.86
llm_function: REASON
related:
  - bld_knowledge_card_workflow_primitive
  - p03_sp_workflow_primitive_builder
  - bld_output_template_workflow_primitive
  - p11_qg_workflow_primitive
  - bld_config_workflow_primitive
  - bld_schema_workflow_primitive
  - workflow-primitive-builder
  - bld_examples_workflow_primitive
  - bld_architecture_workflow_primitive
  - bld_collaboration_workflow_primitive
---
## Context
The workflow-primitive-builder produces `workflow_primitive` artifacts — YAML definitions of
atomic orchestration building blocks. A workflow primitive is the smallest reusable unit of
a workflow: it takes typed inputs, performs one operation, and produces typed outputs. Seven
types exist: step (single action), condition (branch), loop (repeat), parallel (fan-out),
router (dynamic dispatch), gate (sync barrier), and merge (fan-in). Primitives compose
left-to-right into full workflows.
**Input contract**:
- `{{type}}`: one of step, condition, loop, parallel, router, gate, merge
- `{{name}}`: descriptive name for this primitive instance (e.g. `research_step`, `quality_gate`)
- `{{inputs}}`: list of typed input fields the primitive consumes
- `{{outputs}}`: list of typed output fields the primitive produces
- `{{guards}}`: max_iter (loops), threshold (gates), timeout_s (parallel)
**Output contract**: A single `workflow_primitive` YAML file named `p12_wp_{{type}}.yaml`,
under 4096 bytes, with type, inputs, outputs, and guard clauses. No full workflow graphs,
no DAG edges, no signal payloads.
**Boundaries**:
- A workflow primitive is atomic — one type, one operation, one file.
- Full multi-step workflows belong in a workflow artifact.
- DAG edge definitions belong in a DAG artifact.
- Inter-agent signals belong in a signal artifact.
- Primitives must be composable: outputs of one primitive type-match inputs of the next.
## Phases
### Phase 1: Classify
**Primary action**: Confirm this is an atomic workflow block and determine the required
structure based on primitive type.
```
INPUT: type, name, inputs, outputs, guards
1. Confirm this is an atomic building block, not a full workflow or DAG:
   Is it a single operation with typed I/O?               -> workflow_primitive
   Is it multiple operations connected by edges?          -> NOT a workflow_primitive
   Is it an inter-agent status notification?              -> NOT a workflow_primitive
2. Validate type:
   Must be one of: step, condition, loop, parallel, router, gate, merge
   Each type has specific required guards:
     step:      none (simplest primitive)
     condition: requires condition_expr (boolean expression)
     loop:      requires max_iter (integer > 0)
     parallel:  requires merge_ref (reference to corresponding merge primitive)
     router:    requires routes (list of {match, target} pairs)
     gate:      requires threshold (float 0.0-1.0 or integer count)
     merge:     requires strategy (all, any, first, majority)
3. Validate inputs:
   Each input must have: name (string), type (string), required (boolean)
   At least 1 input required (primitives do not create data from nothing)
4. Validate outputs:
   Each output must have: name (string), type (string)
   At least 1 output required (primitives do not consume data without producing)
5. Validate guards (type-specific):
   loop: max_iter must be integer > 0 and <= 100
   gate: threshold must be numeric (0.0-1.0 for ratio, integer for count)
   parallel: timeout_s must be integer > 0
OUTPUT: validated_type, validated_inputs, validated_outputs, validated_guards
```
Verification: `validated_type` is in the 7-value enum. Inputs and outputs are typed.
Type-specific guards are present and valid.
### Phase 2: Compose
**Primary action**: Assemble the YAML primitive with typed I/O, guards, and
composition metadata.
```
INPUT: validated_type, name, validated_inputs, validated_outputs, validated_guards
1. Set filename: p12_wp_{{type}}.yaml (or p12_wp_{{type}}_{{name}}.yaml if named)
2. Assemble frontmatter:
   id: p12_wp_{{type}}
   kind: workflow_primitive
   pillar: P12
   type: {{type}}
   quality: null
3. Compose inputs list:
   For each input:
     name: field name (snake_case)
     type: data type (string, integer, float, boolean, list, object, artifact_ref)
     required: true | false
     description: one-line purpose
4. Compose outputs list:
   For each output:
     name: field name (snake_case)
     type: data type
     description: one-line purpose
5. Add type-specific guards:
   step: (no guards)
   condition:
     condition_expr: boolean expression to evaluate
     true_branch: reference to next primitive when true
     false_branch: reference to next primitive when false
   loop:
     max_iter: integer (1-100)
     break_condition: optional early exit expression
     feedback_input: field name that receives loop iteration feedback
   parallel:
     branches: list of primitive references to execute concurrently
     timeout_s: max seconds before killing stalled branches
     merge_ref: reference to the merge primitive that collects results
   router:
     routes: list of {match: pattern, target: primitive_ref}
     default_route: fallback primitive_ref when no match
   gate:
     threshold: ratio (0.0-1.0) or count (integer) required to pass
     wait_for: list of upstream primitive refs
     timeout_s: max seconds to wait before failing
   merge:
     strategy: all | any | first | majority
     source_refs: list of upstream parallel/gate refs
6. Add composition metadata:
   composable_after: list of primitive types that can precede this
   composable_before: list of primitive types that can follow this
7. Size check:
   Estimate YAML byte count
   If > 4096 bytes: compress descriptions
   until size <= 4096 bytes
OUTPUT: workflow_primitive YAML content (assembled, not yet validated)
```
Verification: all required fields present. Type-specific guards present. Inputs
and outputs are typed. Size <= 4096 bytes.
### Phase 3: Validate
**Primary action**: Run all quality gates against the assembled YAML and output the
final file only if all HARD gates pass.
```
INPUT: workflow_primitive YAML content
1. HARD quality gates (all must pass):
   HARD_1: id matches pattern ^p12_wp_[a-z][a-z0-9_]+$
   HARD_2: kind == "workflow_primitive"
   HARD_3: type is one of: step, condition, loop, parallel, router, gate, merge
   HARD_4: inputs is non-empty list with typed entries
   HARD_5: outputs is non-empty list with typed entries
   HARD_6: loop type has max_iter > 0 and <= 100
   HARD_7: parallel type has merge_ref pointing to a merge primitive
   HARD_8: gate type has numeric threshold
   HARD_9: quality == null
   HARD_10: YAML parses without syntax errors
   HARD_11: total YAML size <= 4096 bytes
   HARD_12: no full workflow graph or DAG in the primitive
2. Scope check:
   Verify primitive is atomic: one type, one operation
   Verify primitive contains no signal payloads or handoff instructions
   Verify composition metadata is consistent with type
3. If all HARD gates pass: emit file
   If any HARD gate fails: return to Phase 2 with failure reasons
OUTPUT: validated workflow_primitive YAML file
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_workflow_primitive]] | upstream | 0.58 |
| [[p03_sp_workflow_primitive_builder]] | related | 0.55 |
| [[bld_output_template_workflow_primitive]] | downstream | 0.54 |
| [[p11_qg_workflow_primitive]] | downstream | 0.53 |
| [[bld_config_workflow_primitive]] | downstream | 0.52 |
| [[bld_schema_workflow_primitive]] | downstream | 0.52 |
| [[workflow-primitive-builder]] | downstream | 0.52 |
| [[bld_examples_workflow_primitive]] | downstream | 0.49 |
| [[bld_architecture_workflow_primitive]] | downstream | 0.48 |
| [[bld_collaboration_workflow_primitive]] | upstream | 0.46 |
