---
kind: knowledge_card
id: bld_knowledge_card_enterprise_sla
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for enterprise_sla production
quality: 9.2
title: "Knowledge Card Enterprise Sla"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [enterprise_sla, builder, knowledge_card]
tldr: "Domain knowledge for enterprise_sla production"
domain: "enterprise_sla construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - enterprise-sla-builder
  - p03_sp_enterprise_sla_builder
  - bld_tools_enterprise_sla
  - p10_mem_enterprise_sla_builder
  - bld_examples_enterprise_sla
  - bld_collaboration_enterprise_sla
  - kc_enterprise_sla
  - bld_instruction_enterprise_sla
  - bld_output_template_enterprise_sla
  - p11_qg_enterprise_sla
---

## Domain Overview  
Enterprise SLAs (Service Level Agreements) define contractual obligations between service providers and consumers, ensuring alignment on performance, availability, and support expectations. They are critical in cloud computing, SaaS, and IT outsourcing, where downtime, latency, and response times directly impact business operations. SLAs typically include metrics like uptime percentages (e.g., 99.9%), latency thresholds (e.g., <100ms), and support SLAs (e.g., 24/7 escalation paths). These agreements balance accountability with flexibility, often incorporating service credits or penalties for non-compliance.  

SLAs differ from quality gates (runtime monitoring) and compliance checklists (audit-focused) by focusing on pre-defined contractual commitments rather than runtime validation or regulatory adherence. They require clear definitions of success, measurable KPIs, and mechanisms for dispute resolution. Industry leaders like AWS, Azure, and Salesforce use SLAs to manage customer expectations and operational risks.  

## Key Concepts  
| Concept               | Definition                                                                 | Source                          |  
|----------------------|----------------------------------------------------------------------------|---------------------------------|  
| Uptime SLA           | Percentage of time a service must be operational (e.g., 99.95%).           | ITIL 4                          |  
| Latency SLA          | Maximum allowable response time for critical operations (e.g., <100ms).   | RFC 7348 (HTTP/2)               |  
| Service Credits      | Financial compensation for SLA breaches (e.g., 10% credit per downtime hour). | ISO/IEC 20000-1:2018            |  
| Support SLA          | Guaranteed response/resolution times for incidents (e.g., 15-minute SLA). | ITIL 4                          |  
| SLA Breach         | Failure to meet defined metrics, triggering remedies.                      | Gartner SLA Best Practices      |  
| SLA Monitoring       | Automated tools to track compliance (e.g., Datadog, New Relic).           | DevOps Handbook                 |  
| SLA Renegotiation    | Process to update terms as business needs evolve.                          | IEEE 1220-2005                  |  
| SLA Escalation Path  | Defined steps for resolving breaches (e.g., Tier 1 → Tier 3 support).     | ISO/IEC 20000-1:2018            |  

## Industry Standards  
- ITIL 4 (Service Management Framework)  
- ISO/IEC 20000-1:2018 (IT Service Management)  
- RFC 7348 (HTTP/2 Latency Considerations)  
- Gartner "SLA Best Practices for Cloud Providers" (2022)  
- IEEE 1220-2005 (Service Level Agreements for IT Services)  
- SLA Templates from AWS, Azure, and Salesforce  

## Uptime Math (MUST include in every enterprise_sla)  
| Uptime % | Monthly Downtime | Annual Downtime | Typical Tier |  
|----------|------------------|-----------------|--------------|  
| 99.0%    | 7h 18m           | 3d 15h          | Basic        |  
| 99.5%    | 3h 39m           | 1d 19h          | Standard     |  
| 99.9%    | 43m 50s          | 8h 45m          | Production   |  
| 99.95%   | 21m 55s          | 4h 22m          | Business     |  
| 99.99%   | 4m 22s           | 52m 34s         | Enterprise   |  
| 99.999%  | 26s              | 5m 15s          | Mission-critical |  

## Error Budget (Google SRE Model)  
Error budget = 1 - SLO target. Example: 99.9% SLO = 0.1% error budget = 43.8 min/month.  
- **Burn rate**: ratio of error budget consumed vs. time elapsed. Burn rate > 1 = on pace to exhaust budget.  
- **Alert threshold**: page at 2% budget consumed in 1h (burn rate 14.4x), ticket at 5% in 6h (burn rate 6x).  
- **Budget exhaustion**: triggers freeze on non-critical releases until budget resets.  

## RPO / RTO Definitions  
| Term | Definition | Typical Enterprise Values |  
|------|-----------|---------------------------|  
| RTO (Recovery Time Objective) | Max acceptable downtime before service resumes | Tier 1: 15min, Tier 2: 4h, Tier 3: 24h |  
| RPO (Recovery Point Objective) | Max acceptable data loss window | Tier 1: 0min (sync replication), Tier 2: 1h, Tier 3: 24h |  

## Common Patterns  
1. Define uptime as a percentage with monthly calculation windows (include actual downtime minutes, not just %).  
2. Use tiered latency thresholds per service tier: gold (<50ms p99), silver (<150ms p99), bronze (<300ms p99).  
3. Specify support SLAs with escalation timelines (P0: 15min response/1h resolution, P1: 1h/4h, P2: 4h/24h).  
4. Include service credits proportional to breach severity (e.g., 10% monthly fee per hour over threshold).  
5. Define error budget explicitly and link to release freeze policy.  
6. Specify both RTO and RPO for each service tier.  
7. Align SLA with SLI (Service Level Indicator) definitions for objective measurement.  

## Pitfalls  
- Vague metrics (e.g., "high availability" without a defined percentage and downtime calculation).  
- Missing error budget and burn-rate alerting (SLO without error budget is unenforceable at scale).  
- Omitting RPO/RTO, leaving disaster recovery obligations undefined.  
- Ignoring breach remedies, leading to unresolved disputes.  
- Overcomplicating SLAs with excessive clauses, reducing enforceability.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[enterprise-sla-builder]] | downstream | 0.60 |
| [[p03_sp_enterprise_sla_builder]] | downstream | 0.54 |
| [[bld_tools_enterprise_sla]] | downstream | 0.42 |
| [[p10_mem_enterprise_sla_builder]] | downstream | 0.41 |
| [[bld_examples_enterprise_sla]] | downstream | 0.40 |
| [[bld_collaboration_enterprise_sla]] | downstream | 0.39 |
| [[kc_enterprise_sla]] | sibling | 0.39 |
| [[bld_instruction_enterprise_sla]] | downstream | 0.36 |
| [[bld_output_template_enterprise_sla]] | downstream | 0.26 |
| [[p11_qg_enterprise_sla]] | downstream | 0.25 |
