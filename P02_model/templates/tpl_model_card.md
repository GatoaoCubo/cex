---
id: "p02_mc_[model_slug]"
version: 1.0.0
title: Template - Unknown
tags: [template, model-card, llm, config, selection]
tldr: Documents LLM capabilities, costs, limits, and recommended use cases for informed model selection.
quality: 8.8
model_name: ['nome_do_modelo']
provider: ['openai|anthropic|google|local']
context_window: ['numero_de_tokens']
pricing: ['input_x_output_ou_flat_rate']
updated: "2026-04-07"
domain: "model configuration"
author: n03_builder
created: "2026-04-07"
density_score: 0.99
---

# Unknown: [NAME]

## Purpose
[WHAT this unknown does]
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
