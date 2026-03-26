---
# TEMPLATE: Chain of Thought (P03 Prompt)
# Valide contra P03_prompt/_schema.yaml (types.chain_of_thought)
# Max 2048 bytes

id: p03_cot_{{TASK_SLUG}}
kind: chain_of_thought
pillar: P03
reasoning_type: {{step_by_step|tree|free}}
---

# Chain of Thought: {{TASK_NAME}}

## Task
{{TAREFA_QUE_REQUER_RACIOCINIO}}

## Reasoning Cue
{{INSTRUCAO_DE_RACIOCINIO}}
Example: "Before answering, think through this step by step. Show your reasoning."

## Reasoning Format
```
Step 1: {{ASPECTO_A_CONSIDERAR}}
Step 2: {{ANALISE_OU_CALCULO}}
Step 3: {{SINTESE_OU_COMPARACAO}}
...
```

## Answer Extraction
After reasoning, provide final answer in this format:
```
{{FORMATO_DA_RESPOSTA_FINAL}}
```

## Quality Gate
- Reasoning has {{MIN_STEPS}} steps minimum
- Each step references evidence (not assumptions)
- Final answer is consistent with reasoning
