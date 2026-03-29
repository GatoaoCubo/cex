---
kind: examples
id: bld_examples_lens
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of lens artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: lens-builder
## Golden Example
INPUT: "Cria uma lens de custo para avaliar model_cards e embedding_configs"
OUTPUT:
```yaml
id: p02_lens_cost_efficiency
kind: lens
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
perspective: "cost_efficiency"
applies_to: [model_card, embedding_config, agent_card]
focus: "Pricing, token costs, and cost-per-task efficiency"
filters: [pricing, context_window, tokens_per_second, batch_size, dimensions]
bias: "Favors lower cost-per-output-token when quality is comparable"
interpretation: "Ranks artifacts by cost efficiency ratio: quality / cost. Higher = better."
weight: 0.8
priority: 1
scope: "LLM selection, satellite model routing, embedding provider choice"
domain: "infrastructure-optimization"
quality: null
tags: [lens, cost, efficiency, pricing, model-selection]
tldr: "Cost efficiency lens — evaluates artifacts by quality-to-cost ratio for infra decisions."
```
## Perspective
Evaluates artifacts through cost efficiency: what is the quality-per-dollar ratio?
Applies to model_cards (LLM pricing), embedding_configs (vector cost), agent_cards (model allocation).
## Filters
- **pricing**: input/output token costs, batch discounts, free tiers
- **context_window**: cost per context unit (larger window = fewer calls)
- **tokens_per_second**: throughput efficiency (faster = lower wall-clock cost)
- **batch_size**: bulk processing economics
- **dimensions**: embedding size vs retrieval accuracy tradeoff
## Application
1. Read the artifact's cost-related fields
2. Calculate quality-to-cost ratio where applicable
3. Compare against alternatives in the same kind
4. Flag artifacts where cost exceeds 2x the cheapest comparable option
## Limitations
- Does not evaluate quality directly (that is scoring_rubric P07)
- Ignores latency preferences (a speed lens would cover that)
- May undervalue high-cost options justified for critical tasks
## References
- LiteLLM pricing comparison
- Hugging Face MTEB leaderboard (embedding cost/quality)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p02_lens_ pattern (H02 pass)
- kind: lens (H04 pass)
- 20 frontmatter fields present (H06 pass)
- perspective non-empty string (H07 pass)
- applies_to has 3 entries (H08 pass)
- YAML parses cleanly (H01 pass)
- id == filename stem (H03 pass)
- tldr <= 160 chars, dense (S01 pass)
- tags list len >= 3, includes "lens" (S02 pass)
## Anti-Example
INPUT: "Create a cost lens"
BAD OUTPUT:
```yaml
id: cost_lens
kind: perspective
pillar: Model
perspective: Cost Analysis
applies_to: models
quality: 8.5
tags: cost
focus: Analyzing the cost of various things in great detail across many dimensions and aspects of the system to ensure we are making the most efficient choices possible
```
This is a general cost analysis document that covers everything about costs.
FAILURES:
1. id: no `p02_lens_` prefix -> H02 FAIL
2. kind: "perspective" not "lens" -> H04 FAIL
3. pillar: "Model" not "P02" -> H01 FAIL (wrong literal)
4. quality: 8.5 (not null) -> H05 FAIL
5. applies_to: string not list -> H08 FAIL
6. tags: string not list, len < 3 -> S02 FAIL
7. focus: filler prose ("great detail", "many dimensions") -> S07 FAIL
8. No body sections (Perspective, Filters, Application, Limitations) -> S03-S06 FAIL
9. perspective: natural case "Cost Analysis" instead of snake_case -> S05 FAIL
10. Missing required fields: version, created, updated, author, domain, tldr -> H06 FAIL
