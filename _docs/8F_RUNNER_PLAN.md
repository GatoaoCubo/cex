# 8F Runner Architecture -- Execution Plan

**Version**: 1.0.0 | **Date**: 2026-03-29
**Status**: PLAN

---

## O GAP

Hoje o CEX tem:
- Motor 8F: classifica intent, agrupa builders por funcao
- Crew Runner: itera builders em ordem, gera prompts
- cex_intent.py: compoe 1 prompt gigante com tudo junto

O que FALTA: cada funcao 8F ser um STEP real de processamento.

---

## AS 8 FUNCOES COMO PIPELINE

    USER INPUT
         |
    F1 CONSTRAIN  - carrega limites: schemas, guardrails, budget
    F2 BECOME     - seta identidade: system_prompt, persona
    F3 INJECT     - busca conhecimento: KCs, context, few_shots
    F4 REASON     - planeja: decomposicao, CoT, decisoes [LLM]
    F5 CALL       - executa tools se necessario [condicional]
    F6 PRODUCE    - gera o artefato final [LLM principal]
    F7 GOVERN     - valida: quality_gate, scoring [retry loop]
    F8 COLLABORATE - salva, compila, commita, notifica
         |
    ARTEFATO SALVO

F1-F3: lookup only (zero LLM calls)
F4: 1 LLM call (modelo leve, planeja)
F5: condicional (so se precisa de tool)
F6: 1 LLM call (modelo forte, gera)
F7: validacao + optional LLM judge
F8: file ops only

---

## CADA FUNCAO

### F1 CONSTRAIN
Carrega _schema.yaml (max_bytes, frontmatter_required), guardrails, rate limits.
Output: constraints dict. LLM: NAO.

### F2 BECOME
Carrega bld_system_prompt + bld_config do builder. Define persona.
Output: identity dict. LLM: NAO.

### F3 INJECT
Busca KC-Domains via feeds_kinds. Carrega bld_knowledge_card + bld_examples + bld_memory.
Output: knowledge dict. LLM: NAO.

### F4 REASON
PRIMEIRA CHAMADA LLM: dado contexto, planejar geracao.
Retorna: campos a preencher, decisoes, tradeoffs, decomposicao.
Output: reasoning dict. LLM: SIM (haiku/sonnet).

### F5 CALL
Se plano precisa dados externos: executa tools (search, code, API).
90% dos casos: SKIP.
Output: tool_results dict. LLM: CONDICIONAL.

### F6 PRODUCE
CHAMADA LLM PRINCIPAL: gera artefato com tudo acima como contexto.
Prompt: system_prompt + instruction + KCs + template + reasoning.
Output: artifact string. LLM: SIM (opus/sonnet).

### F7 GOVERN
Valida: frontmatter, size, formato, optional LLM-as-judge.
Se FAIL: feedback para F6 retry (max 2).
Output: verdict dict. LLM: CONDICIONAL.

### F8 COLLABORATE
Salva artefato, compila, git add+commit, signal.
Output: result dict. LLM: NAO.

---

## CHAMADAS LLM POR ARTEFATO

| Caso | F4 | F5 | F6 | F7 | Total |
|------|----|----|----|----|-------|
| Simples (KC, enum) | skip | skip | 1 | validate | 1 call |
| Medio (agent, prompt) | 1 | skip | 1 | validate | 2 calls |
| Complexo (director) | 1 | 1 | 1 | judge | 3-4 calls |
| Retry (F7 fail) | - | - | +1 | +1 | +1-2 calls |

---

## IMPLEMENTACAO: cex_8f_runner.py (~400 loc)

class EightFRunner:
    def __init__(self, intent, kind=None, dry_run=True)
    def f1_constrain(self) -> dict
    def f2_become(self) -> dict
    def f3_inject(self) -> dict
    def f4_reason(self) -> dict
    def f5_call(self) -> dict
    def f6_produce(self) -> str
    def f7_govern(self, artifact) -> dict
    def f8_collaborate(self, artifact, verdict) -> dict
    def run(self) -> dict

Modos:
  --dry-run: F1-F3 executam (lookup), F4-F8 geram prompts
  --execute: todas as Fs executam com LLM calls
  --step N: executa ate funcao N
  --retry: re-executa F6+F7 com feedback

---

## RELACAO COM TOOLS EXISTENTES

| Tool | Papel | Status |
|------|-------|--------|
| cex_8f_motor.py | Classifica intent | NAO muda |
| cex_crew_runner.py | Itera builders | DEPRECADO pelo runner |
| cex_intent.py | Compoe 1 prompt | ABSORVIDO pelo runner |
| cex_pipeline.py | 5-stage build | COEXISTE (batch) |
| cex_forge.py | Gera de 1 kind | COEXISTE (simple) |
| cex_8f_runner.py | Pipeline 8F | NOVO |

---

## WAVES

### Wave 1: Core (~45 min, 1 EDISON)
- F1-F3 (lookup), F6 (produce), F8 (save)
- Test: dry-run chunk_strategy

### Wave 2: Intelligence (~30 min, 1 EDISON)
- F4 (reason), F7 (govern + retry)
- Test: execute mode com validation

### Wave 3: Polish (~20 min, 1 EDISON)
- F5 (tools), --step/--retry flags, verbose logging
- Test: full F1-F8 end-to-end

### Wave 4: Proof (~15 min, STELLA)
- 3 artefatos reais: chunk_strategy, agent, eval_dataset
- Comparar runner vs intent.py

## ETA: ~2h | DEPS: PyYAML + anthropic (opcional)