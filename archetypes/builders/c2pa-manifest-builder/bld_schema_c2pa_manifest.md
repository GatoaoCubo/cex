---
kind: schema
id: bld_schema_c2pa_manifest
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for c2pa_manifest
quality: 9.1
title: "Schema C2PA Manifest"
version: "1.0.0"
author: n04_wave7
tags: [c2pa_manifest, builder, schema, C2PA, claim, assertion, ingredient, signature]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for c2pa_manifest"
domain: "c2pa_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_pitch_deck
  - bld_schema_reranker_config
  - bld_schema_sandbox_config
  - bld_schema_benchmark_suite
  - bld_schema_search_strategy
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
  - bld_schema_api_reference
---

## Frontmatter Fields
### Required
| Field               | Type    | Required | Default | Notes |
|---------------------|---------|----------|---------|-------|
| id                  | string  | yes      |         | p10_cm_{{name}}.md |
| kind                | string  | yes      |         | Must be "c2pa_manifest" |
| pillar              | string  | yes      |         | P10 |
| title               | string  | yes      |         | Content + manifest purpose |
| version             | string  | yes      |         | Semantic version |
| created             | date    | yes      |         | ISO 8601 date |
| updated             | date    | yes      |         | ISO 8601 date |
| author              | string  | yes      |         | Generating nucleus or agent |
| domain              | string  | yes      |         | Content type + use case |
| quality             | null    | yes      | null    | Never self-score; peer review assigns |
| tags                | array   | yes      |         | Must include: C2PA, content-credential, provenance |
| tldr                | string  | yes      |         | One-line manifest purpose |
| content_format      | string  | yes      |         | IANA MIME type of target content |
| digital_source_type | string  | yes      |         | trainedAlgorithmicMedia or compositeSynthetic |
| generator_model     | string  | yes      |         | AI model name and version |
| signer_id           | string  | yes      |         | Certificate CN or DID of signer |

### Recommended
| Field              | Type    | Notes |
|--------------------|---------|-------|
| prompt_text        | string  | Original generation prompt |
| training_data_refs | array   | URIs of training datasets |
| ingredient_count   | integer | Number of ingredient assertions |
| thumbnail_hash     | string  | SHA-256 of embedded thumbnail |

## ID Pattern
^p10_cm_[a-z][a-z0-9_]+\.md$

## Body Structure
1. **Manifest Store** - JUMBF box structure description
2. **Claim** - dc:format, ingredients, assertions, signature reference
3. **AI-ML Generator Assertion** - digitalSourceType, model, prompt
4. **Ingredient Assertions** - Source media with content hashes
5. **Signature Block** - COSE_Sign1 signer reference
6. **Embedding Instructions** - How to embed in target file format

## Constraints
- All required fields must be present and valid.
- id must match the regex pattern exactly.
- content_format must be a valid IANA MIME type.
- digital_source_type must be trainedAlgorithmicMedia or compositeSynthetic.
- signer_id must be X.509 CN or DID.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.70 |
| [[bld_schema_quickstart_guide]] | sibling | 0.67 |
| [[bld_schema_pitch_deck]] | sibling | 0.67 |
| [[bld_schema_reranker_config]] | sibling | 0.67 |
| [[bld_schema_sandbox_config]] | sibling | 0.66 |
| [[bld_schema_benchmark_suite]] | sibling | 0.66 |
| [[bld_schema_search_strategy]] | sibling | 0.66 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.65 |
| [[bld_schema_dataset_card]] | sibling | 0.65 |
| [[bld_schema_api_reference]] | sibling | 0.65 |
