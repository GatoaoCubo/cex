# ROADMAP CEX - 6 Ondas

---

## ONDA 1: DESTILAR [COMPLETA]
- [x] 1.1 Selecionar top golden (score >= 9.5) do codexa-core
- [x] 1.2 Analisar padroes (3 reports: KC + TPL/HOP + AGT/SKL = 42KB)
- [x] 1.3 Criar P01/_schema.yaml v0 baseado em dados reais
- [x] 1.4 Criar _meta/meta_template approach (CODEX defines)
- [x] 1.5 Primeiro golden example (p01_kc_catalogo_proprio_mercado_livre)

## ONDA 2: SCHEMAS COMPLETOS [COMPLETA]
- [x] 2.1 P01-P04 CORE schemas (27 types)
- [x] 2.2 P05-P07+P11 QUALITY schemas (20 types)
- [x] 2.3 P08-P10+P12 SCALE schemas (21 types)
- [x] 2.4 Total: 12 schemas, 68 types defined
- [ ] 2.5 Generators para cada LP (P01 done, P02-P12 pending)

## ONDA 3: TEMPLATES + EXAMPLES [PROXIMO]
- [ ] 3.1 Templates com {{vars}} para cada tipo de cada LP
- [ ] 3.2 Migrar 50 golden KCs para P01/examples/
- [ ] 3.3 Migrar golden HOPs para P03/examples/
- [ ] 3.4 Meta-template v1 (gera templates de qualquer tipo)

## ONDA 4: MIGRACAO MASSIVA
- [ ] 638 KC>P01 | 701 HOP>P03 | 570 AGT>P02 | 238 FAT/ADW>P12

## ONDA 5: ANTI-FRAGILIDADE
- [ ] _custom/ + promotion engine + lifecycle + density validator

## ONDA 6: PRODUTO
- [ ] Bootstrap script + York wizard + boot multi-provider + dogfood

---
*Updated: 2026-03-22 | Ondas 1-2 completas em 1 sessao*