---
lp: P04
llm_function: CALL
purpose: Tools and APIs available for model_card production
---

# Tools: model-card-builder

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| validate_kc.py | Validate artifact structure | Phase 3 (post-production) |
| brain_query | Search existing model_cards in pool | Phase 1 (check if exists) |
| cex_forge.py | Generate artifact from seeds | Alternative to manual compose |

## Data Sources (APIs)
| Source | URL | Data |
|--------|-----|------|
| Anthropic docs | https://docs.anthropic.com/en/docs/about-claude/models | Claude models pricing+specs |
| OpenAI docs | https://platform.openai.com/docs/models | GPT models specs |
| Google AI | https://ai.google.dev/gemini-api/docs/models | Gemini models specs |
| LiteLLM registry | https://github.com/BerriAI/litellm | 2593 models pricing JSON |
| HuggingFace API | https://huggingface.co/api/models/{id} | Model metadata YAML |

## Validation Tools
| Tool | Gate | Auto? |
|------|------|-------|
| YAML parser | frontmatter valid | yes |
| id == stem check | naming compliance | yes |
| pricing != null | concrete data | yes |
| capabilities = bool | no prose in flags | yes |
