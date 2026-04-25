---
id: p01_kc_llm_benchmark_ecommerce_copy
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "LLM Benchmark for PT-BR E-Commerce Copy"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: research_agent
domain: research
quality: 9.1
tags: [llm-benchmark, ecommerce, pt-br, copywriting, pricing, json]
tldr: "Claude Sonnet leads PT-BR quality and JSON; GPT-4o leads reliability; Gemini Flash and DeepSeek win on cost and volume."
when_to_use: "Choose LLM stack for copy, catalog or content automation in Portuguese"
keywords: [pt_br_copy, model_selection, json_reliability, throughput, token_cost]
long_tails:
  - "Which LLM to use for PT-BR e-commerce copy"
  - "How to balance PT-BR quality, cost and reliable JSON"
axioms:
  - "ALWAYS separate premium model from bulk model"
  - "NEVER promote Gemini 2.5 without your own PT-BR test"
linked_artifacts:
  primary: null
  related: [p01_kc_claude_model_capabilities_2026]
density_score: 1.0
data_source: "Comparative benchmark of throughput, uptime, price and PT-BR quality for commercial copy"
related:
  - bld_tools_model_card
  - bld_examples_model_card
  - p02_mc_google_gemini_2_5_pro
  - bld_examples_model_provider
  - p01_kc_claude_model_capabilities_2026
  - p01_kc_universal_llm
  - bld_config_fallback_chain
  - smoke_test_gemini_20260415
  - p06_bp_model_card
  - bld_tools_model_provider
---

## Quick Reference

topic: model selection | scope: PT-BR ecommerce copy | criticality: high
recommended stack: Claude for premium, DeepSeek bulk, GPT-4o backup, Gemini for latency

## Key Concepts

- Claude Sonnet wins on PT-BR quality and strict JSON
- GPT-4o wins on uptime and operational predictability
- Gemini Flash delivers lowest latency cost per request
- DeepSeek V3 dominates massive workloads by price

## Comparison

| Model | Main strength | Numeric signal | Ideal use |
|-------|---------------|----------------|-----------|
| Claude Sonnet | PT-BR quality | JSON 100% with constraints | Landing and premium copy |
| GPT-4o | Reliability | 99.6% uptime, 99.9% SLA | Backup and critical flows |
| Gemini 2.5 Flash | Speed | TTFT 0.34s, 249 t/s | High volume and low latency |
| DeepSeek V3 | Cost | 53x cheaper than Claude output | Bulk catalog and SEO |

| Cost 1M in + 1M out | Value |
|----------------------|-------|
| DeepSeek V3 | ~$0.34 |
| Gemini 2.5 Flash | ~$2.80 |
| GPT-4o | ~$12.50 |
| Claude Sonnet | ~$18.00 |

## Golden Rules

- ALWAYS use premium model only where margin pays for the difference
- ALWAYS measure JSON compliance before automation without review
- NEVER assume English benchmark as proxy for PT-BR
- ALWAYS maintain operational fallback between vendors

## Code

<!-- lang: python | purpose: route copy tasks by quality and cost -->
```python
def route_copy_job(task: str, requires_json: bool, scale: str) -> str:
    if requires_json or "premium" in task:
        return "claude-sonnet"
    if scale == "bulk":
        return "deepseek-v3"
    if "sla" in task or "critical" in task:
        return "gpt-4o"
    return "gemini-2.5-flash"
```

## References

- external: https://www.anthropic.com/pricing
- external: https://openai.com/api/pricing/
- external: https://ai.google.dev/pricing
- external: https://api-docs.deepseek.com/quick_start/pricing/
- deepens: p01_kc_claude_model_capabilities_2026


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_model_card]] | downstream | 0.31 |
| [[bld_examples_model_card]] | downstream | 0.29 |
| [[p02_mc_google_gemini_2_5_pro]] | downstream | 0.28 |
| [[bld_examples_model_provider]] | downstream | 0.26 |
| [[p01_kc_claude_model_capabilities_2026]] | sibling | 0.23 |
| [[p01_kc_universal_llm]] | sibling | 0.23 |
| [[bld_config_fallback_chain]] | downstream | 0.21 |
| [[smoke_test_gemini_20260415]] | downstream | 0.21 |
| [[p06_bp_model_card]] | downstream | 0.20 |
| [[bld_tools_model_provider]] | downstream | 0.19 |
