---
id: p01_kc_lifecycle_rule
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P11
title: "Lifecycle Rule — Deep Knowledge for lifecycle_rule"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: lifecycle_rule
quality: 9.1
tags: [lifecycle_rule, P11, GOVERN, kind-kc]
tldr: "Declarative rule governing artifact freshness, archival, and promotion thresholds across the knowledge lifecycle"
when_to_use: "Building, reviewing, or reasoning about lifecycle_rule artifacts"
keywords: [freshness, archive, promote]
feeds_kinds: [lifecycle_rule]
density_score: null
related:
  - bld_manifest_lifecycle_rule
  - bld_collaboration_lifecycle_rule
  - bld_memory_lifecycle_rule
  - p03_sp_lifecycle_rule_builder
  - p11_lc_{{RULE_SLUG}}
  - bld_knowledge_card_lifecycle_rule
  - bld_architecture_lifecycle_rule
  - bld_examples_lifecycle_rule
  - p03_ins_lifecycle_rule
  - p01_kc_quality_gate
---

# Lifecycle Rule

## Spec
```yaml
kind: lifecycle_rule
pillar: P11
llm_function: GOVERN
max_bytes: 4096
naming: p11_lc_{{rule}}.yaml
core: true
```

## What It Is
A lifecycle rule is a declarative, evaluable policy that governs when artifacts transition between states: draft → active → stale → archived, or when they are promoted to golden/pool status. Rules specify freshness TTL, promotion score thresholds, archival triggers, and deprecation signals. It is NOT hook (P04 — executable code that runs on events) nor runtime_rule (P09 — technical operational constraint); lifecycle rules are declarative governance policies, not imperative code.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Custom metadata-based TTL policy | No native; implement via document metadata + scheduled cleanup |
| LlamaIndex | `DocumentStore` TTL + refresh pipeline | Nodes have metadata; custom freshness check on retrieval |
| CrewAI | N/A — manual task lifecycle | No native lifecycle management; implement via crew orchestration |
| DSPy | Optimizer compilation cache invalidation | Compiled programs have implicit freshness; no declarative TTL |
| Haystack | Pipeline versioning + document refresh | Component serialization enables versioned lifecycle |
| OpenAI | File API lifecycle (expires_after) | Files have TTL; assistants file attachments expire automatically |
| Anthropic | N/A — custom governance layer | No native; implement lifecycle rules as system-level cron |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| ttl_days | int | 90 | Shorter = fresher data; more maintenance overhead |
| promote_threshold | float | 8.0 | Higher = fewer promoted artifacts; better pool quality |
| archive_trigger | enum | staleness | staleness/superseded/score_drop — defines what triggers archival |
| deprecation_notice_days | int | 7 | Lead time before archival; allows consumers to adapt |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Score-decay promotion | Artifacts that age out of relevance | Promote at 8.0+; auto-archive if score drops below 6.0 after 30 days |
| Supersession chain | New artifact replaces old | Write `supersedes: [old_id]` on new artifact; archive old on publish |
| Freshness-gated retrieval | RAG pipelines with time-sensitive data | Skip retrieval of artifacts with `updated` > ttl_days ago |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No TTL on knowledge cards | Stale facts injected into LLM context indefinitely | Set ttl_days; default 90 for domain KCs, 365 for axioms |
| Promoting everything at 7.0 | Pool fills with marginal artifacts; golden quality diluted | Pool threshold 8.0; golden threshold 9.5 |
| Silent archival with no notice | Consumers reference archived artifact; silent failures | deprecation_notice_days >= 7; write deprecation marker in artifact |

## Integration Graph
```
[quality_gate] --> [lifecycle_rule] --> [pool]
[reward_signal] ----^          |
                          [archive]
```

## Decision Tree
- IF artifact score >= 9.5 THEN promote to golden pool
- IF artifact score 8.0–9.4 THEN promote to pool; set lifecycle_rule with ttl_days=365
- IF artifact not updated in ttl_days THEN trigger staleness; start deprecation countdown
- IF superseded by newer artifact THEN archive immediately after deprecation_notice_days
- DEFAULT: All artifacts have lifecycle_rule; none are eternal without explicit axiom designation

## Quality Criteria
- GOOD: Has ttl_days, promote_threshold, archive_trigger, deprecation_notice_days; parseable YAML
- GREAT: Explicit supersession chain; freshness-gated retrieval flag; score-decay thresholds calibrated
- FAIL: No TTL; promotes at any score; silent archival without notice; no archive_trigger defined

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_manifest_lifecycle_rule]] | related | 0.37 |
| [[bld_collaboration_lifecycle_rule]] | related | 0.34 |
| [[bld_memory_lifecycle_rule]] | upstream | 0.33 |
| [[p03_sp_lifecycle_rule_builder]] | upstream | 0.30 |
| [[p11_lc_{{RULE_SLUG}}]] | related | 0.30 |
| [[bld_knowledge_card_lifecycle_rule]] | sibling | 0.29 |
| [[bld_architecture_lifecycle_rule]] | upstream | 0.27 |
| [[bld_examples_lifecycle_rule]] | related | 0.25 |
| [[p03_ins_lifecycle_rule]] | upstream | 0.24 |
| [[p01_kc_quality_gate]] | sibling | 0.23 |
