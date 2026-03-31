---
id: p01_kc_system_testing_patterns
kind: knowledge_card
pillar: P01
title: "System Testing Patterns in Software Engineering"
version: "1.0.0"
created: "2023-10-06"
updated: "2023-10-06"
author: "knowledge-card-builder"
domain: Software Engineering
quality: null
tags: [system-testing, patterns, software-engineering, knowledge]
tldr: "System testing patterns standardize approaches to validate integrated software against specified requirements."
when_to_use: "When testing end-to-end functionality of a software system in an integrated environment."
keywords: [system-testing, black-box, end-to-end, usability]
long_tails:
  - How to implement black-box testing in integrated systems
  - Combining usability and end-to-end testing for software validation
axioms:
  - ALWAYS ensure system requirements are met through comprehensive testing.
linked_artifacts:
  primary: null
  related: []
density_score: 0.83
data_source: "https://www.softwaretestinghelp.com/system-testing/"

---

## Quick Reference
```yaml
topic: System Testing Patterns
scope: Software testing methodologies for complete systems
owner: knowledge-card-builder
criticality: high
```

## Key Concepts
- **Black-Box Testing**: Tests based on requirements and functionality without internal code inspection.
- **End-to-End Testing**: Validates the system flow from start to finish in a real-world scenario.
- **Usability Testing**: Evaluates the user interface and user experience to ensure user-friendliness.

## Strategy Phases
1. **Identify Requirements**: Determine system specifications and performance criteria.
2. **Select Testing Pattern**: Choose suitable patterns based on requirements and scenarios.
3. **Execute Tests**: Run tests and evaluate results against expected outcomes.

## Golden Rules
- ALWAYS validate the system as a whole in a production-like environment.
- NEVER skip usability testing when user interaction is critical.
- Combine multiple testing patterns for comprehensive coverage.

## Flow
```
[Requirements] -> [Select Pattern] -> [Execute Test] -> [Evaluate Results]
```

## Comparativo
| Pattern Type | Black-Box Testing | End-to-End Testing | Usability Testing |
|--------------|-------------------|--------------------|------------------|
| Focus | Functional correctness | System flow | User experience |
| Use Cases | APIs, UI elements | Full application | Interface design |
| Approach | Input/output validation | Scenario simulation | User interaction |

## References
- Source: https://www.softwaretestinghelp.com/system-testing/
- Related artifact: null