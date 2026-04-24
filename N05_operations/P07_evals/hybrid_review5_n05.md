---
id: hybrid_review5_n05
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "HYBRID_REVIEW5 N05 Audit: rbac_policy + sso_config + usage_quota (39 ISOs)"
version: "1.0.0"
quality: 8.9
tags: [audit, hybrid_review5, wave4, rbac_policy, sso_config, usage_quota, security]
domain: operations audit
created: "2026-04-14"
updated: "2026-04-14"
author: n05_operations
tldr: "39 ISOs across 3 Wave 4 security/ops builders audited. 8 defects fixed: D02 (x3), D07 (x3), D10 (x3), D11 (x1), D03 (x1), D15 (x1), SECURITY (x1). All 39 ISOs pass validator post-fix."
source_model: qwen3:14b (Wave 4 gen_v2)
related:
  - bld_schema_rbac_policy
  - bld_schema_sso_config
  - bld_schema_kind
  - bld_collaboration_rbac_policy
  - bld_schema_reranker_config
  - n04_audit_stt_provider_builder
  - bld_schema_api_reference
  - bld_schema_bugloop
  - bld_schema_oauth_app_config
  - bld_schema_safety_policy
---

# HYBRID_REVIEW5 N05 Audit

## Scope

| Builder | ISOs | Pillar | Domain |
|---------|------|--------|--------|
| rbac-policy-builder | 13 | P09 | access control, NIST RBAC, Casbin, OPA/Rego |
| sso-config-builder | 13 | P09 | SAML 2.0, OIDC/OAuth 2.1, SCIM, JWT |
| usage-quota-builder | 13 | P09 | token bucket, leaky bucket, sliding window, 429 headers |
| **TOTAL** | **39** | | |

## Industry Standard References Applied

| Builder | Standards | Key Concepts |
|---------|-----------|--------------|
| rbac_policy | NIST SP 800-162, Casbin, OPA/Rego, Auth0 | Least privilege, ABAC vs RBAC, role hierarchy, tenant isolation |
| sso_config | SAML 2.0 (OASIS), OIDC 1.0 + OAuth 2.1, JWT RFC 7519, SCIM 2.0 RFC 7642 | IdP-initiated vs SP-initiated, JIT provisioning, attribute mapping |
| usage_quota | RFC 6585, IETF rate-limit headers, Stripe metered billing, AWS API Gateway | Token bucket, leaky bucket, sliding window, graceful degradation, 429 |

## Defect Inventory

| # | Defect | Builder | ISO | Severity | Fixed |
|---|--------|---------|-----|----------|-------|
| D02-rbac | kind=learning_record (should be memory) | rbac_policy | bld_memory | CRITICAL | YES |
| D02-sso | kind=learning_record (should be memory) | sso_config | bld_memory | CRITICAL | YES |
| D02-uq | kind=learning_record (should be memory) | usage_quota | bld_memory | CRITICAL | YES |
| D07-rbac | Fabricated tools (rbac_compile.py, rbac_validator.py, etc.) | rbac_policy | bld_tools | HIGH | YES |
| D07-sso | Fabricated tools (sso_compile.py, sso_score.py, etc.) | sso_config | bld_tools | HIGH | YES |
| D07-uq | Mixed: real CEX tools + fabricated (cex_analyzer.py, val_*.py, QuotaManager API) | usage_quota | bld_tools | HIGH | YES |
| D10-rbac | References SCHEMA.md + OUTPUT_TEMPLATE.md (not real ISO filenames) | rbac_policy | bld_instruction | HIGH | YES |
| D10-sso | References SCHEMA.md + OUTPUT_TEMPLATE.md (not real ISO filenames) | sso_config | bld_instruction | HIGH | YES |
| D10-uq | References SCHEMA.md + OUTPUT_TEMPLATE.md (not real ISO filenames) | usage_quota | bld_instruction | HIGH | YES |
| D11-uq | SOFT weights sum 0.90 (not 1.00): D01+D02 both at 0.15, gap of 0.10 | usage_quota | bld_quality_gate | MEDIUM | YES |
| D03-uq | Definition uses runtime metrics (API calls/day 1M, 5TB, 200%); H05 "Rate limiting configured" contradicts scope boundary | usage_quota | bld_quality_gate | MEDIUM | YES |
| D15-rbac | Collaboration uses generic non-CEX names (Security Architect, Compliance Officer) | rbac_policy | bld_collaboration | LOW | YES |
| SEC-sso | SECURITY: output_template includes client_secret as frontmatter field + literal "supersecretkey123!" in example | sso_config | bld_output_template | CRITICAL | YES |

## 5D Scoring

### rbac_policy

| Dim | Dimension | Score | Notes |
|-----|-----------|-------|-------|
| D1 | Relevance | 9.0 | NIST RBAC, tenant isolation, least privilege -- all on-target |
| D2 | Completeness | 8.5 | All 13 ISOs present; D07+D10+D15 fixed; collaboration boundary clear |
| D3 | Accuracy | 9.0 | RBAC concepts correct; H02 pattern consistent with schema naming |
| D4 | Density | 8.5 | density_score=0.85 uniform; actual content dense with security patterns |
| D5 | Usability | 8.5 | System prompt has clear ALWAYS/NEVER; quality_gate passes H01-H08 |
| **TOTAL** | | **8.7** | PUBLISH |

### sso_config

| Dim | Dimension | Score | Notes |
|-----|-----------|-------|-------|
| D1 | Relevance | 9.0 | SAML 2.0, OIDC, SCIM, JWT -- full federation protocol coverage |
| D2 | Completeness | 8.5 | All 13 ISOs present; SECURITY fix critical -- client_secret removed |
| D3 | Accuracy | 9.0 | Protocol details correct; SAML HTTP-Redirect, OIDC discovery endpoints right |
| D4 | Density | 8.5 | Quality gate has 10 HARD gates -- thorough artifact checking |
| D5 | Usability | 8.0 | Output template improved; secret handling now explicit with pointer to secret_config |
| **TOTAL** | | **8.6** | PUBLISH |

### usage_quota

| Dim | Dimension | Score | Notes |
|-----|-----------|-------|-------|
| D1 | Relevance | 8.5 | Token bucket/leaky bucket referenced; scope boundary (NOT rate limiting) correct |
| D2 | Completeness | 8.5 | All 13 ISOs present; D11+D03 fixed; weights now sum 1.00 |
| D3 | Accuracy | 8.5 | Enforcement policy "hard"/"soft" correct; ISO 8601 duration format right |
| D4 | Density | 8.0 | Schema has 4 domain-specific required fields (quota_limit, usage_metric, reset_interval, enforcement_policy) |
| D5 | Usability | 8.5 | HARD gates now test artifact structure not runtime; D03 resolved |
| **TOTAL** | | **8.4** | PUBLISH |

## Fixes Applied

### D02 -- Memory kind corrected (all 3 builders)

Changed `kind: learning_record` -> `kind: memory` and `id: p10_lr_*` -> `id: p10_mem_*` in:
- archetypes/builders/rbac-policy-builder/bld_memory_rbac_policy.md
- archetypes/builders/sso-config-builder/bld_memory_sso_config.md
- archetypes/builders/usage-quota-builder/bld_memory_usage_quota.md

### D07 -- Fabricated tools replaced (all 3 builders)

Replaced fabricated `rbac_*.py`, `sso_*.py`, `val_*.py`, `cex_analyzer.py` with real CEX tools:
- cex_compile.py, cex_score.py --apply, cex_doctor.py, cex_hygiene.py (production)
- cex_wave_validator.py, cex_hooks.py pre-commit, cex_retriever.py (validation)
External refs updated to real industry standards (OPA, Casbin, NIST; SAML 2.0, OIDC, SCIM; RFC 6585, Stripe, AWS API Gateway)

### D10 -- File reference drift corrected (all 3 builders)

Changed `SCHEMA.md` -> `bld_schema_{kind}.md` and `OUTPUT_TEMPLATE.md` -> `bld_output_template_{kind}.md` in all 3 bld_instruction ISOs.

### D11 -- SOFT weight sum corrected (usage_quota)

D01: 0.15->0.20, D02: 0.15->0.20. Sum: 0.90->1.00.

### D03 -- Runtime gates removed (usage_quota quality_gate)

Definition section: removed runtime metrics (API calls/day, 5TB transfer, 200% burst) -- replaced with artifact structure checks.
H05: "Rate limiting configured" -> "enforcement_policy field present" (artifact field, matches schema).
H06-H08: replaced runtime logging/error checks with artifact field checks (reset_interval ISO 8601, quota_limit positive, usage_metric present).

### D15 -- Collaboration uses real CEX builder names (rbac_policy)

Replaced generic "Security Architect/Compliance Officer/System Administrator" with real CEX builders:
- Receives from: permission-builder, guardrail-builder, env-config-builder
- Produces for: agent-profile-builder, sandbox-config-builder, compliance-framework-builder

### SECURITY -- client_secret removed from sso_config output_template

Removed `client_secret` from frontmatter fields. Added explicit `# NEVER inline` comment.
Replaced literal `"supersecretkey123!"` example with structured SAML 2.0 example using real fields (idp_entity_id, acs_url, slo_url, metadata_url).
Added `client_secret | NEVER` row in field table with pointer to secret_config.

## Validator Results

| Builder | Pre-fix | Post-fix |
|---------|---------|----------|
| rbac-policy-builder | 13/13 structural PASS | 13/13 structural PASS |
| sso-config-builder | 13/13 structural PASS | 13/13 structural PASS |
| usage-quota-builder | 13/13 structural PASS | 13/13 structural PASS |

Note: cex_wave_validator.py checks structural validity (frontmatter, kind, pillar, llm_function). Semantic defects (D02/D07/D10/D11/D03/D15/SECURITY) require manual review and were identified via N05 audit against master_systemic_defects.md.

## PASS/FAIL vs Prior Waves

| Defect | Wave 1+2 frequency | This wave |
|--------|--------------------|-----------|
| D01 system_prompt INJECT | 10/11 audits | FIXED -- all 3 BECOME |
| D02 memory kind | 2/11 audits | STILL PRESENT -- all 3 fixed |
| D07 fabricated tools | 5/11 audits | STILL PRESENT -- all 3 fixed |
| D10 file ref drift | 1/11 audits | STILL PRESENT -- all 3 fixed |
| D11 weight sum | 2/11 audits | PRESENT (usage_quota) -- fixed |
| D03 runtime gates | 2/11 audits | PRESENT (usage_quota) -- fixed |
| SECURITY credential leak | NEW | PRESENT (sso_config) -- fixed |

## Recommendations for Generator Fix

1. **SEC-sso (new defect class)**: `wave1_builder_gen_v2` must add explicit instruction to `build_output_template_prompt`: "NEVER include client_secret, password, private_key, or API key fields in output_template frontmatter. Use placeholder reference to secret_config instead."
2. **D02**: Still present in Wave 4 -- generator fix NOT yet propagated. Confirm wave1_builder_gen.py line 84 was updated.
3. **D07**: Generator still fabricates tool names matching `{kind}_*.py` pattern. Add real CEX tool list to prompt context.
4. **D10**: Generator still uses SCHEMA.md/OUTPUT_TEMPLATE.md as generic references. Fix `build_instruction_prompt` to inject `bld_schema_{kind}.md` + `bld_output_template_{kind}.md`.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_rbac_policy]] | downstream | 0.34 |
| [[bld_schema_sso_config]] | downstream | 0.34 |
| [[bld_schema_kind]] | downstream | 0.31 |
| [[bld_collaboration_rbac_policy]] | downstream | 0.29 |
| [[bld_schema_reranker_config]] | downstream | 0.29 |
| [[n04_audit_stt_provider_builder]] | sibling | 0.28 |
| [[bld_schema_api_reference]] | downstream | 0.27 |
| [[bld_schema_bugloop]] | downstream | 0.27 |
| [[bld_schema_oauth_app_config]] | downstream | 0.27 |
| [[bld_schema_safety_policy]] | downstream | 0.27 |
