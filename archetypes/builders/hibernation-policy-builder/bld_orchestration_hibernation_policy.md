---
kind: handoff
id: bld_collaboration_hibernation_policy
pillar: P12
llm_function: COLLABORATE
purpose: F8 signals and collaboration protocol for hibernation_policy
quality: 8.8
title: "Collaboration: hibernation_policy Builder"
version: "1.0.0"
author: n03_engineering
tags: [hibernation_policy, builder, collaboration]
tldr: "F8 signals and collaboration protocol for hibernation_policy"
domain: "hibernation_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - p03_ins_vector_store
  - p12_ho_admin_template
  - p11_qg_admin_orchestration
  - bld_collaboration_session_backend
  - agent_card_engineering_nucleus
  - p12_wf_create_orchestration_agent
  - bld_tools_session_backend
  - p02_agent_creation_nucleus
  - doctor
  - p04_ct_cex_compile
---

## F8 COLLABORATE Protocol

### 1. Save
Save to `environments/` directory alongside the sibling `terminal_backend` artifact.
Example paths: `environments/p09_hp_modal.yaml`, `environments/p09_hp_daytona.yaml`.

### 2. Compile
```bash
python _tools/cex_compile.py environments/p09_hp_BACKEND.yaml
# Or: python _tools/cex_compile.py --all
```
Replace `BACKEND` with the actual backend slug (modal, daytona, singularity, generic).

### 3. Validate
```bash
python _tools/cex_doctor.py
python -m json.tool .cex/kinds_meta.json > /dev/null && echo "JSON valid"
```

### 4. Commit
```bash
git add environments/p09_hp_BACKEND.yaml
git commit -m "[N05] hibernation_policy: p09_hp_BACKEND (TARGET_BACKEND idle guard)"
```

### 5. Signal
```python
from _tools.signal_writer import write_signal
write_signal('n05', 'complete', 9.0, mission='hibernation_policy_BACKEND')
```

## Downstream Consumers

| Consumer | How they use hibernation_policy |
|----------|--------------------------------|
| N07 Orchestrator | Reads wake_latency_sla_seconds to route latency-sensitive tasks to warm instances |
| N05 Operations | Deploys the policy to the backend API at environment setup |
| terminal_backend artifact | Sibling -- references same backend slug |
| cost_budget artifact | Complements -- budget caps total spend; hibernation reduces idle spend |

## Handoff to N07 (on build complete)
When a new hibernation_policy artifact is created, N07 should:
1. Verify the sibling terminal_backend artifact exists (same backend slug)
2. Update the cost model in the backend config to reflect the new savings estimate
3. Route latency-sensitive tasks away from backends with high wake_latency_sla_seconds

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_vector_store]] | upstream | 0.22 |
| [[p12_ho_admin_template]] | sibling | 0.22 |
| [[p11_qg_admin_orchestration]] | upstream | 0.21 |
| [[bld_collaboration_session_backend]] | related | 0.21 |
| [[agent_card_engineering_nucleus]] | upstream | 0.21 |
| [[p12_wf_create_orchestration_agent]] | related | 0.20 |
| [[bld_tools_session_backend]] | upstream | 0.20 |
| [[p02_agent_creation_nucleus]] | upstream | 0.20 |
| [[doctor]] | upstream | 0.20 |
| [[p04_ct_cex_compile]] | upstream | 0.20 |
