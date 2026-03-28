---
id: p03_ins_director_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Director Builder Instructions
target: director-builder agent
phases_count: 4
prerequisites:
  - Mission is defined (non-empty string describing what the crew accomplishes)
  - At least two builder ids are identified
  - Data flow direction between builders is known
  - Entry point and exit point builders are specified
validation_method: checklist
domain: crew_orchestration
quality: null
tags: [instruction, crew-orchestration, architecture, P08]
idempotent: true
atomic: false
rollback: Delete generated director file and restart from Phase 1
dependencies: []
logging: true
tldr: Build a complete director covering crew composition, DAG structure, handoff contracts, parallelism rules, failure handling, and entry/exit anchoring.
density_score: 0.91
---

## Context
The director-builder produces `director` artifacts — complete orchestration specifications
for multi-builder crews. A director defines everything needed to coordinate a set of builders:
which builders participate, in what DAG order they execute, what data passes between them,
which can run in parallel, and how failures are handled.
**Input contract**:
- `{{mission}}`: one-sentence description of what the crew produces (e.g. `generate a satellite spec with system prompt and diagram`)
- `{{builders}}`: comma-separated list of builder ids (e.g. `mental-model-builder, satellite-spec-builder, system-prompt-builder`)
- `{{entry_point}}`: first builder invoked (must be in builders list)
- `{{exit_point}}`: final output builder (must be in builders list)
- `{{constraints_raw}}`: free-text description of crew-level operational boundaries
**Output contract**: A single `director` Markdown file with 24+ frontmatter fields,
a crew composition table, DAG diagram, handoff contracts, parallelism rules, failure strategies,
and entry/exit anchors.
**Boundaries**:
- Handles crew coordination only.
- Individual builder logic belongs in the builder's own identity files.
- Satellite architecture belongs in satellite_spec artifacts.
- Reusable coordination patterns belong in pattern artifacts.
## Phases
### Phase 1: Analyze Mission and Builder Roster
**Primary action**: Define the crew's mission outcome and enumerate all participating builders
with their roles.
```
INPUT: mission, builders[], entry_point, exit_point
1. Express the crew's single mission outcome:
   mission_statement = "This crew produces [ONE DELIVERABLE]"
   Reject vague missions like "do stuff" or "help the user"
2. For each builder in builders[]:
   builder_entry = {
     id: builder_id,
     role: "what this builder contributes to the mission",
     input_type: "what data it receives",
     output_type: "what data it produces"
   }
3. Validate entry_point and exit_point:
   - entry_point MUST be in builders[]
   - exit_point MUST be in builders[]
   - entry_point has no incoming edges
   - exit_point has no outgoing edges
4. Extract coordination_keywords (5-10 terms) from mission description.
OUTPUT: mission_statement, builder_roster[], entry_point, exit_point, coordination_keywords[]
```
Verification: `mission_statement` is one sentence. `builder_roster` has >= 2 entries. Both anchors validated.
### Phase 2: Design DAG and Parallelism
**Primary action**: Map directed edges between builders and identify which builder groups
can execute concurrently.
```
INPUT: builder_roster[], entry_point, exit_point
1. For each pair of builders where one depends on the other:
   dag_edge = {
     from: source_builder_id,
     to: target_builder_id,
     data: "description of what is passed"
   }
2. Verify DAG has no cycles:
   - Topological sort must succeed
   - Any cycle = invalid crew design; must restructure
3. Identify parallel groups:
   parallel_groups = []
   for each level in topological sort:
     if level has > 1 builder with no mutual dependency:
       parallel_groups.append(level_builders)
4. Identify forced sequences:
   must_sequence = []
   for each edge where output of A is required input of B:
     must_sequence.append([A, B])
OUTPUT: dag_edges[], parallel_groups[], must_sequence[], topological_order[]
```
Verification: DAG is acyclic. `dag_edges` covers all builder dependencies. At least one edge defined.
### Phase 3: Define Handoffs and Failure Handling
**Primary action**: Specify the data contracts between connected builder pairs and the
fallback strategy for each builder that can fail.
```
INPUT: dag_edges[], builder_roster[]
1. Handoff contracts (one per dag_edge):
   handoff = {
     from: source_builder_id,
     to: target_builder_id,
     schema: "type or fields passed (e.g. satellite_spec YAML, system_prompt Markdown)",
     required: true | false
   }
2. Failure handling (one per builder):
   failure_entry = {
     builder: builder_id,
     strategy: "skip" | "retry" | "abort_crew" | "fallback_to",
     fallback: null | fallback_builder_id,
     max_retries: integer (default 1)
   }
   Rules:
   - entry_point failure: strategy = abort_crew (crew cannot proceed without entry)
   - exit_point failure: strategy = retry (output is the crew's deliverable)
   - intermediate builder: strategy = skip if output is optional, abort_crew if required
3. Crew-level constraints from constraints_raw:
   for each sentence in constraints_raw:
     if NEVER/MUST NOT/FORBIDDEN -> hard_constraint
     if PREFER/AVOID/MINIMIZE    -> soft_constraint
OUTPUT: handoff_contracts[], failure_handling[], hard_constraints[], soft_constraints[]
```
Verification: one handoff per dag_edge. One failure_handling entry per builder. entry_point uses abort_crew.
### Phase 4: Assemble and Validate Artifact
**Primary action**: Combine all phase outputs into the final director Markdown file and run
quality gates.
```
INPUT: all outputs from Phases 1-3
1. Assemble frontmatter with 24+ required fields (id, kind, pillar, version,
   created, updated, author, name, mission, entry_point, exit_point,
   builders[], dag_edges[], parallelism{}, handoff_contracts[], failure_handling[],
   constraints[], dependencies[], estimated_duration, domain, quality, tags, tldr)
2. Write body sections in order:
   ## Crew Composition   (builder_roster table)
   ## DAG Structure      (edges + mermaid or text graph)
   ## Handoff Protocol   (handoff_contracts table)
   ## Parallelism Rules  (parallel_groups + must_sequence)
   ## Failure Handling   (failure_handling table)
   ## Entry and Exit     (entry_point + exit_point with criteria)
   ## Constraints        (hard_constraints list)
3. Run HARD gates H01-H10. Fail = restart relevant phase.
4. Run SOFT scoring S01-S08. Score < 7.0 = revise before delivery.
5. Set quality: null (gate assigns score, not author).
OUTPUT: complete director artifact file, gate_results[], soft_score
```
Verification: all 7 body sections present. `quality: null`. YAML frontmatter parses. `id` matches filename stem.
