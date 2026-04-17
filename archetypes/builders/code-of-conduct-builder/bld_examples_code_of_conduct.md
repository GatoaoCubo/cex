---
kind: examples
id: bld_examples_code_of_conduct
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of code_of_conduct artifacts
quality: 9.0
title: "Examples Code of Conduct"
version: "1.0.0"
author: n04_knowledge
tags: [code_of_conduct, builder, examples]
tldr: "Golden and anti-examples of code_of_conduct artifacts"
domain: "code_of_conduct construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---

## Golden Example
```markdown
---
id: p05_coc_openwidget.md
kind: code_of_conduct
pillar: P05
title: "OpenWidget Code of Conduct"
contact_email: "conduct@openwidget.org"
enforcement_version: "2.1"
scope: "online_and_offline"
response_sla: "48h"
quality: null
version: "1.0.0"
created: "2026-04-14"
updated: "2026-04-14"
---

# Contributor Covenant Code of Conduct

## Our Pledge
We as members, contributors, and leaders of OpenWidget pledge to make
participation in our community a harassment-free experience for everyone...

## Our Standards
Examples of behavior that contributes to a positive environment:
- Using welcoming and inclusive language
- Being respectful of differing viewpoints

Examples of unacceptable behavior:
- Harassment, trolling, or personal attacks
- Publishing others' private information

## Enforcement Responsibilities
Community leaders are responsible for clarifying and enforcing standards...

## Scope
This CoC applies within all community spaces, online and offline.

## Enforcement
Report incidents to conduct@openwidget.org. Response within 48h guaranteed.

### Enforcement Guidelines
1. Correction -- written warning for minor infractions
2. Warning -- formal warning with restrictions
3. Temporary Ban -- time-limited removal from community
4. Permanent Ban -- permanent removal for repeated violations

## Attribution
Adapted from the Contributor Covenant, version 2.1.
```

## Anti-Example 1: Missing Enforcement Ladder
```markdown
---
kind: code_of_conduct
title: "Project Rules"
---
Be nice. No harassment. Email us if there are problems at info@project.com.
```
Why it fails: No enforcement ladder, no pledge section, no scope definition, no attribution. Unactionable for maintainers facing a real incident.

## Anti-Example 2: Domain Contamination
```markdown
---
kind: code_of_conduct
title: "Investment Community Code of Conduct"
---
All members must disclose financial interests before recommending assets...
```
Why it fails: Financial/investment domain language contaminating an OSS community conduct document. CoC is about contributor behavior, not financial disclosures.

## Anti-Example 3: Weights Not Summing to 1.0
```
D01 | Pledge quality | 0.10
D02 | Standards | 0.20
D03 | Enforcement | 0.15
D04 | Reporting | 0.10
-- Total: 0.55 (FAIL -- must be 1.00)
```
Why it fails: Quality gate soft scoring weights must sum exactly to 1.00 for valid normalization.
