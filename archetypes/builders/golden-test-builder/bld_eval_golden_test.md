---
kind: quality_gate
id: p11_qg_golden_test
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of golden_test artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: golden_test"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, golden-test, calibration, evaluation, quality-baseline, P11]
tldr: "Validates golden_test artifacts: verified 9.5+ source quality, rationale-to-gate mapping, and non-self-referential target kind."
domain: "golden_test — reference quality calibration cases scoring 9.5+ with rationale mapped to evaluation gates"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.93
related:
  - p11_qg_few_shot_example
  - bld_instruction_golden_test
  - golden-test-builder
  - p11_qg_formatter
  - p11_qg_quality_gate
  - bld_output_template_golden_test
  - bld_knowledge_card_golden_test
  - p11_qg_glossary_entry
  - bld_architecture_golden_test
  - p03_sp_golden_test_builder
---

## Quality Gate

# Gate: golden_test
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden (the golden_test itself must also reach 9.5) |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: golden_test` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p07_gt_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `golden_test` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, target_kind, quality_threshold, reviewer, domain, quality, tags, tldr | Any missing field |
| H07 | `quality_threshold` >= 9.5 | Threshold below the golden standard |
| H08 | `target_kind` is non-empty and NOT `golden_test` | Self-referential calibration |
| H09 | `Golden Output` section present and non-empty | No reference output to calibrate against |
| H10 | `Input Scenario` section present and non-empty | No input; test is unverifiable |
| H11 | `rationale` references at least one gate ID (pattern: H\d+ or S\d+) | No gate mapping; rationale is unstructured |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` <= 160 chars, names `target_kind` and what makes this golden | 0.10 | Named=1.0, vague=0.3 |
| S02 | Tags list len >= 3, includes `target_kind` as keyword | 0.06 | Present=1.0, absent=0.0 |
| S03 | Rationale maps to >= 3 distinct gate IDs of `target_kind` | 0.15 | 3+=1.0, 2=0.6, 1=0.3, 0=0.0 |
| S04 | Golden Output is complete and copy-pasteable as a real artifact | 0.14 | Complete=1.0, skeleton=0.4, absent=0.0 |
| S05 | Input Scenario is non-trivial (edge case or high-complexity scenario) | 0.12 | Edge/complex=1.0, trivial=0.3 |
| S06 | Boundary from `few_shot_example` stated (teaches format vs. evaluates quality) | 0.09 | Explicit=1.0, implied=0.4, absent=0.0 |
| S07 | Boundary from `unit_eval` stated | 0.07 | Explicit=1.0, implied=0.4, absent=0.0 |
| S08 | Verification source cited for 9.5+ quality claim (reviewer name or process) | 0.10 | Cited=1.0, absent=0.0 |
| S09 | Evaluation Criteria section present with pass/fail conditions | 0.10 | Present=1.0, absent=0.0 |
| S10 | `density_score` >= 0.85 (golden tests must be information-dense) | 0.07 | Met=1.0, below=0.0 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — accepted into calibration set; informs all future scoring for `target_kind` |
| >= 8.0 | PUBLISH — pool-eligible reference; not yet calibration-authoritative |
| >= 7.0 | REVIEW — rationale incomplete or verification source missing |
| < 7.0  | REJECT — redo; likely unverified source quality or missing gate mapping |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Bootstrap only: first golden_test for a brand-new kind where no prior calibration set exists |
| approver | Two independent reviewers must sign off in lieu of automated verification |
| audit trail | Required: both reviewer names, review date, written agreement on quality assessment |

## Examples

# Examples: golden-test-builder
## Golden Example
INPUT: "Create golden test from knowledge_card about prompt caching"
OUTPUT:
```yaml
id: p07_gt_kc_prompt_caching
kind: golden_test
pillar: P07
title: "Golden: KC Prompt Caching"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
target_kind: "knowledge_card"
input: "Destila knowledge about prompt caching for optimize costs LLM"
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
## Input Scenario
Destila knowledge about prompt caching for optimize costs LLM.
Foco: as funciona, quando usar, economia esperada, limitactions.
## Golden Output
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
## Limitactions
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
