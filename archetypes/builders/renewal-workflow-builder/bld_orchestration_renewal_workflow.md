---
kind: collaboration
id: bld_collaboration_renewal_workflow
pillar: P12
llm_function: COLLABORATE
purpose: How renewal_workflow-builder works in crews with other builders
quality: 9.0
title: "Collaboration Renewal Workflow"
version: "1.0.0"
author: wave6_n06
tags: [renewal_workflow, builder, collaboration, renewal, GRR, CSM, Gainsight]
tldr: "How renewal_workflow-builder works in crews with other builders"
domain: "renewal_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p12_sp_renewal_workflow_builder
  - bld_knowledge_card_renewal_workflow
  - renewal-workflow-builder
  - bld_output_template_renewal_workflow
  - bld_examples_renewal_workflow
  - bld_config_renewal_workflow
  - bld_instruction_renewal_workflow
  - bld_tools_renewal_workflow
  - bld_architecture_renewal_workflow
  - bld_collaboration_churn_prevention_playbook
---

## Crew Role
Designs and automates renewal stage workflows that protect existing ARR, coordinating CSM outreach, pricing negotiations, and contract close within the 90/60/30-day renewal cadence.

## Receives From
| Builder / Source         | What                              | Format        |
|--------------------------|-----------------------------------|---------------|
| CRM (Salesforce)         | Contract end dates, ARR, PO data  | JSON/API      |
| CS Platform (Gainsight)  | Health scores, CTA triggers       | JSON/API      |
| Legal                    | Contract amendment templates      | DOCX/PDF      |
| Finance (CFO team)       | Price escalation authority matrix | Spreadsheet   |
| expansion_play-builder   | Expansion context for multi-year  | YAML          |

## Produces For
| Consumer / Builder       | What                              | Format        |
|--------------------------|-----------------------------------|---------------|
| CSM (Customer Success)   | Renewal stage tasks, email templates| Markdown    |
| RevOps                   | GRR model, renewal forecast       | YAML/CSV      |
| CRM (Salesforce)         | Renewal Opportunity stage updates | JSON/API      |
| Gainsight                | CTA configuration blueprints      | YAML/JSON     |
| Legal                    | Contract amendment checklist      | Markdown      |
| CFO / Finance            | GRR scenario report               | CSV/Dashboard |

## Boundary
Does NOT handle expansion plays (expansion_play) -- renewal protects existing ARR, expansion grows it. Does NOT handle churn intervention (churn_prevention_playbook) -- workflows for accounts with health score <40 belong there. Legal enforcement of contract terms and compliance litigation are handled by the Legal team, not this builder.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_sp_renewal_workflow_builder]] | related | 0.52 |
| [[bld_knowledge_card_renewal_workflow]] | upstream | 0.48 |
| [[renewal-workflow-builder]] | related | 0.48 |
| [[bld_output_template_renewal_workflow]] | upstream | 0.43 |
| [[bld_examples_renewal_workflow]] | upstream | 0.40 |
| [[bld_config_renewal_workflow]] | upstream | 0.39 |
| [[bld_instruction_renewal_workflow]] | upstream | 0.39 |
| [[bld_tools_renewal_workflow]] | upstream | 0.39 |
| [[bld_architecture_renewal_workflow]] | upstream | 0.36 |
| [[bld_collaboration_churn_prevention_playbook]] | sibling | 0.35 |
