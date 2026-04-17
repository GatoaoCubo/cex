---
kind: examples
id: bld_examples_legal_vertical
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of legal_vertical artifacts
quality: 8.9
title: "Examples Legal Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [legal_vertical, builder, examples]
tldr: "Golden and anti-examples of legal_vertical artifacts"
domain: "legal_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```markdown
---
title: Legal Vertical Artifact for Contract Analysis
kind: legal_vertical
vendor: ContractWorks
use_case: Contract Review for M&A Transactions
date: 2023-10-05
---
**Privilege Management**: Uses AI to flag privileged communications in due diligence, integrating with Relativity for e-discovery workflows.
**Billable Hour Tracking**: Syncs with Bill.com to auto-generate time entries for contract review tasks, reducing manual logging by 40%.
**Contract Analysis**: Parses 10,000+ clauses across 500+ contracts using natural language processing, identifying non-compliance with GDPR and CCPA.
**Use Cases**: Deployed by Baker McKenzie for cross-border merger contracts, reducing review time from 8 weeks to 3 weeks.
```

## Anti-Example 1: Compliance Checklist Misuse
```markdown
---
title: Legal Vertical Artifact for Audit Compliance
kind: legal_vertical
vendor: LogicGate
use_case: SOC 2 Audit Preparation
date: 2023-09-20
---
**Privilege Management**: N/A
**Billable Hour Tracking**: N/A
**Contract Analysis**: N/A
**Use Cases**: Tracks compliance controls for cloud providers, not legal workflows.
```
## Why it fails:
Confuses compliance_checklist (audit) with legal_vertical. No legal-specific use cases (e.g., privilege, contract analysis) are addressed.

## Anti-Example 2: Generic Case Study
```markdown
---
title: Legal Vertical Artifact for General Practice
kind: legal_vertical
vendor: Clio
use_case: Small Business Law
date: 2023-08-15
---
**Privilege Management**: Basic document storage with no AI features.
**Billable Hour Tracking**: Manual time entry only.
**Contract Analysis**: No clause parsing or automation.
**Use Cases**: "Helps lawyers manage their practice" (too vague, not aligned with legal_vertical KC).
```
## Why it fails:
Lacks specificity in legal vertical use cases (e.g., privilege logs, contract analysis). Treats Clio as a general tool rather than a legal_vertical artifact.
