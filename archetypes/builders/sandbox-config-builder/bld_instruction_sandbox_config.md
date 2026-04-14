---
kind: instruction
id: bld_instruction_sandbox_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for sandbox_config
quality: null
title: "Instruction Sandbox Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [sandbox_config, builder, instruction]
tldr: "Step-by-step production process for sandbox_config"
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify execution constraints (e.g., CPU, memory, I/O limits).  
2. Research isolation mechanisms (containers, VMs, kernel namespaces).  
3. Analyze security models (SELinux, AppArmor, seccomp policies).  
4. Review existing sandbox_config schemas for compatibility.  
5. Evaluate compliance with Pillar P09 (isolation rigor).  
6. Document threat models for code execution risks.  

## Phase 2: COMPOSE  
1. Set base image (e.g., alpine, ubuntu minimal).  
2. Define sandbox constraints in SCHEMA.md (version, isolation level).  
3. Specify resource limits (CPU cores, memory caps, timeout thresholds).  
4. Configure network isolation (firewall rules, no external access).  
5. Embed security policies (seccomp, cgroup restrictions).  
6. Integrate logging and monitoring hooks (auditd, syscalls tracing).  
7. Write config file using OUTPUT_TEMPLATE.md syntax.  
8. Validate against SCHEMA.md using JSON schema tools.  
9. Test config in staging environment with sample payloads.  

## Phase 3: VALIDATE  
- [ ] ✅ Schema compliance (jsonschema validation).  
- [ ] ✅ Isolation boundaries (no host filesystem access).  
- [ ] ✅ Resource limits enforced (CPU/memory caps).  
- [ ] ✅ Security policies applied (seccomp/cgroup checks).  
- [ ] ✅ Pillar P09 constraints met (no code escape paths).
