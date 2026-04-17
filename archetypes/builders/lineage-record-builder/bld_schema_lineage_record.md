---
id: bld_schema_lineage_record
kind: schema
pillar: P06
llm_function: CONSTRAIN
purpose: "Formal schema -- SINGLE SOURCE OF TRUTH for lineage_record"
quality: null
title: "Schema: lineage_record"
version: "1.0.0"
author: builder
tags: [schema, lineage_record, P01]
domain: "knowledge provenance"
created: "2026-04-17"
updated: "2026-04-17"
density_score: null
---

# Schema: lineage_record

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p01_lr_{name_slug}) | YES | - | Namespace compliance |
| kind | literal "lineage_record" | YES | - | Type integrity |
| pillar | literal "P01" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Version |
| target_artifact | string | YES | - | Artifact whose provenance is recorded |
| sources_count | integer | YES | - | Must match sources list |
| activities_count | integer | YES | - | Must match activities list |
| derivation_type | enum: wasDerivedFrom, wasGeneratedBy, wasQuotedFrom, wasRevisionOf | YES | wasDerivedFrom | Primary PROV-O relation |
| domain | string | YES | - | Knowledge domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "lineage_record" |
| tldr | string <= 160ch | YES | - | Dense summary |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |

## ID Pattern
Regex: `^p01_lr_[a-z][a-z0-9_]+$`

## Body Structure
1. `## Entities` -- table: id, type, location, retrieval_timestamp
2. `## Activities` -- table: id, label, used, generated, agent, timestamp
3. `## Agents` -- table: id, type, role
4. `## Derivation Relations` -- PROV-O triples in table or list

## Constraints
- max_bytes: 3072
- naming: p01_lr_{name_slug}.md
- sources_count and activities_count must match actual list lengths
- All timestamps: ISO 8601 format
- quality: null always
