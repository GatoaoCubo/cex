---
id: p01_kc_artifact_quality_evaluation_methods
kind: knowledge_card
pillar: P01
title: "Artifact Quality Evaluation Methods"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
domain: quality_assurance
quality: 9.2
tags: [quality-evaluation, hard-gates, soft-scoring, peer-review, quality-assurance, knowledge]
tldr: "Quality evaluation combines binary HARD gates (block failures) + weighted SOFT scoring (D1-D5) + peer review; thresholds: 7.0 use / 8.0 pool / 9.5 golden"
when_to_use: "When assessing artifact fitness for publication, identifying quality gaps, or designing validation pipelines for any CEX artifact kind"
keywords: [hard_gates, soft_scoring, peer_review, density_score, quality_dimensions]
long_tails:
  - How to evaluate artifact quality using hard and soft gates in CEX
  - What is the difference between HARD and SOFT quality gates
  - How to score artifact quality with D1-D5 weighted dimensions
  - When does an artifact pass quality review for publication
axioms:
  - ALWAYS run HARD gates before SOFT scoring — a HARD fail blocks regardless of SOFT score
  - NEVER self-assign quality score — external peer review assigns quality field
  - IF density_score < 0.80 THEN reject artifact before scoring other dimensions
  - ALWAYS set quality: null at creation — scoring is a separate peer review step
linked_artifacts:
  primary: p11_qg_knowledge_card
  related: [p01_kc_prompt_caching, p01_kc_rag_fundamentals]
density_score: 0.88
data_source: "https://github.com/anthropics/claude-code/issues"
related:
  - p01_kc_creation_best_practices
  - bld_knowledge_card_quality_gate
  - n04_qg_knowledge
  - bld_memory_quality_gate
  - p01_kc_knowledge_best_practices
  - p11_qg_quality_gate
  - bld_examples_invariant
  - bld_examples_axiom
  - bld_collaboration_quality_gate
  - p11_qg_creation_artifacts
---
# Artifact Quality Evaluation Methods

## Quick Reference
```yaml
topic: artifact_quality_evaluation_methods
scope: CEX quality gates, scoring, peer review — all artifact kinds
owner: quality_assurance
criticality: high
gate_types: HARD (binary) + SOFT (weighted 0-10)
publish_thresholds: "7.0 use | 8.0 pool | 9.5 golden"
```

## Key Concepts

| Concept | Definition | Applies To |
|---------|------------|------------|
| **HARD Gate** | Binary pass/fail — any fail = immediate reject | All artifact kinds |
| **SOFT Score** | Weighted 0-10 across dimensions D1-D5 | Post-HARD-pass artifacts |
| **Density Gate** | data_lines / total_non_empty_lines >= 0.80 | knowledge_card, context_doc |
| **Peer Review** | External qualified reviewer assigns `quality` | All published artifacts |
| **Publish Threshold** | Min score required per publication tier | Pool, golden, use |
| **quality: null** | Default at creation — never self-scored | Every artifact kind |

## Scoring Dimensions (D1–D5)

| Dim | Name | Weight | What It Measures |
|-----|------|--------|-----------------|
| D1 | Frontmatter Compliance | 20% | Required fields present, id matches filename, kind correct |
| D2 | Information Density | 25% | Ratio of concrete data to total content; tables > bullets > prose |
| D3 | Axiom Quality | 20% | ALWAYS/NEVER/IF-THEN form; actionable, not observational |
| D4 | Structure Completeness | 20% | >= 4 sections, each >= 3 non-empty lines, largest >= 30% of body |
| D5 | Format Adherence | 15% | >= 1 table + >= 1 code block + >= 1 URL; bullets <= 80 chars |

## Strategy Phases

1. **HARD Gate Pass**: Run automated validator; fix any binary failures before continuing
2. **Density Check**: Calculate data_lines / total; if < 0.80, restructure prose into tables/bullets
3. **SOFT Score**: Apply D1-D5 weighted formula; identify lowest-scoring dimension
4. **Threshold Decision**: Score >= 9.5 → golden; >= 8.0 → pool; >= 7.0 → use; < 7.0 → reject
5. **Peer Assignment**: Assign external reviewer; they write quality field in frontmatter
6. **Archive Signal**: Emit complete signal with score; log to experiments/results.tsv

## Golden Rules

- HARD gates are AND-logic: ALL must pass — one failure rejects the artifact
- SOFT scoring is weighted average: D2 (density 25%) outweighs D5 (format 15%)
- Self-scored `quality` field is always rejected — H05 hard gate catches any non-null value
- Retry budget: max 2 F6→F7 cycles; escalate to human review if score < 7.0 after 2 retries
- Tables over prose: tables carry ~3x information per line; prioritize in dense artifacts

## Evaluation Flow

```text
[Artifact Draft]
      |
      v
[HARD Gates: H01-H10]
      |
   FAIL -> [Fix & Retry] (max 2 cycles)
      |
   PASS
      v
[SOFT Score: D1-D5 weighted]
      |
      v
[Threshold Decision]
   < 7.0  -> Reject (return with gate report)
   7.0-7.9 -> Use tier (flag for improvement)
   8.0-9.4 -> Pool tier (publish + log pattern)
   >= 9.5  -> Golden (authoritative reference)
      |
      v
[Peer Review: external reviewer sets quality field]
      |
      v
[Archive + Signal: experiments/results.tsv + signal_writer]
```

## Comparativo: Evaluation Approaches

| Approach | Speed | Consistency | Coverage | Use Case |
|----------|-------|-------------|----------|----------|
| Automated HARD gates | < 1s | 100% | Syntax/compliance | CI pre-commit hook |
| Weighted SOFT score | < 5s | High | Content quality | Post-build validation |
| Peer review (human) | Hours | Medium | Subjective quality | Publication approval |
| LLM judge | ~10s | Medium | Semantic quality | Batch quality checks |
| A/B evaluation | Days | Low | User preference | Copy/marketing artifacts |

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| density < 0.80 | Too much prose | Replace paragraphs with bullet lists + tables |
| quality: X.X | Self-scored | Set quality: null; let peer review assign |
| Axiom as observation | "Caching helps" | Rewrite as "ALWAYS declare TTL when caching" |
| Missing required field | H06 fail | Add all 14 required frontmatter fields |
| Bullet > 80 chars | S10 fail | Split into two bullets or convert to table row |
| Body > 5120 bytes | H09 fail | Split into two focused atomic cards |

## References
- Source: https://docs.anthropic.com/en/docs/build-with-claude/overview
- Related artifact: p11_qg_knowledge_card (full HARD+SOFT gate spec)
- Related artifact: p01_kc_prompt_caching (golden density example, score 0.91)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_creation_best_practices]] | sibling | 0.36 |
| [[bld_knowledge_card_quality_gate]] | sibling | 0.34 |
| [[n04_qg_knowledge]] | related | 0.33 |
| [[bld_memory_quality_gate]] | downstream | 0.32 |
| [[p01_kc_knowledge_best_practices]] | sibling | 0.32 |
| [[p11_qg_quality_gate]] | downstream | 0.32 |
| [[bld_examples_invariant]] | downstream | 0.31 |
| [[bld_examples_axiom]] | downstream | 0.31 |
| [[bld_collaboration_quality_gate]] | downstream | 0.31 |
| [[p11_qg_creation_artifacts]] | downstream | 0.31 |
