---
id: kc_usage_report
kind: knowledge_card
title: Usage Analytics Report Specification
version: 1.0.0
quality: 8.7
pillar: P01
density_score: 1.0
related:
  - usage-report-builder
  - bld_instruction_usage_report
  - bld_collaboration_usage_report
  - bld_knowledge_card_usage_report
  - p03_sp_usage_report_builder
  - bld_tools_usage_report
  - p10_mem_usage_report_builder
  - bld_config_usage_report
  - kc_usage_quota
  - kc_system_prompt
---

# Usage Analytics Report Specification

## Purpose
Standardized format for billing and CFO dashboards showing system resource utilization patterns.

## Structure
1. **Overview** (10% of report)
2. **Key Metrics** (40% of report)
3. **Trend Analysis** (30% of report)
4. **Anomaly Detection** (15% of report)
5. **Recommendations** (5% of report)

## Data Points
- User activity metrics (login frequency, session duration)
- API call volume by endpoint
- Storage utilization trends
- CPU/memory usage patterns
- Error rate statistics
- Feature adoption rates
- Geographic usage distribution

## Formatting
- Use tables for quantitative data
- Include time-series charts for trend analysis
- Highlight anomalies with color-coding
- Add contextual notes for irregular patterns
- Maintain consistent date formatting (YYYY-MM-DD)

## Usage Guidelines
- Update monthly for recurring subscriptions
- Generate quarterly summaries for CFO analysis
- Include system health indicators in technical reports
- Annotate seasonal variations in usage patterns
- Flag potential fraud patterns for audit review

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[usage-report-builder]] | downstream | 0.37 |
| [[bld_instruction_usage_report]] | downstream | 0.31 |
| [[bld_collaboration_usage_report]] | downstream | 0.25 |
| [[bld_knowledge_card_usage_report]] | sibling | 0.24 |
| [[p03_sp_usage_report_builder]] | downstream | 0.23 |
| [[bld_tools_usage_report]] | downstream | 0.23 |
| [[p10_mem_usage_report_builder]] | downstream | 0.22 |
| [[bld_config_usage_report]] | downstream | 0.22 |
| [[kc_usage_quota]] | sibling | 0.20 |
| [[kc_system_prompt]] | sibling | 0.20 |
