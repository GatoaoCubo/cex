---
id: p01_kc_n03_software_engineering
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "N03 Master KC — Software Engineering Capabilities"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.1
tags: [n03, software-engineering, master-kc, capabilities]
tldr: "Master knowledge card for N03's software engineering capabilities. Maps 12 platform KCs + 23 CEX tools + software-project-builder into a unified engineering model. N03 can now: scaffold, implement, test, lint, dockerize, CI/CD, deploy, and review."
density_score: 1.0
when_to_use: "Apply when master knowledge card for n03's software engineering capabilities. maps 12 platform kcs + 23 cex ..."
keywords: [verticalization, knowledge-card, layer, already, master]
linked_artifacts:
  primary: null
  related: []
related:
  - p12_dr_software_project
  - bld_sp_instruction_software_project
  - p12_mission_software_engineering_n03
  - bld_sp_collaboration_software_project
  - bld_sp_manifest_software_project
  - bld_sp_system_prompt_software_project
  - p12_wf_spec_to_code
  - p04_tool_software_project
  - p12_dr_builder_nucleus
  - bld_sp_schema_software_project
---

# N03 Software Engineering — Master KC

## What N03 Knows (After Verticalization)

### Layer 1: Meta-Construction (Bootstrap — Already Had)
- 8F Pipeline (F1→F8) — mandatory for every artifact
- 11 Construction Laws (3 layers: Foundation/Execution/Quality)
- 3-Phase Build Protocol (pre-flight/execute/synthesize)
- 300 kinds, 301 builders, kind resolution via Motor
- Quality gates (H01-H07, 12LP, 5D rubric)

### Layer 2: Software Engineering (NEW — This Mission)
- **Python project structure**: pyproject.toml, hatchling, src layout, CLI entry points
- **Testing**: pytest fixtures, conftest, parametrize, markers, coverage
- **Linting**: Ruff (lint+format), mypy (types), pre-commit hooks
- **Containerization**: Multi-stage Docker, compose, non-root, healthcheck
- **CI/CD**: GitHub Actions (11 workflow patterns from codexa-core)
- **Deploy**: Railway, Render, nixpacks, Procfile
- **Security**: 5-layer scanning (deps, secrets, SAST, container, CodeQL)
- **Code review**: 7-dimension rubric, GitHub MCP, PR validation
- **Error handling**: Exception hierarchy, retry, circuit breaker, structured logging
- **API patterns**: FastAPI middleware stack, Pydantic models, dependency injection

### Layer 3: Self-Knowledge (NEW — CEX Tooling)
- 23 CEX tools documented (was 4/23, now 23/23)
- Tool dependency graph understood
- Can explain/modify/extend any CEX tool

## Capability Matrix

| Task | KC Source | Builder Step |
|------|----------|-------------|
| "scaffold Python project" | kc_python_project_structure | SCAFFOLD (step 2) |
| "implement FastAPI service" | kc_fastapi_patterns | IMPLEMENT (step 3) |
| "write pytest tests" | kc_pytest_patterns | TEST (step 4) |
| "configure Ruff linting" | kc_ruff_uv | LINT (step 5) |
| "create Dockerfile" | kc_docker_patterns | DOCKER (step 6) |
| "setup GitHub Actions CI" | kc_github_actions | CI (step 7) |
| "deploy to Railway" | kc_deploy_paas | DEPLOY (step 8) |
| "review PR on GitHub" | kc_code_review | REVIEW (step 9) |
| "add security scanning" | kc_security_practices | CI (security job) |
| "handle errors properly" | kc_error_handling_python | IMPLEMENT (error layer) |
| "validate data models" | kc_pydantic_patterns | IMPLEMENT (models) |
| "setup pre-commit hooks" | kc_git_hooks_ci | LINT (hooks) |

## Cross-Nucleus Service Map

```
N01 says: "implement research pipeline"
  → N03 reads: bld_instruction_research_pipeline + kc_fastapi_patterns
  → N03 outputs: src/research_pipeline/ + tests/ + Dockerfile + CI

N02 says: "implement social publisher"
  → N03 reads: bld_instruction_social_publisher + kc_python_project_structure
  → N03 outputs: src/social_publisher/ + tests/ + Dockerfile + CI

N04 says: "deploy Supabase migrations"
  → N03 reads: kc_supabase_database + kc_deploy_paas
  → N03 runs: supabase db push + health check

N07 says: "add --batch flag to 8F runner"
  → N03 reads: kc_cex_tooling_master + kc_cex_8f_runner
  → N03 modifies: _tools/cex_8f_runner.py + tests
```

## Knowledge Inventory

| Category | Count | Location |
|----------|-------|----------|
| Platform KCs (software eng) | 12 | P01_knowledge/library/platform/ |
| CEX Tooling KC (master) | 1 | N03_engineering/P01_knowledge/ |
| Builder ISOs | 14 | archetypes/builders/software-project-builder/ |
| Instance config template | 1 | _instances/_template/N03_engineering/ |
| Dispatch rules | 2 | N03_engineering/P12_orchestration/ |
| Workflows | 2 | N03_engineering/P12_orchestration/ |


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dr_software_project]] | downstream | 0.52 |
| [[bld_sp_instruction_software_project]] | downstream | 0.47 |
| [[p12_mission_software_engineering_n03]] | downstream | 0.43 |
| [[bld_sp_collaboration_software_project]] | downstream | 0.42 |
| [[bld_sp_manifest_software_project]] | downstream | 0.39 |
| [[bld_sp_system_prompt_software_project]] | downstream | 0.38 |
| [[p12_wf_spec_to_code]] | downstream | 0.37 |
| [[p04_tool_software_project]] | downstream | 0.34 |
| [[p12_dr_builder_nucleus]] | downstream | 0.28 |
| [[bld_sp_schema_software_project]] | downstream | 0.28 |
