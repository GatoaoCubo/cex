---
kind: quality_gate
id: p11_qg_chunk_strategy
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of chunk_strategy artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: chunk_strategy"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, chunk-strategy, P01]
tldr: "Pass/fail gate for chunk_strategy artifacts: required fields, id pattern, body sections, parameter completeness."
domain: "text chunking and splitting for RAG pipelines"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 1.0
related:
  - bld_examples_chunk_strategy
  - p11_qg_constraint_spec
  - p11_qg_retriever_config
  - p11_qg_memory_scope
  - p11_qg_handoff_protocol
  - p11_qg_output_validator
  - p11_qg_prompt_version
  - p11_qg_effort_profile
  - p11_qg_document_loader
  - bld_instruction_chunk_strategy
---

## Quality Gate

# Gate: chunk_strategy
## Definition
| Field | Value |
|---|---|
| metric | chunk_strategy artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: chunk_strategy` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p01_chunk_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | id field != filename without extension |
| H04 | Kind equals literal `chunk_strategy` | Any other kind value |
| H05 | Quality field is null | Any non-null value |
| H06 | All required fields present | Missing quality, tags, tldr or other required fields |
| H07 | All required body sections present | Missing ## Overview or ## Method or ## Parameters or ## Integration |
| H08 | Body <= 2048 bytes | Body exceeds size limit |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Parameter completeness | 1.0 | All parameters have concrete values (no placeholders) |
| Rationale quality | 1.0 | Each parameter value has clear rationale |
| Pattern selection | 1.0 | Correct pattern chosen for the use case |
| Boundary clarity | 1.0 | Explicitly states what this IS and IS NOT |
| Integration mapping | 0.5 | Upstream and downstream connections documented |
| Density | 1.0 | Information density >= 0.8, no filler content |
| Tags quality | 0.5 | Tags >= 3, includes "chunk_strategy", relevant to content |
| Tldr quality | 0.5 | Tldr <= 160 chars, dense, accurate summary |
| Domain specificity | 1.0 | Parameters and values specific to declared domain |
| Testability | 0.5 | Configuration can be validated with known inputs |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental text chunking and splitting for RAG pipelines artifact under active A/B testing |
| approver | Nucleus lead (written approval required) |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML parse), H05 (quality null) |

## Examples

# Examples: chunk-strategy-builder
## Golden Example
INPUT: "Create chunk strategy for RAG over technical documentation"
OUTPUT:
```yaml
id: p01_chunk_tech_docs_recursive
kind: chunk_strategy
pillar: P01
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Technical Documentation Recursive Splitter"
quality: null
tags: [chunk_strategy, P01, chunk]
tldr: "Technical Documentation Recursive Splitter — production-ready chunk_strategy configuration"
```
## Overview
Recursive character splitter tuned for technical documentation with Markdown headings.
Splits on heading boundaries first, then paragraphs, then sentences.

## Method
Algorithm: recursive_character (LangChain RecursiveCharacterTextSplitter)
Separators tried in order: H2 heading > H3 heading > paragraph > line > sentence > word.
Falls back to next separator only when chunk exceeds chunk_size.

## Parameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| chunk_size | 512 tokens | Fits nomic-embed-text (8192) with 16x chunks per query |
| chunk_overlap | 64 tokens | 12.5% overlap preserves cross-boundary context |
| separators | [\n## , \n### , \n\n, \n, . , ] | Heading-first preserves section coherence |
| strip_whitespace | true | Remove leading/trailing whitespace from chunks |
| keep_separator | true | Retain heading markers for context |

## Integration
- Input: raw Markdown documents from document_loader
- Output: list of Document chunks with metadata (source, chunk_index, heading_path)
- Pairs with: p01_emb_nomic (embedding), p01_retr_hybrid (retrieval)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p01_chunk_ pattern (H02 pass)
- kind: chunk_strategy (H04 pass)
- All required fields present (H06 pass)
- Body has all 4 sections: Overview, Method, Parameters, Integration (H07 pass)
- Parameters table with value and rationale (S03 pass)
- tldr under 160 chars (S01 pass)
- tags >= 3 items, includes "chunk_strategy" (S02 pass)
## Anti-Example
INPUT: "Create chunk strategy for code files"
BAD OUTPUT:
```yaml
id: code-chunker
kind: chunker
quality: 9.0
tags: [chunker]
```
FAILURES:
1. id has hyphens and no p01_chunk_ prefix -> H02 FAIL
2. kind: 'chunker' not 'chunk_strategy' -> H04 FAIL
3. Missing fields: method, chunk_size, chunk_overlap, separators -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. No ## Method section in body -> H07 FAIL
6. No parameters table -> S03 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
