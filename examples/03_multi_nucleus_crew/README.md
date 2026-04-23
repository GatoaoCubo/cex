# 03 -- Multi-Nucleus Crew

**Difficulty:** Intermediate

## What it does

Composes 3 nuclei into a sequential crew where each role depends on the
previous one's output:

1. **N01 (Intelligence)** -- research the domain
2. **N04 (Knowledge)** -- document findings as a knowledge_card
3. **N06 (Commercial)** -- create a pricing model from the research

This is the crew pattern: one coherent deliverable from N roles with handoffs.

## When to use crews vs. solo vs. grid

| Scenario | Use |
|----------|-----|
| 1 artifact, 1 kind | Solo builder |
| N independent artifacts in parallel | Grid dispatch |
| 1 coherent package, N roles with dependencies | **Crew** (this example) |

## Files

- `crew_template.md` -- the reusable crew recipe (roles + topology)
- `main.py` -- Python script that runs the crew via the SDK Workflow API

## How to run

```bash
# CLI approach (recommended):
python _tools/cex_crew.py show research_to_pricing
python _tools/cex_crew.py run research_to_pricing --charter <charter.md>

# SDK approach (this example):
python examples/03_multi_nucleus_crew/main.py
```

## Notes

The `main.py` uses `cex_sdk.workflow.Workflow` with 3 sequential steps,
each calling `CEXAgent.build()`. This is the SDK-native way to compose
multi-step pipelines. For production crews, use `cex_crew.py` which handles
handoff protocols, team charters, and signal coordination.
