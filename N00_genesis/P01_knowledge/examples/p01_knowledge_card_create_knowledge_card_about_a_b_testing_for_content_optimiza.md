---
id: p01_kc_ab_testing_content_optimization
kind: knowledge_card
pillar: P01
title: "A/B Testing Framework for Content Optimization"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder"
domain: content_optimization
quality: 9.2
tags: [ab-testing, content-optimization, conversion, statistical-significance, knowledge]
tldr: "A/B testing content requires 95% confidence, minimum 100 conversions per variant, and 1-2 week test duration for statistical validity"
when_to_use: "When optimizing headlines, CTAs, copy, or layouts with measurable conversion goals"
keywords: [ab-testing, content-optimization, conversion-rate, statistical-significance]
long_tails:
  - How to calculate sample size for content A/B tests
  - Minimum test duration for statistically valid content experiments
axioms:
  - ALWAYS test one variable at time to isolate impact
  - NEVER stop tests before reaching statistical significance
  - IF conversion rate differs by <2%, THEN extend test duration
linked_artifacts:
  primary: null
  related: [p01_kc_conversion_copywriting_framework]
density_score: 0.89
data_source: "https://www.optimizely.com/optimization-glossary/ab-testing/"
related:
  - ab_testing_framework
  - ab-test-config-builder
  - kc_ab_test_config
  - pricing_experiment_tool
  - p03_sp_ab_test_config_builder
  - bld_knowledge_card_experiment_config
  - bld_knowledge_card_ab_test_config
  - p01_kc_experiment_config
  - bld_instruction_ab_test_config
  - p10_lr_experiment_config_builder
---
# A/B Testing Framework for Content Optimization

## Quick Reference
```yaml
topic: ab_testing_content
scope: Content variation testing with statistical validation
owner: marketing_optimization
criticality: high
```

## Key Concepts
- **Statistical Significance**: 95% confidence level (p-value ≤ 0.05) required for valid results
- **Minimum Sample Size**: 100+ conversions per variant; use online calculators for precise N
- **Test Duration**: 1-2 weeks minimum; 4+ weeks for seasonal/cyclical content
- **Effect Size**: 2-5% conversion lift detectable with standard sample sizes
- **Conversion Events**: Primary (purchase/signup) + Secondary (email, download, time-on-page)

## Strategy Phases
1. **Hypothesis**: Define specific prediction ("H1 headline will increase signups by 15%")
2. **Design**: Single variable change, 50/50 traffic split, conversion tracking setup
3. **Execute**: Run until statistical significance + minimum duration achieved
4. **Analyze**: Calculate confidence interval, effect size, practical significance
5. **Implement**: Deploy winner permanently, document learnings for future tests

## Golden Rules
- ISOLATE one variable: headline OR CTA OR layout, never multiple simultaneously
- RANDOMIZE traffic assignment using platform tools, not manual segmentation  
- MEASURE primary conversion metric + 2-3 secondary engagement metrics
- DOCUMENT test parameters, results, and insights in shared repository
- VALIDATE winner performs consistently over 2+ weeks post-implementation

## Flow
```text
[Hypothesis] → [Single Variable] → [50/50 Split] → [Traffic Assignment]
                                                          ↓
[Statistical Check] ← [Data Collection] ← [Conversion Tracking]
        ↓
[Significance: Yes] → [Implement Winner] → [Document Results]
        ↓
[Significance: No] → [Extend Test] → [Re-evaluate Sample Size]
```

## Comparativo
| Test Type | Duration | Sample Size | Confidence | Use Case |
|-----------|----------|-------------|------------|----------|
| Headlines | 1-2 weeks | 1000+ visitors | 95% | Landing pages, email subjects |
| CTA Buttons | 3-7 days | 500+ clicks | 95% | Conversion-focused pages |
| Email Copy | 2-4 weeks | 200+ opens | 90% | Campaign optimization |
| Page Layout | 2-3 weeks | 2000+ sessions | 95% | UX/conversion optimization |

## Statistical Requirements
| Metric | Minimum Threshold | Calculation |
|--------|------------------|-------------|
| Conversions | 100 per variant | Total traffic ÷ baseline conversion rate |
| Confidence Level | 95% (p ≤ 0.05) | Two-tailed t-test or chi-square |
| Effect Size | 2% relative lift | (Treatment - Control) ÷ Control × 100 |
| Test Duration | 7+ days | Account for weekly patterns, user behavior cycles |

## References
- Statistical methods: https://www.optimizely.com/optimization-glossary/ab-testing/
- Sample size calculator: https://www.evanmiller.org/ab-testing/sample-size.html
- Related: p01_kc_conversion_copywriting_framework (content optimization patterns)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[ab_testing_framework]] | downstream | 0.46 |
| [[ab-test-config-builder]] | downstream | 0.43 |
| [[kc_ab_test_config]] | sibling | 0.41 |
| [[pricing_experiment_tool]] | downstream | 0.29 |
| [[p03_sp_ab_test_config_builder]] | downstream | 0.29 |
| [[bld_knowledge_card_experiment_config]] | sibling | 0.28 |
| [[bld_knowledge_card_ab_test_config]] | sibling | 0.27 |
| [[p01_kc_experiment_config]] | sibling | 0.27 |
| [[bld_instruction_ab_test_config]] | downstream | 0.23 |
| [[p10_lr_experiment_config_builder]] | downstream | 0.21 |
