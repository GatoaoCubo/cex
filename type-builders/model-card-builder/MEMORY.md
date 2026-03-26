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
| Google | https://ai.google.dev/pricing | — |
| Meta | N/A (open-weight) | — |
| Mistral | https://mistral.ai/technology/#pricing | — |

### Common Mistakes (learned from production)
1. Confusing context_window with max_output (context = input capacity)
2. Using "128K" (string) instead of 128000 (integer)
3. Forgetting cache pricing (changes economics 10x for Anthropic)
4. Marking open-weight models pricing as 0 instead of null
5. Putting model version in provider field ("anthropic-opus" instead of "anthropic")

### Model Families (for linked_artifacts)
| Provider | Family | Models in CEX |
|----------|--------|---------------|
| Anthropic | Claude 4 | opus_4, sonnet_4, haiku_4 |
| OpenAI | GPT-4o | gpt_4o, gpt_4o_mini |
| Google | Gemini 2.5 | gemini_2_5_pro, gemini_2_5_flash |

### Production Counter
Track: how many model_cards produced, avg quality, common failures.
Use for: identifying patterns, improving INSTRUCTIONS, evolving QUALITY_GATES.

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a model_card, update this file with:
- New verified pricing URL (if found)
- New common mistake (if encountered)
- New model family member (if produced)
