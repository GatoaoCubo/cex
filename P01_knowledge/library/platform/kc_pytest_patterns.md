---
id: p01_kc_pytest_patterns
kind: knowledge_card
pillar: P01
title: "pytest Patterns — Fixtures, Parametrize, Markers, Coverage"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [pytest, testing, fixtures, coverage, python]
tldr: "Production pytest patterns from codexa-core: conftest fixtures, TestClient, parametrize, markers (unit/integration/e2e/slow), coverage config, and async testing."
density_score: 0.93
---

# pytest Patterns

## pyproject.toml Config

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["."]
python_files = ["test_*.py"]
asyncio_mode = "auto"
addopts = ["-v", "--tb=short", "--strict-markers", "-ra"]
markers = [
    "slow: deselect with -m 'not slow'",
    "integration: requires external services",
    "unit: fast, no external deps",
    "e2e: end-to-end tests",
    "smoke: CI smoke tests",
]
filterwarnings = ["ignore::DeprecationWarning"]
```

## conftest.py (Shared Fixtures)

```python
import os
import pytest
from fastapi.testclient import TestClient

# Set test env BEFORE importing app
os.environ["ENV"] = "test"
os.environ["API_KEYS"] = "test-key-123"
os.environ["RATE_LIMIT_ENABLED"] = "false"

from api.main import app

@pytest.fixture
def client():
    """Unauthenticated test client."""
    return TestClient(app)

@pytest.fixture
def auth_client():
    """Authenticated test client."""
    c = TestClient(app)
    c.headers["X-API-Key"] = "test-key-123"
    return c

@pytest.fixture
def sample_data():
    """Reusable test data."""
    return {"name": "test", "value": 42}
```

**Key pattern**: Environment vars set BEFORE app import. TestClient wraps FastAPI app.

## Parametrize (Data-Driven Tests)

```python
@pytest.mark.parametrize("status,expected", [
    (200, "healthy"),
    (503, "degraded"),
    (500, "down"),
])
def test_health_status(client, status, expected):
    # Test multiple scenarios from single test function
    ...

@pytest.mark.parametrize("endpoint", [
    "/api/v1/anuncios/templates",
    "/api/v1/pesquisas/health",
    "/api/v1/cursos/templates",
])
def test_endpoints_require_auth(client, endpoint):
    resp = client.get(endpoint)
    assert resp.status_code == 401
```

## Markers (Test Categories)

```python
@pytest.mark.unit
def test_parse_input():
    """Fast, no external deps."""
    assert parse("hello") == {"text": "hello"}

@pytest.mark.integration
def test_supabase_connection():
    """Requires Supabase running."""
    ...

@pytest.mark.e2e
def test_full_pipeline(auth_client):
    """End-to-end: create → process → verify."""
    resp = auth_client.post("/api/v1/pipeline", json={...})
    assert resp.status_code == 200
    task_id = resp.json()["task_id"]
    # Poll until complete
    ...

@pytest.mark.slow
def test_large_batch():
    """Takes >30s, skip in CI with -m 'not slow'."""
    ...
```

**Run**: `pytest -m unit` (fast), `pytest -m "not slow"` (CI), `pytest` (all).

## Async Testing

```python
import pytest

@pytest.mark.asyncio
async def test_async_endpoint():
    from httpx import AsyncClient
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/health")
    assert resp.status_code == 200
```

Requires: `pytest-asyncio`. Config: `asyncio_mode = "auto"`.

## Coverage Config

```toml
[tool.coverage.run]
source = ["src/mypackage"]
branch = true
omit = ["*/__pycache__/*", "*/tests/*"]

[tool.coverage.report]
fail_under = 60
show_missing = true
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
    "raise NotImplementedError",
    "@abstractmethod",
]
```

**Run**: `pytest --cov=src/mypackage --cov-report=term-missing`

## Test Structure

```
tests/
├── conftest.py          # Shared fixtures
├── test_auth/           # Auth module tests
│   ├── conftest.py      # Auth-specific fixtures
│   ├── test_jwt.py
│   └── test_middleware.py
├── test_core/           # Business logic
├── e2e/                 # End-to-end
│   └── test_pipeline.py
└── test_utils.py        # Helper tests
```

## Anti-Patterns

- ❌ Importing app at module level without setting env vars first
- ❌ Tests that depend on execution order
- ❌ Mocking everything (test real behavior when possible)
- ❌ No markers — can't selectively run fast vs slow tests
- ❌ `coverage fail_under = 100` (unrealistic, causes test avoidance)
