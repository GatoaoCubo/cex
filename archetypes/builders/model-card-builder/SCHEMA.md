---
lp: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for model_card frontmatter and body
---

# Schema: model_card

## Frontmatter Fields

| Field | Type | Required | Default | Source |
|-------|------|----------|---------|--------|
| id | string (p02_mc_{provider}_{slug}) | YES | — | CEX naming |
| type | literal "model_card" | YES | — | CEX |
| lp | literal "P02" | YES | — | CEX |
| version | semver string | YES | "1.0.0" | CEX |
| created | date YYYY-MM-DD | YES | — | CEX |
| updated | date YYYY-MM-DD | YES | — | CEX |
| author | string | YES | — | CEX |
| model_name | string | YES | — | Mitchell 2019 |
| provider | enum | YES | — | LiteLLM |
| model_type | enum | YES | — | HF pipeline_tag |
| status | enum (active/deprecated/sunset) | YES | active | CEX-ext |
| release_date | date or null | REC | null | HF, Meta |
| knowledge_cutoff | YYYY-MM or null | REC | null | Mitchell |
| context_window | integer > 0 | YES | — | Universal |
| max_output | integer > 0 | YES | — | Anthropic SDK |
| modalities | object (5 bools) | YES | — | LangChain |
| features | object (8 bools) | YES | — | LiteLLM |
| pricing | object (4 floats + unit) | YES | — | LiteLLM |
| domain | literal "model_selection" | YES | — | CEX |
| quality | null | YES | null | CEX (never self-score) |
| tags | list[string] | YES | — | CEX |
| tldr | string < 160ch | YES | — | CEX |
| when_to_use | string | YES | — | CEX |
| keywords | list[string] | REC | — | CEX |
| linked_artifacts | object | REC | — | CEX |
| data_source | URL string | YES | — | CEX |

## Body Structure (required sections)
1. ## Boundary (model_card EH / NAO EH)
2. ## Specifications (table with Source column)
3. ## Capabilities (boolean table)
4. ## When to Use (decision table >= 3 rows)
5. ## References (>= 1 URL)

## Constraints
- max_bytes: 3072 (body only, excl frontmatter)
- naming: p02_mc_{provider}_{model_slug}.md
- id == filename stem
- pricing.unit ALWAYS "per_1M_tokens"
- all modalities/features values MUST be boolean
