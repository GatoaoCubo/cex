---
kind: instruction
id: bld_instruction_marketplace_app_manifest
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for marketplace_app_manifest
quality: 8.9
title: "Instruction Marketplace App Manifest"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [marketplace_app_manifest, builder, instruction]
tldr: "Step-by-step production process for marketplace_app_manifest"
domain: "marketplace_app_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Analyze existing Claude/LangChain/HuggingFace app manifests for metadata structure.  
2. Identify required metadata fields: name, version, provider, description, tags.  
3. Map platform-specific permission models (API keys, IAM roles, token-based).  
4. Define pricing tiers: free, tiered, pay-as-you-go, subscription.  
5. Review compliance constraints: data residency, encryption, audit logs.  
6. Document schema dependencies from SCHEMA.md (required/optional fields).  

## Phase 2: COMPOSE  
1. Create YAML file with root key `marketplace_app_manifest`.  
2. Populate metadata section using SCHEMA.md (name, version, provider).  
3. Define permissions under `perms` with platform-specific scopes.  
4. Specify pricing model in `pricing` (type, cost, currency).  
5. Add constraints under `constraints` (data residency, encryption).  
6. Reference OUTPUT_TEMPLATE.md for nested structure (e.g., `dependencies`).  
7. Validate against SCHEMA.md using YAML linter.  
8. Insert platform-specific config blocks (Claude: `api_keys`, LangChain: `llm_type`).  
9. Finalize with `checksum` hash of manifest content.  

## Phase 3: VALIDATE  
- [ ] ✅ All required fields in metadata exist (name, version, provider).  
- [ ] ✅ Permissions align with platform-specific schema (IAM, API keys).  
- [ ] ✅ Pricing model matches declared type (free, tiered, etc.).  
- [ ] ✅ Constraints comply with data residency/encryption rules.  
- [ ] ✅ YAML syntax passes SCHEMA.md validation and linter checks.
