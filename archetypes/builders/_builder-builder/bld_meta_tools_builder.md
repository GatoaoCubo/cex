---
kind: meta_tools
id: bld_meta_tools_builder
meta: true
file_position: 5/13
pillar: P04
llm_function: CALL
purpose: Meta-template for generating TOOLS.md of any kind-builder
---

# Tools: {{builder_name}}
<!-- Este meta-file gera o TOOLS.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: _schema.yaml + tipo de validador existente -->

```yaml
---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for {{type_name}} production
---
```

## Production Tools
<!-- NOTA: Tabela UNIVERSAL presente em todos os 4 builders -->
<!-- TOOLS UNIVERSAIS (incluir em todo builder): -->

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing {{type_name}}s in pool | Phase 1 (check duplicates) | ACTIVE |
| {{validator_name}} | {{validator_purpose}} | Phase 3 | {{ACTIVE_or_PLANNED}} |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

<!-- NOTA: {{validator_name}} = validador especifico se existir -->
<!-- - knowledge_card: validate_kc.py (ACTIVE) -->
<!-- - model_card: validate_artifact.py [PLANNED] -->
<!-- - signal: nenhum especifico (manual) -->
<!-- - quality_gate: nenhum especifico (manual) -->
<!-- NOTA: Adicione tools especificos do dominio se existirem -->

## Data Sources
<!-- NOTA: Tabela de fontes de dados para producao -->
<!-- Varia muito por tipo: -->
<!-- - model_card: APIs de providers (Anthropic, OpenAI, Google, LiteLLM, HuggingFace) -->
<!-- - knowledge_card: CEX Schema, CEX Examples, CEX Pool -->
<!-- - signal: signal_writer.py, spawn_monitor.ps1, P12 schema -->
<!-- - quality_gate: existing gates, validate_kc.py reference -->

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | {{lp_dir}}/_schema.yaml | Field definitions |
| CEX Examples | {{lp_dir}}/examples/ | Real artifacts |
| {{source_1}} | {{path_1}} | {{data_1}} |
| {{source_2}} | {{path_2}} | {{data_2}} |

<!-- NOTA: {{lp_dir}} = P01_knowledge, P02_model, P11_feedback, P12_orchestration, etc. -->

## Interim Validation
<!-- NOTA: Fallback quando o validador automatico nao existe -->
<!-- Padrao UNIVERSAL: -->
{{interim_validation_text}}
<!-- Se validador ACTIVE: "Run {validator} before committing. No manual checking needed." -->
<!-- Se validador PLANNED: "Manually check each QUALITY_GATES.md gate against produced artifact." -->
<!-- Incluir checklist minimo para validacao manual -->
