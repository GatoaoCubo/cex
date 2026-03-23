# Amazon Analytics Agent — Quick Start

60-second self-contained reference for LLM navigation.

## What It Does

Analyzes Amazon campaign performance, validates product viability (PPD), tracks listing conversions, and provides business intelligence for Brazilian sellers.

## Key Metrics

| Metric | Formula | What It Means |
|--------|---------|---------------|
| **ACOS** | Ad Spend / Ad Sales | Lower = more efficient ads |
| **ROAS** | Ad Sales / Ad Spend | Higher = better return |
| **TACOS** | Ad Spend / Total Sales | Measures ad dependency |
| **MPA** | Margin - ACOS | Profit after ads (must be > 0) |
| **CVR** | Orders / Clicks | Listing effectiveness |

## ACOS Tiers

| ACOS | Diagnosis | Action |
|------|-----------|--------|
| <10% | Excelente | Scale budget |
| 10-15% | Bom | Maintain + optimize |
| 15-20% | Aceitavel | Negative keywords + bid adjust |
| 20-30% | Atencao | Restructure campaigns |
| 30-46% | Critico | Pause weak campaigns |
| >46% | Inviavel | Pause immediately |

**Golden rule**: ACOS target = half your margin. ACOS max = your margin.

## PPD Scorecard

| Criterio | Verde | Amarelo | Vermelho |
|----------|-------|---------|----------|
| Vendas/30d | 200+ | 50-199 | <50 |
| Vendedores | 3-15 | 1-2 or 16-30 | 0 or 30+ |
| Avaliacoes | 50+ | 10-49 | <10 |
| Rating | 4.0+ | 3.5-3.9 | <3.5 |
| Margem | >30% | 15-30% | <15% |

## Conversion Benchmarks

| Rate | Status | Action |
|------|--------|--------|
| 4%+ | Excelente | Scale ads |
| 2-4% | Bom | Maintain |
| 1.5-2% | Medio | Review images + bullets |
| 1-1.5% | Baixo | Optimize urgent |
| <1% | Critico | Rebuild listing |

## Maturation Timeline

```
Month 1:  Ads 90% | Org 10% | ACOS 25-40%
Month 3:  Ads 70% | Org 30% | ACOS 15-25%
Month 6:  Ads 50% | Org 50% | ACOS 10-20%
Month 12: Ads 30% | Org 70% | ACOS 8-15%
```

## File Map

| File | Purpose |
|------|---------|
| manifest.yaml | Agent identity, capabilities, integrations |
| system_instruction.md | Self-contained LLM prompt |
| instructions.md | Full execution protocol with all workflows |
| prime.md | Persona, philosophy, decision framework |
| architecture.md | System components, data flow |
| output_template.md | Structured output formats per operation |
| examples.md | 3 complete I/O worked examples |
| error_handling.md | 6 failure modes with recovery |
| tools_and_apis.md | SP-API endpoints, Seller Central |
| data/domain_knowledge.md | ACOS mastery, PPD scorecard, benchmarks |
| data/input_schema.yaml | Input validation schema |
