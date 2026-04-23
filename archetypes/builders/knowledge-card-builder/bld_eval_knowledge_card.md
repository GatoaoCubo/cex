---
kind: quality_gate
id: p11_qg_knowledge_card
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of knowledge_card artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: Knowledge Card"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, knowledge-card, density, fact, distillation, searchability]
tldr: "Gates ensuring knowledge_card artifacts contain concrete atomic facts with density >= 0.8, semantic frontmatter, and file size <= 5KB."
domain: "knowledge_card — atomic searchable facts with high information density"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.94
related:
  - p11_qg_agent_computer_interface
  - p11_qg_input_schema
  - p11_qg_chunk_strategy
  - p11_qg_memory_scope
  - p11_qg_retriever_config
  - p11_qg_handoff
  - p11_qg_quality_gate
  - p11_qg_constraint_spec
  - p11_qg_handoff_protocol
  - p11_qg_output_validator
---

## Quality Gate

# Gate: Knowledge Card
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: knowledge_card` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^KC_[A-Z0-9_]+$` | Lowercase, missing KC_ prefix, or non-alphanumeric chars |
| H03 | ID equals filename stem | `id: KC_REDIS_TTL` in file `KC_CACHE_TTL.md` |
| H04 | Kind equals literal `knowledge_card` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All 19 required fields present | Missing: domain, tldr, density_score, sources, or card_type |
| H07 | `density_score` is a float in range [0.0, 1.0] | Outside range or non-numeric value |
| H08 | `density_score` >= 0.8 | Score below threshold — card too sparse to be useful |
| H09 | Total file size <= 5120 bytes | Exceeds 5KB limit |
| H10 | `tldr` is <= 160 characters | tldr exceeds character limit |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Factual concreteness | 1.0 | Card contains specific values, numbers, or verifiable facts | Mix of facts and vague statements | Entirely vague or conceptual |
| S02 | Atomicity | 1.0 | Card covers exactly one concept with no scope creep | Mostly one concept; minor tangents | Multiple unrelated concepts |
| S03 | Searchability — tags | 1.0 | Tags cover domain, subtopic, and use-case angles (>= 4 distinct tags) | 3 tags | Fewer than 3 tags |
| S04 | Source attribution | 1.0 | At least one specific source (URL, paper, spec version, date) | Source mentioned but not specific | No sources |
| S05 | Card type classification | 0.5 | `card_type` is `domain_kc` or `meta_kc` with correct body structure for that type | Type present but body structure mismatches | Type absent |
| S06 | Density discipline | 1.0 | No padding, no restatements, no filler sentences in body | Minor padding present | More than 20% filler content |
| S07 | tldr precision | 1.0 | tldr is a standalone searchable sentence capturing the key fact | tldr too vague to retrieve the card | tldr absent or over 160 characters |
| S08 | Currency | 0.5 | `created` date present; `updated` reflects last substantive revision | Created date only, no updated | No dates |
| S09 | Cross-references | 0.5 | Related cards or concepts linked in body | Related concepts mentioned but not linked | No cross-references |
| S10 | Practical applicability | 1.0 | Body answers "when would I use this?" with a concrete scenario | Implicitly applicable but not stated | Pure theory with no application context |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to knowledge pool as authoritative reference card |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Rapidly evolving topic where sources are not yet stabilized (e.g., new library release, breaking API change) |
| Approver | Domain expert reviewer |

## Examples

# Examples: knowledge-card-builder
## Golden Example
INPUT: "Destila knowledge about prompt caching for optimize costs LLM"
OUTPUT:
```yaml
id: p01_kc_prompt_caching
kind: knowledge_card
pillar: P01
title: "Prompt Caching Patterns for LLM Cost Optimization"
version: "1.0.0"
created: "2026-03-24"
updated: "2026-03-24"
author: "builder"
domain: llm_engineering
quality: null
tags: [prompt-caching, cost-optimization, latency, anthropic, openai, knowledge]
tldr: "Prompt caching reutiliza prefixos pre-processesdos between chamadas LLM, reduzindo cost em ate 90% e latency em 85%"
when_to_use: "Quanof the system LLM repete context longo between chamadas"
keywords: [prompt-caching, cache-control, context-reuse]
long_tails:
  - Como configurar prompt caching na API da Anthropic
  - Tamanho minimal de prefixo for ativar cache em LLMs
axioms:
  - SEMPRE coloque conteudo estatico ANTES do dinamico
  - NUNCA cache context that muda a each request
linked_artifacts:
  primary: null
  related: [p01_kc_rag_fundamentals]
density_score: 0.91
data_source: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching"
# Prompt Caching Patterns for LLM Cost Optimization
## Quick Reference
```yaml
topic: prompt_caching
scope: LLM API optimization (Anthropic, OpenAI, Google)
owner: builder
criticality: high
```
## Key Concepts
- **Cache-Control**: Anthropic `cache_control: {kind: "ephemeral"}`; TTL 5 min
- **Prefix Matching**: cache hit when prefix identical byte-a-byte
- **Minimum Tokens**: Anthropic >= 1024; OpenAI >= 1024 (auto)
- **Pricing Split**: write 1.25x base, read 0.1x (90% savings on hit)
## Strategy Phases
1. **Audit**: identify prompts with >50% static content
2. **Reorder**: static first (system > few-shot > RAG), dynamic last
3. **Annotate**: add cache breakpoints on last static block
4. **Monitor**: measure hit rate via response headers
5. **Tune**: target >= 80% hit rate, adjust granularity
## Golden Rules
- ORDENE: static first, dynamic last (always)
- AGRUPE: few large cacheable blocks > many small ones
- METRIZE: hit_rate = read / (read + creation + uncached)
- INVALIDE with cuidata: 1 byte diff = full cache miss
## Flow
```text
[Request] -> [Hash Prefix] -> [Cache Lookup]
                                   |
                         HIT: 0.1x cost, 85% faster
                         MISS: 1.25x cost, normal speed
                                   |
                             [Generate] -> [Response]
```
## Comparativo
| Provider | Min Tokens | Config | Write | Read | TTL |
|----------|-----------|--------|-------|------|-----|
| Anthropic | 1024 | Explicit | 1.25x | 0.1x | 5 min |
| OpenAI | 1024 | Automatic | 1.0x | 0.5x | 5-60 min |
| Google | 32768 | Explicit | 1.0x | 0.25x | config |
## References
- Source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- Related: p01_kc_rag_fundamentals (context reuse patterns)
```
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p01_kc_ pattern (H03 pass)
- kind: knowledge_card (H04 pass)
- 13 required fields present (H06 pass)
- tags: list >= 3 (H07 pass)
- body 200-5120 bytes (H08 pass)
- No internal paths (H09 pass)
- author not orchestrator (H10 pass)
- 7 sections >= 3 lines (S06, S08 pass)
- Bullets <= 80 chars (S10 pass)
- Tables + code blocks + external URL (S11-S13 pass)
- linked_artifacts with primary+related (S20 pass)
## Anti-Example
INPUT: "Documenta prompt caching"
BAD OUTPUT:
```yaml
id: prompt_caching_knowledge
kind: knowledge_card
title: Prompt Caching
author: orchestrator
quality: 9.0
tags: "caching, llm"
This document describes how prompt caching works.
In summary, it saves money. As mentioned before, caching is good.
See records/core/docs/caching.md for details.
```
FAILURES:
1. id: no `p01_kc_` prefix -> H03 FAIL
2. lp: missing -> H06 FAIL
3. author: orchestrator -> H10 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
