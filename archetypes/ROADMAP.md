# ROADMAP CEX - 6 Ondas

---

## ONDA 1: DESTILAR [COMPLETA]
- [x] 1.1 Selecionar golden (score >= 9.5) do codexa-core
- [x] 1.2 Grid 3 satellites: 42KB de analise (KC + TPL/HOP + AGT/SKL)
- [x] 1.3 P01/_schema.yaml v0 baseado em dados reais
- [x] 1.4 Primeiro golden example (p01_kc_catalogo_proprio_mercado_livre)

## ONDA 2: SCHEMAS 12LP [COMPLETA]
- [x] 2.1 P01-P04 CORE schemas (27 types)
- [x] 2.2 P05-P07+P11 QUALITY schemas (20 types)
- [x] 2.3 P08-P10+P12 SCALE schemas (21 types)
- [x] 2.4 Total: 12 schemas, 68 types defined

## ONDA 3: GENERATORS + EXAMPLES [COMPLETA]
- [x] 3.1 Generators CORE: P01 + P02 + P03 + P04
- [x] 3.2 Meta-template v1 (archetypes/META_TEMPLATE.md)
- [x] 3.3 Golden examples: P01(7) + P02(4) + P03(4) + P04(3) = 18 total
- [x] 3.4 Generators QUALITY+SCALE: P05 + P06 + P07 + P08 + P09 + P10 + P11 + P12
- [x] 3.5 Templates CORE: 7 (P01:3 + P02:1 + P03:1 + P04:1 + P05:1)
- [x] 3.6 Validation chain test pass (archetypes/VALIDATION_REPORT.md)

## ONDA 4: GOLDEN MIGRATION [COMPLETA]
- [x] 4.1 Migration map: 9916 arquivos classificados em LP buckets
- [x] 4.2 12 golden examples migrados (4 KC + 3 agent + 3 prompt + 2 skill)
- [x] 4.3 GOLDEN_CANDIDATES.md: 22 candidatos identificados, priority queue definida
- [ ] 4.4 Mass migration (638 KC | 701 HOP | 570 AGT) — DEFERRED para Wave 6

## ONDA 5: ANTI-FRAGILIDADE [EM PROGRESSO]
- [x] 5.1 Meta-docs v3 (CODEX + ROADMAP + README atualizados com estado real)
- [x] 5.2 Density report (archetypes/DENSITY_REPORT.md com analise dos 18 examples)
- [ ] 5.3 QUALITY+SCALE templates (P06-P12: 7 templates faltando)
- [ ] 5.4 _custom/ extensibility + lifecycle validator + promotion script
- [ ] 5.5 Density validator no pre-commit (rejeita score < 0.80)

## ONDA 6: PRODUTO
- [ ] 6.1 Bootstrap script (cria LP structure em novo repo)
- [ ] 6.2 York wizard (onboarding interativo)
- [ ] 6.3 Mass migration final (638 KC + 701 HOP + 570 AGT)
- [ ] 6.4 Dogfood: usar CEX para gerar CEX (flywheel)

---

## EXAMPLES POR LP

| LP | Examples | Templates | Generator | Status |
|----|----------|-----------|-----------|--------|
| P01 Knowledge | 7 | 3 | SIM | CORE completo |
| P02 Model | 4 | 1 | SIM | CORE completo |
| P03 Prompt | 4 | 1 | SIM | CORE completo |
| P04 Tools | 3 | 1 | SIM | CORE completo |
| P05 Output | 0 | 1 | SIM | template only |
| P06 Schema | 0 | 0 | SIM | generator only |
| P07 Evals | 0 | 0 | SIM | generator only |
| P08 Architecture | 0 | 0 | SIM | generator only |
| P09 Config | 0 | 0 | SIM | generator only |
| P10 Memory | 0 | 0 | SIM | generator only |
| P11 Feedback | 0 | 0 | SIM | generator only |
| P12 Orchestration | 0 | 0 | SIM | generator only |
| **Total** | **18** | **7** | **12/12** | Wave 5 |

## METRICAS ACUMULADAS

| Metrica | Valor |
|---------|-------|
| CEX commits | 15 |
| Total MD files | 46 |
| Repo size | ~65KB |
| Schemas | 12 (68 tipos) |
| Generators | 12/12 |
| Templates | 7 |
| Examples | 18 |
| Density media | 88.6% |
| Satellites usados | 7 (SHAKA x3 + PYTHA x2 + EDISON x2) |
| Ondas completas | 4 de 6 |

---
*Updated: 2026-03-22 | Next: Wave 5.3 (QUALITY+SCALE templates P06-P12)*
