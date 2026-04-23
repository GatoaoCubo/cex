---
kind: quality_gate
id: p11_qg_model_card
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of model_card artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: Model Card"
version: "1.0.0"
author: builder_agent
tags: [quality-gate, model-card, llm-spec, P02, provider]
tldr: "Quality gate for model_card artifacts: enforces provider, context window, pricing, and capabilities fields."
domain: model_card
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.85
related:
  - p11_qg_model_provider
  - p11_qg_embedder_provider
  - p11_qg_mental_model
  - p11_qg_learning_record
  - p03_ins_model_card
  - p11_qg_quality_gate
  - p11_qg_boot_config
  - p11_qg_vector_store
  - p11_qg_law
  - p11_qg_creation_artifacts
---

## Quality Gate

# Gate: Model Card
## Definition
A `model_card` is a technical spec for a language model: provider, context window, pricing in $/1M tokens, and boolean capability flags. Reference artifact only — not a tutorial. Gates ensure traceability to official sources, comparable pricing, and freshness within 90 days.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p02_mc_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"model_card"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | Required fields present and non-empty: `id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `provider`, `model_name`, `context_window`, `pricing`, `capabilities`, `tags`, `tldr` | Incomplete artifact |
| H07 | `provider` matches a known provider enum (Anthropic, OpenAI, Google, Meta, Mistral, Cohere, or documented costm) | Prevents typos that break routing |
| H08 | `context_window` is a positive integer | Core spec field — must be exact |
| H09 | `pricing` field present with at least `input` and `output` keys (numeric $/1M tokens, or `null` for open-weight) | Non-comparable pricing blocks cost analysis |
| H10 | `capabilities` field is a map of boolean flags | Capability claims require verifiable binary form |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, names provider + model + primary use case |
| S02 | Pricing normalized to $/1M tokens | 1.0 | Both `input` and `output` prices in $/1M tokens; `null` for open-weight |
| S03 | Capabilities list complete | 1.0 | Flags: vision, audio, function_calling, streaming, fine_tuning, json_mode, code, reasoning |
| S04 | Benchmarks referenced | 1.0 | >= 1 public benchmark (MMLU, HumanEval, MATH) with score and date |
| S05 | Limitations documented | 1.0 | >= 2 specific limitations: context degradation, refusal patterns, knowledge cutoff |
| S06 | `tags` includes `"model-card"` | 0.5 | Minimum tag for routing |
| S07 | Use-case recommendations present | 1.0 | >= 3 recommended use cases and >= 1 not-recommended |
| S08 | API endpoint documented | 0.5 | Names the model identifier string used in API calls |
| S09 | Comparison to alternatives noted | 0.5 | >= 1 comparable model named with key difference stated |
| S10 | Version and spec date accurate | 1.0 | `updated` within 90 days; `data_source` is a live URL |
| S11 | `max_output` field present and positive integer | 0.5 | Required for prompt budget calculations |
| S12 | Density >= 0.85 | 1.0 | No narrative: "great for", "one of the best", "in summary" |
| S13 | `linked_artifacts` field present | 0.5 | Lists related model cards, lenses, or routing rules |
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool + record in memory |
| >= 8.0 | PUBLISH | Commit to pool |
| >= 7.0 | REVIEW | Acceptable with documented improvement items |
| < 7.0 | REJECT | Revise and resubmit — do not publish |
| 0 (HARD fail) | REJECTED | Fix failing HARD gate(s) first |
## Bypass
Bypasses are logged and expire automatically.
| Field | Value |
|-------|-------|

## Examples

# Examples: model-card-builder
## Golden Example
INPUT: "Documenta o Claude Sonnet 4 for decidir routing"
OUTPUT:
```yaml
id: p02_mc_anthropic_sonnet_4
kind: model_card
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
model_name: "claude-sonnet-4-6"
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
tldr: "Sonnet 4 — anthropic, 200K ctx, $3/$15 per 1M, melhor cost-beneficio analysis/research"
when_to_use: "Analise e research where opus is overkill e haiku insuficiente"
keywords: [anthropic, claude-sonnet-4, balanced]
linked_artifacts:
  primary: null
  related: [p02_mc_anthropic_opus_4]
data_source: "https://docs.anthropic.com/en/docs/about-claude/models"
## Boundary
model_card IS: spec tecnica do Sonnet 4 (capacidades, costs, limits).
model_card IS NOT: boot_config, agent, benchmark.
## Specifications
| Spec | Value | Source |
|------|-------|--------|
| Model | claude-sonnet-4-6 | https://docs.anthropic.com/en/docs/about-claude/models |
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
