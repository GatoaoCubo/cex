---
meta: true
file_position: 8/13
pillar: P07
llm_function: GOVERN
purpose: Meta-template for generating EXAMPLES.md of any kind-builder
---

# Examples: {{builder_name}}
<!-- Este meta-file gera o EXAMPLES.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: SCHEMA.md + OUTPUT_TEMPLATE.md + QUALITY_GATES.md ja gerados -->
<!-- INPUT RECOMENDADO: exemplos reais do tipo se existirem em {{lp_dir}}/examples/ -->

```yaml
---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of {{type_name}} artifacts
pattern: few-shot learning — LLM reads these before producing
---
```

## Golden Example

INPUT: "{{natural_language_request}}"
<!-- NOTA: {{natural_language_request}} = frase que um user diria para pedir este tipo -->
<!-- Exemplos observados: -->
<!-- - model_card: "Documenta o Claude Sonnet 4 pra decidir roteamento" -->
<!-- - KC: "Destila conhecimento sobre prompt caching para otimizar custos LLM" -->
<!-- - signal: "Emit completion signal for codex after finishing signal-builder" -->
<!-- - quality_gate: "Define gate pra knowledge_cards antes de publicar no pool" -->

OUTPUT:
<!-- NOTA: Produzir um artifact COMPLETO usando OUTPUT_TEMPLATE.md -->
<!-- O exemplo DEVE passar TODOS os HARD gates e >= 95% dos SOFT gates -->
<!-- Usar dados REAIS (nao inventados) sempre que possivel -->

```{{machine_format}}
{{complete_artifact_following_output_template}}
```
<!-- NOTA: {{machine_format}} = yaml (para md kinds) ou json (para signal) -->
<!-- Preencher TODOS os campos do template com valores concretos -->
<!-- Incluir body completo com todas as secoes obrigatorias -->

WHY THIS IS GOLDEN:
<!-- NOTA: Listar 6-10 razoes mapeadas para gates especificos -->
<!-- Padrao UNIVERSAL observado em todos os 4 builders: -->
- quality: null ({{hard_gate_quality}} pass)
- id matches {{id_prefix}} pattern ({{hard_gate_id}} pass)
- kind: {{type_name}} ({{hard_gate_type}} pass)
- {{required_fields_count}} required fields present ({{hard_gate_fields}} pass)
- {{soft_gate_check_1}} ({{soft_gate_id_1}} pass)
- {{soft_gate_check_2}} ({{soft_gate_id_2}} pass)
<!-- NOTA: Referenciar gate IDs (H01, S03, etc.) de QUALITY_GATES.md -->

## Anti-Example

INPUT: "{{simple_request}}"

BAD OUTPUT:
```{{machine_format}}
{{deliberately_bad_artifact}}
```
<!-- NOTA: Incluir 6-10 erros comuns para este tipo -->
<!-- Padrao UNIVERSAL observado: -->
<!-- 1. id sem prefixo correto -->
<!-- 2. lp ausente -->
<!-- 3. quality com valor (nao null) -->
<!-- 4. tipo do campo errado (string vs integer, string vs list) -->
<!-- 5. body com filler/prose ao inves de dados concretos -->
<!-- 6. secoes obrigatorias ausentes -->

FAILURES:
<!-- NOTA: Lista numerada com gate ID e descricao da falha -->
1. id: no `{{id_prefix}}` prefix -> {{hard_gate_id}} FAIL
2. lp: missing -> {{hard_gate_lp}} FAIL
3. quality: self-assigned -> {{hard_gate_quality}} FAIL
4. {{failure_4}} -> {{gate_4}} FAIL
5. {{failure_5}} -> {{gate_5}} FAIL
6. {{failure_6}} -> {{gate_6}} FAIL
<!-- NOTA: Mapear CADA falha para o gate exato (H01-H10, S01-S20) -->
<!-- Incluir falhas tanto HARD (bloqueiam) quanto SOFT (reduzem score) -->
