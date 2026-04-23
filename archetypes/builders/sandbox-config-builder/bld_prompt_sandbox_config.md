---
kind: instruction
id: bld_instruction_sandbox_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for sandbox_config
quality: 8.9
title: "Instruction Sandbox Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [sandbox_config, builder, instruction]
tldr: "Step-by-step production process for sandbox_config"
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_sandbox_config
  - bld_knowledge_card_sandbox_config
  - bld_output_template_sandbox_config
  - p09_qg_sandbox_config
  - n05_audit_hybrid_review2
  - bld_tools_sandbox_config
  - p10_lr_code_executor_builder
  - bld_instruction_code_executor
  - bld_knowledge_card_code_executor
  - p03_ins_path_config
---

## Phase 1: RESEARCH
1. Identify platform: E2B (Firecracker microVM), Modal (container), Daytona (devcontainer),
   Docker (runc), Firecracker (direct), nsjail (namespace), gVisor (runsc user-space kernel).
2. Determine required resource limits: CPU (cores/millicores), RAM (MB), disk quota (MB),
   execution timeout (seconds), max PID count.
3. Define network policy: air-gapped (none), egress whitelist, or controlled bridge.
4. Define filesystem scope: root path, read-only root flag, ephemeral scratch size and path.
5. Select isolation mechanism: seccomp profile (default/custom/none), AppArmor/SELinux profile,
   Linux capabilities to drop and add, no_new_privs enforcement.
6. Review seccomp default profile (moby/moby) for syscall allowlist baseline.
7. Document threat model for the execution context (untrusted LLM-generated code vs. CI build).

## Phase 2: COMPOSE
1. Select platform and runtime (E2B SDK, Docker + gVisor, nsjail, Firecracker direct).
2. Define resource limits section: cpu, memory_mb, disk_mb, timeout_seconds (ALL four required).
3. Configure network policy section: mode, egress, allowed_hosts, allowed_ports, dns.
4. Configure filesystem scope: read_only_root, scratch_dir, scratch_size_mb, bind mounts.
5. Configure isolation section: runtime, namespaces, seccomp_profile, capabilities.drop=ALL.
6. Add audit logging: log_destination, log_retention_days.
7. Write platform-specific config block (E2B e2b.toml, Docker run flags, nsjail.cfg).
8. Write config file using OUTPUT_TEMPLATE.md syntax.
9. Validate against SCHEMA.md (all required fields present, ID pattern matches).

## Phase 3: VALIDATE
- [ ] All four resource limits defined: cpu, memory_mb, disk_mb, timeout_seconds
- [ ] Network policy explicitly set (not default/unspecified)
- [ ] Filesystem scope: read_only_root and scratch_dir defined
- [ ] Isolation: seccomp_profile or AppArmor specified (not "none" unless documented exception)
- [ ] capabilities.drop includes ALL (or explicit drop list)
- [ ] no_new_privs: true set
- [ ] H01-H08 HARD gates pass (schema, pattern, limits, network, filesystem, seccomp, no-privileged)
- [ ] SOFT score >= 8.0 before publish


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_sandbox_config]] | downstream | 0.52 |
| [[bld_knowledge_card_sandbox_config]] | upstream | 0.46 |
| [[bld_output_template_sandbox_config]] | downstream | 0.46 |
| [[p09_qg_sandbox_config]] | downstream | 0.40 |
| [[n05_audit_hybrid_review2]] | downstream | 0.31 |
| [[bld_tools_sandbox_config]] | downstream | 0.30 |
| [[p10_lr_code_executor_builder]] | downstream | 0.25 |
| [[bld_instruction_code_executor]] | sibling | 0.25 |
| [[bld_knowledge_card_code_executor]] | upstream | 0.24 |
| [[p03_ins_path_config]] | sibling | 0.22 |
