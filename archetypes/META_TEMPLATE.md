# Meta-Template v1.0
# O template que gera TODOS os outros templates do CEX
# Edison usa este arquivo para gerar templates de qualquer LP

## COMO USAR

1. Edison recebe: "criar template para P{{N}} {{type}}"
2. Edison le: este meta-template
3. Edison le: P{{N}}_{{lp}}/_schema.yaml (campos do tipo)
4. Edison gera: P{{N}}_{{lp}}/templates/tpl_{{type}}.md + .yaml
5. Edison valida: contra _schema.yaml
6. Edison commita com quality >= 9.0

## TEMPLATE DE SAIDA (.md)



## TEMPLATE DE SAIDA (.yaml)



## REGRAS DE GERACAO

- NUNCA gerar campo vazio (TBD, TODO, placeholder)
- SEMPRE incluir example concreto em cada variavel
- SEMPRE calcular density (estimar tokens uteis / total)
- SEMPRE incluir semantic_bridge se quality >= 8.0
- SEMPRE dual output: .md (humano) + .yaml (LLM)
- MAX 2KB por template (o template em si, nao a instancia)

## SECOES POR TIPO (referencia rapida)

| LP | Tipo | Secoes obrigatorias |
|----|------|---------------------|
| P01 | knowledge_card (domain) | quick_ref, conceitos, fases, regras, flow |
| P01 | knowledge_card (meta) | summary, spec_table, patterns, anti, refs |
| P02 | agent | arch, when_to_use, capabilities, integration, quality |
| P03 | prompt_template | purpose, variables, body, gates, examples, bridge |
| P04 | skill | purpose, phases, anti_patterns, metrics |
| P07 | eval | setup, execute, assert, teardown |
| P08 | pattern | problem, solution, consequences, example |
| P12 | workflow | trigger, steps, output, rollback |

## EVOLUCAO

Este meta-template melhora durante uso:
1. Gera batch de templates
2. Avalia qualidade dos gerados
3. Identifica gaps (campo faltando, formato ruim)
4. Atualiza este arquivo
5. Re-gera templates melhorados
6. Repete ate quality >= 9.5

---
*Meta-Template v1.0 | Shokunin: builds itself better | 2026-03-22*