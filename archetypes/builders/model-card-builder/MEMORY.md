---
lp: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: model-card-builder

## Accumulated Patterns (update after each production)

### Pricing Sources (verified URLs, refresh quarterly)
| Provider | Pricing URL | Last verified |
|----------|------------|---------------|
| Anthropic | https://docs.anthropic.com/en/docs/about-claude/pricing | 2026-03-26 |
| OpenAI | https://platform.openai.com/docs/pricing | — |
| Google | https://ai.google.dev/pricing | 2026-03-26 |
| Meta | N/A (open-weight, pricing: null) | — |
| Mistral | https://mistral.ai/technology/#pricing | — |

### Common Mistakes (learned from production)
1. Confusing context_window with max_output (context = input+output capacity)
2. Using "128K" (string) instead of 128000 (integer)
3. Forgetting cache pricing (changes economics 10x for Anthropic)
4. Marking open-weight models pricing as 0 instead of null
5. Putting model version in provider field ("anthropic-opus" instead of "anthropic")
6. Spec table Provider row with source `-` instead of URL (every row needs source)
7. Google tiered pricing: use base tier (<=200K), document higher in body
8. cache_write: null when provider has no symmetric write price (Google)

### Model Families (for linked_artifacts)
| Provider | Family | Models in CEX |
|----------|--------|---------------|
| Anthropic | Claude 4 | opus_4, sonnet_4, haiku_4 |
| OpenAI | GPT-4o | gpt_4o, gpt_4o_mini |
| Google | Gemini 2.5 | gemini_2_5_pro, gemini_2_5_flash |

### Production Counter
| Metric | Value |
|--------|-------|
| Cards produced | 1 (gemini_2_5_pro by CODEX) |
| Avg quality | pending validation |
| Common friction | tiered pricing, cache_write ambiguity |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a model_card, update:
- New verified pricing URL (if found)
- New common mistake (if encountered)
- New model family member (if produced)
- Production counter increment
