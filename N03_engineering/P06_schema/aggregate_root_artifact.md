---
quality: 8.6
quality: 8.2
id: p06_ar_artifact
kind: aggregate_root
8f: F4_reason
pillar: P06
title: "Aggregate Root: Artifact"
version: 0.1.0
bounded_context: "KnowledgeProduction"
invariants:
  - "quality MUST be null until peer review assigns a numeric score via cex_score.py"
  - "id MUST match the naming pattern defined in the kind's pillar _schema.yaml"
  - "kind MUST exist in .cex/kinds_meta.json at creation time"
  - "frontmatter MUST include: id, kind, pillar, version, quality, tags, tldr"
commands:
  - "ProduceArtifact: precondition=8F pipeline COMPLETE, postcondition=artifact file exists with valid frontmatter"
  - "ScoreArtifact: precondition=peer reviewer identity known AND quality==null, postcondition=quality set to float 0.0-10.0"
  - "PublishArtifact: precondition=quality >= 8.0, postcondition=artifact committed and compiled"
  - "RetireArtifact: precondition=artifact exists, postcondition=moved to archive/, status=retired"
domain_events:
  - "ArtifactProduced: emitted when ProduceArtifact completes, payload={id, kind, pillar, path, author}"
  - "ArtifactScored: emitted when ScoreArtifact completes, payload={id, score, dimensions, reviewer}"
  - "ArtifactPublished: emitted when PublishArtifact completes, payload={id, commit_sha}"
  - "ArtifactRetired: emitted when RetireArtifact completes, payload={id, archive_path}"
repository: "ArtifactRepository"
cluster_members:
  - "Frontmatter (value_object)"
  - "Body (value_object)"
  - "QualityScore (value_object) -- see value_object_quality_score.md"
  - "Tag (value_object, collection)"
identity_type: slug
concurrency_strategy: optimistic
tags: [aggregate_root, artifact, knowledge_production, P06, ddd]
tldr: "Artifact aggregate root: owns 4 cluster members (Frontmatter, Body, QualityScore, Tags), enforces 4 invariants, emits 4 domain events."
related:
  - SPEC_05_skills_runtime
  - p01_kc_pydantic_patterns
  - bld_examples_repo_map
  - p03_sp_n03_creation_nucleus
  - p12_sig_builder_nucleus
  - p06_is_creation_data
  - skill
  - p01_kg_cex_system_architecture
  - bld_architecture_kind
  - p05_fmt_knowledge_report
density_score: 1.0
updated: "2026-04-22"
---

# Aggregate Root: Artifact

The central domain entity in CEX's KnowledgeProduction bounded context.
An Artifact is the atomic output unit of the 8F pipeline: one kind, one pillar,
one set of invariants that must never be violated regardless of which nucleus produces it.

## Identity

**Root entity**: Artifact
**Bounded context**: KnowledgeProduction
**Cluster members**: Frontmatter (value_object), Body (value_object), QualityScore (value_object), Tag (collection of value_object)
**Identity field**: `id` (slug string, e.g., `p06_ar_artifact`)
**Identity type**: slug (human-readable, kind-scoped, unique within pillar)

## Invariants

1. `quality` MUST be null until peer review assigns a score via `cex_score.py --apply`. A nucleus NEVER self-scores.
2. `id` MUST match the naming pattern from `N00_genesis/P{xx}/_schema.yaml` for the artifact's pillar (e.g., `p06_ar_*` for aggregate_root in P06).
3. `kind` MUST exist as a key in `.cex/kinds_meta.json` at the moment ProduceArtifact is called.
4. Frontmatter MUST contain the required fields: `id`, `kind`, `pillar`, `version`, `quality`, `tags`, `tldr`.

## Commands

### ProduceArtifact(intent, nucleus_id, builder_path)
- Precondition: 8F pipeline has reached F6 PRODUCE; builder ISOs loaded; context assembled
- Postcondition: artifact file written to correct pillar directory; ArtifactProduced emitted
- Emits: `ArtifactProduced`

### ScoreArtifact(reviewer_id, score, dimensions)
- Precondition: quality == null; reviewer_id is a known peer nucleus or CI bot
- Postcondition: quality set to float in [0.0, 10.0]; ArtifactScored emitted
- Emits: `ArtifactScored`

### PublishArtifact(commit_message)
- Precondition: quality >= 8.0; artifact compiled (cex_compile.py returns 0)
- Postcondition: artifact committed to git; ArtifactPublished emitted
- Emits: `ArtifactPublished`

### RetireArtifact(reason)
- Precondition: artifact exists at current path
- Postcondition: file moved to archive/; status field updated to "retired"
- Emits: `ArtifactRetired`

## Domain Events

### ArtifactProduced
- Trigger: ProduceArtifact command
- Payload: `{id: str, kind: str, pillar: str, path: str, author: str, timestamp: RFC3339}`

### ArtifactScored
- Trigger: ScoreArtifact command
- Payload: `{id: str, score: float, dimensions: {D1: float, D2: float, D3: float, D4: float, D5: float}, reviewer: str}`

### ArtifactPublished
- Trigger: PublishArtifact command
- Payload: `{id: str, commit_sha: str, path: str}`

### ArtifactRetired
- Trigger: RetireArtifact command
- Payload: `{id: str, archive_path: str, reason: str}`

## Repository

Interface: `ArtifactRepository`
- `find_by_id(id: str) -> Optional[Artifact]`
- `find_by_kind(kind: str) -> List[Artifact]`
- `find_below_quality(threshold: float) -> List[Artifact]`
- `save(artifact: Artifact) -> void`
- `delete(id: str) -> void`

Implementation: file system under `N{nucleus}/P{xx}_{domain}/` + `.cex/kinds_meta.json` index

## Boundaries

**Inside cluster**: Frontmatter, Body, QualityScore, Tag collection
**Outside (referenced by ID only)**: Builder (lives in archetypes/builders/), Nucleus (lives in N0X_domain/)

## References

- Quality scoring: `_tools/cex_score.py`
- Compiler: `_tools/cex_compile.py`
- Kind registry: `.cex/kinds_meta.json`
- QualityScore value object: `N03_engineering/P06_schema/value_object_quality_score.md`
- NucleusSignal event: `N03_engineering/P06_schema/event_schema_nucleus_signal.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[SPEC_05_skills_runtime]] | upstream | 0.32 |
| [[p01_kc_pydantic_patterns]] | upstream | 0.29 |
| [[bld_examples_repo_map]] | downstream | 0.25 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.23 |
| [[p12_sig_builder_nucleus]] | downstream | 0.23 |
| [[p06_is_creation_data]] | related | 0.23 |
| [[skill]] | downstream | 0.21 |
| [[p01_kg_cex_system_architecture]] | upstream | 0.21 |
| [[bld_architecture_kind]] | downstream | 0.20 |
| [[p05_fmt_knowledge_report]] | upstream | 0.20 |
