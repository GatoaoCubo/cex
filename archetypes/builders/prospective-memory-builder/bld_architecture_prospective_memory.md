---
kind: architecture
id: bld_architecture_prospective_memory
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of prospective_memory
quality: 8.0
title: "Architecture Prospective Memory"
version: "1.0.0"
author: n03_builder
tags: [prospective_memory, builder, architecture]
tldr: "prospective_memory stores future-directed agent intentions, distinct from P12 schedule (workflow config)."
domain: "prospective memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - schedule-builder
  - bld_architecture_schedule
  - p01_kc_schedule
  - bld_collaboration_schedule
  - bld_knowledge_card_schedule
  - bld_architecture_visual_workflow
  - bld_examples_schedule
  - schedule
  - bld_schema_schedule
  - bld_architecture_session_state
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| reminders | Future action intents with triggers | prospective_memory | required |
| owner | Agent/nucleus executing reminders | prospective_memory | required |
| execution_mechanism | How reminders are polled/fired | prospective_memory | required |
| trigger_type | time, event, or condition trigger | reminder | required |
| action_payload | What to do when triggered | reminder | required |
| schedule | P12 workflow orchestration config -- sibling | P12 | sibling |
| session_state | Current session data -- sibling | P10 | sibling |
| episodic_memory | Records of past actions -- sibling | P10 | sibling |

## Boundary Table
| prospective_memory IS | prospective_memory IS NOT |
|-----------------------|--------------------------|
| Agent's future intentions (deferred actions) | Workflow schedule config (that is schedule P12) |
| Memory of what to do later | Memory of what happened (that is episodic_memory) |
| Agent-internal reminder store | Cron job or orchestration primitive |
| Trigger-conditional future actions | Current active task state (that is working_memory) |

## Trigger Type Comparison
| Type | Example | Mechanism |
|------|---------|-----------|
| time | "Check quality scores at 2026-05-01" | datetime or cron |
| event | "After N01 signals complete, do X" | signal polling |
| condition | "When quality_score < 7.0, retrain" | state polling |

## Architecture Checklist

- Verify component inventory is complete (no orphans)
- Validate dependency graph has no cycles
- Cross-reference with boundary table for scope correctness
- Test layer map against actual codebase structure

## Architecture Pattern

```yaml
# Architecture validation
components: inventoried
dependencies: acyclic
boundaries: defined
layers: mapped
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope architecture
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[schedule-builder]] | downstream | 0.25 |
| [[bld_architecture_schedule]] | sibling | 0.23 |
| [[p01_kc_schedule]] | downstream | 0.23 |
| [[bld_collaboration_schedule]] | downstream | 0.23 |
| [[bld_knowledge_card_schedule]] | upstream | 0.20 |
| [[bld_architecture_visual_workflow]] | sibling | 0.20 |
| [[bld_examples_schedule]] | upstream | 0.20 |
| [[schedule]] | downstream | 0.19 |
| [[bld_schema_schedule]] | upstream | 0.19 |
| [[bld_architecture_session_state]] | sibling | 0.19 |
