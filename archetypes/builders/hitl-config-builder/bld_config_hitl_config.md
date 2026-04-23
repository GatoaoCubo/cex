---
kind: config
id: bld_config_hitl_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Hitl Config"
version: "1.0.0"
author: n03_builder
tags: [hitl_config, builder, config, P09]
tldr: "Naming, paths, size limits, and enum constraints for hitl_config production: p11_hitl_{name}.yaml, body <= 3072B, approval_flow/fallback enums."
domain: "hitl_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_knowledge_card_hitl_config
  - bld_instruction_hitl_config
  - p10_lr_hitl_config_builder
  - bld_examples_hitl_config
  - bld_config_retriever_config
  - bld_config_output_validator
  - bld_config_memory_scope
  - p01_kc_hitl_config
  - bld_config_prompt_version
  - bld_config_hook_config
---
# Config: hitl_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p11_hitl_{name}.yaml` | `p11_hitl_marketing_copy_review.yaml` |
| Builder directory | kebab-case | `hitl-config-builder/` |
| Frontmatter fields | snake_case | `review_trigger`, `escalation_chain` |
| Name slug | snake_case, lowercase, no hyphens | `content_review`, `legal_approval`, `medical_triage` |
| Reviewer roles | snake_case | `content_reviewer`, `brand_lead`, `legal_counsel` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
1. Output: `P11_feedback/examples/p11_hitl_{name}.md`
2. Compiled: `P11_feedback/compiled/p11_hitl_{name}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 3072 bytes
2. Total (frontmatter + body): ~4200 bytes
3. Density: >= 0.85 (no filler)
## Enum Values (HARD constraints -- no other values accepted)
### approval_flow
| Value | Meaning | Best For |
|-------|---------|---------|
| binary | Reviewer chooses accept or reject only | High-throughput triage |
| edit | Reviewer modifies output before approving | Content generation |
| score | Reviewer assigns numeric rating (1-5) | Training data collection |
### fallback_action
| Value | Meaning | Use When |
|-------|---------|---------|
| reject | Output is discarded without human review | High-risk workflow (medical, legal, financial) |
| accept_with_flag | Output proceeds with audit flag attached | Medium-risk, pipeline continuity needed |
| retry | Model is re-run with different parameters | Model uncertainty triggered review (not domain requirement) |
## Escalation Chain Conventions
| Level | Role Convention | SLA Target |
|-------|----------------|-----------|
| L1 | generalist reviewer, fast response | 15-60 min async; 1-3 min real-time |
| L2 | domain expert, slower but accurate | 60-240 min async |
| L3 | senior/legal/admin, escalation only | as needed; reserved for critical |
## Timeout Sizing Reference
| Workflow Type | timeout_seconds | Justification |
|--------------|----------------|---------------|
| Real-time agent | 300 | User is waiting |
| Async content pipeline | 3600 | Business-hours SLA |
| Low-urgency batch | 86400 | Overnight batch |
| Regulatory compliance | 172800 | 48-hour review window |

## Metadata

```yaml
id: bld_config_hitl_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-hitl-config.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_hitl_config]] | upstream | 0.39 |
| [[bld_instruction_hitl_config]] | upstream | 0.38 |
| [[p10_lr_hitl_config_builder]] | downstream | 0.35 |
| [[bld_examples_hitl_config]] | upstream | 0.34 |
| [[bld_config_retriever_config]] | sibling | 0.33 |
| [[bld_config_output_validator]] | sibling | 0.32 |
| [[bld_config_memory_scope]] | sibling | 0.31 |
| [[p01_kc_hitl_config]] | downstream | 0.31 |
| [[bld_config_prompt_version]] | sibling | 0.31 |
| [[bld_config_hook_config]] | sibling | 0.29 |
