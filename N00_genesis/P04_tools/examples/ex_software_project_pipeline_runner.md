---
id: p04_ex_software_project_pipeline_runner
kind: example
pillar: P04
title: "Example — Pipeline Runner (Research Pipeline)"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [example, software-project, pipeline-runner, research, stages]
tldr: "Complete pipeline runner: Research pipeline with STORM+CRAG stages. Stage-based executor pattern (like CEX 8F), async stages, retry per stage, structured output, pytest with stage mocks."
density_score: 0.90
related:
  - bld_sp_examples_software_project
  - bld_sp_knowledge_card_software_project
  - p04_ex_software_project_cli_tool
  - bld_instruction_research_pipeline
  - p10_lr_e2e_eval_builder
  - p01_kc_research_pipeline
  - n01_tool_research_pipeline
  - p03_sp_research_pipeline_builder
  - p04_tpl_software_project
  - bld_collaboration_research_pipeline
---

# Example: Pipeline Runner — Research Pipeline

## Config

```yaml
project: { name: research-pipeline, version: 1.0.0, type: pipeline_runner, python: "3.12" }
package: { name: research_pipeline, cli_name: research }
dependencies:
  core: [pydantic>=2.0, httpx>=0.24, typer>=0.9, rich>=13.0, beautifulsoup4>=4.12]
  dev: [pytest>=7.0, pytest-asyncio>=0.21, ruff>=0.1.0, respx>=0.20]
deploy: { target: docker, port: 8000, workers: 1 }
config: { env_prefix: RESEARCH, settings: [llm_api_key, search_api_key, max_sources] }
```

## Key Files

**src/research_pipeline/cli.py**: Typer CLI with `run`, `status`, `export` commands.
**src/research_pipeline/pipeline.py**: Pipeline class with ordered stage list.
**src/research_pipeline/stages/**: IntentStage, PlanStage, RetrieveStage, ScoreStage, SynthesizeStage.
**src/research_pipeline/models.py**: Query, Source, Finding, Report Pydantic models.
**tests/conftest.py**: Mock HTTP responses, sample queries.
**tests/test_stages.py**: Per-stage tests with mocked external calls.

## Architecture

```
src/research_pipeline/
├── domain/
│   ├── models.py        # Query, Source, Finding, Report
│   ├── scoring.py       # Source scoring (7-dimension Gartner)
│   └── errors.py        # RetrievalError, ScoringError
├── stages/              # Pipeline stages (each is a class)
│   ├── base.py          # Stage ABC with execute(), retry(), rollback()
│   ├── intent.py        # Parse query → structured intent
│   ├── plan.py          # STORM: generate multi-perspective plan
│   ├── retrieve.py      # CRAG: fetch + assess + correct sources
│   ├── score.py         # Score sources on 7 dimensions
│   └── synthesize.py    # Graph-of-Thought synthesis
├── infra/
│   ├── http_client.py   # httpx with retry + circuit breaker
│   ├── llm_client.py    # LLM API wrapper
│   └── config.py        # BaseSettings
├── pipeline.py          # Pipeline orchestrator
└── cli.py               # Typer interface
```

## Stage Pattern

```python
class Stage(ABC):
    name: str
    max_retries: int = 2

    @abstractmethod
    async def execute(self, state: dict) -> StageResult: ...

    async def run(self, state: dict) -> StageResult:
        for attempt in range(self.max_retries + 1):
            try:
                return await self.execute(state)
            except RetryableError as e:
                if attempt == self.max_retries: raise
                await asyncio.sleep(2 ** attempt)
```

## What Makes It Good

- Stage pattern mirrors CEX 8F (familiar to N03)
- Each stage independently testable (mock execute())
- Retry with backoff per stage (not all-or-nothing)
- Structured output (Pydantic models, not raw dicts)
- CLI + API dual interface (Typer for CLI, FastAPI optional)
- Circuit breaker on HTTP client (prevents cascade failure)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_sp_examples_software_project]] | sibling | 0.43 |
| [[bld_sp_knowledge_card_software_project]] | upstream | 0.41 |
| [[p04_ex_software_project_cli_tool]] | sibling | 0.33 |
| [[bld_instruction_research_pipeline]] | upstream | 0.31 |
| [[p10_lr_e2e_eval_builder]] | downstream | 0.29 |
| [[p01_kc_research_pipeline]] | related | 0.28 |
| [[n01_tool_research_pipeline]] | related | 0.27 |
| [[p03_sp_research_pipeline_builder]] | upstream | 0.26 |
| [[p04_tpl_software_project]] | related | 0.25 |
| [[bld_collaboration_research_pipeline]] | downstream | 0.24 |
