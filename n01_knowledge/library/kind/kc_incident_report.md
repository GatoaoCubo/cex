---
id: kc_incident_report
kind: knowledge_card
title: Incident Report
version: 1.0.0
quality: null
pillar: P01
---

# Incident Report

## Purpose
Standardized documentation for AI system incidents, including technical analysis, root cause identification, and corrective actions.

## Key Components
- **Incident Summary**: Date, time, affected systems, severity level
- **Technical Analysis**: System logs, error codes, latency metrics
- **Root Cause**: Causal factors (algorithmic bias, data corruption, infrastructure failure)
- **Impact Assessment**: User impact, business risk, compliance violations
- **Corrective Actions**: Immediate fixes, preventive measures, process improvements
- **Owner Responsibility**: Assigning accountability for resolution

## Example
```
DATE: 2023-10-15
TIME: 14:32 UTC
SYSTEM: AI Moderation Engine
SEVERITY: Critical

ERROR CODE: MOD-404-777
LATENCY: 920ms (threshold: 500ms)

ROOT CAUSE: Data corruption in training dataset (duplicate entries)
IMPACT: 12% false positive rate in content filtering
ACTION: Re-train model with deduplicated dataset (completed 2023-10-18)
OWNER: Data Science Team
```
```