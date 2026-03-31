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
quality: null
tags: [mission, software-engineering, N03, python, cicd, deploy, testing, builder]
tldr: "55-artifact mission: verticalize N03 from artifact engineer to full software engineer. Distill 145K lines from codexa-core + 12.5K CEX tools into typed knowledge."
node_count: 55
edge_count: 8
estimated_duration: "8-10h"
density_score: 0.92
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
- [ ] F0: MCP + scraping prep
- [ ] F1: Scrape codexa-core
- [ ] F2: Scrape external docs
- [ ] F3: 12 platform KCs
- [ ] F4: 19 CEX tool KCs
- [ ] F5: 14 builder ISOs
- [ ] F6: 6 N03 nucleus artifacts
- [ ] F7: Template + 3 examples
- [ ] F8: Score + compile + test + commit
