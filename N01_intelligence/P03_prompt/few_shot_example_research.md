---
id: few_shot_example_research
kind: few_shot_example
pillar: P03
nucleus: n01
title: "N01 Research Few-Shot Examples"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.2
tags: [few_shot_example, in_context_learning, n01, research_quality, analytical_envy]
tldr: "4 labeled few-shot examples for N01 research quality calibration: 2 high-quality (score 9+) and 2 low-quality (score 6-7) with annotations explaining the difference. Used to ground llm_judge_n01 scoring."
density_score: 0.89
updated: "2026-04-17"
---

<!-- 8F: F1 constrain=P03/few_shot_example F2 become=few-shot-example-builder F3 inject=scoring_rubric_research+eval_framework_n01+llm_judge_n01 F4 reason=calibration examples make the rubric operational -- without concrete examples of what 9.0 and 6.0 look like, judges drift; few-shot examples anchor the scale F5 call=cex_compile F6 produce=few_shot_example_research.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P03_prompt/ -->

## Purpose

The eval_framework and scoring_rubric define the scale abstractly.
These examples make the scale concrete. Used by:
- llm_judge_n01 (in judge prompt as few-shot examples)
- Human reviewers (calibration reference)
- self_improvement_loop (as target quality reference)

## Example 1: HIGH QUALITY (Score 9.4)

**Topic**: "Claude API vs. OpenAI API pricing comparison, April 2026"

```
## Competitive Benchmark: AI API Pricing

| Provider | Input ($/1M tokens) | Output ($/1M tokens) | Context | Speed | Free Tier |
|----------|---------------------|----------------------|---------|-------|-----------|
| Anthropic Claude Sonnet | $3.00 | $15.00 | 200K | fast | no |
| OpenAI GPT-4o | $2.50 | $10.00 | 128K | fast | $5 credit |
| Google Gemini 1.5 Pro | $1.25 | $5.00 | 1M | medium | yes (limited) |
| Mistral Large | $2.00 | $6.00 | 32K | medium | no |

**Key Finding**: Google Gemini offers the lowest token cost at 60% discount vs. Claude,
but Claude's 200K context window [confidence: 0.92, source: anthropic.com/pricing 2026-04-15]
commands a premium for long-document use cases where context is the bottleneck, not price.

**Counter-argument**: For batch processing short prompts at scale, Google's pricing makes
it economically superior to Claude by ~2.5x -- a compelling case for cost-sensitive workloads
[confidence: 0.87, source: calculated from public pricing].

**Implications**:
1. Enterprise buyers: choose by use case. Context-heavy (Claude), cost-sensitive (Google).
2. Claude's 200K window is a defensible moat for document-heavy workflows.
3. OpenAI's mid-tier position (2nd most expensive) may face margin pressure as Gemini gains.
```

**Annotations**:
- D1 Source Quality = 9: primary sources (pricing pages) with dates and URLs
- D2 Analytical Depth = 9: identifies mechanism (context window as premium driver)
- D3 Comparative Coverage = 10: 4 providers, 5 metrics, quantified deltas
- D4 Claim Confidence = 9: every key claim has explicit confidence
- D5 Actionability = 9: 3 specific implications with target audiences
- Bias score = 8: no obvious confirmation bias, counter-argument present

## Example 2: HIGH QUALITY (Score 9.1)

**Topic**: "GitHub Copilot hiring velocity vs. Cursor vs. Tabnine, Q1 2026"

```
## Hiring Velocity Analysis: AI Code Assistant Market

| Company | Open Roles | 30d Delta | 90d Delta | Trending Direction |
|---------|-----------|-----------|-----------|------------------|
| GitHub Copilot (Microsoft) | 42 | +8% | +31% | RISING [confidence: 0.88] |
| Cursor | 18 | +24% | +67% | RISING FAST [confidence: 0.91] |
| Tabnine | 7 | -14% | -22% | FALLING [confidence: 0.84] |
| Category avg | -- | +6% | +18% | STABLE |

**Finding**: Cursor's 67% 90-day hiring surge (vs. category avg 18%) is the strongest signal
of competitive intent in this cohort [confidence: 0.89]. Paired with the series B raise
in January 2026, this represents a direct threat to Copilot's enterprise positioning.

**Tabnine signal**: 22% decline in open roles over 90 days strongly suggests contraction,
not optimization [confidence: 0.83]. Revenue pressure is likely.
```

**Annotations**:
- D3 Comparative Coverage = 10: 3 competitors + category average, trend quantified
- D4 Claim Confidence = 9: all claims labeled with confidence
- High signal-to-noise ratio; no padding

## Example 3: LOW QUALITY (Score 6.8)

**Topic**: "AI market is growing"

```
The AI market is growing rapidly. Many companies are investing in AI.
OpenAI is a major player and has raised billions. Google also has AI products.
According to a recent report, the AI market will reach $500B by 2030.
This shows that AI is an important technology.
```

**Annotations**:
- D1 Source Quality = 4: "recent report" not cited, no URL, no date
- D2 Analytical Depth = 3: pure description, zero analysis
- D3 Comparative Coverage = 2: OpenAI and Google mentioned but not compared
- D4 Claim Confidence = 2: "$500B by 2030" stated without source or confidence
- D5 Actionability = 1: "AI is important" is not actionable
- Analytical Envy violation: fails H06 (no comparison), H08 (no confidence scores)

## Example 4: LOW QUALITY (Score 7.2, with bias)

**Topic**: "Why ChatGPT is the best AI assistant"

```
ChatGPT is the best AI assistant on the market. It has the most users
and was the first major LLM product. OpenAI is well-funded and has
excellent researchers. The product is very capable and users love it.
[Source: OpenAI blog, 2025]
```

**Annotations**:
- D3 Comparative Coverage = 3: "best" stated without comparing to Claude, Gemini, Copilot
- B2 Confirmation bias = 4: pre-formed conclusion, supporting evidence only
- D1 Source Quality = 3: single source (OpenAI's own blog = not independent)
- Gate H06 fail: no competitive comparison despite superlative claim
- Gate H07 fail: "best" is a metaphor without quantified basis

**Fix path**: add comparison table (Claude, Gemini, GPT-4o, Llama), replace "best" with
ranked metric table, add independent sources (G2 reviews, academic benchmarks).

## Usage in llm_judge_n01

These examples are prepended to the judge prompt:

```
[CALIBRATION EXAMPLES]
Example A (score 9.4): {Example 1 text}
Example B (score 6.8): {Example 3 text}

Now evaluate the following research using the same rubric...
```
