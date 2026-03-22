# Generator: P03 Prompt Template

## QUANDO USAR
- Criar prompt reutilizavel com variaveis
- Padronizar instrucoes para agentes
- Documentar system prompt existente

## SINTAXE DE VARIAVEIS
- Tier 1: {{MUSTACHE}} = template engine resolve na geracao
- Tier 2: [BRACKET] = humano/agente resolve na autoria
- NUNCA: {single_curly} = deprecated

## PASSO A PASSO
1. SCOUT: verificar se prompt similar ja existe
2. DEFINIR purpose (1 linha: o que este prompt faz)
3. LISTAR variables (tabela: name | type | description | example)
4. ESCREVER template body (com {{vars}} nos lugares certos)
5. ADICIONAR quality_gates (min 3 criterios mensuráveis)
6. CRIAR examples (min 2 pares input/output concretos)
7. ADICIONAR semantic_bridge (se quality >= 8.0)
8. VALIDAR contra P03/_schema.yaml
9. SALVAR dual output (.md + .yaml)

## GOLDEN FORMULA (destilada de 257 golden HOPs)
GOLDEN = Specific Frontmatter
       + Clear Purpose (1-2 lines)
       + Typed Variables (table with examples)
       + Structured Body (numbered steps)
       + Quality Gates (measurable)
       + Examples (2+ concrete pairs)
       + Semantic Bridge (cross-framework)

## SEMANTIC BRIDGE (obrigatorio score >= 8)
Secao final com:
- Also known as: nomes equivalentes em outros frameworks
- Keywords: termos de busca (SEO para Brain)
- Framework equivalents: tabela LangChain|OpenAI|Anthropic|LlamaIndex

## ANTI-PATTERNS
- Variables sem example (ninguem sabe o que preencher)
- Quality gates genericos ("be good")
- Examples com placeholders ("output: [RESULTADO]")
- Prompt sem scope claro (tenta fazer tudo)

---
*Generator v1.0 | Evidence: 257 golden HOPs, 108 templates | 2026-03-22*