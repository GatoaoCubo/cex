---
id: p01_kc_dispatch_rule
kind: knowledge_card
type: kind
pillar: P12
title: "Dispatch Rule — Deep Knowledge for dispatch_rule"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: dispatch_rule
quality: 9.1
tags: [dispatch_rule, P12, REASON, kind-kc]
tldr: "Keyword-to-agent_group routing rule that maps intent signals to execution targets without running the task itself"
when_to_use: "Building, reviewing, or reasoning about dispatch_rule artifacts"
keywords: [routing, keyword, agent_group]
feeds_kinds: [dispatch_rule]
density_score: null
related:
  - p01_kc_router
  - bld_knowledge_card_dispatch_rule
  - bld_schema_dispatch_rule
  - bld_architecture_dispatch_rule
  - bld_instruction_dispatch_rule
  - p03_sp_dispatch_rule_builder
  - p12_dr_admin_orchestration
  - p11_qg_dispatch_rule
  - dispatch-rule-builder
  - bld_knowledge_card_router
---

# Dispatch Rule

## Spec
```yaml
kind: dispatch_rule
pillar: P12
llm_function: REASON
max_bytes: 3072
naming: p12_dr_{{scope}}.yaml
core: false
```

## What It Is
A dispatch rule maps keyword or intent signals to target agent_groups/agents, determining where a task should be routed for execution. It contains trigger patterns, target agent_group, priority, and confidence threshold. It is NOT router (P02 — routes task to model/provider based on complexity; dispatch_rule routes to agent_group based on domain intent) nor workflow (P12 — workflow executes the task; dispatch_rule only decides where to send it).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `ConditionalRouter` / LCEL branching | `RunnableBranch` routes to different chains based on conditions |
| LlamaIndex | `RouterQueryEngine` / `SubQuestionQueryEngine` | Routes query to different index/engine based on semantic classification |
| CrewAI | `Process.hierarchical` manager agent routing | Manager LLM decides which worker agent handles each task |
| DSPy | Custom `Module` with `dspy.Predict` classifier | Classify intent → route to specialized sub-module |
| Haystack | `ConditionalRouter` component | Route pipeline flow based on metadata or score conditions |
| OpenAI | Tool selection via `tool_choice` | Model selects appropriate tool/function based on intent |
| Anthropic | Tool use routing via system prompt classification | System prompt encodes routing logic; model selects tool |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| keywords | list | required | Broader keywords = more matches; higher false-positive rate |
| target | string | required | agent_group/agent name; one target per rule |
| confidence_threshold | float | 0.70 | Higher = fewer routes; more unmatched queries fall through |
| priority | int | 5 | Higher priority rules evaluated first; lower = fallback |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Domain-scoped rules | Clear domain separation | keywords: [pesquisar, mercado, scrape] → target: research_agent |
| Fallback rule | Catch-all for unmatched intent | keywords: ["*"], priority: 0, target: orchestrator |
| Multi-keyword OR | Synonyms for same intent | keywords: [anuncio, copy, titulo, vender, marketing] → target: marketing_agent |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Single keyword per rule | Low recall; many valid queries unmatched | List 5+ synonyms and related terms per rule |
| Overlapping high-priority rules | Ambiguous routing; wrong agent_group selected | Use priority tiers; highest priority = most specific keywords |
| No fallback rule | Unmatched queries silently dropped | Always define priority:0 fallback to orchestrator |

## Integration Graph
```
[signal] --> [dispatch_rule] --> [spawn_config]
[handoff] ----^           |
                     [workflow]
```

## Decision Tree
- IF keyword matches high-priority rule (priority >= 8) THEN route immediately
- IF keyword matches multiple rules THEN use highest priority
- IF no rule matches THEN route to fallback (orchestrator)
- IF confidence < threshold THEN escalate to orchestrator for clarification
- DEFAULT: Always have fallback rule at priority 0

## Quality Criteria
- GOOD: Has keywords list (5+), target, priority, confidence_threshold; YAML parseable
- GREAT: Domain-exclusive keywords (no overlap); fallback defined; priority tiers documented
- FAIL: Single keyword; no fallback rule; overlapping high-priority rules; target undefined

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_router]] | sibling | 0.50 |
| [[bld_knowledge_card_dispatch_rule]] | sibling | 0.50 |
| [[bld_schema_dispatch_rule]] | upstream | 0.45 |
| [[bld_architecture_dispatch_rule]] | upstream | 0.42 |
| [[bld_instruction_dispatch_rule]] | upstream | 0.40 |
| [[p03_sp_dispatch_rule_builder]] | upstream | 0.39 |
| [[p12_dr_admin_orchestration]] | related | 0.39 |
| [[p11_qg_dispatch_rule]] | upstream | 0.38 |
| [[dispatch-rule-builder]] | related | 0.36 |
| [[bld_knowledge_card_router]] | sibling | 0.35 |
