---
kind: output_template
id: bld_output_template_hibernation_policy
pillar: P05
llm_function: PRODUCE
purpose: P05 output shape for hibernation_policy
quality: 8.6
title: "Output Template: hibernation_policy"
version: "1.0.0"
author: n03_engineering
tags: [hibernation_policy, builder, output_template]
tldr: "P05 output shape for hibernation_policy"
domain: "hibernation_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_instruction_memory_scope
  - bld_instruction_golden_test
  - p03_ins_vector_store
  - bld_instruction_session_backend
  - bld_instruction_input_schema
  - p11_qg_runtime_state
  - bld_instruction_handoff_protocol
  - bld_knowledge_card_response_format
  - bld_collaboration_session_backend
  - p11_qg_session_backend
---

## Output Shape

Every hibernation_policy artifact MUST follow this structure:

### Section 1: Frontmatter (required)
```yaml
---
id: p09_hp_{{backend}}
kind: hibernation_policy
pillar: P09
title: "Hibernation Policy: {{backend}}"
target_backend: {{target_backend}}
idle_trigger:
  type: {{trigger_type}}
  threshold_seconds: {{threshold}}
wake_on:
  - {{condition_1}}
  [- {{condition_2}}]
state_persistence:
  keep_memory: {{bool}}
  snapshot_disk: {{bool}}
  checkpoint_cadence_seconds: {{int|null}}
wake_latency_sla_seconds: {{int}}
cost_savings_estimate_pct: {{int|null}}
version: 1.0.0
quality: null
tags: [hermes_origin, hibernation, serverless, cost]
---
```

### Section 2: Policy Overview (required)
```markdown
## Policy Overview

**Target backend:** {{target_backend}}
**Purpose:** {{one-line description}}
**Nucleus owner:** N05 Operations
```

### Section 3: Idle Trigger Table (required)
```markdown
## Idle Trigger

| Field | Value |
|-------|-------|
| Trigger type | {{idle_trigger.type}} |
| Threshold | {{idle_trigger.threshold_seconds}}s |
```

### Section 4: Wake Conditions Table (required)
```markdown
## Wake Conditions

| Condition | Description |
|-----------|-------------|
| `{{condition}}` | {{description}} |
```

### Section 5: State Persistence Table (required)
```markdown
## State Persistence

| Setting | Value | Description |
|---------|-------|-------------|
| keep_memory | {{bool}} | {{rationale}} |
| snapshot_disk | {{bool}} | {{rationale}} |
| checkpoint_cadence_seconds | {{value}} | {{rationale}} |
```

### Section 6: SLA Table (required)
```markdown
## SLA

| Metric | Value | Notes |
|--------|-------|-------|
| Wake latency SLA | {{wake_latency_sla_seconds}}s | {{notes}} |
| Cost savings estimate | {{cost_savings_estimate_pct}}% | {{notes}} |
```

### Section 7: Notes (required)
```markdown
## Notes

- Pair with `terminal_backend` (p09_tb_{{backend}}) for complete execution config
- {{backend-specific note}}
```

## Density Target
Minimum 5 sections. All tables populated. Frontmatter complete. Target density >= 0.85.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_memory_scope]] | upstream | 0.21 |
| [[bld_instruction_golden_test]] | upstream | 0.21 |
| [[p03_ins_vector_store]] | upstream | 0.19 |
| [[bld_instruction_session_backend]] | upstream | 0.19 |
| [[bld_instruction_input_schema]] | upstream | 0.18 |
| [[p11_qg_runtime_state]] | downstream | 0.17 |
| [[bld_instruction_handoff_protocol]] | upstream | 0.17 |
| [[bld_knowledge_card_response_format]] | related | 0.17 |
| [[bld_collaboration_session_backend]] | downstream | 0.17 |
| [[p11_qg_session_backend]] | downstream | 0.17 |
