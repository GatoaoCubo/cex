---
id: tpl_retriever_business_intel
kind: template
pillar: P04
title: "Retriever — Multi-Source Business Intelligence"
version: 1.0.0
quality: 9.1
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo/P04 retriever artifacts
variables: [SOURCES, MERGE_STRATEGY, DEDUP_FIELDS, INDUSTRY, REGION]
density_score: 0.95
tags: [template, retriever, business-intelligence, merge, dedup, instance-extraction]
tldr: "Multi-source business intelligence retriever — merge data from N sources with configurable dedup and quality scoring."
updated: "2026-04-13"
---

# Business Intelligence Retriever

## Source Registry

{{#SOURCES}}
| # | Source | Type | Trust Level | Fields Provided |
|---|--------|------|:-----------:|-----------------|
{{#each}}
| {{position}} | {{name}} | {{type}} | {{trust}} | {{fields}} |
{{/each}}
{{/SOURCES}}

---

## Merge Strategy: `{{MERGE_STRATEGY | default: 'trust_weighted'}}`

### Available Strategies

| Strategy | Description | Use When |
|----------|-------------|----------|
| `trust_weighted` | Higher-trust source wins conflicts | Multiple overlapping sources |
| `most_complete` | Record with most non-null fields wins | Sparse data from many sources |
| `latest_wins` | Most recently fetched data wins | Time-sensitive data |
| `manual_review` | Flag conflicts for human review | Critical data (financial, legal) |

### Merge Rules

```yaml
merge:
  strategy: {{MERGE_STRATEGY | default: 'trust_weighted'}}
  conflict_resolution:
    phone: highest_trust       # Phone from most trusted source
    address: most_complete     # Longest/most detailed address
    rating: average            # Average across sources
    name: longest              # Longest version (usually most complete)
    tax_id: any_non_null       # First non-null wins (unique identifier)
```

---

## Dedup Configuration

### Primary Key Fields

```yaml
dedup:
  primary_fields: {{DEDUP_FIELDS | default: '[nome_fantasia, cidade]'}}
  algorithm: fuzzy_match
  threshold: 0.85              # Levenshtein similarity threshold
  normalize:
    - lowercase
    - strip_accents
    - remove_legal_suffixes    # "LTDA", "ME", "EIRELI", "LLC", "Inc"
    - collapse_whitespace
```

### Dedup Pipeline

```
Input: N records from K sources
  │
  ├── 1. Normalize all name fields
  ├── 2. Group by city (exact match)
  ├── 3. Within city: pairwise fuzzy match on name
  ├── 4. If similarity > threshold → merge (using strategy)
  ├── 5. If tax_id match → merge (override name match)
  └── 6. Output: M unique records (M ≤ N)

Stats:
  - Input: {N} records from {K} sources
  - Duplicates found: {N - M}
  - Unique output: {M}
  - Merge rate: {(N-M)/N * 100}%
```

---

## Quality Scoring

Each merged record gets a quality score (0-100):

| Factor | Weight | Scoring |
|--------|:------:|---------|
| Phone present | 20 | +20 if valid phone |
| Address present | 15 | +15 if street-level address |
| Tax ID present | 15 | +15 if validated |
| Email/website | 10 | +10 if any web presence |
| Social media | 10 | +10 if Instagram/Facebook |
| Rating available | 10 | +10 if any platform rating |
| Multiple sources | 10 | +10 if found in 2+ sources |
| Location coords | 10 | +10 if lat/lng available |

**Tiers**: S+ (90-100) | S (80-89) | A (70-79) | B (60-69) | C (< 60)

---

## Output Schema

```json
{
  "id": "uuid",
  "nome_fantasia": "string",
  "cidade": "string",
  "quality_score": "integer (0-100)",
  "quality_tier": "S+ | S | A | B | C",
  "sources": ["string (list of source names)"],
  "source_count": "integer",
  "merged_at": "ISO-8601 datetime",
  "fields_filled": "integer (out of total)",
  "completeness": "float (0-1)"
}
```
