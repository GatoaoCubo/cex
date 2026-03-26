---
# TEMPLATE: Router Prompt (P03 Prompt)
# Valide contra P03_prompt/_schema.yaml (types.router_prompt)
# Max 3072 bytes

id: p03_rp_{{SCOPE_SLUG}}
kind: router_prompt
pillar: P03
routes: [{{ROUTE_1}}, {{ROUTE_2}}, {{ROUTE_3}}]
fallback: {{FALLBACK_HANDLER}}
---

# Router: {{SCOPE_NAME}}

## Classification Task
Given user input, classify into one of these routes:

## Routes
| Pattern | Handler | When to use |
|---------|---------|-------------|
| {{KEYWORD_PATTERN_1}} | {{HANDLER_1}} | {{DESCRICAO}} |
| {{KEYWORD_PATTERN_2}} | {{HANDLER_2}} | {{DESCRICAO}} |
| {{KEYWORD_PATTERN_3}} | {{HANDLER_3}} | {{DESCRICAO}} |

## Confidence Threshold
- Auto-route if confidence >= {{THRESHOLD}}
- Ask for clarification if confidence < {{THRESHOLD}}

## Fallback
If no route matches: {{FALLBACK_ACTION}}

## Examples
Input: "{{EXEMPLO_INPUT_1}}"
Route: {{HANDLER}} (confidence: {{SCORE}})

Input: "{{EXEMPLO_INPUT_2}}"
Route: {{HANDLER}} (confidence: {{SCORE}})

Input: "{{EXEMPLO_INPUT_3}}"
Route: {{HANDLER}} (confidence: {{SCORE}})
