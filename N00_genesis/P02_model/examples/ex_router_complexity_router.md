---
id: p02_rt_complexity_router
kind: router
pillar: P02
title: "Complexity Router"
routes:
  - {threshold: 0.45, target: local, model: ollama/llama3}
  - {threshold: 0.70, target: hybrid, model: claude-sonnet}
  - {threshold: 1.0, target: cloud, model: claude-opus}
fallback: cloud
scoring_factors: 6
tags: [router, complexity, scoring, cost-optimization]
tldr: "Routes requests by complexity score (6 weighted factors) to local/hybrid/cloud tiers for cost-optimal inference."
quality: 9.1
domain: "model configuration"
density_score: 0.82
author: "n03_builder"
created: "2026-04-07"
updated: "2026-04-07"
version: "1.0.0"
related:
  - bld_instruction_reasoning_strategy
  - kc_reasoning_strategy
  - p03_qg_reasoning_strategy
  - p01_kc_few_shot_example
  - bld_knowledge_card_reasoning_strategy
  - p01_kc_reasoning_trace
  - p03_rt_n03_builder_agent_20260406
  - bld_output_template_reasoning_strategy
  - p03_sp_reasoning_strategy_builder
  - p11_qg_router
---

# Router: Complexity

## Scoring Algorithm

Complexity score = weighted sum of 6 factors, each normalized to [0, 1]:

| Factor | Weight | Measurement | Example |
|--------|--------|-------------|---------|
| `token_est` | 0.20 | Expected output length (normalized by 4096) | Short answer=0.1, essay=0.8 |
| `reasoning` | 0.25 | Reasoning depth required (chain-of-thought steps) | Lookup=0.1, multi-step logic=0.9 |
| `tools` | 0.15 | Number of tool calls needed | 0 tools=0.0, 3+ tools=0.8 |
| `domain` | 0.20 | Domain specificity (specialized knowledge) | General=0.1, legal/medical=0.9 |
| `output` | 0.10 | Output structure complexity (format, schema) | Plain text=0.1, structured JSON=0.7 |
| `multi_step` | 0.10 | Sequential dependency between steps | Single=0.0, 5+ dependent steps=0.9 |

```python
def complexity_score(request: dict) -> float:
    factors = {
        "token_est": estimate_tokens(request) / 4096,
        "reasoning": classify_reasoning_depth(request),
        "tools": min(len(request.get("tools", [])) / 4, 1.0),
        "domain": domain_specificity(request["intent"]),
        "output": output_complexity(request.get("format", "text")),
        "multi_step": count_dependencies(request) / 5,
    }
    weights = {"token_est": 0.20, "reasoning": 0.25, "tools": 0.15,
               "domain": 0.20, "output": 0.10, "multi_step": 0.10}
    return sum(factors[k] * weights[k] for k in weights)
```

## Route Thresholds

| Score Range | Tier | Model | Use Cases | Avg Cost/req |
|-------------|------|-------|-----------|--------------|
| 0.00 – 0.44 | Local (Ollama) | llama3-8B | Lookups, formatting, simple Q&A | ~$0.00 |
| 0.45 – 0.69 | Hybrid | claude-sonnet | Summarization, code review, analysis | ~$0.02 |
| 0.70 – 1.00 | Cloud | claude-opus | Multi-step reasoning, specialized, creative | ~$0.15 |

## Scoring Examples

### Example 1: Simple (score = 0.18 → Local)
```
Intent: "What's the capital of France?"
token_est=0.05  reasoning=0.05  tools=0.0  domain=0.1  output=0.1  multi_step=0.0
Score = 0.05×0.20 + 0.05×0.25 + 0×0.15 + 0.1×0.20 + 0.1×0.10 + 0×0.10 = 0.033
→ Route: LOCAL
```

### Example 2: Medium (score = 0.54 → Hybrid)
```
Intent: "Summarize this 10-page PDF and extract key action items"
token_est=0.6  reasoning=0.4  tools=0.25  domain=0.3  output=0.5  multi_step=0.3
Score = 0.6×0.20 + 0.4×0.25 + 0.25×0.15 + 0.3×0.20 + 0.5×0.10 + 0.3×0.10 = 0.398
→ Route: HYBRID (borderline — hybrid handles safely)
```

### Example 3: Complex (score = 0.82 → Cloud)
```
Intent: "Design a microservice architecture for a payment system with PCI compliance"
token_est=0.9  reasoning=0.9  tools=0.5  domain=0.95  output=0.8  multi_step=0.8
Score = 0.9×0.20 + 0.9×0.25 + 0.5×0.15 + 0.95×0.20 + 0.8×0.10 + 0.8×0.10 = 0.82
→ Route: CLOUD
```

## Edge Cases

| Scenario | Behavior |
|----------|----------|
| Score exactly on threshold (0.45, 0.70) | Routes to higher tier (conservative) |
| Scoring function errors | Falls back to cloud (safest default) |
| Local model unavailable | Transparently routes to hybrid |
| Cloud rate-limited | Triggers fallback_chain (see `p02_fb_model_cascade`) |

## Fallback

Cloud (Claude API) is the universal fallback. If scoring fails or the target tier is unavailable, requests route to cloud to guarantee a response. Source: `records/core/python/complexity_router.py`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_reasoning_strategy]] | downstream | 0.22 |
| [[kc_reasoning_strategy]] | upstream | 0.22 |
| [[p03_qg_reasoning_strategy]] | downstream | 0.21 |
| [[p01_kc_few_shot_example]] | upstream | 0.18 |
| [[bld_knowledge_card_reasoning_strategy]] | upstream | 0.18 |
| [[p01_kc_reasoning_trace]] | downstream | 0.17 |
| [[p03_rt_n03_builder_agent_20260406]] | downstream | 0.17 |
| [[bld_output_template_reasoning_strategy]] | downstream | 0.17 |
| [[p03_sp_reasoning_strategy_builder]] | downstream | 0.17 |
| [[p11_qg_router]] | downstream | 0.17 |
