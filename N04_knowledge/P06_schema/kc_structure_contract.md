---
id: p06_schema_kc_structure
kind: schema
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