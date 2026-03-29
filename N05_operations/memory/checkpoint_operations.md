---

```yaml
id: p12_ck_operations_nucleus_step_analysis
kind: checkpoint
pillar: P12
version: "1.0.0"
created: "2023-10-01"
updated: "2023-10-01"
author: "checkpoint-builder"
name: "Operations Nucleus — Step Analysis Checkpoint"
workflow_ref: "op_nucleus_workflow"
step: "step_analysis"
quality: null
tags: [checkpoint, operations, nucleus]
tldr: "Checkpoint at the step analysis stage within the Operations workflow."
description: "Captures the state of step analysis in the Operations workflow for resume capability."
state:
  analysis_data: byte array # approx 256 bytes
  analysis_status: string # very small, max 10 bytes
resumable: true
ttl: "24h"
parent_checkpoint: "p12_ck_operations_nucleus_previous_step"
retry_count: 0
error: null
```

## Overview
This checkpoint captures the state during the step analysis in the Operations workflow, enabling resumption without reprocessing completed analyses. This stage is critical to ensure that the operation's analysis can continue smoothly in the event of a pause or failure.

## State
| Key           | Type        | Size           | Description                             |
|---------------|-------------|----------------|-----------------------------------------|
| analysis_data | byte array  | approx 256 bytes| Contains processed data up to this point|
| analysis_status| string     | max 10 bytes   | Status of analysis, e.g., "completed"   |

Serialization format: yaml
Total state budget: approx 266 bytes (max 2048)

## Resume
Prerequisites:
- All external data sources accessible
- Valid authentication to access necessary systems

Resume steps:
1. Load checkpoint by id: `p12_ck_operations_nucleus_step_analysis`
2. Restore state keys: analysis_data, analysis_status
3. Re-enter workflow at step: `step_analysis`
4. Validate state integrity: Ensure `analysis_status` is "completed" before proceeding

Idempotent: yes — if already completed state is detected, reinstate only for data consistency.

## Lifecycle
TTL: 24h — Suitable for batch processing in operations; checkpoint prevents unnecessary repeat processing within the day.
Cleanup: auto_delete after TTL expiry
Archival: Standard operational archival policy applies
Chain: p12_ck_operations_nucleus_previous_step -> this -> p12_ck_operations_nucleus_next_step

---