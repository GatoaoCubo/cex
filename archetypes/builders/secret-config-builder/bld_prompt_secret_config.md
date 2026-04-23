---
kind: instruction
id: bld_instruction_secret_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for secret_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Secret Config"
version: "1.0.0"
author: n03_builder
tags: [secret_config, builder, examples]
tldr: "Golden and anti-examples for secret config construction, demonstrating ideal structure and common pitfalls."
domain: "secret config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_memory_scope
  - bld_instruction_retriever_config
  - bld_instruction_chunk_strategy
  - bld_instruction_output_validator
  - bld_instruction_handoff_protocol
  - bld_instruction_search_tool
  - bld_instruction_prompt_version
  - bld_instruction_constraint_spec
  - bld_instruction_hook_config
  - bld_instruction_enum_def
---

# Instructions: How to Produce a secret_config
## Phase 1: RESEARCH
1. Identify what credentials this config governs (API keys, DB passwords, tokens, certificates, etc.)
2. Determine the provider: vault, k8s, aws, portkey, 1password, or sops — match to runtime platform
3. Define rotation_policy: frequency (daily/weekly/monthly/on-breach) and method (automatic/manual/triggered)
4. Determine access_pattern: dynamic (lease), static (deploy-time), injected (sidecar), or env (platform)
5. Map encryption posture: at_rest algorithm and in_transit protocol
6. List secret_paths as placeholder references — NEVER real values
7. Check for existing secret_config artifacts to avoid duplicates
8. Confirm slug for id: snake_case, lowercase, no hyphens, descriptive of what is governed
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Overview section: what credentials this governs, which system uses them, and risk level
5. Write Provider section: backend details, auth method, paths/ARNs as placeholders
6. Write Rotation Policy section: frequency, method, trigger condition, and rollback procedure
7. Write Access Pattern section: exactly how agents/services retrieve the secret at runtime
8. Include lease_duration if provider supports TTL-based leases
9. Set audit_log: true unless there is an explicit documented reason not to
10. Verify body <= 1024 bytes
11. Verify id matches `^p09_sec_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p09_sec_` prefix pattern
4. Confirm kind == secret_config
5. Confirm provider is one of the allowed enum values
6. Confirm rotation_policy has both frequency and method
7. Confirm encryption has both at_rest and in_transit
8. Confirm access_pattern is one of: dynamic, static, injected, env
9. Confirm NO actual secrets appear anywhere in the file — scan for patterns like live tokens, passwords, or keys
10. HARD gates: frontmatter valid, id pattern matches, required fields present, no plaintext secrets
11. SOFT gates: score against QUALITY_GATES.md
12. Cross-check: is this a SECRET (sensitive credential with rotation)? Not a generic env var (env_config)? Not an access rule (permission)? Not a toggle (feature_flag)?
13. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify secret
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | secret config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_memory_scope]] | sibling | 0.51 |
| [[bld_instruction_retriever_config]] | sibling | 0.51 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.51 |
| [[bld_instruction_output_validator]] | sibling | 0.50 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.49 |
| [[bld_instruction_search_tool]] | sibling | 0.48 |
| [[bld_instruction_prompt_version]] | sibling | 0.48 |
| [[bld_instruction_constraint_spec]] | sibling | 0.48 |
| [[bld_instruction_hook_config]] | sibling | 0.45 |
| [[bld_instruction_enum_def]] | sibling | 0.45 |
