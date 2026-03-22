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

## ONDA 3: GENERATORS + EXAMPLES [EM PROGRESSO]
- [x] 3.1 Generators CORE: P01 + P02 + P03 + P04
- [x] 3.2 Meta-template v1 (_meta/META_TEMPLATE.md)
- [x] 3.3 Golden examples: P01 (kc domain), P02 (agent), P03 (prompt)
- [ ] 3.4 Generators QUALITY+SCALE (P05-P12)
- [ ] 3.5 Templates com {{vars}} para cada tipo CORE
- [x] 3.6 Migrar golden do codexa-core (Wave 4.2: 12 examples migrated)

## ONDA 4: MIGRACAO MASSIVA
- [ ] 638 KC > P01 | 701 HOP > P03 | 570 AGT > P02
- [ ] 238 FAT/ADW > P12 | 61 BLK dissolvidos
- [ ] Archive score < 7.0 (~500 files)

## ONDA 5: ANTI-FRAGILIDADE
- [ ] _custom/ + promotion + lifecycle + density validator

## ONDA 6: PRODUTO
- [ ] Bootstrap script + York wizard + boot multi-provider + dogfood

---

## EXAMPLES POR LP

| LP | Examples | Novos (Wave 4.2) | Total |
|----|----------|-------------------|-------|
| P01 Knowledge | 7 | +4 (quality_gate, orchestration, coding_skills, cicd) | 7 |
| P02 Model | 4 | +3 (catalogo_ml, gateway, amazon_ads) | 4 |
| P03 Prompt | 4 | +3 (satellite_orchestrator, sdk_builder, catalogo_ml) | 4 |
| P04 Tools | 3 | +2 (voice_pipeline, design_extractor) | 3 |
| **Total** | **18** | **+12** | **18** |

## METRICAS DA SESSAO
- Repos: codexa-core (22 commits) + CEX (8 commits)
- Grid: 6 satellites total (3 SHAKA research + 2 PYTHA + 1 EDISON distill + 1 EDISON migrate)
- Reports: 9 research (133KB) + 3 distillation (42KB) = 175KB
- Files CEX: 36 arquivos, ~65KB
- Ondas completas: 2.8 de 6

---
*Updated: 2026-03-22 | Next: Wave 3.4 (generators P05-P12)*