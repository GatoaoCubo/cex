---
quality: 8.4
quality: 7.9
kind: instruction
id: bld_instruction_terminal_backend
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for terminal_backend
title: "Instruction Terminal Backend"
version: "1.0.0"
author: n03_engineering
tags: [terminal_backend, builder, instruction]
tldr: "Step-by-step production process for terminal_backend"
domain: "terminal_backend construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - p03_ins_vector_store
  - bld_instruction_input_schema
  - bld_collaboration_multi_modal_config
  - bld_instruction_sandbox_config
  - p03_ins_mcp_server
  - bld_tools_multi_modal_config
  - bld_instruction_client
  - bld_instruction_memory_scope
  - bld_instruction_instruction
  - p03_ins_model_card
---

## Phase 1: RESEARCH
1. Identify the target backend: local | docker | ssh | daytona | modal | singularity.
2. Determine auth requirements: none (local/docker), ssh_key, api_token (daytona/modal), or oauth.
3. Gather resource constraints: cpu_cores (null=provider default), memory_gb, timeout_seconds (required).
4. Determine billing model: free (local), per_second (modal), per_task (daytona), subscription (ssh cluster).
5. Check whether backend is serverless (modal, daytona) or persistent (local, docker, ssh, singularity).
6. Check hibernation capability: daytona supports hibernation; most others do not.
7. Identify any related artifacts: secret_config for auth.secret_ref, sandbox_config for isolation layer.

## Phase 2: COMPOSE
1. Write frontmatter block with all required fields from schema.
2. Set `backend_type` to one of: local, docker, ssh, daytona, modal, singularity.
3. Set `serverless` and `hibernation_capable` booleans.
4. Populate `auth` block: method + optional secret_ref.
5. Populate `limits` block: cpu_cores (null if provider default), memory_gb (null if unlimited), timeout_seconds (required).
6. Populate `cost_model` block: billing enum + estimated_usd_per_hour (null if free or unknown).
7. Write backend-specific connection section in body (host/port for ssh, image for docker, app_name for modal, etc.).
8. Add resource limits table and cost model table in body.
9. Add pairing note: link to sandbox_config if security isolation is required.

## Phase 3: VALIDATE
- [ ] `backend_type` is one of the 6 supported values
- [ ] `auth.method` is one of: none, ssh_key, api_token, oauth
- [ ] `limits.timeout_seconds` is set (required; cannot be null)
- [ ] `cost_model.billing` is one of: free, per_second, per_task, subscription
- [ ] If auth.method != none: `auth.secret_ref` points to a valid secret_config id
- [ ] `serverless: true` only for modal and daytona backends
- [ ] `hibernation_capable: true` only for daytona (current HERMES support)
- [ ] ID matches naming pattern: `p09_tb_{{backend}}`
- [ ] H01-H05 HARD gates pass
- [ ] SOFT score >= 8.0 before publish


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_vector_store]] | sibling | 0.20 |
| [[bld_instruction_input_schema]] | sibling | 0.20 |
| [[bld_collaboration_multi_modal_config]] | downstream | 0.19 |
| [[bld_instruction_sandbox_config]] | sibling | 0.19 |
| [[p03_ins_mcp_server]] | sibling | 0.18 |
| [[bld_tools_multi_modal_config]] | downstream | 0.18 |
| [[bld_instruction_client]] | sibling | 0.18 |
| [[bld_instruction_memory_scope]] | sibling | 0.18 |
| [[bld_instruction_instruction]] | sibling | 0.18 |
| [[p03_ins_model_card]] | sibling | 0.17 |
