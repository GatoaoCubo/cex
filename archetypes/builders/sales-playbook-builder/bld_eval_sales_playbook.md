---
kind: quality_gate
id: p03_qg_sales_playbook
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for sales_playbook
quality: 9.0
title: "Quality Gate Sales Playbook"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sales_playbook, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for sales_playbook"
domain: "sales_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_sales_playbook
  - sales-playbook-builder
  - bld_instruction_sales_playbook
  - p03_sp_sales_playbook_builder
  - p10_mem_sales_playbook_builder
  - kc_sales_playbook
  - bld_knowledge_card_sales_playbook
  - p05_qg_user_journey
  - discovery-questions-builder
  - p01_qg_discovery_questions
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| completeness | 100% | >= | all sections |
| alignment | strategy | 1:1 | company goals |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | invalid YAML |
| H02 | ID matches ^p03_sp_[a-z][a-z0-9_]+.md$ | invalid ID pattern |
| H03 | kind field matches 'sales_playbook' | incorrect kind |
| H04 | personas section present | missing personas |
| H05 | discovery flow structured | unstructured flow |
| H06 | objection handling strategies | missing strategies |
| H07 | close patterns documented | missing patterns |
| H08 | aligned with company strategy | misalignment detected |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Clarity | 0.15 | 1.0=concise/role-aligned, 0.5=vague |
| D02 | Completeness | 0.20 | 1.0=all sections, 0.7=minor gaps |
| D03 | Alignment | 0.15 | 1.0=matches GTM strategy, 0.5=misaligned |
| D04 | Practicality | 0.15 | 1.0=field-ready, 0.5=academic |
| D05 | Objection depth | 0.10 | 1.0=3+ rebuttals/category, 0.5=generic |
| D06 | Close effectiveness | 0.10 | 1.0=persona-specific patterns, 0.5=generic |
| D07 | Versioning | 0.05 | 1.0=versioned+changelog, 0.5=none |
| D08 | Stakeholder feedback | 0.10 | 1.0=peer-approved, 0.5=draft |

## Actions
| Score | Action |
|---|---|
| >=9.5 | GOLDEN |
| >=8.0 | PUBLISH |
| >=7.0 | REVIEW |
| <7.0 | REJECT |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| executive approval | CTO | documented |

## Examples

## Golden Example
**Frontmatter**:
```yaml
title: Sales Playbook for CRM Platform Implementation
target_account: Mid-market SaaS companies
created_by: Sales Enablement Team, Acme AI
last_updated: 2023-10-05
```
**Body**:
### Personas
- **Primary Buyer**: Marketing Director at a mid-sized e-commerce company (e.g., "A. Smith," 35, 8 years in digital marketing).
- **Influencer**: IT Manager concerned about data security (e.g., "J. Lee," 40, 12 years in enterprise tech).

### Discovery Flow
1. **Initial Contact**: Ask, "What’s your current CRM’s biggest pain point?"
2. **Needs Assessment**: Explore integration with existing tools and chat platforms.
3. **Solution Demo**: Highlight the platform’s automation and analytics.
4. **Negotiation**: Align pricing with ROI from lead generation improvements.

### Objection Handling
- **Objection**: "We’re happy with our current system."
  **Response**: "Let’s compare your current system’s lead conversion rate with our platform’s 30% improvement benchmark."

### Close Patterns
- **Time-Sensitive Offer**: "Our Q4 discount ends October 31 -- can we lock this in today?"
- **ROI Guarantee**: "If the platform doesn’t deliver 20% faster sales cycles, we’ll refund 50% of the first year’s cost."

## Anti-Example 1: Vague Personas
**Frontmatter**:
```yaml
title: Sales Playbook for "ProviderA"
target_account: "Any company"
created_by: "Sales Team"
```
**Body**:
### Personas
- **Primary Buyer**: "Someone in marketing who cares about efficiency."

### Discovery Flow
- "Ask them about their goals."

### Objection Handling
- "They say ‘no’? Try again later."

## Why it fails
Lacks specificity in personas, discovery steps, and objections. Sales reps can’t tailor approaches without concrete examples or strategies.

## Anti-Example 2: Missing Key Sections
**Frontmatter**:
```yaml
title: Sales Playbook for "ExampleModel"
target_account: Startups
created_by: "SomeVendor"
```
**Body**:
### Personas
- **Primary Buyer**: Startup founder (e.g., "R. Tanaka," 28, founder of a fintech startup).

### Discovery Flow
- "Discuss their product."

## Why it fails
Omits objection handling and close patterns, making the playbook incomplete. Sales teams can’t address common objections or apply proven closing techniques.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
