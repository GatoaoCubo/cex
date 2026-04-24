---
id: p07_sr_ops_3layer
kind: scoring_rubric
8f: F7_govern
pillar: P07
title: "Rubric: N05 Operations 3-Layer"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: scoring-rubric-builder
framework: "ops_3layer"
target_kinds:
  - env_config
  - rate_limit_config
  - secret_config
  - feature_flag
  - cli_tool
  - browser_tool
  - mcp_server
  - webhook
  - api_client
  - quality_gate
  - bugloop
  - guardrail
  - eval_framework
dimensions_count: 4
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "operations"
quality: 9.1
tags: [scoring-rubric, ops, operations, n05, 3-layer, gating-wrath]
tldr: "3-layer rubric for N05 ops artifacts: structural 30%, rubric 30%, semantic 40%. Gating Wrath bias: reject if not production-trustworthy."
density_score: 0.91
calibration_set: [p07_e2e_n05, p07_efw_n05_operations, p07_tc_n05_operations]
inter_rater_agreement: 0.88
appeals_process: "Re-submit to N05 with cex_score.py --apply output attached; N07 arbitrates on score delta > 1.0"
linked_artifacts:
  primary: "N05_operations/P08_architecture/nucleus_def_n05.md"
  related:
    - "N05_operations/P07_evals/p07_efw_n05_operations.md"
    - "N05_operations/P07_evals/p07_e2e_n05.md"
    - "N05_operations/P07_evals/p07_tc_n05_operations.md"
related:
  - p03_sp_verification_agent
  - p11_qg_creation_artifacts
  - p07_sr_knowledge_eval
  - p08_ac_verification
  - p11_qg_kind_builder
  - p01_kc_artifact_quality_evaluation_methods
  - p11_qg_quality_gate
  - p07_qg_12_point_validation
  - p11_qg_intelligence_artifact
  - build_and_review
---

## Framework Overview

3-Layer evaluates all operational artifacts produced by N05 (Operations nucleus, sin: Gating
Wrath). The three layers are independent and non-overlapping: structural integrity (L1),
rubric compliance (L2), and semantic production-readiness (L3). Weights reflect the Gating
Wrath bias -- semantic trust (L3 40%) outweighs structural checks (L1 30%) because an
artifact that passes formatting but fails in production is worse than an unformatted one.

Applies to all N05-owned kinds: config (P09), tools (P04), quality gates (P11), and
eval artifacts (P07). Does NOT apply to knowledge_card (N04), agent design (N02/N03), or
orchestration artifacts (N07).

L1 and L2 are partially automated via `cex_score.py` + `cex_doctor.py`. L3 requires
human or LLM-as-judge evaluation (recommended: only when L1+L2 >= 8.5).

## Dimensions

| Dimension | Layer | Weight | Scale | Criteria | Score=10 | Score=5 |
|-----------|-------|--------|-------|----------|----------|---------|
| Structural Integrity | L1 | 30% | 0-10 | All required frontmatter fields present; id == filename stem; byte size <= kind limit; naming matches `p{xx}_{kind}_{scope}`; code is ASCII-only | 12+ fields, id matches, under limit, correct naming, 0 non-ASCII in .py/.sh | Missing `tldr`, id mismatch, over byte limit, camelCase naming |
| Domain Accuracy | L2 | 15% | 0-10 | Canonical ops terms only: env_config not "settings file"; mcp_server not "plugin"; rate_limit_config not "throttle"; no invented synonyms for P04/P09/P11 kinds | All headings and fields use canonical kind names; pillar reference correct | Uses "settings file", "plugin", "test suite" in place of kind names |
| Actionability | L2 | 15% | 0-10 | Commands include exact flags; config keys are named and typed with defaults; no abstract "configure as needed" without concrete value | `python _tools/cex_doctor.py --scope n05 --strict`; typed config block; webhook includes curl example | "Run the doctor tool"; config shows `<value>` placeholder with no type or default |
| Semantic Trust | L3 | 40% | 0-10 | Artifact solves stated problem end-to-end; operator can deploy without clarification; Gating Wrath lens evident (blocks bad states, does not merely describe them) | env_config has all envvars with validation + fallback; quality_gate has PASS/FAIL predicates with error messages | quality_gate describes checks in prose but has no PASS/FAIL logic; env_config lists vars with no validation |

**Weight verification:** 30 + 15 + 15 + 40 = 100%

## Thresholds

| Tier | Score | Range | Action |
|------|-------|-------|--------|
| GOLDEN | >= 9.5 | 9.5-10.0 | Promote to calibration set; mark as reference example for N05 builders |
| PUBLISH | >= 8.0 | 8.0-9.4 | Merge to nucleus pool; no changes required |
| REVIEW | >= 7.0 | 7.0-7.9 | Return to F6 with dimension feedback; single retry allowed |
| REJECT | < 7.0 | 0-6.9 | Discard; restart from F2 with full builder reload |

**Gating Wrath rule:** if Semantic Trust (L3) score < 7.0, the artifact is REJECT regardless
of total weighted score. An operationally untrustworthy artifact cannot be saved by clean
frontmatter.

## Calibration

| Tier | Score | Reference | Rationale |
|------|-------|-----------|-----------|
| GOLDEN | 9.6 | `p07_efw_n05_operations.md` | All fields, canonical terms, exact tool invocations, executable test pyramid -- operator can invoke immediately |
| PUBLISH | 8.3 | Typical N05 config | Complete frontmatter, correct naming, commands present, one flag unspecified, staging-adequate trust |
| REVIEW | 7.4 | Config with placeholders | All sections present; 2 commands use `<value>`; "settings" used once; fallback behavior missing |
| REJECT | 4.1 | quality_gate (prose-only) | No PASS/FAIL predicates; Gating Wrath lens absent; L3=3.0 triggers hard reject override |

## Automation

| Dimension | Status | Tool | Checks |
|-----------|--------|------|--------|
| Structural Integrity | automated | `cex_score.py --layer structural` + `cex_doctor.py` | Field presence, byte count, naming regex, ASCII scan |
| Domain Accuracy | semi-automated | `cex_doctor.py --vocab` + manual | Canonical term grep; human verifies no synonyms |
| Actionability | semi-automated | `cex_hooks.py post-tool-use` + manual | Placeholder `<value>` grep; human verifies runnability |
| Semantic Trust | manual | Human / LLM-as-judge (L3) | Only triggered when L1+L2 >= 8.5 per score protocol |

L3 Semantic Trust uses `cex_score.py` LLM judge mode. Invocation:
`python _tools/cex_score.py --apply {path} --layer semantic --nucleus n05`

## References

- `N05_operations/P08_architecture/nucleus_def_n05.md` (N05 domain + sin lens definition)
- `N05_operations/P07_evals/p07_efw_n05_operations.md` (calibration: GOLDEN tier example)
- `archetypes/builders/scoring-rubric-builder/bld_schema_scoring_rubric.md` (rubric schema)
- `_tools/cex_score.py` (3-layer scorer implementation)
- `_tools/cex_doctor.py` (structural automation tool)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_verification_agent]] | upstream | 0.25 |
| [[p11_qg_creation_artifacts]] | downstream | 0.25 |
| [[p07_sr_knowledge_eval]] | sibling | 0.24 |
| [[p08_ac_verification]] | downstream | 0.24 |
| [[p11_qg_kind_builder]] | downstream | 0.24 |
| [[p01_kc_artifact_quality_evaluation_methods]] | upstream | 0.23 |
| [[p11_qg_quality_gate]] | downstream | 0.23 |
| [[p07_qg_12_point_validation]] | related | 0.23 |
| [[p11_qg_intelligence_artifact]] | downstream | 0.23 |
| [[build_and_review]] | downstream | 0.23 |
