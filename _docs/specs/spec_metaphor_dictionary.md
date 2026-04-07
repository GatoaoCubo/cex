---
id: spec_metaphor_dictionary
kind: context_doc
title: Metaphor Dictionary -- Internal Language to Universal Terms
version: 1.0.0
quality: 9.0
pillar: P01
created: 2026-04-07
purpose: When the user says X, the system means Y. Translation table for all internal metaphors.
density_score: 1.0
---

# Metaphor Dictionary

The user (and internal docs) use metaphors to explain concepts. LLMs and artifacts must use universal terms. This dictionary maps one to the other.

## Game Architecture Metaphors

| User says | System means | Industry term | CEX implementation |
|-----------|-------------|---------------|-------------------|
| card | artifact | **artifact** (MLOps, CI/CD) | .md file with YAML frontmatter |
| deck (file) | agent self-description | **agent card** (Google A2A, MCP) | agent_card_n0X.md — capabilities, routing, gaps |
| deck (concept) | assembled context | **context assembly** (prompt eng.) | artifacts selected + composed for one task |
| base deck | boot context | **system prompt** / agent init | agent_card + rules + sin identity (loaded on startup) |
| mission deck | task context | **task spec** / instruction payload | task_spec + referenced builders + KCs + templates |
| hand | active context | **working context** / working set (OS) | all artifacts loaded during one 8F pipeline run |
| draw | F3 INJECT | **retrieval** (the R in RAG) | pulling artifacts from library into working context |
| play | F6 PRODUCE | **generation** / inference | generating output using loaded context |
| round | 8F cycle | **pipeline run** (MLOps) | one complete F1-F8 pipeline execution |
| table | grid dispatch | **multi-agent orchestration** (LangGraph, CrewAI) | multiple agents working in parallel |
| dealer | N07 orchestrator | **orchestrator** / supervisor agent | selects context, writes task specs, dispatches |
| slot | {{mustache}} variable | **template variable** / slot (NLU) | template field the LLM fills contextually |
| combo | context combination | **prompt composition** | multiple artifacts assembled for compound effect |
| library | CEX repository | **knowledge base** / artifact store | all artifacts across 12 pillars + 117 kinds |
| game | pipeline | **pipeline** (MLOps, CI/CD) | the 8F execution flow |

## Architecture Metaphors

| User says | System means | Industry term | CEX implementation |
|-----------|-------------|---------------|-------------------|
| genesis | base layer | **schema layer** / archetype layer | archetypes/ + P{01-12}/ schemas + templates (read-only) |
| mold | archetype builder | **archetype** / template (OOP: class) | archetypes/builders/{kind}-builder/ (13 components) |
| filled mold | nucleus artifact | **instance** (OOP: class→instance) | N{01-06}_*/ domain-specific instances |
| fractal | mirrored structure | **convention over configuration** (Rails) | nuclei mirror the 12 pillar categories |
| building | CEX system | **system** / repository | the full repository with all layers |
| floor | nucleus domain | **agent domain** | one N0X directory with its artifacts |
| superintendent | nucleus agent | **autonomous agent** | the LLM running in that nucleus |
| department | sector/domain | **domain** | research, marketing, builder, knowledge, operations, commercial |

## Process Metaphors

| User says | System means | Industry term | CEX implementation |
|-----------|-------------|---------------|-------------------|
| spawn | launch process | **spawn/fork** (POSIX) ✅ | Start-Process cmd -> boot/n0X.cmd -> pi |
| kill | terminate process | **kill/SIGTERM** (POSIX) ✅ | taskkill /F /PID /T (tree-kill) |
| idle | completed but alive | **idle** ✅ | process finished task, waiting for input |
| boot | startup sequence | **bootstrap** ✅ | CMD sets theme -> pi loads agent card + rules + prompt |
| overnight | autonomous background run | **batch job** / cron job | boot/overnight_h1.cmd (evolve + audit) |
| grid | parallel layout | **agent topology** / multi-agent layout | 6 windows, 2x3, dynamic resolution |
| signal | completion message | **event/signal** (POSIX, event-driven) ✅ | .cex/runtime/signals/signal_n0X_*.json |
| handoff | task document | **task spec** (CEX keeps "handoff" as convention) | .cex/runtime/handoffs/n0X_task.md |
| wave | sequential group | **execution phase** / wave (deployment) ✅ | set of parallel dispatches with gate between |

## Quality Metaphors

| User says | System means | Industry term | CEX implementation |
|-----------|-------------|---------------|-------------------|
| improve | evolve artifact | **optimize** / AutoML evolve | cex_evolve.py (heuristic or agent mode) |
| fix | update/refactor | **refactor** / patch ✅ | edit specific file or tool |
| check | audit/validate | **audit** / lint ✅ | cex_doctor.py + cex_flywheel_audit.py |
| clean | sanitize | **sanitize** ✅ | cex_sanitize.py (ASCII compliance) |
| gate | quality threshold | **quality gate** (CI/CD) ✅ | quality >= 8.5 to pass, cex_score.py |
| ship | release | **release** / ship ✅ | cex_release_check.py (28 checks, all green) |

## Brand Metaphors

| User says | System means | Industry term | CEX implementation |
|-----------|-------------|---------------|-------------------|
| blank brain | unbootstrapped CEX | **unconfigured instance** | {{BRAND_*}} variables unresolved |
| assimilate | bootstrap brand | **bootstrap** / provision ✅ | /init -> brand_config.yaml -> brand_inject.py |
| the X | brand variable | **brand identity** (unique to CEX) | CEX = C + E + X, where X = the brand identity |
| digital asset | configured CEX instance | **configured instance** / deployed agent | CEX + brand = specialized AI system |

## Rules

1. **Artifacts, code, docs**: use "Industry term" column. ALWAYS.
2. **User input**: accept "User says" column, translate silently.
3. **This dictionary**: the ONLY place both columns coexist.
4. **Llama-7B test**: if the term needs this dictionary to be understood, it's wrong for artifacts.
5. **Rename cascade**: changing a term requires CRUD across all files that reference it. See `N07_admin/memory/terminology_standardization.md` for the full map.
