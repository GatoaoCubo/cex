---
id: p06_is_orchestration_dispatch
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "input-schema-builder"
scope: "N07 orchestration dispatch — mission routing and nucleus coordination"
fields:
  - name: "mission"
    type: "string"
    required: true
    default: null
    description: "High-level goal or objective to orchestrate across nuclei"
    error_message: "mission is required — provide a goal string describing what to accomplish"
  - name: "nuclei"
    type: "list"
    required: true
    default: null
    description: "Ordered list of nucleus identifiers (n01–n07) to involve in execution"
    error_message: "nuclei is required — provide at least one nucleus identifier (e.g. [n03])"
  - name: "priority"
    type: "string"
    required: false
    default: "normal"
    description: "Execution priority: low | normal | high | urgent"
    error_message: null
  - name: "dependencies"
    type: "list"
    required: false
    default: []
    description: "Prerequisite task IDs or artifact paths that must complete before dispatch"
    error_message: null
  - name: "constraints"
    type: "object"
    required: false
    default: null
    description: "Execution constraints keyed by: max_parallel (integer), timeout_minutes (integer), allow_retry (boolean)"
    error_message: null
  - name: "decision_manifest_path"
    type: "string"
    required: false
    default: ".cex/runtime/decisions/decision_manifest.yaml"
    description: "Path to GDP decision manifest injected into every nucleus handoff file"
    error_message: null
  - name: "handoff_dir"
    type: "string"
    required: false
    default: ".cex/runtime/handoffs"
    description: "Directory where per-nucleus handoff .md files are written before dispatch"
    error_message: null
  - name: "signal_on_complete"
    type: "boolean"
    required: false
    default: true
    description: "Emit completion signal to .cex/runtime/signals/ when all nuclei finish"
    error_message: null
  - name: "dry_run"
    type: "boolean"
    required: false
    default: false
    description: "Simulate dispatch: writes handoffs but skips bash _spawn/dispatch.sh execution"
    error_message: null
coercion:
  - from: "string"
    to: "list"
    rule: "Single nucleus string (e.g. 'n03') coerced to ['n03'] for uniform list processing"
  - from: "string"
    to: "boolean"
    rule: "Literals 'true'/'false' (case-insensitive) coerced for dry_run and signal_on_complete"
  - from: "null"
    to: "list"
    rule: "Null dependencies coerced to [] before dependency resolution; never passed as null downstream"
examples:
  - mission: "Build brand knowledge card and system prompt"
    nuclei: ["n03"]
    priority: "high"
    dry_run: false
  - mission: "Full brand launch — research + copy + artifacts"
    nuclei: ["n01", "n02", "n03"]
    priority: "normal"
    dependencies: []
    constraints:
      max_parallel: 3
      timeout_minutes: 60
      allow_retry: true
    decision_manifest_path: ".cex/runtime/decisions/decision_manifest.yaml"
    handoff_dir: ".cex/runtime/handoffs"
    signal_on_complete: true
    dry_run: false
domain: "orchestration"
quality: 9.1
tags: [input-schema, orchestration, dispatch, n07, nuclei, mission, gdp]
tldr: "Input contract for N07 dispatch: requires mission string and nuclei list; optional priority, constraints, manifest path, dry-run, and signal flags."
keywords: [orchestration, dispatch, mission, nuclei, handoff, gdp, n07, parallel, signal, dry_run]
density_score: 0.91
related:
  - p08_ac_orchestrator
  - p03_sp_orchestration_nucleus
  - p01_kc_orchestration_best_practices
  - p12_wf_orchestration_pipeline
  - p01_ctx_cex_project
  - p03_pt_orchestration_task_dispatch
  - dispatch
  - ctx_cex_new_dev_guide
  - p02_agent_admin_orchestrator
  - p03_sp_admin_orchestrator
---
## Contract Definition

The N07 orchestration system receives dispatch requests from users and agents. Callers provide a mission goal and the target nuclei; N07 writes handoff files, injects the GDP decision manifest, and spawns nuclei via `bash _spawn/dispatch.sh`. Optional constraints govern parallelism and timeout. `dry_run: true` enables simulation without spawning processes.

## Fields

| # | Name | Type | Req | Default | Description |
|---|------|------|-----|---------|-------------|
| 1 | mission | string | YES | — | Goal string passed to every nucleus handoff |
| 2 | nuclei | list | YES | — | Nucleus IDs (n01–n07) to dispatch, in execution order |
| 3 | priority | string | NO | normal | low / normal / high / urgent |
| 4 | dependencies | list | NO | [] | Task IDs or artifact paths that must exist before dispatch |
| 5 | constraints | object | NO | null | max_parallel, timeout_minutes, allow_retry |
| 6 | decision_manifest_path | string | NO | .cex/runtime/decisions/decision_manifest.yaml | GDP manifest injected into handoffs |
| 7 | handoff_dir | string | NO | .cex/runtime/handoffs | Target directory for nucleus handoff files |
| 8 | signal_on_complete | boolean | NO | true | Emit signal when all nuclei finish |
| 9 | dry_run | boolean | NO | false | Write handoffs but skip dispatch.sh execution |

## Validation Rules

| Field | Rule |
|-------|------|
| mission | Non-empty string; max 512 chars |
| nuclei | list len >= 1; each item matches `^n0[1-7]$` |
| priority | enum: low, normal, high, urgent |
| constraints.max_parallel | integer 1–6 (matches CEX grid ceiling) |
| constraints.timeout_minutes | integer 1–480 |
| decision_manifest_path | Valid relative path; file must exist unless dry_run is true |

## Coercion Rules

| From | To | Rule |
|------|----|------|
| string | list | Single nucleus string → single-element list |
| string | boolean | 'true'/'false' (case-insensitive) → bool for dry_run, signal_on_complete |
| null | list | null dependencies → [] before dependency resolution |

## Examples

```json
{
  "mission": "Build brand knowledge card and system prompt",
  "nuclei": ["n03"],
  "priority": "high",
  "dry_run": false
}
```

```json
{
  "mission": "Full brand launch — research + copy + artifacts",
  "nuclei": ["n01", "n02", "n03"],
  "priority": "normal",
  "dependencies": [],
  "constraints": {"max_parallel": 3, "timeout_minutes": 60, "allow_retry": true},
  "decision_manifest_path": ".cex/runtime/decisions/decision_manifest.yaml",
  "signal_on_complete": true,
  "dry_run": false
}
```

## References

- N07 Orchestrator Rules: `.claude/rules/n07-orchestrator.md`
- GDP protocol: `.claude/rules/guided-decisions.md`
- Dispatch script: `_spawn/dispatch.sh`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_ac_orchestrator]] | downstream | 0.40 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.40 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.38 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.37 |
| [[p01_ctx_cex_project]] | upstream | 0.35 |
| [[p03_pt_orchestration_task_dispatch]] | upstream | 0.34 |
| [[dispatch]] | downstream | 0.31 |
| [[ctx_cex_new_dev_guide]] | related | 0.31 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.31 |
| [[p03_sp_admin_orchestrator]] | upstream | 0.31 |
