---
id: p01_kc_llm_benchmark_ecommerce_copy
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "LLM Benchmark para Copy de E-Commerce em PT-BR"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: research_agent
domain: research
quality: 9.1
tags: [llm-benchmark, ecommerce, pt-br, copywriting, pricing, json]
tldr: "Claude Sonnet lidera qualidade PT-BR e JSON; GPT-4o lidera confiabilidade; Gemini Flash e DeepSeek vencem em custo e volume."
when_to_use: "Escolher stack LLM para copy, catalogo ou automacao de conteudo em portugues"
keywords: [pt_br_copy, model_selection, json_reliability, throughput, token_cost]
long_tails:
  - "Qual LLM usar para copy de e-commerce em portugues brasileiro"
  - "Como balancear qualidade PT-BR, custo e JSON confiavel"
axioms:
  - "SEMPRE separar modelo premium de modelo bulk"
  - "NUNCA promover Gemini 2.5 sem teste PT-BR proprio"
linked_artifacts:
  primary: null
  related: [p01_kc_claude_model_capabilities_2026]
density_score: 1.0
data_source: "Benchmark comparativo de throughput, uptime, preco e qualidade PT-BR para copy comercial"
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
stack recomendada: Claude para premium, DeepSeek bulk, GPT-4o backup, Gemini para latencia

## Conceitos Chave

- Claude Sonnet ganha em qualidade PT-BR e JSON estrito
- GPT-4o ganha em uptime e previsibilidade operacional
- Gemini Flash entrega menor custo de latencia por request
- DeepSeek V3 domina workloads massivos por preco

## Comparativo

| Modelo | Forca principal | Sinal numerico | Uso ideal |
|--------|------------------|----------------|-----------|
| Claude Sonnet | Qualidade PT-BR | JSON 100% com constraints | Landing e premium copy |
| GPT-4o | Confiabilidade | 99.6% uptime, 99.9% SLA | Backup e fluxos criticos |
| Gemini 2.5 Flash | Velocidade | TTFT 0.34s, 249 t/s | Alto volume e baixa latencia |
| DeepSeek V3 | Custo | 53x mais barato que Claude output | Bulk catalog e SEO |

| Custo 1M in + 1M out | Valor |
|----------------------|-------|
| DeepSeek V3 | ~$0.34 |
| Gemini 2.5 Flash | ~$2.80 |
| GPT-4o | ~$12.50 |
| Claude Sonnet | ~$18.00 |

## Regras de Ouro

- SEMPRE usar modelo premium so onde margem paga a diferenca
- SEMPRE medir JSON compliance antes de automacao sem review
- NUNCA assumir benchmark em ingles como proxy de PT-BR
- SEMPRE manter fallback operacional entre vendors

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
