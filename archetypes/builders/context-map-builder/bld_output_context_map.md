---
kind: output_template
id: bld_output_template_context_map
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a context_map artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 8.6
title: "Output Template Context Map"
version: "1.0.0"
author: n03_builder
tags: [context_map, builder, output_template]
tldr: "Fill-in template for context_map: BC inventory, relationships with DDD patterns, integration details, team coupling."
domain: "context map construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_schema_integration_guide
  - bld_schema_dual_loop_architecture
  - bld_output_template_rag_source
  - bld_schema_reranker_config
  - bld_schema_sandbox_spec
  - bld_schema_effort_profile
  - bld_schema_diff_strategy
  - bld_schema_safety_policy
  - bld_schema_benchmark_suite
  - bld_output_template_audio_tool
---

# Output Template: context_map

```yaml
id: p08_cm_{{system_slug}}
kind: context_map
pillar: P08
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
system_name: "{{human_friendly_system_name}}"
contexts_count: {{integer_count_of_BCs}}
quality: null
tags: [context_map, {{system_slug}}, {{domain_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```

## Bounded Contexts

| Context | Team | Core Domain? | Description |
|---------|------|-------------|-------------|
| {{ContextName1}} | {{TeamName1}} | {{YES|SUPPORTING|GENERIC}} | {{one_line_description}} |
| {{ContextName2}} | {{TeamName2}} | {{YES|SUPPORTING|GENERIC}} | {{one_line_description}} |

## Relationships

| Upstream (U) | Downstream (D) | Pattern | Integration Type | Notes |
|-------------|----------------|---------|-----------------|-------|
| {{ContextA}} | {{ContextB}} | {{ACL|OHS|Conformist|Partnership|Shared_Kernel|Customer_Supplier}} | {{sync|async|batch}} | {{brief_note}} |

## Integration Details

| Relationship | Translation Layer | Protocol | Sync/Async |
|-------------|-----------------|----------|-----------|
| {{ContextA}} -> {{ContextB}} {{Pattern}} | {{layer_name_or_none}} | {{REST|Kafka|gRPC|EventBus}} | {{sync|async}} |

## Team Coupling

| Relationship | Coupling Level | Risk | Mitigation |
|-------------|----------------|------|-----------|
| {{ContextA}} -> {{ContextB}} ({{Pattern}}) | {{Low|Medium|High|Very High}} | {{risk_description}} | {{mitigation_strategy}} |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | downstream | 0.22 |
| [[bld_schema_dual_loop_architecture]] | downstream | 0.20 |
| [[bld_output_template_rag_source]] | sibling | 0.20 |
| [[bld_schema_reranker_config]] | downstream | 0.19 |
| [[bld_schema_sandbox_spec]] | downstream | 0.19 |
| [[bld_schema_effort_profile]] | downstream | 0.19 |
| [[bld_schema_diff_strategy]] | downstream | 0.18 |
| [[bld_schema_safety_policy]] | downstream | 0.18 |
| [[bld_schema_benchmark_suite]] | downstream | 0.18 |
| [[bld_output_template_audio_tool]] | sibling | 0.18 |
