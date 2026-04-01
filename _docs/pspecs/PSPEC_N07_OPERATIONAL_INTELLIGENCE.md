---
id: pspec_n07_operational_intelligence
kind: constraint_spec
pillar: P06
title: PSPEC N07 -- Operational Intelligence Layer
version: 1.0.0
created: 2026-04-01
author: n07_admin
domain: orchestration-operations
quality_target: 9.0
status: SPEC
scope: N07_admin
tags: [pspec, n07, workflows, patterns, operational, intelligence]
tldr: N07 gains 14 operational workflows + 53 universal KCs. Maps real-world DevOps/AI concepts to CEX kinds.
density_score: 0.96
---

# PSPEC N07 -- Operational Intelligence Layer

## THE PROBLEM

CEX has 108 sub-agents, 46 tools, 8F pipeline. But lacks operational muscle:
no cross-session transfer, no deploy pipeline, no health dashboard, no security audit,
no knowledge gap detection, no parallel dispatch from within a session.
These are REAL-WORLD operations concepts. Not invented taxonomy.

## REAL-WORLD NAME MAPPING

| codexa name | Real-world concept | Industry term | CEX kind |
|-------------|-------------------|---------------|----------|
| /handoff | Session context transfer | Shift handoff (medicine, ops) | workflow P12 |
| /ship | Deploy pipeline | CI/CD ship (GitHub, GitLab) | workflow P12 |
| /health | System health check | Health probe (k8s, Docker) | workflow P12 |
| /debug-error | Systematic debugging | Root Cause Analysis (ITIL) | workflow P12 |
| /security-scan | Vulnerability assessment | VAPT (OWASP, NIST) | workflow P12 |
| /spawn | Parallel task dispatch | Fan-out (distributed systems) | spawn_config P12 |
| /research | Structured web research | Competitive Intelligence (CI) | workflow P12 |
| /rollback | Service rollback | Rollback (SRE, DevOps) | workflow P12 |
| /evolve | Knowledge gap fill | Continuous Learning (MLOps) | workflow P12 |
| /compose | Prompt assembly | RAG/Prompt Chaining (LLM eng) | workflow P12 |
| /diagnose | System audit | Observability (SRE) | workflow P12 |
| /hydrate | Input enrichment | Data Enrichment (ETL/sales) | workflow P12 |
| /review | Peer review | Code Review (GitHub PR) | workflow P12 |
| /consolidate | Deduplication | Consolidation (data warehouse) | workflow P12 |

All 14 are standard industry operations. Zero invented taxonomy.
CEX kind system already supports: workflow, handoff, spawn_config, knowledge_card, cli_tool.

---

## 8F DECOMPOSITION

### F1 CONSTRAIN
Workflows: P12/_schema.yaml (max 3072 bytes). KCs: P01/_schema.yaml. Tools: P04/_schema.yaml.
Every workflow: trigger, input, output, steps, guards, timeout.

### F2 BECOME
N07 evolves: basic orchestrator -> Operational Intelligence Hub.
Gains: self-diagnosis, deploy management, security awareness, knowledge curation.
Does NOT execute (dispatches to N03/N05). DECIDES which workflow to invoke.

### F3 INJECT
30 universal KCs (Tier 2 migrate), 15 pattern KCs (Tier 3 distill), 8 framework KCs (extract). Total: 53 new KCs.

### F4 REASON
N07 system prompt gains workflow routing. Intent keywords trigger workflows.
Complexity scoring: direct (simple) vs dispatch (complex).

### F5 CALL
14 workflows invokable as /commands. Each references P04 tools. Workflows dispatch to nuclei.

### F6 PRODUCE
Health reports, handoff docs, deploy logs, security reports, gap reports, consolidation reports.

### F7 GOVERN
Workflow execution passes quality gate. Health covers: git, tools, nuclei, knowledge, config.
Security covers: OWASP Top 10, secrets, dependencies. Deploy verifies health < 30s.

### F8 COLLABORATE
N07 dispatches heavy work: /ship->N05, /research->N01, /review->N03, /security->N05.
N07 keeps: /health, /diagnose, /consolidate, /handoff, /hydrate, /evolve.

---

## WAVE 1: OPERATIONAL WORKFLOWS (P12) -- 14 CREATE

All follow tpl_workflow.md. Naming: p12_wf_{name}.md

### 1.1 p12_wf_handoff.md (Session Context Transfer)
Industry: Shift handoff (medicine). scan state > compress > save to .cex/runtime/handoffs/ > output reference. Captures: goals, progress, decisions, next steps, file changes.

### 1.2 p12_wf_ship.md (Deploy Pipeline)
Industry: CI/CD ship. validate > conventional commit > git push > railway up > health check < 30s > log. Dispatches to N05.

### 1.3 p12_wf_health.md (System Health Check)
Industry: k8s health probes. check git > check tools > check nuclei (7) > check KCs > check config > check errors. Output: dashboard green/yellow/red. < 30s.

### 1.4 p12_wf_debug.md (Root Cause Analysis)
Industry: ITIL 5-Whys RCA. reproduce > stack trace > root cause (5-whys) > propose fix > implement > verify > document. Dispatches to N03/N05.

### 1.5 p12_wf_security_scan.md (Vulnerability Assessment)
Industry: OWASP ASVS. dependency audit > secrets scan > OWASP Top 10 > config review > report. Dispatches to N05.

### 1.6 p12_wf_dispatch.md (Parallel Fan-Out)
Industry: MapReduce. decompose > create handoffs > validate independence > spawn via _spawn/ > monitor signals > collect. Uses spawn_grid.ps1.

### 1.7 p12_wf_research.md (Competitive Intelligence)
Industry: Market research. define scope > sources > scrape (firecrawl) > extract patterns > synthesize KC > validate. Dispatches to N01.

### 1.8 p12_wf_rollback.md (Service Rollback)
Industry: SRE rollback. identify service > check versions > railway rollback > verify health > notify. Dispatches to N05.

### 1.9 p12_wf_evolve.md (Continuous Learning)
Industry: MLOps continuous learning. scan KCs > detect gaps > prioritize > research > generate KCs > validate > integrate. Dispatches to N04.

### 1.10 p12_wf_compose.md (Prompt Assembly)
Industry: RAG prompt chaining. parse intent > retrieve KCs > retrieve ISOs > inject brand > assemble > optimize tokens. Uses cex_crew_runner.py.

### 1.11 p12_wf_diagnose.md (System Audit)
Industry: SRE observability. health + CLAUDE.md check + hooks + artifact count + quality scores + git log + disk. Output: findings + risk.

### 1.12 p12_wf_hydrate.md (Input Enrichment)
Industry: Data enrichment (ETL). parse input > extract intent > find KCs > find agents > add brand context > suggest routing.

### 1.13 p12_wf_review.md (Peer Review)
Industry: GitHub PR review. identify artifacts > check schema > check quality > check style > check completeness. Dispatches to N03.

### 1.14 p12_wf_consolidate.md (Deduplication)
Industry: DW consolidation. scan KCs > compute similarity (TF-IDF) > identify duplicates > suggest merges > report. Uses cex_retriever.py.

---

## WAVE 2: UNIVERSAL KCs (P01) -- 30 MIGRATE from codexa-core

Copy from pool/knowledge/, scrub satellite names, keep patterns.

### llm_patterns/ (13 KCs)
chain_of_thought, llm_tool_use, agent_self_healing, llm_autonomy, meta_agent_factory, recursive_refinement, open_variable, prompt_caching, continuous_batching, multi_agent_orchestration, prompt_engineering, universal_llm, rag_hybrid_search.

### anti_patterns/ (4 KCs)
anti_file_storage, anti_full_context, anti_isolated_sessions, anti_patterns_general.

### operations/ (5 KCs)
zero_touch_execution, error_recovery, test_automation, quality_gates, production_monitoring.

### orchestration/ (5 KCs)
orchestration_coordination, orchestration_enterprise, memory_consolidation, subagent_forking, subagent_dispatch.

### meta/ (3 KCs)
claude_md_patterns, mcp_server_patterns, tdd_as_llm_skill.

---

## WAVE 3: DISTILLED SKILL PATTERNS (P01) -- 15 CREATE

NEW KCs distilled from 128 skills. Location: P01_knowledge/library/patterns/

| KC | Source skill | Pattern |
|----|-------------|--------|
| pattern_extraction | pattern_extractor | Mine reusable patterns from code |
| knowledge_distillation | knowledge_distillation | Compress knowledge 10:1 |
| gap_detection | gap_detector | Systematic coverage analysis |
| confidence_scoring | confidence_scorer | Trust-based routing 0-1 |
| token_budgeting | token_budget_enforcer | Token counting + allocation |
| source_triangulation | source_triangulator | 3+ source cross-reference |
| query_decomposition | query_decomposer | Complex -> sub-queries |
| prompt_evolution | prompt_evolution | Iterative prompt optimization |
| iterative_refinement | recursive_refiner | Quality improvement loops |
| memory_management | memory_consolidation | Merge, prune, decay |
| web_scraping_ethics | web_scraper | Ethical: robots.txt, rate limits |
| seo_technical | seo_optimizer | Technical SEO checklist |
| incident_response | incident_response | ITIL incident flow |
| context_overflow | context_overflow_manager | Strategies when > window |
| self_healing | self_healing_code | Auto-fix patterns |

---

## WAVE 4: FRAMEWORK PATTERN KCs (P01) -- 8 CREATE

De-branded from codexa-core/records/framework/docs/. Location: P01_knowledge/library/frameworks/

| KC | Source | Pattern |
|----|--------|--------|
| input_hydration | IHP doc | Enrich user input before processing |
| operational_laws | LAWS_v3 | Operational principles for agent systems |
| context_scoping | CONTEXT_CONDITIONAL | File-scoped context (Stripe pattern) |
| distillation_pipeline | DISTILLATION_GUIDE | RAG > rerank > distill > template |
| spawn_patterns | SPAWN_PLAYBOOK | Solo, grid, continuous batching |
| meta_bootstrap | META_BOOTSTRAP | Self-constructing system patterns |
| qa_validation | QA_VALIDATION | Quality assurance for agent outputs |
| workflow_orchestration | WORKFLOW_ORCH | Multi-step coordination |

---

## TOTALS

| Wave | Category | Count | Kind | Pillar |
|------|----------|-------|------|--------|
| W1 | Operational Workflows | 14 | workflow | P12 |
| W2 | Universal KCs (migrate) | 30 | knowledge_card | P01 |
| W3 | Skill Patterns (distill) | 15 | knowledge_card | P01 |
| W4 | Framework Patterns (extract) | 8 | knowledge_card | P01 |
| **Total** | | **67** | | |

All 67 use existing CEX kinds. Zero new taxonomy.

## EXECUTION: 4 focused sessions.

N07 becomes Operational Intelligence Hub: 14 workflows + 53 KCs + zero invented terms.
