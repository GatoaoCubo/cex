---
kind: examples
id: bld_examples_director
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of director artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: director-builder
## Golden Example
INPUT: "Orquestra um crew para onboarding de novo satelite: mental-model-builder, satellite-spec-builder, system-prompt-builder"
OUTPUT:
```yaml
id: p08_dir_satellite_onboarding
kind: director
pillar: P08
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
name: "satellite-onboarding"
mission: "Produce a fully specified autonomous satellite with mental model, spec, and system prompt"
entry_point: "mental-model-builder"
exit_point: "system-prompt-builder"
builders: [mental-model-builder, satellite-spec-builder, system-prompt-builder]
dag_edges:
  - from: "mental-model-builder"
    to: "satellite-spec-builder"
    data: "domain map and cognitive constraints"
  - from: "satellite-spec-builder"
    to: "system-prompt-builder"
    data: "satellite_spec YAML with role, model, MCPs, and constraints"
parallelism:
  parallel_groups: []
  must_sequence:
    - [mental-model-builder, satellite-spec-builder]
    - [satellite-spec-builder, system-prompt-builder]
handoff_contracts:
  - from: "mental-model-builder"
    to: "satellite-spec-builder"
    schema: "mental_model YAML: domain_map, personality, cognitive_constraints"
    required: true
  - from: "satellite-spec-builder"
    to: "system-prompt-builder"
    schema: "satellite_spec YAML: role, model, mcps, constraints, dispatch_keywords"
    required: true
failure_handling:
  - builder: "mental-model-builder"
    strategy: "abort_crew"
    fallback: null
  - builder: "satellite-spec-builder"
    strategy: "retry"
    fallback: null
  - builder: "system-prompt-builder"
    strategy: "retry"
    fallback: null
constraints:
  - "NEVER skip mental-model-builder — satellite-spec-builder requires domain map as input"
  - "NEVER run system-prompt-builder before satellite-spec-builder completes"
  - "NEVER self-assign quality score — quality: null always"
dependencies: [brain_mcp]
estimated_duration: "15-25 minutes"
domain: "crew_orchestration"
quality: null
tags: [director, crew-orchestration, satellite-onboarding, P08]
tldr: "Satellite onboarding crew: mental-model -> satellite-spec -> system-prompt, fully sequenced with handoff contracts."
```
## Crew Composition
| Builder | Role | Input | Output | Sequence |
|---------|------|-------|--------|----------|
| mental-model-builder | Define satellite domain map and personality | satellite name + domain description | mental_model YAML | 1 |
| satellite-spec-builder | Produce full satellite spec | mental_model YAML | satellite_spec YAML | 2 |
| system-prompt-builder | Author satellite system prompt | satellite_spec YAML | system_prompt Markdown | 3 |
## DAG Structure
```
mental-model-builder
  --[domain map + constraints]--> satellite-spec-builder
                                    --[satellite_spec YAML]--> system-prompt-builder
```
All edges are required. No parallel execution in this crew.
## Handoff Protocol
- mental-model-builder -> satellite-spec-builder: `mental_model YAML` (required). Fields: domain_map, personality, cognitive_constraints.
- satellite-spec-builder -> system-prompt-builder: `satellite_spec YAML` (required). Fields: role, model, mcps, constraints, dispatch_keywords.
## Parallelism Rules
All builders must sequence. No parallel groups. Each builder waits for the previous builder's output before starting.
## Failure Handling
- mental-model-builder: abort_crew (crew cannot proceed without domain map)
- satellite-spec-builder: retry once (spec is recoverable; abort if retry fails)
- system-prompt-builder: retry once (final output; abort if retry fails)
## Entry and Exit
- Entry: mental-model-builder. Acceptance: satellite name and domain provided by caller.
- Exit: system-prompt-builder. Acceptance: system_prompt Markdown <= 4096 bytes, quality: null.
## Constraints
- NEVER skip mental-model-builder — satellite-spec-builder requires domain map as input
- NEVER run system-prompt-builder before satellite-spec-builder completes
- NEVER self-assign quality score — quality: null always
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p08_dir_ pattern (H02 pass)
- kind: director (H04 pass)
- 24 frontmatter fields present (H06 pass)
- mission non-empty (H07 pass)
- entry_point and exit_point valid (H08-H09 pass)
- dag_edges form valid acyclic graph (H10 pass)
- YAML parses cleanly (H01 pass)
- id == filename stem (H03 pass)
- tldr <= 160 chars (S01 pass)
- tags list len >= 3 (S02 pass)
- All 7 body sections present (S03-S09 pass)
## Anti-Example
INPUT: "Define satellite onboarding crew"
BAD OUTPUT:
```yaml
id: onboarding_crew
kind: crew
pillar: Architecture
mission: Help onboard satellites
builders: mental-model-builder, satellite-spec-builder
quality: 9.0
```
WHY THIS FAILS:
- id does not match p08_dir_ pattern (H02 fail)
- kind is "crew" not "director" (H04 fail)
- quality self-assigned as 9.0 (H05 fail)
- mission is vague "Help onboard satellites" (H07 borderline)
- builders is a string, not a list (H06 fail)
- Missing entry_point, exit_point, dag_edges (H08-H10 fail)
- No body sections present
