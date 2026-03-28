---
kind: schema
id: bld_schema_director
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for director artifacts
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: director
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p08_dir_{name}) | YES | - | Namespace compliance |
| kind | literal "director" | YES | - | Type integrity |
| pillar | literal "P08" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Director name (kebab-case) |
| mission | string | YES | - | What this crew accomplishes |
| entry_point | string | YES | - | First builder invoked (builder id) |
| exit_point | string | YES | - | Final output builder (builder id) |
| builders | list[string] | YES | - | All builder ids in this crew |
| dag_edges | list[object] | YES | - | Directed edges: {from, to, data} |
| parallelism | object or null | REC | null | Parallel groups and sequence constraints |
| handoff_contracts | list[object] | REC | [] | Data contracts between builder pairs |
| failure_handling | list[object] | REC | [] | Per-builder fallback strategies |
| constraints | list[string] | REC | [] | Crew-level operational limitations |
| dependencies | list[string] | REC | [] | External services required by the crew |
| estimated_duration | string or null | REC | null | Expected wall-clock time for full crew run |
| domain | string | YES | - | Domain this artifact belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "director" |
| tldr | string <= 160ch | YES | - | Dense summary |
## Complex Objects
```yaml
dag_edges:
  - from: string          # builder id of source
    to: string            # builder id of target
    data: string          # description of data passed

parallelism:
  parallel_groups:        # list of lists — builders in same group run concurrently
    - [builder_a, builder_b]
  must_sequence:          # list of pairs — first must complete before second starts
    - [builder_c, builder_d]

handoff_contracts:
  - from: string          # source builder id
    to: string            # target builder id
    schema: string        # data type or field description passed
    required: boolean     # whether target requires this input to proceed

failure_handling:
  - builder: string       # builder id
    strategy: string      # skip | retry | abort_crew | fallback_to
    fallback: string      # fallback builder id if strategy is fallback_to
```
## ID Pattern
Regex: `^p08_dir_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Crew Composition` — table of all builders with role, input, output, and sequence position
2. `## DAG Structure` — directed graph with edges and data flow
3. `## Handoff Protocol` — data contracts for each connected pair
4. `## Parallelism Rules` — concurrent groups and sequencing constraints
5. `## Failure Handling` — per-builder fallback and crew-level recovery
6. `## Entry and Exit` — entry_point and exit_point with acceptance criteria
7. `## Constraints` — operational NEVER rules for the crew
## Constraints
- max_bytes: 4096 (body only)
- naming: p08_dir_{name_lower}.md
- machine_format: yaml frontmatter + markdown body
- id == filename stem
- mission MUST describe the crew's outcome
- entry_point MUST be a valid builder id in builders list
- exit_point MUST be a valid builder id in builders list
- dag_edges MUST form a valid DAG (no cycles)
- quality: null always
