---
id: p02_mc_claude_opus_4
type: model_card
lp: P02
model_name: claude-opus-4-0520
provider: anthropic
context_window: 200000
pricing:
  input: 15.00
  output: 75.00
  unit: per_1M_tokens
version: 1.0.0
created: 2026-03-24
author: STELLA
domain: model_selection
quality: 9.0
tags: [model-card, opus, anthropic, pricing, capabilities]
---

# Claude Opus 4 — Model Card

## Specifications
| Spec | Value |
|------|-------|
| Model | claude-opus-4-0520 |
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

## CODEXA Satellite Mapping
- **EDISON** (build): opus — code complexity demands reasoning depth
- **ATLAS** (execute): opus — deployment requires zero-error precision
- **STELLA** (orchestrate): opus — routing decisions affect all satellites
- **SHAKA/LILY/PYTHA/YORK**: sonnet — analysis tasks don't need opus
