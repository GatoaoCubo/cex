---
id: p01_kc_engineering_best_practices
kind: knowledge_card
pillar: P01
title: "Software Engineering Best Practices for Quality and Maintainability"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder"
domain: software_engineering
quality: 9.1
tags: [software-engineering, best-practices, code-quality, maintainability, testing, knowledge]
tldr: "Core engineering practices: automated testing >80% coverage, code review before merge, CI/CD pipelines, semantic versioning, documentation-as-code"
when_to_use: "When establishing development standards for new projects or improving existing codebase quality and team productivity"
keywords: [engineering-practices, code-review, testing, ci-cd, documentation]
long_tails:
  - How to implement automated testing strategy with 80% coverage minimum
  - What code review checklist ensures consistent quality standards
  - When to use semantic versioning for API stability
axioms:
  - ALWAYS require code review before merging to main branch
  - NEVER deploy without automated tests passing
  - IF bug found in production THEN add regression test immediately
linked_artifacts:
  primary: null
  related: [p01_kc_git_workflow_patterns, p01_kc_testing_strategies]
density_score: 0.87
data_source: "Industry standards from Google SRE, GitHub flow, Martin Fowler patterns"
related:
  - p07_sr_engineering_quality
  - p02_agent_test_ops
  - n05_operations
  - bld_knowledge_card_contributor_guide
  - p11_qg_tdd_compliance
  - p02_agent_code_review
  - p01_kc_code_review
  - agent_card_n05
  - p01_kc_system_testing_patterns
  - p01_kc_tdd_as_llm_skill
---
# Software Engineering Best Practices for Quality and Maintainability

## Quick Reference
```yaml
topic: software_engineering_practices
scope: Team development standards and code quality gates
owner: engineering_lead
criticality: high
```

## Key Concepts
- **Code Review**: Pre-merge validation requiring 1+ approvers, automated checks, 24h max turnaround
- **Test Pyramid**: 70% unit, 20% integration, 10% E2E with >80% total coverage
- **CI/CD Pipeline**: Automated build → test → security scan → deploy with rollback capability
- **Semantic Versioning**: MAJOR.MINOR.PATCH format for API compatibility contracts
- **Documentation-as-Code**: README, API docs, ADRs maintained in repository with code changes

## Strategy Phases
1. **Foundation**: Establish git workflow, branch protection, automated testing framework
2. **Quality Gates**: Implement code review process, coverage thresholds, linting rules
3. **Automation**: Set up CI/CD pipelines, automated deployment, monitoring alerts
4. **Optimization**: Measure DORA metrics, reduce cycle time, improve developer experience
5. **Culture**: Regular retrospectives, knowledge sharing, incident post-mortems

## Golden Rules
- Test first: write failing test before implementation code
- Small commits: each commit addresses single logical change
- Fail fast: catch errors early in development cycle, not production
- Document decisions: record architectural choices and trade-offs
- Monitor everything: logs, metrics, alerts for production systems

## Flow
```text
[Feature Request] -> [Branch] -> [TDD] -> [Code Review] -> [CI/CD] -> [Deploy] -> [Monitor]
                                   |
                              GATES: tests pass, coverage >80%, security scan clean
```

## Comparativo
| Practice | Time Investment | Quality Impact | Maintenance Cost |
|----------|----------------|----------------|------------------|
| Code Review | 2-4 hours/week | High (defect reduction 60%) | Low |
| Automated Testing | 20-30% dev time | Very High (regression prevention) | Medium |
| CI/CD Pipeline | 1-2 weeks setup | Medium (deployment reliability) | Low |
| Documentation | 10-15% dev time | Medium (onboarding speed 3x) | Low |

## References
- Google SRE Book: https://sre.google/sre-book/
- GitHub Flow: https://docs.github.com/en/get-started/quickstart/github-flow
- Martin Fowler on CI: https://martinfowler.com/articles/continuousIntegration.html
- DORA Metrics: https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_sr_engineering_quality]] | downstream | 0.24 |
| [[p02_agent_test_ops]] | downstream | 0.23 |
| [[n05_operations]] | downstream | 0.23 |
| [[bld_knowledge_card_contributor_guide]] | sibling | 0.23 |
| [[p11_qg_tdd_compliance]] | downstream | 0.21 |
| [[p02_agent_code_review]] | downstream | 0.21 |
| [[p01_kc_code_review]] | sibling | 0.20 |
| [[agent_card_n05]] | related | 0.19 |
| [[p01_kc_system_testing_patterns]] | sibling | 0.19 |
| [[p01_kc_tdd_as_llm_skill]] | sibling | 0.19 |
