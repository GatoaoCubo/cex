---
pillar: P01
llm_function: INJECT
purpose: Operational knowledge and patterns for dispatch_rule production
sources: [gateway routing systems, orchestrator routing tables, multi-agent collaboration protocols, real routing workflows]
---

# Domain Knowledge: dispatch_rule

## Core Concept
A dispatch_rule is a routing policy record answering: **"Which target receives tasks matching these keywords, at what priority, with what fallback?"** Rules are decisions, not instructions. Consumed by routers/dispatchers. Does NOT tell the target what to do (that's a handoff).

## The Routing Triad

```
TRIGGER: keywords[] + confidence_threshold
  -> TARGET: agent/service + model + priority
  -> FALLBACK: alternative target (if unavailable or below threshold)
```
One rule = one triad. Multiple rules compose into a routing table.

## Keyword Design

| Principle | Example | Why |
|-----------|---------|-----|
| Cover synonyms | [build, create, implement] | Same intent, different words |
| Include abbreviations | [docs, documentation] | Short forms common |
| Bilingual variants | [pesquisar, research] | Multi-language systems |
| Avoid ambiguous words | NOT [run] | Too generic, false matches |
| Use verb forms | [deploy, deploying] | Intent = actions |
| Keep focused | 5-12 per rule | Too many = noise |

Overlap resolution: (1) highest priority, (2) most matches, (3) first defined.

## Routing Strategy

| Strategy | When | Precision | Cost |
|----------|------|-----------|------|
| keyword_match | Clear taxonomy, <20 keywords | High for known terms | Zero |
| semantic | Ambiguous domain, many paraphrases | High for novel inputs | LLM call |
| hybrid | Large bilingual set, mixed needs | Highest | Keyword + LLM fallback |

Default: start with `keyword_match`. Add semantic only when keywords prove insufficient.

## Priority and Threshold

| Priority | Meaning | Examples |
|----------|---------|---------|
| 9-10 | Critical: core routing, security | orchestration, deploy |
| 7-8 | High: primary business | build, research |
| 5-6 | Normal: supporting tasks | docs, indexing |
| 1-4 | Low: optional/rare | logging, archival |

| Threshold | Behavior | Use case |
|-----------|----------|----------|
| 0.9+ | Near-exact only | Security-critical ops |
| 0.7-0.89 | Standard (default) | Most business routing |
| 0.5-0.69 | Permissive | Many synonyms/informal |

## Fallback Rules
- Must differ from primary target (no self-fallback)
- Should be broader agent, not peer specialist
- Universal gateway is safe default
- No chain fallbacks in single rule; use separate rule

## Cross-Reference
- Bidirectional: if A routes to B, B must acknowledge A
- Catches stale routes when targets renamed/removed
- Crew members specify upstream (who sends) and downstream (who receives)

## Scope
One rule = one domain. If keywords span two domains, create two rules.

## Anti-Patterns

| Anti-Pattern | Fix |
|--------------|-----|
| Circular routing (A->B->A) | Acyclic fallback chains; universal catch-all |
| Ambiguous keywords (do, run) | Domain-specific verbs |
| Missing fallback | Always define; gateway as default |
| Same priority overlap | Unique priority per keyword space |
| Stale cross-references | Audit: verify target exists |
| Monolithic 50-keyword rule | Split into focused rules per domain |
| Self-fallback | Fallback must be different target |

## Boundary

| Type | Why NOT dispatch_rule |
|------|----------------------|
| handoff | Tells target WHAT TO DO |
| signal | Reports WHAT HAPPENED |
| workflow | Coordinates HOW work flows |
| spawn_config | Configures HOW to launch |
| router (P02) | Full routing ENGINE, not single RULE |

## Constraints
- Max 3072 bytes per rule
- ID: `p12_dr_{scope}.yaml`
- `quality: null` invariant at authoring
- One rule per scope domain
- Priority 1-10 integer, no fractions
