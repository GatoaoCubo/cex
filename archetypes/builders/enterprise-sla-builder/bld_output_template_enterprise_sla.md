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
