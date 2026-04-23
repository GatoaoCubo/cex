---
id: bld_sp_memory_software_project
kind: memory
pillar: P10
title: "Memory — Software Project Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [builder, memory, software-project, learnings]
tldr: "Learnings from codexa-core (145K lines): CORS must be outermost middleware, env vars before imports, multi-stage Docker cuts 600MB, pytest markers save CI time, Railway rollback is instant."
density_score: 0.89
memory_scope: project
observation_types: [user, feedback, project, reference]
llm_function: INJECT
related:
  - p03_ins_pattern
  - p11_qg_pattern
  - p01_kc_fastapi_patterns
  - p10_mem_pitch_deck_builder
  - pattern-builder
  - bld_collaboration_pattern
  - bld_sp_system_prompt_software_project
  - p03_sp_pattern_builder
  - bld_schema_pattern
  - bld_instruction_pitch_deck
---
# Memory — Learnings

This ISO describes a software project: its repository layout, modules, and build graph.

## From codexa-core (Production)

### L01: CORS Middleware Must Be Outermost
**Problem**: Auth middleware returned 401/403 but browser blocked response (no CORS headers).
**Solution**: Add CORSMiddleware LAST (FastAPI processes last-added first).
**Impact**: All error responses now include CORS headers.

### L02: Environment Variables Before App Import
**Problem**: Tests importing app before setting env vars caused config errors.
**Solution**: Set `os.environ["ENV"] = "test"` BEFORE `from api.main import app`.
**Impact**: Consistent test behavior, no env pollution.

### L03: Multi-Stage Docker Saves 600MB
**Problem**: Single-stage image was 800MB+ (includes gcc, build tools).
**Solution**: Builder stage installs deps → Runtime stage copies only venv.
**Impact**: 200MB runtime image, faster deploys, smaller attack surface.

### L04: pytest Markers Save 80% CI Time
**Problem**: Full test suite took 5min, blocking PRs.
**Solution**: Mark slow/integration tests, run `pytest -m "not slow"` in CI.
**Impact**: PR checks complete in 60s. Full suite runs nightly.

### L05: Railway Rollback Is Instant
**Problem**: Bad deploy broke production, manual fix took 20min.
**Solution**: `railway rollback` reverts to previous build in <30s.
**Impact**: Zero-downtime recovery for deploy failures.

### L06: Hatchling Build Is Fastest
**Problem**: setuptools build took 15s, required setup.py.
**Solution**: Switch to hatchling (pure Python, no C compilation).
**Impact**: Build in <2s, single pyproject.toml config.

### L07: Body Size Limit Prevents OOM
**Problem**: Large POST payloads caused API worker to OOM crash.
**Solution**: Middleware checks Content-Length before processing.
**Impact**: 413 response for >5MB payloads, no more OOM.

### L08: Structured Logging with Request IDs
**Problem**: Couldn't trace errors across middleware→handler→service.
**Solution**: ContextVar-based request_id in every log line.
**Impact**: Full request tracing with `grep request_id` in logs.

## From CEX Tools Development

### L09: `_clean_llm_output()` Is Essential
**Problem**: LLM returned markdown with ```yaml blocks, breaking parsing.
**Solution**: Strip everything before first `---` in 8F runner.
**Impact**: 100% reliable artifact production.

### L10: Score Normalization Prevents Inflation
**Problem**: First scorer gave everything 9.5+.
**Solution**: Normalized to 8.0-9.3 range with 5D heuristics.
**Impact**: Meaningful quality differentiation.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_pattern]] | upstream | 0.26 |
| [[p11_qg_pattern]] | downstream | 0.21 |
| [[p01_kc_fastapi_patterns]] | upstream | 0.20 |
| [[p10_mem_pitch_deck_builder]] | sibling | 0.20 |
| [[pattern-builder]] | upstream | 0.20 |
| [[bld_collaboration_pattern]] | upstream | 0.20 |
| [[bld_sp_system_prompt_software_project]] | upstream | 0.19 |
| [[p03_sp_pattern_builder]] | upstream | 0.19 |
| [[bld_schema_pattern]] | upstream | 0.19 |
| [[bld_instruction_pitch_deck]] | upstream | 0.19 |
