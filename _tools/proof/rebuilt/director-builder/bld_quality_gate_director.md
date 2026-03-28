---
id: p11_qg_director
kind: quality_gate
pillar: P11
title: "Gate: Director"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: EDISON
domain: crew_orchestration
quality: null
density_score: 0.85
tags:
  - quality-gate
  - director
  - crew-orchestration
  - p11
tldr: "Gates ensuring director files define a fully orchestratable crew with mission, DAG, handoff contracts, entry/exit anchors, and failure handling."
---

## Definition
A director describes a fully orchestratable multi-builder crew: its mission outcome, the DAG connecting participating builders, the data contracts between them, which builders run in parallel, how failures are handled, and which builder starts and which produces the final output. A director passes this gate when any operator could launch and monitor the full crew from the document alone, without consulting the author.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`director-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `director` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, version, created, updated, author, name, mission, entry_point, exit_point, builders, dag_edges, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | `mission` is a non-empty string describing one crew outcome | Without mission, operators cannot determine if the crew is appropriate for a task |
| H08 | `entry_point` names a builder id present in the `builders` list | Entry point outside the builders list creates a dangling reference |
| H09 | `exit_point` names a builder id present in the `builders` list | Exit point outside the builders list means the crew has no defined output |
| H10 | `dag_edges` form a valid acyclic graph (topological sort succeeds with no cycles) | Cyclic edges produce infinite loops; crew never terminates |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Handoff contracts documented (data type per dag_edge) | 1.0 | No contracts listed | Some edges have contracts | Every dag_edge has a named schema and required flag |
| 3 | Failure handling present (per-builder strategy defined) | 1.0 | No failure handling | Some builders covered | Every builder has strategy; entry uses abort_crew |
| 4 | Parallelism rules defined (concurrent groups and forced sequences) | 0.5 | No mention | Single sequential path only | Parallel groups identified; must_sequence pairs listed |
| 5 | Monitoring configuration (completion signal, alerting) | 1.0 | No monitoring | Logs only | Completion signal on exit_point + failure alert defined |
| 6 | Tags include `director` | 0.5 | Missing | Present but misspelled | Exactly `director` in tags list |
| 7 | Builder boundary explicit (what each builder does and does not handle in this crew) | 1.0 | No boundaries | Implicit in examples | Explicit role per builder in crew composition table |
| 8 | Handoff data types specific with field names or schema reference | 1.0 | None listed | Type names only | Type names + required flag + field list per handoff |
