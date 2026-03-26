```yaml
---
pillar: P01
llm_function: INJECT
purpose: Standards and patterns for lifecycle_rule production
sources: [Content lifecycle management, ITIL Service Lifecycle, Data governance, CEX Laws]
---
```

# Domain Knowledge: lifecycle_rule

## Foundational Concepts
Lifecycle rules originate from content management systems (CMS) and data governance.
Core idea: every piece of content has a finite useful life. Without explicit lifecycle
policies, repositories accumulate stale artifacts that mislead consumers. In AI agent
systems, stale knowledge cards or outdated model cards cause hallucination-amplifying
decisions. lifecycle_rules make artifact freshness a first-class concern.

## Industry Patterns
| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| ITIL Service Lifecycle | 5 stages: strategy, design, transition, operation, improvement | States + transitions model |
| Contentful Content Lifecycle | Draft, changed, published, archived statuses | State machine with entry criteria |
| Data Governance (DAMA-DMBOK) | Data quality dimensions + retention policies | freshness_days + review_cycle |
| Confluence Page Archival | Auto-archive after N days inactive | Automated stale -> archived transition |
| AWS S3 Lifecycle Rules | Transition objects between storage tiers by age | Time-based automated transitions |

## Key Principles
- Every artifact has a FINITE useful life (no artifact is "forever fresh")
- Freshness is DOMAIN-SPECIFIC (LLM pricing = 30 days; architectural law = 365 days)
- State transitions must be MEASURABLE (days since update, score threshold, usage count)
- Automation reduces human burden but MANUAL review catches context no cron can
- Ownership is MANDATORY (unowned artifacts always rot)
- Notification prevents silent staleness (stale artifact with no alert = hidden debt)

## CEX-Specific Extensions
| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| freshness_days | Concrete integer for automated staleness detection | S3 lifecycle transition days |
| review_cycle | Periodic human re-evaluation schedule | ITIL continual improvement |
| ownership | Satellite or agent responsible for review | DAMA data steward |
| automation | Level of automated transitions (full/semi/manual) | Confluence auto-archive setting |

## Boundary vs Nearby Types
| Type | What it does | NOT this |
|------|-------------|----------|
| hook (P04) | EXECUTES code on events (pre/post triggers) | Does NOT declare lifecycle policy |
| runtime_rule (P09) | Manages SYSTEM behavior (timeouts, retries, circuit breakers) | Does NOT manage artifact freshness |
| quality_gate (P11) | Checks QUALITY at one point in time (pass/fail with score) | Does NOT track state over time |
| guardrail (P11) | Prevents DAMAGE (safety boundaries) | Does NOT manage freshness |

## References
- ITIL Service Lifecycle: https://www.axelos.com/certifications/itil-service-management
- DAMA-DMBOK Data Governance: https://www.dama.org/cpages/body-of-knowledge
- AWS S3 Lifecycle: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html
- Contentful Content Lifecycle: https://www.contentful.com/help/content-lifecycle/
