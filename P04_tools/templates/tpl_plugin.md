---
# TEMPLATE: Plugin (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.plugin)
# Max 2048 bytes

id: p04_plug_{{PLUGIN_SLUG}}
type: plugin
name: {{PLUGIN_NAME}}
entrypoint: {{MODULE_OR_COMMAND}}
capabilities: [{{CAP_1}}, {{CAP_2}}]
---

# Plugin: {{PLUGIN_NAME}}

## Purpose
<!-- INSTRUCAO: explicar extensao e fronteira do plugin. -->
- Extends: {{HOST_SYSTEM}}
- Adds: {{CAPABILIDADE_PRINCIPAL}}
- Does not own: {{AREA_FORA_DE_ESCOPO}}

## Integration
| Field | Value |
|-------|-------|
| Entrypoint | {{MODULE_OR_COMMAND}} |
| Inputs | {{INPUTS_ESPERADOS}} |
| Outputs | {{OUTPUTS_GERADOS}} |
| Dependencies | {{DEP_1}}, {{DEP_2}} |

## Lifecycle
1. Load: {{COMO_CARREGA}}
2. Execute: {{COMO_OPERA}}
3. Unload: {{COMO_LIBERA_ESTADO}}

## Failure Handling
- Retry: {{POLITICA_DE_RETRY}}
- Fallback: {{COMPORTAMENTO_DEGRADADO}}
- Audit: {{ONDE_LOGAR}}
