---
id: p01_kc_system_testing_patterns
kind: knowledge_card
pillar: P01
title: "System Testing Patterns"
version: 1.0.0
created: 2023-11-01
updated: 2023-11-01
author: "Knowledge Distillation Specialist"
domain: Software Testing
quality: null
tags: [system_testing, testing_patterns, software_quality, knowledge]
tldr: "Outlines types and applications of system testing patterns, enhancing QA."
when_to_use: "When designing or improving system testing strategies."
keywords: [system testing, testing patterns, QA]
long_tails:
  - How to apply system testing patterns for better software quality
  - Examples of effective system testing strategies
axioms:
  - ALWAYS analyze project requirements before selecting testing patterns
linked_artifacts:
  primary: null
  related: []
density_score: 0.85
data_source: "https://www.softwaretestingmaterial.com/system-testing/"

---

# System Testing Patterns

## Quick Reference
topic: System Testing Patterns
scope: Detailed patterns and methodologies for enhancing software quality assurance through systematic and structured testing processes.
owner: Knowledge Distillation Specialist
criticality: high

## Key Concepts
- **Scenario Testing**: Simulate real-world use cases for application robustness.
- **Smoke Testing**: Initial testing to catch major failures before deeper checks.
- **Regression Testing**: Verifies new code changes have not disrupted existing functionality.

## Strategy Phases
1. **Identify Needs**: Determine project-specific testing requirements.
2. **Design Patterns**: Choose appropriate testing approaches like scenario or smoke.
3. **Implement and Monitor**: Execute tests and continuously assess test coverage.

## Golden Rules
- ALWAYS start with smoke testing to identify major issues early.
- NEVER skip regression testing after code alterations, regardless of size.
- IF possible, automate repetitive tests for efficiency.

## Flow
[Identify Requirements] -> [Design Tests] -> [Execute Tests] -> [Assess Results]

## Comparativo
| Pattern | Time Efficiency | Coverage Depth |
|---------|----------------|----------------|
| Smoke | Fast | Shallow |
| Scenario | Moderate | Deep |
| Regression | Slow | Comprehensive |

## References
- Related artifact: None
- Source: https://www.softwaretestingmaterial.com/system-testing/