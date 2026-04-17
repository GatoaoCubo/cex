---
kind: collaboration
id: bld_collaboration_churn_prevention_playbook
pillar: P12
llm_function: COLLABORATE
purpose: How churn_prevention_playbook-builder works in crews with other builders
quality: 8.9
title: "Collaboration Churn Prevention Playbook"
version: "1.0.0"
author: n05_wave6
tags: [churn_prevention_playbook, builder, collaboration]
tldr: "How churn_prevention_playbook-builder works in crews with other builders"
domain: "churn_prevention_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role
Produces churn intervention playbooks for CS teams. Acts as the retention strategy layer
between health score monitoring and renewal workflow execution.

## Receives From
| Source                  | What                                    | Format   |
|-------------------------|-----------------------------------------|----------|
| nps_survey kind         | Detractor score + follow-up text        | JSON     |
| Gainsight / ChurnZero   | Health score drop alerts, CTA triggers  | JSON     |
| cohort_analysis (N01)   | At-risk cohort definitions              | CSV      |
| customer_segment kind   | ICP attributes (tier, ARR, tenure)      | YAML     |

## Produces For
| Consumer                | What                                    | Format   |
|-------------------------|-----------------------------------------|----------|
| CSM (direct use)        | Save-the-account script + call guide    | Markdown |
| Gainsight               | CTA trigger config + playbook steps     | YAML     |
| renewal_workflow kind   | Save outcome status (saved/churned)     | JSON     |
| content_monetization N06| Win-back offer parameters               | Markdown |

## Boundary
Does NOT handle:
- Renewal contract execution -> renewal_workflow kind
- Upsell/expansion plays -> expansion_play kind
- NPS survey configuration -> nps_survey kind
- Customer cohort analysis -> cohort_analysis kind (N01)
