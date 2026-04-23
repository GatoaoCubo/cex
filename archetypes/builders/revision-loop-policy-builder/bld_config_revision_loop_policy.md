---
id: p11_config_revision_loop_policy
kind: env_config
pillar: P11
llm_function: CONSTRAIN
purpose: P09 config knobs for revision_loop_policy builder
quality: 8.3
title: "Config: Revision Loop Policy Builder"
version: "1.0.0"
author: n03_hermes_w1_6
tags: [config, revision_loop_policy, builder, p11, governance]
domain: "revision_loop_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.87
related:
  - bld_collaboration_llm_evaluation_scenario
  - skill
  - brand_override_config
  - p02_bc_builder_nucleus
  - ex_env_config_default
  - p03_sp_env_config_builder
  - kind-builder
  - llm-evaluation-scenario-builder
  - bld_config_kind
  - n06_intent_resolution_depth_spec
---

## Builder Configuration

### Runtime Defaults

| Config Key | Default | Description |
|------------|---------|-------------|
| `RLP_MAX_ITERATIONS` | `3` | Global default for max revision cycles |
| `RLP_QUALITY_FLOOR` | `8.5` | Score below which revision triggers |
| `RLP_ESCALATION_TARGET` | `user` | Default escalation route |
| `RLP_PRIORITY_ORDER` | `security,quality,implementation` | Default conflict resolution order |
| `RLP_SECURITY_OVERRIDE` | `5` | max_iterations for security_critical scenario |
| `RLP_DOCS_OVERRIDE` | `2` | max_iterations for documentation scenario |

### Environment Variables

```bash
# Override defaults for all new revision_loop_policy artifacts
export RLP_MAX_ITERATIONS=3
export RLP_QUALITY_FLOOR=8.5
export RLP_ESCALATION_TARGET=user

# Headless pipeline mode (no user to escalate to)
export RLP_ESCALATION_TARGET=freeze
```

### Per-Scenario Override Table

| Scenario Key | Default | Description |
|-------------|---------|-------------|
| `security_critical` | 5 | High-stakes security artifacts |
| `documentation` | 2 | Knowledge cards, guides, READMEs |
| `standard` | 3 | All other artifact kinds |
| `experimental` | 1 | Fast-iteration prototypes |

### Quality Thresholds (CEX standards)

| Threshold | Value | When |
|-----------|-------|------|
| Floor (trigger revision) | 8.5 | Below this, a revision cycle starts |
| Publish minimum | 8.0 | CEX system floor (quality_gate) |
| Target | 9.0 | N03 inventive pride target |
| Excellence | 9.5+ | For showcased artifacts |

### Builder Execution Config

```yaml
builder_config:
  kind: revision_loop_policy
  pillar: P11
  max_bytes: 2048
  naming: "p11_rlp_{{name}}.yaml"
  compile_target: yaml
  validate_on_produce: true
  hard_gate_count: 6
  soft_gate_count: 4
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_llm_evaluation_scenario]] | downstream | 0.18 |
| [[skill]] | upstream | 0.17 |
| [[brand_override_config]] | sibling | 0.17 |
| [[p02_bc_builder_nucleus]] | upstream | 0.17 |
| [[ex_env_config_default]] | sibling | 0.17 |
| [[p03_sp_env_config_builder]] | upstream | 0.16 |
| [[kind-builder]] | upstream | 0.16 |
| [[llm-evaluation-scenario-builder]] | upstream | 0.16 |
| [[bld_config_kind]] | upstream | 0.15 |
| [[n06_intent_resolution_depth_spec]] | related | 0.15 |
