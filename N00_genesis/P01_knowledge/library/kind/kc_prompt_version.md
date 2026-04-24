---
id: p01_kc_prompt_version
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P03
title: "Prompt Version — Deep Knowledge for prompt_version"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: prompt_version
quality: 9.1
tags: [prompt_version, P03, GOVERN, kind-kc]
tldr: "Immutable snapshot of a prompt at a point in time, enabling A/B testing, rollback, and audit trails"
when_to_use: "Building, reviewing, or reasoning about prompt_version artifacts"
keywords: [versioning, snapshot, prompt-audit]
feeds_kinds: [prompt_version]
density_score: 0.99
linked_artifacts:
  primary: null
  related: []
related:
  - prompt-version-builder
  - bld_collaboration_prompt_version
  - bld_knowledge_card_prompt_version
  - bld_examples_prompt_version
  - p03_sp_prompt_version_builder
  - p10_lr_prompt_version_builder
  - action-prompt-builder
  - bld_architecture_prompt_version
  - p01_kc_prompt_engineering
  - bld_collaboration_action_prompt
---

# Prompt Version

## Spec
```yaml
kind: prompt_version
pillar: P03
llm_function: GOVERN
max_bytes: 2048
naming: p03_pv.md
core: false
```

## What It Is
A prompt version is an immutable snapshot of a prompt (template, system, or action) frozen at a specific point in time. It enables A/B testing between versions, rollback to known-good prompts, and audit trails for compliance. It is NOT a prompt_template (which is mutable and has variables). A prompt version is a sealed record — once created, it never changes.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | LangSmith prompt versioning / Hub versioning | Track prompt iterations with run metadata |
| LlamaIndex | Manual prompt versioning (no native support) | Version prompts via git or custom metadata |
| CrewAI | No native versioning | Track via task description snapshots |
| DSPy | Optimizer traces / saved program state | `module.save()` serializes optimized prompt state |
| Haystack | Pipeline serialization (`to_dict` / `from_dict`) | Serialize entire pipeline config including prompts |
| OpenAI | Evals dataset versioning | Snapshot prompt + expected outputs for eval runs |
| Anthropic | Prompt caching with `cache_control` | Ephemeral cache creates a de facto versioned snapshot |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| version_id | string | required | Semantic (v1.2.0) = readable vs hash = tamper-proof |
| parent_id | string | null | Links version chain but adds maintenance overhead |
| frozen_at | datetime | required | Timestamp enables temporal queries and audit |
| metrics | map | {} | Storing perf metrics per version enables data-driven rollback |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Semantic versioning | Structured prompt evolution | v1.0.0 → v1.1.0 (minor tweak) → v2.0.0 (rewrite) |
| A/B split | Testing prompt effectiveness | Route 50% traffic to v1, 50% to v2, measure quality |
| Rollback chain | Production incident recovery | Detect quality drop → revert to last known-good version |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Mutating a "versioned" prompt | Breaks immutability contract, corrupts audit trail | Create new version instead of editing existing one |
| Versioning without metrics | No data to decide which version is better | Always attach quality score and usage count to each version |

## Integration Graph
```
[prompt_template] --> [prompt_version] --> [eval_suite]
                           |
                      [action_prompt]
```

## Decision Tree
- IF prompt is in production and will be iterated THEN create prompt_version
- IF prompt is experimental/one-off THEN version is unnecessary overhead
- IF compliance requires audit trail THEN prompt_version is mandatory
- DEFAULT: Version prompts that serve >100 requests or are A/B tested

## Quality Criteria
- GOOD: Has version_id, frozen_at timestamp, and full prompt content
- GREAT: Includes parent_id chain, performance metrics, and rollback instructions
- FAIL: Mutable content; no timestamp; no link to parent version; >2048 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[prompt-version-builder]] | related | 0.57 |
| [[bld_collaboration_prompt_version]] | downstream | 0.48 |
| [[bld_knowledge_card_prompt_version]] | sibling | 0.44 |
| [[bld_examples_prompt_version]] | downstream | 0.40 |
| [[p03_sp_prompt_version_builder]] | related | 0.40 |
| [[p10_lr_prompt_version_builder]] | downstream | 0.34 |
| [[action-prompt-builder]] | related | 0.34 |
| [[bld_architecture_prompt_version]] | downstream | 0.34 |
| [[p01_kc_prompt_engineering]] | sibling | 0.33 |
| [[bld_collaboration_action_prompt]] | downstream | 0.29 |
