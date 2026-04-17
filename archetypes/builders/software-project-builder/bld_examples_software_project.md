---
id: bld_sp_examples_software_project
kind: example
pillar: P04
title: "Examples — Software Project Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [builder, examples, software-project, cli, api, pipeline]
tldr: "3 concrete project examples: CLI scoring tool (Typer+Rich), API service (FastAPI+Supabase+Stripe), Pipeline runner (stage-based like 8F). Each shows pyproject.toml + key files."
density_score: 0.90
llm_function: GOVERN
---
# Software Project Builder — Examples

This ISO describes a software project: its repository layout, modules, and build graph.

## Example 1: CLI Scoring Tool

**Intent**: "Build a CLI tool that scores CEX artifacts"

```toml
# pyproject.toml
[project]
name = "cex-scorer"
version = "1.0.0"
dependencies = ["pydantic>=2.0", "typer>=0.9", "rich>=13.0", "pyyaml>=6.0"]
[project.scripts]
cex-score = "cex_scorer.cli:app"
[tool.ruff]
line-length = 100
select = ["E", "W", "F", "I", "B", "UP"]
```

```python
# cli.py — Typer+Rich entry point
app = typer.Typer(help="Score CEX artifacts")
@app.command()
def score(path: str, verbose: bool = False):
    result = score_artifact(path)
    color = "green" if result.score >= 8.0 else "yellow"
    Console().print(f"[{color}]{result.score:.1f}[/{color}] {path}")
```

```python
# conftest.py — pytest fixtures
@pytest.fixture
def sample_artifact(tmp_path):
    f = tmp_path / "test.md"
    f.write_text("---\nid: t\nkind: knowledge_card\npillar: P01\nquality: null\n---\n# T\nBody.")
    return str(f)
```

## Example 2: API Service

**Intent**: "Build a FastAPI service for product management"

```toml
# pyproject.toml
[project]
name = "product-api"
version = "1.0.0"
dependencies = ["fastapi>=0.100", "uvicorn[standard]>=0.23", "pydantic>=2.0", "httpx>=0.24", "asyncpg>=0.29"]
[project.scripts]
product-api = "product_api.cli:main"
```

```python
# models.py — Pydantic V2 with Field constraints
class Product(BaseModel):
    model_config = {"from_attributes": True}
    id: str
    name: str = Field(..., min_length=1, max_length=300)
    price: float = Field(..., gt=0)
    sku: str = Field(..., pattern=r'^[A-Z0-9-]{3,20}$')
# config.py — BaseSettings with env_prefix
class Settings(BaseSettings):
    model_config = {"env_prefix": "APP_"}
    database_url: str
    debug: bool = False
```

```dockerfile
FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
FROM python:3.12-slim
RUN useradd --uid 1000 appuser
COPY --from=builder /usr/local /usr/local
COPY --chown=appuser src/ ./src/
USER appuser
CMD ["uvicorn", "product_api.api.main:app", "--host", "0.0.0.0"]
```

## Example 3: Pipeline Runner

**Intent**: "Build a pipeline runner for research processing"

```python
# pipeline.py — Stage-based like CEX 8F
@dataclass
class StageResult:
    stage: str; success: bool; data: dict; error: str | None = None
class Stage:
    name: str = "base"
    async def execute(self, state: dict) -> StageResult: raise NotImplementedError
class IntentStage(Stage):
    name = "intent"
    async def execute(self, state):
        return StageResult(self.name, True, {"intent": parse(state["input"]["query"])})
class Pipeline:
    def __init__(self, stages: list[Stage]): self.stages = stages
    async def run(self, input_data: dict) -> dict:
        state = {"input": input_data, "stages": []}
        for stage in self.stages:
            result = await stage.execute(state)
            state["stages"].append(result)
            state[result.stage] = result.data
            if not result.success: break
        return state
```

```yaml
# ci.yml — lint→test→build
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install -e ".[dev]"
      - run: ruff check . && pytest --cov -m "not slow"
```
