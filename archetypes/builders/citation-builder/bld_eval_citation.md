---
kind: quality_gate
id: p11_qg_citation
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of citation artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: Citation"
version: "1.0.0"
author: "n04_knowledge"
tags: [quality-gate, citation, provenance, attribution, reliability]
tldr: "Gates ensuring citation artifacts have verifiable provenance, reliability tier, excerpt, and temporal freshness."
domain: "citation — structured source attribution with provenance"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_citation
  - bld_examples_knowledge_card
  - bld_examples_golden_test
  - bld_output_template_citation
  - p01_kc_citation
  - bld_instruction_citation
  - p03_sp_citation_builder
  - p11_qg_prompt_cache
  - bld_schema_citation
  - p01_kc_caching
---

## Quality Gate

# Gate: Citation
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: citation` |
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | ID matches `^p01_cit_[a-z][a-z0-9_]+$` | Wrong prefix or format |
| H03 | ID equals filename stem | Mismatch |
| H04 | Kind equals literal `citation` | Wrong kind |
| H05 | Quality field is `null` | Non-null value |
| H06 | source_type is valid enum | Not in web/paper/book/internal/api |
| H07 | reliability_tier is valid enum | Not in tier_1/tier_2/tier_3 |
| H08 | url is present and non-empty | Missing URL |
| H09 | date_accessed is present | Missing access date |
| H10 | excerpt is 1-3 sentences | Empty or too long |
| H11 | Total file <= 2048 bytes | Exceeds limit |
## SOFT Scoring
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Excerpt concreteness | 1.0 | Specific numbers, dates, named entities | Partial specifics | Vague summary |
| S02 | Reliability classification | 1.0 | Tier matches source type correctly | Reasonable but debatable | Wrong tier |
| S03 | Relevance mapping | 0.5 | relevance_scope with 2+ specific domains | 1 domain | No mapping |
| S04 | Temporal freshness | 0.5 | Freshness policy defined with days | Date only | No temporal info |
| S05 | Verification completeness | 1.0 | URL + DOI/ISBN + access date | URL + date | URL only |
| S06 | Body structure | 1.0 | All 5 sections present with content | 3-4 sections | Fewer |

## Cross-References

- **Pillar**: P11 (Feedback)
- **Kind**: `quality gate`
- **Artifact ID**: `p11_qg_citation`
- **Tags**: [quality-gate, citation, provenance, attribution, reliability]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P11 | Feedback domain |
| Kind `quality gate` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Examples

# Examples: citation-builder
## Golden Example
INPUT: "Create citation for Anthropic prompt caching documentation"
OUTPUT:
```yaml
---
id: p01_cit_anthropic_prompt_caching
kind: citation
pillar: P01
title: "Anthropic Prompt Caching Documentation"
version: "1.0.0"
created: "2026-04-07"
updated: "2026-04-07"
author: "citation-builder"
source_type: web
reliability_tier: tier_2
url: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching"
date_accessed: "2026-04-07"
excerpt: "Prompt caching allows you to cache frequently used context between API calls, reducing latency by up to 85% and costs by up to 90% for long prompts."
relevance_scope: [llm_engineering, prompt_cache, cost_optimization]
domain: llm_engineering
quality: 8.8
tags: [citation, anthropic, prompt-caching, cost-optimization]
tldr: "Official Anthropic docs on prompt caching — 90% cost reduction, 85% latency reduction via prefix reuse with 5min TTL"
---

# Anthropic Prompt Caching Documentation

## Source
- **Author**: Anthropic
- **Title**: Prompt Caching (Build with Claude)
- **Publisher/Venue**: docs.anthropic.com
- **Date**: 2025 (continuously updated)
- **Type**: web (tier_2 — official documentation)

## Excerpt
> Prompt caching allows you to cache frequently used context between API calls, reducing latency by up to 85% and costs by up to 90% for long prompts. Minimum cacheable prefix is 1024 tokens. Cache TTL is 5 minutes.

## Relevance
- Supports: p01_kc_prompt_caching, prompt_cache configuration decisions
- Scope: llm_engineering, cost optimization, API integration

## Verification
- URL: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- Accessed: 2026-04-07
- Freshness policy: 90 days (API docs evolve)
- DOI/ISBN: N/A
```
WHY THIS IS GOLDEN:
- quality: null
- id matches p01_cit_ pattern
- source_type and reliability_tier are valid enums
- excerpt is concrete (numbers: 85%, 90%, 1024 tokens, 5min)
- date_accessed present
- relevance_scope mapped
- Under 2048 bytes

## Anti-Example
INPUT: "Cite prompt caching"
BAD OUTPUT:
```yaml
id: caching_ref
kind: citation
url: https://docs.anthropic.com
quality: 8.5
```
FAILURES:
1. id: no p01_cit_ prefix
2. quality: not null — self-scored
3. No source_type, reliability_tier, excerpt, date_accessed
4. URL too generic (no specific page)
5. No body sections

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
