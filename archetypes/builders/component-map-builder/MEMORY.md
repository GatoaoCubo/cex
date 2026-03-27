---
id: p10_lr_component_map_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Component maps that listed orphan components (present in the component table but absent from connections) provided false confidence about system boundaries. In 4 of 6 architecture reviews, orphan components concealed undocumented dependencies that caused production incidents."
pattern: "Every component in the map must appear in at least one connection. Use explicit direction annotations on all connections. Scope to 3-15 components per map; split at 15."
evidence: "6 architecture reviews: 4 had orphan components that concealed undocumented dependencies. After enforcing the no-orphan rule, all 4 systems revealed hidden dependencies on first validation pass."
confidence: 0.7
outcome: SUCCESS
domain: component_map
tags: [component-map, architecture, orphan-detection, connection-direction, scope-boundary]
tldr: "No orphan components. Every component must appear in at least one connection. Explicit direction on all connections. Split scope at 15 components."
impact_score: 7.5
decay_rate: 0.05
satellite: edison
keywords: [component map, architecture mapping, orphan detection, connection direction, data flow, dependency, scope boundary, ownership]
---

## Summary

A component map's value is making hidden dependencies visible. Orphan components — listed in the component table but absent from connections — destroy that value. Orphans signal either truly isolated components (rare, annotate explicitly) or omitted connections (common, dangerous).

The second most common failure is undirected connections ("A relates to B"): structural information without operational information. Direction is what makes a map reasoned from vs. merely looked at.

## Pattern

**No orphans. Explicit direction. Bounded scope.**

No-orphan rule: after writing both the component table and the connection table, verify every component_id in the component table appears at least once as source or target in the connection table. Any component with no connections must be annotated explicitly as `isolated: true` with a justification.

Connection direction types:
- data_flow: data moves from source to target (A sends records to B)
- dependency: source cannot function without target (A requires B to be running)
- signal: source sends event/trigger to target (A emits events consumed by B)
- produces: source creates target as output artifact (A generates B)
- consumes: source reads or uses target (A reads from B)

Scope boundary rules:
- 3-15 components per map. Fewer than 3: use a satellite spec instead. More than 15: split by domain.
- Scope statement must name what is explicitly excluded, not just what is included.
- Right-size example: "Brain search infrastructure: indexing, embedding, retrieval. Excludes: UI layer, API routing, authentication."

Component table required columns: id, name, type, owner, description (one sentence). No prose beyond the table.

## Anti-Pattern

- Orphan components without `isolated: true` annotation (conceals dependencies).
- Undirected connections without type annotation (structurally present, operationally useless).
- Scope too broad ("the whole system") — split by domain.
- Scope too narrow ("just the BM25 index") — use a spec for single-component documentation.
- Prose connections instead of a table (kills density; S08 fail).
- Confusing component map (structured data) with diagram (visual rendering).
- component_count not matching actual table rows (H06 fail).

## Context

Orphan detection emerged from maps where components were listed to signal existence without documenting connections — creating false completeness while hiding the actual dependency graph.

Ownership column is required for incident response: knowing who owns a component halves time-to-contact when it is implicated in a failure. Health status column (optional): current, degraded, deprecated, unknown — doubles as a live dashboard when kept current.

Component_map vs. diagram decision: ask "is this data or a picture?" If you need to query it (all components owned by team X, all data_flow connections to component Y), use component_map. If you need to present it visually, use diagram.

## Impact

A map with the no-orphan rule enforced provides a complete, queryable dependency graph. Primary uses: impact analysis before changes, incident response (upstream/downstream of failing component), and onboarding. Highest impact for systems with 5+ components across multiple teams. Lower for single-team services where architecture is held in shared memory.

## Reproducibility

Applies to any architecture regardless of stack. No-orphan validation: `set(component_ids) - set(source_ids | target_ids)` must equal only explicitly isolated components. The 3-15 scope limit is a guideline; adjust based on consumer cognitive load.

## References

- Builder domain: component_map, P08
- Related builders: diagram-builder (visual), satellite-spec-builder (single component)
- Scope heuristic: MEMORY.md > Scope Scoping Heuristics (existing)
- Connection types: MEMORY.md > Connection Type Decision (existing)
