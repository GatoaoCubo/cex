---
# TEMPLATE: Component Map (P08 Architecture)
# Valide contra P08_architecture/_schema.yaml (types.component_map)
# Max 3072 bytes

id: p08_cmap_{{SCOPE_SLUG}}
kind: component_map
pillar: P08
title: "Component Map: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Component Map: {{SCOPE_NAME}}

## Components
| Component | Responsibility | Depends On |
|-----------|----------------|------------|
| {{COMPONENT_1}} | {{RESPONSIBILITY_1}} | {{DEPENDENCY_1}} |
| {{COMPONENT_2}} | {{RESPONSIBILITY_2}} | {{DEPENDENCY_2}} |
| {{COMPONENT_3}} | {{RESPONSIBILITY_3}} | {{DEPENDENCY_3}} |

## Interfaces
- {{COMPONENT_1}} -> {{COMPONENT_2}}: {{INTERFACE_RULE}}
- {{COMPONENT_2}} -> {{COMPONENT_3}}: {{INTERFACE_RULE}}

## Change Impact
- Safe to change alone: {{COMPONENT_SAFE}}
- Requires coordination: {{COMPONENT_RISKY}}
