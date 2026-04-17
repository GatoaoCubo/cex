---
kind: output_template
id: bld_output_template_team_charter
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for team_charter production
quality: 9.1
title: "Output Template Team Charter"
version: "1.0.0"
author: n06_wave8
tags: [team_charter, builder, output_template, governance]
tldr: "Template with vars for team_charter production"
domain: "team_charter construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
---
id: p12_tc_{{mission_slug}}_v1.md
kind: team_charter
pillar: P12
title: "Team Charter: {{mission_name}}"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
quality: null
tags: [team_charter, {{mission_slug}}, governance]
tldr: "Mission contract for {{mission_name}} crew"
domain: "{{domain}}"
charter_id: "{{charter_id}}"
crew_template_ref: "{{crew_template_path}}"
mission_statement: "{{mission_statement}}"
deadline: "{{deadline_iso8601}}"
---

## Mission Statement
{{mission_statement}}

## Deliverables
| # | Kind | Pillar Path | Owner Nucleus | Due |
|---|------|-------------|---------------|-----|
| 1 | {{kind_1}} | {{path_1}} | {{nucleus_1}} | {{deadline_1}} |
| 2 | {{kind_2}} | {{path_2}} | {{nucleus_2}} | {{deadline_2}} |

## Success Metrics (OKR)
**Objective**: {{objective}}

| Key Result | Threshold | Metric Type | Owner |
|------------|-----------|-------------|-------|
| {{kr_1}} | {{threshold_1}} | {{type_1}} | {{owner_1}} |
| {{kr_2}} | {{threshold_2}} | {{type_2}} | {{owner_2}} |
| {{kr_3}} | {{threshold_3}} | {{type_3}} | {{owner_3}} |

## Budget
| Resource | Allocated | Hard Ceiling | Notes |
|----------|-----------|--------------|-------|
| Tokens | {{tokens_allocated}} | {{tokens_ceiling}} | Per nucleus total |
| Time (hours) | {{time_hours}} | {{time_ceiling_hours}} | Wall-clock |
| Cost (USD) | ${{cost_usd}} | ${{cost_ceiling_usd}} | API + infra |

## Stakeholders (RACI)
| Role | Identity | R | A | C | I |
|------|----------|---|---|---|---|
| Orchestrator | N07 | - | X | - | - |
| {{role_2}} | {{identity_2}} | X | - | - | - |
| {{role_3}} | {{identity_3}} | - | - | X | - |
| User / Sponsor | {{user_id}} | - | X | - | X |

## Quality Gate
| Level | Threshold | Action |
|-------|-----------|--------|
| Floor | 8.0 | Block publish; trigger escalation |
| Target | 9.0 | Auto-publish |
| Golden | 9.5 | Promote to gold example library |

## Escalation Protocol
| Trigger | Condition | Action | Escalation Target |
|---------|-----------|--------|-------------------|
| Score below floor | score < 8.0 | Retry F6 (max 2x) then escalate | N07 |
| Timeout | wall_clock > {{time_ceiling_hours}}h | Terminate + report partial | User |
| Budget exceeded | cost_usd > ${{cost_ceiling_usd}} | Pause + notify | User |
| GDP conflict | manifest contradicts charter | Halt + re-run GDP | User |

## Termination Criteria
| Condition | Trigger | State |
|-----------|---------|-------|
| SUCCESS | All deliverables at >= quality floor, all Key Results met | COMPLETE |
| FAILURE | 2 consecutive retries below floor, or any HARD gate blocked | FAILED |
| TIMEOUT | `deadline_iso8601` reached with < 80% deliverables complete | EXPIRED |
```
