---
kind: knowledge_card
id: bld_knowledge_card_dispatch_rule
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for dispatch_rule production — routing policy specification
sources: gateway routing systems, multi-agent collaboration protocols, API gateway patterns
---

# Domain Knowledge: dispatch_rule
## Executive Summary
Dispatch rules are routing policy records that map keywords to targets with priority and fallback. They answer "which target receives tasks matching these keywords?" Rules are decisions consumed by routers — they do NOT tell the target what to do (that is a handoff). Multiple rules compose into a routing table.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P12 (orchestration) |
| llm_function | REASON |
| Max size | 3072 bytes |
| Naming | p12_dr_{scope}.yaml |
| Quality | null (always, at authoring time) |
| Core structure | TRIGGER (keywords) → TARGET (agent+model) → FALLBACK |
| Keywords per rule | 5-12 focused terms |
| Priority range | 1-10 integer |
## Patterns
- **Routing triad**: every rule defines trigger (keywords + threshold) → target (agent + model + priority) → fallback (alternative target)
- **Keyword design**: cover synonyms, include abbreviations, bilingual variants, use verb forms, avoid ambiguous generic words
| Principle | Example | Why |
|-----------|---------|-----|
| Synonyms | [build, create, implement] | Same intent, different words |
| Abbreviations | [docs, documentation] | Short forms common in queries |
| Bilingual | [pesquisar, research] | Multi-language systems |
| Verb forms | [deploy, deploying] | Intent expressed as actions |
- **Priority and threshold calibration**:
| Priority | Meaning | Threshold | Behavior |
|----------|---------|-----------|----------|
| 9-10 | Critical | 0.9+ | Near-exact match only |
| 7-8 | High | 0.7-0.89 | Standard routing |
| 5-6 | Normal | 0.5-0.69 | Permissive matching |
- **Fallback rules**: must differ from primary; use broader agent, not peer specialist; gateway is safe default
- **Scope discipline**: one rule = one domain; spanning two domains requires two rules
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Circular routing (A→B→A) | Infinite loop; use acyclic fallback chains |
| Ambiguous keywords ("do", "run") | False matches on unrelated tasks |
| Missing fallback | No recovery when primary target unavailable |
| Self-fallback | Same target retried; no degradation |
| 50+ keywords in one rule | Too broad; split into focused domain rules |
| Stale cross-references | Target renamed/removed; route goes nowhere |
## Application
1. Define scope: one domain per rule
2. Select 5-12 keywords: synonyms, abbreviations, bilingual, verb forms
3. Set target: agent/service, model, priority (1-10)
4. Define fallback: different, broader target; gateway as default
5. Set threshold: 0.9+ (critical), 0.7-0.89 (standard), 0.5-0.69 (permissive)
6. Validate: <= 3072 bytes, no circular routes, no self-fallback
## References
- API gateway routing: nginx, Kong, AWS API Gateway patterns
- Multi-agent routing: keyword-based and semantic dispatch
- Circuit breaker: fallback chain design for routing resilience
- Overlap resolution: highest priority → most matches → first defined
