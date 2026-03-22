# Generator: P07 Evals

## QUANDO USAR
- Testar agente/prompt de forma reproduzivel
- Criar benchmark de performance (latencia, custo, qualidade)
- Definir golden test (caso referencia quality 9.5+)
- Documentar rubric de scoring (5D, 12LP, custom)

## TIPOS (ver _schema.yaml)
| Tipo | Naming | Uso |
|------|--------|-----|
| unit_eval | p07_ue_{{target}}.md + .yaml | Teste unitario de agent/prompt |
| smoke_eval | p07_se_{{scope}}.md | Sanidade rapida (< 30s) |
| e2e_eval | p07_e2e_{{pipeline}}.md + .yaml | Teste de pipeline completo |
| benchmark | p07_bm_{{metric}}.md + .yaml | Medicao performance |
| golden_test | p07_gt_{{case}}.md + .yaml | Caso referencia (9.5+) |
| scoring_rubric | p07_sr_{{framework}}.md + .yaml | Criterio de avaliacao |

## PASSO A PASSO
1. SCOUT: verificar se eval similar ja existe para o target
2. CLASSIFICAR: unit, smoke, e2e, benchmark, golden ou rubric
3. DEFINIR input fixo (dado concreto, nao "exemplo generico")
4. DEFINIR expected output (resposta exata ou criterios mensuraveis)
5. CRIAR assertion rules (match exato, contains, regex, score >= N)
6. ESTABELECER baseline (primeira execucao = referencia)
7. DEFINIR pass/fail threshold (ex: score >= 8.0, latencia < 5s)
8. INCLUIR edge cases (min 2: input vazio, input maximo)
9. VALIDAR contra P07/_schema.yaml (max_bytes: 1024-2048)
10. SALVAR dual output (.md descritivo + .yaml executavel)

## ANTI-PATTERNS
- Eval sem input fixo (resultado muda a cada run = inutil)
- Golden test com score < 9.5 (nao eh golden, eh exemplo)
- Benchmark sem baseline (numero isolado nao informa)
- Rubric com criterios subjetivos ("good quality")
- Smoke eval que demora > 30s (nao eh smoke, eh integration)
- Assertion vaga ("output should be reasonable")

## QUALITY TIERS
- Elite (90%+): Eval executavel + baseline + 3+ edge cases + historico de runs
- High (80-88%): Input/output fixos + assertions claras + threshold
- Standard (70-78%): Input/output documentados sem automacao
- Low (<65%): REJEITAR — eval sem criterio mensuravel nao eh eval

---
*Generator v1.0 | Layer: SCALE | 2026-03-22*
