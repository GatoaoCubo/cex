---
kind: meta_collaboration
id: bld_meta_collaboration_builder
meta: true
file_position: 13/13
pillar: P12
llm_function: COLLABORATE
purpose: Meta-template for generating COLLABORATION.md of any kind-builder
---

# Collaboration: {{builder_name}}
<!-- Este meta-file gera o COLLABORATION.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: TAXONOMY_LAYERS.yaml (dependencias), ARCHITECTURE.md ja gerado -->

```yaml
---
pillar: P12
llm_function: COLLABORATE
purpose: How {{builder_name}} works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---
```

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "{{one_question}}"
<!-- NOTA: {{one_question}} = mesma pergunta do MANIFEST Crew Role -->
I do not {{exclusion_verb_1}}. I do not {{exclusion_verb_2}}.
I {{primary_verb}} so {{downstream_consumers}} can {{consumer_benefit}}.
<!-- NOTA: Padrao observado em todos os 4 builders: -->
<!-- - model_card: "I INFORM other builders so they can make better decisions" -->
<!-- - KC: "I DISTILL knowledge so other builders and agents have factual context" -->
<!-- - signal: "I report what just happened so monitors can decide what happens next" -->
<!-- - quality_gate: "I define WHAT must pass. I do not implement HOW." -->

## Crew Compositions
<!-- NOTA: 2-3 crews tipicas onde este builder participa -->
<!-- Padrao: lista numerada com seta mostrando output de cada builder -->

### Crew: "{{crew_name_1}}"
```
  1. {{builder_role_1}} -> "{{output_description_1}}"
  2. {{builder_role_2}} -> "{{output_description_2}}"
  3. {{builder_role_3}} -> "{{output_description_3}}"
```
<!-- NOTA: Marcar builders que nao existem com [PLANNED] -->
<!-- Posicao do builder na crew reflete dependencies: -->
<!-- - Layer 0 (infrastructure): primeiro na crew -->
<!-- - Content: depois de pesquisa, antes de identity -->
<!-- - Runtime: depois de specs, antes de orquestracao -->
<!-- - Governance: ultimo na crew (valida output dos outros) -->

### Crew: "{{crew_name_2}}"
```
  1. {{builder_a}} -> "{{output_a}}"
  2. {{builder_b}} -> "{{output_b}}"
```

## Handoff Protocol

### I Receive
- seeds: {{minimum_seeds}}
- optional: {{optional_context}}
<!-- NOTA: {{minimum_seeds}} = inputs minimos para o builder funcionar -->
<!-- Exemplos: -->
<!-- - model_card: "model name, provider" -->
<!-- - KC: "topic name, domain" -->
<!-- - signal: "emitter satellite, event/status" -->
<!-- - quality_gate: "domain (what artifact kind), severity" -->

### I Produce
- {{output_artifact}} ({{output_format}})
- committed to: `cex/{{lp_dir}}/examples/{{naming_pattern}}`
<!-- NOTA: Consistente com CONFIG.md File Paths -->

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
<!-- NOTA: Padrao UNIVERSAL — todos os builders sinalizam da mesma forma -->

## Builders I Depend On
{{dependencies_or_none}}
<!-- NOTA: A maioria dos builders eh INDEPENDENTE (layer 0) -->
<!-- Se depende de outro builder, listar: -->
<!-- "- {builder-name}: provides {what}" -->
<!-- Buscar em ARCHITECTURE.md Dependency Graph -->

## Builders That Depend On Me [PLANNED]
<!-- NOTA: GERAR a partir de ARCHITECTURE.md Dependency Graph -->

| Builder | Why |
|---------|-----|
| {{dependent_builder_1}} | {{why_depends_1}} |
| {{dependent_builder_2}} | {{why_depends_2}} |
<!-- NOTA: Marcar [PLANNED] se o builder dependente nao existe ainda -->
<!-- Buscar em TAXONOMY_LAYERS.yaml quais tipos usam este tipo como input -->
