---
kind: quality_gate
id: p11_qg_action_prompt
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of action_prompt artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: action_prompt"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, action-prompt, P11, P03, governance, task-execution]
tldr: "Gates for action_prompt artifacts — task-focused prompts with defined input/output contracts."
domain: action_prompt
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.87
related:
  - bld_examples_action_prompt
  - bld_instruction_action_prompt
  - p11_qg_builder
  - bld_knowledge_card_action_prompt
  - p11_qg_agent
  - p03_sp_action_prompt_builder
  - p11_qg_boot_config
  - action-prompt-builder
  - bld_output_template_action_prompt
  - p11_qg_naming_rule
---

## Quality Gate

# Gate: action_prompt
## Definition
| Field     | Value                                        |
|-----------|----------------------------------------------|
| metric    | input/output contract clarity + edge coverage |
| threshold | 8.0                                          |
| operator  | >=                                           |
| scope     | all action_prompt artifacts (P03)            |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = broken prompt at runtime |
| H02 | id matches `^p03_ap_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "action_prompt" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All 21 required fields present | Completeness |
| H07 | edge_cases has >= 2 entries | Robustness requirement |
| H08 | body has all 5 required sections: Action, Input, Output, Validation, Edge Cases | Structure compliance |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "action_prompt" | 0.5 |
| S03 | action field is a verb phrase (starts with verb) | 1.0 |
| S04 | input_required lists specific data items with types | 1.0 |
| S05 | output_expected describes verifiable structure | 1.0 |
| S06 | purpose explains WHY, not just WHAT | 0.5 |
| S07 | No identity or persona content (not system_prompt territory) | 1.0 |
| S08 | No step-by-step recipe with prerequisites (not instruction territory) | 1.0 |
| S09 | Validation section has verifiable, concrete criteria | 0.5 |
| S10 | Input section uses table or structured format | 0.5 |
| S11 | density_score >= 0.80 | 0.5 |
| S12 | No filler phrases ("this document", "in summary", "please note") | 1.0 |
Weights sum: 9.5. Normalize: divide each by 9.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference action_prompt |
| >= 8.0 | PUBLISH — ready for runtime injection |
| >= 7.0 | REVIEW — tighten I/O contract or add edge cases |
| < 7.0  | REJECT — rework action definition and output spec |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Urgent task requiring runtime prompt before full validation cycle |
| approver | p03-chief |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |

## Examples

# Examples: action-prompt-builder
## Golden Example
INPUT: "Create action prompt for extracting product metrics from marketplace scrape data"
OUTPUT:
```yaml
id: p03_ap_extract_product_metrics
kind: action_prompt
pillar: P03
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
title: "Extract Product Metrics from Marketplace Scrape"
action: "Extract and normalize product metrics from raw marketplace scrape data"
input_required:
  - "scrape_data: JSON object with raw marketplace response"
  - "marketplace: enum (mercado_livre, shopee, amazon_br)"
output_expected: "Normalized JSON with price, rating, reviews_count, seller_score, availability"
purpose: "Normalize heterogeneous scrape formats for cross-marketplace comparison"
steps_count: 4
timeout: "30s"
edge_cases:
  - "Missing price field (some listings show 'Sob consulta')"
  - "Rating format varies (4.5 vs 4,5 vs 45/50)"
  - "Seller score absent on new sellers"
constraints:
  - "Do NOT infer missing data — use null"
  - "Do NOT convert currencies"
domain: "research"
quality: null
tags: [action_prompt, marketplace, metrics, extraction, research]
tldr: "Extract and normalize product metrics from raw marketplace scrape into structured JSON for comparison"
density_score: 0.92
```
## Context
Marketplace scrapes return heterogeneous formats per platform. This prompt normalizes
raw scrape data into a consistent schema for cross-marketplace product comparison.
Purpose: enable pricing and competitive analysis across ML, Shopee, Amazon BR.
## Input
| Item | Type | Format | Required |
|------|------|--------|----------|
| scrape_data | JSON object | Raw marketplace API/scrape response | YES |
| marketplace | enum string | mercado_livre, shopee, amazon_br | YES |
## Execution
1. Identify marketplace-specific field mappings for price, rating, reviews, seller
2. Extract each metric, applying format normalization (comma->dot, percentage->decimal)
3. Set missing fields to null (never infer)
4. Return normalized JSON object
## Output
Format: JSON
Structure:
```json
{
  "price_brl": 149.90,
  "rating": 4.5,
  "reviews_count": 1247,
  "seller_score": 0.95,
  "availability": true
}
```
## Validation
- All 5 output fields present (null OK for missing)
- price_brl is float or null (never string)
- rating normalized to 0.0-5.0 scale
- Edge case: "Sob consulta" -> price_brl: null
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p03_ap_ pattern (H02 pass)
- kind: action_prompt (H04 pass)
- 21 required fields present (H06 pass)
- edge_cases: 3 entries >= 2 (H07 pass)
- body has all 5 sections (H08 pass)
- action is verb phrase "Extract and normalize..." (S03 pass)
- input_required lists specific types (S04 pass)
- output_expected is verifiable JSON structure (S05 pass)
- No identity/persona content (S07 pass)
## Anti-Example
INPUT: "Create action prompt for analyzing data"
BAD OUTPUT:
```yaml
id: analyze-data
kind: prompt
pillar: prompt
action: data analysis
input_required: some data
output_expected: analysis results
quality: 9.0
tags: [analysis]
edge_cases: []
```
You are a data analysis expert. Analyze the provided data thoroughly and
provide comprehensive insights. Make sure your analysis is detailed and helpful.
FAILURES:
1. id: no `p03_ap_` prefix, uses hyphens -> H02 FAIL
2. kind: "prompt" not "action_prompt" -> H04 FAIL
3. pillar: "prompt" not "P03" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. edge_cases: empty list (need >= 2) -> H07 FAIL
6. Missing fields: version, created, updated, author, title, purpose, domain -> H06 FAIL
7. action: "data analysis" is noun phrase, not verb phrase -> S03 FAIL
8. input_required: "some data" is vague string, not typed list -> S04 FAIL
9. Contains persona ("You are a data analysis expert") -> S07 FAIL
10. No ## Context, ## Input, ## Execution, ## Output, ## Validation sections -> H08 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
