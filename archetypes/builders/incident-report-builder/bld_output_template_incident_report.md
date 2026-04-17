---
kind: output_template
id: bld_output_template_incident_report
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for incident_report production
quality: 9.2
title: "Output Template Incident Report"
version: "1.1.0"
author: n05_ops
tags: [incident_report, builder, output_template, post-mortem, nist, sre]
tldr: "Blameless post-mortem template with 5-Whys RCA, NIST SP 800-61 phases, and SRE severity tiers"
domain: "incident_report construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

```yaml
id: p11_ir_{{incident_id}}
kind: incident_report
pillar: P11
title: "Incident Report: {{incident_title}}"
version: "1.0.0"
created: "{{datetime_iso8601}}"
updated: "{{datetime_iso8601}}"
author: "{{incident_commander}}"
domain: "{{affected_system}}"
quality: null
incident_date: "{{datetime_iso8601}}"
impact_summary: "{{one_sentence_impact}}"
resolution_status: "{{open|closed|investigating}}"
tags: [{{severity_p1_to_p5}}, {{affected_domain}}, post-mortem]
tldr: "{{one_sentence_summary_of_incident_and_resolution}}"
```

## 1. Executive Summary

**Severity:** P{{1-5}} ({{Critical|High|Medium|Low|Informational}})
**Duration:** `{{start_datetime}}` - {{end_datetime}} (`{{total_duration}}`)
**Incident Commander:** {{name}}
**Affected Systems:** `{{comma_separated_systems}}`
**Customer Impact:** `{{number_of_users_affected}}` users affected; `{{service_disruption_description}}`

> {{2-3 sentence plain language summary of what happened, impact, and current status}}

## 2. Timeline (NIST SP 800-61 Phases)

| Timestamp (UTC) | Phase | Event | Actor | Evidence |
|-----------------|-------|-------|-------|----------|
| `{{datetime}}` | Detection | {{event_description}} | {{system_or_person}} | Log: `{{log_ref}}` |
| `{{datetime}}` | Analysis | {{event_description}} | {{person}} | Ticket: `{{ticket_id}}` |
| `{{datetime}}` | Containment | {{event_description}} | {{person}} | Runbook: `{{runbook_ref}}` |
| `{{datetime}}` | Eradication | {{event_description}} | {{person}} | Commit: `{{commit_sha}}` |
| `{{datetime}}` | Recovery | {{event_description}} | {{person}} | Monitor: `{{dashboard_url}}` |
| `{{datetime}}` | Post-Incident | This report created | `{{author}}` | - |

## 3. Impact Assessment

### User Impact
- **Affected users:** `{{count}}`
- **Degraded functionality:** `{{description}}`
- **Data integrity:** {{intact|compromised|under_investigation}}

### Business Impact
- **Downtime cost:** $`{{estimated_cost}}` (`{{calculation_basis}}`)
- **SLO breach:** {{yes|no}} -- `{{slo_details}}`
- **Regulatory exposure:** {{none|GDPR Art. 33|HIPAA Breach|other}}

### Technical Impact
- **Systems affected:** `{{list}}`
- **Data affected:** `{{records_count}}` records of type `{{data_type}}`
- **Dependencies broken:** `{{downstream_services}}`

## 4. Root Cause Analysis

### Method: 5 Whys (Google SRE)

1. **Why did `{{observable_failure}}` occur?**
   Because `{{reason_1}}`.

2. **Why did `{{reason_1}}` occur?**
   Because `{{reason_2}}`.

3. **Why did `{{reason_2}}` occur?**
   Because `{{reason_3}}`.

4. **Why did `{{reason_3}}` occur?**
   Because `{{reason_4}}`.

5. **Why did `{{reason_4}}` occur?**
   Because `{{root_cause}}` -- THIS IS THE ROOT CAUSE.

### Contributing Factors
| Factor | Category | Description |
|--------|----------|-------------|
| `{{factor}}` | Technical/Process/Human/Environmental | `{{description}}` |

### Not Root Cause (ruled out)
- `{{hypothesis_1}}`: `{{why_ruled_out}}`

## 5. Detection Gap Analysis

**Time to Detect (TTD):** `{{duration}}`
**Time to Acknowledge (TTA):** `{{duration}}`
**Time to Resolve (TTR):** `{{duration}}`

Was this detected by:
- [ ] Automated monitoring alert
- [ ] User report
- [ ] Manual inspection
- [ ] External disclosure

Gap: `{{what_monitoring_or_process_should_have_caught_this_sooner}}`

## 6. Containment, Eradication, and Recovery

### Containment Actions
| Action | Taken By | Time | Effect |
|--------|---------|------|--------|
| `{{action}}` | {{person}} | {{datetime}} | `{{outcome}}` |

### Eradication
`{{description_of_permanent_fix_applied}}`

### Recovery Validation
- [ ] Service restored and monitored for `{{duration}}`
- [ ] No recurrence in `{{observation_window}}`
- [ ] Stakeholders notified of resolution

## 7. Action Items (Corrective and Preventive)

| ID | Action | Owner | Due Date | Priority | Status |
|----|--------|-------|----------|----------|--------|
| A01 | `{{action}}` | {{team}} | `{{date}}` | P1/P2/P3 | Open |
| A02 | `{{action}}` | {{team}} | `{{date}}` | P1/P2/P3 | Open |

## 8. Lessons Learned

**What went well:**
- `{{positive_1}}`

**What could be improved:**
- `{{improvement_1}}`

**Systemic gaps identified:**
- `{{gap_1}}` -- maps to action A`{{id}}`

## 9. Notifications and Regulatory Obligations

| Stakeholder | Notified At | Method | Required By |
|-------------|------------|--------|-------------|
| Engineering leadership | `{{datetime}}` | Slack | Internal SLA |
| Customers (if applicable) | `{{datetime}}` | Status page | SLA / GDPR Art. 34 |
| DPA (if personal data breach) | Within 72h of discovery | Formal report | GDPR Art. 33 |

## 10. Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Incident Commander | {{name}} | `{{signature}}` | `{{date}}` |
| Engineering Lead | {{name}} | `{{signature}}` | `{{date}}` |
| Compliance Officer | {{name}} | `{{signature}}` | `{{date}}` |

## References

- NIST SP 800-61 Rev. 2: Computer Security Incident Handling Guide
- Google SRE Book: Chapter 14 -- Managing Incidents
- ISO/IEC 27035: Information Security Incident Management
- ITIL 4: Incident Management Practice Guide
