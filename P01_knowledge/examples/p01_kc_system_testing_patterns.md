---
id: p01_kc_system_testing_patterns
kind: knowledge_card
pillar: P01
title: "System Testing Patterns for Distributed Systems"
version: "1.0.0"
created: "2024-12-19"
updated: "2024-12-19"
author: "knowledge-card-builder"
domain: "software_testing"
quality: null
tags: [system-testing, integration-testing, distributed-systems, qa-patterns, testing-strategy]
tldr: "Essential patterns for system testing: contract, smoke, canary, shadow, chaos testing with implementation triggers and tooling examples"
when_to_use: "When designing system test strategies, validating service integrations, or implementing testing automation pipelines"
keywords: [contract-testing, smoke-testing, canary-deployment, chaos-engineering]
long_tails:
  - "How to implement contract testing between microservices"
  - "When to use shadow testing vs canary testing in production"
  - "System testing patterns for CI/CD pipeline integration"
axioms:
  - "ALWAYS test critical paths with smoke tests after deployment"
  - "NEVER deploy without contract validation between service boundaries"
  - "IF testing in production THEN use shadow/canary patterns for safety"
linked_artifacts:
  primary: null
  related: []
density_score: 0.87
data_source: "https://martinfowler.com/articles/practical-test-pyramid.html"
---

# System Testing Patterns for Distributed Systems

## Quick Reference
```yaml
topic: system_testing_patterns
scope: Distributed systems, microservices, CI/CD integration
owner: qa_engineering
criticality: high
```

## Key Concepts

### Contract Testing
- **Purpose**: API boundary validation between services
- **Tools**: Pact, Spring Cloud Contract, Postman Contract Testing
- **Trigger**: Service API changes, dependency updates
- **Success**: 100% contract compatibility across service versions

### Smoke Testing
- **Purpose**: Critical path verification post-deployment
- **Coverage**: 5-10 essential user journeys, <5min execution
- **Trigger**: Every deployment to staging/production
- **Tools**: Cypress, Playwright, TestCafe for web; REST Assured for APIs

### Canary Testing
- **Purpose**: Progressive rollout validation with real traffic
- **Pattern**: 5% -> 25% -> 50% -> 100% traffic split
- **Metrics**: Error rate <0.1%, latency P95 <500ms, success rate >99.9%
- **Tools**: Istio, Linkerd, AWS App Mesh, Argo Rollouts

## Strategy Phases

1. **Risk Assessment**: Identify critical paths, failure impact, rollback cost
2. **Pattern Selection**: Match testing patterns to risk level and deployment frequency
3. **Tool Integration**: Embed patterns into CI/CD pipeline stages
4. **Metrics Definition**: Set success/failure thresholds for automated decisions
5. **Monitoring Setup**: Real-time dashboards for test execution and system health

## Golden Rules

- Test pyramid: 70% unit, 20% integration, 10% system/e2e
- Fail fast: Run smoke tests before expensive integration tests
- Production safety: Use canary/shadow for high-risk changes
- Contract first: Validate API contracts before integration testing
- Monitor everything: Test execution time, flakiness, coverage gaps

## Flow
```text
[Code Commit] -> [Unit Tests] -> [Contract Tests] -> [Integration Tests]
                                                           |
[Smoke Tests] <- [Deploy to Staging] <- [Security Tests] <-+
     |
[Canary Deploy] -> [Shadow Testing] -> [Full Production] -> [Chaos Tests]
```

## Pattern Selection Matrix

| Risk Level | Pattern | Execution Time | Cost | When to Use |
|------------|---------|---------------|------|-------------|
| Low | Smoke | 2-5 min | $ | Every deployment |
| Medium | Contract + Integration | 10-20 min | $$ | API changes |
| High | Canary + Shadow | 30-60 min | $$$ | Major releases |
| Critical | Full E2E + Chaos | 2-4 hours | $$$$ | Monthly validation |

## Implementation Triggers

### Contract Testing
- **Pre-deployment**: API schema changes, version bumps
- **Continuous**: Nightly compatibility checks across service matrix
- **Tools**: `pact-broker verify`, `spring-cloud-contract test`

### Shadow Testing
- **Production traffic**: Replay 1-10% traffic to new version
- **Zero user impact**: Compare responses, log differences
- **Tools**: GoReplay, Diffy, Istio traffic mirroring

### Chaos Engineering
- **Scheduled**: Weekly failure injection during low-traffic periods
- **Patterns**: Service shutdown, network partition, resource exhaustion
- **Tools**: Chaos Monkey, Litmus, Gremlin, Chaos Toolkit

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| E2E everywhere | Slow, flaky, expensive | Follow test pyramid ratios |
| Production-only testing | High blast radius | Use staging + canary patterns |
| Manual smoke tests | Deployment bottleneck | Automate critical path validation |
| No contract testing | Integration surprises | API-first development with contracts |

## References
- Source: https://martinfowler.com/articles/practical-test-pyramid.html
- Pattern catalog: https://microservices.io/patterns/testing/
- Chaos engineering: https://principlesofchaos.org/