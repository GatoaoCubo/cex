---
id: bld_rules_domain_vocabulary
kind: guardrail
pillar: P11
llm_function: GOVERN
version: 1.0.0
quality: null
tags: [domain_vocabulary, rules, guardrail]
title: "Rules: domain_vocabulary Builder"
---
# Builder Rules: domain_vocabulary
## ALWAYS
- ALWAYS scope to a single bounded_context (not global)
- ALWAYS include anti_patterns per term (drift prevention)
- ALWAYS list governed_agents (who must load this)
- ALWAYS track lifecycle: proposed -> active -> deprecated
- ALWAYS include loading instructions (F2b SPEAK protocol)
- ALWAYS set quality: null

## NEVER
- NEVER create a global vocabulary spanning all bounded contexts
- NEVER include formal ontological relations (IS-A, PART-OF) -- use ontology kind
- NEVER duplicate glossary_entry content -- reference it instead
- NEVER delete deprecated terms -- mark deprecated + replaced_by
- NEVER list terms without at least a definition and status

## EDGE CASES
| Case | Rule |
|------|------|
| Same word in two BCs | Two separate entries in two separate vocabularies |
| Term needs formal definition | Link to glossary_entry; keep summary in vocabulary |
| Vocabulary for a sub-context | Extend parent vocabulary, don't duplicate |
| Term from external framework (Evans, NIST) | Credit in industry_standard field |

## Naming Conventions
| Pattern | Example |
|---------|---------|
| dv_{bounded_context}_vocabulary | dv_sales_vocabulary |
| Terms in PascalCase in headings | ### Order, ### Customer |
| status values | proposed, active, deprecated |

## Size Budget
max_bytes: 5120 (core: true kind -- gets 5KB like knowledge_card)
Table format per term preferred over free prose.
