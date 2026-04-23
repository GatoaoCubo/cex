---
id: incident_report_n01
kind: incident_report
pillar: P11
nucleus: n01
title: "N01 Research Intelligence Incident Report Template"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.2
tags: [incident_report, research_failure, n01, post_mortem, quality_failure]
tldr: "Incident report template for N01 research quality failures: captures what went wrong, root cause, impact, and systematic fix. Filed when any research output scores < 7.0 or causes downstream harm."
density_score: 0.86
updated: "2026-04-17"
related:
  - bld_instruction_incident_report
  - incident-report-builder
  - bld_examples_incident_report
  - kc_incident_report
  - bld_knowledge_card_incident_report
  - bld_schema_incident_report
  - p01_kc_incident_response
  - bld_output_template_incident_report
  - bld_collaboration_incident_report
  - p03_sp_incident_report_builder
---

<!-- 8F: F1 constrain=P11/incident_report F2 become=incident-report-builder F3 inject=regression_check_n01+learning_record_n01+quality_gate_intelligence+eval_framework_n01 F4 reason=Analytical Envy demands we learn from failures -- an incident without a post-mortem is just accepted degradation F5 call=cex_compile F6 produce=incident_report_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P11_feedback/ -->

## Purpose

Research quality failures have consequences:
- Downstream decisions based on wrong competitive data
- N07 dispatching with incorrect intelligence
- Brand / commercial artifacts built on bad market analysis

This template documents failures systematically to:
1. Capture immediate remediation
2. Identify root cause
3. Prevent recurrence via pipeline improvements

## Incident Classification

| Severity | Condition | Response Time |
|----------|-----------|--------------|
| SEV-1 | False information published downstream | immediate fix |
| SEV-2 | Research score < 6.0 in any dimension | 24 hours |
| SEV-3 | Systematic bias detected after publication | 48 hours |
| SEV-4 | Process violation (skipped F7) | 72 hours |

## Incident Report Template

```markdown
---
incident_id: INC-N01-{YYYY}-{NNN}
severity: SEV-{1-4}
status: OPEN | INVESTIGATING | RESOLVED
detected_at: {ISO8601}
resolved_at: {ISO8601 or null}
reporter: {nucleus or human}
---

## Summary
One-sentence description of what failed.

## Impact
| Artifact Affected | Downstream Use | Users Impacted |
|-------------------|---------------|---------------|

## Timeline
| Time | Event |
|------|-------|
| T+0 | Failure first observable |
| T+N | Detected by regression_check / human |
| T+N | Investigation started |
| T+N | Temporary mitigation applied |
| T+N | Root cause identified |
| T+N | Permanent fix deployed |
| T+N | Incident closed |

## Root Cause Analysis

### Immediate Cause
What directly caused the failure?

### Contributing Factors
What conditions allowed this failure to occur?

### Why Not Caught Earlier
Which quality gate should have caught this?
Why did it fail?

## Evidence

| Finding | Source | Confidence |
|---------|--------|-----------|

## Remediation

### Immediate
Actions taken to stop the bleeding.

### Permanent
Pipeline changes to prevent recurrence.
| Change | Artifact Modified | Implementation Date |
|--------|------------------|-------------------|

## Lessons Learned
What should be updated in learning_record_n01.md?
```

## Incident Registry

| Incident ID | Severity | Status | Root Cause Category | Closed |
|-------------|---------|--------|---------------------|--------|
| INC-N01-2026-001 | SEV-3 | RESOLVED | B2 Confirmation bias (pre-formed hypothesis not rejected) | 2026-04-17 |

## Root Cause Categories

| Category | Description | Most Common Fix |
|----------|-------------|----------------|
| BIAS | One of B1-B5 bias types not caught | improve bias_audit thresholds |
| SOURCE | Incorrect or stale source used as truth | improve source validation |
| EXTRACTION | Data extractor hallucinated a field | add validation constraint |
| JUDGE | llm_judge missed hallucination | improve judge adversarial prompt |
| PROCESS | 8F step skipped | enforce in system_prompt |
| SCHEMA | Type mismatch in output | update sch_type_def validation |

## Integration

```
quality_gate_intelligence (F7 GOVERN):
  if any gate FAIL AND impact_detected:
    -> file incident_report_n01
    -> write to learning_record_n01
    -> optionally alert N07
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_incident_report]] | upstream | 0.33 |
| [[incident-report-builder]] | related | 0.32 |
| [[bld_examples_incident_report]] | upstream | 0.32 |
| [[kc_incident_report]] | upstream | 0.30 |
| [[bld_knowledge_card_incident_report]] | upstream | 0.28 |
| [[bld_schema_incident_report]] | upstream | 0.27 |
| [[p01_kc_incident_response]] | upstream | 0.26 |
| [[bld_output_template_incident_report]] | upstream | 0.25 |
| [[bld_collaboration_incident_report]] | downstream | 0.25 |
| [[p03_sp_incident_report_builder]] | upstream | 0.25 |
