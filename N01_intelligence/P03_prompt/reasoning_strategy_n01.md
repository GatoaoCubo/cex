---
id: reasoning_strategy_n01
kind: reasoning_strategy
pillar: P03
nucleus: n01
title: "N01 Structured Analytical Reasoning Protocol"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: null
tags: [reasoning_strategy, analytical_reasoning, n01, intelligence, structured_thinking, analytical_envy]
tldr: "5-step analytical reasoning protocol for N01: Decompose -> Source -> Triangulate -> Compare -> Synthesize. Analytical Envy lens forces competitive context at every step. Maps to 8F F4 REASON."
density_score: 0.92
---

<!-- 8F: F1 constrain=P03/reasoning_strategy F2 become=reasoning-strategy-builder F3 inject=search_strategy_n01+eval_framework_n01+bias_audit_n01+system_prompt_intelligence F4 reason=N01 needs a structured reasoning protocol to ensure Analytical Envy is operationalized -- not just a vibe but a method F5 call=cex_compile F6 produce=reasoning_strategy_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P03_prompt/ -->

## Purpose

Analytical Envy without method is just anxiety.
This strategy operationalizes N01's sin lens into a 5-step protocol
that applies at F4 REASON for every research task.

The protocol enforces two invariants:
1. No conclusion without comparison (Analytical Envy)
2. No comparison without confidence scores (epistemic integrity)

## The DSTCS Protocol (5 Steps)

### Step 1: DECOMPOSE

Break the research goal into atomic sub-questions.

| Input | Method | Output |
|-------|--------|--------|
| Research goal | 5W decomposition | 5-10 atomic questions |
| "Why is Anthropic growing?" | Who benefits? What mechanism? When did it start? Where is growth? Why that approach? | 8 atomic questions |

Analytical Envy check: for each sub-question, add the comparative variant:
- "What is X?" -> "What is X vs. Y, Z, and category avg?"
- "Why did A happen?" -> "Why did A happen here but not at B?"

### Step 2: SOURCE

For each atomic question, select sources from the search strategy:

| Question Type | Primary Source | Secondary Source | Confidence Floor |
|---------------|---------------|------------------|-----------------|
| Quantitative (how many, how much) | financial filings, APIs | news | 0.7 |
| Technical (how does X work) | papers, docs, GitHub | blogs | 0.6 |
| Strategic (why did X do Y) | press releases, exec interviews | analyst reports | 0.5 |
| Sentiment (what do users think) | G2, reviews, forums | social | 0.4 |
| Historical (what happened) | archives, Wayback Machine | news | 0.6 |

Minimum sources per question: 2. Hard fail at 1.

### Step 3: TRIANGULATE

For each atomic question, check source agreement:

```
answers = [s.answer(question) for s in sources]
consensus = cluster(answers, similarity_threshold=0.7)

if len(consensus) == 1:
    confidence = 0.9 if len(answers) >= 3 else 0.6
elif len(consensus) == 2:
    confidence = 0.5
    flag("CONTESTED: two camps, investigate root cause")
else:
    confidence = 0.2
    flag("CONFLICTING: investigate methodology differences")
```

### Step 4: COMPARE

Every finding must be placed in competitive context.

| Finding Type | Comparison Required | Example |
|-------------|---------------------|---------|
| Market size | vs. adjacent markets + YoY growth | "TAM $4B vs $6B for adjacent X, growing 23% vs 15%" |
| Pricing | vs. 3 competitors | "$29/mo vs OpenAI $20, Google $0 (free tier)" |
| Feature | vs. competitor parity | "Feature X: ahead of A, parity with B, behind C" |
| Revenue / growth | vs. category benchmark | "42% YoY vs SaaS median 28%" |
| Team / hiring | vs. competitor headcount signal | "50 new roles vs competitor 12 (4x hiring signal)" |

Analytical Envy fail: any finding that does NOT include competitive context.

### Step 5: SYNTHESIZE

Combine triangulated, compared findings into a structured output.

Synthesis template:

```
HEADLINE: [one sentence summary of the most important insight]
EVIDENCE: [top 3 supporting data points with confidence scores]
COMPARISON: [how this compares to alternatives/competitors]
CONFIDENCE: [overall confidence: high/medium/low with basis]
IMPLICATIONS: [2-3 actionable implications]
CAVEATS: [known limitations, gaps, contested findings]
```

## Reasoning Templates by Task Type

| Task Type | Decomposition | Emphasis | Output Format |
|-----------|--------------|----------|---------------|
| Competitive analysis | Who, What, Where (market), How (moat) | D3 Comparative Coverage | competitive matrix |
| Market sizing | TAM/SAM/SOM breakdown | quantitative sources | size table + growth |
| Technology assessment | Capability, Limitation, Trajectory | technical + adoption data | radar chart (table) |
| Investment signal | Growth, Moat, Risk, Team | financial + hiring signals | signal scorecard |
| Literature review | Consensus, Controversy, Gaps | academic sources | evidence map |

## Anti-Patterns (Analytical Envy Violations)

| Anti-Pattern | What It Looks Like | Fix |
|-------------|-------------------|-----|
| Single-entity focus | "Company X is doing well" | add 3 competitors to comparison |
| Vacuous positive | "strong growth" | quantify: "37% YoY vs 22% avg" |
| Confident without evidence | "X is the leader" | cite source + confidence 0-1 |
| Conclusion first | hypothesis built from conclusion | state hypothesis BEFORE research |
| Recency as depth | citing only last-30-day sources | add 1Y, 3Y historical context |

## Integration with 8F

```
F1 CONSTRAIN: apply step 1 (DECOMPOSE) to resolve research scope
F3 INJECT: apply step 2 (SOURCE) to select relevant KCs and sources
F4 REASON: apply steps 3-4 (TRIANGULATE + COMPARE) -- this is the core step
F6 PRODUCE: apply step 5 (SYNTHESIZE) to generate output
F7 GOVERN: eval_framework_n01.md validates D2 (depth) and D3 (comparison)
```

## Comparison vs. Alternative Reasoning Approaches

| Approach | Comparative Coverage | Source Rigor | N01 Fit |
|----------|---------------------|-------------|---------|
| Chain-of-thought (naive) | none | none | fail -- no comparison |
| MECE framework | medium | none | partial |
| SCAMPER | medium | none | creative but not rigorous |
| Intelligence analysis (ACH) | high | high | closest standard |
| This DSTCS protocol | high (Envy-driven) | high (triangulation) | optimal |

N01 specific: the COMPARE step (step 4) is not present in any standard reasoning framework.
It is the Analytical Envy innovation -- forced comparison as a reasoning step, not an afterthought.
