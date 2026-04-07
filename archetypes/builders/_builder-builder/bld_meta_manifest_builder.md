---
meta: true
file_position: 1/13
pillar: P02
llm_function: BECOME
purpose: Meta-template for generating MANIFEST.md of any kind-builder
quality: 9.1
title: "Meta Manifest Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# {{builder_name}}
<!-- This meta-file generates the MANIFEST.md of any builder -->
<!-- REQUIRED INPUT: _schema.yaml do type-target, TAXONOMY_LAYERS.yaml, SEED_BANK.yaml -->

<!-- NOTE: {{builder_name}} = kebab-case of the type. Ex: model-card-builder, signal-builder -->
<!-- NOTE: {{type_name}} = snake_case of the type. Ex: model_card, signal, quality_gate -->
<!-- NOTE: {{lp}} = Pillar of the target type (P01-P12). Look up in TAXONOMY_LAYERS.yaml -->
<!-- NOTE: {{lp_chief}} = {lp}-chief. Ex: p02-chief, p01-chief -->
<!-- NOTE: {{domain}} = usually same as {{type_name}}, but may vary -->
<!-- NOTE: {{type_name_kebab}} = kebab-case of the type. Ex: model-card, knowledge-card -->
<!-- NOTE: {{tags}} = [kind-builder, {{type_name_kebab}}, {{lp}}, specialist, ...extras] -->

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
tags: [kind-builder, {{type_name_kebab}}, {{lp}}, specialist]
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}, {{keyword_4}}]
triggers: ["{{trigger_phrase_1}}", "{{trigger_phrase_2}}"]
geo_description: >
  L1: {{what_it_does}}. L2: {{how_it_does_it}}. L3: {{when_to_use_it}}.
---
```

<!-- NOTE: keywords = 4-8 routing/search terms. Extract from ## Routing body existente -->
<!-- NOTE: triggers = 2-4 frases naturais that ativam this builder -->
<!-- NOTE: geo_description = 3 semantic layers (L1=o que, L2=como, L3=quando). Min 50 chars -->

## Identity
Specialist in building `{{type_name}}` — {{one_line_description}}.
<!-- NOTE: {{one_line_description}} = extract from TAXONOMY_LAYERS.yaml kinds[].description or _schema.yaml purpose -->
<!-- Add 1-2 frases about domain, tools, and o that produz -->

## Capabilities
<!-- NOTE: 4-6 bullets descrevendo o that the builder PODE fazer -->
<!-- Pattern observed in the 4 existing builders: -->
1. Research/analisar {{domain_knowledge}} for produzir {{type_name}}
2. Produce {{type_name}} with frontmatter complete ({{field_count}} fields)
3. Validate artifact against quality gates ({{hard_count}} HARD + {{soft_count}} SOFT)
4. {{capability_extra_1}}
<!-- NOTE: {{field_count}} = count fields in _schema.yaml -->
<!-- NOTE: {{hard_count}}/{{soft_count}} = define in QUALITY_GATES.md -->

## Routing
<!-- CANONICAL SOURCE: frontmatter keywords + triggers + geo_description -->
<!-- Body section below is DERIVED from frontmatter for human readability -->
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}, {{keyword_4}}]
triggers: "{{trigger_phrase_1}}", "{{trigger_phrase_2}}", "{{trigger_phrase_3}}"
<!-- NOTE: keywords = 4-8 termos that ativam this builder via brain_query -->
<!-- NOTE: triggers = 2-3 frases naturais that um user diria -->
<!-- NOTE: Manter body sincronizado with frontmatter. Frontmatter = source of truth -->

## Crew Role
In a crew, I handle {{ROLE_CAPS}}.
I answer: "{{one_question_this_builder_answers}}"
I do NOT handle: {{exclusion_1}}, {{exclusion_2}}, {{exclusion_3}}.
<!-- NOTE: {{ROLE_CAPS}} = role in CAPS. Ex: MODEL DOCUMENTATION, KNOWLEDGE DISTILLATION -->
<!-- NOTE: {{exclusions}} = types vizinhos no mesmo Pillar or frequentemente confundidos -->
<!-- Look up confusions in TAXONOMY_LAYERS.yaml overlaps e na _schema.yaml do Pillar -->

## Properties

| Property | Value |
|----------|-------|
| Kind | `` |
| Pillar | P02 |
| Domain | _builder construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
