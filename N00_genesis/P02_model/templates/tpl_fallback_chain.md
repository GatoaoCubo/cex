---
id: p02_fb_CHAIN_SLUG
kind: fallback_chain
8f: F8_collaborate
pillar: P02
version: 1.0.0
title: "Template — Fallback Chain"
tags: [template, fallback, resilience, retry, chain]
tldr: "Ordered list of strategies from strongest to most resilient. Each step has a trigger condition, timeout, and abort criteria. Ensures graceful degradation."
chain: ["[STEP_1]", "[STEP_2]", "[STEP_3]"]
timeout_per_step: 30
quality: 9.0
domain: "model configuration"
density_score: 0.84
author: "n03_builder"
created: "2026-04-07"
updated: "2026-04-07"
related:
  - p03_ch_{{PIPELINE_SLUG}}
  - p10_lr_chain_builder
  - p11_qg_chain
  - bld_architecture_chain
  - p01_kc_chain
  - p10_lr_fallback_chain_builder
  - bld_instruction_chain
  - bld_instruction_fallback_chain
  - bld_memory_workflow
  - tpl_instruction
---

# Fallback Chain: [CHAIN_SLUG]

## Chain Definition
Order: strongest → most resilient. Each step tries before falling to the next.

| Priority | Step | When to Use | Fallback Trigger |
|----------|------|-------------|------------------|
| 1 | [STEP_1] | [DEFAULT_PATH — best quality] | [TIMEOUT \| ERROR_CODE \| QUALITY_BELOW_X] |
| 2 | [STEP_2] | [Step 1 failed] | [TIMEOUT \| RATE_LIMIT \| 5xx] |
| 3 | [STEP_3] | [Steps 1+2 failed — last resort] | [NEVER — this is the floor] |

## Timing
- **Timeout per step**: [SECONDS]s
- **Total chain timeout**: [SECONDS * STEPS]s
- **Backoff**: [none | linear | exponential]
- **Jitter**: [0-500ms] — prevents thundering herd

## Abort Conditions
Abort the entire chain (do NOT continue to next step) when:
- [CONDITION_1 — e.g., authentication failure (won't succeed on retry)]
- [CONDITION_2 — e.g., invalid input (not a transient error)]
- [CONDITION_3 — e.g., budget exhausted]

## Logging & Observability
```yaml
log_fields:
  chain_id: "[CHAIN_SLUG]"
  step_index: [0-N]
  step_name: "[STEP_NAME]"
  duration_ms: [elapsed]
  outcome: [success | fallback | abort]
  error_type: "[ERROR_CLASS]"
```

## Recovery
After a fallback triggers:
- **Alert**: [log_warn | notify_slack | page_oncall]
- **Circuit breaker**: After [N] failures in [M]min, skip directly to step [X]
- **Recovery probe**: Check step 1 health every [INTERVAL]

## Quality Gate
- [ ] ≥ 2 steps in chain (1 step = no fallback)
- [ ] Last step never fails (static response, cached value, or graceful error)
- [ ] Abort conditions defined (prevent infinite retry)
- [ ] Logging captures step transitions

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ch_{{PIPELINE_SLUG}}]] | downstream | 0.49 |
| [[p10_lr_chain_builder]] | downstream | 0.47 |
| [[p11_qg_chain]] | downstream | 0.45 |
| [[bld_architecture_chain]] | downstream | 0.44 |
| [[p01_kc_chain]] | downstream | 0.42 |
| [[p10_lr_fallback_chain_builder]] | downstream | 0.42 |
| [[bld_instruction_chain]] | downstream | 0.41 |
| [[bld_instruction_fallback_chain]] | downstream | 0.40 |
| [[bld_memory_workflow]] | downstream | 0.38 |
| [[tpl_instruction]] | downstream | 0.37 |
