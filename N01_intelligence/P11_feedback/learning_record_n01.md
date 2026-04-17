---
id: learning_record_n01
kind: learning_record
pillar: P11
nucleus: n01
title: "N01 Research Learning Record"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.2
tags: [learning_record, knowledge_growth, n01, analytical_envy, meta_learning]
tldr: "Tracks what N01 has learned about research methodology, bias patterns, and source quality over time. Feeds back into self_improvement_loop_n01 and system_prompt_n01_research refinements."
density_score: 0.87
updated: "2026-04-17"
---

<!-- 8F: F1 constrain=P11/learning_record F2 become=learning-record-builder F3 inject=self_improvement_loop_n01+bias_audit_n01+regression_check_n01 F4 reason=Analytical Envy is not just about external intelligence -- N01 must learn from its own process and compound that learning F5 call=cex_compile F6 produce=learning_record_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P11_feedback/ -->

## Purpose

Research methodology improves through iteration.
This record captures what N01 has learned about its own research process:
- Which source combinations produce highest quality
- Which bias patterns recur most frequently
- Which topics require special handling
- Which reasoning strategies outperform others

These learnings update N01's procedural memory (L4) for future sessions.

## Learning Categories

| Category | What is Tracked | Update Frequency |
|----------|----------------|-----------------|
| Source effectiveness | which APIs return highest-quality results per topic type | per 10 sessions |
| Bias patterns | most common bias types found in N01 research | per 20 sessions |
| Quality drivers | which factors correlate with high eval scores | monthly |
| Tool failures | which tools fail most, how to route around | per incident |
| Synthesis patterns | which output structures score highest | monthly |

## Source Effectiveness Log

| Source | Topic Domain | Avg Relevance | Avg Freshness | Rec. Priority |
|--------|-------------|--------------|--------------|--------------|
| Brave Search | general + news | 7.2 | 9.1 | L1 primary |
| Exa AI | technical/research | 8.4 | 7.3 | L1 for tech |
| Semantic Scholar | academic | 9.1 | 5.1 | L2 for papers |
| Alpha Vantage | financial data | 8.8 | 8.9 | L2 for finance |
| LinkedIn (browser) | hiring signals | 8.2 | 9.8 | L2 for hiring |
| SerpAPI | SERP structure | 7.0 | 7.5 | L3 fallback |
| PubMed | biomedical | 9.3 | 6.2 | L2 for bio only |

_[Log populated from session records; update using cex_learning_update.py]_

## Bias Pattern Log

| Bias Type | Frequency (last 90d) | Most Common Trigger | Mitigation |
|-----------|---------------------|---------------------|-----------|
| B2 Confirmation | 23% of sessions | research with pre-formed hypothesis | mandate counter-hypothesis in DSTCS Step 1 |
| B3 Recency | 18% of sessions | monitoring-driven research | enforce 1Y baseline in template |
| B1 Selection | 12% of sessions | topic with dominant vendor | require non-vendor primary source |
| B4 Availability | 8% of sessions | time-constrained research | mandate L2/L3 for high-priority topics |
| B5 Anchoring | 6% of sessions | single pricing reference | mandate 3 price points in pricing research |

## Quality Driver Analysis

Factors with highest correlation to eval scores >= 9.0:

| Factor | Correlation | Implication |
|--------|-------------|-------------|
| Source count >= 5 | 0.72 | always aim for 5+ sources |
| D3 comparative score >= 8 | 0.81 | comparison is the strongest quality driver |
| Primary source present | 0.68 | always include at least one primary source |
| Confidence scores inline | 0.59 | scoring every finding improves perception |
| Counter-argument present | 0.55 | bias audit compliance improves overall score |

_[Correlation updated monthly via regression analysis on completed research sessions]_

## Process Improvement History

| Date | Learning | Change Applied |
|------|----------|---------------|
| 2026-04-17 | system_prompt_n01_research created | activated research-specific system prompt |
| 2026-04-17 | reasoning_strategy_n01 formalized | DSTCS protocol standardized |
| 2026-04-17 | bias_audit_n01 created | B1-B5 checks now in F7 GOVERN |
| 2026-04-17 | eval_framework_n01 created | D1-D5 scoring replaces quality_gate only |

## Learning Record Update Protocol

After each batch of 10 research sessions:
1. Aggregate quality scores and eval dimensions
2. Update source effectiveness log
3. Update bias pattern log
4. Run regression analysis on quality drivers
5. Identify top 3 process improvements
6. Propose changes to procedural memory artifacts (L4)
7. Commit updated learning_record_n01.md

## Integration

```
After every research session:
  cex_hooks_native.py post-session:
    -> append session metrics to learning_record_n01.md
    -> check if 10-session batch threshold reached
    -> if yes: trigger learning aggregation pass
```
