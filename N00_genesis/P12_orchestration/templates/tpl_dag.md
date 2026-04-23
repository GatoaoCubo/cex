---
# TEMPLATE: DAG (P12 Orchestration)
# Valide contra P12_orchestration/_schema.yaml (types.dag)
# Max 3072 bytes

id: p12_dag_{{PIPELINE_SLUG}}
kind: dag
pillar: P12
title: "DAG: {{PIPELINE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# DAG: {{PIPELINE_NAME}}

## Nodes
```text
{{NODE_A}} -> {{NODE_B}} -> {{NODE_D}}
{{NODE_A}} -> {{NODE_C}} -> {{NODE_D}}
```

## Dependencies
| Node | Depends On | Output |
|------|------------|--------|
| {{NODE_B}} | {{NODE_A}} | {{OUTPUT_B}} |
| {{NODE_C}} | {{NODE_A}} | {{OUTPUT_C}} |
| {{NODE_D}} | {{NODE_B}}, {{NODE_C}} | {{OUTPUT_D}} |

## Scheduling Rule
- Parallelizable: {{YES_OR_NO}}
- Critical path: {{CRITICAL_PATH}}
