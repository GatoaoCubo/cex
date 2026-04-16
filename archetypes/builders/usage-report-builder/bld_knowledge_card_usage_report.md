---
kind: knowledge_card
id: bld_knowledge_card_usage_report
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for usage_report production
quality: 9.2
title: "Knowledge Card Usage Report"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_report, builder, knowledge_card]
tldr: "Domain knowledge for usage_report production"
domain: "usage_report construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Domain Overview  
Usage reports are critical for SaaS and cloud providers to track resource consumption, enabling accurate billing, capacity planning, and compliance. These reports aggregate telemetry data on API calls, compute hours, storage usage, and network traffic, often aligned with metering frameworks like OpenStack Telemetry or Microsoft Azure’s usage analytics. CFOs rely on these metrics to forecast revenue, optimize infrastructure spending, and identify underutilized services. Regulatory requirements (e.g., GDPR, SOC 2) further mandate transparency in usage tracking to ensure data governance and audit readiness.  

## Key Concepts  
| Concept              | Definition                                                                 | Source                                  |  
|----------------------|----------------------------------------------------------------------------|-----------------------------------------|  
| Metering             | Quantification of resource consumption for billing and analytics          | OpenStack Telemetry (2010)             |  
| Usage Metrics        | Numerical indicators of service consumption (e.g., API requests/hour)     | ITIL 4 (2017)                          |  
| Billable Usage       | Usage data directly tied to invoicing (e.g., compute hours)               | OMB Circular A-123 (2020)              |  
| Resource Utilization | Percentage of allocated resources consumed (CPU, memory, storage)        | ISO/IEC 20000-1 (2018)                 |  
| Usage Events         | Logs of user actions triggering resource consumption (e.g., file uploads) | W3C Usage Statistics (2019)            |  
| Quota Exceeded       | Threshold violation alerting (e.g., storage limits)                       | Kubernetes API (2021)                  |  
| Usage Aggregation    | Consolidation of raw data into time-based intervals (hourly, daily)      | ELK Stack Documentation (2022)         |  
| Time Granularity     | Resolution of time intervals in usage reports (e.g., 1-minute increments) | RFC 7280 (2014)                        |  
| Normalization        | Conversion of raw usage data into standardized units (e.g., GB to TB)    | IEEE 1471 (2000)                       |  
| Data Retention       | Policy for storing usage records (e.g., 7 years for audit compliance)    | GDPR Article 30 (2018)                 |  

## Industry Standards  
- OpenStack Telemetry (2010)  
- ITIL 4 (2017)  
- OMB Circular A-123 (2020)  
- ISO/IEC 20000-1 (2018)  
- W3C Usage Statistics (2019)  
- Kubernetes API (2021)  
- RFC 7280 (2014)  
- IEEE 1471 (2000)  
- GDPR Article 30 (2018)  
- ELK Stack Documentation (2022)  

## Showback vs. Chargeback  
Critical distinction for enterprise billing and FinOps alignment:  

| Model | Definition | Who Pays | Use Case |  
|-------|-----------|----------|----------|  
| **Showback** | Usage visibility only -- teams see what they consume but are not billed internally | Central IT / Finance | Cost awareness, optimization culture |  
| **Chargeback** | Internal billing -- departments are invoiced for actual consumption | Each business unit | Cost accountability, P&L per team |  
| **Hybrid** | Showback for new services, chargeback for mature services | Mixed | Gradual FinOps maturity rollout |  

- Every usage_report artifact must declare `billing_model: showback | chargeback | hybrid`.  
- Chargeback reports require: department_id, cost_center, allocation_rule, invoice_period.  
- Showback reports require: team_id, resource_label, consumption_summary.  

## Department Allocation Rules  
| Rule Type | Logic | Example |  
|-----------|-------|---------|  
| Proportional | Allocate cost by % of total usage | Team A used 40% of API calls -> 40% of total cost |  
| Fixed quota | Pre-allocated budget per department | Marketing: $5,000/mo cap |  
| Actual metered | Bill exactly what was consumed | Per-API-call billing at $0.001/call |  
| Tiered commitment | Volume discount at thresholds | >1M calls/mo = $0.0008/call |  

## Data Export Integrations (MUST reference in usage_report)  
| Platform | Use Case | Config Key |  
|----------|----------|------------|  
| Snowflake Data Share | Cross-org data access without copying | `snowflake_share_name` |  
| Databricks Delta Lake | Usage data lakehouse for analytics | `databricks_table_path` |  
| Metabase | Self-serve CFO/manager dashboards | `metabase_dashboard_id` |  
| Looker | Embedded analytics for enterprise portals | `looker_explore_url` |  
| CSV export | Manual reporting, audit submissions | `csv_export_enabled: true` |  

## Common Patterns  
1. Time-based aggregation with ISO 8601 intervals (hourly, daily, monthly).  
2. Normalization to standard units: requests -> thousands, bytes -> GB, seconds -> hours.  
3. Multi-dimensional filtering: user_id, team_id, region, service_name, cost_center.  
4. Anomaly detection for outlier usage patterns (>2 standard deviations = flag).  
5. Hierarchical rollup: per-user -> per-team -> per-department -> organization-wide.  
6. Showback vs. chargeback mode declared explicitly in report metadata.  
7. Data share to Snowflake/Databricks for cross-org FinOps integration.  

## Pitfalls  
- Conflating showback and chargeback -- each has different authorization and approval flows.  
- Over-aggregation leading to loss of actionable per-team detail.  
- Inconsistent time zone handling across global users (always store in UTC, display in local).  
- Missing allocation_rule for chargeback (causes finance disputes at month-end).  
- No CSV export option (audit teams always need raw data access).
