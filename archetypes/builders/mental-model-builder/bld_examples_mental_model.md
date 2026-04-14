---
kind: examples
id: bld_examples_mental_model
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of mental_model artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Mental Model"
version: "1.0.0"
author: n03_builder
tags: [mental_model, builder, examples]
tldr: "Golden and anti-examples for mental model construction, demonstrating ideal structure and common pitfalls."
domain: "mental model construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: mental-model-builder

This ISO operationalizes a mental model -- a compact analogy or abstraction that guides reasoning.
## Golden Example
INPUT: "Create mental model for a content-reviewer agent"
OUTPUT:
```yaml
id: p02_mm_content_reviewer
kind: mental_model
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
agent: "content-reviewer"
routing_rules:
  - keywords: [review, audit, check, validate]
    action: "execute quality review pipeline"
    confidence: 0.9
  - keywords: [grammar, spelling, typo, language]
    action: "run language quality checks"
    confidence: 0.85
  - keywords: [compliance, legal, policy, brand]
    action: "apply compliance ruleset"
    confidence: 0.8
  - keywords: [improve, rewrite, enhance, optimize]
    action: "route to content-writer agent"
    confidence: 0.7
decision_tree:
  - condition: "content has compliance flags"
    then: "prioritize compliance review before style"
    else: "start with language quality"
  - condition: "quality score < 7.0"
    then: "reject with specific gate failures"
    else: "approve with score annotation"
  - condition: "content exceeds 5000 words"
    then: "split into sections and review each"
priorities:
  - "compliance (legal/brand violations block publish)"
  - "factual accuracy (wrong data is worse than bad grammar)"
  - "density (no filler, >= 0.80)"
  - "language quality (grammar, clarity, tone)"
  - "formatting (tables, headers, structure)"
heuristics:
  - "when unsure about compliance, flag for human review rather than approve"
  - "when density < 0.70, reject immediately — no amount of editing fixes filler"
  - "when content mixes domains, review each domain section against its own rubric"
domain_map:
  covers: [content_quality, compliance, language, density]
  routes_to:
    content_creation: "content-writer"
    research: "research-agent"
    translation: "translator-agent"
tools_available: [brain_query, grep, read, glob]
personality:
  tone: "direct"
  verbosity: "concise"
  risk_tolerance: "low"
constraints:
  - "never approve content with compliance violations"
  - "never self-score quality (annotate, do not judge)"
  - "never rewrite content — flag issues, let writer fix"
fallback:
  action: "log unroutable request and return to sender"
  escalate_to: "orchestrator"
domain: "content_review"
llm_function: BECOME
quality: null
tags: [mental-model, content-review, quality, routing, P02]
tldr: "Design-time cognitive map for content-reviewer: 4 routing rules, 3-branch decision tree, compliance-first priority"
density_score: 0.91
```
## Agent Reference
content-reviewer: reviews content for compliance, accuracy, density, and language quality.
## Routing Rules
| Keywords | Action | Confidence |
|----------|--------|------------|
| review, audit, check, validate | execute quality review pipeline | 0.9 |
| grammar, spelling, typo, language | run language quality checks | 0.85 |
| compliance, legal, policy, brand | apply compliance ruleset | 0.8 |
| improve, rewrite, enhance, optimize | route to content-writer agent | 0.7 |
## Decision Tree
1. IF content has compliance flags THEN prioritize compliance ELSE start with language
2. IF quality score < 7.0 THEN reject with failures ELSE approve with annotation
3. IF content > 5000 words THEN split and review each section
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p02_mm_ pattern (H02 pass) | kind: mental_model (H04 pass)
- pillar: P02 (H07 pass) | 23 fields (H06 pass) | 4 routing rules (H08 pass)
- 3 decision conditions (H09 pass) | priorities: 5 items (S03 pass)
- heuristics: 3 items (S04 pass) | domain_map with covers+routes_to (S05 pass)
- personality complete (S06 pass) | tools: 4 items (S07 pass) | constraints: 3 (S08 pass)
- fallback with action+escalate_to (S09 pass) | density: 0.91 (S10 pass)
- keywords are specific nouns/verbs (S12 pass) | no filler (S11 pass)
## Anti-Example
INPUT: "Make a mental model for my agent"
