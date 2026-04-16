---
kind: instruction
id: bld_instruction_sso_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for sso_config
quality: 8.9
title: "Instruction Sso Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sso_config, builder, instruction]
tldr: "Step-by-step production process for sso_config"
domain: "sso_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify required identity providers (IDP) and their supported protocols (SAML, OIDC).  
2. Retrieve IDP metadata (e.g., SAML metadata URL, OIDC discovery document).  
3. Determine user attribute mappings (e.g., email, roles) required for application integration.  
4. Review organizational security policies (e.g., encryption, token lifetime constraints).  
5. Document existing SSO infrastructure (e.g., federation services, proxy configurations).  
6. Confirm compliance with regulatory requirements (e.g., GDPR, HIPAA).  

## Phase 2: COMPOSE  
1. Set up working directory with bld_schema_sso_config.md and bld_output_template_sso_config.md as references.  
2. Define artifact structure: `idp_config`, `protocol`, `attribute_mapping`, `constraints`.  
3. Populate `idp_config` with metadata URLs, entity IDs, and certificate fingerprints.  
4. Specify protocol version (SAML 2.0, OIDC 1.0) and message signing requirements.  
5. Map user attributes to application claims (e.g., `user.email` → `email`).  
6. Apply constraints: token lifetime (e.g., `max_age=3600`), encryption algorithms (e.g., `RSA256`).  
7. Validate against bld_schema_sso_config.md using a JSON schema validator (e.g., jsonschema).  
8. Use bld_output_template_sso_config.md to format final configuration (YAML or JSON).  
9. Add comments for audit trails (e.g., `last_modified`, `author`).  

## Phase 3: VALIDATE  
- [ ] [OK] Check syntax compliance with bld_schema_sso_config.md (no schema errors).  
- [ ] ✅ Verify protocol compatibility (SAML/OIDC endpoints match IDP metadata).  
- [ ] ✅ Confirm attribute mappings align with application requirements.  
- [ ] ✅ Ensure constraints (e.g., `max_age`, `encryption`) meet security policies.  
- [ ] ✅ Test artifact with IDP using mock SSO flow (e.g., SAML response validation).
