# CEX Roadmap Consolidado v1.0

**Data**: 2026-03-28 | **Fontes**: Checkpoint, Whitepaper, Phase3 Plan, Overnight Report, Gap Analysis

---

## Estado Atual (commit 74305b6)

| Metrica | Valor |
|---------|-------|
| Builders | 70 dirs x 13 files = 931 (doctor 100% PASS) |
| Pillars | 12/12 com _schema + _generator + templates + examples |
| Tools | 14 scripts, 5054 lines |
| Docs | 20 docs, 3966 lines |
| Examples | 386 + 353 compiled |
| Nuclei | 7 dirs, 22 skeleton files (VAZIOS) |
| Crews definidos | 71 builders com crew compositions |
| Dependency edges | 70+ builder-to-builder |
| Motor 8F | TEORICO (whitepaper 94.7%) — NAO IMPLEMENTADO |

---

## Waves Completas (0-5)

| Wave | Nome | Status |
|------|------|--------|
| 0 | CLEANUP | DONE — naming v2.0, nuclei, whitepaper |
| 1 | GOVERNANCE | DONE — doctor v2, validator, multi-LLM entry |
| 2 | ENGINE | DONE — index, pipeline, feedback |
| 3 | PRODUCT | DONE — cex init, onboarding docs |
| 4 | LAUNCH | DONE — README v2, CHANGELOG, LICENSE |
| 5 | REVIEW | DONE — universalize, compile, audit, doctor 100% |

---

## OS 3 GAPS CRITICOS

### Gap 1: Motor 8F nao existe como codigo

8 funcoes LLM: BECOME, INJECT, REASON, CALL, PRODUCE, CONSTRAIN, GOVERN, COLLABORATE

Cada builder TEM llm_function (705/931 files). Cada pillar mapeia funcoes.
Mas NAO existe runtime que decomponha intent em 8 dimensoes e preencha gaps.
Pipeline atual faz hydrate por template (formulario), nao por funcao (inteligencia).

**Falta**: cex_8f_engine.py — gap analysis dimensional + hydrate inteligente.

### Gap 2: Crews existem mas ninguem os executa

71 builders definem crews (sequencia de colaboracao):

  Crew "New Agent End-to-End":
    1. knowledge-card-builder -> domain knowledge
    2. agent-builder -> agent definition
    3. instruction-builder -> execution steps
    4. boot-config-builder -> provider config
    5. iso-package-builder -> deployable package

Cada builder tem handoff protocol (I Receive / I Produce / I Signal).
Taxonomia P12: workflow, dispatch_rule, handoff, signal, dag.

Mas NAO existe orquestrador que:
- Le crew composition
- Invoca cada builder como agente especializado
- Passa handoffs entre eles
- Coleta signals + valida quality gates

**Falta**: cex_crew_runner.py — orquestrador de crews multi-builder.

Gap 2 e MAIS profundo: cada agente especializado e invocado para
construir em COLABORACAO com outros builders do mesmo crew.
Builders = agents = teams que constroem types juntos.

### Gap 3: Zero instances reais (nuclei vazios)

N01-N07 tem 22 skeleton files. Nenhum agente real foi construido PELO CEX.
O genesis test: CEX constroi 1 agente usando seus proprios builders + crews.

---

## ROADMAP: Waves 6-12

### Wave 6: GENESIS ENGINE (~3h) — PRIORIDADE MAXIMA

| Batch | Task | Output |
|-------|------|--------|
| 6.1 | Criar _meta/TYPE_TO_TEMPLATE.yaml | Config file |
| 6.2 | Fix cex_forge.py — builder generator funcional | Tool fix |
| 6.3 | Criar cex_8f_engine.py — gap analysis por 8 funcoes | 8F decomposer |
| 6.4 | Criar cex_crew_runner.py — orquestrador de crews | Crew executor |
| 6.5 | GENESIS TEST: forge reconstroi knowledge-card-builder | Self-build proof |
| 6.6 | GENESIS TEST: crew constroi agente real end-to-end | Agent-build proof |

Criterio: forge >= 85% similaridade. Crew gera agente 8/8 dimensoes. Doctor passa.

### Wave 7: SELF-BUILD LOOP (~2h)

| Batch | Task |
|-------|------|
| 7.1 | CEX reconstroi 5 builders via forge (diff < 15%) |
| 7.2 | CEX reconstroi 1 builder via crew (multi-builder) |
| 7.3 | Feedback loop: rebuild output alimenta MEMORY.md |
| 7.4 | Doctor valida todos os rebuilds |

### Wave 8: FIRST REAL AGENTS (~2h)

| Batch | Task | Nucleus |
|-------|------|---------|
| 8.1 | Agente web-scraper (crew: agent+skill+mcp) | N03_engineering |
| 8.2 | Agente ad-copywriter (crew: agent+prompt+quality) | N02_marketing |
| 8.3 | Agente knowledge-indexer (crew: agent+rag+brain) | N04_knowledge |
| 8.4 | Relocar 157 packages/ para nuclei corretos | All |

### Wave 9: TESTING + CI (~1h)

| Batch | Task |
|-------|------|
| 9.1 | Unit tests (pytest) para 14 tools |
| 9.2 | Integration test: pipeline + forge + crew E2E |
| 9.3 | GitHub Actions: lint + test + doctor on PR |

### Wave 10: PACKAGING (~1h)

| Batch | Task |
|-------|------|
| 10.1 | pyproject.toml + entry points |
| 10.2 | pip install cex + PyPI test |
| 10.3 | Tag v7.0.0-genesis |

### Wave 11: CONTENT MATURITY (~2h)

| Batch | Task |
|-------|------|
| 11.1 | Recompilar 159 legacy compiled/ |
| 11.2 | Universalizar ~213 files restantes |
| 11.3 | OUTPUT_TEMPLATE.md redo (69/70) |
| 11.4 | Enriquecer examples: min 3 goldens/pillar |

### Wave 12: PUBLIC LAUNCH (~2h)

| Batch | Task |
|-------|------|
| 12.1 | Demo video: init, create, compile, validate |
| 12.2 | Landing page / GitHub showcase |
| 12.3 | PyPI public release |
| 12.4 | Tag v1.0.0-public |

---

## CADEIA DE DEPENDENCIA

Wave 6 (Genesis Engine) <- TUDO depende disso
  |
Wave 7 (Self-Build) <- prova que funciona
  |
Wave 8 (Real Agents) <- produto tangivel
  |                     |
Wave 9 (Testing)   Wave 11 (Content)  <- paralelos
  |
Wave 10 (Packaging)
  |
Wave 12 (Launch)

---

## GENESIS: O LOOP AUTO-REFERENCIAL

O ciclo completo:

  USER INTENT: "quero agente X"
       |
  8F GAP ANALYSIS: motor identifica 8 dimensoes faltando
       |
  CREW DISPATCH: seleciona crew de builders para cada gap
       |
  BUILDER EXECUTION: cada builder e invocado como agente especializado
    - system-prompt-builder (BECOME)
    - knowledge-card-builder (INJECT)
    - instruction-builder (REASON)
    - skill-builder (CALL)
    - response-format-builder (PRODUCE)
    - validation-schema-builder (CONSTRAIN)
    - quality-gate-builder (GOVERN)
    - dispatch-rule-builder (COLLABORATE)
       |
  HANDOFF CHAIN: output de cada builder -> input do proximo
       |
  COMPILE + GOVERN: valida contra schemas + quality gates
       |
  AGENTE COMPLETO: 8/8 dimensoes, em N0X_nucleus/

E quando o agente sendo construido E um builder?
-> CEX constroi builders que constroem agentes que constroem builders.
-> Loop auto-referencial: GENESIS.

---

## PLANOS OBSOLETOS (arquivados)

| Plano | Status | Substituido por |
|-------|--------|-----------------|
| OVERNIGHT_REPORT next steps | DONE (batches 18-20) | Este roadmap |
| CHECKPOINT Waves 6-9 | REORDENADO | Wave 6 = Genesis |
| PHASE3_WAVE_PLAN | DONE (70 builders) | Wave 7 = self-build |
| Whitepaper Day 1/2/3 | TEORICO | Wave 8 = real agents |

---

*v1.0 | 2026-03-28 | Fonte unica de verdade para planejamento CEX*
