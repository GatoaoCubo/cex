---
id: p01_kc_cex_function_govern
kind: knowledge_card
pillar: P01
title: "CEX Function GOVERN — Quality Inspection and System Governance"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.0
tags: [cex, llm-function, govern, quality-gate, shokunin, evals, benchmark]
tldr: "GOVERN avalia e controla qualidade via 22 tipos (28% do CEX) — a maior funcao, Shokunin do pipeline"
when_to_use: "Entender como LLMs garantem qualidade e a contribuicao mais original do CEX (governanca como cidadao de 1a classe)"
keywords: [govern, quality_gate, validator, benchmark, golden_test, evals, shokunin]
long_tails:
  - "Por que GOVERN eh a maior funcao do CEX com 22 tipos"
  - "Qual a diferenca entre quality_gate e validator no CEX"
axioms:
  - "SEMPRE implementar GOVERN em todo output consumido por outro sistema"
  - "NUNCA tratar governanca como step opcional no final do pipeline"
linked_artifacts:
  primary: p01_kc_cex_function_constrain
  related: [p01_kc_cex_function_produce, p01_kc_cex_function_collaborate]
density_score: null
data_source: "https://arxiv.org/abs/2303.11366"
related:
  - p01_kc_lp07_evals
  - p01_kc_cex_lp07_evals
  - p01_kc_lp11_feedback
  - p01_kc_cex_taxonomy
  - p01_kc_cex_lp11_feedback
  - p01_kc_validator
  - bld_architecture_quality_gate
  - bld_architecture_golden_test
  - p01_kc_cex_function_produce
  - p01_kc_cex_function_inject
---

## Summary

GOVERN avalia, controla e melhora a qualidade dos outputs via quality gates, benchmarks, validators e lifecycle rules. Com 22 tipos (28% do CEX), eh a maior funcao — refletindo uma lacuna critica na industria onde nenhum framework trata governanca como cidadao de primeira classe. LangChain tem Callback (rudimentar), DSPy tem Metric (parcial), CrewAI nao tem nada. O CEX trata qualidade como funcao arquitetural tao importante quanto geracao. Analogia: Shokunin japones — o artesao que recusa entregar peca abaixo do padrao. REFLECT (auto-critica) eh sub-funcao de GOVERN aplicada internamente.

## Spec

| Sub-funcao | Tipos | LPs | Funcao |
|------------|-------|-----|--------|
| Avaliacao | 6 tipos | P07 | Medir qualidade objetivamente |
| Validacao | 6 tipos | P05-P06 | Verificar conformidade formal |
| Config | 8 tipos | P02+P09 | Controlar comportamento do sistema |
| Feedback | 6 tipos | P04+P11 | Corrigir e melhorar iterativamente |

Tipos de avaliacao: unit_eval, smoke_eval, e2e_eval, benchmark,
golden_test, scoring_rubric. De teste unitario a rubrica multi-dimensional.
quality_gate (score numerico holistic) vs validator (pass/fail binario).
benchmark (comparativo entre versoes) vs eval (absoluto por criterio).
confidence_threshold opera PRE-geracao; quality_gate opera POS-geracao.
law (constitucional, inviolavel) vs runtime_rule (ajustavel em execucao).
guardrail (proativo, previne) vs validator (reativo, detecta).
bugloop (test->fail->fix->verify->commit) vs retry simples (repete).
Reflexion (Shinn 2023) e Self-Refine (Madaan 2023) confirmam:
auto-critica eh GOVERN aplicado ao proprio output, nao funcao separada.
22 tipos formais vs LangChain Callback (1) vs DSPy Metric (2).
Nenhum framework trata governanca com esta granularidade.

## Patterns

| Trigger | Action |
|---------|--------|
| Output consumido por outro sistema | quality_gate com threshold |
| Conformidade com regras especificas | validator (pass/fail) |
| Comparacao entre versoes ou modelos | benchmark padronizado |
| Detectar regressao de qualidade | golden_test como referencia |
| Avaliacao reproduzivel e explicavel | scoring_rubric com criterios |
| Teste rapido pos-mudanca | smoke_eval antes de suite completa |
| Correcao automatica de defeitos | bugloop (test->fix->verify) |
| Rollout gradual de funcionalidade | feature_flag sem deploy |
| Principio inviolavel do sistema | law (constitucional) |

## Code

<!-- lang: python | purpose: quality gate and eval patterns -->
```python
# quality_gate: score numerico com threshold
score = scoring_rubric.evaluate(output, criteria=["density", "accuracy"])
if score < 7.0:
    output = refine(output)  # GOVERN triggers re-PRODUCE
elif score >= 9.5:
    pool.promote(output, tier="golden")  # Shokunin standard

# golden_test: regressao contra referencia conhecida
expected = load_golden("kc_function_call_v1.md")
similarity = compare(output, expected)
assert similarity > 0.85, "Regression detected"

# bugloop: test -> fail -> fix -> verify -> commit
while not tests_pass(module) and attempts < 3:
    diagnosis = analyze_failure(test_output)
    apply_fix(diagnosis)
    attempts += 1
```

## Anti-Patterns

- Producao sem governanca (fabrica sem controle de qualidade)
- quality_gate apenas no final (erro propaga por todo pipeline)
- Auto-scoring de qualidade (quality: null ate validacao externa)
- Confundir validator (formato) com quality_gate (qualidade)
- golden_test desatualizado (referencia obsoleta gera falsos negativos)
- Guardrail sem log (bloqueio silencioso impede debugging)

## References

- source: https://arxiv.org/abs/2303.11366
- source: https://arxiv.org/abs/2303.17651
- related: p01_kc_cex_function_constrain
- related: p01_kc_cex_function_produce
- related: p01_kc_cex_function_collaborate

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_lp07_evals]] | sibling | 0.36 |
| [[p01_kc_cex_lp07_evals]] | sibling | 0.31 |
| [[p01_kc_lp11_feedback]] | sibling | 0.27 |
| [[p01_kc_cex_taxonomy]] | sibling | 0.27 |
| [[p01_kc_cex_lp11_feedback]] | sibling | 0.25 |
| [[p01_kc_validator]] | sibling | 0.25 |
| [[bld_architecture_quality_gate]] | downstream | 0.23 |
| [[bld_architecture_golden_test]] | downstream | 0.22 |
| [[p01_kc_cex_function_produce]] | sibling | 0.21 |
| [[p01_kc_cex_function_inject]] | sibling | 0.21 |
