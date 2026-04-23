---
id: p03_fse_schema_design
kind: few_shot_example
pillar: P03
title: "Few-Shot Example -- P06 Schema Design via 8F"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: schema-design
quality: 8.7
tags: [few_shot_example, P06, schema, type_def, input_schema, validation_schema, 8F, coc]
tldr: "Input/output pair demonstrating how N03 applies 8F to P06 schema design. Covers type_def, input_schema, and validation_schema in one cohesive example. Reusable by any LLM runtime for schema-kind builds."
density_score: 0.89
related:
  - p06_vs_frontmatter
  - bld_schema_reranker_config
  - bld_schema_prompt_compiler
  - bld_schema_kind
  - bld_schema_integration_guide
  - bld_schema_thinking_config
  - bld_schema_input_schema
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
  - bld_schema_voice_pipeline
---

# Few-Shot Example: P06 Schema Design

> **Usage:** Inject this artifact at F3 INJECT when building any P06 schema kind. It demonstrates the complete reasoning pattern from intent to validated artifact.

---

## Example 1: type_def via Template-First

### INPUT

```
User: "define a type for artifact metadata"
Context: N03_engineering, pillar P06, schema domain
```

### REASONING (8F abbreviated)

```
F1: kind=type_def, pillar=P06, nucleus=N03
    schema: N00_genesis/P06_schema/_schema.yaml
    max_bytes: 2048

F2: type-def-builder loaded (13 ISOs)
    sin_lens: Inventive Pride (precision of types reflects pride in contracts)

F3: template match -> type_def_cex_types.md (similarity: 78%)
    approach: Template-First (>= 60%)
    injected: kc_engineering_vocabulary.md, type_def_cex_types.md

F4: sections: TypeDef, Fields table, Constraints, Usage
    approach: Template-First (adapt type_def_cex_types.md)

F7: H01-H07 all pass, density=0.87, score=9.1
```

### OUTPUT

```markdown
---
id: p06_td_artifact_metadata
kind: type_def
pillar: P06
title: "Type -- ArtifactMetadata"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: schema
quality: null
tags: [type_def, artifact, metadata, frontmatter]
tldr: "Structural type for CEX artifact frontmatter. Enforces required fields, type constraints, and naming conventions across all 257 kinds."
density_score: 0.87
---

# Type: ArtifactMetadata

## TypeDef

```typescript
interface ArtifactMetadata {
  id: string           // pattern: p{pillar}_{prefix}_{slug}
  kind: KindName       // enum: 257 values from kinds_meta.json
  pillar: PillarCode   // enum: P01-P12
  title: string        // max: 120 chars
  version: SemVer      // pattern: /^\d+\.\d+\.\d+$/
  created: ISODate     // format: YYYY-MM-DD
  author: string       // nucleus id or username
  domain: string       // kebab-case domain tag
  quality: null | float // null (produced) or 0-10 (scored by peer)
  tags: string[]       // min: 2, all lowercase, kebab-case
  tldr: string         // max: 160 chars
}
```

## Fields

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| id | string | YES | pattern `p{XX}_{prefix}_{slug}`, globally unique |
| kind | KindName | YES | must exist in kinds_meta.json |
| pillar | P01-P12 | YES | must match kind's canonical pillar |
| quality | null\|float | YES | null when produced; peer sets value |
| tags | string[] | YES | min 2, lowercase, kebab-case |
| tldr | string | YES | <= 160 chars |

## Cross-References
- `N03_engineering/P06_schema/type_def_cex_types.md` — master CEX type registry
- `N03_engineering/P06_schema/enum_def_build_actions.md` — KindName enum source
```
```

---

## Example 2: input_schema via Hybrid

### INPUT

```
User: "create input schema for the 8F pipeline build request"
Context: N03_engineering, pillar P06
```

### REASONING (8F abbreviated)

```
F1: kind=input_schema, pillar=P06, nucleus=N03
    max_bytes: 4096

F2: input-schema-builder loaded (13 ISOs)

F3: partial match -> input_schema_engineering.md (similarity: 52%)
    approach: Hybrid (30-60% match)
    injected: input_schema_engineering.md + interface_builder_protocol.md

F4: composite from input_schema_engineering (structure)
    + fresh content for 8F-specific fields

F7: density_score: 0.91, gates 7/7, score: 9.2
```

### OUTPUT (key sections only)

```markdown
---
id: p06_is_8f_build_request
kind: input_schema
pillar: P06
title: "Input Schema -- 8F Pipeline Build Request"
quality: null
---

## Schema

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| intent | string | YES | — | Natural language or structured intent |
| kind | KindName | NO | auto-resolved | Override kind resolution |
| pillar | P01-P12 | NO | auto-resolved | Override pillar assignment |
| nucleus | N01-N07 | NO | auto-routed | Force specific nucleus |
| budget_tokens | int | NO | 50000 | Agent loop token budget |
| target_score | float | NO | 9.0 | Minimum acceptable quality |
| dry_run | bool | NO | false | Validate without writing |
| manifest_path | string | NO | auto-detect | GDP decision manifest |

## Validation Rules

| Rule | Message |
|------|---------|
| intent.length >= 3 | "Intent too short -- be specific" |
| kind IN kinds_meta.json | "Unknown kind -- check .cex/kinds_meta.json" |
| target_score IN [0, 10] | "Score out of range" |
| nucleus IN [n01..n07] | "Unknown nucleus" |
```

---

## Example 3: validation_schema via Fresh

### INPUT

```
User: "validation schema for CoC artifact compliance"
Context: N03_engineering, P06, no existing template
```

### REASONING (8F abbreviated)

```
F1: kind=validation_schema, pillar=P06
    template match: 22% (below 30%) -> Fresh approach

F2: validation-schema-builder loaded

F3: injected kc_engineering_vocabulary.md + invariant_n03.md (INV-07 through INV-12)
    No template; build from schema and invariants

F4: Fresh from first principles:
    what validates CoC? -> structure check + field check + naming check

F7: density_score: 0.88, score: 9.0
```

### OUTPUT (key sections only)

```markdown
---
id: p06_vs_coc_artifact
kind: validation_schema
pillar: P06
title: "Validation Schema -- CoC Artifact Compliance"
quality: null
---

## Validation Rules

| Rule ID | Check | Pass Condition | Fail Action |
|---------|-------|----------------|-------------|
| COC-01 | Frontmatter present | YAML block at file start | REJECT |
| COC-02 | kind in kinds_meta.json | exact match | REJECT |
| COC-03 | pillar matches kind | schema lookup | REJECT |
| COC-04 | id format: p{XX}_{prefix}_{slug} | regex match | WARN |
| COC-05 | quality: null | exact match | REJECT (self-scoring) |
| COC-06 | File in correct pillar dir | path.startswith("N0X/P{XX}") | WARN |
| COC-07 | density_score >= 0.85 | numeric check | WARN |
| COC-08 | No filler phrases | grep pattern list | WARN |
```

---

## What This Example Teaches

| Pattern | Demonstrated |
|---------|-------------|
| Template-First selects when match >= 60% | Example 1 (78% match -> adapt) |
| Hybrid selects when match 30-60% | Example 2 (52% match -> composite) |
| Fresh selects when match < 30% | Example 3 (22% match -> first principles) |
| All three still run full F1-F8 | Every example shows F7 pass |
| Output format is consistent across patterns | Frontmatter structure identical |

---

## Cross-References

- `N03_engineering/P06_schema/type_def_cex_types.md` — CEX type definitions (source)
- `N03_engineering/P06_schema/input_schema_engineering.md` — Example 2 source template
- `N03_engineering/P08_architecture/pattern_construction_triad.md` — Template/Hybrid/Fresh decision
- `N03_engineering/P08_architecture/pattern_8f_full_trace.md` — F3 template match field

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_vs_frontmatter]] | downstream | 0.42 |
| [[bld_schema_reranker_config]] | downstream | 0.39 |
| [[bld_schema_prompt_compiler]] | downstream | 0.39 |
| [[bld_schema_kind]] | downstream | 0.38 |
| [[bld_schema_integration_guide]] | downstream | 0.37 |
| [[bld_schema_thinking_config]] | downstream | 0.37 |
| [[bld_schema_input_schema]] | downstream | 0.37 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.37 |
| [[bld_schema_dataset_card]] | downstream | 0.37 |
| [[bld_schema_voice_pipeline]] | downstream | 0.36 |
