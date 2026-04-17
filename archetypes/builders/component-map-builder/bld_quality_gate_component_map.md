---
id: p11_qg_component_map
kind: quality_gate
pillar: P11
title: "Gate: component_map"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "system component inventory — structured catalogs of components, connections, dependencies, and data flows"
quality: 9.0
tags: [quality-gate, component-map, P08, inventory, architecture, dependency-mapping]
tldr: "Pass/fail gate for component_map artifacts: component completeness, connection accuracy, interface boundary documentation, and inventory scope."
density_score: 0.90
llm_function: GOVERN
---
# Gate: component_map
## Definition
| Field | Value |
|---|---|
| metric | component_map artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: component_map` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | `id: my_map` but file is `other_map.md` |
| H04 | Kind equals literal `component_map` | `kind: diagram` or `kind: architecture` or any other value |
| H05 | Quality field is null | `quality: 8.5` or any non-null value |
| H06 | All required fields present | Missing `components`, `connections`, or `scope` |
| H07 | At least two components defined | Single-component map is a agent_card, not a component_map |
| H08 | Each connection references valid component IDs | Connection references a component ID not listed in components |
| H09 | Scope boundary declared | `scope` field absent or empty; map must state what system boundary it covers |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Component completeness | 1.0 | All components within the declared scope boundary are inventoried |
| Connection accuracy | 1.0 | Connections reflect actual data or control flow; direction (A->B vs B->A) correct |
| Interface boundary clarity | 1.0 | Each component's public interface (API surface, events, data contracts) documented |
| Dependency direction | 1.0 | Dependency edges are directional and semanticslly labeled (calls, subscribes, reads) |
| Ownership documentation | 0.5 | Each component has an owner (team, service, person) assigned |
| Health status inclusion | 0.5 | Component health or operational status noted where known |
| Data flow labeling | 1.0 | Connections labeled with data type or payload schema, not just arrows |
| External dependency marking | 0.5 | External services or components distinguished from internal ones |
| Scope fence completeness | 1.0 | Map explicitly lists what is OUT of scope, not just what is in scope |
| Freshness metadata | 0.5 | Map includes `as_of` date or version reference for accuracy tracking |
| Visual parity potential | 0.5 | Structure sufficiently detailed that a diagram could be generated from it |
| Domain specificity | 1.0 | Component names, interfaces, and connections specific to the declared system |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Map created during active system migration where component inventory is in flux |
| approver | Architecture owner acknowledgment with migration ticket reference |
| audit_trail | Bypass reason, migration ticket ID, and expected stable date in frontmatter comment |
| expiry | 21d — map must reach >= 7.0 or be updated once migration phase complete |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics) |
