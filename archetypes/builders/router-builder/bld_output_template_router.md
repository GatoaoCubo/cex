---
kind: output_template
id: bld_output_template_router
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a router artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: router
```yaml
id: p02_router_{{router_slug}}
kind: router
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
routes_count: {{integer_matching_table}}
fallback_route: "{{default_destination}}"
confidence_threshold: {{0.0_to_1.0}}
domain: "{{routing_domain}}"
quality: null
tags: [router, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
timeout_ms: {{integer_ms}}
retry_count: {{integer}}
load_balance: "{{round_robin|weighted|priority|none}}"
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]
density_score: {{0.80_to_1.00}}
```
## Routes
| Pattern | Destination | Priority | Confidence Min | Conditions |
|---------|-------------|----------|----------------|------------|
| {{pattern_1}} | {{destination_1}} | {{1-100}} | {{0.0-1.0}} | {{conditions_or_dash}} |
| {{pattern_2}} | {{destination_2}} | {{1-100}} | {{0.0-1.0}} | {{conditions_or_dash}} |
## Decision Logic
Algorithm: {{priority_first|confidence_weighted|load_balanced}}
Tie-breaking: {{highest_priority|most_specific_pattern|round_robin}}
Evaluation order: {{sequential_top_down|parallel_all_then_rank}}
## Fallback
Default destination: {{fallback_route}}
Trigger: no route matches above confidence_threshold
Behavior: {{route_to_fallback|queue_for_review|escalate}}
## Escalation
Trigger: {{ambiguous_match_description}}
Action: {{escalation_action}}
Notification: {{signal_type_or_none}}
## Integration
- Receives from: {{upstream_source}}
- Routes to: {{downstream_destinations}}
- Consults: {{dispatch_rules_or_model_cards}}
- Signal on failure: {{signal_type}}
## References
- {{reference_1}}
- {{reference_2}}
