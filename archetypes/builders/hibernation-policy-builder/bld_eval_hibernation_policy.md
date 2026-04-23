---
kind: quality_gate
id: bld_quality_gate_hibernation_policy
pillar: P07
llm_function: GOVERN
purpose: F7 GOVERN quality gates for hibernation_policy
quality: 8.8
title: "Quality Gate: hibernation_policy"
version: "1.0.0"
author: n03_engineering
tags: [hibernation_policy, builder, quality_gate]
tldr: "F7 GOVERN quality gates for hibernation_policy"
domain: "hibernation_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_quality_gate_memory_type
  - p11_qg_quality_gate
  - p11_qg_runtime_state
  - bld_collaboration_multi_modal_config
  - p05_qg_github_issue_template
  - bld_tools_multi_modal_config
  - p11_qg_type_def
  - bld_knowledge_card_quality_gate
  - p11_qg_kind_builder
  - p11_qg_function_def
---

## Quality Gate
## hibernation_policy HARD Gates (must all pass -- H01-H05)
| Gate | Check | Fail action |
|------|-------|------------|
| H01 | Frontmatter present with all required fields | Reject -- missing fields |
| H02 | `target_backend` in {daytona, modal, singularity, generic} | Reject -- invalid backend |
| H03 | `idle_trigger.type` in {no_activity_seconds, no_requests_seconds, explicit_signal} | Reject -- invalid trigger type |
| H04 | `idle_trigger.threshold_seconds` >= 0 | Reject -- negative threshold |
| H05 | `wake_on` list has at least one condition | Reject -- nothing to wake on |

## SOFT Gates (scored 0-10, target >= 8.0)
| Dimension | Weight | Check |
|-----------|--------|-------|
| D1 Structural | 30% | 6+ sections present; all tables populated; no empty cells |
| D2 Correctness | 30% | threshold_seconds reasonable for backend type; state_persistence consistent with backend capabilities |
| D3 Completeness | 20% | wake_latency_sla_seconds set; cost_savings_estimate_pct populated; Notes section present |
| D4 Density | 10% | density >= 0.85; no padding prose; tables > narrative |
| D5 Boundary | 10% | Does not conflate with cost_budget, rate_limit_config, terminal_backend, or runtime_rule |

## Scoring Formula
```
soft_score = (D1*0.30 + D2*0.30 + D3*0.20 + D4*0.10 + D5*0.10) * 10
final = min(soft_score, 10.0)
publish_threshold = 8.0
quality_target = 9.0
```

## Common Failure Patterns
| Pattern | Gate failed | Fix |
|---------|-------------|-----|
| `threshold_seconds: -1` | H04 | Set to 0 for explicit_signal or >= 60 for time-based |
| `wake_on: []` | H05 | Add at least incoming_request or explicit_signal |
| Missing idle_trigger block | H01 | Add both type and threshold_seconds |
| `target_backend: kubernetes` | H02 | Use generic for unsupported backends |
| `cost_budget` field in frontmatter | Semantic | Remove -- cost_budget is a separate kind |

## Examples
## Example 1: Modal GPU serverless (5-minute idle)
**Intent:** Configure Modal serverless container to scale-to-zero after 5 minutes of no requests.

```yaml
---
id: p09_hp_modal
kind: hibernation_policy
pillar: P09
title: "Hibernation Policy: modal"
target_backend: modal
idle_trigger:
  type: no_requests_seconds
  threshold_seconds: 300
wake_on:
  - incoming_request
  - scheduled_cron
state_persistence:
  keep_memory: false
  snapshot_disk: false
  checkpoint_cadence_seconds: null
wake_latency_sla_seconds: 5
cost_savings_estimate_pct: 85
version: 1.0.0
quality: null
tags: [hermes_origin, hibernation, serverless, cost, modal]
---

## Policy Overview
**Target backend:** modal
**Purpose:** Scale-to-zero after 5 minutes of idle to eliminate GPU idle cost
**Nucleus owner:** N05 Operations

## Idle Trigger
| Field | Value |
|-------|-------|
| Trigger type | no_requests_seconds |
| Threshold | 300s |

## Wake Conditions
| Condition | Description |
|-----------|-------------|
| `incoming_request` | Any inbound HTTP request wakes the container |
| `scheduled_cron` | 8am pre-warm ensures warm instance at peak hours |

## State Persistence
| Setting | Value | Description |
|---------|-------|-------------|
| keep_memory | false | Ephemeral; re-initialized on wake |
| snapshot_disk | false | No filesystem persistence needed |
| checkpoint_cadence_seconds | null | No checkpoints |

## SLA
| Metric | Value | Notes |
|--------|-------|-------|
| Wake latency SLA | 5s | Modal cold-start is typically 2-4s for this image |
| Cost savings estimate | 85% | GPU idle eliminated outside active request windows |

## Notes
- Pair with `terminal_backend` (p09_tb_modal) for complete execution config
- `scheduled_cron` pre-warm prevents cold starts during business hours
```

---

## Example 2: Daytona long-running agent workspace (30-minute idle)
**Intent:** Configure Daytona workspace to hibernate after 30 minutes of agent inactivity, preserving full filesystem state.

```yaml
---
id: p09_hp_daytona
kind: hibernation_policy
pillar: P09
title: "Hibernation Policy: daytona"
target_backend: daytona
idle_trigger:
  type: no_activity_seconds
  threshold_seconds: 1800
wake_on:
  - incoming_request
  - explicit_signal
state_persistence:
  keep_memory: true
  snapshot_disk: true
  checkpoint_cadence_seconds: 60
wake_latency_sla_seconds: 10
cost_savings_estimate_pct: 70
version: 1.0.0
quality: null
tags: [hermes_origin, hibernation, serverless, cost, daytona]
---

## Policy Overview
**Target backend:** daytona
**Purpose:** Pause workspace after 30 minutes of agent inactivity; resume with full state intact
**Nucleus owner:** N05 Operations

## Idle Trigger
| Field | Value |
|-------|-------|
| Trigger type | no_activity_seconds |
| Threshold | 1800s |

## State Persistence
| Setting | Value | Description |
|---------|-------|-------------|
| keep_memory | true | Agent in-process state preserved via workspace snapshot |
| snapshot_disk | true | Full filesystem checkpointed to Daytona storage |
| checkpoint_cadence_seconds | 60 | Periodic 60-second checkpoints while active |

## Notes
- 60-second checkpoints protect against data loss if the platform terminates before idle trigger fires
- wake_latency_sla_seconds=10 enables N07 to route interactive tasks to this workspace
```

---

## Example 3: Singularity HPC batch (explicit signal)
**Intent:** Configure Singularity job to hibernate only on explicit orchestrator signal after batch completion.

```yaml
---
id: p09_hp_singularity
kind: hibernation_policy
pillar: P09
title: "Hibernation Policy: singularity"
target_backend: singularity
idle_trigger:
  type: explicit_signal
  threshold_seconds: 0
wake_on:
  - explicit_signal
  - scheduled_cron
state_persistence:
  keep_memory: false
  snapshot_disk: true
  checkpoint_cadence_seconds: 300
wake_latency_sla_seconds: 60
cost_savings_estimate_pct: 60
version: 1.0.0
quality: null
tags: [hermes_origin, hibernation, hpc, cost, singularity]
---

## Policy Overview
**Target backend:** singularity
**Purpose:** SLURM job suspend triggered by N07 after batch wave completion
**Nucleus owner:** N05 Operations

## Notes
- `explicit_signal` means only N07 can hibernate this job -- no auto-sleep during a running batch
- checkpoint_cadence_seconds=300 provides 5-minute interval checkpoints for long jobs
- wake_latency_sla_seconds=60 reflects SLURM job resume overhead; not suitable for interactive tasks
```

---

## Example 4: Generic fallback policy
**Intent:** Abstract policy for backends that resolve at runtime.

```yaml
---
id: p09_hp_generic
kind: hibernation_policy
pillar: P09
title: "Hibernation Policy: generic"
target_backend: generic
idle_trigger:
  type: no_activity_seconds
  threshold_seconds: 900
wake_on:
  - incoming_request
  - explicit_signal
state_persistence:
  keep_memory: true
  snapshot_disk: false
  checkpoint_cadence_seconds: null
wake_latency_sla_seconds: 30
cost_savings_estimate_pct: 70
version: 1.0.0
quality: null
tags: [hermes_origin, hibernation, serverless, cost]
---
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
