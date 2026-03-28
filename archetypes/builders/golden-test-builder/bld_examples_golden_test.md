---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of golden_test artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: golden-test-builder

## Golden Example

INPUT: "Cria golden test de knowledge_card sobre prompt caching"

OUTPUT:
```yaml
---
id: p07_gt_kc_prompt_caching
kind: golden_test
pillar: P07
title: "Golden: KC Prompt Caching"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
target_kind: "knowledge_card"
input: "Destila conhecimento sobre prompt caching para otimizar custos LLM"
golden_output_ref: "inline"
quality_threshold: 9.5
rationale: "H01-H10 pass, S01-S18 pass. All HARD gates clear. Density 0.93, actionable, sourced."
edge_case: false
reviewer: "orchestrator"
approval_date: "2026-03-26"
domain: "knowledge"
quality: null
tags: [golden-test, knowledge-card, calibration]
tldr: "Reference KC: prompt caching, density 0.93, all 10 HARD + 18 SOFT gates pass"
density_score: 0.93
linked_artifacts:
  primary: "quality-gate-builder"
  related: [p11_qg_kc_publish]
---

## Input Scenario
Destila conhecimento sobre prompt caching para otimizar custos LLM.
Foco: como funciona, quando usar, economia esperada, limitacoes.

## Golden Output
---
id: p01_kc_prompt_caching
kind: knowledge_card
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "knowledge-engine"
domain: "llm_optimization"
quality: null
tags: [prompt-caching, cost-optimization, llm, anthropic]
tldr: "Prompt caching reuses prefixes across API calls, cutting costs 90% and latency 85%"
density_score: 0.93
---

## Conceitos
- Prompt caching stores computed prefixes server-side for reuse
- Minimum cacheable prefix: 1024 tokens (Anthropic), 128 tokens (OpenAI)
- Cache TTL: 5 minutes (Anthropic), session-scoped (OpenAI)
- Write cost: 1.25x base price; read cost: 0.1x base price

## Quando Usar
- System prompts > 1024 tokens repeated across requests
- Few-shot examples reused in batch processing
- Tool definitions shared across conversation turns
- RAG contexts with stable document prefixes

## Economia Esperada
- Anthropic: 90% cost reduction on cached tokens, 85% latency reduction
- OpenAI: 50% cost reduction on cached tokens
- Break-even: 2+ requests with same prefix within TTL window

## Limitacoes
- Prefix must be identical byte-for-byte (no variation allowed)
- Cache eviction after TTL — no persistence guarantee
- Only prefix caching (beginning of prompt, not middle/end)
- Minimum token threshold — short prompts get no benefit

## Comparativo
| Provider | Min Tokens | TTL | Write Cost | Read Cost |
|----------|-----------|-----|------------|-----------|
| Anthropic | 1024 | 5 min | 1.25x | 0.1x |
| OpenAI | 128 | session | 1.0x | 0.5x |
| Google | 32768 | 1 hour | 1.0x | 0.25x |

## References
- https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- https://platform.openai.com/docs/guides/prompt-caching

## Rationale
- YAML parses without error (H01 pass)
- id starts with p01_kc_ (H02 pass)
- id == filename stem (H03 pass)
- kind == knowledge_card (H04 pass)
- quality == null (H05 pass)
- body >= 3 bullet points per section (H06 pass)
- size <= 5120 bytes (H07 pass)
- tags is list with >= 3 items (S02 pass)
- density >= 0.80 (actual 0.93) (S07 pass)
- All 6 body sections present with concrete data (S03-S06 pass)
- Comparativo table has real provider data with URLs (S08 pass)

## Evaluation Criteria
- [ ] All 10 KC HARD gates pass
- [ ] Density >= 0.90 (golden threshold)
- [ ] Every bullet is concrete (no filler)
- [ ] Comparativo has >= 3 providers with URLs
- [ ] Economia section has specific percentages
```

WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p07_gt_ pattern (H02 pass)
- kind: golden_test (H04 pass)
- 22 frontmatter fields present (H08 pass)
- quality_threshold == 9.5 (H07 pass)
- rationale maps to specific gate IDs H01-H07, S02-S08 (S03 pass)
- golden_output is complete KC with all sections (S04 pass)
- reviewer assigned: orchestrator (S06 pass)
- Input Scenario is specific and actionable (S04 pass)
- Evaluation Criteria has 5 concrete checks (S05 pass)

## Anti-Example

INPUT: "Golden test for a KC"

BAD OUTPUT:
```yaml
---
id: golden_test_kc
kind: golden_test
title: "A good KC test"
quality: 8.5
quality_threshold: 8.0
target_kind: kc
---

## Golden Output
A knowledge card about some topic. Should have good density and be well-written.
The card should follow best practices and include relevant information.
```

FAILURES:
1. id: no p07_gt_ prefix -> H02 FAIL
2. pillar: missing -> H05 FAIL
3. quality: self-scored 8.5 instead of null -> H06 FAIL
4. quality_threshold: 8.0 < 9.5 minimum -> H07 FAIL
5. target_kind: "kc" not valid kind name (should be "knowledge_card") -> H08 FAIL
6. golden_output: vague prose, not a complete artifact -> S04 FAIL
7. rationale: missing entirely -> S03 FAIL
8. Input Scenario: missing section -> S04 FAIL
9. Evaluation Criteria: missing section -> S05 FAIL
10. tags: missing -> S02 FAIL
11. tldr: missing -> S01 FAIL
12. density: near zero (all filler prose) -> S07 FAIL
