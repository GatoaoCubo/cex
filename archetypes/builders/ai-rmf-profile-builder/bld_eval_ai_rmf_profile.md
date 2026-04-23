---
kind: quality_gate
id: p11_qg_ai_rmf_profile
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for ai_rmf_profile
quality: 9.0
title: "Quality Gate AI RMF Profile"
version: "1.0.0"
author: n01_wave7
tags: [ai_rmf_profile, builder, quality_gate, NIST, AI-RMF, GOVERN, MAP, MEASURE, MANAGE, GenAI-profile, 600-1, action-ID, risk-category]
tldr: "Quality gate with HARD and SOFT scoring for ai_rmf_profile"
domain: "ai_rmf_profile construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_ai_rmf_profile
  - bld_instruction_ai_rmf_profile
  - p03_sp_ai_rmf_profile_builder
  - ai-rmf-profile-builder
  - bld_schema_ai_rmf_profile
  - bld_output_template_ai_rmf_profile
  - bld_knowledge_card_ai_rmf_profile
  - kc_ai_rmf_profile
  - p11_qg_safety_hazard_taxonomy
  - p11_qg_audit_log
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| AI-RMF profile completeness | 100% | equals | All 4 functions + 12 risk categories |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|---------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches pattern ^p11_rmf_[a-z][a-z0-9_]+\.md$ | ID format mismatch |
| H03 | kind field equals 'ai_rmf_profile' | Kind field incorrect or missing |
| H04 | All 4 functions present (GOVERN/MAP/MEASURE/MANAGE) | Any function missing from Function Coverage table |
| H05 | All 12 GenAI risk categories from AI 600-1 present | Any risk category missing from Risk Category Severity Matrix |
| H06 | Action-IDs follow NIST format (GV/MP/MS/MG prefix) | Malformed action-ID (e.g., "Govern-1" instead of "GV-1.1") |
| H07 | profile_scope field present | Missing system name or deployment context |
| H08 | review_date field present and valid ISO 8601 | Missing or malformed review date |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|--------------|
| D01 | Function coverage depth (action-IDs per function) | 0.25 | >= 3 action-IDs per function = 1.0, 1-2 = 0.5, none = 0 |
| D02 | Risk category severity assignments | 0.25 | All 12 categories with severity = 1.0, partial = 0.5, < 6 = 0 |
| D03 | Implementation status completeness | 0.20 | All action-IDs have status = 1.0, partial = 0.5, none = 0 |
| D04 | Crosswalk table present (ISO 42001 or EU AI Act) | 0.15 | Crosswalk with >= 1 framework = 1.0, partial = 0.5, absent = 0 |
| D05 | Evidence pointers per action-ID | 0.15 | Evidence for >= 50% of IDs = 1.0, < 50% = 0.5, none = 0 |

## Actions
| Score | Action |
|-------|--------|
| GOLDEN | >= 9.5 | Auto-publish with no review |
| PUBLISH | >= 8.0 | Auto-publish after validation |
| REVIEW | >= 7.0 | Require manual review by AI governance team |
| REJECT | < 7.0 | Reject and return for revision |

## Bypass
| Condition | Approver | Audit Trail |
|-----------|---------|-------------|
| Emergency regulatory audit | CISO + Legal | Exception log with justification |

## Examples

## Golden Example
```markdown
---
kind: ai_rmf_profile
id: p11_rmf_customer_support_llm_v1
title: "AI RMF GenAI Profile -- Customer Support LLM (v1.0)"
profile_scope: "Customer support chatbot, SaaS deployment, B2B users, English-only"
review_date: "2026-04-14"
profiler: "AI Governance Team"
version: "1.0"
---

## Function Coverage

| Function | Action-IDs Covered | Status |
|----------|-------------------|--------|
| GOVERN | GV-1.1, GV-2.2, GV-4.1, GV-6.1 | Implemented |
| MAP | MP-2.3, MP-3.1, MP-5.2 | Partial |
| MEASURE | MS-1.1, MS-2.5, MS-4.1 | Planned |
| MANAGE | MG-1.1, MG-3.2 | Partial |

## Risk Category Severity Matrix

| Category | Severity | Controlling Action-IDs | Response |
|---------|---------|----------------------|---------|
| CBRN Information | Critical | MP-3.1, MG-1.1 | Hard block + logging |
| Confabulation | High | MS-2.5, MG-3.2 | Disclaimer on uncertain outputs |
| Data Privacy | High | GV-4.1, MP-2.3 | PII redaction pre-output |
| Harmful Bias | High | MS-1.1, MP-5.2 | Bias eval quarterly |
...
```

## Anti-Example 1: Missing Action-IDs
```markdown
---
kind: ai_rmf_profile
title: "Our AI Governance Profile"
---
We follow the GOVERN, MAP, MEASURE, and MANAGE functions.
We assess risks and manage them responsibly.
```
Why it fails: No action-IDs referenced, no risk categories listed, no implementation status.
The output is narrative prose, not a structured profile. Useless for audit or compliance purposes.

## Anti-Example 2: Confusing with Compliance Framework
```markdown
---
kind: compliance_framework
title: "NIST AI-RMF Compliance Checklist"
---
GDPR: Compliant
SOC 2: Compliant
NIST AI-RMF: In Progress
```
Why it fails: This is a general compliance_framework artifact. An ai_rmf_profile requires
function-specific action-ID mapping and GenAI risk-category severity assignments per AI 600-1.
The kind field is wrong and the content has no AI-RMF structure.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
