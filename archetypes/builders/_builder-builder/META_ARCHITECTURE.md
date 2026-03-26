---
meta: true
file_position: 9/13
lp: P08
llm_function: CONSTRAIN
purpose: Meta-template for generating ARCHITECTURE.md of any type-builder
---

# Architecture: {{type_name}} in the CEX
<!-- Este meta-file gera o ARCHITECTURE.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: TAXONOMY_LAYERS.yaml (posicao + overlaps), _schema.yaml -->

```yaml
---
lp: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of {{type_name}} in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---
```

## Boundary
{{type_name}} EH: {{boundary_is_description}}.
<!-- NOTA: {{boundary_is_description}} = o que o tipo EH em uma frase densa -->
<!-- Exemplos observados: -->
<!-- - model_card: "spec tecnica de LLM (capacidades, custos, limites, status lifecycle)" -->
<!-- - KC: "fato atomico destilado, pesquisavel, versionado, com densidade >= 0.80" -->
<!-- - signal: "evento runtime atomico emitido por um satellite para informar status" -->
<!-- - quality_gate: "barreira de qualidade com score numerico (pass/fail + weighted dimensions)" -->

{{type_name}} NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| {{confused_type_1}} | {{why_not_1}} | {{correct_lp}} {{correct_type_1}} |
| {{confused_type_2}} | {{why_not_2}} | {{correct_lp}} {{correct_type_2}} |
| {{confused_type_3}} | {{why_not_3}} | {{correct_lp}} {{correct_type_3}} |
<!-- NOTA: 3-5 tipos confundidos. Buscar em: -->
<!-- 1. TAXONOMY_LAYERS.yaml overlaps (pares com severity high/medium) -->
<!-- 2. Tipos no MESMO LP (compartilham namespace) -->
<!-- 3. Tipos com nomes similares em OUTROS LPs -->
<!-- Padrao da frase "Por que NAO": "{confused} VERBO. {type_name} VERBO_DIFERENTE." -->

Regra: "{{decision_question}}" -> {{type_name}}.
<!-- NOTA: {{decision_question}} = pergunta que se respondida "sim" => usar este tipo -->
<!-- Exemplos: -->
<!-- - model_card: "o que este LLM PODE e quanto CUSTA?" -->
<!-- - KC: "qual o fato essencial sobre este topico?" -->
<!-- - signal: "o que aconteceu agora?" -->
<!-- - quality_gate: "o que deve passar antes de publicar?" -->

## Position in {{flow_name}}
<!-- NOTA: Diagrama ASCII mostrando onde o tipo se encaixa no fluxo -->
<!-- {{flow_name}} varia: "Boot Flow", "Knowledge Flow", "Runtime Flow", etc. -->

```text
{{flow_diagram}}
```
<!-- NOTA: Diagrama com setas mostrando etapas: -->
<!-- - model_card: boot_config → model_card (layer 0) → system_prompt → agent -->
<!-- - KC: Raw Source → Research → KC → Brain Index → Retrieval → Agent -->
<!-- - signal: dispatch_rule → handoff → execution → signal → monitor -->
<!-- - quality_gate: artifact produced → quality_gate check → publish/reject -->
<!-- Indicar ONDE neste fluxo o tipo se posiciona -->

{{type_name}} is {{layer_description}}.
<!-- NOTA: Descricao da camada: "INFRASTRUCTURE", "CONTENT LAYER", etc. -->

## Dependency Graph

```text
{{type_name}} <--{{rel_1}}-- {{dependent_1}} ({{why_1}})
{{type_name}} <--{{rel_2}}-- {{dependent_2}} ({{why_2}})
{{type_name}} --independent-- {{independent_types}}
```
<!-- NOTA: Tipos de relacao observados: -->
<!-- used_by, queried_by, injected_in, referenced_by, consumed_by -->
<!-- implements, uses_criteria, triggers, emitted_after, may_trigger -->
<!-- Buscar dependencias em TAXONOMY_LAYERS.yaml e nos outros builders -->

## Fractal Position
LP: {{lp}} ({{lp_description}})
Function: {{llm_function_primary}}
Scale: L0 ({{scale_description}})
<!-- NOTA: {{lp_description}} = ex: "Model — who the entity IS", "Knowledge — what the entity KNOWS" -->
<!-- NOTA: {{llm_function_primary}} = funcao principal do tipo (GOVERN, INJECT, COLLABORATE, etc.) -->
<!-- NOTA: {{scale_description}} = ex: "infrastructure artifact", "content artifact", "runtime event" -->
<!-- Incluir 1 frase sobre o que torna este tipo unico no LP -->
