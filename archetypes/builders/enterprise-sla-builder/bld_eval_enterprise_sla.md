---
kind: quality_gate
id: p11_qg_enterprise_sla
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for enterprise_sla
quality: 9.1
title: "Quality Gate Enterprise Sla"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [enterprise_sla, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for enterprise_sla"
domain: "enterprise_sla construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_enterprise_sla
  - p11_qg_audit_log
  - p10_qg_consolidation_policy
  - p10_qg_procedural_memory
  - bld_knowledge_card_enterprise_sla
  - p11_qg_white_label_config
  - p01_qg_faq_entry
  - p10_qg_memory_architecture
  - p04_qg_stt_provider
  - p05_qg_github_issue_template
---

## Quality Gate

## Definition
| metric             | threshold                         | operator | scope              |
|--------------------|-----------------------------------|----------|--------------------|
| artifact_id        | ^p11_sla_[a-z][a-z0-9_]+.md$     | matches  | all artifact files |

## HARD Gates
| ID  | Check                                    | Fail Condition                                        |
|-----|------------------------------------------|-------------------------------------------------------|
| H01 | YAML frontmatter valid                   | Invalid YAML syntax or missing required fields        |
| H02 | ID matches ^p11_sla_[a-z][a-z0-9_]+.md$ | ID does not conform to schema naming pattern          |
| H03 | kind field = 'enterprise_sla'            | kind field is absent or incorrect                     |
| H04 | service_level_objective field present    | service_level_objective missing or empty              |
| H05 | compliance_requirements field is a list  | compliance_requirements absent or not a list          |
| H06 | SLO section present in body              | Body lacks Service Level Objectives section           |
| H07 | Escalation Procedures section present    | Body lacks escalation procedures section              |
| H08 | quality field = null                     | quality is non-null (self-score violation)            |

## SOFT Scoring
| Dim | Dimension                   | Weight | Scoring Guide                                        |
|-----|-----------------------------|--------|------------------------------------------------------|
| D1  | SLO specificity             | 0.20   | 1.00=numeric SLO+credits+RPO/RTO, 0.50=numeric SLO only, 0.00=vague |
| D2  | Uptime math accuracy        | 0.15   | 1.00=both 99.9% and 99.99% with downtime minutes, 0.50=one tier, 0.00=absent |
| D3  | Error budget coverage       | 0.15   | 1.00=error budget + burn rate defined, 0.50=partial, 0.00=absent |
| D4  | Penalty and credit clauses  | 0.15   | 1.00=tiered credits with calculation formula, 0.50=flat credit, 0.00=absent |
| D5  | Standards citations         | 0.10   | 1.00=ITIL4+ISO20000+SRE cited, 0.50=one standard, 0.00=none |
| D6  | Escalation path depth       | 0.10   | 1.00=Tier1-3 with timelines, 0.50=partial, 0.00=absent |
| D7  | Completeness (all sections) | 0.15   | 1.00=all 5 body sections present, 0.50=3-4, 0.00=<3  |

## Actions
| Score      | Action                   |
|------------|--------------------------|
| GOLDEN     | Auto-publish             |
| PUBLISH    | Manual approval required |
| REVIEW     | Peer review required     |
| REJECT     | Reject and fix required  |

## Bypass
| conditions                          | approver       | audit trail              |
|------------------------------------|----------------|--------------------------|
| Critical production outage         | CTO            | Emergency bypass log     |
| Regulatory compliance override     | Legal team     | Compliance audit trail   |
| Temporary SLA exception            | SVP Operations | Exception approval log   |

## Examples

## Golden Example
```markdown
---
title: "AWS Enterprise SLA"
vendor: "Amazon Web Services, Inc."
effective_date: "2023-10-01"
---

**Uptime Commitment**
AWS guarantees 99.95% monthly uptime for EC2 instances in regions with multiple availability zones. Downtime exceeding this threshold triggers service credits (5% for 1–29 days, 10% for 30+ days).

**Latency SLA**
For AWS Global Accelerator, latency between 50ms and 150ms is guaranteed for 95% of requests in North America. Latency exceeding 150ms for >5% of requests incurs credits.

**Support Commitments**
24/7 enterprise support via phone, email, and chat. Critical issues (e.g., outages) must be resolved within 2 hours; non-critical issues within 24 hours.

**Penalties**
Service credits are issued automatically for breaches. No cap on credits for outages exceeding 30 days.
```

## Anti-Example 1: Missing Key Metrics
```markdown
---
title: "CloudCo Enterprise SLA"
vendor: "CloudCo Inc."
effective_date: "2023-09-15"
---

**Uptime Commitment**
We strive to provide reliable service.

**Support Commitments**
Our team will help you as best as possible.
```
## Why it fails
No quantifiable metrics (uptime, latency, response times) or penalties. Vague language makes enforcement impossible.

## Anti-Example 2: Vague Language
```markdown
---
title: "DataCorp SLA"
vendor: "DataCorp Solutions"
effective_date: "2023-08-01"
---

**Uptime Commitment**
High availability is guaranteed.

**Latency SLA**
Low latency is ensured for all users.

**Support Commitments**
Support is available when needed.
```
## Why it fails
Terms like "high availability" and "low latency" lack definitions or benchmarks. No clear accountability or remedies for failures.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
