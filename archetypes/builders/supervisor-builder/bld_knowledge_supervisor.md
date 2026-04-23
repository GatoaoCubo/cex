---
kind: knowledge_card
id: bld_knowledge_card_supervisor
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for supervisor artifact production
sources: CEX P08 schema, cex_mission_runner.py, cex_coordinator.py, multi-agent orchestration literature (CrewAI, LangChain, OpenAI, Anthropic)
quality: 9.1
title: "Knowledge Card Supervisor"
version: "1.0.0"
author: n03_builder
tags: [supervisor, builder, examples]
tldr: "Golden and anti-examples for supervisor construction, demonstrating ideal structure and common pitfalls."
domain: "supervisor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_director_builder
  - p01_kc_supervisor
  - bld_instruction_supervisor
  - bld_config_supervisor
  - supervisor-builder
  - bld_collaboration_supervisor
  - p11_qg_director
  - bld_architecture_supervisor
  - bld_schema_supervisor
  - bld_examples_supervisor
---

# Domain Knowledge: supervisor
## Executive Summary
A supervisor is the crew orchestration artifact in CEX — a declarative coordination plan that dispatches multiple builders across waves without executing tasks itself. The supervisor kind defines HOW builders are coordinated: dispatch order, signal gates, fallback behavior, and consensus gathering. Every supervisor requires a builders list (>= 2), explicit dispatch_mode, signal_check, wave_topology, and fallback_per_builder.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P08 (architecture) |
| llm_function | ORCHESTRATE (coordination, never execution) |
| Required fields | topic, builders, dispatch_mode, signal_check |
| Max body | 2048 bytes |
| Naming | ex_director_{topic}.md |
| Quality gates | 8 HARD + 10 SOFT |
| Dispatch modes | sequential, parallel, conditional |
## Patterns
- **Wave dispatch**: builders grouped into ordered waves; Wave N+1 starts only after all Wave N signals received
- **Conditional routing**: route to specific builders based on task type or signal content
- **Consensus gather**: collect all builder outputs before synthesis step
- **Parallel fan-out**: independent builders run simultaneously within a wave for speed
| Pattern | When to Use | CEX Tool |
|---------|-------------|----------|
| Wave dispatch | Builders have inter-wave dependencies | cex_mission_runner.py |
| Conditional routing | Task type determines which builders activate | cex_coordinator.py |
| Consensus gather | All outputs needed before merge | cex_signal_watch.py |
| Parallel fan-out | Independent builders within same wave | _spawn/dispatch.sh grid |
## Cross-Framework Map
| Framework | Equivalent | Notes |
|-----------|-----------|-------|
| CrewAI | Crew + manager_agent (hierarchical) | Most direct: manager delegates, workers execute |
| LangChain | RunnableParallel + LCEL compose | Fan-out chains with orchestration |
| OpenAI | Orchestrator assistant pattern | Meta-assistant calling assistants via tools |
| Anthropic | Orchestrator agent_group pattern | Dispatch spawns + monitor signals |
| LlamaIndex | AgentWorkflow multi-agent | Event-driven agent coordination |
| DSPy | Ensemble / pipeline Module | Sub-module coordination with voting |
## Anti-Patterns
| Anti-Pattern | Why it fails | Fix |
|-------------|-------------|-----|
| Supervisor that executes | Violates orchestration boundary — builders get confused | Supervisor ONLY dispatches, NEVER executes |
| No signal wait | Assumes builders finish instantly — causes data races | Always signal_check: true unless explicit fire-and-forget |
| Nested directors >2 levels | Spaghetti orchestration — impossible to debug | Flatten to max 2 levels |
| Silent dispatch_mode default | Sequential when parallel intended (or vice versa) | Always set dispatch_mode explicitly |
| Missing fallback | One builder failure kills entire mission | Define fallback_per_builder for every builder |
## Application
1. Define mission scope: what outcome do the builders collectively produce?
2. List builders: name, nucleus, role — minimum 2
3. Map waves: group builders by dependency order
4. Set dispatch_mode: sequential for safety, parallel for speed, conditional for routing
5. Define signal_check: true unless explicitly fire-and-forget
6. Configure fallback_per_builder: retry, skip, substitute(alternate), or abort
7. Validate: no execution logic in body, all builders have fallbacks, wave topology is consistent
## References
- CEX: cex_mission_runner.py (autonomous orchestration), cex_coordinator.py (wave gates), _spawn/dispatch.sh (dispatch)
- CrewAI: hierarchical Crew with manager_agent delegation pattern
- Anthropic: multi-agent orchestration patterns (building effective agents, 2025)
- OpenAI: orchestrator pattern in Assistants API with function-calling dispatch

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_director_builder]] | downstream | 0.58 |
| [[p01_kc_supervisor]] | sibling | 0.51 |
| [[bld_instruction_supervisor]] | downstream | 0.50 |
| [[bld_config_supervisor]] | downstream | 0.49 |
| [[supervisor-builder]] | downstream | 0.47 |
| [[bld_collaboration_supervisor]] | downstream | 0.44 |
| [[p11_qg_director]] | downstream | 0.42 |
| [[bld_architecture_supervisor]] | downstream | 0.41 |
| [[bld_schema_supervisor]] | downstream | 0.39 |
| [[bld_examples_supervisor]] | downstream | 0.39 |
