# Generator: P03 Prompt (9 tipos)

## TIPOS E QUANDO USAR

| Tipo | Quando usar | Exemplo real |
|------|-------------|-------------|
| system_prompt | Definir identidade/regras de agente | PRIME_SHAKA.md, ISO_SYSTEM_INSTRUCTION |
| user_prompt | Pedir ao agente que execute tarefa | HOPs, handoffs, comandos |
| prompt_template | Criar molde reusavel com {{vars}} | Meta-templates TPL_EDISON_009-020 |
| few_shot | Dar exemplos input->output ao LLM | few_shot_bank.yaml, golden examples |
| chain_of_thought | Forcar raciocinio antes de resposta | "Think step by step", extended thinking |
| react | Interleavar raciocinio + tool use | Anthropic tool_use, DSPy ReAct |
| chain | Encadear prompts A->B->C | ADW workflows, prompt pipelines |
| meta_prompt | Gerar/melhorar outros prompts | Genesis prompt, PITER loop, DSPy MIPRO |
| router_prompt | Classificar input e rotear | STELLA_RULES, semantic routing |

## SINTAXE DE VARIAVEIS
- Tier 1: {{MUSTACHE}} = template engine resolve
- Tier 2: [BRACKET] = humano/agente resolve
- NUNCA: {single_curly} = deprecated

## PASSO A PASSO (qualquer tipo)
1. SCOUT: verificar se prompt similar ja existe
2. ESCOLHER tipo correto (tabela acima)
3. COPIAR template: `P03_prompt/templates/tpl_{{tipo}}.md`
4. PREENCHER frontmatter (todos campos required do schema)
5. ESCREVER body seguindo body_structure do schema
6. ADICIONAR semantic_bridge se quality >= 8.0
7. VALIDAR contra `P03_prompt/_schema.yaml`
8. TESTAR: dar o prompt pra um LLM e avaliar output

## GOLDEN FORMULA (destilada de 713 artefatos)
```
GOLDEN = Specific Frontmatter
       + Clear Purpose (1-2 lines)
       + Typed I/O (input/output com tipos e exemplos)
       + Structured Body (numbered steps com criterios)
       + Quality Gates (min 3 mensuráveis)
       + Examples (min 2 pares concretos)
       + Semantic Bridge (cross-framework mapping)
```

## POR TIPO — GUIA RAPIDO

### system_prompt
- Comece com "You are..." (identidade clara)
- Liste always/never (regras explicitas)
- Defina output format (como responder)
- Referencia: Anthropic system prompt best practices

### user_prompt
- 1 tarefa por prompt (nao misturar)
- Input tipado (YAML block com exemplos)
- Steps numerados com criterios de saida
- Validacao no final (checklist)

### prompt_template
- Toda {{VAR}} deve ter exemplo na tabela
- Min 2 exemplos de uso completo (input+output)
- Semantic bridge obrigatorio se score >= 8

### few_shot
- Min 2, max 10 exemplos
- Exemplos devem cobrir edge cases (nao so happy path)
- Diversidade > volume (3 exemplos diversos > 8 similares)

### chain_of_thought
- Use "Let's think step by step" ou equivalente
- Defina formato do raciocinio (numbered, tree, free)
- Sempre extraia resposta final separada do raciocinio

### react
- Liste ALL tools com schemas JSON
- Defina loop: Thought -> Action -> Observation -> repeat
- SEMPRE defina max_iterations (seguranca)
- Stop condition explicita

### chain
- Defina data_flow entre steps (output N -> input N+1)
- Error handling por step (nao so no final)
- Teste a chain E2E antes de versionar

### meta_prompt
- Defina o TIPO de prompt que quer gerar
- Inclua criterios de qualidade para o prompt gerado
- Teste: o prompt gerado produz output score 8+?

### router_prompt
- Tabela de rotas: pattern -> handler
- Confidence threshold (quando auto-rotear vs perguntar)
- Fallback obrigatorio (nenhum input fica sem rota)
- Min 3 exemplos de classificacao

## ANTI-PATTERNS
- Variables sem example (ninguem sabe o que preencher)
- Quality gates genericos ("be good")
- Examples com placeholders ("output: [RESULTADO]")
- Prompt sem scope claro (tenta fazer tudo)
- system_prompt com tarefas (mistura identidade + acao)
- Prompt sem semantic_bridge (irreplicavel entre frameworks)

## SEMANTIC BRIDGE (obrigatorio score >= 8)
Secao final mapeando equivalentes:
| Termo CEX | LangChain | OpenAI | Anthropic | DSPy |
|-----------|-----------|--------|-----------|------|
| system_prompt | SystemMessagePromptTemplate | system message | system prompt | — |
| user_prompt | HumanMessagePromptTemplate | user message | human turn | dspy.Predict |
| prompt_template | PromptTemplate | — | — | dspy.Signature |
| few_shot | FewShotPromptTemplate | — | — | dspy.BootstrapFewShot |
| chain_of_thought | — | — | extended thinking | dspy.ChainOfThought |
| react | AgentExecutor | function calling | tool_use | dspy.ReAct |
| chain | SequentialChain | — | — | dspy.Module |
| meta_prompt | — | — | — | dspy.MIPROv2 |
| router_prompt | RouterChain | — | — | — |

---
*Generator v2.0 | 9 tipos | 713 artefatos evidence | 2026-03-23*
