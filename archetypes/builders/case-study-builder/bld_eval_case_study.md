---
kind: quality_gate
id: p05_qg_case_study
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for case_study
quality: 9.0
title: "Quality Gate Case Study"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [case_study, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for case_study artifacts"
domain: "case_study construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_case_study
  - bld_knowledge_card_case_study
  - bld_schema_case_study
  - bld_instruction_case_study
  - p10_mem_case_study_builder
  - p03_sp_case_study_builder
  - case-study-builder
  - bld_tools_case_study
  - bld_output_template_case_study
  - p11_qg_audit_log
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|--------|-----------|----------|-------|
| ID pattern | ^p05_cs_[a-z][a-z0-9_]+\\.md$ | matches | all case_study files |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | invalid YAML syntax |
| H02 | ID matches pattern ^p05_cs_[a-z][a-z0-9_]+\\.md$ | ID does not match pattern |
| H03 | kind field equals "case_study" | kind != "case_study" |
| H04 | Challenge section present (150+ words) | missing or < 100 words |
| H05 | Solution section present with named product features | missing or generic "our product" |
| H06 | Outcome section present with 3+ KPIs | fewer than 3 measurable KPIs |
| H07 | Pullquote present with champion name and title | anonymous or missing quote |
| H08 | ROI call-out present with headline metric and source | no ROI metric or unverified claim |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Narrative structure | 0.20 | Clear Challenge->Solution->Outcome arc with transitions = 1.0 |
| D2 | Metric specificity | 0.20 | Before/after comparison with % or absolute numbers = 1.0; vague = 0.0 |
| D3 | Pullquote quality | 0.15 | Direct, attributed, emotionally resonant = 1.0; generic = 0.5 |
| D4 | Data verification | 0.15 | Metrics approved by customer = 1.0; unverified = 0.0 |
| D5 | Clarity | 0.15 | Plain language, no jargon without context = 1.0 |
| D6 | Completeness | 0.15 | All 6 sections: Snapshot/Challenge/Solution/Outcome/ROI/Lessons = 1.0 |

## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | Highlight as exemplar |
| >= 8.0 | Deploy to public repo |
| >= 7.0 | Request minor edits |
| < 7.0 | Discard, rework required |

## Bypass
| conditions | approver | audit trail |
|------------|----------|-------------|
| Strategic customer reference with legal deadline | CTO | Note in audit log with customer name and deadline |

## Examples

## Golden Example  
**Title:** Scaling Telemedicine with Cloud Infrastructure: An Example Corp Case Study  
**Author:** A. Smith, Content Strategist  
**Date:** October 2023  

**Challenge**  
Example Corp, a telemedicine platform serving 2 million users, faced scalability issues during peak hours. Their on-premise infrastructure could not handle surges in traffic, leading to 30% system downtime and frustrated users.  

**Solution**  
They migrated to a cloud provider, leveraging auto-scaling compute, serverless functions, and a managed NoSQL database. This allowed dynamic resource allocation and reduced infrastructure management overhead.  

**Outcome**  
After migration, downtime dropped to 2%, and costs decreased by 50%. The platform scaled to 5 million users within 6 months.  

**Quote**  
"Moving to the cloud transformed our operations. We now handle traffic spikes effortlessly." -- J. Lee, CTO, Example Corp  

## Anti-Example 1: Missing Narrative Structure  
**Challenge**  
"CompanyX had a problem."  

**Solution**  
"They used ToolY to fix it."  

**Why it fails**  
Lacks depth in challenge/solution/outcome. No specific metrics, quotes, or context. Reads like a bullet point list, not a story.  

## Anti-Example 2: Generic Vendors and Names  
**Challenge**  
"ProviderA helped ClientB solve a generic issue with their ExampleModel."  

**Solution**  
"They deployed a generic solution using unspecified tools."  

**Outcome**  
"ClientB saw some improvements."  

**Quote**  
"ProviderA was great." – Anonymous  

**Why it fails**  
Uses placeholder names and vague language. No real-world details, making the case study unconvincing and unactionable.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
