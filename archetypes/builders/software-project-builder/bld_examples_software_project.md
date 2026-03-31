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
quality: 8.8
tags: [builder, examples, software-project, cli, api, pipeline]
tldr: "3 concrete project examples: CLI scoring tool (Typer+Rich), API service (FastAPI+Supabase+Stripe), Pipeline runner (stage-based like 8F). Each shows pyproject.toml + key files."
density_score: 0.90
---

# Software Project Builder — Examples

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
# src/cex_scorer/cli.py
import typer; from rich.console import Console
app = typer.Typer(help="Score CEX artifacts")
console = Console()

@app.command()
def score(path: str, verbose: bool = False):
    from .scorer import score_artifact
    result = score_artifact(path)
    color = "green" if result.score >= 8.0 else "yellow"
    console.print(f"[{color}]{result.score:.1f}[/{color}] {path}")
    if verbose:
        for note in result.notes: console.print(f"  {note}")
```

```python
# tests/conftest.py
import pytest; from pathlib import Path
@pytest.fixture
def sample_artifact(tmp_path):
    f = tmp_path / "test.md"
    f.write_text("---\nid: test\nkind: knowledge_card\npillar: P01\nquality: null\n---\n# Test\nContent here.")
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
# src/product_api/models.py
from pydantic import BaseModel, Field
class Product(BaseModel):
    model_config = {"from_attributes": True}
    id: str
    name: str = Field(..., min_length=1, max_length=300)
    price: float = Field(..., gt=0)
    sku: str = Field(..., pattern=r'^[A-Z0-9-]{3,20}$')

# src/product_api/config.py
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    model_config = {"env_prefix": "APP_"}
    database_url: str
    api_keys: str = ""
    debug: bool = False
```

```dockerfile
# Dockerfile
FROM python:3.12-slim AS builder
WORKDIR /build
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.12-slim
RUN useradd --uid 1000 appuser
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY --chown=appuser src/ ./src/
USER appuser
CMD ["uvicorn", "product_api.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Example 3: Pipeline Runner

**Intent**: "Build a pipeline runner for research processing"

```python
# src/research_runner/pipeline.py
from dataclasses import dataclass
from typing import Any

@dataclass
class StageResult:
    stage: str
    success: bool
    data: dict
    error: str | None = None

class Stage:
    name: str = "base"
    async def execute(self, state: dict) -> StageResult:
        raise NotImplementedError

class IntentStage(Stage):
    name = "intent"
    async def execute(self, state):
        query = state["input"]["query"]
        return StageResult(self.name, True, {"intent": parse(query)})

class RetrieveStage(Stage):
    name = "retrieve"
    async def execute(self, state):
        sources = await fetch_sources(state["intent"])
        return StageResult(self.name, True, {"sources": sources})

class Pipeline:
    def __init__(self, stages: list[Stage]):
        self.stages = stages

    async def run(self, input_data: dict) -> dict:
        state = {"input": input_data, "stages": []}
        for stage in self.stages:
            result = await stage.execute(state)
            state["stages"].append(result)
            state[result.stage] = result.data
            if not result.success:
                state["error"] = result.error
                break
        return state
```

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12', cache: 'pip' }
      - run: pip install -e ".[dev]"
      - run: ruff check .
      - run: pytest --cov --cov-report=xml -m "not slow"
```
