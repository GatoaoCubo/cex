---
lp: P01
llm_function: INJECT
purpose: Standards and industry knowledge for model_card production
sources: SHAKA(sonnet) + PYTHA-GEMINI(gemini-2.5-pro) + ATLAS-CODEX(codex) + EDISON(opus)
---

# Domain Knowledge: model_card

## Foundational Standard
Mitchell et al. 2019 "Model Cards for Model Reporting" (https://arxiv.org/abs/1810.03993)
Defines: model name, developers, intended use, limitations, ethical considerations.
947 unique section names across industry (AI Transparency Atlas 2024) = severe fragmentation.
CEX normalizes, does not invent.

## Industry Implementations

| Source | What it defines | CEX uses |
|--------|----------------|----------|
| HuggingFace Model Cards | YAML frontmatter + MD body, pipeline_tag, model-index, eval_results | Format pattern, eval schema |
| LiteLLM registry | 2593 models, capability booleans (supports_*), per-token pricing | Capability flags, pricing schema |
| Anthropic SDK ModelInfo | ModelCapabilities with typed booleans, context limits | Capability object design |
| LangChain ModelProfile | Modality booleans (text/image/audio), tool_calling flags | Feature coverage |
| Google Model Card Toolkit | Proto-based JSON schema, HTML rendering | Structural validation |
| OpenAI Model API | Minimal: id, created, owned_by | Baseline fields |

## Universal Fields (8+/10 providers)
model_name, provider, release_date, context_window, benchmarks, intended_use, architecture, official_url

## Frequent Fields (5-7/10)
parameters, safety, limitations, training_data, license, max_output, knowledge_cutoff

## Key Patterns (from code analysis)
- Separate IDENTITY (immutable) from CAPABILITIES (mutable) from ECONOMICS (volatile)
- Capabilities as explicit booleans, never prose
- Pricing normalized to per_1M_tokens for comparison
- Status lifecycle: active → deprecated → sunset
- Freshness gate: 90 days (pricing/features change quarterly)

## CEX-Extensions (justified gaps)
| Field | Justification | Closest industry equivalent |
|-------|--------------|---------------------------|
| status (active/deprecated/sunset) | Models deprecate; cards go stale | HF new_version, LiteLLM deprecation_date |
| fine_tunable (bool) | Routing decision: fine-tune vs prompt | Meta finetuning_recipe (narrative) |
| pricing.cache_read/write | Caching changes economics 10x | Not separated in LiteLLM |
| freshness gate (90d) | model_cards degrade 4x faster than KCs | No standard defines this |

## References
- https://arxiv.org/abs/1810.03993 (Mitchell 2019)
- https://huggingface.co/docs/hub/en/model-cards
- https://github.com/BerriAI/litellm (model registry)
- https://github.com/anthropics/anthropic-sdk-python (ModelCapabilities)
- https://arxiv.org/html/2512.12443 (AI Transparency Atlas)
