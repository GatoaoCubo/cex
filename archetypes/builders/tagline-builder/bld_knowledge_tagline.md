---
id: bld_knowledge_card_tagline
kind: knowledge_card
pillar: P01
builder: tagline-builder
version: 1.0.0
quality: 9.1
title: "Knowledge Card Tagline"
author: n03_builder
tags: [tagline, builder, examples]
tldr: "Golden and anti-examples for tagline construction, demonstrating ideal structure and common pitfalls."
domain: "tagline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: INJECT
related:
  - kc_tagline
  - tagline-builder
  - bld_collaboration_tagline
  - bld_output_template_tagline
  - bld_schema_tagline
  - bld_tools_tagline
  - bld_system_prompt_tagline
  - bld_quality_gate_tagline
  - bld_instruction_tagline
  - bld_config_tagline
---
# Knowledge Card: Tagline

## What is a Tagline?
A tagline is a short, memorable phrase (3-15 words) that captures a brand's essence,
value proposition, or emotional promise. It appears everywhere: website hero, social bios,
ad headlines, email signatures, pitch decks.

## Frameworks
| Framework | Pattern | Example |
|-----------|---------|---------|
| AIDA Headline | Attention→Interest→Desire→Action | "Stop guessing. Start knowing." |
| PAS Hook | Problem→Agitate→Solution | "Tired of X? Y changes everything." |
| Before/After | Old state → New state | "From chaos to clarity." |
| Question Hook | Provocative question | "What if your code tested itself?" |
| Command | Direct imperative | "Just Do It." / "Think Different." |
| Metaphor | Analogy-based | "The Swiss Army knife of AI." |

## Best Practices
1. 3-5 words = gold standard (Nike, Apple, McDonald's)
2. Test against competitors: if they could use it, it's not unique enough
3. Rhythm matters: iambic or trochaic patterns are more memorable
4. One idea per tagline — never compound
5. Translate to check: if it breaks in another language, it might be fragile

## Anti-Patterns
1. Buzzword soup: "Innovative synergistic solutions"
2. Too long: anything over 15 words is a sentence, not a tagline
3. Generic: "Excellence in every detail" (fits any company)
4. Feature-focused: "128-bit encryption with real-time sync" (not a tagline)

## Retrieval

```yaml
query: "tagline construction"
kind_filter: knowledge_card
top_k: 5
threshold: 0.7
```

```bash
python _tools/cex_retriever.py "tagline construction" --top 5
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_tagline]] | sibling | 0.66 |
| [[tagline-builder]] | downstream | 0.48 |
| [[bld_collaboration_tagline]] | downstream | 0.42 |
| [[bld_output_template_tagline]] | downstream | 0.41 |
| [[bld_schema_tagline]] | downstream | 0.40 |
| [[bld_tools_tagline]] | downstream | 0.39 |
| [[bld_system_prompt_tagline]] | downstream | 0.39 |
| [[bld_quality_gate_tagline]] | downstream | 0.37 |
| [[bld_instruction_tagline]] | downstream | 0.36 |
| [[bld_config_tagline]] | downstream | 0.36 |
