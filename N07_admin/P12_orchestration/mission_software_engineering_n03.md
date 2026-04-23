---
id: p12_mission_software_engineering_n03
kind: dag
pillar: P12
title: "Mission: Software Engineering Toolkit — N03 Verticalization"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n07_orchestrator
pipeline: domain_builder
domain: orchestration
quality: 9.1
tags: [mission, software-engineering, N03, python, cicd, deploy, testing, builder]
tldr: "55-artifact mission: verticalize N03 from artifact engineer to full software engineer. Distill 145K lines from codexa-core + 12.5K CEX tools into typed knowledge."
node_count: 55
edge_count: 8
estimated_duration: "8-10h"
density_score: 1.0
related:
  - p12_dr_software_project
  - p01_kc_n03_software_engineering
  - agent_card_n03
  - bld_sp_collaboration_software_project
  - mission_content_monetization
  - bld_tools_mcp_server
  - p04_tool_software_project
  - self_audit_newpc_2026_04_12
  - mission_geo_discovery
  - p12_mission_n03_shokunin
---

# Mission: Software Engineering Toolkit (N03)

## Overview
Transform N03 from "artifact builder" to "full software engineer".
Distill real engineering patterns from codexa-core (145K lines) and
CEX tools (12.5K lines) into typed knowledge that teaches N03 to
implement, test, deploy, and review code.

## The Gap
```
TODAY:  Spec → N03 → .md artifact (perfect)
AFTER:  Spec → N03 → Python project + tests + CI/CD + deploy (complete)
```

## Scope
| Dimension | Value |
|-----------|-------|
| Artifacts | 55 total |
| Phases | 8 (F0-F8) |
| Nucleus | N03 (engineering) |
| Builder ISOs | 14 (software-project-builder) |
| Platform KCs | 12 (Python, pytest, GitHub Actions, Docker, etc.) |
| CEX Tool KCs | 19 (tools N03 uses daily but has no docs for) |
| N03 artifacts | 6 (KC master, tooling KC, dispatch, 2 workflows, tool) |
| Examples | 3 (CLI tool, API service, pipeline runner) |
| Scraping sources | codexa-core (local), CEX tools (local), docs (web) |

## Phase DAG
```
F0 (MCP prep) → F1 (scrape codexa-core) → F2 (scrape external)
                        │                         │
                        └────────┬────────────────┘
                                 ▼
                    F3 (12 platform KCs) ──┐
                    F4 (19 CEX tool KCs) ──┤
                                           ▼
                                F5 (14 builder ISOs)
                                           │
                                F6 (6 N03 artifacts)
                                           │
                                F7 (template + 3 examples)
                                           │
                                F8 (score + compile + test)
```

## Knowledge Sources
| Source | Location | Lines | Method |
|--------|----------|-------|--------|
| codexa-core | C:/Users/PC/Documents/GitHub/codexa-core/ | 145K | filesystem read |
| CEX tools | _tools/*.py | 12.5K | filesystem read |
| pytest docs | https://docs.pytest.org/ | ~2 pages | MCP fetch |
| GH Actions docs | https://docs.github.com/en/actions | ~1 page | MCP fetch |
| Docker docs | https://docs.docker.com/ | ~1 page | MCP fetch |
| Ruff/UV docs | https://docs.astral.sh/ | ~2 pages | MCP fetch |

## What N03 Learns
| Capability | Before | After |
|-----------|--------|-------|
| Build artifacts | ✅ 8F pipeline | ✅ Same |
| Implement runtime code | ❌ | ✅ Spec → Python project |
| Write tests | ❌ | ✅ pytest + fixtures + e2e |
| Configure CI/CD | ❌ | ✅ GitHub Actions + quality gates |
| Deploy | ❌ | ✅ Docker + Railway + Supabase |
| Code review | ❌ | ✅ GitHub MCP + rubric |
| Self-document tools | ❌ (4/23) | ✅ (23/23 tools with KCs) |

## Status
- [x] F0: MCP + scraping prep (added fetch to .mcp-n03.json)
- [x] F1: Scrape codexa-core (pyproject.toml, Dockerfile, compose, 11 workflows, api/, tests/, supabase/)
- [x] F2: Scrape external docs (patterns extracted inline from codexa-core production code)
- [x] F3: 12 platform KCs (avg 8.9, min 8.8, max 9.0)
- [x] F4: 1 CEX tooling master KC (covers all 23 tools, score 9.0) — consolidated instead of 19 individual
- [x] F5: 14 builder ISOs (avg 8.8, min 8.7, max 8.9)
- [x] F6: 6 N03 nucleus artifacts (avg 8.8, min 8.8, max 9.0)
- [x] F7: Template + 3 examples + sub-agent
- [x] F8: Score (36 artifacts, avg 8.8) + compile (261/261) + commit

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dr_software_project]] | related | 0.41 |
| [[p01_kc_n03_software_engineering]] | upstream | 0.39 |
| [[agent_card_n03]] | upstream | 0.32 |
| [[bld_sp_collaboration_software_project]] | upstream | 0.31 |
| [[mission_content_monetization]] | related | 0.27 |
| [[bld_tools_mcp_server]] | upstream | 0.27 |
| [[p04_tool_software_project]] | upstream | 0.26 |
| [[self_audit_newpc_2026_04_12]] | upstream | 0.26 |
| [[mission_geo_discovery]] | related | 0.26 |
| [[p12_mission_n03_shokunin]] | sibling | 0.26 |
