# Amazon Analytics — Domain Knowledge

## ACOS Mastery

### Core Formulas

```
ACOS = Ad Spend / Ad Revenue * 100
ROAS = Ad Revenue / Ad Spend  (inverse of ACOS / 100)
MPA  = Profit Margin % - ACOS %
TACOS = Ad Spend / Total Revenue * 100
```

### ACOS Decision Matrix

| ACOS | Diagnostico | Acao Recomendada |
|------|-------------|------------------|
| <10% | Excelente | Escalar orcamento, manter targeting |
| 10-15% | Bom | Manter, otimizar keywords marginais |
| 15-20% | Aceitavel | Negativar keywords ruins, ajustar lances |
| 20-30% | Atencao | Reestruturar campanhas, revisar targeting |
| 30-46% | Critico | Pausar campanhas fracas, revalidar produto |
| >46% | Inviavel | Pausar imediatamente, reavaliar produto |

### ACOS Target Rules

- **ACOS Objetivo**: Metade da margem de lucro
- **ACOS Maximo**: Igual a margem de lucro (break-even em ads)
- Example: Margin 40% -> ACOS target 20%, ACOS max 40%
- MPA positive = profitable ads; MPA negative = losing money on every ad sale

---

## Product Validation (PPD Method)

### PPD Scorecard Weights

| Criterio | Peso | Verde | Amarelo | Vermelho |
|----------|------|-------|---------|----------|
| Vendas/30d | 30% | 200+ | 50-199 | <50 |
| Vendedores | 20% | 3-15 | 1-2 ou 16-30 | 0 ou 30+ |
| Avaliacoes | 15% | 50+ | 10-49 | <10 |
| Rating | 10% | 4.0+ | 3.5-3.9 | <3.5 |
| Preco margem | 25% | >30% | 15-30% | <15% |

### Seller Count Interpretation

- 0 sellers: product may not exist (opportunity OR no demand)
- 1-2 sellers: monopoly risk — if they leave, no validation
- 3-15 sellers: healthy competition, demand proven
- 16-30 sellers: crowded but manageable
- 30+ sellers: commoditized, Buy Box war, avoid unless differentiated

### Sweet Spot: 200-600 sales/month

- Under 200: insufficient volume to validate demand
- Over 600: check if top seller concentration is risk (1 seller = 80%+ of sales?)

---

## Conversion Rate Benchmarks

| Taxa | Status | Acao |
|------|--------|------|
| 4%+ | Excelente | Nao mexer, escalar Ads |
| 2-4% | Bom | Manter, pequenos ajustes |
| 1.5-2% | Medio | Revisar imagens e bullet points |
| 1-1.5% | Baixo | Otimizar urgente (titulo, imagens, preco) |
| <1% | Critico | Recriar listagem do zero |

---

## Maturation Curve (12-Month Timeline)

```
Mes 1:  Ads 90% | Org 10% | ACOS esperado: 25-40%
Mes 3:  Ads 70% | Org 30% | ACOS esperado: 15-25%
Mes 6:  Ads 50% | Org 50% | ACOS esperado: 10-20%
Mes 12: Ads 30% | Org 70% | ACOS esperado: 8-15%
```

### Interpretation

- Organic share growing = healthy listing rank signal
- Organic share stagnant after month 6 = listing quality problem
- Ads share never dropping = product may not be ranking organically

---

## Campaign Type Benchmarks

| Tipo | ACOS Esperado | Uso Principal |
|------|--------------|---------------|
| Auto | 25-40% | Discovery de keywords |
| Manual Exact | 8-20% | Conversao eficiente |
| Manual Broad | 15-30% | Expansao de alcance |
| Brand Defense | 5-12% | Protecao de marca |
| Display | 20-45% | Remarketing e awareness |

---

## Business Intelligence Formulas

```
Faturamento Total = Organico + Patrocinado
Split% Patrocinado = Ad Sales / Total Sales * 100
Custo Real por Pedido = Total Spend / Total Orders
ROI Ads = (Ad Sales - COGS - Ad Spend) / Ad Spend * 100
```

### Minimum Data Requirements

- Campaign decisions: >= 7 days, >= 20 clicks
- Product validation: 30-day window minimum
- Seasonal adjustments: compare same period prior year
