---
id: deck_n05
kind: context_doc
title: N05 Deck -- Available Capabilities
nucleus: N05
sin: Ira Construtiva
version: 1.0.0
pillar: P08
quality: null
created: 2026-04-07
---

## Identity

| Field | Value |
|-------|-------|
| Nucleus | N05 Operations |
| Sin | Ira Construtiva (Constructive Wrath) |
| Domain | Code review, testing, debugging, deployment, CI/CD, infrastructure, monitoring |
| CLI | claude (Opus 4.6, 1M context) |
| Sub-agents | Up to 5 parallel |
| Route TO N05 | Code review, testing, debugging, deploy, CI/CD, infrastructure, monitoring |
| Route AWAY | Research (N01), marketing (N02), artifact construction (N03) |

## My Artifacts

| Subdir | Count | Purpose |
|--------|-------|---------|
| agents | 1 | Agent definition for operations nucleus |
| architecture | 1 | Agent card with capabilities and routing |
| feedback | 1 | Quality gate definitions and validation rules |
| knowledge | 8 | Domain KCs: Railway, health monitoring, deployments, Nixpacks, PostgreSQL, Uvicorn |
| memory | 1 | Checkpoint for session state persistence |
| orchestration | 3 | Dispatch rules, spawn config, workflow definitions |
| output | 11 | Deploy checklists, env contracts, health endpoints, middleware, Railway configs, SDK audits |
| prompts | 1 | System prompt for N05 persona and behavior |
| schemas | 6 | API response, env contract, health check, middleware, Railway TOML, startup sequence |
| compiled | 20 | YAML compilations of source artifacts |
| **Total** | **33** | **(source .md files, excluding compiled)** |

## Kinds I Build

| Kind | Pillar | Domain Relevance |
|------|--------|-----------------|
| benchmark | P07 | Performance benchmarks and load testing |
| bugloop | P11 | Bug detection, reproduction, fix verification loops |
| checkpoint | P12 | Session state snapshots for recovery |
| code_executor | P04 | Sandboxed code execution environments |
| daemon | P04 | Background services and process management |
| dag | P12 | Directed acyclic graphs for pipeline orchestration |
| e2e_eval | P07 | End-to-end integration testing evaluation |
| env_config | P09 | Environment variable contracts and validation |
| eval_dataset | P07 | Test datasets for evaluation suites |
| golden_test | P07 | Canonical test cases with known-good outputs |
| hook | P04 | Pre/post execution hooks (git, CI, deploy) |
| hook_config | P04 | Hook configuration and trigger rules |
| lifecycle_rule | P11 | Artifact and process lifecycle management |
| output_validator | P05 | Output format and schema validation |
| quality_gate | P11 | Pass/fail gates for CI and deploy pipelines |
| regression_check | P07 | Regression detection between versions |
| runtime_rule | P09 | Runtime behavior constraints and policies |
| runtime_state | P10 | Runtime state tracking and inspection |
| reward_signal | P11 | Quality feedback signals for improvement loops |
| schedule | P12 | Cron and time-based task scheduling |
| signal | P12 | Inter-nucleus and inter-process signaling |
| smoke_eval | P07 | Quick-pass validation for deployment readiness |
| trace_config | P07 | Observability, tracing, and telemetry setup |
| unit_eval | P07 | Unit-level test evaluation |
| validator | P06 | Schema and data validation logic |
| red_team_eval | P07 | Security and adversarial testing |
| webhook | P04 | Webhook endpoint configuration and handling |
| workflow | P12 | Multi-step pipeline orchestration |

**28 kinds** across 8 pillars (P04, P05, P06, P07, P09, P10, P11, P12).

## Tools I Use

| Tool | Purpose |
|------|---------|
| `cex_compile.py` | Compile .md artifacts to .yaml |
| `cex_doctor.py` | Builder health check -- validates all 118 builders |
| `cex_hooks.py` | Pre/post validation hooks + git pre-commit |
| `cex_system_test.py` | Full system validation (54 tests) |
| `cex_e2e_test.py` | End-to-end test runner |
| `cex_score.py` | Peer review scoring (--apply) |
| `cex_feedback.py` | Quality tracking, archive, metrics |
| `cex_quality_monitor.py` | Quality snapshots + regression detection |
| `cex_sanitize.py` | ASCII-only enforcement for code files |
| `cex_release_check.py` | Release gate: README, deps, CI, versions |
| `cex_flywheel_audit.py` | Doc vs practice: 109 checks, 7 layers, 7 wires |
| `cex_signal_watch.py` | Blocking signal poll for nucleus completion |
| `cex_8f_runner.py` | Full 8F pipeline executor |
| `signal_writer.py` | Inter-nucleus signal emission |

## MCP Servers

| Server | Purpose |
|--------|---------|
| `@anthropic-ai/mcp-server-postgres` | PostgreSQL database access -- query, inspect, validate schemas |
| `@anthropic/mcp-server-github` | GitHub API -- PRs, issues, checks, releases, code review |

## My Strengths

1. **Deep Railway expertise**: 7 domain KCs covering Railway platform, CLI, networking, PostgreSQL, Nixpacks, Uvicorn, zero-downtime deploys
2. **Schema-driven contracts**: 6 schema artifacts define strict API response, env, health check, middleware, Railway TOML, and startup sequence contracts
3. **Deploy pipeline coverage**: Checklists, rollback plans, env contracts, health endpoints -- full deploy lifecycle
4. **Quality enforcement**: Quality gates, hooks, validators, regression checks, smoke evals -- the N05 toolbelt for CI/CD
5. **Broad eval coverage**: 8 eval/test kinds (unit, e2e, smoke, golden, regression, red-team, benchmark, eval-dataset) for comprehensive validation
6. **Observability**: Trace configs, health monitoring KCs, signal infrastructure

## My Gaps

| Gap | Description |
|-----|-------------|
| agents/ | Only 1 agent definition -- could have specialized sub-agents for deploy, test, review |
| architecture/ | Only 1 agent card -- missing architecture decision records for infra choices |
| memory/ | Only 1 checkpoint -- no persistent session memory across operations |
| prompts/ | Only 1 system prompt -- could have specialized prompts for review, deploy, debug modes |
| feedback/ | Only 1 quality gate -- needs more domain-specific gates (security, performance, a11y) |
| Missing kinds built | No `trace_config`, `benchmark`, `smoke_eval`, `regression_check` artifacts yet -- kinds exist but no N05 instances |
| No CI/CD pipeline artifacts | No GitHub Actions, Railway deploy configs, or automation workflows in output/ |
| No security artifacts | No `red_team_eval` or security-focused validation schemas |

## Cards in My Deck

| Category | Count |
|----------|-------|
| Source artifacts (.md) | 33 |
| Compiled artifacts (.yaml) | 20 |
| Kinds I can build | 28 |
| Tools relevant to my domain | 14 |
| MCP servers | 2 |
| Infrastructure KCs (shared library) | 10 |
| **Total cards** | **107** |
