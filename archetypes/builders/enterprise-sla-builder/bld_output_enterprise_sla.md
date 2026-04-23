---
kind: output_template
id: bld_output_template_enterprise_sla
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for enterprise_sla production
quality: 8.7
title: "Output Template Enterprise Sla"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [enterprise_sla, builder, output_template]
tldr: "Template with vars for enterprise_sla production"
domain: "enterprise_sla construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_enterprise_sla
  - enterprise-sla-builder
  - bld_config_enterprise_sla
  - kc_enterprise_sla
  - bld_tools_enterprise_sla
  - p03_sp_enterprise_sla_builder
  - bld_examples_enterprise_sla
  - bld_knowledge_card_enterprise_sla
  - bld_instruction_enterprise_sla
  - bld_output_template_eval_metric
---

```yaml
---
id: p11_sla_{{service_name}}.md
name: {{service_name}}
pillar: P11
quality: null
version: {{version}}
description: {{SLA_description}}
scope: {{scope}}
service_level_objectives:
  - metric: {{metric_name}}
    target: {{target}}
    compliance: {{compliance}}
contact: {{contact_email}}
revision_history:
  - date: {{date}}
    changes: {{changes}}
---
```

<!-- id: p11_sla_[a-z][a-z0-9_]+.md -->
<!-- name: Service name (e.g., "enterprise_api") -->
<!-- pillar: Always "P11" -->
<!-- quality: Must be "null" -->
<!-- version: Semantic version (e.g., "1.0.0") -->
<!-- description: Brief SLA overview -->
<!-- scope: Targeted systems/regions -->
<!-- metric_name: Uptime, latency, etc. -->
<!-- target: 99.9%, <200ms, etc. -->
<!-- compliance: Monitoring tool/protocol -->
<!-- contact_email: SLA owner email -->
<!-- date: YYYY-MM-DD -->
<!-- changes: Summary of revisions -->

| Metric       | Target  | Compliance Tool |
|--------------|---------|-----------------|
| Uptime       | 99.9%   | Prometheus      |
| Latency      | <200ms  | Datadog         |
| Downtime     | 0h      | PagerDuty       |

```yaml
compliance_checks:
  - name: "Uptime Monitoring"
    tool: "Prometheus"
    threshold: "99.9%"
    alert: "page_on_99_5"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_enterprise_sla]] | downstream | 0.21 |
| [[enterprise-sla-builder]] | downstream | 0.20 |
| [[bld_config_enterprise_sla]] | downstream | 0.19 |
| [[kc_enterprise_sla]] | upstream | 0.19 |
| [[bld_tools_enterprise_sla]] | upstream | 0.19 |
| [[p03_sp_enterprise_sla_builder]] | upstream | 0.19 |
| [[bld_examples_enterprise_sla]] | downstream | 0.18 |
| [[bld_knowledge_card_enterprise_sla]] | upstream | 0.17 |
| [[bld_instruction_enterprise_sla]] | upstream | 0.17 |
| [[bld_output_template_eval_metric]] | sibling | 0.17 |
