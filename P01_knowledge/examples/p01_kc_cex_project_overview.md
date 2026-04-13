---
id: p01_kc_cex_project_overview
kind: knowledge_card
pillar: P01
title: "CEX — Typed Knowledge System for LLM Agents"
version: "1.0.0"
created: "2026-04-12"
updated: "2026-04-12"
author: "knowledge-card-builder"
domain: ai-orchestration
quality: 9.1
tags: [cex, architecture, nuclei, 8f-pipeline, knowledge-system, orchestration]
tldr: "CEX: 123 kinds, 12 pillars, 8 nuclei (N00-N07), 8F pipeline, 125 builders, 59 tools — transforms vague user intent into validated production artifacts."
when_to_use: "When onboarding to CEX, choosing nucleus/kind for a task, or explaining CEX topology to a collaborator."
keywords: [cex, nucleus, 8f, pillar, knowledge-system]
long_tails:
  - What nucleus should I use to build an artifact in CEX
  - How does the 8F pipeline work in CEX
  - What is the difference between nuclei in CEX
axioms:
  - ALWAYS run 8F for every task — research, build, deploy, orchestrate
  - NEVER have N07 build artifacts directly — dispatch to builder nuclei
  - ALWAYS set quality: null — peer review assigns scores, never self-score
linked_artifacts:
  primary: null
  related: [p01_kc_8f_pipeline, p01_kc_nucleus_routing]
density_score: 0.88
data_source: "https://github.com/anthropics/claude-code"
---

# CEX — Typed Knowledge System for LLM Agents

## Quick Reference
```yaml
topic: CEX system architecture
scope: 123 kinds, 12 pillars, 8 nuclei, 8F pipeline
owner: N07 (orchestrator)
criticality: high
```

## System Identity
- **123 kinds** across 12 pillars — typed artifact taxonomy
- **8 nuclei** (N00-N07) — specialized agents per domain
- **8F pipeline** — mandatory reasoning protocol for every task
- **125 builders** — one per kind, 13 ISOs each
- **59 tools** — SDK runtime (`cex_sdk/`, 78 .py files, 4504 lines)

## 12 Pillars

| Pillar | Domain | Example Kinds |
|--------|--------|---------------|
| P01 | Knowledge | knowledge_card, chunk_strategy, embedding_config |
| P02 | Model | agent, model_provider, boot_config |
| P03 | Prompt | prompt_template, action_prompt, chain |
| P04 | Tools | cli_tool, browser_tool, mcp_server |
| P05 | Output | landing_page, output_template, diagram |
| P06 | Schema | schema, validation_schema, input_schema |
| P07 | Evaluation | quality_gate, scoring_rubric, benchmark |
| P08 | Architecture | agent_card, component_map, interface |
| P09 | Config | env_config, path_config, secret_config |
| P10 | Memory | knowledge_index, memory_scope, entity_memory |
| P11 | Feedback | bugloop, learning_record, regression_check |
| P12 | Orchestration | workflow, dispatch_rule, schedule |

## 8 Nuclei

| ID | Role | Domain | Model |
|----|------|--------|-------|
| N00 | Genesis | Archetype source | — |
| N01 | Intelligence | Research, market analysis, papers | opus-4-6 1M |
| N02 | Marketing | Copy, ads, campaigns, brand voice | opus-4-6 1M |
| N03 | Builder | Artifact construction, templates, ISOs | opus-4-6 1M |
| N04 | Knowledge | RAG, embeddings, KCs, taxonomy | opus-4-6 1M |
| N05 | Operations | Code, testing, CI/CD, deploy | opus-4-6 1M |
| N06 | Commercial | Pricing, funnels, monetization | opus-4-6 1M |
| N07 | Orchestrator | Mission planning, dispatch, consolidate | opus-4-6 1M |

## 8F Pipeline

| Stage | Function | Output |
|-------|----------|--------|
| F1 CONSTRAIN | Resolve kind, pillar, schema | kind + max_bytes + naming |
| F2 BECOME | Load builder ISOs (13 per kind) | Builder identity |
| F3 INJECT | KC + memory + brand + examples | Context assembly |
| F4 REASON | Plan approach, GDP if subjective | Section plan |
| F5 CALL | Run tools, fetch references | Enriched context |
| F6 PRODUCE | Generate complete artifact | Draft with frontmatter |
| F7 GOVERN | Quality gate (floor 8.0, target 9.0) | Score + retry if fail |
| F8 COLLABORATE | Save, compile, commit, signal | Committed artifact |

## Command Reference

| Command | Purpose |
|---------|---------|
| `/init` | First-run brand setup (~2 min) |
| `/plan <goal>` | Decompose into tasks + nuclei |
| `/guide [goal]` | Co-pilot: ask before building |
| `/build <intent>` | Single artifact via 8F |
| `/grid [spec]` | Autonomous dispatch to nuclei |
| `/validate [file]` | Check artifact quality |
| `/consolidate` | Verify + score + clean after grid |
| `/status` | System health dashboard |

## Routing Rules

| Domain | Nucleus |
|--------|---------|
| Research, papers, market intel | N01 |
| Copy, ads, landing pages | N02 |
| Artifact build, templates | N03 |
| RAG, KCs, knowledge org | N04 |
| Code review, testing, deploy | N05 |
| Pricing, courses, funnels | N06 |
| Mission orchestration | N07 |

## Key Constraints
- `quality: null` — never self-score; peer review via `cex_score.py`
- ASCII-only in `.py`, `.ps1`, `.sh` (no emoji, no em-dash)
- N07 dispatches via `bash _spawn/dispatch.sh` — never builds directly
- GDP before dispatch: user decides WHAT, LLM decides HOW

## References
- Builders: `archetypes/builders/{kind}-builder/` (13 ISOs each)
- Runtime: `.cex/runtime/` (handoffs, signals, pids, decisions)
- SDK: `cex_sdk/` (78 Python files, 4504 lines)
- Rules: `.claude/rules/` (8F, GDP, per-nucleus, ASCII)