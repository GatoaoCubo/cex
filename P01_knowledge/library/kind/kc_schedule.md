---
id: p01_kc_schedule
kind: knowledge_card
type: kind
pillar: P12
title: "Schedule — Deep Knowledge for schedule"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: schedule
quality: 9.1
tags: [schedule, P12, GOVERN, kind-kc]
tldr: "Temporal trigger specification (cron or interval) that initiates a workflow or agent_group task at defined times"
when_to_use: "Building, reviewing, or reasoning about schedule artifacts"
keywords: [cron, trigger, temporal]
feeds_kinds: [schedule]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
---

# Schedule

## Spec
```yaml
kind: schedule
pillar: P12
llm_function: GOVERN
max_bytes: 1024
naming: p12_sched.md
core: false
```

## What It Is
A schedule defines WHEN a workflow or agent_group task runs — via cron expression, interval, or event-based trigger. It is a temporal governance artifact, not a routing artifact. It is NOT dispatch_rule (P12 — decides WHERE to route based on intent; schedule decides WHEN to trigger regardless of intent).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | External scheduler (APScheduler, Celery Beat) | No native scheduling; wrap chain in APScheduler job |
| LlamaIndex | External scheduler or `IngestionPipeline` refresh | Schedule periodic re-ingestion with cron |
| CrewAI | External cron + crew kickoff | Schedule `crew.kickoff()` via cron or task queue |
| DSPy | External scheduler triggering program run | No native scheduling; wrap dspy.Module in cron job |
| Haystack | External pipeline trigger (Airflow, cron) | No native scheduling; integrate with Airflow DAG |
| OpenAI | Scheduled function calls via external cron | No native scheduling; use cloud functions + cron |
| Anthropic | External cron triggering API calls | No native scheduling; AWS EventBridge or similar |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| cron | string | required | Standard 5-field cron; use cron validator before deploying |
| target | string | required | workflow/agent_group/handoff to trigger |
| timezone | string | UTC | Always explicit; avoid ambiguous local time |
| enabled | bool | true | Toggle without deleting; enables safe pause |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Daily research trigger | Recurring market research | `cron: 0 8 * * 1-5` → target: research agent research handoff |
| Freshness-check schedule | Knowledge base maintenance | `cron: 0 2 * * 0` (weekly) → trigger lifecycle_rule evaluation |
| Retry schedule | Failed task recovery | `cron: */30 * * * *` (every 30min) → check signal queue for failures |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No timezone specified | Schedule runs at unexpected time on server | Always set timezone: UTC or explicit IANA timezone |
| Overlapping schedule intervals | Previous run still active when next triggers | Set min interval > expected task duration + buffer |
| Hardcoded cron in multiple files | One change needs multiple file edits | Single p12_sched.md per schedule; reference by id |

## Integration Graph
```
[lifecycle_rule] --> [schedule] --> [workflow]
                          |    --> [handoff]
                     [dag]
```

## Decision Tree
- IF trigger is time-based THEN use cron field
- IF trigger is interval-based THEN use interval_minutes field
- IF timezone is ambiguous THEN default to UTC
- DEFAULT: enabled: true; always set timezone; document expected duration

## Quality Criteria
- GOOD: Has cron, target, timezone, enabled flag; YAML parseable; under 1024 bytes
- GREAT: Expected duration documented; overlap prevention noted; pause/resume via enabled flag
- FAIL: No timezone; cron not validated; target undefined; schedule never tested
