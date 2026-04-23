---
id: p06_is_builder_nucleus
kind: input_schema
pillar: P06
title: Input Schema -- Builder Nucleus
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [input-schema, builder, N03]
tldr: What the builder accepts as input -- intent string, kind override, context, output dir, flags.
density_score: 0.88
related:
  - bld_schema_kind
  - bld_architecture_kind
  - p04_ct_cex_8f_motor
  - p08_pat_builder_construction
  - bld_schema_model_registry
  - bld_schema_prompt_compiler
  - kind-builder
  - p06_if_builder_nucleus
  - p06_is_knowledge_data_model
  - p06_is_creation_data
---

# Input Schema: Builder Nucleus

## Primary Input

The builder accepts natural language intent. The Motor resolves it to kind(s).

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| intent | string | yes (or kind) | Natural language request |
| kind | string | no | Explicit kind override (bypasses Motor) |
| pillar | string P[0-9]{2} | no | Override pillar (usually derived) |
| context | string max 5000 | no | Additional context for F3 INJECT |
| domain | string | no | Domain scope |
| output_dir | path | no | Override output directory |
| dry_run | boolean | no (default false) | Simulate without writing |
| model | enum haiku/sonnet/opus | no | Override model selection |

## Validation Rules

1. intent OR kind must be provided (at least one)
2. If kind provided, must exist in kinds_meta.json
3. context trimmed to 5000 chars if longer
4. output_dir must be writable
5. model override only affects F4 REASON and F6 PRODUCE

## Examples

| Intent | Resolved Kind | Model |
|--------|--------------|-------|
| create an agent for research | agent | sonnet |
| build workflow for deploy pipeline | workflow | opus |
| scaffold KC about embeddings | knowledge_card | sonnet |
| register new kind called metric | (kind_register tool) | N/A |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_kind]] | related | 0.29 |
| [[bld_architecture_kind]] | downstream | 0.29 |
| [[p04_ct_cex_8f_motor]] | upstream | 0.26 |
| [[p08_pat_builder_construction]] | downstream | 0.26 |
| [[bld_schema_model_registry]] | related | 0.25 |
| [[bld_schema_prompt_compiler]] | related | 0.25 |
| [[kind-builder]] | downstream | 0.25 |
| [[p06_if_builder_nucleus]] | related | 0.25 |
| [[p06_is_knowledge_data_model]] | sibling | 0.25 |
| [[p06_is_creation_data]] | sibling | 0.24 |
