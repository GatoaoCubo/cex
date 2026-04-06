---
id: bld_architecture_tagline
kind: architecture
pillar: P08
builder: tagline-builder
version: 1.0.0
---
# Architecture: Tagline Builder

## Pipeline
```
DISCOVER → EXTRACT_USP → GENERATE(5 approaches × 3 lengths) → FILTER(3 tests) → RANK → ADAPT(contexts) → DELIVER
```

## Data Flow
- Input: brand_config.yaml OR user answers (industry, audience, tone, differentiator)
- Processing: 15+ candidates → filter → top 5 → adapt → recommend 1
- Output: YAML with variants, scores, context adaptations, reasoning

## Dependencies
- brand_config.yaml (optional — falls back to user interview)
- Competitor taglines (optional — for differentiation check)

## Integration Points
- N02 Marketing: consumes taglines for campaigns, ads, social posts
- N06 Commercial: uses taglines in pricing pages, pitch decks, brand book
- landing-page-builder: uses recommended tagline as hero headline
