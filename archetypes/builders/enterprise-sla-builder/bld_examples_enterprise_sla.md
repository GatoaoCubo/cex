---
kind: examples
id: bld_examples_enterprise_sla
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of enterprise_sla artifacts
quality: 8.9
title: "Examples Enterprise Sla"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [enterprise_sla, builder, examples]
tldr: "Golden and anti-examples of enterprise_sla artifacts"
domain: "enterprise_sla construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

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
