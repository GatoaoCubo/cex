---
id: "p02_mc_[model_slug]"
kind: model_card
8f: F2_become
pillar: P02
version: 1.0.0
title: "Template — Model Card"
tags: [template, model-card, llm, config, selection]
tldr: Documents LLM capabilities, costs, limits, and recommended use cases for informed model selection.
quality: 9.0
model_name: ['nome_do_modelo']
provider: ['openai|anthropic|google|local']
context_window: ['numero_de_tokens']
pricing: ['input_x_output_ou_flat_rate']
updated: "2026-04-07"
domain: "model configuration"
author: n03_builder
created: "2026-04-07"
density_score: 0.99
related:
  - research_then_build
  - full_pipeline
  - build_and_review
  - skill
  - doctor
  - p03_up_dispatch_agent_group
  - status
  - p05_output_validator
  - p03_ap_{{ACTION_SLUG}}
  - p01_rs_brain_faiss_index
---

# Model Card: [NAME]

## Purpose
[WHAT model this card documents — capabilities, costs, limits, recommended usage]
## Model Identity
| Field | Value |
|-------|-------|
| Provider | [anthropic | openai | google | local] |
| Model | [MODEL_NAME] |
| Context window | [N tokens] |
| Output max | [N tokens] |
## Capabilities
| Task | Quality | Speed | Cost |
|------|---------|-------|------|
| Coding | [excellent/good/fair] | [fast/med/slow] | [$N/1M] |
| Analysis | [excellent/good/fair] | [fast/med/slow] | [$N/1M] |
| Creative | [excellent/good/fair] | [fast/med/slow] | [$N/1M] |
| Tool use | [excellent/good/fair] | [fast/med/slow] | [$N/1M] |
## Recommended Use
1. **Best for**: [PRIMARY_USE_CASE]
2. **Good for**: [SECONDARY_USE_CASE]
3. **Avoid for**: [WHEN_NOT_TO_USE]
## Cost
```yaml
input_cost_per_1m: [N.NN]
output_cost_per_1m: [N.NN]
rate_limit_rpm: [N]
```
## Quality Gate
1. [ ] Context window documented
2. [ ] At least 3 capabilities rated
3. [ ] Cost documented
4. [ ] Use case recommendations present

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
| [[research_then_build]] | downstream | 0.35 |
| [[full_pipeline]] | downstream | 0.34 |
| [[build_and_review]] | downstream | 0.34 |
| [[skill]] | downstream | 0.34 |
| [[doctor]] | downstream | 0.32 |
| [[p03_up_dispatch_agent_group]] | downstream | 0.29 |
| [[status]] | downstream | 0.28 |
| [[p05_output_validator]] | downstream | 0.27 |
| [[p03_ap_{{ACTION_SLUG}}]] | downstream | 0.26 |
| [[p01_rs_brain_faiss_index]] | related | 0.26 |
