---
id: p12_wn_f1_constrain
name: F1 CONSTRAIN
description: Resolves user intent to a canonical (kind, pillar, schema, max_bytes) tuple by querying kinds_meta.json and loading the pillar schema. First mandatory step in every 8F pipeline run.
type: resolution
inputs:
  - user_intent
  - kinds_meta_json
outputs:
  - kind
  - pillar
  - schema
  - max_bytes
  - naming_pattern
parameters:
  confidence_threshold: 0.6
  fallback_to_gdp: true
quality: 8.5
status: production
pillar: P12
kind: workflow_node
8f: F8_collaborate
version: "1.0.0"
created: "2026-04-19"
updated: "2026-04-19"
author: "n03_engineering"
tags: [workflow_node, 8f_pipeline, f1_constrain, P12, resolution]
tldr: "F1 CONSTRAIN node: intent -> (kind, pillar, schema, max_bytes). Resolution type. Confidence gate at 0.6; GDP fallback if ambiguous."
related:
  - p01_kc_prompt_compiler
  - bld_architecture_kind
  - p03_ins_prompt_compiler
  - bld_collaboration_prompt_compiler
  - bld_schema_kind
  - p01_kc_input_intent_resolution
  - bld_instruction_kind
  - kind-builder
  - bld_schema_prompt_compiler
  - atom_12_dify
density_score: 1.0
---

# Workflow Node: F1 CONSTRAIN

Models the first step of the 8F pipeline as a self-contained workflow node.
Used by `cex_mission_runner.py` and crew templates to compose multi-step pipelines
where 8F steps are wired as explicit nodes rather than implicit function calls.

## Description

F1 CONSTRAIN takes a raw user intent string and resolves it to a concrete
CEX taxonomy tuple `{kind, pillar, schema, max_bytes, naming_pattern}`.
Resolution uses `.cex/kinds_meta.json` (300 kinds) and the intent transmutation
pattern table at `N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md`.

If resolution confidence falls below `confidence_threshold` (default 0.6):
- If `fallback_to_gdp=true`: pause, present top-3 candidates to user (GDP mode)
- If `fallback_to_gdp=false`: select the highest-confidence candidate and continue

**Inputs/Outputs**

| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| user_intent | string | input | Raw user request (any language, any metaphor) |
| kinds_meta_json | dict | input | Parsed .cex/kinds_meta.json (293 kind entries) |
| kind | string | output | Resolved canonical kind name (e.g., "knowledge_card") |
| pillar | string | output | Resolved pillar (P01-P12) |
| schema | dict | output | Loaded pillar _schema.yaml as parsed object |
| max_bytes | integer | output | Maximum artifact byte size from schema |
| naming_pattern | string | output | Artifact ID naming regex from schema |

## Configuration Example

```yaml
parameters:
  confidence_threshold: 0.6   # below this -> GDP or auto-select top candidate
  fallback_to_gdp: true        # true=ask user, false=auto-select and log warning
```

## Parameters

- `confidence_threshold`: Minimum match score (0.0-1.0) to accept a kind resolution without fallback. Default: 0.6. Lower = more permissive but risks wrong kind. Higher = safer but more GDP interruptions.
- `fallback_to_gdp`: When confidence < threshold, present top-3 candidates to user if true; auto-select highest if false. Default: true (co-pilot mode). Set false for fully autonomous dispatch.

## Wiring (next node)

| Output | Next Node | Condition |
|--------|-----------|-----------|
| kind + pillar resolved | F2_BECOME | confidence >= threshold |
| ambiguous candidates | GDP_PAUSE | confidence < threshold AND fallback_to_gdp=true |
| top candidate auto-selected | F2_BECOME | confidence < threshold AND fallback_to_gdp=false |
| kind not in kinds_meta | FAILED | no candidate above 0.2 |

## Status

production -- F1 CONSTRAIN is the mandatory entry point for every 8F run.
Any task that bypasses this node violates the 8F protocol.

## References

- Intent transmutation source: `N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md`
- Kind registry: `.cex/kinds_meta.json`
- Python resolver (token-free): `_tools/cex_intent_resolver.py`
- Full state machine: `N03_engineering/P08_architecture/state_machine_8f_pipeline.md`
- Next node definition: `archetypes/builders/{kind}-builder/bld_manifest_{kind}.md` (F2 target)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_prompt_compiler]] | upstream | 0.27 |
| [[bld_architecture_kind]] | upstream | 0.25 |
| [[p03_ins_prompt_compiler]] | upstream | 0.25 |
| [[bld_collaboration_prompt_compiler]] | upstream | 0.24 |
| [[bld_schema_kind]] | upstream | 0.23 |
| [[p01_kc_input_intent_resolution]] | upstream | 0.23 |
| [[bld_instruction_kind]] | upstream | 0.23 |
| [[kind-builder]] | upstream | 0.23 |
| [[bld_schema_prompt_compiler]] | upstream | 0.22 |
| [[atom_12_dify]] | upstream | 0.22 |
