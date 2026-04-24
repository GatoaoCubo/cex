---
id: action_prompt_n01
kind: action_prompt
8f: F6_produce
pillar: P03
nucleus: n01
title: "N01 Research Action Prompts"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.1
tags: [action_prompt, research_actions, n01, analytical_envy, structured_prompts]
tldr: "Library of 8 action prompts for N01 research operations: competitive analysis, market sizing, literature review, source triangulation, entity extraction, bias check, trend detection, synthesis. Each enforces Analytical Envy lens."
density_score: 0.90
updated: "2026-04-17"
related:
  - p11_qg_intelligence
  - p03_sp_intelligence_nucleus
  - p10_out_market_snapshot
  - p12_wf_intelligence
  - p01_kc_source_triangulation
  - p06_schema_research_depth
  - bld_collaboration_entity_memory
  - p10_lr_research_sessions
  - p10_out_source_dossier
  - p10_out_research_brief
---

<!-- 8F: F1 constrain=P03/action_prompt F2 become=action-prompt-builder F3 inject=system_prompt_n01_research+reasoning_strategy_n01+prompt_template_intelligence F4 reason=discrete action prompts are reusable, testable, and composable -- they operationalize the system_prompt into specific executable instructions F5 call=cex_compile F6 produce=action_prompt_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P03_prompt/ -->

## Purpose

Action prompts are discrete, callable instructions that implement specific research operations.
Unlike the system_prompt (sets identity), action prompts drive specific F6 PRODUCE steps.
Each prompt enforces Analytical Envy: comparison is built into the instruction, not optional.

## Action Prompt Library

### AP-01: Competitive Analysis

```
Analyze {entity} in the context of {market}.

Required output structure:
1. Entity profile: what {entity} does, for whom, at what price
2. Competitive position: rank {entity} against {competitors} on: {metrics}
3. Competitive advantages: what {entity} does better than alternatives
4. Competitive gaps: where {entity} trails competitors
5. Strategic trajectory: where {entity} appears to be heading

Constraints:
- Compare quantitatively on at least 3 metrics
- Include source and date for every data point
- Add [confidence: X] after every claim
- Flag any metric where {entity} leads with [EDGE] and where it trails with [GAP]
```

### AP-02: Market Sizing

```
Estimate TAM, SAM, SOM for {market} in {year}.

Methodology:
1. TAM: total addressable market (top-down from analyst reports AND bottom-up from unit economics)
2. SAM: serviceable addressable market (geographic + segmentation filters)
3. SOM: serviceable obtainable market (realistic capture given competitive dynamics)

Required comparisons:
- YoY growth rate vs. adjacent markets
- Compare TAM estimates from >= 2 analyst sources (Gartner, CB Insights, IDC)
- Flag discrepancies between sources

Output: table with three rows (TAM/SAM/SOM), source column, confidence column
```

### AP-03: Literature Review

```
Synthesize academic research on {topic}.

Steps:
1. Identify 5-10 seminal papers (high citation count) on {topic}
2. Identify 3-5 recent papers (< 2 years, high velocity) on {topic}
3. Synthesize: what is the consensus? where do papers disagree?
4. Identify research gaps: what has NOT been studied?

Required output:
- Evidence map: table of papers with year, citations, key finding
- Consensus finding (high confidence only)
- Contested finding (low confidence, flag sources)
- Research gap: 2-3 open questions the literature has not answered
```

### AP-04: Source Triangulation

```
Triangulate the following claim: "{claim}"

Process:
1. Find >= 3 independent sources supporting or refuting this claim
2. For each source: URL, date, excerpt, confidence contribution
3. If sources agree: composite confidence = min(0.95, source_avg * 1.1)
4. If sources disagree: report both positions with evidence
5. Conclude: claim validity with composite confidence score

Output format:
Claim: {claim}
Verdict: SUPPORTED | CONTESTED | REFUTED
Confidence: X.XX
Sources: [table]
Counter-evidence: [if any]
```

### AP-05: Entity Extraction

```
Extract structured data from the following text.

Target type: {entity_type} (from sch_type_def_n01.md)
Text: {raw_text}

Rules:
- Use null for missing fields, not guesses
- Include extraction_confidence (0-1) for each field
- Flag any field where the text is ambiguous with [AMBIGUOUS]
- Output: valid JSON matching the {entity_type} schema
```

### AP-06: Bias Check

```
Audit the following research for bias.

Research: {research_text}

Check each bias type:
B1 Selection: are sources diverse in type, geography, organization?
B2 Confirmation: does the conclusion align too strongly with the hypothesis?
B3 Recency: are all sources from the same time window?
B4 Availability: are only easy-to-find sources used?
B5 Anchoring: does one source disproportionately drive the conclusion?

Output: bias report (JSON) with scores per type and specific evidence for each flag.
```

### AP-07: Trend Detection Prompt

```
Detect trends for {entity} in {category} over {time_window}.

Data: {time_series}

Calculate:
1. Baseline: average over first 50% of time window
2. Recent: average over last 25% of time window
3. Trend score: (recent - baseline) / baseline
4. Direction: RISING | STABLE | FALLING (threshold: +/- 20%)
5. Confidence: based on data point count and variance

Compare to: {competitors} on same metric.
Output: trend table with all entities ranked by trend_score.
```

### AP-08: Research Synthesis

```
Synthesize findings from the following research into a structured intelligence brief.

Findings: {findings_list}

Structure:
HEADLINE: [1 sentence: the most important insight]
EVIDENCE: [top 3 data points with confidence]
COMPETITIVE CONTEXT: [how this compares to alternatives]
IMPLICATIONS: [2-3 actionable implications for {target_audience}]
CONFIDENCE: [overall research confidence with basis]
CAVEATS: [known gaps, contested points, limitations]
COUNTER-ARGUMENT: [strongest argument against the main conclusion]
```

## Usage Pattern

Action prompts are called at F6 PRODUCE:
```
task_type = classify_task(handoff)
selected_prompt = AP_LIBRARY[task_type]
filled_prompt = fill_slots(selected_prompt, task_context)
output = llm.generate(system=system_prompt_n01_research, user=filled_prompt)
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_intelligence]] | downstream | 0.40 |
| [[p03_sp_intelligence_nucleus]] | related | 0.36 |
| [[p10_out_market_snapshot]] | downstream | 0.29 |
| [[p12_wf_intelligence]] | downstream | 0.28 |
| [[p01_kc_source_triangulation]] | upstream | 0.25 |
| [[p06_schema_research_depth]] | downstream | 0.25 |
| [[bld_collaboration_entity_memory]] | downstream | 0.24 |
| [[p10_lr_research_sessions]] | downstream | 0.24 |
| [[p10_out_source_dossier]] | downstream | 0.24 |
| [[p10_out_research_brief]] | downstream | 0.23 |
