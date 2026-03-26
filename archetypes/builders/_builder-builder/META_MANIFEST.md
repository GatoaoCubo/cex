---
meta: true
file_position: 1/13
pillar: P02
llm_function: BECOME
purpose: Meta-template for generating MANIFEST.md of any type-builder
---

# {{builder_name}}
<!-- Este meta-file gera o MANIFEST.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: _schema.yaml do tipo-alvo, TAXONOMY_LAYERS.yaml, SEED_BANK.yaml -->

<!-- NOTA: {{builder_name}} = kebab-case do tipo. Ex: model-card-builder, signal-builder -->
<!-- NOTA: {{type_name}} = snake_case do tipo. Ex: model_card, signal, quality_gate -->
<!-- NOTA: {{lp}} = LP do tipo-alvo (P01-P12). Buscar em TAXONOMY_LAYERS.yaml -->
<!-- NOTA: {{lp_chief}} = {lp}-chief. Ex: p02-chief, p01-chief -->
<!-- NOTA: {{domain}} = geralmente igual a {{type_name}}, mas pode variar -->
<!-- NOTA: {{type_name_kebab}} = kebab-case do tipo. Ex: model-card, knowledge-card -->
<!-- NOTA: {{tags}} = [type-builder, {{type_name_kebab}}, {{lp}}, specialist, ...extras] -->

```yaml
---
id: {{builder_name}}
kind: type_builder
pillar: {{lp}}
parent: {{lp_chief}} [PLANNED]
domain: {{type_name}}
llm_function: BECOME
version: 1.0.0
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: {{author}}
tags: [type-builder, {{type_name_kebab}}, {{lp}}, specialist]
---
```

## Identity
Especialista em construir `{{type_name}}` — {{one_line_description}}.
<!-- NOTA: {{one_line_description}} = extrair de TAXONOMY_LAYERS.yaml types[].description ou _schema.yaml purpose -->
<!-- Acrescente 1-2 frases sobre dominio, ferramentas, e o que produz -->

## Capabilities
<!-- NOTA: 4-6 bullets descrevendo o que o builder PODE fazer -->
<!-- Padrao observado nos 4 builders existentes: -->
- Pesquisar/analisar {{domain_knowledge}} para produzir {{type_name}}
- Produzir {{type_name}} com frontmatter completo ({{field_count}} campos)
- Validar artifact contra quality gates ({{hard_count}} HARD + {{soft_count}} SOFT)
- {{capability_extra_1}}
<!-- NOTA: {{field_count}} = contar campos em _schema.yaml -->
<!-- NOTA: {{hard_count}}/{{soft_count}} = definir em QUALITY_GATES.md -->

## Routing
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}, {{keyword_4}}]
triggers: "{{trigger_phrase_1}}", "{{trigger_phrase_2}}", "{{trigger_phrase_3}}"
<!-- NOTA: keywords = 4-8 termos que ativam este builder via brain_query -->
<!-- NOTA: triggers = 2-3 frases naturais que um user diria -->

## Crew Role
In a crew, I handle {{ROLE_CAPS}}.
I answer: "{{one_question_this_builder_answers}}"
I do NOT handle: {{exclusion_1}}, {{exclusion_2}}, {{exclusion_3}}.
<!-- NOTA: {{ROLE_CAPS}} = papel em CAPS. Ex: MODEL DOCUMENTATION, KNOWLEDGE DISTILLATION -->
<!-- NOTA: {{exclusions}} = tipos vizinhos no mesmo LP ou frequentemente confundidos -->
<!-- Buscar confusoes em TAXONOMY_LAYERS.yaml overlaps e na _schema.yaml do LP -->
