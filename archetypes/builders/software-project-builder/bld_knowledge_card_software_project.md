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
quality: 8.9
tags: [builder, knowledge-card, software-project, python, patterns]
tldr: "Core knowledge for building Python projects: 3 project archetypes (CLI/API/pipeline), tech stack decisions, dependency tiers, the 'spec→code' bridge pattern from codexa-core production system."
density_score: 0.91
---

# Software Project Knowledge

## 3 Project Archetypes

### 1. CLI Tool (Typer + Rich)

```python
# src/myapp/cli.py
import typer
from rich.console import Console

app = typer.Typer(help="My CLI tool")
console = Console()

@app.command()
def run(input: str, output: str = "result.json", verbose: bool = False):
    """Execute the pipeline."""
    if verbose: console.print("[bold]Starting...[/bold]")
    result = process(input)
    Path(output).write_text(json.dumps(result))
    console.print(f"[green]Done[/green]: {output}")

if __name__ == "__main__": app()
```

**Entry point**: `[project.scripts] myapp = "myapp.cli:app"`

### 2. API Service (FastAPI + Pydantic)

```python
# src/myapp/api/main.py
app = FastAPI(title="My API", version="1.0.0")
app.add_middleware(CORSMiddleware, ...)
app.include_router(v1_router)

@app.get("/health")
async def health(): return {"status": "healthy", "version": "1.0.0"}
```

**Stack**: FastAPI + Pydantic + asyncpg + Redis + Celery

### 3. Pipeline Runner (Stage-based)

```python
# src/myapp/pipeline.py
class Pipeline:
    def __init__(self, config):
        self.stages = [
            ParseStage(config),
            TransformStage(config),
            ValidateStage(config),
            OutputStage(config),
        ]

    async def run(self, input_data):
        state = {"input": input_data}
        for stage in self.stages:
            state = await stage.execute(state)
            if state.get("error"): break
        return state
```

**Pattern**: Each stage is a class with `execute(state) → state`. Like CEX 8F.

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
