---
id: p01_kc_system_testing_patterns
kind: knowledge_card
pillar: P01
title: "System Testing Patterns"
version: "1.0.0"
created: "2023-10-09"
updated: "2023-10-09"
author: "knowledge-card-builder"
domain: "Software Engineering"
quality: null
tags: [system testing, testing patterns, software quality, test automation]
tldr: "Overview of system testing patterns like smoke, sanity, and regression for software quality."
when_to_use: "When planning system testing strategies for comprehensive test coverage."
keywords: [system testing, smoke testing, regression testing]
long_tails:
  - How to apply smoke testing in continuous integration
  - Benefits of regression testing in software rollouts
axioms:
  - ALWAYS ensure test patterns align with testing objectives
linked_artifacts:
  primary: null
  related: []
density_score: 0.85
data_source: "https://softwaretestingfundamentals.com/types-of-software-testing/"

---

## Quick Reference
topic: system_testing_patterns
scope: Software testing patterns and strategies
owner: knowledge-card-builder
criticality: high

## Key Concepts
- **Smoke Testing**: Verifies basic functionality without detailed examination.
- **Sanity Testing**: Confirms that recent changes work without further disrupting existing features.
- **Regression Testing**: Ensures new changes don't break existing features.

## Strategy Phases
1. **Identify Patterns**: Select appropriate testing patterns based on project needs.
2. **Implement Tests**: Develop tests using the chosen patterns to cover all functionalities.
3. **Monitor Results**: Analyze test outcomes to improve future testing strategies.

## Golden Rules
- Use **smoke tests** to quickly validate critical paths.
- Apply **sanity tests** after minor bug fixes or tweaks.
- Conduct **regression tests** before major releases.

## Flow
[Code Change] -> [Select Pattern] -> [Apply Test] -> [Analyze Results]

## Comparativo
| Pattern Type     | Purpose                      | Frequency            |
|------------------|------------------------------|----------------------|
| Smoke Testing    | Basic functionality check    | On each build        |
| Sanity Testing   | Verify specific fixes        | Post-bug fix         |
| Regression Testing | Ensure no new bugs introduced | Pre-release cycle    |

## References
- Related artifact: null
- Source: https://softwaretestingfundamentals.com/types-of-software-testing/