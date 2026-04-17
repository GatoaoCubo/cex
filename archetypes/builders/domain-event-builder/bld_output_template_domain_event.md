---
id: bld_tpl_domain_event
kind: prompt_template
pillar: P03
llm_function: PRODUCE
version: 1.0.0
quality: 6.2
tags: [domain_event, template, output]
title: "Output Template: domain_event"
density_score: 1.0
updated: "2026-04-17"
---
# Output Template: domain_event
```markdown
---
id: de_{{aggregate_snake}}_{{verb_past_tense}}
kind: domain_event
pillar: P12
title: "{{EventNamePastTense}}"
version: 1.0.0
quality: null
aggregate_root: {{AggregateClassName}}
bounded_context: {{context_name}}
event_version: v1
occurred_at: "{{YYYY-MM-DDTHH:MM:SSZ}}"
causation_id: "{{causation_uuid_or_null}}"
correlation_id: "{{saga_or_trace_id_or_null}}"
tags: [{{aggregate}}, {{context}}, domain-event]
---

# {{EventNamePastTense}}

## What Happened
{{One sentence: what domain fact this event records.}}

## Payload
| Field | Type | Value at Occurrence |
|-------|------|---------------------|
| {{field_1}} | {{type}} | {{example_value}} |
| {{field_2}} | {{type}} | {{example_value}} |

## Causal Chain
- Command/trigger: {{what_caused_this_event}}
- causation_id: {{uuid}}
- correlation_id: {{saga_id}}

## Consumers
| Bounded Context | Reaction |
|----------------|----------|
| {{context_name}} | {{what_it_does_with_event}} |

## Invariants
- {{business_rule_this_event_enforces}}
```
