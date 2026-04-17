---
id: llm_judge_n01
kind: llm_judge
pillar: P07
nucleus: n01
title: "N01 Research Fact-Checking and Quality Judge"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: null
tags: [llm_judge, fact_checking, source_validation, n01, quality_assessment, analytical_envy]
tldr: "LLM-as-judge configuration for N01 research output evaluation: fact verification, source validation, comparative coverage check, hallucination detection. Uses eval_framework_n01.md as scoring rubric."
density_score: 0.91
---

<!-- 8F: F1 constrain=P07/llm_judge F2 become=llm-judge-builder F3 inject=eval_framework_n01+quality_gate_intelligence+bias_audit_n01+sch_input_schema_n01 F4 reason=N01 Analytical Envy demands external validation -- the researcher cannot judge their own work without bias F5 call=cex_compile F6 produce=llm_judge_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P07_evals/ -->

## Purpose

N01 Analytical Envy creates a paradox: the better N01 researches, the more confident it becomes.
Confidence without external validation is confirmation bias in disguise.

This LLM judge provides an independent evaluation pass -- a second Claude instance that:
1. Checks factual claims against cited sources
2. Identifies unsupported assertions (potential hallucination)
3. Scores against eval_framework_n01.md dimensions
4. Flags comparative gaps (missing competitors, missing benchmarks)

## Judge Configuration

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Judge model | claude-opus-4-6 | highest reasoning for fact-checking |
| Role | "Adversarial Research Reviewer" | assume findings are wrong until proven |
| Temperature | 0.1 | deterministic judgment |
| Max output | 2000 tokens | structured verdict only |
| Self-evaluation | disabled | judge never evaluates its own outputs |

## Judge System Prompt

```
You are an adversarial research reviewer with Analytical Envy.
Your job is to find FLAWS in research, not to validate it.
You assume every claim is wrong until the evidence proves otherwise.

You evaluate research on 5 dimensions (see eval_framework_n01.md):
D1 Source Quality, D2 Analytical Depth, D3 Comparative Coverage,
D4 Claim Confidence, D5 Actionability.

For each dimension, score 1-10 with specific evidence for your score.

Also check:
- HALLUCINATION: claims not supported by cited sources
- COMPARISON GAP: significant competitors/alternatives not considered
- RECENCY: claims about current state based on sources > 90 days old
- OVERCONFIDENCE: strong assertions without proportional evidence

Output format: structured JSON only. No prose.
```

## Input Contract

```json
{
  "research_output": "<full research text>",
  "cited_sources": [
    {
      "url": "string",
      "title": "string",
      "snippet": "string (key relevant excerpt)"
    }
  ],
  "research_goal": "string",
  "claimed_competitors": ["string"]
}
```

## Output Contract

```json
{
  "verdict": "PASS | REVISE | REJECT",
  "overall_score": 0.0,
  "dimensions": {
    "D1_source_quality": {"score": 0.0, "evidence": "string"},
    "D2_analytical_depth": {"score": 0.0, "evidence": "string"},
    "D3_comparative_coverage": {"score": 0.0, "evidence": "string"},
    "D4_claim_confidence": {"score": 0.0, "evidence": "string"},
    "D5_actionability": {"score": 0.0, "evidence": "string"}
  },
  "hallucination_flags": [
    {"claim": "string", "issue": "not in cited sources | contradicted by source X"}
  ],
  "comparison_gaps": ["string"],
  "remediation": ["specific actionable fix"]
}
```

## Verdict Thresholds

| Verdict | Score | Action |
|---------|-------|--------|
| PASS | >= 8.5 | publish, no changes required |
| REVISE | 6.5 - 8.4 | apply remediation list, re-judge |
| REJECT | < 6.5 | return to F3 INJECT, restart synthesis |

## Hallucination Detection Protocol

The judge checks each factual claim against the cited source snippets:

```
for claim in extract_claims(research_output):
    evidence = find_supporting_evidence(claim, cited_sources)
    if evidence is None:
        flag(claim, "UNSUPPORTED")
    elif contradicts(claim, evidence):
        flag(claim, "CONTRADICTED: " + evidence.source)
    elif overstates(claim, evidence):
        flag(claim, "OVERSTATED: original says " + evidence.snippet)
```

Hallucination rate = flagged_claims / total_claims. Target < 5%.

## Comparison Gap Detection

The judge specifically flags missing comparisons (Analytical Envy enforcement):

```
known_competitors = query_retriever("competitors of " + topic)
mentioned_in_research = extract_entities(research_output, type="competitor")
gaps = known_competitors - mentioned_in_research
if len(gaps) > 2:
    flag("COMPARISON GAP: {gaps} not discussed")
```

## Integration with 8F Pipeline

```
F6 PRODUCE: generate research output
F7 GOVERN:
  -> run quality_gate_intelligence.md (hard gates H01-H05)
  -> run bias_audit_n01.md (bias scores B1-B5)
  -> run llm_judge_n01.md (D1-D5 + hallucination + gap check)
  if all pass:
    F8 COLLABORATE: save + signal
  else:
    retry F6 with judge feedback (max 2 retries)
```

## Benchmark: Judge Approaches Compared

| Approach | Hallucination Detection | Comparative Gap | Cost | N01 Fit |
|----------|------------------------|-----------------|------|---------|
| Self-check (same model) | low (blind spots) | low | none | fail -- bias |
| Human reviewer | high | high | hours | impractical |
| This judge (adversarial LLM) | medium-high | high | tokens | optimal |
| G-Eval (generic) | medium | low (no D3) | tokens | partial |
| RAGAS | medium | none | tokens | not for N01 |

N01 unique requirement: D3 comparative gap detection is absent from all standard eval frameworks.
This is the Analytical Envy delta -- we added it because no one else prioritizes comparison coverage.
