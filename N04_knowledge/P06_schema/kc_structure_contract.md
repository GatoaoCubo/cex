---
id: p06_schema_kc_structure
kind: schema
8f: F1_constrain
pillar: P06
title: "KC Structure Contract"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.1
tags: [schema, n04, kc, structure, frontmatter, format]
tldr: "Standard KC format: required frontmatter (14 fields), section order, density rules. The template every KC must follow."
density_score: 0.94
related:
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - p06_is_creation_data
  - p01_fse_kc_creation
  - bld_schema_integration_guide
  - bld_schema_prompt_compiler
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
  - p06_is_knowledge_data_model
  - bld_schema_training_method
---

# KC Structure Contract

## Required Frontmatter

| Field | Type | Example |
|-------|------|---------|
| id | string | p01_kc_chain_of_thought |
| kind | literal: knowledge_card | knowledge_card |
| type | enum: kind\|domain\|platform\|infrastructure | domain |
| pillar | enum: P01-P12 | P01 |
| title | string (5-80 chars) | "Chain-of-Thought Prompting" |
| version | semver | 1.0.0 |
| created | date | 2026-03-31 |
| author | string | n07_orchestrator |
| domain | string | llm_patterns |
| quality | null or float | null (on creation) |
| tags | list[string] (3-10) | [cot, reasoning, llm] |
| tldr | string (20-200 chars) | "Step-by-step reasoning..." |
| keywords | list[string] (3-8) | [chain-of-thought, cot] |
| density_score | float 0-1 | 0.92 |

## Section Order
1. H1 title (matches frontmatter title)
2. Core concept (1-3 paragraphs max)
3. Tables/structured data (primary content)
4. CEX Integration (how it connects to the system)

## Density Rules
- No "In this KC we will discuss..." → just discuss it
- Tables over prose when data is structured
- Maximum 2KB for focused KCs, 4KB for comprehensive
- Every sentence must pass: "if I delete this, does the KC lose value?"

## Anti-Patterns

| ❌ Wrong | ✅ Correct | Why |
|----------|------------|-----|
| `quality: 8.5` | `quality: null` | Never self-score on creation |
| Missing `tldr` field | Required 20-200 char summary | Index generation needs it |
| `title: "This KC explains..."` | `title: "Chain-of-Thought"` | Direct naming, not meta |
| 3 intro paragraphs | 1 focused paragraph | Density rule violation |
| Prose list of 8 items | Table with 8 rows | Structured data needs tables |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_registry]] | sibling | 0.36 |
| [[bld_schema_experiment_tracker]] | sibling | 0.34 |
| [[p06_is_creation_data]] | related | 0.34 |
| [[p01_fse_kc_creation]] | upstream | 0.32 |
| [[bld_schema_integration_guide]] | sibling | 0.32 |
| [[bld_schema_prompt_compiler]] | sibling | 0.31 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.31 |
| [[bld_schema_dataset_card]] | sibling | 0.31 |
| [[p06_is_knowledge_data_model]] | related | 0.30 |
| [[bld_schema_training_method]] | sibling | 0.30 |
