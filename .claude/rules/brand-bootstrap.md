---
id: brand_bootstrap
kind: instruction
pillar: P08
glob: "**"
alwaysApply: true
description: "Brand bootstrap detection — trigger brand setup on first interaction"
quality: 9.1
title: "Brand-Bootstrap"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - skill
  - doctor
  - p01_kc_cex_as_digital_asset
  - n02_marketing
  - p03_sp_brand_nucleus
  - research_then_build
  - n05_operations
  - full_pipeline
  - n04_knowledge
  - status
---

# Brand Bootstrap Detection

## CHECK ON EVERY SESSION START

Before executing ANY user request, check if CEX has been bootstrapped:

```bash
python _tools/cex_bootstrap.py --check
```

### If NOT bootstrapped (exit code 1):

**DO NOT proceed with the user's request.** Instead:

1. Explain briefly:
   > "I notice this CEX instance hasn't been configured for your brand yet.
   > The X in CEX is a variable — let me fill it with YOUR identity.
   > This takes about 2 minutes and makes everything I produce match your brand."

2. Ask the MINIMUM questions in natural conversation:
   - "What's your company/brand name?"
   - "What do you do in one sentence?"
   - "What are your 3 core values?"
   - "How would you describe your brand's personality — more formal or casual? Technical or friendly?"
   - "Who is your ideal customer?"
   - "How do you make money — subscription, one-time sales, courses?"

3. From the answers, write a YAML file and bootstrap:
   ```bash
   python _tools/cex_bootstrap.py --from-file /tmp/brand_init.yaml
   ```

4. Confirm: "Done! CEX is now configured for [BRAND_NAME]. Let's get to work."

5. THEN proceed with the user's original request.

### If ALREADY bootstrapped (exit code 0):

Proceed normally. The brand context is auto-injected into all prompts.

## WHY THIS MATTERS

Without brand_config.yaml, every nucleus produces GENERIC output.
With it, every output matches the user's voice, colors, and identity.
The 2-minute investment saves hours of "make it sound more like us" revisions.

## Properties

| Property | Value |
|----------|-------|
| Kind | `` |
| Pillar |  |
| Domain | CEX system |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## System Context

This artifact participates in the CEX typed knowledge system, a fractal
architecture with 12 pillars, 8 nuclei, and 125 specialized builders.
Artifacts flow through the 8F pipeline: Focus, Frame, Fetch, Filter,
Format, Forge, Furnish, and Feedback.

Quality is enforced via 3-layer scoring: structural (30%), rubric (30%),
and semantic (40%). All artifacts target quality >= 9.0.

| Layer | Weight | Method |
|-------|--------|--------|
| Structural | 30% | Automated count-based checks |
| Rubric | 30% | Quality gate dimension scoring |
| Semantic | 40% | LLM evaluation (when L1+L2 >= 8.5) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[skill]] | sibling | 0.46 |
| [[doctor]] | sibling | 0.40 |
| [[p01_kc_cex_as_digital_asset]] | upstream | 0.38 |
| [[n02_marketing]] | sibling | 0.37 |
| [[p03_sp_brand_nucleus]] | upstream | 0.36 |
| [[research_then_build]] | related | 0.36 |
| [[n05_operations]] | sibling | 0.36 |
| [[full_pipeline]] | related | 0.36 |
| [[n04_knowledge]] | sibling | 0.35 |
| [[status]] | sibling | 0.35 |
