---
id: spec_n07_operational_intelligence
kind: constraint_spec
pillar: P06
title: Spec N07 -- Operational Intelligence Layer
version: 2.0.0
created: 2026-04-01
updated: 2026-04-01
author: n07_admin
domain: orchestration-operations
quality_target: 9.0
status: EXECUTED
scope: N07_admin
tags: [spec, n07, autonomous, workflows, patterns, plan, spec, grid]
tldr: User needs 4 commands (/plan /spec /grid /consolidate). N07 auto-chains 14 internal workflows + 53 KCs.
density_score: 0.97
quality: 9.1
---

# Spec N07 -- Operational Intelligence Layer v2

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

---

## CEX TAXONOMY AUDIT

104 kinds total. Breakdown:
- 43 universal (industry standard: agent, api_client, dag, webhook, workflow...)
- 30 AI-domain (recognized in LLM eng: prompt_template, chain, mcp_server, quality_gate...)
- 13 semi-standard (recognized in context: decision_record/ADR, schedule/cron, env_config...)
- 18 CEX-invented (axiom, bugloop, director, law, lens, effort_profile...)

**Score: 83% standard taxonomy. 17% CEX-specific.**

The 18 invented kinds serve internal CEX mechanics. Not exposed to users.
User-facing artifacts use standard kinds: workflow, knowledge_card, agent, constraint_spec.

**No skill kind exists in CEX.** codexa-core skills map to:
- knowledge_card (P01) — the knowledge of HOW to do something
- workflow (P12) — the STEPS to execute something
- pattern (P08) — a reusable architectural pattern
- cli_tool (P04) — an executable script

---

## ARTIFACT MANIFEST

### Wave 1: User Commands (3 REWRITE + 1 CREATE)

| # | File | Action | Maps to |
|---|------|--------|--------|
| 1 | .claude/commands/plan.md | REWRITE /mission | decompose > hydrate > route > handoff |
| 2 | .claude/commands/spec.md | CREATE | research > analyze > write constraint_spec |
| 3 | .claude/commands/grid.md | REWRITE /dispatch | fan-out > spawn nuclei > monitor |
| 4 | .claude/commands/consolidate.md | KEEP+refine | collect > verify > stop > commit |

### Wave 2: Autonomous Workflows (12 CREATE, kind: workflow P12)

N07 invokes these internally. User never types them.

| # | File | Auto-trigger | Industry pattern |
|---|------|-------------|------------------|
| 5 | p12_wf_auto_hydrate | Every user input | Data enrichment |
| 6 | p12_wf_auto_health | Before dispatch | Health probe (k8s) |
| 7 | p12_wf_auto_research | Knowledge gap found | Competitive intel |
| 8 | p12_wf_auto_compose | Prompt assembly | RAG chaining |
| 9 | p12_wf_auto_review | Nucleus output arrives | PR review |
| 10 | p12_wf_auto_debug | Error during execution | RCA / 5-Whys |
| 11 | p12_wf_auto_ship | Quality gate passes | CI/CD pipeline |
| 12 | p12_wf_auto_rollback | Deploy fails health | SRE rollback |
| 13 | p12_wf_auto_security | Before production | OWASP VAPT |
| 14 | p12_wf_auto_handoff | Session end / overflow | Shift handoff |
| 15 | p12_wf_auto_evolve | Gap detector triggers | Continuous learning |
| 16 | p12_wf_auto_diagnose | Health degraded | SRE observability |

### Wave 3: Knowledge (53 KCs, kind: knowledge_card P01)

30 MIGRATE (from codexa-core, scrub branding):
  llm_patterns/(13): CoT, tool_use, self_healing, autonomy, meta_factory, refinement, open_var, caching, batching, orchestration, prompt_eng, universal_llm, rag_hybrid
  anti_patterns/(4): file_storage, full_context, isolated_sessions, general
  operations/(5): zero_touch, error_recovery, test_automation, quality_gates, monitoring
  orchestration/(5): coordination, enterprise, memory_consolidation, forking, dispatch
  meta/(3): claude_md_patterns, mcp_server_patterns, tdd_as_llm_skill

15 CREATE (distilled from codexa-core skills):
  patterns/: pattern_extraction, knowledge_distillation, gap_detection, confidence_scoring, token_budgeting, source_triangulation, query_decomposition, prompt_evolution, iterative_refinement, memory_management, web_scraping_ethics, seo_technical, incident_response, context_overflow, self_healing

8 CREATE (extracted from codexa-core framework docs):
  frameworks/: input_hydration, operational_laws, context_scoping, distillation_pipeline, spawn_patterns, meta_bootstrap, qa_validation, workflow_orchestration

---

## TOTALS

| Wave | What | Count | Action |
|------|------|-------|--------|
| W1 | User commands | 4 | 2 REWRITE + 1 CREATE + 1 KEEP |
| W2 | Auto workflows | 12 | CREATE |
| W3a | Universal KCs | 30 | MIGRATE |
| W3b | Skill pattern KCs | 15 | CREATE |
| W3c | Framework KCs | 8 | CREATE |
| **Total** | | **69** | |

## USER EXPERIENCE

/spec "evolve N06 into brand architect" -> N07 writes Spec
/plan "execute N06 Spec waves 1-2" -> N07 decomposes, presents plan
/grid -> N07 dispatches, monitors, auto-reviews
/consolidate -> N07 collects, verifies, commits, pushes

4 commands. Everything else autonomous. 83% standard taxonomy.

---

## ADDENDUM: kind:skill REGISTERED (v2.1 fix)

CEX had a skill-builder (9 ISO files), 3 KCs about skills, and AgentSkills.io spec knowledge.
But `kind: skill` was never registered in kinds_meta.json. Gap fixed:

- kinds_meta.json: 104 -> 105 kinds (skill added to P04)
- archetypes/builders/skill-builder/: 9 ISO files materialized from proof/
- .claude/agents/skill-builder.md: agent registered (109th)

**skill** is the most universal term in AI agent systems:
Alexa Skills, Semantic Kernel Skills, AgentSkills.io, AutoGPT, Devin.
Boundary: trigger + phases + reusable. No identity (that is agent). No orchestration (that is workflow).

### Revised taxonomy score
- 44 universal + 30 AI-domain + 13 semi + 18 invented = 105 kinds
- skill joins universal tier (Alexa, Semantic Kernel, AgentSkills.io)
- **84% standard taxonomy** (was 83%)
