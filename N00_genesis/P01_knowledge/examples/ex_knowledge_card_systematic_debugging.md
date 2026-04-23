---
id: p01_kc_systematic_debugging
kind: knowledge_card
pillar: P01
title: "Systematic Debugging — 4-Phase Root Cause Methodology"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: debugging
quality: 9.1
tags: [debugging, root-cause, systematic-process, defense-in-depth, condition-based-waiting]
tldr: "Debugging em 4 fases (root cause, pattern, hypothesis, implementation) com lei de ferro: nenhum fix sem investigacao primeiro"
when_to_use: "Bug encontrado — antes de qualquer tentativa de fix, seguir este processo sistematico"
keywords: [systematic-debugging, root-cause-analysis, defense-in-depth, flaky-tests, hypothesis-testing]
long_tails:
  - "Como debugar sistematicamente sem thrashing ou tentativa e erro"
  - "Quando parar de tentar fixes e questionar a arquitetura"
axioms:
  - "NUNCA fixar sem root cause investigation primeiro"
  - "SEMPRE testar UMA hipotese por vez com mudanca minima"
  - "NUNCA acumular multiplos fixes simultaneamente"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_function_reason]
density_score: null
data_source: "https://jvns.ca/blog/2019/06/23/a-few-debugging-resources/"
related:
  - p12_wf_auto_diagnose
  - p03_sp_debug_ops
  - p01_kc_feedback_loops
  - p12_wf_auto_debug
  - n01_hybrid_review_wave1
  - p10_lr_bugloop_builder
  - p01_kc_self_healing_skill
  - p01_kc_skill_format_universal
---

## Summary

Metodologia de debugging em 4 fases que eleva first-time fix rate de 40% (random) para 95% (sistematico).
Tempo medio cai de 2-3h (thrashing) para 15-30min (processo estruturado).
Lei de ferro: nenhum fix sem root cause investigation primeiro.
4 tecnicas de suporte: root cause tracing, defense-in-depth (4 camadas de validacao), condition-based waiting (elimina flaky tests — 60% para 100% pass rate) e test pressure levels.
Regra critica: 3+ fixes falhados = problema arquitetural, nao bug isolado.

## Spec

| Fase | Atividade | Criterio de Saida |
|------|-----------|-------------------|
| 1. Root Cause | Ler erros, reproduzir, checar mudancas, instrumentar | Entender O QUE e POR QUE |
| 2. Pattern | Encontrar exemplos funcionando, comparar linha a linha | Identificar diferencas |
| 3. Hypothesis | Formular UMA teoria, testar com mudanca minima | Confirmado ou nova hipotese |
| 4. Implementation | Criar teste falhando, fixar causa raiz, verificar | Bug resolvido, testes passam |

| Metrica | Random | Sistematico |
|---------|--------|-------------|
| Tempo medio | 2-3h | 15-30min |
| First-time fix rate | 40% | 95% |
| Fix threshold | — | >= 3 falhas = problema arquitetural |

| Tecnica Suporte | Quando Usar | Resultado |
|-----------------|-------------|-----------|
| Root Cause Tracing | Erro fundo no call stack | Fix na fonte, nao no sintoma |
| Defense-in-Depth | Apos root cause encontrado | Bug torna-se estruturalmente impossivel |
| Condition-Based Waiting | Testes com setTimeout/sleep | 15 flaky tests fixados, 40% mais rapido |
| Test Pressure Levels | Treinar processo sob pressao | Processo sistematico vence thrashing |

Defense-in-depth: Entry Point (validar input) → Business Logic (validar semantica) → Environment Guards (NODE_ENV) → Debug Instrumentation (logging forense).

## Patterns

| Trigger | Action |
|---------|--------|
| Bug encontrado | Phase 1: ler errors completos, reproduzir, git diff |
| Erro em sistema multi-componente | Instrumentar cada boundary: log entrada e saida |
| Root cause identificado | Phase 3: UMA hipotese, UMA mudanca, testar |
| Fix falhou 3+ vezes | PARAR — questionar arquitetura com humano |
| Testes flaky com setTimeout | Substituir por condition-based waiting |
| Bug fixado | Defense-in-depth: 4 camadas tornam bug impossivel |

## Anti-Patterns

- "It's probably X, let me fix that" — assumir sem verificar
- "Quick fix for now, investigate later" — o problema retorna
- "Just try changing X and see" — thrashing sem hipotese
- Acumular multiplos fixes e testar juntos — impossivel isolar
- Fixar onde o erro aparece, nao onde origina (sintoma vs causa)

## Code

<!-- lang: typescript | purpose: condition-based waiting replaces flaky setTimeout -->
```typescript
async function waitFor<T>(
  condition: () => T | undefined,
  description: string,
  timeoutMs = 5000
): Promise<T> {
  const start = Date.now();
  while (true) {
    const result = condition();
    if (result) return result;
    if (Date.now() - start > timeoutMs)
      throw new Error(`Timeout: ${description} (${timeoutMs}ms)`);
    await new Promise(r => setTimeout(r, 10));
  }
}

// Antes: await new Promise(r => setTimeout(r, 50));
// Depois: await waitFor(() => getResult(), "result ready");
// Resultado: 15 flaky tests fixados, 60% -> 100% pass rate
```

```bash
# Root cause tracing: instrumentar boundary
echo "DEBUG: input=$input cwd=$(pwd)" >> /tmp/debug.log
# Rastrear para cima ate a fonte — fix la, nao no sintoma
```

## References

- source: https://jvns.ca/blog/2019/06/23/a-few-debugging-resources/
- source: https://wizardzines.com/zines/debugging-guide/
- related: p01_kc_cex_function_reason

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_auto_diagnose]] | downstream | 0.23 |
| [[p03_sp_debug_ops]] | downstream | 0.23 |
| [[p01_kc_feedback_loops]] | sibling | 0.22 |
| [[p12_wf_auto_debug]] | downstream | 0.21 |
| [[n01_hybrid_review_wave1]] | related | 0.18 |
| [[p10_lr_bugloop_builder]] | downstream | 0.17 |
| [[p01_kc_self_healing_skill]] | sibling | 0.15 |
| [[p01_kc_skill_format_universal]] | sibling | 0.15 |
