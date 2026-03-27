---
pillar: P01
llm_function: INJECT
purpose: Operational knowledge and patterns for dispatch_rule production
sources: [gateway routing systems, orchestrator routing tables, multi-agent collaboration protocols, real routing workflows]
---

# Domain Knowledge: dispatch_rule

## Core Concept

A `dispatch_rule` is a routing policy record. It answers one narrow question:
**"Which target should receive tasks matching these keywords, at what priority, with what fallback?"**

Rules are decisions, not instructions. They are consumed by orchestrators, routers, and dispatch engines. They do NOT tell the target what to do — that is the job of a handoff or instruction document.

## The Routing Triad: Trigger → Target → Fallback

Every dispatch rule follows the same three-part structure:

```
TRIGGER: keywords[] + confidence_threshold
    |
    v
TARGET: satellite/agent + model + priority
    |
    v (if target unavailable or confidence below threshold)
FALLBACK: alternative satellite/agent
```

This triad is the atomic unit of routing. One rule = one triad. Multiple rules compose into a routing table.

## Keyword-Based Routing

### How Keyword Matching Works

The simplest and most reliable routing strategy: match input text against a keyword list.

```yaml
keywords: [build, code, component, create, implement]
confidence_threshold: 0.75
```

**Matching semantics**:
- All keywords are OR-matched (any single match can trigger the rule)
- Confidence score = f(keyword overlap, position, context)
- Score >= threshold → rule fires
- Score < threshold → fallback activates

### Keyword Design Principles

| Principle | Example | Why |
|-----------|---------|-----|
| Cover synonyms | [build, create, implement, construct] | Users express the same intent differently |
| Include abbreviations | [docs, documentation, doc] | Short forms are common in commands |
| Cover bilingual variants | [pesquisar, research, search] | Multi-language systems need both |
| Avoid ambiguous words | NOT [run] (too generic) | Ambiguous keywords cause false matches |
| Use verb forms | [deploy, deploying, deployed] | Intent detection works on actions |
| Keep list focused | 5-12 keywords per rule | Too many = noisy matches; too few = missed intent |

### Keyword Overlap Resolution

When multiple rules share keywords, priority resolves the conflict:

```yaml
# Rule A: priority 8
keywords: [deploy, infrastructure, server]

# Rule B: priority 6
keywords: [deploy, code, release]
```

Input "deploy the code" matches both rules. Rule A wins (priority 8 > 6).

**Resolution order**: (1) highest priority, (2) most keyword matches, (3) first defined.

## Routing Strategy Selection

| Strategy | When to use | Precision | Cost |
|----------|-------------|-----------|------|
| `keyword_match` | Clear keyword taxonomy, small keyword set (<20) | High for known terms | Zero (string matching) |
| `semantic` | Ambiguous domain, many paraphrases, no clear keywords | High for novel inputs | LLM call per match |
| `hybrid` | Large bilingual keyword set, mixed precision needs | Highest overall | Keyword pass + LLM fallback |

**Default**: Start with `keyword_match`. Move to `hybrid` only when keyword coverage proves insufficient.

## Priority Semantics

Priority is a 1-10 integer that resolves conflicts when multiple rules match the same input.

| Priority | Meaning | Example domains |
|----------|---------|-----------------|
| 9-10 | Critical: core system routing, security | orchestration, deploy, authentication |
| 7-8 | High: primary business domains | build, research, marketing |
| 5-6 | Normal: supporting tasks | documentation, formatting, indexing |
| 1-4 | Low: optional or rare tasks | logging, archival, cleanup |

**Rule**: Two rules in the same domain should NOT share the same priority. If they do, routing behavior is undefined.

## Confidence Threshold Guidance

The threshold gates whether a keyword match actually fires the rule.

| Threshold | Behavior | Use case |
|-----------|----------|----------|
| 0.9+ | Near-exact match only; very conservative | Security-critical routing, destructive operations |
| 0.7-0.89 | Standard precision; recommended default | Most business domain routing |
| 0.5-0.69 | Permissive; catches broad intent | Domains with many synonyms or informal language |
| < 0.5 | Noisy; high false-positive rate | Avoid unless semantic routing handles disambiguation |

## Fallback Logic

Fallback activates when the primary target is unavailable OR confidence is below threshold.

### Common Fallback Pairs

| Primary | Fallback | Rationale |
|---------|----------|-----------|
| Research agent | Knowledge agent | Both handle information retrieval |
| Build agent | Execution agent | Execution can handle simpler builds |
| Marketing agent | Monetization agent | Overlapping commercial domain |
| Any specialist | Gateway/orchestrator | Universal catch-all for re-routing |

### Fallback Rules
1. `fallback` MUST differ from `satellite` (no self-fallback)
2. Fallback should be a **broader** agent, not a peer specialist
3. A universal execution agent is a safe default fallback
4. Chain fallbacks are NOT supported in a single rule — use a separate fallback rule instead

## Cross-Reference Pattern

### Bidirectional Acknowledgment

When routing rules reference targets, the targets should reference back. This prevents orphan routes and ensures consistency.

```
dispatch_rule for "build" → routes to Edison satellite
Edison satellite's capability list → includes "build" domain
```

**The cross-reference norm**: If A's routing table mentions B, B's documentation must mention A as a source. Both files acknowledge the relationship. This catches stale routes — if B is renamed or removed, A's reference becomes detectably broken.

### Crew Collaboration Protocol

In multi-agent systems, dispatch rules often chain into crew compositions. Each crew member has a defined role:

```
Crew: "Research Pipeline"
  1. Researcher → "gather raw data"         [dispatch_rule: research keywords]
  2. Analyst   → "synthesize findings"       [dispatch_rule: analysis keywords]
  3. Reporter  → "format final output"       [dispatch_rule: report keywords]
```

**Handoff protocol per crew member**:

| Stage | Content |
|-------|---------|
| Receives | Input data + context from upstream member |
| Produces | Output artifact + quality signal for downstream |
| Signals | Completion status: complete, partial, blocked |

**Rule**: Every crew member's dispatch rule must specify upstream (who sends to me) and downstream (who I send to). Orphan members — those with no upstream or no downstream — indicate a broken pipeline.

## Scope Boundaries

One dispatch rule covers one scope domain. Do NOT combine unrelated scopes:

```yaml
# GOOD: focused scope
scope: build
keywords: [build, code, component, create]

# BAD: mixed scope
scope: build_and_research  # Two unrelated domains in one rule
keywords: [build, code, research, analyze]
```

**Rule**: If keywords span two distinct domains, create two separate rules. Shared keywords (like "analyze") can appear in both rules — priority resolves which fires.

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT dispatch_rule |
|------|------------|---------------------------|
| handoff | Full instruction packet: context, tasks, scope fence, commit | Tells target WHAT TO DO, not WHO receives |
| signal | Runtime event: status + quality_score + timestamp | Reports WHAT HAPPENED, not WHERE to route |
| workflow | Step graph with dependencies and sequencing | Coordinates HOW work flows, not WHO receives |
| spawn_config | Launch parameters: mode, slots, timeout | Configures HOW to launch, not routing policy |
| router (P02) | Complex multi-step intent classification system | Full routing ENGINE, not a single routing RULE |

**Decision rule**:
- "Route these keywords to target X" → `dispatch_rule`
- "Tell target X what to do" → `handoff`
- "Target X just finished" → `signal`
- "Run N targets in parallel" → `spawn_config`
- "Build a complete routing system" → `router`

## Anti-Patterns

| Anti-pattern | Why it fails | Fix |
|-------------|-------------|-----|
| Circular routing | A falls back to B, B falls back to A — infinite loop | Ensure fallback chains are acyclic; use a universal catch-all |
| Ambiguous keywords | Generic words like "do", "run", "make" match everything | Use domain-specific verbs: "deploy", "research", "compose" |
| Missing fallback | No fallback defined — request dropped if primary unavailable | Always define a fallback; universal gateway is safe default |
| Overlapping priority | Two rules with same keywords AND same priority — undefined behavior | Unique priority per rule in same keyword space |
| Stale cross-references | Rule routes to target that no longer exists | Audit: for each rule, verify target exists and acknowledges the route |
| Monolithic rule | One rule with 50 keywords covering 5 domains | Split into 5 focused rules, one per domain |
| Self-fallback | `satellite: X, fallback: X` — fallback to self is no fallback | Fallback must be a DIFFERENT target |

## Operational Constraints

- Max bytes: 3072 per rule
- ID must match filename scope segment: `p12_dr_{scope}.yaml`
- `quality: null` is invariant at authoring time — never self-score
- Keywords should cover common abbreviations and multilingual variants
- One rule per scope domain; do not combine unrelated scopes
- Priority 1-10 integer; no fractional priorities

## Key Principles Summary

1. **One rule, one scope**: Never mix unrelated domains in a single rule
2. **Trigger → Target → Fallback**: Every rule follows this triad
3. **Keywords are OR-matched**: Any single keyword can trigger the rule
4. **Priority resolves conflicts**: Higher priority wins when rules overlap
5. **Fallback is mandatory**: Always define what happens when primary is unavailable
6. **Cross-reference bidirectionally**: If A routes to B, B must acknowledge A
7. **Start with keyword_match**: Only add semantic routing when keywords prove insufficient
