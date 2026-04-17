---
id: hybrid_review7_n03
kind: audit
pillar: P07
title: HYBRID_REVIEW7 N03 Audit -- partner_listing + marketplace_app_manifest + oauth_app_config
version: 1.0.0
quality: 8.9
tags: [audit, hybrid_review7, n03, wave6, partner_platform_cluster]
domain: builder quality assurance
created: "2026-04-14"
updated: "2026-04-14"
author: n03_engineering
mission: HYBRID_REVIEW7
wave: review
source_model: qwen3:14b (Wave 6 gen_v2)
auditor_model: claude-opus-4-6
---

# HYBRID_REVIEW7 N03 Audit

## Scope

39 ISOs across 3 Wave 6 partner-platform kinds:

| Kind | Builder Dir | ISOs | Pillar |
|------|------------|------|--------|
| partner_listing | archetypes/builders/partner-listing-builder/ | 13 | P05 |
| marketplace_app_manifest | archetypes/builders/marketplace-app-manifest-builder/ | 13 | P09 |
| oauth_app_config | archetypes/builders/oauth-app-config-builder/ | 13 | P09 |

## Validator Results (cex_wave_validator.py)

| Builder | Pre-fix | Post-fix |
|---------|---------|----------|
| partner-listing-builder | 13/13 PASS | 13/13 PASS |
| marketplace-app-manifest-builder | 13/13 PASS | 13/13 PASS |
| oauth-app-config-builder | 13/13 PASS | 13/13 PASS |

All 7 systemic checks (C1-C7) passed on all 39 ISOs.

## 5D Scoring (industry-benchmarked)

Dimensions: D1 Schema alignment / D2 Industry citation / D3 Density / D4 Boundary clarity / D5 ISO coherence.

### 1. partner_listing -- Score 8.2/10 (surgical fixes applied)

| Dim | Score | Evidence |
|-----|-------|----------|
| D1 Schema alignment | 8.5 | ID pattern `^p05_pl_[a-z][a-z0-9_]+.md$` valid; required fields include partner_name, partner_type, listing_status, start_date |
| D2 Industry citation | 7.5 | Cites ISO/IEC 27001, ITIL 4, GS1, RFC 5322, Gartner Partner Ecosystem, PMI. **Missing: Salesforce AppExchange listing fields (AppListing__c, tier metadata), AWS Partner Network tiers (Select/Advanced/Premier/Registered), HubSpot Solutions Directory schema, co-sell/co-market flags** |
| D3 Density | 8.5 | KC has 8 Key Concepts with sources, 7 Industry Standards, 6 Patterns, 5 Pitfalls. Not padded |
| D4 Boundary clarity | 8.0 | Scope limited to channel/partner data. Boundary with crm/partner_program not explicit |
| D5 ISO coherence | 8.5 | Schema ID pattern matches quality_gate H02. Tier vocabulary consistent (platinum/gold/silver) across KC, schema, QG |

**Fix applied (this audit):** Quality gate SOFT weights previously summed to 0.90 (defect D11 from master_systemic_defects). Rebuilt 5D dimensions to sum to 1.00 and aligned dimension names with industry benchmarks (AppExchange fields, AWS PN tiers, ISO 3166-1 region, RFC 5322 email, NAICS industry).

| Before | After |
|--------|-------|
| 8 dimensions summing 0.90 (generic: completeness, accuracy, consistency...) | 5 dimensions summing 1.00 (benchmarked to AppExchange + AWS PN + HubSpot Solutions) |

### 2. marketplace_app_manifest -- Score 8.4/10 (leave as-is)

| Dim | Score | Evidence |
|-----|-------|----------|
| D1 Schema alignment | 8.5 | ID pattern `^p09_mam_[a-z][a-z0-9_]+.yaml$`, required fields cover app_id + marketplace_url + metadata |
| D2 Industry citation | 8.5 | Cites SPDX 2.2 (license), OAuth 2.0 RFC 6749 (scopes), OpenAPI v3.0.3, JSON Schema RFC 8259, GDPR 2016/679, ISO/IEC 27001:2022, NIST CSF, OWASP API Top 10, OCI Image Spec. **Could add: Slack app manifest YAML schema, GitHub App manifest, Claude Marketplace skill metadata, HuggingFace model card metadata** |
| D3 Density | 8.5 | 8 Key Concepts + sources, 10 Industry Standards, 6 Patterns, 5 Pitfalls |
| D4 Boundary clarity | 8.0 | Focus on marketplace listing + metadata + pricing. Clear separation from runtime/sandbox |
| D5 ISO coherence | 8.5 | SOFT weights sum to 1.00 (D01-D05=0.10, D06=0.15, D07-D08=0.10, D09=0.05, D10=0.10); QG H02 pattern matches schema |

**No changes needed.** Minor nit: unicode `>=` and `<=` glyphs used in QG Actions/HARD gates (acceptable in .md files, not code).

### 3. oauth_app_config -- Score 8.3/10 (surgical fixes applied)

| Dim | Score | Evidence |
|-----|-------|----------|
| D1 Schema alignment | 8.5 | ID pattern `^p09_oauth_[a-z][a-z0-9_]+.yaml$`, required fields: client_id, client_secret, domain |
| D2 Industry citation | 8.8 | Now cites RFC 6749 OAuth 2.0, RFC 6750 Bearer, RFC 7636 PKCE, RFC 8252 native apps, RFC 7662 introspection, RFC 7009 revocation, RFC 7519 JWT, RFC 9068 JWT access token profile, OAuth 2.1 draft, OIDC Core 1.0, OIDC Discovery, OAuth BCP, NIST SP 800-63B |
| D3 Density | 8.5 | 12 Key Concepts with RFC section references (e.g., `RFC 6749 §3.3` for scopes), 7->13 Industry Standards post-fix |
| D4 Boundary clarity | 8.5 | Explicitly distinguishes from SSO (workforce) and secret mgmt (raw credentials). Focus: third-party API access control + token lifecycle |
| D5 ISO coherence | 7.8 | QG HARD gates now enforce OAuth 2.1 constraints (no implicit, no ROPC, PKCE mandatory, short access token, rotating refresh); schema still names field `client_secret` as `yes` required but OAuth 2.1 public clients (SPA, native) MUST NOT have secrets -- nuance acceptable for confidential-client default but flag for doc |

**Fixes applied (this audit):**

1. **RFC numbering errors corrected:** "RFC 8256" (fake) -> removed, OIDC Core 1.0 noted as OpenID Foundation not IETF. "RFC 8253" (fake) -> replaced with `draft-ietf-oauth-security-topics BCP`.
2. **Missing standards added:** OIDC Discovery (.well-known/openid-configuration), OAuth 2.1 draft, RFC 7662 introspection, RFC 7009 revocation, RFC 7519 JWT, RFC 9068 JWT access token profile.
3. **Quality gate HARD gates hardened:** H07 access token <= 24h -> <= 1h (OAuth BCP); H08 refresh policy 'fixed or rolling' -> 'rotating' only (OAuth 2.1); added H09 grant_types subset check (no implicit/ROPC); added H10 PKCE S256 required.
4. **D07 vague "CEX OAuth2 spec" -> concrete "OAuth 2.1 + RFC 7636 PKCE + RFC 8252"**.

## Systemic Defects Cross-Check vs master_systemic_defects.md

| Defect | Present? | Notes |
|--------|----------|-------|
| D01 system_prompt llm_function=INJECT | NO | All 3 builders have BECOME correctly |
| D02 memory kind=learning_record | NO | gen_v2 fixed this; all 3 have kind=memory |
| D03 quality_gate tests runtime metrics | NO | All 3 QGs test artifact structure, not deployed systems |
| D04 Domain hallucination (crypto/trading) | NO | Zero financial-domain contamination detected (validator C5 confirms) |
| D05 schema quality non-null defaults | NO | All 3 schemas have `quality: null` |
| D06 H02 pattern divorced from schema | NO | partner_listing H02 `^p05_pl_...` matches schema. marketplace_app_manifest `^p09_mam_...` matches. oauth_app_config `^p09_oauth_...` matches |
| D07 Fabricated tools | NO | Spot-check: tools ISOs reference CEX tools (cex_compile, cex_doctor, cex_score) |
| D08 Bare template {{placeholders}} | NO | Validator C6 pass |
| D09 architecture generic tech stack | NO | Wave 6 gen_v2 produced ISO inventory lists, not generic stacks |
| D10 File reference drift | NO | Cross-references use `bld_schema_{kind}.md` naming |
| D11 SOFT weights do not sum to 1.00 | **YES (partner_listing only)** | **FIXED**: 0.90 -> 1.00 |
| D12 ASCII violations | NO (markdown) | QG uses unicode `>=`/`<=` in marketplace_app_manifest -- acceptable in .md |
| D13 density_score hardcoded 0.85 | YES (all 39) | Systemic across wave1_builder_gen_v2. Not in-scope to fix per-artifact; requires generator patch |
| D14 Empty config fields | NO | Spot-check OK |
| D15 Generic collaboration names | NO | Spot-check uses real nucleus names (N03, N06) |

**Post-fix health:** 0 CRITICAL + 0 HIGH defects remaining on these 39 ISOs.

## Industry Alignment Summary

| Kind | Benchmarks met | Benchmarks partial/missing |
|------|---------------|---------------------------|
| partner_listing | ISO/IEC 27001 certs, RFC 5322 email, GS1 IDs, ISO 3166-1 regions (post-fix) | Salesforce AppExchange listing schema specifics, AWS PN tier exact naming, HubSpot Solutions Directory fields |
| marketplace_app_manifest | SPDX licensing, OAuth 2.0 scopes, OpenAPI 3.0.3, JSON Schema, OCI, GDPR, NIST CSF, OWASP API Top 10 | Slack/GitHub App manifest YAML schemas, Claude Marketplace skill format, HF model card fields |
| oauth_app_config | OAuth 2.0/2.1, PKCE RFC 7636, RFC 8252 native apps, OIDC Core + Discovery, JWT RFC 7519/9068, BCP, NIST SP 800-63B | DPoP (RFC 9449) for sender-constrained tokens; mTLS client auth (RFC 8705); PAR (RFC 9126) |

## Audit Verdict

| Kind | Pre-audit score | Action | Post-audit score |
|------|----------------|--------|------------------|
| partner_listing | ~7.8 (weight defect) | Surgical: QG 5D rebuild | **8.2** |
| marketplace_app_manifest | 8.4 | Leave | **8.4** |
| oauth_app_config | ~7.6 (RFC errors + weak QG) | Surgical: KC + QG | **8.3** |

All 3 builders cleared the 8.0 PUBLISH floor. 2 surgical fixes applied across 3 files (partner_listing QG, oauth_app_config KC + QG). Validator re-run: 39/39 PASS.

## Files Modified

1. `archetypes/builders/partner-listing-builder/bld_quality_gate_partner_listing.md` -- SOFT dimensions rebuilt (5 dims, weights sum 1.00, benchmarked to AppExchange/AWS PN/HubSpot)
2. `archetypes/builders/oauth-app-config-builder/bld_knowledge_card_oauth_app_config.md` -- Industry Standards list corrected (fake RFCs removed, added OIDC Discovery, OAuth 2.1, JWT RFC 9068, RFC 7662 introspection, RFC 7009 revocation, BCP)
3. `archetypes/builders/oauth-app-config-builder/bld_quality_gate_oauth_app_config.md` -- HARD gates hardened (H07 token lifetime 24h -> 1h, H08 rotating refresh only, H09 grant_types allowlist, H10 PKCE S256); D07 vague reference replaced with concrete RFCs

## Recommendations (next waves)

1. **Generator patch:** inject marketplace-specific references (Slack/GitHub App manifest, Claude/HF metadata) for marketplace_app_manifest builder template.
2. **Generator patch:** inject AppExchange/AWS PN/HubSpot Solutions references for partner_listing builder template.
3. **Add DPoP + mTLS + PAR** to oauth_app_config KC in HYBRID_REVIEW8 (advanced OAuth 2.1 extensions).
4. **D13 resolution:** replace hardcoded `density_score: 0.85` in wave1_builder_gen_v2 with a measured value (e.g., content-entropy heuristic).
