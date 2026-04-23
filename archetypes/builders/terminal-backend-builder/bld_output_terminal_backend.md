---
quality: 8.2
quality: 7.8
kind: output_template
id: bld_output_template_terminal_backend
pillar: P05
llm_function: PRODUCE
purpose: Output shape and structure for terminal_backend artifacts
title: "Output Template Terminal Backend"
version: "1.0.0"
author: n03_engineering
tags: [terminal_backend, builder, output_template]
tldr: "Standard output shape for terminal_backend: frontmatter + backend overview + connection + limits + cost"
domain: "terminal_backend construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - p03_ins_vector_store
  - p11_qg_session_backend
  - bld_collaboration_session_backend
  - bld_schema_vector_store
  - bld_instruction_session_backend
  - bld_schema_session_backend
  - bld_config_session_backend
  - p03_sp_session_backend_builder
  - bld_tools_session_backend
  - bld_instruction_memory_scope
---

## Output Shape

Every terminal_backend artifact MUST follow this structure:

```
---
[FRONTMATTER: all required fields from schema]
---

## Backend Overview
[1-2 sentences: type, purpose, nucleus owner]

## Connection
[Backend-specific YAML or table]

## Resource Limits
| Resource | Limit | Unit |
|----------|-------|------|
...

## Authentication
| Field | Value |
|-------|-------|
...

## Cost Model
| Field | Value |
|-------|-------|
...

## Notes
[Optional: pairing recommendations, warnings, limitations]
```

## Frontmatter Completeness Checklist
- [ ] id matches `p09_tb_{{backend}}`
- [ ] kind = "terminal_backend"
- [ ] pillar = "P09"
- [ ] title includes backend name
- [ ] backend_type is one of 6 supported values
- [ ] serverless is a boolean
- [ ] hibernation_capable is a boolean
- [ ] auth.method is set
- [ ] limits.timeout_seconds is a positive integer (not null)
- [ ] cost_model.billing is one of 4 billing types
- [ ] quality = null (peer-review assigns)
- [ ] tags includes "hermes_origin", "backend", "runtime"

## Body Completeness Checklist
- [ ] Backend Overview section present
- [ ] Connection section with backend-specific config
- [ ] Resource Limits table with at least timeout_seconds
- [ ] Authentication table showing method and secret_ref
- [ ] Cost Model table showing billing and estimated rate
- [ ] Notes section present if backend has pairing restrictions or hibernation policy

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_vector_store]] | upstream | 0.34 |
| [[p11_qg_session_backend]] | downstream | 0.29 |
| [[bld_collaboration_session_backend]] | downstream | 0.26 |
| [[bld_schema_vector_store]] | downstream | 0.25 |
| [[bld_instruction_session_backend]] | upstream | 0.25 |
| [[bld_schema_session_backend]] | downstream | 0.24 |
| [[bld_config_session_backend]] | downstream | 0.24 |
| [[p03_sp_session_backend_builder]] | upstream | 0.24 |
| [[bld_tools_session_backend]] | upstream | 0.24 |
| [[bld_instruction_memory_scope]] | upstream | 0.23 |
