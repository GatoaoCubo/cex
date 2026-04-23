---
id: bld_instruction_tagline
kind: instruction
pillar: P03
builder: tagline-builder
version: 1.0.0
quality: 9.1
title: "Instruction Tagline"
author: n03_builder
tags: [tagline, builder, examples]
tldr: "Golden and anti-examples for tagline construction, demonstrating ideal structure and common pitfalls."
domain: "tagline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: REASON
related:
  - bld_quality_gate_tagline
  - bld_system_prompt_tagline
  - bld_architecture_tagline
  - tagline-builder
  - bld_output_template_tagline
  - bld_memory_tagline
  - bld_tools_tagline
  - bld_collaboration_tagline
  - bld_config_tagline
  - bld_schema_tagline
---
# Instruction: Tagline Creation Pipeline

## Steps
1. **DISCOVER** — Read brand_config.yaml OR ask user for: brand name, industry, target audience, tone, key differentiator, competitor taglines to avoid
2. **EXTRACT** — Identify the core USP in one sentence. What does this brand do that nobody else does?
3. **GENERATE** — Produce 10+ variants across 5 approaches:
   - **Emotional**: triggers feeling (fear, aspiration, belonging, pride)
   - **Functional**: states the benefit clearly ("X that does Y")
   - **Aspirational**: paints the future state ("Become X", "The world where Y")
   - **Provocative**: challenges assumptions ("Why X when Y?", "Stop doing X")
   - **Minimal**: fewest words possible (2-4 words, Nike "Just Do It" style)
4. **FILTER** — Apply 3 tests to each variant:
   - Billboard test (3-second comprehension)
   - Competitor swap test (unique to this brand)
   - Memory test (sticky after 24h)
5. **RANK** — Score surviving variants 1-10 on: memorability, clarity, differentiation, emotional impact, versatility
6. **ADAPT** — For top 3: produce context variants (hero, social bio, email subject, ad, pitch deck)
7. **DELIVER** — Structured output with recommended + reasoning

## Anti-Patterns
1. Generic lines that fit any brand ("Innovation meets excellence")
2. Puns that don't translate across markets
3. Taglines longer than 15 words
4. Copying competitor patterns too closely

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify tagline
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | tagline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_quality_gate_tagline]] | downstream | 0.41 |
| [[bld_system_prompt_tagline]] | related | 0.39 |
| [[bld_architecture_tagline]] | downstream | 0.36 |
| [[tagline-builder]] | related | 0.35 |
| [[bld_output_template_tagline]] | downstream | 0.34 |
| [[bld_memory_tagline]] | downstream | 0.33 |
| [[bld_tools_tagline]] | downstream | 0.32 |
| [[bld_collaboration_tagline]] | downstream | 0.30 |
| [[bld_config_tagline]] | downstream | 0.29 |
| [[bld_schema_tagline]] | downstream | 0.29 |
