---
id: pspec_n07_operational_intelligence
kind: constraint_spec
pillar: P06
title: PSPEC N07 -- Operational Intelligence Layer
version: 2.0.0
created: 2026-04-01
updated: 2026-04-01
author: n07_admin
domain: orchestration-operations
quality_target: 9.0
status: SPEC
scope: N07_admin
tags: [pspec, n07, autonomous, workflows, patterns, plan, spec, grid]
tldr: User needs 4 commands (/plan /spec /grid /consolidate). N07 auto-chains 14 internal workflows + 53 KCs.
density_score: 0.97
---

# PSPEC N07 -- Operational Intelligence Layer v2

## THE INSIGHT

The user is NOT a DevOps engineer. The user says:
- "quero uma landing page" (I want a landing page)
- "pesquisa os concorrentes" (research competitors)
- "prepara o deploy" (prepare the deploy)

The user needs **4 commands**. N07 does the rest autonomously.

## USER SURFACE (4 commands)

| Command | Universal term | What user says | What N07 does |
|---------|---------------|----------------|---------------|
|  | Project planning | "planeja X", "quero fazer Y" | Decompose > hydrate > route > handoff > dispatch |
|  | Specification | "cria spec de X", "documenta Y" | Research > analyze > write constraint doc |
|  | Parallel dispatch | "executa", "roda o grid" | Fan-out handoffs > spawn nuclei > monitor |
|  | Post-execution | "consolida", "finaliza" | Collect > verify > stop > commit > push |

Both  and  are universal:
- plan = project management (sprint planning, OKR decomposition)
- spec = engineering (RFC, PRD, design doc, technical spec)
- grid = parallel execution (MapReduce, fan-out)
- consolidate = post-processing (ETL, data warehouse)

### /plan vs /spec

| Aspect | /plan | /spec |
|--------|-------|-------|
| Purpose | WHAT to do | WHAT to build |
| Output | Handoffs + dispatch order | Specification document |
| Leads to | /grid (execution) | /plan (planning from spec) |
| Scope | Operational (tasks) | Documentary (design) |
| Example | "plan: rebuild N06" | "spec: brand verticalization" |
| CEX kind | dag (P12) | constraint_spec (P06) |
| Autonomy | High (auto-route) | Medium (user reviews) |

Typical flow:  first (write the plan) >  (decompose into tasks) >  (execute) >  (clean up).
Or skip /spec:  directly (N07 auto-specs internally).

---

## N07 AUTONOMOUS BEHAVIORS (internal, never user-invoked)

These are workflows N07 chains AUTOMATICALLY inside /plan and /grid:

| Behavior | When N07 triggers it | Industry pattern |
|----------|---------------------|------------------|
| hydrate | Every user input, before routing | Data enrichment (ETL) |
| health_check | Before dispatching any nucleus | Health probe (k8s) |
| research | When knowledge gap detected during planning | Competitive intelligence |
| compose | When assembling prompt for nucleus | RAG prompt chaining |
| review | When nucleus output arrives | Code review (PR) |
| debug | When error occurs during execution | Root cause analysis (ITIL) |
| ship | When all tasks pass quality gate | CI/CD pipeline |
| rollback | When deploy fails health check | SRE rollback procedure |
| security_scan | Before deploy to production | VAPT (OWASP) |
| handoff | When session ends or context overflow | Shift handoff (ops) |
| evolve | When gap detector finds missing KCs | Continuous learning (MLOps) |
| diagnose | When /health shows degraded state | Observability (SRE) |

User never types these. N07 invokes them as sub-workflows.

### How /plan chains them:


---

## 8F DECOMPOSITION

### F1 CONSTRAIN
User commands: 4 max. Internal workflows: validated against P12 schema.
KCs: validated against P01 schema. All use existing CEX kinds.

### F2 BECOME
N07 = Operational Intelligence Hub. 4 user commands, 12 autonomous behaviors.
User sees simplicity. N07 handles complexity internally.

### F3 INJECT
53 KCs total: 30 universal (migrate), 15 skill patterns (distill), 8 framework (extract).
These feed the autonomous behaviors with knowledge.

### F4 REASON
/plan: intent -> decompose -> route. /spec: intent -> research -> document.
Internal behaviors: triggered by conditions, not user input.

### F5 CALL
4 user commands in .claude/commands/. 12 internal workflows in P12.
Internal workflows call _tools/ and _spawn/ as needed.

### F6 PRODUCE
/plan: execution plan (dag + handoffs). /spec: constraint_spec document.
/grid: dispatch report. /consolidate: completion report.

### F7 GOVERN
Auto-review gates every nucleus output. Auto-health before dispatch.
Auto-security before deploy. Quality >= 8.0 or redo.

### F8 COLLABORATE
N07 dispatches to all nuclei via /grid. Nuclei signal back.
N07 never builds -- only plans, specs, dispatches, consolidates.

