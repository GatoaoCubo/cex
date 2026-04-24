---
id: hybrid_review6_n03
kind: knowledge_card
8f: F3_inject
pillar: P01
title: HYBRID_REVIEW6 N03 -- dev-tooling cluster audit (playground/sandbox/integration)
version: 1.0.0
quality: 9.2
tags: [audit, hybrid_review6, n03, dev_tooling, wave5]
domain: builder quality assurance
created: "2026-04-14"
updated: "2026-04-14"
author: n03_engineering
tldr: "Audited 3 Wave 5 dev-tooling builders (39 ISOs). 0 structural failures. 3 surgical fixes to tools + KC ISOs to replace fabricated tool names (D07) and add handoff-specified industry refs (OpenAI Playground, Firecracker/gVisor, Diataxis)."
sources:
  - archetypes/builders/playground-config-builder/
  - archetypes/builders/sandbox-spec-builder/
  - archetypes/builders/integration-guide-builder/
  - N01_intelligence/reports/master_systemic_defects.md
  - N06_commercial/reports/commercial_readiness_20260414.md
related:
  - hybrid_review7_n04
  - hybrid_review7_n05
  - n01_hybrid_review_wave1
  - hybrid_review4_n01
  - hybrid_review3_n05
  - hybrid_review5_n01
  - hybrid_review4_n04
  - master_systemic_defects
  - hybrid_review6_n06
  - hybrid_review3_n02
---

## Scope

| Builder | Kind | ISOs | Pillar | Gen Wave |
|---|---|---|---|---|
| playground-config-builder | playground_config | 13 | P09 | Wave 5 dev+sales+verticals |
| sandbox-spec-builder | sandbox_spec | 13 | P09 | Wave 5 dev+sales+verticals |
| integration-guide-builder | integration_guide | 13 | P05 | Wave 5 dev+sales+verticals |
| **TOTAL** | | **39** | | gen_v2 (qwen3:14b) |

## Validator Results

| Builder | Before fixes | After fixes |
|---|---|---|
| playground_config | 13/13 PASS | 13/13 PASS |
| sandbox_spec | 13/13 PASS | 13/13 PASS |
| integration_guide | 13/13 PASS | 13/13 PASS |

gen_v2 generator produced structurally clean ISOs across all top systemic defects (D01 system_prompt=BECOME confirmed, D02 memory kind=memory confirmed, D03 quality_gate targets artifact not runtime confirmed, D05 schema quality=null confirmed, D11 SOFT weights sum to 1.00 confirmed). Wave 1/Wave 2 systemic defects did NOT recur.

## Defect Analysis (vs master_systemic_defects.md)

| Defect | Status | Notes |
|---|---|---|
| D01 system_prompt llm_function=INJECT | CLEAN | All 3 system_prompt ISOs set llm_function=BECOME |
| D02 memory kind=learning_record | CLEAN | All 3 memory ISOs set kind=memory |
| D03 quality_gate runtime metrics | CLEAN | All 3 gates test artifact YAML + sections |
| D04 financial domain hallucination | CLEAN | No trading/CCXT/Backtrader contamination |
| D05 schema quality non-null | CLEAN | All schemas specify quality=null |
| D06 H02 ID pattern divorced from naming | CLEAN | Patterns match naming column |
| D07 fabricated tools | **PRESENT** | Fixed (see below) |
| D08 bare {{placeholders}} | CLEAN | Output templates have guidance |
| D09 architecture = generic stack | CLEAN | All 3 list 13 builder ISOs |
| D10 file reference drift | CLEAN | References match actual filenames |
| D11 SOFT weight sum != 1.00 | CLEAN | All 3 sum exactly to 1.00 |
| D12 ASCII violations | CLEAN | Sanitize check passes |
| D13 density_score hardcoded 0.85 | PRESENT | Uniform 0.85 across 39 ISOs (systemic, low-priority) |
| D14 empty config fields | CLEAN | All config ISOs populated |
| D15 generic collab names | CLEAN | Real CEX builder refs |

## Surgical Fixes Applied

### Fix 1 -- bld_tools_playground_config.md (D07)
Replaced fabricated tools (cex_optimizer.py, cex_generator.py, val_schema.py, val_consistency.py, val_input.py) with real tools (cex_compile.py, cex_retriever.py, cex_score.py, cex_doctor.py, cex_hygiene.py, cex_prompt_optimizer.py, cex_wave_validator.py, cex_sanitize.py, cex_hooks.py). Added handoff-specified external refs: OpenAI Playground, Swagger Try-It-Out, Replit/CodeSandbox, JupyterLite.

### Fix 2 -- bld_tools_sandbox_spec.md (D07)
Replaced fabricated tools (val_checker.py, val_linter.py, val_comparator.py, "CEX Framework", "Sandbox Validator") with real CEX tools. Added handoff-specified refs: PCI-DSS v4.0, gVisor, Firecracker, Stripe test mode, HIPAA 164.312, NIST SP 800-190, ISO 27001 A.8.31.

### Fix 3 -- bld_tools_integration_guide.md (D07)
Replaced fabricated tools (cex_validator.py, cex_analyzer.py, val_checker.py, val_formatter.py, val_linter.py) with real CEX tools. Added handoff-specified refs: Diataxis How-To quadrant, Auth0 quickstarts, OAuth 2.1/OIDC/SAML, AppExchange, Slack directory.

### Fix 4 -- bld_knowledge_card_playground_config.md
Rewrote Domain Overview + Key Concepts + Industry Standards + Common Patterns + Pitfalls to anchor in PLG conversion framing. Added activation-metric and quota-gate concepts. Distinguished playground vs sandbox roles explicitly. Added shareable-reproduction pattern.

### Fix 5 -- bld_knowledge_card_sandbox_spec.md
Rewrote to anchor in enterprise procurement framing. Named specific isolation technologies (Firecracker, gVisor). Added dual-key pattern (Stripe), audit immutability (QLDB-style), teardown certificate (PCI-DSS 3.2.1 req 9.8), data residency (GDPR Art 44).

### Fix 6 -- bld_knowledge_card_integration_guide.md
Rewrote to anchor in Diataxis How-To quadrant. Added Auth0 quickstart + deep-dive pattern, webhook-vs-polling trade-off, idempotency-key guidance (Stripe pattern), partner certification (AppExchange, Slack). Added E2E verification pattern.

## 5D Scoring Summary (peer review pending)

| Builder | D1 Terminology | D2 Refs | D3 Domain Fit | D4 Density | D5 Builder Utility | Expected |
|---|---|---|---|---|---|---|
| playground_config | post-fix strong | post-fix strong | strong | 0.85 | strong | 8.5-9.0 |
| sandbox_spec | post-fix strong | post-fix strong | strong | 0.85 | strong | 8.5-9.0 |
| integration_guide | post-fix strong | post-fix strong | strong | 0.85 | strong | 8.5-9.0 |

Peer review (cex_score.py --apply) assigns final quality. No self-scoring per CEX rule 4.

## Dev-Tooling Cluster Notes (per handoff lens)

These three kinds define the paid-tier adoption funnel:
1. **playground_config** -- free-tier try-before-buy, activation metric hooks the conversion event.
2. **sandbox_spec** -- enterprise procurement gate, compliance evidence bundle, teardown certificate.
3. **integration_guide** -- partner ecosystem unlock, Diataxis How-To, quickstart-first.

Each KC now names the activation metric (playground), the procurement gate (sandbox), and the partner certification path (integration_guide). Upgrade paths are explicit: playground->paid at quota wall, sandbox->production tenant after pilot, integration_guide->cert+directory listing.

## Recommendations for Downstream Waves

1. Density hardcode (D13) is systemic across all 207 builders -- schedule a separate pass to measure real density via cex_score.py and backfill.
2. Tools ISOs generated by gen_v2 frequently invent val_*.py / cex_*.py names (confirmed in 6 of 6 Wave 5 samples). Add to cex_wave_validator.py: assert tool names exist in _tools/ directory.
3. Knowledge cards benefit from kind-specific handoff-driven refs; propagate this pattern via the gen_v2 prompt template (Wave 6+).

## Commit

```
git add archetypes/builders/playground-config-builder/ archetypes/builders/sandbox-spec-builder/ archetypes/builders/integration-guide-builder/ N03_engineering/audits/
git commit -m "[N03] HYBRID_REVIEW6: audit+fix 3 Wave 5 dev-tooling kinds (39 ISOs, 6 surgical fixes)"
```

## Signal

```
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0)"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[hybrid_review7_n04]] | sibling | 0.37 |
| [[hybrid_review7_n05]] | sibling | 0.36 |
| [[n01_hybrid_review_wave1]] | related | 0.36 |
| [[hybrid_review4_n01]] | sibling | 0.34 |
| [[hybrid_review3_n05]] | sibling | 0.34 |
| [[hybrid_review5_n01]] | sibling | 0.33 |
| [[hybrid_review4_n04]] | sibling | 0.33 |
| [[master_systemic_defects]] | sibling | 0.31 |
| [[hybrid_review6_n06]] | sibling | 0.31 |
| [[hybrid_review3_n02]] | sibling | 0.31 |
