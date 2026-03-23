---
# TEMPLATE: ReAct Pattern (P03 Prompt)
# Valide contra P03_prompt/_schema.yaml (types.react)
# Max 3072 bytes

id: p03_react_{{AGENT_SLUG}}
type: react
lp: P03
tools_available: [{{TOOL_1}}, {{TOOL_2}}, {{TOOL_3}}]
---

# ReAct: {{AGENT_NAME}}

## Objective
{{O_QUE_O_AGENTE_DEVE_ALCANCAR}}

## Available Tools
| Tool | Description | Input | Output |
|------|-------------|-------|--------|
| {{TOOL_1}} | {{DESC}} | {{INPUT_SCHEMA}} | {{OUTPUT_SCHEMA}} |
| {{TOOL_2}} | {{DESC}} | {{INPUT_SCHEMA}} | {{OUTPUT_SCHEMA}} |
| {{TOOL_3}} | {{DESC}} | {{INPUT_SCHEMA}} | {{OUTPUT_SCHEMA}} |

## Loop Format
```
Thought: {{RACIOCINIO_SOBRE_PROXIMO_PASSO}}
Action: {{TOOL_NAME}}
Action Input: {{INPUT_JSON}}
Observation: {{RESULTADO_DA_TOOL}}
... (repeat until done)
Thought: I have enough information to answer.
Final Answer: {{RESPOSTA_FINAL}}
```

## Stop Conditions
- {{CONDICAO_DE_SUCESSO}}
- Max iterations: {{MAX_ITER}}
- Error: {{O_QUE_FAZER_SE_TOOL_FALHA}}
