---
kind: quality_gate
id: p11_qg_reasoning_trace
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of reasoning_trace artifacts
pattern: few-shot learning for structured decision audit records
quality: 9.0
title: 'Gate: Reasoning Trace'
version: 1.0.0
author: builder
tags:
- eval
- P11
- quality_gate
- examples
tldr: Gates ensuring reasoning traces define complete step-evidence-confidence chains,
  record rejected alternatives, calibrate confidence scores, and contain no execution
  instructions.
domain: reasoning_trace
created: '2026-04-06'
updated: '2026-04-06'
density_score: 0.85
related:
  - p03_ins_reasoning_trace_builder
  - bld_knowledge_card_reasoning_trace
  - bld_schema_reasoning_trace
  - p03_sp_reasoning_trace_builder
  - bld_memory_reasoning_trace
  - bld_examples_reasoning_trace
  - bld_collaboration_reasoning_trace
  - p01_kc_reasoning_trace
  - reasoning-trace-builder
  - bld_output_template_reasoning_trace
---

## Quality Gate

## Definition
A reasoning_trace is a structured decision record capturing WHY an agent chose a particular path. It passes this gate when every step has concrete evidence, confidence is calibrated to the 0.0-1.0 scale, at least one alternative is rejected with an evidence-based reason, the conclusion references the strongest evidence, and the trace contains no execution instructions or workflow logic.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches pattern `p03_rt_{agent}_{timestamp}` | Mismatched IDs cause routing failures |
| H03 | `kind` is exactly `reasoning_trace` (literal match) | Kind drives the loader; wrong literal silently misroutes |
| H04 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H05 | `agent` field is non-empty string | Traces without agent attribution cannot be audited |
| H06 | `intent` field is non-empty string | Traces without intent have no decision context |
| H07 | `steps` is a non-empty list with >= 2 entries | Single-step traces are assertions, not reasoning chains |
| H08 | Each step has non-empty `thought`, `evidence`, and `confidence` fields | Missing fields break the step-evidence-confidence contract |
| H09 | All `confidence` values are numeric in range 0.0-1.0 | Out-of-range values break geometric mean calculation |
| H10 | `conclusion` is non-empty string | Traces without conclusions are incomplete |
| H11 | `timestamp` is valid ISO 8601 datetime | Untimestamped traces cannot be ordered or deduplicated |
| H12 | Total YAML size <= 8192 bytes | Oversized traces exceed budget and slow consumers |
| H13 | Trace contains NO execution instructions or action items | Reasoning traces record WHY, not WHAT to do |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Evidence concreteness (references specific data, files, metrics vs vague claims) | 1.5 | Vague assertions ("it seemed better") | Some references ("benchmark showed improvement") | All steps cite specific metrics, files, or data points |
| 3 | Confidence calibration (scores match evidence strength, not over/under-confident) | 1.5 | All steps 0.9+ regardless of evidence | Most steps reasonably calibrated | Confidence clearly tracks evidence strength; low evidence = low confidence |
| 4 | Alternatives rejected with reasons (at least 1 rejected path with evidence-based reason) | 1.0 | No alternatives listed | Alternatives listed without reasons | Each alternative has specific evidence-based rejection reason |
| 5 | Conclusion references evidence (final decision cites strongest supporting data) | 1.0 | Conclusion is unsupported opinion | Conclusion mentions evidence vaguely | Conclusion directly references specific step evidence |
| 6 | Step ordering is logical (chronological or logical progression, no jumps) | 0.5 | Steps in random order | Mostly ordered | Clear logical/chronological progression |
| 7 | Tags include `reasoning_trace` | 0.5 | Missing | Present but misspelled | Exactly `reasoning_trace` in tags list |
| 8 | Duration_ms present when timing data available | 0.5 | Timing available but omitted | Present but approximate | Precise timing data included |

## Examples

# Examples: reasoning-trace-builder
## Golden Example
INPUT: "Record why research-agent selected ada-002 over cohere-embed-v3 for P01 retriever"
OUTPUT (`p03_rt_research_agent_20260406T143000.yaml`):
```yaml
agent: research-agent
intent: select embedding model for P01 retriever
steps:
  - step: 1
    thought: OpenAI ada-002 is the most widely deployed embedding model with extensive documentation
    evidence: "MTEB benchmark: 63.4% average, 8191 token limit, $0.0001/1K tokens, 1536 dimensions"
    confidence: 0.8
  - step: 2
    thought: Cohere embed-v3 offers higher benchmark scores and multilingual support
    evidence: "MTEB benchmark: 66.1% average, 512 token limit, requires API key rotation every 90 days"
    confidence: 0.7
  - step: 3
    thought: Our chunk size is 512 tokens — both models handle this, but ada-002 has 16x headroom
    evidence: "P01 embedding_config.yaml shows chunk_size=512, overlap=64"
    confidence: 0.9
  - step: 4
    thought: Cost comparison favors ada-002 for our projected volume of 50K documents/month
    evidence: "ada-002: ~$5/month at 50K docs; cohere-v3: ~$12/month at same volume (pricing page 2026-03)"
    confidence: 0.85
conclusion: "Selected ada-002 — 16x token headroom over chunk size, 58% lower cost at projected volume, and no API key rotation overhead. The 2.7% MTEB gap does not justify the operational complexity of cohere-v3."
alternatives_rejected:
  - alternative: Cohere embed-v3
    reason: "Higher MTEB score (+2.7%) but 512 token limit matches chunk size exactly (zero headroom), 2.4x higher cost, and API key rotation adds operational burden"
  - alternative: Local sentence-transformers (all-MiniLM-L6-v2)
    reason: "Zero API cost but 384 dimensions (vs 1536) reduces retrieval precision, and self-hosting adds infra maintenance"
confidence: 0.81
timestamp: "2026-04-06T14:30:00-03:00"
duration_ms: 4500
```
WHY THIS IS GOLDEN:
- filename follows `p03_rt_{agent}_{timestamp}.yaml`
- all required fields present: agent, intent, steps, conclusion, confidence, timestamp
- each step has thought + concrete evidence + calibrated confidence
- alternatives_rejected has evidence-based rejection reasons
- conclusion directly references step evidence (token headroom, cost, MTEB gap)
- overall confidence (0.81) is geometric mean of step confidences
- no execution instructions, no workflow logic
## Golden Low-Confidence Example
OUTPUT (`p03_rt_build_sat_20260406T160000.yaml`):
```yaml
agent: build-sat
intent: determine if kc_toolkit.md needs restructuring
steps:
  - step: 1
    thought: Current KC has 3 sections but toolkit kind has expanded to cover MCP mapping
    evidence: "kc_toolkit.md last updated 2026-02-15; toolkit-builder added MCP fields 2026-03-20"
    confidence: 0.7
  - step: 2
    thought: No user complaints about KC accuracy reported in feedback logs
    evidence: "grep of .cex/learning_records/ shows 0 entries mentioning kc_toolkit"
    confidence: 0.3
conclusion: "Insufficient evidence to justify restructuring — no user-reported issues, but KC is 5 weeks stale relative to builder updates. Recommend monitoring for 2 more weeks."
alternatives_rejected:
  - alternative: Immediate restructuring
    reason: "No concrete evidence of user impact; restructuring without cause wastes builder cycles"
confidence: 0.46
timestamp: "2026-04-06T16:00:00-03:00"
duration_ms: 2100
```
WHY THIS PASSES:
- low confidence (0.46) correctly reflects weak evidence at step 2
- conclusion honestly states insufficient evidence
- step 2 confidence capped at 0.3 due to absence-of-evidence reasoning
- would trigger memory feedback loop (confidence < 0.5)
## Anti-Example
BAD OUTPUT (`p03_rt_agent.md`):
```markdown
# Reasoning Trace
The agent decided to use ada-002 because it's a good model.
We considered other options but ada-002 seemed best.
Confidence: high.
```
FAILURES:
1. wrong format: markdown prose instead of structured YAML
2. wrong extension: `.md` instead of `.yaml`
3. no `agent` field — who reasoned?
4. no `steps` list — no chain-of-thought structure
5. no `evidence` — "it's a good model" is assertion, not reasoning
6. confidence is string "high" instead of numeric 0.0-1.0
7. no `alternatives_rejected` — what else was considered?
8. no `timestamp` — when was this decided?
9. includes no concrete data — completely unauditable
## Anti-Example: Instruction Drift
BAD OUTPUT (`p03_rt_build_sat_20260406.yaml`):
```yaml
agent: build-sat
intent: build landing page
steps:
  - step: 1
    thought: First, create the hero section with a CTA button
    evidence: "landing page best forctices document"
    confidence: 0.9
  - step: 2
    thought: Then add testimonials section below the fold
    evidence: "conversion rate optimization guide"
    confidence: 0.85
next_actions:
  - "Create hero section HTML"
  - "Add testimonials component"
  - "Deploy to staging"
```
FAILURES:
1. steps describe WHAT to do, not WHY a decision was made — this is an instruction
2. `next_actions` is an execution directive — belongs in instruction artifact
3. evidence is vague document references, not concrete data
4. no `conclusion`, no `alternatives_rejected`, no `timestamp`
5. this artifact is an instruction masquerading as a reasoning trace

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
