---
quality: 8.6
quality: 8.3
id: p04_sdk_cex_hello_world
name: CEX SDK Hello World
description: Minimal working example that builds a knowledge_card artifact via cex_sdk using CEXAgent and Claude. Demonstrates the 3-line path from intent to artifact path.
pillar: P04
category: sdk_example
tags: [sdk_example, cex_sdk, hello_world, P04, getting_started]
kind: sdk_example
version: "1.0.0"
created: "2026-04-19"
updated: "2026-04-19"
author: "n03_engineering"
tldr: "3-line hello world: CEXAgent + Claude -> build(intent) -> artifact_path. Shows minimal cex_sdk usage for contributors."
related:
  - spec_infinite_bootstrap_loop
  - self_audit_n03_builder_20260408
  - p06_is_builder_nucleus
  - p08_pat_builder_construction
  - bld_knowledge_card_nucleus_def
  - p06_if_builder_nucleus
  - p02_nd_n03.md
  - p02_agent_creation_nucleus
  - quality_gate_intent_resolution
  - bld_architecture_kind
density_score: 1.0
---

# SDK Example: CEX Hello World

The minimal working example for `cex_sdk` v10.2.0.
Builds a `knowledge_card` artifact from a natural-language intent using `CEXAgent`.
Intended for contributors following CONTRIBUTING.md Path 1 (New Builder) to
verify their environment before building builders.

## Prerequisites

```bash
git clone https://github.com/your-org/cex
cd cex
pip install -e ".[dev]"
python _tools/cex_doctor.py   # must show 0 FAIL
```

## Example Usage

```python
from cex_sdk import CEXAgent, Claude

# 1. Initialize agent bound to a nucleus and model
agent = CEXAgent(
    model=Claude("claude-sonnet-4-6"),
    nucleus="n04",                      # Knowledge nucleus for knowledge_card
    kind="knowledge_card",              # Override resolved kind (optional)
)

# 2. Build artifact from intent -- runs full 8F pipeline internally
result = agent.build(intent="document the 8F pipeline reasoning protocol")

# 3. Inspect result
print(result.artifact_path)    # e.g., N04_knowledge/P01_knowledge/kc_8f_pipeline.md
print(result.score)            # None until peer review scores it
print(result.kind)             # knowledge_card
print(result.pillar)           # P01
```

## Async Version

```python
import asyncio
from cex_sdk import CEXAgent, Claude

async def build_async():
    agent = CEXAgent(model=Claude("claude-sonnet-4-6"), nucleus="n03")
    result = await agent.abuild(intent="create a state machine for 8F pipeline")
    return result.artifact_path

path = asyncio.run(build_async())
print(path)
```

## With Explicit Kind and Pillar

```python
from cex_sdk import CEXAgent, Claude

agent = CEXAgent(model=Claude("claude-sonnet-4-6"), nucleus="n03")

result = agent.build(
    intent="model the artifact domain entity",
    kind="aggregate_root",
    pillar="P06",
)

print(result.artifact_path)   # N03_engineering/P06_schema/aggregate_root_*.md
```

## Parameter Table

| Name | Type | Default | Description |
|------|------|---------|-------------|
| model | Model | required | LLM provider instance (e.g., Claude("claude-sonnet-4-6")) |
| nucleus | str | "n03" | Target nucleus ID: n01-n07 |
| kind | str | None | Force-override resolved kind; if None, resolved via intent transmutation |
| pillar | str | None | Force-override pillar; if None, derived from kind |

| Name | Type | Description |
|------|------|-------------|
| intent | str | Natural language or structured build intent |

## Sample Response

```json
{
  "artifact_path": "N04_knowledge/P01_knowledge/kc_8f_pipeline.md",
  "kind": "knowledge_card",
  "pillar": "P01",
  "score": null,
  "compiled": true,
  "committed": true,
  "signal_written": true,
  "bytes": 3840,
  "sections": 6
}
```

## References

- CEXAgent source: `cex_sdk/agent/`
- Claude provider: `cex_sdk/models/providers/anthropic.py`
- Build pipeline: `_tools/cex_8f_runner.py` (called internally by CEXAgent.build())
- Artifact aggregate root: `N03_engineering/P06_schema/aggregate_root_artifact.md`
- Full SDK reference: `N03_engineering/P06_schema/openapi_spec_cex_sdk.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_infinite_bootstrap_loop]] | related | 0.31 |
| [[self_audit_n03_builder_20260408]] | upstream | 0.30 |
| [[p06_is_builder_nucleus]] | downstream | 0.29 |
| [[p08_pat_builder_construction]] | downstream | 0.26 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.26 |
| [[p06_if_builder_nucleus]] | downstream | 0.24 |
| [[p02_nd_n03.md]] | upstream | 0.23 |
| [[p02_agent_creation_nucleus]] | upstream | 0.23 |
| [[quality_gate_intent_resolution]] | downstream | 0.23 |
| [[bld_architecture_kind]] | downstream | 0.23 |
