---
id: p01_kc_bling_erp_automation_boundary
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Bling ERP: Automation Boundary for Product Registration"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: knowledge_agent
domain: execution
quality: 9.1
tags: [bling, automation, boundary, tiering, human-in-the-loop, erp]
tldr: "44 Bling fields in 3 tiers: Tier1 auto via pipeline, Tier2 heuristic with override, Tier3 fiscal/physical data only by user."
when_to_use: "Define what the pipeline can fill automatically vs what requires human confirmation in Bling"
keywords: [automation_boundary, human_override, tier1_tier2_tier3, product_onboarding]
long_tails:
  - "Which Bling fields can be automated without a human operator"
  - "How to separate system fallback and user confirmation in ERP registration"
axioms:
  - "ALWAYS automate only what has a repeatable source or safe default"
  - "NEVER push sensitive fiscal data into blind automation"
linked_artifacts:
  primary: p01_kc_bling_erp_field_parametrization
  related: [p01_kc_zero_touch_execution]
density_score: 1.0
data_source: "https://developer.bling.com.br/homologacao"
related:
  - p01_kc_bling_erp_field_parametrization
  - bld_tools_subscription_tier
  - kc_subscription_tier
  - p01_kc_llm_benchmark_ecommerce_copy
  - p11_qg_agent_package
  - bld_examples_rate_limit_config
  - p01_kc_tag_grading_structured_data
  - bld_instruction_pricing_page
  - bld_output_template_subscription_tier
  - bld_instruction_subscription_tier
---

## Quick Reference

topic: automation boundary | scope: product registration in Bling | criticality: high
model: Tier 1 automatic | Tier 2 fallback with override | Tier 3 human

## Key Concepts

- Tier 1 covers repeatable fields or those derived by simple rules
- Tier 2 accepts heuristics but needs easy override
- Tier 3 depends on physical, fiscal, or contractual reality
- Good automation boundary reduces errors without hiding uncertainty

## Comparison

| Tier | Dominant Source | Example | System Action |
|------|----------------|---------|---------------|
| 1 | defaults/pipeline | name, SKU, images | fill directly |
| 2 | research/heuristic | price, brand, NCM | suggest and allow editing |
| 3 | operator/company | GTIN, PIS, supplier | block auto-fill |

| Category | Confidence | Fields | Policy |
|----------|------------|--------|--------|
| Commercial | high | title, description, status | automate |
| Operational | medium | weight, dimensions, stock | review |
| Fiscal | low-medium | NCM, CEST, tax rates | confirm |
| Unique identification | low | GTIN, batch, expiry | user defines |

## Golden Rules

- ALWAYS expose to the user everything that came from Tier 2 heuristics
- ALWAYS maintain audit trail of pipeline-defaulted values
- NEVER auto-fill GTIN, supplier, or fixed tax without proof
- ALWAYS degrade to draft when Tier 3 is incomplete

## Code

<!-- lang: python | purpose: route fields by automation confidence tier -->
```python
TIER_1 = {"nome", "codigo", "tipo", "situacao", "formato", "imagens"}
TIER_2 = {"preco", "marca", "pesoLiquido", "ncm", "cest"}
TIER_3 = {"gtin", "fornecedores", "pis", "cofins", "validade"}

def classify_field(field: str) -> str:
    if field in TIER_1:
        return "auto"
    if field in TIER_2:
        return "suggest"
    return "require_user"
```

## References

- external: https://developer.bling.com.br/homologacao
- external: https://www.bling.com.br/api-bling
- external: https://developer.bling.com.br/como-testar
- deepens: p01_kc_bling_erp_field_parametrization
- deepens: p01_kc_zero_touch_execution


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_bling_erp_field_parametrization]] | sibling | 0.36 |
| [[bld_tools_subscription_tier]] | downstream | 0.31 |
| [[kc_subscription_tier]] | sibling | 0.19 |
| [[p01_kc_llm_benchmark_ecommerce_copy]] | sibling | 0.19 |
| [[p11_qg_agent_package]] | downstream | 0.17 |
| [[bld_examples_rate_limit_config]] | downstream | 0.17 |
| [[p01_kc_tag_grading_structured_data]] | sibling | 0.16 |
| [[bld_instruction_pricing_page]] | downstream | 0.16 |
| [[bld_output_template_subscription_tier]] | downstream | 0.15 |
| [[bld_instruction_subscription_tier]] | downstream | 0.15 |
