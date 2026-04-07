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

| User says | System means | CEX implementation |
|-----------|-------------|-------------------|
| card | artifact | .md file with YAML frontmatter |
| deck | loaded context | artifacts assembled for one agent per task |
| base deck | boot context | deck_n0X.md + rules + sin identity (loaded on startup) |
| mission deck | task context | handoff + referenced builders + KCs + templates |
| hand | active context | all artifacts loaded during one 8F pipeline run |
| draw | F3 INJECT | pulling artifacts from library into active context |
| play | F6 PRODUCE | generating output using loaded context |
| round | 8F cycle | one complete F1-F8 pipeline execution |
| table | grid dispatch | multiple agents working in parallel |
| dealer | N07 orchestrator | selects context, writes handoffs, dispatches |
| slot | {{mustache}} variable | template field the LLM fills contextually |
| combo | context combination | multiple artifacts assembled for compound effect |
| library | CEX repository | all artifacts across 12 pillars + 117 kinds |
| game | pipeline | the 8F execution flow |

## Architecture Metaphors

| User says | System means | CEX implementation |
|-----------|-------------|-------------------|
| genesis | base layer | archetypes/ + P{01-12}/ schemas + templates (read-only molds) |
| mold | archetype builder | archetypes/builders/{kind}-builder/ (13 components) |
| filled mold | nucleus artifact | N{01-06}_*/ domain-specific instances |
| fractal | mirrored structure | nuclei mirror the 12 pillar categories |
| building | CEX system | the full repository with all layers |
| floor | nucleus department | one N0X directory with its artifacts |
| superintendent | nucleus agent | the LLM running in that nucleus |
| department | sector/domain | research, marketing, builder, knowledge, operations, commercial |

## Process Metaphors

| User says | System means | CEX implementation |
|-----------|-------------|-------------------|
| spawn | launch process | Start-Process cmd -> boot/n0X.cmd -> pi |
| kill | terminate process | taskkill /F /PID /T (tree-kill) |
| idle | completed but alive | process finished task, waiting for input |
| boot | startup sequence | CMD sets theme -> pi loads deck + rules + prompt |
| overnight | autonomous background run | boot/overnight_h1.cmd (evolve + audit) |
| grid | parallel layout | 6 windows, 2x3, dynamic resolution |
| signal | completion message | .cex/runtime/signals/signal_n0X_*.json |
| handoff | task document | .cex/runtime/handoffs/n0X_task.md |
| wave | sequential group | set of parallel dispatches with gate between |

## Quality Metaphors

| User says | System means | CEX implementation |
|-----------|-------------|-------------------|
| improve | evolve artifact | cex_evolve.py (heuristic or agent mode) |
| fix | update/refactor | edit specific file or tool |
| check | audit/validate | cex_doctor.py + cex_flywheel_audit.py |
| clean | sanitize | cex_sanitize.py (ASCII compliance) |
| gate | quality threshold | quality >= 8.5 to pass, cex_score.py |
| ship | release | cex_release_check.py (28 checks, all green) |

## Brand Metaphors

| User says | System means | CEX implementation |
|-----------|-------------|-------------------|
| blank brain | unbootstrapped CEX | {{BRAND_*}} variables unresolved |
| assimilate | bootstrap brand | /init -> brand_config.yaml -> brand_inject.py |
| the X | brand variable | CEX = C + E + X, where X = the brand identity |
| digital asset | configured CEX instance | CEX + brand = specialized AI system |

## Rule

When writing artifacts, handoffs, or code: use the "System means" column. The "User says" column is for understanding human input, not for output.
