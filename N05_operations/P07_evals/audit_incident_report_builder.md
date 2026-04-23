---
id: n05_audit_incident_report_builder
kind: audit_report
pillar: P11
title: "Audit: incident-report-builder (13 ISOs)"
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: n05_ops
domain: security_operations
quality: 8.9
tags: [incident_report, audit, post-mortem, nist, sre, n05]
tldr: "8 pass, 4 fix, 1 rebuild -- primary gaps: output template had no post-mortem structure, quality gate weights summed to 1.10, config had max_turns=0"
related:
  - n01_hybrid_review_wave1
  - incident-report-builder
  - bld_knowledge_card_incident_report
  - hybrid_review7_n05
  - n01_audit_voice_pipeline_builder
  - n05_audit_threat_model_builder
  - p03_sp_incident_report_builder
  - bld_output_template_incident_report
  - bld_architecture_incident_report
  - hybrid_review7_n04
---

## Summary

| ISO | Score Before | Score After | Action |
|-----|-------------|------------|--------|
| bld_instruction_incident_report | 8.0 | 8.0 | PASS |
| bld_system_prompt_incident_report | 8.5 | 8.5 | PASS |
| bld_knowledge_card_incident_report | 8.5 | 8.5 | PASS |
| bld_quality_gate_incident_report | 6.5 | 9.0 | FIX: Weights fixed (1.10->1.00), 7 dims remain (merged D8 into D7), D3 raised to 0.25 (root cause is the most critical dimension) |
| bld_output_template_incident_report | 5.0 | 9.0 | REBUILD: Full NIST SP 800-61 lifecycle template with 5-Whys RCA, TTD/TTA/TTR metrics, regulatory notification matrix, signed attestation |
| bld_schema_incident_report | 8.0 | 8.0 | PASS |
| bld_examples_incident_report | 8.5 | 8.5 | PASS |
| bld_manifest_incident_report | 8.5 | 8.5 | PASS |
| bld_architecture_incident_report | 7.5 | 8.5 | FIX: Removed "trading" language, added NIST SP 800-61 lifecycle positioning and upstream/downstream builder relationships |
| bld_collaboration_incident_report | 8.0 | 8.0 | PASS |
| bld_config_incident_report | 7.0 | 8.5 | FIX: max_turns: 0 -> 5, effort_level: low -> medium, max_bytes: 5120 -> 8192 (incident reports are inherently large) |
| bld_memory_incident_report | 8.0 | 8.0 | PASS |
| bld_tools_incident_report | 7.5 | 8.5 | FIX: Added NIST SP 800-61, PagerDuty, Jira, Grafana references; kept Loguru |

**Total: 8 pass, 4 fixed, 1 rebuilt**

## Framework Coverage

| Framework | Referenced In | Citation Quality |
|-----------|--------------|-----------------|
| NIST SP 800-61 | knowledge_card, output_template, architecture, tools, system_prompt | Lifecycle phases in template |
| Google SRE Book | knowledge_card, output_template, system_prompt | 5-Whys methodology |
| ISO/IEC 25010 | knowledge_card | Standard name |
| IEEE 1220-2010 | knowledge_card | Standard name |
| ITIL | system_prompt, manifest | Framework name |
| ISO 22301 | manifest | Business continuity |
| GDPR Art. 33 | output_template | Breach notification requirement |

## Top 5 Security Gaps Found

1. **Output template had no post-mortem structure** -- every section was `{{placeholder}}`. A builder that produces placeholder-only output for incident reports is a compliance risk; reports could be filed incomplete.
2. **Quality gate weights summed to 1.10** -- would produce inflation of scores by 10%. Root cause analysis (D3) was underweighted at 0.20 given it is the primary value of a post-mortem. Raised to 0.25.
3. **config max_turns: 0** -- this would prevent the builder from iterating on the draft. Incident reports require multiple passes (timeline -> RCA -> actions -> review). Set to 5.
4. **No GDPR Art. 33 guidance** -- incident reports for personal data breaches must be filed with DPA within 72 hours. Output template now includes this regulatory notification section.
5. **No detection gap analysis section** -- TTD/TTA/TTR metrics are the primary learning output of SRE post-mortems and were completely absent from the original template.

## Recommendations

- Add a `severity_classification.md` knowledge card covering P1-P5 severity matrix with SLO impact thresholds
- Add hard gate H09: "For incidents involving personal data, GDPR Art. 33 notification section must be present"
- Consider creating `runbook` kind (P12) that incident reports can reference as corrective action targets

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n01_hybrid_review_wave1]] | sibling | 0.33 |
| [[incident-report-builder]] | related | 0.32 |
| [[bld_knowledge_card_incident_report]] | upstream | 0.29 |
| [[hybrid_review7_n05]] | upstream | 0.29 |
| [[n01_audit_voice_pipeline_builder]] | sibling | 0.26 |
| [[n05_audit_threat_model_builder]] | sibling | 0.26 |
| [[p03_sp_incident_report_builder]] | upstream | 0.25 |
| [[bld_output_template_incident_report]] | upstream | 0.25 |
| [[bld_architecture_incident_report]] | upstream | 0.23 |
| [[hybrid_review7_n04]] | upstream | 0.23 |
