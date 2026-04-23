---
id: bld_sp_quality_gate_software_project
kind: quality_gate
pillar: P07
title: "Quality Gate — Software Project Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.1
tags: [builder, quality-gate, software-project, validation]
tldr: "8 hard gates for software projects: syntax valid, tests pass, lint clean, no secrets, Docker builds, CI valid, health endpoint exists, deps audited. Must pass all 8 for ≥8.0."
density_score: 1.0
llm_function: GOVERN
related:
  - bld_sp_schema_software_project
  - bld_sp_instruction_software_project
  - bld_sp_system_prompt_software_project
  - bld_sp_examples_software_project
  - bld_sp_knowledge_card_software_project
  - p04_tool_software_project
  - p04_ex_software_project_cli_tool
  - bld_sp_output_template_software_project
  - n04_qg_knowledge
  - p11_qg_artifact
---

## Quality Gate

# Quality Gates

This ISO describes a software project: its repository layout, modules, and build graph.

## 8 Hard Gates

| Gate | Check | Pass Criteria | Weight |
|------|-------|---------------|--------|
| **G1: Syntax** | `python -m py_compile` on all .py | 0 errors | BLOCK |
| **G2: Tests** | `pytest --collect-only` | ≥3 tests found | BLOCK |
| **G3: Lint** | `ruff check .` | 0 errors | BLOCK |
| **G4: Secrets** | Scan for API keys, passwords | 0 matches in non-test files | BLOCK |
| **G5: Docker** | Dockerfile has multi-stage + non-root | Both present | WARN |
| **G6: CI** | .github/workflows/ci.yml valid YAML | Parses without error | WARN |
| **G7: Health** | `/health` endpoint exists (API mode) | Returns 200 | WARN |
| **G8: Deps** | `pip-audit` on dependencies | 0 critical CVEs | WARN |

**BLOCK** = fails build, **WARN** = allows but flags

## Scoring Rubric

```
9.0-9.3: All 8 gates pass + rich tests + full CI/CD + security scanning
8.5-8.9: G1-G4 pass + Docker + CI present
8.0-8.4: G1-G4 pass (syntax, tests, lint, no secrets)
7.0-7.9: G1-G2 pass only (syntax valid, some tests)
<7.0:    Syntax errors or no tests → REJECT
```

## Gate Details

### G1: Syntax Validation

```bash
find src/ -name "*.py" -exec python -m py_compile {} \;
# Must return 0 for all files
```

### G2: Test Collection

```bash
pytest --collect-only tests/
# Must find ≥3 test items
# Must have conftest.py with ≥1 fixture
```

### G3: Lint

```bash
ruff check . --output-format=json
# Must return [] (empty issues list)
```

### G4: Secret Scanning

```python
PATTERNS = [
    r'password\s*=\s*["\'][^"\']+["\']',
    r'api_key\s*=\s*["\'][^"\']+["\']',
    r'sk-[a-zA-Z0-9]{20,}',
    r'ghp_[a-zA-Z0-9]{36}',
    r'-----BEGIN (RSA |EC )?PRIVATE KEY-----',
]
# Scan all files except tests/ and .env.example
```

### G5: Docker Validation

```python
def validate_dockerfile(content):
    checks = {
        "multi_stage": "AS builder" in content or "AS build" in content,
        "non_root": "USER " in content and "USER root" not in content,
        "healthcheck": "HEALTHCHECK" in content,
        "no_install_recommends": "--no-install-recommends" in content,
    }
    return all(checks.values())
```

### G6: CI Validation

```python
import yaml
with open(".github/workflows/ci.yml") as f:
    ci = yaml.safe_load(f)
assert "jobs" in ci
assert any(j for j in ci["jobs"] if "test" in j.lower() or "lint" in j.lower())
```

## Retry Policy

- If G1-G3 fail: retry implementation (max 2 attempts)
- If G4 fails: remove secrets, replace with env vars, retry
- If G5-G8 fail: flag as warnings, allow build to proceed
- After 2 retries: save as DRAFT with quality < 8.0

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish as exemplar |
| >= 8.0 | PUBLISH | Ready for runtime |
| >= 7.0 | REVIEW | Flag for review |
| < 7.0  | REJECT | Rework required |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental software-engineering artifact under active A/B testing |
| approver | Nucleus lead (written approval required) |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML parse), H05 (quality null) |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
