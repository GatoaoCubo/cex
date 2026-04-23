---
kind: meta_collaboration
id: bld_meta_collaboration_builder
meta: true
file_position: 13/13
pillar: P12
llm_function: COLLABORATE
purpose: Meta-template for generating COLLABORATION.md of any kind-builder
quality: 9.1
title: "Meta Collaboration Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_builder
  - bld_meta_manifest_builder
  - bld_collaboration_kind
  - bld_collaboration_workflow
  - bld_collaboration_golden_test
  - bld_collaboration_memory_scope
  - bld_collaboration_retriever_config
  - bld_collaboration_output_validator
  - bld_collaboration_quality_gate
  - bld_collaboration_signal
---

# Collaboration: {{builder_name}}
<!-- This meta-file generates the COLLABORATION.md of any builder -->
<!-- REQUIRED INPUT: TAXONOMY_LAYERS.yaml (dependencies), ARCHITECTURE.md ja gerado -->

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
<!-- NOTE: {{one_question}} = mesma pergunta do MANIFEST Crew Role -->
I do not {{exclusion_verb_1}}. I do not {{exclusion_verb_2}}.
I {{primary_verb}} so {{downstream_consumers}} can {{consumer_benefit}}.
<!-- NOTE: Padrao observado em all os 4 builders: -->
<!-- - model_card: "I INFORM other builders so they can make better decisions" -->
<!-- - KC: "I DISTILL knowledge so other builders and agents have factual context" -->
<!-- - signal: "I report what just happened so monitors can decide what happens next" -->
<!-- - quality_gate: "I define WHAT must pass. I do not implement HOW." -->

## Crew Compositions
<!-- NOTE: 2-3 crews tipicas where this builder participa -->
<!-- Padrao: lista numerada with seta mostrando output de each builder -->

### Crew: "{{crew_name_1}}"
```
  1. {{builder_role_1}} -> "{{output_description_1}}"
  2. {{builder_role_2}} -> "{{output_description_2}}"
  3. {{builder_role_3}} -> "{{output_description_3}}"
```
<!-- NOTE: Marcar builders that not existem with [PLANNED] -->
<!-- Posicao do builder na crew reflete dependencies: -->
<!-- - Layer 0 (infrastructure): primeiro na crew -->
<!-- - Content: depois de research, antes de identity -->
<!-- - Runtime: depois de specs, antes de orquestraction -->
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
<!-- NOTE: {{minimum_seeds}} = inputs minimal for the builder funcionar -->
<!-- Exemplos: -->
<!-- - model_card: "model name, provider" -->
<!-- - KC: "topic name, domain" -->
<!-- - signal: "emitter agent_group, event/status" -->
<!-- - quality_gate: "domain (what artifact kind), severity" -->

### I Produce
- {{output_artifact}} ({{output_format}})
- committed to: `cex/{{lp_dir}}/examples/{{naming_pattern}}`
<!-- NOTE: Consistente with CONFIG.md File Paths -->

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
<!-- NOTE: Padrao UNIVERSAL — all os builders sinalizam da mesma forma -->

## Builders I Depend On
{{dependencies_or_none}}
<!-- NOTE: A maioria dos builders is INDEPENDENTE (layer 0) -->
<!-- Se depende de outro builder, listar: -->
<!-- "- {builder-name}: provides {what}" -->
<!-- Look up in ARCHITECTURE.md Dependency Graph -->

## Builders That Depend On Me [PLANNED]
<!-- NOTE: GERAR a partir de ARCHITECTURE.md Dependency Graph -->

| Builder | Why |
|---------|-----|
| {{dependent_builder_1}} | {{why_depends_1}} |
| {{dependent_builder_2}} | {{why_depends_2}} |
<!-- NOTE: Marcar [PLANNED] se the builder dependente not existe ainda -->
<!-- Look up in TAXONOMY_LAYERS.yaml quais types usam this type as input -->

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_builder]] | related | 0.43 |
| [[bld_meta_manifest_builder]] | upstream | 0.38 |
| [[bld_collaboration_kind]] | related | 0.37 |
| [[bld_collaboration_workflow]] | related | 0.34 |
| [[bld_collaboration_golden_test]] | related | 0.33 |
| [[bld_collaboration_memory_scope]] | related | 0.33 |
| [[bld_collaboration_retriever_config]] | related | 0.32 |
| [[bld_collaboration_output_validator]] | related | 0.32 |
| [[bld_collaboration_quality_gate]] | upstream | 0.31 |
| [[bld_collaboration_signal]] | related | 0.31 |
