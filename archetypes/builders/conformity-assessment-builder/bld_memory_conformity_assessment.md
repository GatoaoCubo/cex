---
kind: learning_record
id: bld_memory_conformity_assessment
pillar: P10
llm_function: INJECT
purpose: Learned patterns, pitfalls, and evidence from prior conformity assessment build runs
quality: 9.2
title: "Conformity Assessment Builder -- Memory"
version: "1.0.0"
author: wave7_n05
tags: [conformity_assessment, builder, memory]
tldr: "Accumulated learning on EU-AI-Act Annex-IV pitfalls, common RMS gaps, and high-scoring patterns"
domain: "conformity_assessment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_system_prompt_conformity_assessment
  - bld_examples_conformity_assessment
  - bld_instruction_conformity_assessment
  - bld_knowledge_card_conformity_assessment
  - bld_output_template_conformity_assessment
  - bld_collaboration_conformity_assessment
  - bld_manifest_conformity_assessment
  - kc_conformity_assessment
  - bld_tools_conformity_assessment
  - bld_output_template_compliance_framework
---
# Conformity Assessment Builder -- Memory
## Learning Record Type
This is a `correction` + `convention` memory artifact.
It records lessons from prior conformity assessment build cycles to prevent recurrence.
Injected at F3 INJECT to inform F4 REASON and F6 PRODUCE.
---
## Observations (What the Builder Has Learned)
### O-001: RMS Is the Most Common Failure Point
| Attribute | Detail |
|-----------|--------|
| Observation | The risk-management-system section fails H04 gate more than any other section |
| Frequency | ~40% of first-pass builds |
| Root cause | Builders treat RMS as a narrative ("we manage risks") not a structured process with named risks, IDs, and controls |
| Evidence | Anti-example 1 in bld_examples_conformity_assessment.md |
### O-002: DoC vs. Annex IV Confusion Is Endemic
| Attribute | Detail |
|-----------|--------|
| Observation | ~25% of builds confuse the Declaration of Conformity (Art. 47) with the Annex-IV package |
| Root cause | Both are "conformity" documents; the boundary is rarely explained |
| Evidence | Anti-example 2 in bld_examples_conformity_assessment.md |
| Rule derived | System prompt rule: "NEVER conflate the conformity assessment package with the EU Declaration of Conformity document" |
### O-003: Aug-2026 Deadline Often Not Flagged
| Attribute | Detail |
|-----------|--------|
| Observation | When deadlines are not surfaced in output, legal teams miss them in review |
| Root cause | Builders treat the deadline as background context, not a required output element |
| Rule derived | Flag all mandatory Annex-IV items with [AUG-2026-DEADLINE] regardless of declaration_date |
### O-004: PMM Plans Are Frequently Omitted

| Attribute | Detail |
|-----------|--------|
| Observation | Post-market-monitoring (Art. 72) is often absent or one sentence |
| Root cause | Art. 72 is in Chapter VI of the Act; builders focus on Chapter III (high-risk requirements) |
| Fix | H08 gate explicitly checks PMM; instruction Phase 1.5 mandates PMM data collection |

### O-005: Data Governance Conflated with GDPR

| Attribute | Detail |
|-----------|--------|
| Observation | ~15% of builds include GDPR data subject rights in the data-governance section |
| Root cause | "Data governance" is used in both GDPR and EU AI Act contexts |
| Rule derived | EU AI Act Art. 10 data governance = training data quality, bias, provenance. NOT GDPR |
| Boundary | GDPR is out of scope for this builder -- route to DPO |

### O-006: Notified Body Requirement Missed for Biometric ID

| Attribute | Detail |
|-----------|--------|
| Observation | Builders select "internal_check" for real-time remote biometric identification systems |
| Root cause | Article 43(1)(a) exception is not well-known |
| Rule derived | REQUIRE_NB_FOR_BIOMETRIC config flag is true by default; H07 gate checks category |
| Evidence | Annex III(1)(a): real-time remote biometric ID in public spaces requires notified body |

### O-007: Accuracy Metrics Without Test Dataset Reference

| Attribute | Detail |
|-----------|--------|
| Observation | Accuracy claims like "95% accuracy" with no dataset reference fail D03 (evidence density) |
| Root cause | Builders copy accuracy from system specs without adding evaluation context |
| Rule derived | Every accuracy metric MUST include: metric name, threshold, achieved value, AND test dataset name |

---

## Pitfalls (Anti-Patterns to Avoid)

| ID | Pitfall | Prevention |
|----|---------|-----------|
| P-001 | Writing RMS as narrative prose | Use structured table: Risk ID, description, severity, likelihood, mitigation, residual |
| P-002 | Omitting notified body ID for biometric ID systems | Check REQUIRE_NB_FOR_BIOMETRIC flag; enforce at H02 |
| P-003 | Including GDPR in the Annex IV package | Explicitly exclude GDPR at system prompt NEVER rules |
| P-004 | Leaving placeholder text (unfilled template variables) in published artifact | F7 GOVERN check: scan for unfilled double-brace patterns |
| P-005 | Saying system "complies" | Builder documents evidence; provider DECLARES conformity via DoC (Art. 47) |
| P-006 | Generating Aug-2026 deadlines without flags | FLAG_DEADLINE_ITEMS config flag enforces [AUG-2026-DEADLINE] |
| P-007 | Omitting data provenance documentation | Instruction Phase 1.3 mandates provenance reference |
| P-008 | Using em-dashes or smart quotes in output | ASCII rule: use "--" and straight quotes; enforced by cex_sanitize.py |
| P-009 | Self-scoring quality | quality: null always; cex_score.py --apply assigns score after peer review |
| P-010 | Missing post-market-monitoring KPIs | PMM table must have: KPI name, measurement method, threshold, corrective action |

---

## High-Scoring Patterns (Evidence of What Works)

| Pattern | Score Impact | Evidence |
|---------|-------------|---------|
| Named risks with R-00X IDs in RMS table | +0.5 D04 traceability | MedTriage golden example |
| Specific dataset names in data governance | +0.5 D03 evidence density | MedTriage golden example |
| Named XAI tools in human oversight | +0.3 D03 evidence density | MedTriage golden example |
| Art. 9 citation in every RMS paragraph | +0.3 D02 regulatory accuracy | Pattern from legal review |
| PMM table with quantified thresholds | +0.4 D01 completeness | PMM plan structure |
| [AUG-2026-DEADLINE] on all 6 mandatory items | +0.3 D05 auditability | Deadline compliance |

---

## Recommendations (Derived from Learning)

| Recommendation | Applies To | Priority |
|----------------|-----------|---------|
| Always ask for the system's existing risk register before building | F1 CONSTRAIN | HIGH |
| Request accuracy test results from N05 before F6 PRODUCE | F3 INJECT | HIGH |
| Use a 5x5 risk matrix (severity x likelihood) for RMS table | F6 PRODUCE | MEDIUM |
| Derive Annex III category from product description if user does not specify | F1 CONSTRAIN | MEDIUM |
| Cross-reference Art. 10 sub-clauses in data governance section | F6 PRODUCE | MEDIUM |
| Add "not applicable" rows for PMM items that don't apply -- don't omit | F6 PRODUCE | LOW |
| Verify provider address is a full legal registered address | F7 GOVERN | LOW |

---

## Memory Update Protocol

When a new pattern is discovered during a build run:
1. Add an observation (O-XXX) with frequency estimate
2. Add the corresponding pitfall (P-XXX) if actionable
3. Update high-scoring patterns table if score > 9.0 was achieved
4. Log to .cex/learning_records/ via cex_memory_update.py

```bash
python _tools/cex_memory_update.py --kind correction --source conformity_assessment \
  --note "Pattern: DESCRIPTION_TEXT" --impact "SCORE_DELTA_VALUE"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_system_prompt_conformity_assessment]] | upstream | 0.41 |
| [[bld_examples_conformity_assessment]] | upstream | 0.41 |
| [[bld_instruction_conformity_assessment]] | upstream | 0.40 |
| [[bld_knowledge_card_conformity_assessment]] | upstream | 0.40 |
| [[bld_output_template_conformity_assessment]] | upstream | 0.37 |
| [[bld_collaboration_conformity_assessment]] | downstream | 0.36 |
| [[bld_manifest_conformity_assessment]] | downstream | 0.34 |
| [[kc_conformity_assessment]] | upstream | 0.29 |
| [[bld_tools_conformity_assessment]] | upstream | 0.24 |
| [[bld_output_template_compliance_framework]] | upstream | 0.24 |
