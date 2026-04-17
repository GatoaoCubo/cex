---
kind: examples
id: bld_examples_ai_rmf_profile
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of ai_rmf_profile artifacts
quality: 9.1
title: "Examples AI RMF Profile"
version: "1.0.0"
author: n01_wave7
tags: [ai_rmf_profile, builder, examples, NIST, AI-RMF, GOVERN, MAP, MEASURE, MANAGE, GenAI-profile, 600-1, action-ID, risk-category]
tldr: "Golden and anti-examples of ai_rmf_profile artifacts"
domain: "ai_rmf_profile construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

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
