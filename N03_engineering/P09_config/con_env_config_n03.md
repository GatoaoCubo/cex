---
id: con_env_config_n03
kind: env_config
pillar: P09
nucleus: n03
title: Engineering Environment Config
version: 1.0
quality: 9.0
tags: [config, env, engineering, runtime, n03]
density_score: 1.0
related:
  - bld_schema_env_config
  - schema_prompt_template_builder
  - p03_sp_env_config_builder
  - bld_schema_validation_schema
  - ex_env_config_default
  - bld_schema_enum_def
  - bld_schema_model_registry
  - p06_is_orchestration_dispatch
  - bld_schema_sandbox_config
  - bld_schema_dataset_card
---


<!-- 8F: F1 constrain=P09/env_config F2 become=env-config-builder F3 inject=nucleus_def_n03, agent_engineering, kc_env_config, P09_config, boot_config example
     F4 reason=environment variable catalog for disciplined N03 execution F5 call=rg, Get-Content, apply_patch F6 produce=5093 bytes
     F7 govern=frontmatter+sections+tables+ascii+self-check F8 collaborate=save N03_engineering/P09_config/con_env_config_n03.md -->

# Engineering Environment Config

## Purpose

| Field | Value |
|-------|-------|
| Mission fit | Runtime environment catalog for N03 builder execution and artifact governance |
| Pride lens | Variables are named for clarity, bounded by validation, and stripped of ambiguity |
| Primary use | Standardize N03 local, CI, and mission-run execution without leaking secrets |
| Boundary | Environment values only; secret contents live in `secret_config` |
| Precedence | `runtime env > mission override > repo default > documented fallback` |
| Failure prevented | Hidden machine-specific behavior and vague execution defaults |

## Values

| Variable | Required | Type | Default | Scope | Rule |
|----------|----------|------|---------|-------|------|
| `CEX_ROOT` | yes | path string | auto-detect | all | Must resolve to repo root |
| `CEX_NUCLEUS` | yes | string | `n03` | all | Must equal current nucleus |
| `CEX_MODEL` | no | string | `gpt-5-codex` | local, CI | Explicit override for build model |
| `CEX_QUALITY_MIN` | no | float string | `9.0` | all | Must be `>= 8.0` |
| `CEX_MAX_RETRIES` | no | integer string | `2` | all | `0-3` only |
| `CEX_AUTO_COMPILE` | no | boolean string | `true` | all | Must be `true` for mission runs |
| `CEX_AUTO_INDEX` | no | boolean string | `false` | local, CI | Allowed to be disabled for speed |
| `CEX_STRICT_ASCII` | no | boolean string | `true` | all | Guards executable-code hygiene |
| `CEX_HANDOFF_FILE` | no | path string | `n03_task.md` | mission | Must point to existing task file |
| `CEX_SIGNAL_ON_COMPLETE` | no | boolean string | `true` | mission | Can be disabled only for dry runs |
| `CEX_DRY_RUN` | no | boolean string | `false` | local | Must never be `true` in mission closeout |
| `CEX_TRACE_LEVEL` | no | string | `standard` | all | Enum: `minimal`, `standard`, `verbose` |

## Validation Rules

| Rule ID | Statement | Why it matters |
|---------|-----------|----------------|
| `E01` | `CEX_ROOT` must contain `archetypes/` and `N03_engineering/` | Repo identity cannot be guessed loosely |
| `E02` | `CEX_NUCLEUS` must be `n03` | Cross-nucleus contamination is avoidable |
| `E03` | `CEX_QUALITY_MIN` below `9.0` is permitted only for ad hoc local exploration | Mission-grade work stays proud |
| `E04` | `CEX_AUTO_COMPILE=true` for production-like execution | Config without compilation is half-finished work |
| `E05` | Any secret-bearing variable name must be registered in `con_secret_config_n03.md` | Environment and secret governance stay aligned |
| `E06` | Boolean strings are lowercase ASCII `true` or `false` | No shell-specific ambiguity |

## Rationale

| Design choice | Why it exists | Pride expression |
|---------------|---------------|------------------|
| Narrow variable set | Better to govern twelve variables well than fifty vaguely | Sharpness over clutter |
| Explicit mission file variable | Handoffs are first-class inputs, not hidden assumptions | Respect the operating model |
| `CEX_STRICT_ASCII` flag | The repo already treats text hygiene seriously | Small discipline protects big systems |
| Conservative retry cap | Repair should happen in authored revisions, not infinite loops | Control beats flailing |
| Default compile on | N03 owns artifacts that others consume | Finish the job |
| Trace level enum | Observability should be deliberate, not ad hoc log noise | Elegance includes restraint |

## Example

```env
CEX_ROOT=C:/Users/CEX/Documents/GitHub/cex
CEX_NUCLEUS=n03
CEX_MODEL=gpt-5-codex
CEX_QUALITY_MIN=9.0
CEX_MAX_RETRIES=2
CEX_AUTO_COMPILE=true
CEX_AUTO_INDEX=false
CEX_STRICT_ASCII=true
CEX_HANDOFF_FILE=n03_task.md
CEX_SIGNAL_ON_COMPLETE=true
CEX_DRY_RUN=false
CEX_TRACE_LEVEL=standard
```

## Operating Notes

| Environment | Expected overrides | Guardrail |
|-------------|--------------------|-----------|
| local authoring | May set `CEX_TRACE_LEVEL=verbose` | Must not lower `CEX_STRICT_ASCII` |
| CI validation | Forces `CEX_AUTO_COMPILE=true` | Rejects missing `CEX_ROOT` |
| orchestrated mission | Uses explicit `CEX_HANDOFF_FILE` | Requires `CEX_SIGNAL_ON_COMPLETE=true` |
| exploratory debug | May set `CEX_DRY_RUN=true` | Output cannot be treated as mission-complete |

## Properties

| Property | Value |
|----------|-------|
| Nucleus | `n03` |
| Pillar | `P09` |
| Kind | `env_config` |
| Variables | `12` |
| Secret-bearing values stored here | `0` |
| Precedence model | `env > mission > default` |
| Validation rules | `6` |
| Lens | `Inventive Pride` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_env_config]] | upstream | 0.32 |
| [[schema_prompt_template_builder]] | upstream | 0.32 |
| [[p03_sp_env_config_builder]] | upstream | 0.28 |
| [[bld_schema_validation_schema]] | upstream | 0.28 |
| [[ex_env_config_default]] | sibling | 0.28 |
| [[bld_schema_enum_def]] | upstream | 0.27 |
| [[bld_schema_model_registry]] | upstream | 0.27 |
| [[p06_is_orchestration_dispatch]] | upstream | 0.27 |
| [[bld_schema_sandbox_config]] | upstream | 0.27 |
| [[bld_schema_dataset_card]] | upstream | 0.27 |
