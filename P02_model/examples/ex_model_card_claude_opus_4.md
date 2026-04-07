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
