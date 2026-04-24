---
quality: 8.0
quality: 7.6
id: p06_vo_quality_score
kind: value_object
8f: F4_reason
pillar: P06
title: "Value Object: QualityScore"
version: 0.1.0
attributes:
  - name: "value"
    type: "float"
    constraint: "0.0 <= value <= 10.0; two decimal places max; null NOT permitted after scoring"
  - name: "dimensions"
    type: "dict[str, float]"
    constraint: "keys must be D1-D5; each value in [0.0, 10.0]; all 5 keys required"
  - name: "scored_by"
    type: "str"
    constraint: "non-empty; identifies the scoring agent or tool (e.g., 'n04_peer', 'cex_score.py')"
equality: structural
used_in:
  - "Artifact (aggregate_root -- N03_engineering/P06_schema/aggregate_root_artifact.md)"
transformations:
  - "withDimension(dim: str, score: float) -> QualityScore: returns new instance with updated dimension score and recalculated value"
  - "normalize() -> QualityScore: returns new instance with value clamped to [0.0, 10.0] if float precision drift occurred"
hashable: true
tags: [value_object, quality_score, P06, ddd, cex, scoring]
tldr: "QualityScore: immutable value defined by value(float) + dimensions(D1-D5) + scored_by, structural equality, used in Artifact aggregate root."
related:
  - bld_knowledge_card_scoring_rubric
  - p11_qg_scoring-rubric
  - p01_qg_reranker_config
  - p11_qg_enum_def
  - p08_ac_verification
  - p01_kc_artifact_quality_evaluation_methods
  - p11_qg_creation_artifacts
  - p11_qg_entity_memory
  - quality-gate-builder
  - bld_collaboration_quality_gate
density_score: 1.0
updated: "2026-04-22"
---

# Value Object: QualityScore

Immutable record of an artifact's peer-review quality assessment.
Produced by `_tools/cex_score.py --apply` during F7 GOVERN or post-production peer review.
A QualityScore instance is NEVER produced by the artifact's own nucleus (no self-scoring).

## Attributes

| Attribute | Type | Constraint | Valid Example | Invalid Example |
|-----------|------|-----------|---------------|-----------------|
| value | float | 0.0 <= v <= 10.0, max 2 decimal places | 8.75 | 10.5 or -1.0 |
| dimensions | dict[str,float] | keys={D1,D2,D3,D4,D5}, each in [0.0,10.0] | {D1:9.0, D2:8.5, D3:8.0, D4:9.0, D5:9.5} | {D1:9.0} (missing D2-D5) |
| scored_by | str | non-empty, identifies reviewer | "n04_peer" | "" (empty string) |

## Dimension Map

| Dimension | Weight | Meaning |
|-----------|--------|---------|
| D1 | 20% | Structural completeness (frontmatter fields, sections) |
| D2 | 20% | Rubric compliance (builder quality gates H01-H07) |
| D3 | 20% | Semantic density (information per byte ratio) |
| D4 | 20% | Cross-reference accuracy (referenced artifacts exist) |
| D5 | 20% | Domain correctness (kind-specific correctness criteria) |

**Weighted formula**: `value = (D1*0.2 + D2*0.2 + D3*0.2 + D4*0.2 + D5*0.2)`

## Equality

Two `QualityScore` instances are equal if and only if all three attributes are equal:
`value`, `dimensions` (all 5 keys with identical float values), and `scored_by`.
No identity field. Reference equality is NOT domain equality.

## Validation

**Valid**: `QualityScore(value=9.0, dimensions={D1:9.0,D2:9.0,D3:9.0,D4:9.0,D5:9.0}, scored_by="n04_peer")`
**Invalid**: `QualityScore(value=11.0, ...)` -- violates 0.0-10.0 constraint on `value`
**Invalid**: `QualityScore(value=9.0, dimensions={D1:9.0}, scored_by="n03")` -- missing D2-D5
**Invalid**: `QualityScore(value=9.0, dimensions={...}, scored_by="")` -- empty scored_by
**Invalid (self-scoring)**: `scored_by="n03"` on artifact produced by N03 -- policy violation, not type constraint

## Transformations

- `withDimension("D3", 9.5)` -> new `QualityScore` with updated D3 and recalculated value: `QualityScore(value=8.9, dimensions={..., D3:9.5}, scored_by="n04_peer")`
- `normalize()` -> new `QualityScore` with value clamped to [0.0, 10.0]: guards against float summation drift beyond bounds

## Usage

Used as the `quality` field in Artifact aggregate root. Before scoring:
`quality: null` in frontmatter (YAML null, not the string "null").
After scoring:
`quality: 9.0` (float) -- the `value` attribute of QualityScore is serialized directly.
Full QualityScore (with dimensions) stored in `.cex/runtime/scores/{artifact_id}.json`.

## References

- Scoring tool: `_tools/cex_score.py`
- Quality monitor: `_tools/cex_quality_monitor.py`
- Aggregate root: `N03_engineering/P06_schema/aggregate_root_artifact.md`
- Quality floor: 8.0 (publish gate); quality target: 9.0+ (CEX standard)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_scoring_rubric]] | upstream | 0.24 |
| [[p11_qg_scoring-rubric]] | downstream | 0.23 |
| [[p01_qg_reranker_config]] | downstream | 0.22 |
| [[p11_qg_enum_def]] | downstream | 0.22 |
| [[p08_ac_verification]] | downstream | 0.21 |
| [[p01_kc_artifact_quality_evaluation_methods]] | upstream | 0.20 |
| [[p11_qg_creation_artifacts]] | downstream | 0.20 |
| [[p11_qg_entity_memory]] | downstream | 0.19 |
| [[quality-gate-builder]] | downstream | 0.19 |
| [[bld_collaboration_quality_gate]] | downstream | 0.19 |
