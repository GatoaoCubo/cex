---
kind: examples
id: bld_examples_ab_test_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of ab_test_config artifacts
quality: 8.8
title: "Examples Ab Test Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ab_test_config, builder, examples]
tldr: "Golden and anti-examples of ab_test_config artifacts"
domain: "ab_test_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
kind: ab_test_config
title: "Homepage CTA Optimization"
description: "A/B test to evaluate impact of CTA button color and headline text on conversion rate"
experiment_name: "HomepageCTAExperiment"
tool: "Google Optimize"
variables:
  - name: primary_button_color
    variants: ["#FF4B5C", "#3498DB", "#2ECC71"]
  - name: hero_headline
    variants: ["Upgrade Now", "Get Started Today", "Join Thousands"]
audience:
  - segment: "US users"
  - segment: "Mobile Safari users"
metrics:
  - conversion_rate
  - click_through_rate
schedule:
  start: "2023-11-01"
  end: "2023-12-15"
```

## Anti-Example 1: Confusing with feature flag
```yaml
kind: feature_flag
title: "Toggle for new button color"
description: "Enable/disable blue button on checkout page"
flag_name: "checkout_button_color"
state: "off"
```
## Why it fails
This is a feature flag configuration, not an A/B test. It lacks experiment variables, audience segmentation, and metrics tracking required for conversion optimization experiments.

## Anti-Example 2: Missing critical fields
```yaml
kind: ab_test_config
title: "CTA Experiment"
description: "Test different CTA texts"
variables:
  - name: call_to_action
    variants: ["Sign Up", "Register Now"]
```
## Why it fails
Incomplete configuration missing essential fields: experiment name, tool integration, audience definition, metrics tracking, and schedule. Cannot be implemented or measured as a valid A/B test.
