---
id: p02_mc_claude_opus_4
kind: model_card
pillar: P02
model_name: claude-opus-4-6520
provider: anthropic
context_window: 200000
pricing:
  input: 15.00
  output: 75.00
  unit: per_1M_tokens
version: 1.0.0
created: 2026-03-24
author: orchestrator
domain: model_selection
quality: 9.0
tags: [model-card, opus, anthropic, pricing, capabilities]
updated: "2026-04-07"
title: "Model Card Claude Opus 4"
density_score: 0.92
tldr: "Defines model card for model card claude opus 4, with validation gates and integration points."
related:
  - p01_kc_claude_model_capabilities_2026
  - p12_dr_keyword_agent_group
  - self_audit_n03_builder_20260408
  - spec_infinite_bootstrap_loop
  - p02_mp_anthropic
  - token_efficiency_gap_map
  - bld_knowledge_card_effort_profile
  - output_sdk_validation_audit
  - n01_sdk_validation_self_audit
  - bld_examples_model_card
---

# Claude Opus 4 — Model Card

## Specifications
| Spec | Value |
|------|-------|
| Model | claude-opus-4-6520 |
| Provider | Anthropic |
| Context Window | 200K tokens |
| Max Output | 32K tokens |
| Input Price | $15.00 / 1M tokens |
| Output Price | $75.00 / 1M tokens |
| Extended Thinking | Supported (xhigh budget) |
| Tool Use | Full support |

## When to Use
| Scenario | Use Opus? |
|----------|-----------|
| Complex code generation/refactoring | YES |
| Architecture design and review | YES |
| Multi-file edits with dependencies | YES |
| Production deployment pipelines | YES |
| Simple text formatting or copy | NO (use haiku, 5% cost) |
| Research and analysis | NO (use sonnet, 25% cost) |

## organization Agent_group Mapping
1. **builder_agent** (build): opus — code complexity demands reasoning depth
2. **operations_agent** (execute): opus — deployment requires zero-error precision
3. **orchestrator** (orchestrate): opus — routing decisions affect all agent_groups
4. **research_agent/marketing_agent/knowledge_agent/commercial_agent**: sonnet — analysis tasks don't need opus

## Metadata

```yaml
id: p02_mc_claude_opus_4
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p02-mc-claude-opus-4.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_claude_model_capabilities_2026]] | upstream | 0.39 |
| [[p12_dr_keyword_agent_group]] | downstream | 0.39 |
| [[self_audit_n03_builder_20260408]] | upstream | 0.32 |
| [[spec_infinite_bootstrap_loop]] | related | 0.31 |
| [[p02_mp_anthropic]] | related | 0.31 |
| [[token_efficiency_gap_map]] | upstream | 0.31 |
| [[bld_knowledge_card_effort_profile]] | upstream | 0.30 |
| [[output_sdk_validation_audit]] | related | 0.29 |
| [[n01_sdk_validation_self_audit]] | downstream | 0.26 |
| [[bld_examples_model_card]] | downstream | 0.25 |
