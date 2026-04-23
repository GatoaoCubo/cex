---
id: skill_n05
kind: skill
nucleus: n05
pillar: P04
mirrors: N00_genesis/P04_tools/layers/p04_skill_simplify.md
overrides:
  tone: strict, deterministic, gate-heavy
  voice: imperative, risk-averse
  sin_lens: IRA
  required_fields:
    - sla_target
    - failure_mode
    - rollback_procedure
  quality_threshold: 9.3
  density_target: 0.90
  example_corpus: 3+ examples with failure modes section
title: "N05 Operations -- Skill (Monitoring, Alerting, Runbook)"
version: 1.0.0
quality: 8.2
tags: [mirror, n05, operations, hermes_assimilation, skill]
tldr: "N05 ops skills: monitoring, alerting, runbook execution, incident triage -- auto-generated from repeated tool patterns."
auto_generated_from: null
self_improves: true
agentskills_catalog_category: operations
related:
  - bld_collaboration_skill
  - bld_architecture_skill
  - bld_memory_skill
  - bld_knowledge_card_procedural_memory
  - bld_system_prompt_skill
  - procedural-memory-builder
  - p01_kc_skill
  - skill-builder
  - p03_ins_skill_builder
  - p11_qg_skill
---

## Ops Skill Catalog

N05 maintains operational skills: monitoring, alerting, runbook execution, and
incident response. Skills are auto-captured when a tool pattern repeats 5+ times
with success (HERMES DP7 threshold).

### Active Skills

| Skill | Trigger | Tool Chain | SLA | Failure Mode |
|-------|---------|-----------|-----|--------------|
| process_cleanup | orphan detected | Get-Process + taskkill /T | 5min | alert oncall |
| health_check | schedule (30s) | HTTP GET /health | 2s response | circuit breaker |
| log_rotation | disk >80% | compress + archive + delete old | 15min | alert |
| credential_rotation | token age >75d | vault rotate + update config | 24h | block + alert |
| deploy_gate | pre-merge | cex_doctor + cex_system_test | 15min | block merge |
| incident_triage | error spike >2x | collect logs + classify + route | 10min | escalate to user |
| signal_monitor | continuous | read .cex/runtime/signals/ | 60s poll | log gap |

### Skill Auto-Generation (HERMES)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Tool call threshold | 5 | Minimum repetitions before skill candidate |
| Require success | true | Only successful completions count |
| Self-improves | true | Skill refines itself based on execution feedback |
| Catalog category | operations | agentskills_catalog_category for discovery |
| Auto-generated marker | null (manual) | Set to tool_pattern_id when auto-created |

### Skill Execution Protocol

| Step | Action | Gate |
|------|--------|------|
| 1 | Detect trigger condition | trigger valid |
| 2 | Load skill definition + tool chain | tools available |
| 3 | Execute tool chain in sequence | each tool succeeds |
| 4 | Validate result against expected outcome | outcome matches |
| 5 | Log execution to audit trail | audit written |
| 6 | Update skill metrics (success rate, avg duration) | metrics updated |

### Failure Modes

| Failure | Detection | Response | Escalation |
|---------|-----------|----------|------------|
| Tool not found | import error / path missing | skip + alert | N05 oncall |
| Tool timeout | execution >2x SLA | kill + retry 1x | alert |
| Unexpected output | validation mismatch | log + skip | review queue |
| Permission denied | OS error | alert immediately | user |
| Cascading failure | >3 skills fail in 5min | pause all skills | N07 + user |

### Monitoring

| Metric | Threshold | Alert |
|--------|-----------|-------|
| Skill execution success rate | >95% | warn at 90%, page at 80% |
| Avg execution time vs SLA | <100% SLA | warn at 80% SLA |
| Auto-generated candidates | >0 pending | weekly review prompt |
| Failed skill count (24h) | <3 | alert at 3, page at 5 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_skill]] | downstream | 0.37 |
| [[bld_architecture_skill]] | downstream | 0.35 |
| [[bld_memory_skill]] | downstream | 0.33 |
| [[bld_knowledge_card_procedural_memory]] | upstream | 0.31 |
| [[bld_system_prompt_skill]] | upstream | 0.31 |
| [[procedural-memory-builder]] | downstream | 0.30 |
| [[p01_kc_skill]] | related | 0.30 |
| [[skill-builder]] | related | 0.29 |
| [[p03_ins_skill_builder]] | upstream | 0.29 |
| [[p11_qg_skill]] | downstream | 0.27 |
