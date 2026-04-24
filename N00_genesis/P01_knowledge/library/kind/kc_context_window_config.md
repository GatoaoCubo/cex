---
id: p01_kc_context_window_config
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P03
title: "Context Window Config — Deep Knowledge for context_window_config"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n04_knowledge
domain: context_window_config
quality: 9.1
tags: [context_window_config, P03, CONSTRAIN, kind-kc]
tldr: "context_window_config defines token budget allocation, priority tiers, and overflow rules for assembling LLM prompts within a model's context window limit."
when_to_use: "Building, reviewing, or reasoning about context_window_config artifacts"
keywords: [context_window, token_budget, priority, overflow, truncation, prompt_assembly]
feeds_kinds: [context_window_config]
density_score: null
related:
  - bld_knowledge_card_context_window_config
  - context-window-config-builder
  - p03_sp_context_window_config_builder
  - bld_collaboration_context_window_config
  - bld_output_template_context_window_config
  - p10_lr_context_window_config_builder
  - bld_instruction_context_window_config
  - p01_kc_token_budgeting
  - p01_kc_model_card
  - bld_architecture_context_window_config
---

# Context Window Config

## Spec
```yaml
kind: context_window_config
pillar: P03
llm_function: CONSTRAIN
max_bytes: 2048
naming: p03_cwc_{{model}}.yaml
core: true
```

## What It Is
A context_window_config is the budget allocation spec for fitting prompt components into a model's finite context window — defining total token limit, per-section budgets (system prompt, few-shot examples, retrieved context, user query, output reserve), priority tiers for overflow truncation, and compression fallbacks. It is NOT a prompt_template (P03, which defines content structure), NOT a system_prompt (P03, which defines agent identity), NOT a model_card (P02, which describes model capabilities).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| OpenAI | `max_tokens`, `max_completion_tokens` | Output budget; input managed by caller |
| Anthropic | 200K/1M context, `max_tokens` output | Large windows reduce overflow pressure |
| LangChain | `ConversationTokenBufferMemory` | Auto-truncates history to fit token limit |
| LlamaIndex | `PromptHelper(context_window, num_output)` | Budget allocation for retrieval + synthesis |
| CrewAI | `max_rpm`, `max_tokens` in agent config | Per-agent token limits |
| DSPy | `max_tokens` in LM config | Output cap; input assembly is manual |
| Haystack | `PromptBuilder` with token counting | Template-based assembly with limits |
| cex_sdk | `cex_token_budget.py` | Token counting + budget allocation across ISOs |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| total_tokens | int | model-dependent | Hard ceiling from model; cannot exceed |
| system_prompt_budget | int | 2000 | Higher = richer identity but less room for context |
| few_shot_budget | int | 3000 | More examples = better calibration but costly |
| retrieved_context_budget | int | 8000 | More RAG context = better grounding but more noise |
| user_query_budget | int | 1000 | Usually small; long queries rare |
| output_reserve | int | 4000 | Must reserve enough for complete response |
| overflow_strategy | enum | truncate_lowest | truncate_lowest/compress/drop_section |
| priority_tiers | list | [system, query, context, examples] | Order of protection during overflow |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Fixed allocation | Predictable prompt structure | system=2K, context=8K, output=4K |
| Dynamic scaling | Variable-length retrieval results | context gets remaining after fixed sections |
| Priority truncation | Context exceeds budget | Drop lowest-priority tier first (examples before system) |
| Compression fallback | All tiers needed but over budget | Summarize retrieved context before injection |
| Model-specific profiles | Different models, different limits | opus=200K profile, haiku=200K profile, gpt4=128K profile |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No output reserve | Model truncates response mid-sentence | Always reserve ≥2000 tokens for output |
| Equal budgets | System prompt and examples get same allocation | Priority-based: protect system > query > context |
| Ignore model limit | Assemble 300K tokens for 128K model | Profile per model; validate before API call |
| Static budget for dynamic content | Fixed 8K for retrieval that varies 2-20K | Dynamic allocation: context = total - fixed - reserve |

## Integration Graph
```
model_card, system_prompt --> [context_window_config] --> prompt_template, agent_card
                                       |
                                 few_shot_example, retriever_config, token_budget
```

## Decision Tree
- IF model has >100K context THEN generous budgets, less overflow pressure
- IF model has <32K context THEN tight budgets, aggressive priority truncation
- IF RAG-heavy workflow THEN prioritize retrieved_context_budget (50%+ of total)
- IF few-shot critical THEN protect examples budget above context
- DEFAULT: system=10%, examples=15%, context=40%, query=5%, output=30%

## Quality Criteria
- GOOD: total_tokens, per-section budgets, overflow_strategy, priority_tiers all present
- GREAT: model-specific profiles, compression fallback defined, validation hook
- FAIL: no output reserve, no overflow strategy, budgets exceed total

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_context_window_config]] | sibling | 0.56 |
| [[context-window-config-builder]] | related | 0.49 |
| [[p03_sp_context_window_config_builder]] | related | 0.42 |
| [[bld_collaboration_context_window_config]] | downstream | 0.40 |
| [[bld_output_template_context_window_config]] | downstream | 0.40 |
| [[p10_lr_context_window_config_builder]] | downstream | 0.37 |
| [[bld_instruction_context_window_config]] | related | 0.34 |
| [[p01_kc_token_budgeting]] | sibling | 0.34 |
| [[p01_kc_model_card]] | sibling | 0.33 |
| [[bld_architecture_context_window_config]] | downstream | 0.33 |
