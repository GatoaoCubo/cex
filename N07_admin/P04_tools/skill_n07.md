---
id: skill_n07
kind: skill
nucleus: n07
pillar: P04
mirrors: N00_genesis/P04_tools/templates/tpl_skill.md
overrides:
  tone: terse, dispatch-oriented, meta
  voice: imperative orchestrator
  sin_lens: PREGUICA ORQUESTRADORA
  required_fields:
    - target_nucleus
    - expected_deliverables
    - do_not_list
  quality_threshold: 9.2
  density_target: 0.90
  example_corpus: 3+ examples with full do-not lists
version: 1.0.0
quality: 8.5
tags: [mirror, n07, orchestration, skill, hermes_assimilation]
tldr: "N07 orchestration skills: dispatch, monitor, consolidate, wave-plan, GDP-collect"
created: "2026-04-18"
updated: "2026-04-18"
author: n07_admin
related:
  - p01_kc_orchestration_best_practices
  - p03_sp_orchestration_nucleus
  - p03_sp_admin_orchestrator
  - dispatch
  - p02_agent_admin_orchestrator
  - p08_ac_orchestrator
  - p01_kc_orchestration
  - agent_card_n07
  - p12_wf_admin_orchestration
  - ctx_cex_new_dev_guide
density_score: 1.0
---

## Override Rationale

N07's skills are orchestration primitives: dispatch, monitor, consolidate.
Where N03's skills are build tools and N05's are ops runbooks, N07's skills
coordinate other nuclei without touching artifacts directly.

## Skill Registry (N07)

| Skill | Trigger | Input | Output | Tool Chain |
|-------|---------|-------|--------|------------|
| dispatch | `/dispatch`, `/grid`, `/mission` | intent + nucleus | handoff file + PID | dispatch.sh + signal_writer |
| monitor | wave active | PID file | status report | dispatch.sh status + git log |
| consolidate | wave complete | signal files | consolidation report | cex_doctor.py + taskkill |
| wave_plan | `/plan`, `/mission` | user goal | plan.md with waves | cex_mission.py |
| gdp_collect | `/guide`, subjective task | decision points | decision_manifest.yaml | cex_gdp.py |
| intent_resolve | any user input | natural language | {kind, pillar, nucleus, verb} | cex_intent_resolver.py |

## Skill: dispatch

```yaml
name: dispatch
trigger: "/dispatch <nucleus> <task>"
steps:
  1. Resolve intent via prompt_compiler
  2. Write handoff to .cex/runtime/handoffs/
  3. Copy to n0X_task.md
  4. Run: bash _spawn/dispatch.sh solo <nucleus>
  5. Record PID to spawn_pids.txt
output: "Dispatched N0X. PID: {{pid}}. Monitor: dispatch.sh status"
```

## Skill: monitor

```yaml
name: monitor
trigger: wave_active (automatic)
steps:
  1. Check: git log --oneline --since="3 minutes ago"
  2. Check: bash _spawn/dispatch.sh status
  3. Check: ls .cex/runtime/signals/signal_*
  4. Report: "{{completed}}/{{total}} nuclei signaled"
interval: 60-90 seconds
```

## Skill: consolidate

```yaml
name: consolidate
trigger: all_wave_nuclei_signaled
steps:
  1. Verify: all deliverables exist on disk
  2. Run: python _tools/cex_doctor.py
  3. Stop: bash _spawn/dispatch.sh stop
  4. Commit: git add + commit (gemini nuclei only)
  5. Archive: move signals to .cex/runtime/archive/
  6. Report: consolidation summary
output: "W{{n}} consolidated. {{files}} files, {{quality}} avg quality."
```

## Skill: intent_resolve

```yaml
name: intent_resolve
trigger: every user input (F1 CONSTRAIN)
steps:
  1. Run: python _tools/cex_intent_resolver.py "{{input}}"
  2. If confidence >= 60%: proceed with resolved tuple
  3. If confidence < 60%: present top-3 via GDP
output: "{kind: X, pillar: PXX, nucleus: N0X, verb: Y}"
```

## DO NOT

- Build artifacts (dispatch to N03)
- Run tests (dispatch to N05)
- Write copy (dispatch to N02)
- Research topics (dispatch to N01)

## Links

- N03 engineering sibling: [[N03_engineering/P04_tools/skill_n03.md]]
- N05 operations sibling: [[N05_operations/P04_tools/skill_n05.md]]
- Dispatch script: [[_spawn/dispatch.sh]]
- Intent resolver: [[_tools/cex_intent_resolver.py]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_orchestration_best_practices]] | upstream | 0.50 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.50 |
| [[p03_sp_admin_orchestrator]] | upstream | 0.50 |
| [[dispatch]] | downstream | 0.47 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.44 |
| [[p08_ac_orchestrator]] | downstream | 0.42 |
| [[p01_kc_orchestration]] | upstream | 0.41 |
| [[agent_card_n07]] | downstream | 0.41 |
| [[p12_wf_admin_orchestration]] | downstream | 0.40 |
| [[ctx_cex_new_dev_guide]] | related | 0.38 |
