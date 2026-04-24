---
id: p04_tool_software_project
kind: cli_tool
8f: F5_call
pillar: P04
title: "Software Project Tool — N03 CLI"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.1
tags: [cli-tool, software-project, scaffold, test, deploy, n03]
tldr: "CLI tool for N03 software project operations: scaffold (new project), implement (spec→code), test (run pytest), lint (ruff+mypy), docker (build container), deploy (railway/render), review (PR check)."
density_score: 0.89
related:
  - bld_sp_instruction_software_project
  - bld_sp_system_prompt_software_project
  - bld_sp_schema_software_project
  - p04_tpl_software_project
  - p01_kc_software_project
  - p12_dr_software_project
  - p02_agent_software_project_manifest
  - bld_sp_knowledge_card_software_project
  - p04_ct_cex_init
  - bld_sp_quality_gate_software_project
---

# Software Project Tool

## Commands

### scaffold — Create new project

```bash
python -m n03_tools.software_project scaffold \
  --name my-pipeline \
  --type pipeline_runner \
  --python 3.12 \
  --deps "pydantic,httpx,typer"
```

**Output**: pyproject.toml + src/ + tests/ + Dockerfile + .github/

### implement — Transform spec into code

```bash
python -m n03_tools.software_project implement \
  --builder archetypes/builders/research-pipeline-builder/ \
  --config _instances/codexa/N01_intelligence/research_pipeline_config.md \
  --output ./projects/research-pipeline/
```

**Input**: Builder ISOs + instance config
**Output**: Complete Python project with all code

### test — Run project tests

```bash
python -m n03_tools.software_project test \
  --project ./projects/research-pipeline/ \
  --markers "not slow" \
  --coverage
```

### lint — Check code quality

```bash
python -m n03_tools.software_project lint \
  --project ./projects/research-pipeline/ \
  --fix  # Auto-fix issues
```

### docker — Build container

```bash
python -m n03_tools.software_project docker \
  --project ./projects/research-pipeline/ \
  --tag research-pipeline:latest
```

### deploy — Deploy to PaaS

```bash
python -m n03_tools.software_project deploy \
  --project ./projects/research-pipeline/ \
  --target railway \
  --environment staging
```

### review — Check project quality

```bash
python -m n03_tools.software_project review \
  --project ./projects/research-pipeline/ \
  --rubric 7d  # 7-dimension review
```

## Integration with 8F Pipeline

```
Intent: "implement research pipeline in Python"
  → F1 CONSTRAIN: load project schema
  → F2 BECOME: software project builder identity
  → F3 INJECT: builder ISOs + platform KCs + instance config
  → F4 REASON: plan project structure
  → F5 CALL: identify tools (pytest, ruff, docker, railway)
  → F6 PRODUCE: generate project files
  → F7 GOVERN: 8 quality gates (syntax, tests, lint, secrets, docker, ci, health, deps)
  → F8 COLLABORATE: save + commit + signal
```

## Dependencies

- Python ≥ 3.10
- hatch, uv, ruff, mypy, pytest (for project building)
- docker (for container building)
- @railway/cli (for Railway deploy)
- @anthropic/mcp-server-github (for PR review)


## Integration Checklist

Software project tools must satisfy these operational requirements:

- **Reproducible builds**: running the same command twice produces identical output
- **Dependency lockfiles**: all dependencies pinned to exact versions in lockfile
- **Test harness**: project includes test runner with minimum 80% coverage target
- **CI-ready**: project includes configuration for at least one CI provider

| Check | Tool | Threshold |
|-------|------|-----------|
| Build reproducibility | Hash comparison | 100% match |
| Dependency freshness | Version checker | < 90 days old |
| Test coverage | Coverage reporter | >= 80% lines |
| Lint compliance | Linter | 0 errors |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_sp_instruction_software_project]] | upstream | 0.48 |
| [[bld_sp_system_prompt_software_project]] | upstream | 0.43 |
| [[bld_sp_schema_software_project]] | upstream | 0.39 |
| [[p04_tpl_software_project]] | related | 0.38 |
| [[p01_kc_software_project]] | upstream | 0.36 |
| [[p12_dr_software_project]] | downstream | 0.34 |
| [[p02_agent_software_project_manifest]] | upstream | 0.32 |
| [[bld_sp_knowledge_card_software_project]] | upstream | 0.30 |
| [[p04_ct_cex_init]] | sibling | 0.30 |
| [[bld_sp_quality_gate_software_project]] | downstream | 0.29 |
