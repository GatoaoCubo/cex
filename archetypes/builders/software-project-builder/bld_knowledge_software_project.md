---
id: bld_sp_knowledge_card_software_project
kind: knowledge_card
pillar: P01
title: "Knowledge Card — Software Project Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.1
tags: [builder, knowledge-card, software-project, python, patterns]
tldr: "Core knowledge for building Python projects: 3 project archetypes (CLI/API/pipeline), tech stack decisions, dependency tiers, the 'spec→code' bridge pattern from codexa-core production system."
density_score: 1.0
when_to_use: "Apply when core knowledge for building python projects: 3 project archetypes (cli/api/pipeline), tech stack ..."
keywords: [knowledge-card, project, software-engineering, rich, archetypes]
linked_artifacts:
  primary: null
  related: []
llm_function: INJECT
related:
  - bld_sp_examples_software_project
  - p04_ex_software_project_pipeline_runner
  - bld_sp_system_prompt_software_project
  - p04_tpl_software_project
  - bld_sp_schema_software_project
  - p04_ex_software_project_cli_tool
  - p01_kc_python_project_structure
  - bld_sp_instruction_software_project
  - p04_ex_software_project_api_service
  - bld_sp_output_template_software_project
---
# Software Project Knowledge

This ISO describes a software project: its repository layout, modules, and build graph.

## 3 Project Archetypes

### 1. CLI Tool (Typer + Rich)
```python
app = typer.Typer(help="My CLI tool")
console = Console()
@app.command()
def run(input: str, output: str = "result.json", verbose: bool = False):
    """Execute the pipeline."""
    result = process(input)
    Path(output).write_text(json.dumps(result))
    console.print(f"[green]Done[/green]: {output}")
```
Entry point: `[project.scripts] myapp = "myapp.cli:app"`
### 2. API Service (FastAPI + Pydantic)
```python
app = FastAPI(title="My API", version="1.0.0")
app.add_middleware(CORSMiddleware, ...)
app.include_router(v1_router)
@app.get("/health")
async def health(): return {"status": "healthy", "version": "1.0.0"}
```
Stack: FastAPI + Pydantic + asyncpg + Redis + Celery
### 3. Pipeline Runner (Stage-based)
```python
class Pipeline:
    def __init__(self, config):
        self.stages = [ParseStage, TransformStage, ValidateStage, OutputStage]
    async def run(self, input_data):
        state = {"input": input_data}
        for stage_cls in self.stages:
            state = await stage_cls(self.config).execute(state)
            if state.get("error"): break
        return state
```
Pattern: Each stage has `execute(state) → state`. Mirrors CEX 8F pipeline.

## Tech Stack Decisions

| Decision | Default | Why |
|----------|---------|-----|
| Build backend | Hatchling | Fastest, no C deps |
| HTTP client | httpx | Async support, modern API |
| CLI framework | Typer | Type hints → CLI args |
| Validation | Pydantic V2 | FastAPI integration, performance |
| API framework | FastAPI | Async, OpenAPI, Pydantic native |
| Lint/format | Ruff | 100x faster than alternatives |
| Test | pytest | Fixtures, parametrize, plugins |
| Package manager | UV | 10-100x faster pip |
| Container | Docker multi-stage | Minimal runtime image |
| Deploy | Railway | Zero-config PaaS |

## The Spec→Code Bridge

CEX builders produce **specifications** (typed .md artifacts).
This builder transforms those specs into **executable code**.

```
Builder ISOs → describe WHAT the system does
                ↓
Software Project Builder → creates HOW it runs
                ↓
Outputs: pyproject.toml + src/ + tests/ + Dockerfile + CI/CD
```

### Mapping: Builder ISO → Project File

| Builder ISO | Maps To |
|-------------|---------|
| bld_system_prompt | README.md + docstrings |
| bld_instruction | src/{name}/pipeline.py (stage order) |
| bld_architecture | src/{name}/ directory layout |
| bld_config | src/{name}/config.py (BaseSettings) |
| bld_schema | src/{name}/models.py (Pydantic) |
| bld_quality_gate | tests/ + .github/workflows/ci.yml |
| bld_error_handling | src/{name}/errors.py |
| bld_tools | pyproject.toml [dependencies] |
| bld_examples | tests/test_examples.py |

## Dependency Tiers

```toml
# Tier 0: Zero deps (stdlib only)
dependencies = []

# Tier 1: Minimal (validation + HTTP)
dependencies = ["pydantic>=2.0", "httpx>=0.24"]

# Tier 2: CLI (add Typer + Rich)
dependencies = ["pydantic>=2.0", "typer>=0.9", "rich>=13.0"]

# Tier 3: API (add FastAPI + uvicorn)
dependencies = ["fastapi>=0.100", "uvicorn[standard]>=0.23", "pydantic>=2.0"]

# Tier 4: Full (add DB + cache + async)
dependencies = [..., "asyncpg>=0.29", "redis>=5.0", "celery>=5.3"]
```


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_sp_examples_software_project]] | downstream | 0.56 |
| [[p04_ex_software_project_pipeline_runner]] | downstream | 0.41 |
| [[bld_sp_system_prompt_software_project]] | downstream | 0.41 |
| [[p04_tpl_software_project]] | downstream | 0.39 |
| [[bld_sp_schema_software_project]] | downstream | 0.39 |
| [[p04_ex_software_project_cli_tool]] | downstream | 0.37 |
| [[p01_kc_python_project_structure]] | sibling | 0.36 |
| [[bld_sp_instruction_software_project]] | downstream | 0.34 |
| [[p04_ex_software_project_api_service]] | downstream | 0.31 |
| [[bld_sp_output_template_software_project]] | downstream | 0.31 |
