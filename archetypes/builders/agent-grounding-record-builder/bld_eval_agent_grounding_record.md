---
kind: quality_gate
id: bld_quality_gate_agent_grounding_record
pillar: P11
llm_function: GOVERN
purpose: Define hard gates H01-H08 and soft scoring dimensions for agent_grounding_record quality control
quality: 9.1
title: "Agent Grounding Record -- Quality Gate"
version: "1.0.0"
author: wave7_n05
tags: [agent_grounding_record, builder, quality_gate]
tldr: "8 hard gates (all must pass) + 5D soft scoring targeting >= 9.0 overall for compliance-grade provenance"
domain: "agent_grounding_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_agent_grounding_record
  - p11_qg_quality_gate
  - bld_knowledge_card_quality_gate
  - p11_qg_kind_builder
  - p11_qg_few_shot_example
  - p11_qg_builder
  - p11_qg_creation_artifacts
  - bld_schema_agent_grounding_record
  - bld_collaboration_quality_gate
  - p11_qg_response_format
---

## Quality Gate

# Agent Grounding Record -- Quality Gate

## Scoring Overview

| Layer       | Weight | Method                                                   |
|-------------|--------|----------------------------------------------------------|
| Structural  | 30%    | Hard gate pass/fail count (H01-H08, must all pass)      |
| Rubric      | 30%    | 5D dimension scoring (D1-D5 weighted)                    |
| Semantic    | 40%    | LLM evaluation when structural + rubric score >= 8.5    |
| Target      | --     | >= 9.0 overall for production-grade grounding record     |

A record that fails ANY hard gate receives a score of 0.0 regardless of rubric or semantic scores.

## Hard Gates (H01-H08)

ALL hard gates must pass. One FAIL = record is invalid = do not publish.

| Gate | Field / Check                  | Pass Condition                                                         | Fail Action                                          |
|------|-------------------------------|-------------------------------------------------------------------------|------------------------------------------------------|
| H01  | Frontmatter YAML              | Parses without error; all required frontmatter keys present             | Return to F6, fix YAML syntax                        |
| H02  | Artifact ID naming pattern    | Matches ^p10_gr_[a-z0-9_]+\.md$                                        | Rename file to match pattern before scoring          |
| H03  | kind field                    | Exactly "agent_grounding_record" (string match, no whitespace)          | Fix frontmatter kind field                           |
| H04  | inference_id present          | Non-empty string matching UUIDv4 pattern                               | Generate new UUIDv4; do not reuse existing IDs       |
| H05  | output_hash present           | 64 lowercase hex characters (SHA-256)                                  | Recompute from raw output; this gate never waives    |
| H06  | otel_span_id present          | Non-empty string; 16 hex chars (W3C format) preferred                  | Verify OTel instrumentation is active; retrieve span |
| H07  | timestamp format              | ISO 8601 parseable with timezone (Z or +/-HH:MM)                       | Reformat timestamp; epoch integers are not accepted  |
| H08  | model.id present              | Non-empty string identifying the model                                 | Retrieve from inference session metadata             |

## Hard Gate Failure Reference

| Gate | Most Common Cause                             | Prevention                                                   |
|------|-----------------------------------------------|--------------------------------------------------------------|
| H01  | Copy-paste corruption in frontmatter YAML     | Validate YAML before finalizing                              |
| H02  | Wrong naming prefix (e.g. p01_ instead of p10_) | Check config ISO for naming convention before writing ID  |
| H03  | kind typo or wrong kind for this builder      | Load bld_manifest first; kind is agent_grounding_record      |
| H04  | Missing inference_id or copied from prior run | Generate fresh UUIDv4 at session start                       |
| H05  | Output hash computed after post-processing    | Hash the raw output BEFORE any formatting or truncation      |
| H06  | OTel not instrumented for this inference path | Add OTel GenAI semconv instrumentation to the inference layer|
| H07  | Timezone missing from timestamp               | Always use UTC (Z suffix) or explicit offset                 |
| H08  | Model ID not captured from provider response  | Log model ID from every API response header or body          |

## Soft Scoring Dimensions (D1-D5)

| Dim | Name                    | Weight | Scoring Criteria                                                              |
|-----|-------------------------|--------|-------------------------------------------------------------------------------|
| D1  | Provenance completeness | 0.30   | All required fields populated; no silent nulls; optional fields documented   |
| D2  | RAG-chunk coverage      | 0.25   | Every chunk has source_url AND content_hash; retrieval_score recorded         |
| D3  | Tool-call traceability  | 0.25   | Every tool-call has input_hash + output_hash + timestamp; status explicit    |
| D4  | C2PA integration        | 0.10   | c2pa_manifest_ref present (URI or explicit null); not omitted silently        |
| D5  | Downstream tracking     | 0.10   | downstream_use set; grounding_coverage_pct computed (not defaulted to 1.0)   |

### D1 -- Provenance Completeness Rubric

| Score | Criteria                                                                                        |
|-------|-------------------------------------------------------------------------------------------------|
| 10    | All required fields present; all optional fields documented (null or value); model-signature included |
| 8-9   | All required fields present; most optional fields documented                                    |
| 6-7   | All required fields present; several optional fields silently omitted                           |
| 4-5   | One required field missing or null where value expected                                        |
| 0-3   | Multiple required fields missing; record is structurally incomplete                            |

### D2 -- RAG-Chunk Coverage Rubric

| Score | Criteria                                                                                        |
|-------|-------------------------------------------------------------------------------------------------|
| 10    | Every chunk has source_url, content_hash, retrieval_score, chunk_id; no gaps                   |
| 8-9   | All chunks have source_url and content_hash; retrieval_score missing on <= 1 chunk             |
| 6-7   | All chunks have source_url; content_hash missing on some chunks                                |
| 4-5   | Some chunks missing source_url (any missing source_url is a severe provenance failure)         |
| 0-3   | Chunks present but source_urls absent; output is untraceable                                   |

### D3 -- Tool-Call Traceability Rubric

| Score | Criteria                                                                                        |
|-------|-------------------------------------------------------------------------------------------------|
| 10    | Every tool-call has input_hash, output_hash, timestamp, duration_ms, status                    |
| 8-9   | All tool-calls have input_hash and output_hash; duration_ms missing on <= 1                    |
| 6-7   | All tool-calls have hashes; timestamps missing on some                                         |
| 4-5   | Some tool-calls missing output_hash; tool effects are partially unverifiable                   |
| 0-3   | Tool calls logged without hashes; invocations are unverifiable                                 |

### D4 -- C2PA Integration Rubric

| Score | Criteria                                                                                        |
|-------|-------------------------------------------------------------------------------------------------|
| 10    | c2pa_manifest_ref is a valid URI pointing to an accessible C2PA manifest                       |
| 8     | c2pa_manifest_ref is explicitly null and a comment explains why C2PA is not active             |
| 6     | c2pa_manifest_ref is null with no explanation                                                  |
| 0-3   | c2pa_manifest_ref field is entirely omitted from the record                                    |

### D5 -- Downstream Tracking Rubric

| Score | Criteria                                                                                        |
|-------|-------------------------------------------------------------------------------------------------|
| 10    | downstream_use set; grounding_coverage_pct computed from actual claim analysis                 |
| 8     | downstream_use set; grounding_coverage_pct estimated with methodology noted                    |
| 6     | downstream_use set; grounding_coverage_pct is 0.0 (conservative but honest)                   |
| 0-3   | downstream_use missing or grounding_coverage_pct defaulted to 1.0 without verification        |

## Score Interpretation

| Score Range | Interpretation                       | Action                                     |
|-------------|--------------------------------------|--------------------------------------------|
| 9.0 - 10.0  | Production-grade grounding record    | Publish; link to C2PA manifest if applicable|
| 8.0 - 8.9   | Acceptable; minor gaps               | Publish with note; address gaps in next run |
| 7.0 - 7.9   | Below standard; significant gaps     | Do not publish; return to F6 for revision  |
| < 7.0       | Compliance failure                   | Reject; investigate data capture pipeline  |

## Scoring Commands

```bash
# Score an artifact
python _tools/cex_score.py --apply p10_gr_example.md
# Validate schema fields before scoring
python _tools/cex_compile.py p10_gr_example.md
# Check all P10 grounding records
python _tools/cex_doctor.py --pillar P10
```

## Examples

# Agent Grounding Record -- Examples

## Example 1 -- GOLDEN (Score: 9.5)

**Context**: Medical research agent queried PubMed API 3 times and retrieved 5 internal KB chunks to answer a drug interaction question.

```markdown
---
kind: agent_grounding_record
id: p10_gr_7f3a2c1b
pillar: P10
llm_function: PRODUCE
purpose: Per-inference provenance record for drug interaction query on warfarin + SSRIs
quality: null
title: "Grounding Record -- Drug Interaction Query: Warfarin + SSRIs"
version: "1.0.0"
author: n01_medical_research
tags: [agent_grounding_record, provenance, medical]
tldr: "Inference 7f3a2c1b -- claude-sonnet-4-6 -- 3 tools -- 5 RAG chunks -- production"
domain: "agent_grounding_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---
# Grounding Record -- Drug Interaction Query: Warfarin + SSRIs
## Inference Identity
| Field                  | Value                                                          |
|------------------------|----------------------------------------------------------------|
| inference_id           | 7f3a2c1b-e8d4-4f21-b9a3-1c2d3e4f5a6b                          |
| session_id             | sess_medbot_20260414_0923                                      |
| timestamp              | 2026-04-14T09:23:47Z                                           |
| downstream_use         | production                                                     |
| grounding_coverage_pct | 0.92                                                           |
| otel_span_id           | 4bf92f3577b34da6                                               |
## Model
| Field          | Value                                                          |
|----------------|----------------------------------------------------------------|
| id             | claude-sonnet-4-6                                              |
| version        | 20260412                                                       |
| provider       | anthropic                                                      |
| model-signature| attest:v1:sha256:9a4c1d2e3f...b7c8d9e0f1                      |
## Tool Calls
3 tool invocations during this inference run.
| # | tool_name       | tool_input_hash (sha256)                                         | tool_output_hash (sha256)                                        | duration_ms | timestamp              | status  |
|---|-----------------|------------------------------------------------------------------|------------------------------------------------------------------|-------------|------------------------|---------|
| 1 | pubmed_search   | a1b2c3d4e5f6...7890abcdef01234567890abcdef01234567890abcdef0123 | b2c3d4e5f601...234567890abcdef01234567890abcdef01234567890abc01 | 342         | 2026-04-14T09:23:48Z   | success |
| 2 | pubmed_fetch    | c3d4e5f60123...4567890abcdef01234567890abcdef01234567890abcde02 | d4e5f6012345...67890abcdef01234567890abcdef01234567890abcdef03  | 891         | 2026-04-14T09:23:49Z   | success |
| 3 | drug_db_lookup  | e5f601234567...890abcdef01234567890abcdef01234567890abcdef0104  | f601234567890...abcdef01234567890abcdef01234567890abcdef012305  | 156         | 2026-04-14T09:23:50Z   | success |
## RAG Chunks Retrieved
5 chunks retrieved from internal clinical knowledge base.
| # | chunk_id            | source_url                                                         | retrieval_score | content_hash (sha256)                                            |
|---|---------------------|--------------------------------------------------------------------|-----------------|------------------------------------------------------------------|
| 1 | kb_chunk_0x3f2a     | https://internal.kb/clinical/pharmacology/warfarin-interactions-01 | 0.94            | 1a2b3c4d5e6f...7890abcdef01234567890abcdef01234567890abcde01 |
| 2 | kb_chunk_0x3f2b     | https://internal.kb/clinical/pharmacology/ssri-cyp450-profile      | 0.91            | 2b3c4d5e6f01...234567890abcdef01234567890abcdef01234567890ab02 |
| 3 | kb_chunk_0x3f2c     | https://internal.kb/clinical/guidelines/bleeding-risk-assessment   | 0.87            | 3c4d5e6f0123...4567890abcdef01234567890abcdef01234567890abc03  |
| 4 | kb_chunk_0x3f2d     | https://internal.kb/clinical/pharmacology/fluoxetine-warfarin-rct  | 0.83            | 4d5e6f012345...67890abcdef01234567890abcdef01234567890abcd04   |
| 5 | kb_chunk_0x3f2e     | https://internal.kb/clinical/dosing/inr-monitoring-protocol        | 0.79            | 5e6f01234567...890abcdef01234567890abcdef01234567890abcde05    |
## Integrity
| Field             | Value                                                                            |
|-------------------|----------------------------------------------------------------------------------|
| output_hash       | 6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f (SHA-256)    |
| c2pa_manifest_ref | https://c2pa.internal.kb/manifests/7f3a2c1b-e8d4-4f21-b9a3-1c2d3e4f5a6b.c2pa  |
## Audit Summary
**Inference task**: Answer clinical question about warfarin + SSRI co-administration bleeding risk.
**Grounding sources**:
- 5 RAG chunks from internal clinical knowledge base (pharmacology + guidelines)
- 3 tool calls: PubMed search, PubMed full-text fetch, drug DB lookup
**Traceability chain**:
Query -> PubMed API (3 calls) + KB retrieval (5 chunks) -> claude-sonnet-4-6 -> output (hash: 6f7a8b9c...)
**Coverage note**: 0.92 -- 11 of 12 factual claims in the output are traceable to a RAG chunk or tool result.
One general pharmacokinetic statement draws on model parametric knowledge (no external source).
**OTel linkage**: This record is linked to OTel span 4bf92f3577b34da6. Full trace in Jaeger at trace ID 4bf92f3577b34da6a3c8f9e2d1b057c4.
**C2PA status**: C2PA manifest registered at c2pa.internal.kb. Includes model assertion, training data assertion, and content binding to output_hash.
```

**Why this scores 9.5**: All hard gates pass. All 5 RAG chunks have source_url + content_hash. All 3 tool calls have input/output hashes + timestamps. output_hash present. c2pa_manifest_ref is a valid URI. grounding_coverage_pct is computed and explained. Loses 0.5 for model-signature being abbreviated.

## Example 2 -- ANTI-EXAMPLE: Missing output-hash (Score: 0.0 -- Hard Gate H05 FAIL)

```markdown
---
kind: agent_grounding_record
id: p10_gr_bad_nohash
...
---
inference_id: 3a4b5c6d-...
model:
  id: gpt-4o
  provider: openai
tool_calls:
  - tool_name: web_search
    timestamp: 2026-04-14T10:00:00Z
rag_chunks:
  - chunk_id: chunk_001
    source_url: https://example.com/docs/page1
    retrieval_score: 0.88
output_hash: null    # <-- COMPLIANCE VIOLATION
otel_span_id: a1b2c3d4e5f60718
```

**Why this FAILS**: `output_hash: null` triggers Hard Gate H05 failure. Score = 0.0. A grounding record without an output-hash cannot prove the record corresponds to any specific output. Any post-market-monitoring audit based on this record would be invalid. The record also lacks `tool_input_hash`, `tool_output_hash`, and `content_hash` on RAG chunks.

**Fix**: Recompute SHA-256 from raw model output bytes. If the raw output is no longer available, the inference run must be re-executed under proper instrumentation.

## Example 3 -- ANTI-EXAMPLE: RAG Chunks Without source_url (Score: 2.1 -- D2: 0.0)

```markdown
inference_id: 9b8a7c6d-...
model:
  id: claude-sonnet-4-6
  provider: anthropic
rag_chunks:
  - chunk_id: chunk_abc
    source_url: null      # <-- BREAKS TRACEABILITY
    retrieval_score: 0.91
    content_hash: 1a2b3c...
  - chunk_id: chunk_def
    source_url: unknown   # <-- ALSO INVALID
    retrieval_score: 0.85
    content_hash: 2b3c4d...
output_hash: 7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f70
otel_span_id: b2c3d4e5f6071819
```

**Why this fails D2**: `source_url: null` and `source_url: "unknown"` are both invalid. The entire purpose of RAG-chunk provenance is to trace the output back to a specific source document. Without source_url, the grounding record cannot satisfy EU AI Act post-market-monitoring requirements or C2PA content credential binding.

**Fix**: Trace the chunk back through the vector store to its originating document. If the vector store does not record source metadata, the RAG pipeline must be updated to capture it before grounding records can be generated.

## Example Scoring Summary

| Example                             | H01-H08 | D1   | D2   | D3   | D4   | D5   | Overall |
|-------------------------------------|---------|------|------|------|------|------|---------|
| Golden (medical research agent)     | 8/8     | 9.5  | 9.5  | 9.0  | 10.0 | 9.5  | 9.5     |
| Anti-example 1 (missing hash)       | FAIL H05| --   | --   | --   | --   | --   | 0.0     |
| Anti-example 2 (no source URLs)     | 8/8     | 6.0  | 0.0  | 7.0  | 6.0  | 7.0  | 2.1*    |

*Weighted: (6.0*0.30 + 0.0*0.25 + 7.0*0.25 + 6.0*0.10 + 7.0*0.10) * 1.0 structural pass
= (1.80 + 0.0 + 1.75 + 0.60 + 0.70) = 4.85 rubric; semantic layer not triggered (< 8.5)

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
