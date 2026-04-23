---
kind: output_template
id: bld_output_template_churn_prevention_playbook
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for churn_prevention_playbook production
quality: 9.2
title: "Output Template Churn Prevention Playbook"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [churn_prevention_playbook, builder, output_template]
tldr: "Template with vars for churn_prevention_playbook production"
domain: "churn_prevention_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_churn_prevention_playbook
  - churn-prevention-playbook-builder
  - bld_examples_churn_prevention_playbook
  - bld_config_renewal_workflow
  - p03_qg_churn_prevention_playbook
  - p03_sp_churn_prevention_playbook_builder
  - bld_collaboration_churn_prevention_playbook
  - bld_output_template_renewal_workflow
  - bld_knowledge_card_churn_prevention_playbook
  - bld_instruction_renewal_workflow
---

```yaml
---
id: p03_cpp_{{name}}.md
kind: churn_prevention_playbook
pillar: P03
title: "Churn Prevention Playbook: {{segment}} -- {{trigger_event}}"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "churn_prevention_playbook construction"
quality: null
tags: [churn_prevention_playbook, {{segment_tag}}, {{trigger_tag}}]
tldr: "Playbook for detecting and saving at-risk {{segment}} accounts via {{primary_intervention}}"
target_user_segment: "{{segment}}"      # e.g., enterprise, mid-market, SMB
intervention_type: "{{intervention}}"   # e.g., csa_outreach, automated_email, exec_sponsor
risk_score: {{risk_score}}              # 0-100 churn risk at trigger
---

# Health Score Model
| Component       | Weight | Red Threshold | Yellow Threshold | Data Source     |
|-----------------|--------|---------------|------------------|-----------------|
| Product usage   | 0.30   | <20% WAU      | 20-50% WAU       | Product analytics|
| NPS score       | 0.25   | detractor (0-6)| passive (7-8)   | NPS survey      |
| Support tickets | 0.20   | >3 open P1    | >1 open P1       | Zendesk/Jira    |
| QBR engagement  | 0.15   | missed 2+     | missed 1         | Calendar/CRM    |
| Contract stage  | 0.10   | <60 days      | 60-90 days       | Salesforce      |

# Intervention Triggers
| Risk Band    | Health Score | Trigger Event                        | Owner           | SLA     |
|--------------|--------------|--------------------------------------|-----------------|---------|
| Red          | <40          | Immediate save-the-account outreach  | CSM + VP CS     | 24h     |
| Yellow       | 40-60        | Proactive health review call         | CSM             | 48h     |
| Pre-renewal  | Any          | Contract within {{renewal_days}} days| CSM Manager     | 72h     |

# Save-the-Account Script
## Opening
"{{opening_script}}"  # Acknowledge issue without blame, reference specific value delivered

## Discovery Questions
1. "{{discovery_q1}}"  # Identify root churn reason (product, budget, champion, competitor)
2. "{{discovery_q2}}"
3. "{{discovery_q3}}"

## Objection Handlers
| Objection           | Response Script                               |
|---------------------|-----------------------------------------------|
| Budget constraint   | "{{budget_objection_response}}"               |
| Product gap         | "{{product_objection_response}}"              |
| Competitor offer    | "{{competitor_objection_response}}"           |
| Champion departure  | "{{champion_objection_response}}"             |

## Close
"{{close_script}}"  # Define mutual success criteria and next step with date

# Win-Back Sequence (post-churn)
| Day  | Channel     | Message Theme                              | CTA                     |
|------|-------------|--------------------------------------------|-------------------------|
| 30   | Email + Call| Acknowledge, no pressure                   | Schedule 15-min call    |
| 60   | Email       | New value prop or feature since departure  | Request feedback        |
| 90   | Executive   | Final offer with decision authority        | Formal re-engagement    |

# Escalation Path
| Trigger                         | Escalate To         | SLA      | Method          |
|---------------------------------|---------------------|----------|-----------------|
| Save attempt failed (>2 tries)  | VP Customer Success | 24h      | Direct call     |
| ARR > {{high_value_threshold}}  | Executive sponsor   | Same day | Video call      |
| Champion departure              | CSM Manager         | 48h      | Email + Gainsight CTA|

# Gainsight CTA Configuration
playbook_name: "{{gainsight_playbook_name}}"
trigger_condition: "health_score < {{red_threshold}} OR days_since_login > {{inactivity_days}}"
assignee: "{{csm_role}}"
due_date_sla: "{{sla_days}} days"
success_criteria: "{{success_definition}}"  # e.g., renewal signed, health_score restored to >70
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_churn_prevention_playbook]] | upstream | 0.56 |
| [[churn-prevention-playbook-builder]] | upstream | 0.37 |
| [[bld_examples_churn_prevention_playbook]] | downstream | 0.36 |
| [[bld_config_renewal_workflow]] | downstream | 0.35 |
| [[p03_qg_churn_prevention_playbook]] | downstream | 0.35 |
| [[p03_sp_churn_prevention_playbook_builder]] | upstream | 0.35 |
| [[bld_collaboration_churn_prevention_playbook]] | downstream | 0.33 |
| [[bld_output_template_renewal_workflow]] | sibling | 0.31 |
| [[bld_knowledge_card_churn_prevention_playbook]] | upstream | 0.31 |
| [[bld_instruction_renewal_workflow]] | upstream | 0.29 |
