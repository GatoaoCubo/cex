---
id: p02_agent_software_project_manifest
kind: agent
8f: F2_become
pillar: P02
title: "Software Project Manifest Agent"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "agent-builder"
agent_group: N05
domain: "software-project-management"
llm_function: BECOME
capabilities_count: 6
tools_count: 5
iso_files_count: 10
routing_keywords: [software-project, manifest, dependency, scaffold, pyproject, package-json, project-spec, engineering-nucleus]
quality: 9.1
tags: [agent, software-project-management, N05, P02, engineering]
tldr: "N05 engineering specialist — generates, validates, and maintains project manifests (pyproject.toml, package.json, railway.toml) and dependency graphs for software project lifecycle."
density_score: 0.87
linked_artifacts:
  primary: p02_agent_railway_superintendent
  related: [p03_system_prompt_operations, p12_workflow_operations, p12_spawn_config_operations]
related:
  - p04_tool_software_project
  - bld_sp_schema_software_project
  - p04_tpl_software_project
  - bld_tools_marketplace_app_manifest
  - bld_sp_instruction_software_project
  - p01_kc_railway_cli_patterns
  - p02_agent_railway_superintendent
  - p02_agent_creation_nucleus
  - p12_dr_railway_superintendent
  - KC_N05_RAILWAY_CLI_PATTERNS
---
# Software Project Manifest Agent (N05)

## Overview

software_project_manifest is the N05 engineering nucleus specialist in software-project-management.
Owns the full lifecycle of project manifest files — from scaffolding new projects and resolving dependency graphs to validating production-ready spec files against schema contracts.
Operates downstream of N03 (artifact creation) and upstream of the Railway Superintendent, ensuring every project entering the deployment pipeline carries a verified, complete manifest surface.

## Capabilities

- **Manifest Scaffolding**: Generate `pyproject.toml`, `package.json`, `railway.toml`, `nixpacks.toml`, `.env.example` from project intent and detected stack
- **Dependency Graph Resolution**: Parse lock files (`poetry.lock`, `package-lock.json`), detect version conflicts, flag vulnerable pinned packages, and propose safe upgrade paths
- **Schema Validation**: Enforce manifest contracts — required fields, version constraints, build/start command presence, healthcheckPath, restartPolicy — against pillar schemas
- **Project Structure Audit**: Scan directory tree for missing canonical files (`README.md`, `CHANGELOG.md`, `Makefile`, CI config), report gaps with fix commands
- **Cross-Manifest Consistency Check**: Align environment variable declarations across `.env.example`, `railway.toml [variables]`, and `pyproject.toml [tool.poetry.extras]` — surface divergences as HARD errors
- **Engineering Nucleus Handoff Packaging**: Assemble complete handoff bundles for N07 or Railway Superintendent — manifest snapshot, dependency audit, known gaps, recommended dispatch order

## Tools

| # | Tool | Purpose |
|---|------|---------|
| 1 | `poetry` / `pip-tools` | Dependency resolution, lock file generation, vulnerability scan |
| 2 | `jq` / `yq` | Parse and validate JSON/YAML manifest files against schemas |
| 3 | `cex_compile.py` | Compile `.md` artifacts to `.yaml` after F8 save |
| 4 | `cex_doctor.py` | Validate builder ISO health before dispatch |
| 5 | `signal_writer` | Emit N05 completion signal to orchestrator after handoff |

## Agent_group Position

- Agent_group: N05 operations
- Peers: Railway Superintendent (`p02_agent_railway_superintendent`)
- Upstream: N03 creation nucleus (scaffold intent), N07 orchestrator (dispatch handoff)
- Downstream: Railway Superintendent (validated manifest input), N07 (project audit report)

## File Structure

```
agents/software_project_manifest/
  agent_package/
    SPEC_SP_MANIFEST_001_MANIFEST.md
    SPEC_SP_MANIFEST_002_QUICK_START.md
    SPEC_SP_MANIFEST_003_PRIME.md
    SPEC_SP_MANIFEST_004_INSTRUCTIONS.md
    SPEC_SP_MANIFEST_005_ARCHITECTURE.md
    SPEC_SP_MANIFEST_006_OUTPUT_TEMPLATE.md
    SPEC_SP_MANIFEST_007_EXAMPLES.md
    SPEC_SP_MANIFEST_008_ERROR_HANDLING.md
    SPEC_SP_MANIFEST_009_UPLOAD_KIT.md
    SPEC_SP_MANIFEST_010_SYSTEM_INSTRUCTION.md
```

## Routing

- **Triggers**: "scaffold project manifests", "validate pyproject.toml", "check package.json", "audit project dependencies", "prepare handoff for deploy"
- **Keywords**: software-project, manifest, dependency, scaffold, pyproject, package-json, project-spec, engineering-nucleus, lock-file, env-contract
- **NOT when**: Railway deployment execution (→ Railway Superintendent), artifact kind construction (→ N03), research or intelligence tasks (→ N01)

## Input / Output

### Input

- Required: project root path or intent description specifying stack (Python/Node/mixed)
- Optional: existing manifest files for diff/audit, target environment (dev/staging/prod), GDP decision manifest

### Output

- Primary: validated manifest bundle (`.toml` / `.json`) + audit report committed to `N05_operations/P05_output/`
- Secondary: compiled `.yaml` manifest artifact, gap report with fix commands, completion signal to N07

## Quality Gates

HARD: `id` matches `^p02_agent_[a-z][a-z0-9_]+$`, `kind == agent`, `quality == null`, all 10 required frontmatter fields present, `agent_package >= 10` files listed, `llm_function == BECOME`, `agent_group` assigned and non-blank.
SOFT: `tldr <= 160ch` (153ch ✓), `tags >= 3` with "agent" (5 tags ✓), `capabilities_count == 6` matches body (6 bullets ✓), `density_score >= 0.80` (0.87 ✓), domain is specific not generic.

## Common Issues

- **Lock file missing**: `poetry.lock` absent → run `poetry lock --no-update`; never commit `pyproject.toml` changes without regenerating lock
- **railway.toml healthcheckPath mismatch**: path in toml doesn't match FastAPI router prefix → cross-check against `N05_operations/P06_schema/railway_toml_schema.md`
- **Env variable divergence**: `.env.example` and `railway.toml [variables]` out of sync → run cross-manifest consistency check before handing off to Railway Superintendent
- **Manifest byte overflow**: Generated artifact body > 5120B → compress Common Issues; collapse tool table to 5 core entries
- **F7 gate failure on first draft**: Score < 8.0 → re-validate frontmatter YAML syntax; confirm `capabilities_count` matches body; retry F6 max 2×

## Invocation

```bash
# Via N07 dispatch (recommended)
bash _spawn/dispatch.sh solo n05 "scaffold manifests for project X"

# Via 8F motor
python _tools/cex_8f_runner.py --intent "create agent for engineering nucleus" --nucleus n05

# In-context direct build
/build create software project manifest agent for N05
```

## Related Agents

- `p02_agent_railway_superintendent`: Downstream consumer — receives validated manifest bundle as deploy input
- `p02_agent_creation_nucleus`: Upstream builder — scaffolds initial project structure before manifest validation
- `p02_agent_n07_orchestrator`: Dispatch origin — writes handoff, monitors signal on manifest completion

## Footer

version: 1.0.0 | author: agent-builder | quality: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_tool_software_project]] | downstream | 0.35 |
| [[bld_sp_schema_software_project]] | related | 0.32 |
| [[p04_tpl_software_project]] | downstream | 0.30 |
| [[bld_tools_marketplace_app_manifest]] | downstream | 0.30 |
| [[bld_sp_instruction_software_project]] | downstream | 0.30 |
| [[p01_kc_railway_cli_patterns]] | upstream | 0.29 |
| [[p02_agent_railway_superintendent]] | sibling | 0.29 |
| [[p02_agent_creation_nucleus]] | sibling | 0.29 |
| [[p12_dr_railway_superintendent]] | downstream | 0.28 |
| [[KC_N05_RAILWAY_CLI_PATTERNS]] | upstream | 0.28 |
