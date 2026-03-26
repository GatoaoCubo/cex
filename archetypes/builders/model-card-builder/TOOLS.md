---
lp: P04
llm_function: CALL
purpose: Tools and APIs available for model_card production
---

# Tools: model-card-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing model_cards in pool | Phase 1 (check duplicates) | ACTIVE |
| validate_kc.py | Validate KC artifacts (reference pattern) | — | ACTIVE (KC only) |
| validate_artifact.py | Validate any artifact type via builder gates | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources (APIs)
| Source | URL | Data |
|--------|-----|------|
| Anthropic docs | https://docs.anthropic.com/en/docs/about-claude/models | Claude models specs |
| Anthropic pricing | https://docs.anthropic.com/en/docs/about-claude/pricing | Claude pricing |
| OpenAI docs | https://platform.openai.com/docs/models | GPT models specs |
| OpenAI pricing | https://platform.openai.com/docs/pricing | GPT pricing |
| Google AI | https://ai.google.dev/gemini-api/docs/models | Gemini specs |
| Google pricing | https://ai.google.dev/pricing | Gemini pricing |
| LiteLLM registry | https://github.com/BerriAI/litellm | 2593 models JSON |
| HuggingFace API | https://huggingface.co/api/models/{id} | Model metadata |

## Interim Validation (until validate_artifact.py exists)
Manually check each QUALITY_GATES.md gate against produced artifact.
All 10 HARD gates must pass. SOFT gates contribute to score.
