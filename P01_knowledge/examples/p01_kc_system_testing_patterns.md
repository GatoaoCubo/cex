---
id: p01_kc_system_testing_patterns
kind: knowledge_card
pillar: P01
title: "System Testing Patterns"
version: "1.0.0"
created: "2023-10-21"
updated: "2023-10-21"
author: "knowledge-card-builder"
domain: "software_testing"
quality: null
tags: [system_testing, testing_patterns, software_quality]
tldr: "Common system testing patterns enhance software validation and efficiency."
when_to_use: "When designing system testing strategies for comprehensive validation."
keywords: [smoke_testing, sanity_testing, regression_testing]
long_tails:
  - "how to implement regression testing strategy effectively"
  - "best practices for conducting end-to-end testing"
axioms:
  - "ALWAYS integrate regression testing post modifications."
linked_artifacts:
  primary: null
  related: []
density_score: 0.92
data_source: "https://www.softwaretestinghelp.com/system-testing-patterns/"
---

# System Testing Patterns

## Quick Reference
topic: System Testing Patterns
scope: Software Testing Strategy
owner: Software Testing Team
criticality: high

## Key Concepts
- **Smoke Testing**: Initial testing to check the basic functionality.
- **Sanity Testing**: Focus on verifying specific functionalities after minor changes.
- **Regression Testing**: Ensures new changes don't disrupt existing functionalities.

## Strategy Phases
1. **Identify Critical Paths**: Focus tests on commonly used application flows.
2. **Prioritize Test Cases**: Assign importance based on functionality criticality.
3. **Automate Repetitive Tests**: Use scripts to execute frequent tests efficiently.

## Golden Rules
- ALWAYS automate repetitive regression tests.
- NEVER skip smoke testing before proceeding with detailed tests.
- IF deploying a patch, THEN perform sanity testing to ensure no specific features were disrupted.

## Flow
[Plan Tests] -> [Execute Tests] -> [Analyze Results] -> [Iterate]

## Comparativo
| Pattern            | Use Case                              | Benefit                      |
|--------------------|---------------------------------------|------------------------------|
| Smoke Testing      | Initial build validation              | Quick validation             |
| Sanity Testing     | Post minor updates                    | Specific functionality check |
| Regression Testing | After changes in code base            | Stability assurance          |

## References
- Source: https://www.softwaretestinghelp.com/system-testing-patterns/