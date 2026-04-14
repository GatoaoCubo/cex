---
id: kc_usage_report
kind: knowledge_card
title: Usage Analytics Report
version: 1.0.0
quality: null
pillar: P01
---

# Usage Analytics Report Specification

## Purpose
Define standardized metrics and formatting for billing and CFO dashboards

## Core Metrics
- Monthly active users (MAU)
- Daily active users (DAU)
- Revenue per user (RPU)
- Churn rate
- Session duration
- Feature adoption rate

## Formatting Guidelines
- Use USD currency format
- Display 2 decimal places
- Include 7-day rolling averages
- Highlight anomalies > 20% deviation

## Dashboard Requirements
1. Top 5 revenue-generating features
2. User growth trends (30/60/90 day)
3. Regional usage distribution
4. Peak usage times (hourly)
5. Billing cycle performance

## Data Sources
- Production analytics database
- Billing system API
- User activity logs

## Update Frequency
- Daily for metrics
- Weekly for dashboards
- Monthly for trend analysis

## Security
- Access restricted to finance team
- Data anonymized for reporting
- Compliance with GDPR/CCPA
