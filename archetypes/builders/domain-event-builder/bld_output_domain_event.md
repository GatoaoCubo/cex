---
id: bld_tpl_domain_event
kind: prompt_template
pillar: P03
llm_function: PRODUCE
version: 1.0.0
quality: 8.1
tags: [domain_event, template, output]
title: "Output Template: domain_event"
author: builder
tldr: "Domain Event prompt: output template, formatting rules, and structure"
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_output_template_webhook
  - bld_knowledge_card_context_doc
  - bld_output_template_memory_type
  - p03_ch_kc_to_notebooklm
  - p01_kc_signal
  - bld_collaboration_context_doc
  - kc_model_context_protocol
  - bld_output_template_validation_schema
  - p03_sp_signal_builder
  - bld_output_template_function_def
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

## Output Template Checklist

- Verify output format matches target kind schema
- Validate all frontmatter fields are present in template
- Cross-reference with eval gate for completeness
- Test template rendering with sample data before publishing

## Output Pattern

```yaml
# Output validation
format_match: true
frontmatter_complete: true
eval_gate_aligned: true
sample_rendered: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_webhook]] | downstream | 0.27 |
| [[bld_knowledge_card_context_doc]] | upstream | 0.20 |
| [[bld_output_template_memory_type]] | downstream | 0.18 |
| [[p03_ch_kc_to_notebooklm]] | related | 0.17 |
| [[p01_kc_signal]] | downstream | 0.17 |
| [[bld_collaboration_context_doc]] | downstream | 0.17 |
| [[kc_model_context_protocol]] | upstream | 0.16 |
| [[bld_output_template_validation_schema]] | downstream | 0.16 |
| [[p03_sp_signal_builder]] | related | 0.16 |
| [[bld_output_template_function_def]] | downstream | 0.16 |
