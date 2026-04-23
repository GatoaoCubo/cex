---
kind: config
id: bld_config_guardrail
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for guardrail production
pattern: CONFIG restricts SCHEMA, never contradicts
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Guardrail"
version: "1.0.0"
author: n03_builder
tags: [guardrail, builder, examples]
tldr: "Golden and anti-examples for guardrail construction, demonstrating ideal structure and common pitfalls."
domain: "guardrail construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_guardrail
  - bld_config_quality_gate
  - bld_tools_guardrail
  - p10_lr_guardrail_builder
  - bld_output_template_guardrail
  - bld_instruction_guardrail
  - bld_config_input_schema
  - bld_config_env_config
  - p11_qg_guardrail
  - guardrail-builder
---
# Config: guardrail Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p11_gr_{scope_slug}.md | p11_gr_destructive_commands.md |
| Builder dir | kebab-case | guardrail-builder/ |
| Fields | snake_case | bypass_approver, applies_to |
Rule: id MUST equal filename stem.
## File Paths
1. Output: cex/P11_feedback/examples/p11_gr_{scope_slug}.md
2. Compiled: cex/P11_feedback/compiled/p11_gr_{scope_slug}.yaml
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Density: >= 0.80
## Severity-Enforcement Matrix
| Severity | Default enforcement | Bypass allowed |
|----------|-------------------|----------------|
| critical | block | Yes, orchestrator only |
| high | block | Yes, agent_group chief |
| medium | warn | Yes, any senior agent |
| low | log | Yes, any agent |

## Metadata

```yaml
id: bld_config_guardrail
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-guardrail.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_guardrail]] | upstream | 0.51 |
| [[bld_config_quality_gate]] | sibling | 0.36 |
| [[bld_tools_guardrail]] | upstream | 0.36 |
| [[p10_lr_guardrail_builder]] | downstream | 0.34 |
| [[bld_output_template_guardrail]] | upstream | 0.34 |
| [[bld_instruction_guardrail]] | upstream | 0.33 |
| [[bld_config_input_schema]] | sibling | 0.32 |
| [[bld_config_env_config]] | sibling | 0.31 |
| [[p11_qg_guardrail]] | downstream | 0.31 |
| [[guardrail-builder]] | downstream | 0.30 |
