---
id: p01_kc_cex_function_constrain
kind: knowledge_card
pillar: P01
title: "CEX Function CONSTRAIN — Formatting and Restricting Output to Standards"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, constrain, grammar, schema, template, formatting]
tldr: "CONSTRAIN restringe output via 11 tipos em 3 niveis (hard/medium/soft) — entrega no padrao exigido"
when_to_use: "Entender como LLMs formatam output e a fronteira entre CONSTRAIN (formato) e GOVERN (qualidade)"
keywords: [constrain, grammar, schema, template, response_format, validation, formatting]
long_tails:
  - "Qual a diferenca entre CONSTRAIN e GOVERN no CEX"
  - "Quais os 11 tipos de restricao na taxonomia CEX"
axioms:
  - "SEMPRE preferir grammar (hard) sobre response_format (soft) quando conformidade eh critica"
  - "NUNCA confundir CONSTRAIN (formato de output) com GOVERN (qualidade de output)"
linked_artifacts:
  primary: p01_kc_cex_function_produce
  related: [p01_kc_cex_function_govern, p01_kc_cex_function_call]
density_score: null
data_source: "https://github.com/guidance-ai/guidance"
related:
  - p06_gram_json_object
  - p01_kc_cex_lp06_schema
  - bld_architecture_response_format
  - p01_kc_validation_schema
  - p01_kc_cex_lp05_output
  - bld_knowledge_card_constraint_spec
  - response-format-builder
  - p03_ins_response_format
  - p01_kc_response_format
  - bld_knowledge_card_response_format
---

## Summary

CONSTRAIN formata, estrutura e restringe output para que conforme com schemas, templates e gramaticas formais. Com 11 tipos (14% do CEX), opera em 3 niveis de rigidez: HARD (grammar — impossivel violar no decoder), MEDIUM (law, axiom, guardrail — regras inviolaveis), SOFT (response_format, template — instrucoes que o LLM pode falhar). Insight critico: response_format (LLM ve no prompt) vs grammar (LLM nao ve, decoder aplica). Mesma funcao, garantias radicalmente diferentes. Frameworks como Guidance (Microsoft) e Outlines (dottxt) confirmam que CONSTRAIN intervem no processo de geracao, nao apenas pos-processa.

## Spec

| Tipo | LP | Rigidez | Funcao | Detalhe |
|------|-----|---------|--------|---------|
| grammar | P06 | Hard | Gramatica formal | BNF/EBNF/FSM no decoder |
| law | P08 | Medium | Regra inviolavel | Principio constitucional |
| axiom | P10 | Medium | Verdade assumida | Restricao de dominio |
| guardrail | P11 | Medium | Barreira de seguranca | Previne output inadequado |
| response_format | P05 | Soft | Formato esperado | JSON, Markdown, XML |
| prompt_template | P03 | Soft | Template parametrizado | Reutilizacao de prompts |
| input_schema | P06 | Soft | Validacao de input | Fronteira entre sistemas |
| output_schema | P06 | Soft | Validacao de output | Formato downstream |
| validation_schema | P06 | Soft | Validacao intermediaria | Pipeline multi-step |
| template | P05 | Soft | Template de output | Emails, relatorios |
| style_guide | P05 | Soft | Convencoes de escrita | Tom, terminologia |

HARD: grammar opera DURANTE geracao (token-level). Impossivel violar.
SOFT: response_format opera via prompt. LLM pode ignorar.
MEDIUM: rules aplicadas por sistema externo. Dificil violar mas nao
impossivel. Guidance (MS) e Outlines (dottxt) usam FSMs e CFGs para
constrained generation — alterando o espaco de tokens possiveis.
LMQL (ETH Zurich) oferece WHERE clauses SQL-like para restricao.

## Patterns

| Trigger | Action |
|---------|--------|
| Conformidade matematicamente garantida | grammar (BNF/EBNF no decoder) |
| Output JSON para API downstream | output_schema + response_format |
| Mesmo prompt para inputs variados | prompt_template parametrizado |
| Consistencia entre multiplos outputs | style_guide compartilhado |
| Pipeline multi-step com validacao | validation_schema por etapa |
| Output para consumo humano padronizado | template (email, relatorio) |
| Fronteira entre sistemas | input_schema na entrada |

## Code

<!-- lang: python | purpose: constrained generation patterns -->
```python
# grammar (HARD): decoder-level constraint via Outlines
import outlines
generator = outlines.generate.json(model, ProductSchema)
result = generator("Extract product data")  # IMPOSSIVEL violar schema

# response_format (SOFT): prompt-level instruction
response = llm.complete(
    prompt=f"Return JSON:\n{input_text}",
    response_format={"type": "json_object"}  # LLM PODE ignorar
)

# prompt_template (SOFT): parametrized reuse
template = "Analyze {product} for {market}. Output: {format}"
prompt = template.format(product="LED", market="BR", format="table")
```

## Anti-Patterns

- response_format para dados criticos (LLM pode ignorar, use grammar)
- grammar para output livre/criativo (sobre-restringe geracao)
- Confundir schema (validacao) com format (expectativa)
- Template rigido para output que precisa de adaptacao
- style_guide sem exemplos concretos (ambiguidade interpretativa)
- Validacao apenas no output final (erro cascateia no pipeline)

## References

- source: https://github.com/guidance-ai/guidance
- source: https://github.com/dottxt-ai/outlines
- related: p01_kc_cex_function_produce
- related: p01_kc_cex_function_govern

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_gram_json_object]] | downstream | 0.37 |
| [[p01_kc_cex_lp06_schema]] | sibling | 0.36 |
| [[bld_architecture_response_format]] | downstream | 0.30 |
| [[p01_kc_validation_schema]] | sibling | 0.29 |
| [[p01_kc_cex_lp05_output]] | sibling | 0.29 |
| [[bld_knowledge_card_constraint_spec]] | sibling | 0.28 |
| [[response-format-builder]] | downstream | 0.27 |
| [[p03_ins_response_format]] | downstream | 0.25 |
| [[p01_kc_response_format]] | sibling | 0.24 |
| [[bld_knowledge_card_response_format]] | sibling | 0.24 |
