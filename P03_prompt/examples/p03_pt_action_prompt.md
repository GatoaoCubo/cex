---
id: p03_pt_action_prompt
type: prompt_template
lp: P03
title: Template Universal de Action Prompt
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: EDISON
domain: meta
quality: 10.0
tags: [prompt, template, action, universal, meta]
tldr: Template reutilizavel para criar action prompts com variaveis tipadas
when_to_use: Quando precisa criar prompt de acao para qualquer agente
keywords: [action-prompt, prompt-template, prompt-engineering]
long_tails:
  - como criar prompt de acao para agente AI
  - template de prompt reutilizavel com variaveis
axioms:
  - Todo prompt precisa de PURPOSE, INPUT, EXECUTION, OUTPUT, VALIDATION
density_score: 0.95
---

# Template: Action Prompt

## Variables

| Var | Tipo | Descricao | Exemplo |
|-----|------|-----------|---------|
| {{PROMPT_NAME}} | string | Nome do prompt | Analise de Mercado |
| {{PURPOSE}} | string | O que faz (1 linha) | Analisa concorrentes |
| {{INPUT_FIELDS}} | list | Campos de entrada | [url, domain, depth] |
| {{STEPS}} | list | Passos de execucao | [extrair, analisar, reportar] |
| {{OUTPUT_FORMAT}} | string | Formato de saida | markdown table |
| {{VALIDATIONS}} | list | Checklist final | [dados completos, score >= 8] |

## Template Body



## Quality Gates
- PURPOSE: max 2 linhas, especifico (nao generico)
- INPUT: cada campo com tipo e exemplo
- STEPS: numerados, cada um com output intermediario
- VALIDATION: min 3 criterios mensuraveis

## Semantic Bridge
- Also known as: PromptTemplate, ChatPromptTemplate, SystemMessage
- Keywords: prompt engineering, template variables, instruction following
- LangChain: PromptTemplate | OpenAI: System Prompt | Anthropic: System Message