---
# TEMPLATE: Diagram (P08 Architecture)
# Valide contra P08_architecture/_schema.yaml (types.diagram)
# Max 4096 bytes

id: p08_diag_{{SCOPE_SLUG}}
type: diagram
lp: P08
title: "Diagram: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Diagram: {{SCOPE_NAME}}

## Purpose
{{ONE_SENTENCE_ON_WHAT_THIS_ARCHITECTURE_VIEW_SHOWS}}

## Diagram
```mermaid
flowchart LR
    A[{{COMPONENT_A}}] --> B[{{COMPONENT_B}}]
    B --> C[{{COMPONENT_C}}]
    B --> D[{{COMPONENT_D}}]
    C --> E[{{OUTCOME}}]
```

## Reading Notes
- Entry point: {{ENTRY_POINT}}
- Shared dependency: {{SHARED_COMPONENT}}
- Failure hotspot: {{RISK_AREA}}
