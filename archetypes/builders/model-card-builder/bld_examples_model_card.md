---
kind: examples
id: bld_examples_model_card
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of model_card artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: model-card-builder
## Golden Example
INPUT: "Documenta o Claude Sonnet 4 pra decidir roteamento"
OUTPUT:
```yaml
id: p02_mc_anthropic_sonnet_4
kind: model_card
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
model_name: "claude-sonnet-4-20250514"
provider: "anthropic"
model_type: "text-generation"
status: "active"
release_date: "2025-05-14"
knowledge_cutoff: "2025-04"
context_window: 200000
max_output: 16000
modalities:
  text_input: true
  text_output: true
  image_input: true
  audio_input: false
  pdf_input: true
features:
  tool_calling: true
  structured_output: true
  reasoning: true
  prompt_caching: true
  code_execution: true
  web_search: false
  fine_tunable: false
  batch_api: true
pricing:
  input: 3.00
  output: 15.00
  cache_read: 0.30
  cache_write: 3.75
  unit: per_1M_tokens
domain: model_selection
quality: null
tags: [model-card, anthropic, claude-4, sonnet, balanced]
tldr: "Sonnet 4 — anthropic, 200K ctx, $3/$15 per 1M, melhor custo-beneficio analise/pesquisa"
when_to_use: "Analise e pesquisa onde opus eh overkill e haiku insuficiente"
keywords: [anthropic, claude-sonnet-4, balanced]
linked_artifacts:
  primary: null
  related: [p02_mc_anthropic_opus_4]
data_source: "https://docs.anthropic.com/en/docs/about-claude/models"
## Boundary
model_card EH: spec tecnica do Sonnet 4 (capacidades, custos, limites).
model_card NAO EH: boot_config, agent, benchmark.
## Specifications
| Spec | Value | Source |
|------|-------|--------|
| Model | claude-sonnet-4-20250514 | https://docs.anthropic.com/en/docs/about-claude/models |
| Context | 200K tokens | https://docs.anthropic.com/en/docs/about-claude/models |
| Max Output | 16K tokens | https://docs.anthropic.com/en/docs/about-claude/models |
| Cutoff | Apr 2025 | https://docs.anthropic.com/en/docs/about-claude/models |
| Pricing (input) | $3.00 per 1M | https://docs.anthropic.com/en/docs/about-claude/pricing |
| Pricing (output) | $15.00 per 1M | https://docs.anthropic.com/en/docs/about-claude/pricing |
## Capabilities
| Capability | Supported | Notes |
|------------|-----------|-------|
| Tool Calling | true | parallel supported |
| Structured Output | true | JSON mode |
| Reasoning | true | budget-controlled |
| Prompt Caching | true | 0.1x read cost |
| Code Execution | true | sandbox |
| Web Search | false | — |
| Fine Tuning | false | — |
| Batch API | true | 50% discount |
## When to Use
| Scenario | Sonnet? | Alternative |
|----------|---------|-------------|
| Research + analysis | YES | — |
| Complex architecture, multi-file refactor | NO | Opus ($15/$75) |
| Simple classification, formatting | NO | Haiku ($0.25/$1.25) |
| Vision: PDF/image analysis | YES | — |
| High-volume batch processing | YES | 50% discount via Batch API |
## References
- source: https://docs.anthropic.com/en/docs/about-claude/models
- pricing: https://docs.anthropic.com/en/docs/about-claude/pricing
```
WHY THIS IS GOLDEN:
- Every Spec row has Source URL (never `-`)
- Capabilities: 8 rows, all booleans
- Pricing: concrete, base tier, per_1M_tokens
- quality: null
- When to Use: 5 rows with concrete alternatives and pricing
- Frontmatter strings quoted consistently
## Anti-Example
INPUT: "Documenta o GPT-4"
BAD OUTPUT:
```yaml
id: gpt4_card
kind: model_card
model_name: GPT-4
provider: OpenAI
context_window: "128K"
quality: 9.5
tags: "gpt, openai"
GPT-4 is a powerful model by OpenAI. It can do many things.
Pricing varies by usage tier. Contact OpenAI for details.
```
FAILURES:
1. id: no `p02_mc_` prefix, no provider in id → H02 FAIL
2. provider: uppercase → H08 FAIL
3. context_window: string not integer → H09 FAIL
4. quality: self-assigned 9.5 → H06 FAIL
5. tags: string not list → S02 FAIL
6. lp: missing → H05 FAIL
7. features: missing entirely → S05 FAIL
8. pricing: "varies" → S03 FAIL
