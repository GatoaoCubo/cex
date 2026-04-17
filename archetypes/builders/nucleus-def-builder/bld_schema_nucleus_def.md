---
kind: schema
id: bld_schema_nucleus_def
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for nucleus_def
quality: 9.2
title: "Schema Nucleus Def"
version: "1.0.0"
author: n05_wave8
tags: [nucleus_def, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for nucleus_def"
domain: "nucleus_def construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields

### Required
| Field              | Type    | Required | Default | Notes |
|--------------------|---------|----------|---------|-------|
| id                 | string  | yes      |         | Pattern: p02_nd_n0[0-7].md |
| kind               | string  | yes      |         | Must be "nucleus_def" |
| pillar             | string  | yes      |         | Must be "P02" |
| title              | string  | yes      |         | "Nucleus Def N0{X}" |
| version            | string  | yes      |         | Semver |
| created            | date    | yes      |         | ISO 8601 |
| updated            | date    | yes      |         | ISO 8601 |
| author             | string  | yes      |         | |
| domain             | string  | yes      |         | e.g., "operations" |
| quality            | null    | yes      | null    | Never self-score |
| tags               | array   | yes      |         | |
| tldr               | string  | yes      |         | |
| nucleus_id         | string  | yes      |         | N00-N07 |
| role               | string  | yes      |         | See enum below |
| pillars_owned      | array   | yes      |         | Non-empty subset of P01-P12 |
| sin_lens           | string  | yes      |         | Full sin name + translation |
| cli_binding        | string  | yes      |         | claude|gemini|codex|ollama |
| model_tier         | string  | yes      |         | opus|sonnet|haiku|local |
| boot_script        | string  | yes      |         | Path to .ps1 boot file |
| agent_card_path    | string  | yes      |         | Path to agent_card .md |

### Recommended
| Field                   | Type   | Notes |
|-------------------------|--------|-------|
| crew_templates_exposed  | array  | Composable crew patterns this nucleus can assemble |
| domain_agents           | array  | Non-builder agents in N0{X}_*/P02_model/ |
| model_specific          | string | Full model identifier (e.g., claude-opus-4-6) |
| context_tokens          | int    | Max context tokens (e.g., 200000 or 1000000) |
| fallback_cli            | string | First fallback CLI if primary fails |

## Enums

### role
| Value          | Nucleus | Description |
|----------------|---------|-------------|
| genesis        | N00     | Universal mold -- defines what can exist |
| intelligence   | N01     | Research, analysis, competitor intel |
| marketing      | N02     | Copywriting, ads, campaigns, brand voice |
| builder        | N03     | Artifact construction, 8F pipeline execution |
| knowledge      | N04     | RAG, embeddings, knowledge cards, taxonomy |
| operations     | N05     | Code review, testing, CI/CD, deployment |
| commercial     | N06     | Pricing, monetization, sales funnels |
| orchestrator   | N07     | Dispatch, mission planning, wave coordination |

### cli_binding
claude | gemini | codex | ollama

### model_tier
opus | sonnet | haiku | local

## ID Pattern
^p02_nd_n0[0-7]\.md$

## Body Structure
1. **Identity Table** -- nucleus_id, role, sin_lens, CLI, model in tabular form
2. **Pillars Owned** -- table mapping pillar to domain and sample artifact kinds
3. **Crew Templates Exposed** -- composable crew patterns with roles + input/output
4. **Domain Agents** -- enumeration of non-builder agents in N0{X}_*/agents/
5. **Boot Contract** -- boot_script path, handoff file convention, signal format
6. **Composability** -- upstream producers + downstream consumers in orchestration graph

## Constraints
- nucleus_id must be one of: N00, N01, N02, N03, N04, N05, N06, N07.
- pillars_owned must be a non-empty subset of [P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12].
- cli_binding must match nucleus_models.yaml for the target nucleus.
- boot_script must be a real path (boot/n0{X}.ps1 convention).
- agent_card_path must be a real path (N0{X}_*/agent_card_n0{X}.md convention).
- max_bytes: 5120.
