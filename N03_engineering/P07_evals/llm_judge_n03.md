---
id: p07_lj_n03
kind: llm_judge
8f: F7_govern
pillar: P07
title: "LLM Judge -- N03 Artifact Peer Review"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 9.2
tags: [llm-judge, N03, peer-review, quality, evaluation, semantic]
tldr: "LLM-as-judge configuration for N03 artifact peer review. Applied when L1+L2 structural+rubric score >= 8.5. Semantic evaluation across 3 criteria: domain accuracy, vocabulary compliance, engineering craft."
density_score: 0.90
updated: "2026-04-17"
related:
  - build_and_review
  - bld_collaboration_llm_judge
  - skill
  - p07_llm_judge
  - full_pipeline
  - llm-judge-builder
  - bld_output_template_llm_judge
  - p03_sp_engineering_nucleus
  - p01_kc_llm_judge
  - p01_kc_reward_signal
---

# LLM Judge: N03 Artifact Peer Review

## Purpose

The LLM judge is the L3 (semantic) layer of N03 quality validation.
Activated ONLY when L1 (structural) + L2 (rubric) composite score >= 8.5.
Prevents wasting LLM tokens on structurally deficient artifacts.

**Trigger condition:** `l1_score + l2_score >= 8.5 AND kind in PRIMARY_PILLAR_KINDS`

## Judge Configuration

| Parameter | Value |
|-----------|-------|
| Model | claude-sonnet-4-6 (N03 uses opus for builds; judge uses sonnet to save budget) |
| Temperature | 0.1 (deterministic evaluation) |
| Max tokens | 2048 |
| Role | Senior AI engineer reviewing artifact for production readiness |
| Output format | JSON: {criteria: [{id, score, rationale}], overall: float, recommendation: string} |

## Evaluation Criteria

### C1: Domain Accuracy (weight 40%)

**Question:** Is every claim in this artifact factually accurate within the CEX engineering domain?

| Score | Rubric |
|-------|--------|
| 9.5-10.0 | All claims verifiable; no ambiguity; cross-references accurate |
| 8.0-9.4 | All claims accurate; 1-2 could be clearer but not wrong |
| 6.0-7.9 | Mostly accurate; 1-2 claims need verification or are overly broad |
| < 6.0 | Factual error OR claim that contradicts canonical specs |

**Probe questions:**
- Do field types match CEX canonical definitions?
- Do file paths exist in the repo?
- Do referenced kinds exist in kinds_meta.json?
- Are 8F functions described correctly?

### C2: Vocabulary Compliance (weight 35%)

**Question:** Does this artifact use canonical CEX vocabulary throughout, with zero semantic drift?

| Score | Rubric |
|-------|--------|
| 9.5-10.0 | 100% canonical; every term maps to spec_metaphor_dictionary or kinds_meta |
| 8.0-9.4 | One non-canonical term present but not misleading |
| 6.0-7.9 | 2-3 non-canonical terms; no invented kinds or pillars |
| < 6.0 | Invented synonym for a canonical kind OR pillar misassignment |

**Red flags:**
- "research card" (should be knowledge_card)
- "brain query" (should be cex_retriever.py)
- "deck" used for artifact (should be agent_card or artifact)
- Custom quality score (should be quality: null + 5D model)

### C3: Engineering Craft (weight 25%)

**Question:** Would a senior AI engineer use this artifact as a production contract?

| Score | Rubric |
|-------|--------|
| 9.5-10.0 | Artifact is immediately usable; precise, dense, no gaps |
| 8.0-9.4 | Usable with minor additions; 1 section thin |
| 6.0-7.9 | Needs work; important edge cases missing |
| < 6.0 | Cannot be used as a contract; too abstract or incomplete |

**Craft signals:**
- Error handling documented (not assumed)
- Default values explicit, not "sensible"
- Examples use real CEX artifacts, not generic placeholders
- Edge cases addressed (empty input, conflicts, retries)

## Judge Prompt Template

```
You are a senior AI engineer performing quality review on a CEX artifact.
CEX is a typed knowledge system with 300 kinds, 12 pillars, 8 nuclei, and the 8F pipeline.

ARTIFACT TO REVIEW:
---
{artifact_content}
---

EVALUATION CONTEXT:
- Kind: {kind}
- Pillar: {pillar}
- Builder: N03 (Engineering, Inventive Pride)
- L1+L2 score: {l1_l2_score} (passed gate for semantic review)

EVALUATE on exactly 3 criteria:
1. Domain Accuracy (0-10): Are all facts correct within CEX engineering domain?
2. Vocabulary Compliance (0-10): Does it use canonical CEX vocabulary throughout?
3. Engineering Craft (0-10): Is this a production-quality engineering contract?

OUTPUT JSON only:
{
  "criteria": [
    {"id": "C1", "score": float, "rationale": "one sentence"},
    {"id": "C2", "score": float, "rationale": "one sentence"},
    {"id": "C3", "score": float, "rationale": "one sentence"}
  ],
  "overall": float,
  "recommendation": "approve|revise|reject",
  "revision_notes": "what specifically to fix if revise/reject"
}
```

## Composite with L1+L2

Final quality score formula when LLM judge runs:

```
final = (l1_score * 0.30) + (l2_score * 0.30) + (llm_score * 0.40)
```

| Recommendation | Action |
|----------------|--------|
| approve | Set artifact status=approved; mark quality: null (peer-reviewed by N07 later) |
| revise | Return to F6 with revision_notes injected; retry_count++ |
| reject | Write to signals/ as error; escalate to N07 |

## Budget Guard

LLM judge is skipped if:
- `dry_run=true`
- Artifact kind is in `LOW_PRIORITY_KINDS` (audit logs, changelogs, temp artifacts)
- Session token budget < 10K remaining
- Retry count > 0 (already revised once; accept with warning)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[build_and_review]] | downstream | 0.26 |
| [[bld_collaboration_llm_judge]] | downstream | 0.25 |
| [[skill]] | downstream | 0.24 |
| [[p07_llm_judge]] | sibling | 0.24 |
| [[full_pipeline]] | downstream | 0.23 |
| [[llm-judge-builder]] | related | 0.23 |
| [[bld_output_template_llm_judge]] | upstream | 0.23 |
| [[p03_sp_engineering_nucleus]] | upstream | 0.22 |
| [[p01_kc_llm_judge]] | related | 0.22 |
| [[p01_kc_reward_signal]] | downstream | 0.22 |
