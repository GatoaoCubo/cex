---
id: p04_ex_software_project_cli_tool
kind: example
pillar: P04
title: "Example — CLI Tool (CEX Scorer)"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [example, software-project, cli-tool, typer, scoring]
tldr: "Complete CLI tool project: CEX artifact scorer with Typer+Rich. Shows pyproject.toml, src layout, Pydantic models, pytest fixtures, Ruff config, Dockerfile, GitHub Actions CI."
density_score: 0.90
---

# Example: CLI Tool — CEX Scorer

## Config

```yaml
project: { name: cex-scorer, version: 1.0.0, type: cli_tool, python: "3.12" }
package: { name: cex_scorer, cli_name: cex-score }
dependencies:
  core: [pydantic>=2.0, typer>=0.9, rich>=13.0, pyyaml>=6.0]
  dev: [pytest>=7.0, pytest-cov>=4.0, ruff>=0.1.0]
deploy: { target: none }
config: { env_prefix: SCORER }
```

## Key Files

**pyproject.toml**: Hatchling build, Typer entry point, Ruff+pytest config.
**src/cex_scorer/cli.py**: Typer CLI with `score`, `batch`, `report` commands.
**src/cex_scorer/scorer.py**: 5D scoring logic (size, frontmatter, sections, density, domain).
**src/cex_scorer/models.py**: `ScoreResult(BaseModel)` with score, notes, dimensions.
**tests/conftest.py**: Fixtures for sample artifacts (valid, invalid, empty).
**tests/test_scorer.py**: 12 parametrized tests covering all 5 dimensions.

## Architecture

```
src/cex_scorer/
├── cli.py          # Interface (Typer commands)
├── scorer.py       # Domain (scoring logic, zero deps)
├── models.py       # Domain (Pydantic data models)
└── config.py       # Infra (BaseSettings)
tests/
├── conftest.py     # Fixtures (sample artifacts via tmp_path)
└── test_scorer.py  # Unit tests (parametrized per dimension)
```

## What Makes It Good

- Clear separation: CLI → domain logic → models
- Parametrized tests cover all scoring dimensions
- Rich console output for terminal users
- `--json` flag for programmatic usage
- Zero external service deps (works offline)

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `example`
- **Artifact ID**: `p04_ex_software_project_cli_tool`
- **Tags**: [example, software-project, cli-tool, typer, scoring]

## Example Registry

| Aspect | Detail |
|--------|--------|
| Purpose | Few-shot exemplar for builder prompts |
| Injection | Loaded by `cex_skill_loader.py` at F3 |
| Quality | Must score 9.0+ to serve as exemplar |
