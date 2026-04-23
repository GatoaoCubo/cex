---
kind: knowledge_card
id: bld_knowledge_card_code_of_conduct
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for code_of_conduct production
quality: 9.2
title: "Knowledge Card Code of Conduct"
version: "1.0.0"
author: n04_knowledge
tags: [code_of_conduct, builder, knowledge_card]
tldr: "Domain knowledge for code_of_conduct production"
domain: "code_of_conduct construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - code-of-conduct-builder
  - p03_sp_code_of_conduct_builder
  - bld_instruction_code_of_conduct
  - p10_mem_code_of_conduct_builder
  - bld_examples_code_of_conduct
  - p05_qg_code_of_conduct
  - bld_output_template_code_of_conduct
  - bld_schema_code_of_conduct
  - bld_tools_code_of_conduct
  - bld_collaboration_code_of_conduct
---

## Domain Overview
Code of Conduct artifacts define behavioral expectations, enforcement mechanisms, and reporting channels for open-source communities. The Contributor Covenant (current version: 2.1) is the de facto standard, adopted by thousands of OSS projects including Linux Foundation, Apache, CNCF, and GitHub's own community guidelines. A well-structured CoC reduces maintainer burden by providing a pre-agreed enforcement ladder and reduces community risk by setting clear expectations.

Effective CoCs distinguish between online spaces (issues, PRs, chat, forums) and offline spaces (conferences, meetups). The enforcement ladder progression -- Correction, Warning, Temporary Ban, Permanent Ban -- follows restorative justice principles before escalating to exclusion.

## Key Concepts
| Concept | Definition | Source |
|---------|------------|--------|
| Contributor Covenant | Community CoC standard with pledge, standards, and enforcement | contributor-covenant.org v2.1 |
| Enforcement Ladder | 4-tier escalation: Correction, Warning, Temp Ban, Perm Ban | Mozilla Diversity Guidelines |
| Reporting Channel | Contact method + confidentiality assurance for incident reports | CNCF Community Standards |
| Scope | Online spaces (repo, chat, forums) + offline (events, conferences) | Contributor Covenant v2.1 Section 4 |
| Pledge | Public commitment from community leaders to uphold standards | CoC Section 1 |
| Restorative Justice | Correction-first approach before exclusion | Conflict resolution best practice |
| Protected Characteristics | Attributes that must not be grounds for discrimination | UN Human Rights Framework |
| Response SLA | Maximum time for acknowledging a conduct report | CNCF Code of Conduct v1.3 |

## Industry Standards
- Contributor Covenant v2.1 (primary reference)
- Mozilla Community Participation Guidelines v3.1
- CNCF Code of Conduct v1.3
- Open Source Initiative CoC requirements
- GitHub Community Forum Code of Conduct

## Common Patterns
1. Open with a "We Pledge" statement establishing community intent.
2. Separate positive standards from prohibited behaviors (two lists).
3. Define enforcement ladder with exactly 4 tiers and clear consequences.
4. Provide a single, monitored reporting email (not a generic info@).
5. Include response SLA (48h acknowledgement is the OSS norm).
6. Attribute to source CoC with version number and URL.
7. Keep scope broad: online AND offline spaces.

## Pitfalls
- Enforcement ladder with fewer than 4 tiers reduces maintainer flexibility.
- Missing response SLA creates uncertainty for reporters.
- Vague "be respectful" language without specific prohibited behaviors is unenforceable.
- Using legal liability language without disclaimer creates compliance risks.
- Covering only online spaces misses conference/event incidents.
- No attribution violates Contributor Covenant license terms.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[code-of-conduct-builder]] | downstream | 0.59 |
| [[p03_sp_code_of_conduct_builder]] | downstream | 0.56 |
| [[bld_instruction_code_of_conduct]] | downstream | 0.56 |
| [[p10_mem_code_of_conduct_builder]] | downstream | 0.50 |
| [[bld_examples_code_of_conduct]] | downstream | 0.50 |
| [[p05_qg_code_of_conduct]] | downstream | 0.46 |
| [[bld_output_template_code_of_conduct]] | downstream | 0.45 |
| [[bld_schema_code_of_conduct]] | downstream | 0.35 |
| [[bld_tools_code_of_conduct]] | downstream | 0.32 |
| [[bld_collaboration_code_of_conduct]] | downstream | 0.29 |
