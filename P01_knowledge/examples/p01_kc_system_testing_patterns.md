---
id: p01_kc_system_testing_patterns
kind: knowledge_card
pillar: P01
title: "System Testing Patterns"
version: "1.0.0"
created: "2023-10-05"
updated: "2023-10-05"
author: "knowledge-card-builder"
domain: "Software Testing"
quality: null
tags: [system_testing, testing_patterns, software_testing, knowledge]
tldr: "Comprehensive guide to system testing patterns for effective QA processes."
when_to_use: "During system testing of integrated software applications."
keywords: [system testing, test cases, test suites]
long_tails:
  - How to apply system testing patterns in enterprise software
  - System testing best practices and strategies
axioms:
  - ALWAYS document each test case with precise expected results.
  - NEVER execute system tests without prior unit testing.
linked_artifacts:
  primary: null
  related: []
density_score: 0.85
data_source: "https://www.softwaretestinghelp.com/system-testing-process/"

---

# System Testing Patterns

## Quick Reference
```yaml
topic: System Testing Patterns
scope: Develop, structure, and apply system testing methods
owner: QA Specialist
criticality: high
```

## Key Concepts
- **Test Cases**: Documented scenarios with input and expected output to verify software functionality.
- **Test Suites**: Collection of related test cases executed together to cover broader system areas.
- **Test Scenarios**: High-level ideas describing what to test, serving as a basis for creating test cases.

## Strategy Phases
1. **Design Phase**: Create comprehensive test cases based on requirements.
2. **Execution Phase**: Run test cases and record outcomes rigorously.
3. **Evaluation Phase**: Analyze results to identify defects and ensure coverage.

## Golden Rules
- VERIFY: Each test case should align with a specific functional requirement.
- PRIORITIZE: Continuously prioritize critical tests based on risk assessment.
- DOCUMENT: Thoroughly document each test's setup, execution, and teardown procedures.

## Flow
```text
[Identify Requirements] -> [Design Test Cases] -> [Execute Tests] -> [Evaluate Outcomes]
```

## Comparativo
| Feature       | Manual Testing | Automated Testing |
|---------------|----------------|-------------------|
| Speed         | Slow           | Fast              |
| Scalability   | Limited        | High              |
| Accuracy      | Variable       | Consistent        |

## References
- Related artifact: Not available
- Source: https://www.softwaretestinghelp.com/system-testing-process/