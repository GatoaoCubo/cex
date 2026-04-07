---
kind: meta_instructions
id: bld_meta_instructions_builder
meta: true
file_position: 4/13
pillar: P03
llm_function: REASON
purpose: Meta-template for generating INSTRUCTIONS.md of any kind-builder
---

# Instructions: How to Produce a {{type_name}}
<!-- This meta-file generates the INSTRUCTIONS.md of any builder -->
<!-- REQUIRED INPUT: _schema.yaml + SCHEMA.md + OUTPUT_TEMPLATE.md ja gerados -->

```yaml
---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for {{type_name}}
pattern: 3-phase pipeline (research -> compose -> validate)
---
```

## Phase 1: RESEARCH
<!-- NOTE: Fase de coleta. Nome pode variar: RESEARCH, CLASSIFY, DISCOVER -->
<!-- signal usa CLASSIFY (porque is simples); model_card usa RESEARCH (porque precisa researchr) -->
<!-- Escolha o name that reflete a complexidade do type -->
1. Identify the {{primary_entity}}: {{what_to_identify}}
<!-- NOTE: {{primary_entity}} = "model" for model_card, "topic" for KC, "event" for signal -->
2. {{research_step_2}}
3. Gather sources: {{source_types}}
4. Check brain_query for existing {{type_name}}s (avoid duplicates)
5. {{research_step_extra}}
<!-- NOTE: Steps variam per complexidade: -->
<!-- - Simples (signal): 3-4 steps, foco em classificar o evento -->
<!-- - Medio (KC, quality_gate): 5-6 steps, foco em researchr domain -->
<!-- - Complexo (model_card): 6-7 steps, foco em multiple sources + URLs -->

## Phase 2: COMPOSE
<!-- NOTE: Fase de escrita. Estrutura UNIVERSAL: -->
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: {{field_summary}}
<!-- NOTE: {{field_summary}} = "all N fields (null OK for optional)" -->
4. Set quality: null (NEVER self-score)
<!-- STEPS ESPECIFICOS DO TIPO (gerar a partir de SCHEMA.md body sections): -->
5. Write {{body_section_1}}
6. Write {{body_section_2}}
7. Write {{body_section_3}}
<!-- NOTE: Para each section obrigatoria em SCHEMA.md Body Structure, crie um step -->
<!-- Inclua constraints inline: ">= 5 rows", "booleans only", "Source URL required" -->

## Phase 3: VALIDATE
<!-- NOTE: Fase de validation. Estrutura UNIVERSAL: -->
1. {{validation_tool_instruction}}
<!-- NOTE: Se validator existe (validate_kc.py for KC): "Run: python _tools/validate_kc.py <file>" -->
<!-- NOTE: Se validator planejado: "Check QUALITY_GATES.md manually" -->
2. HARD gates (all must pass): {{hard_gate_summary}}
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: {{cross_check_items}}
5. If score < 8.0: revise in same pass before outputting
<!-- NOTE: {{cross_check_items}} = final verifications specific do type -->
<!-- Ex model_card: "every Spec row has URL?" -->
<!-- Ex KC: "density >= 0.80? No filler?" -->
<!-- Ex signal: "still atomic? not drifting into handoff?" -->
