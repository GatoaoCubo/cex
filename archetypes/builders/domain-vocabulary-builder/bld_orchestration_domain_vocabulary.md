---
id: bld_rules_domain_vocabulary
kind: guardrail
pillar: P11
llm_function: COLLABORATE
version: 1.0.0
quality: 7.7
tags: [domain_vocabulary, rules, guardrail]
title: "Rules: domain_vocabulary Builder"
author: builder
tldr: "Domain Vocabulary feedback: workflow coordination, handoffs, and lifecycle management"
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p03_sp_glossary_entry_builder
  - p01_kc_glossary_entry
  - p03_sp_system-prompt-builder
  - p03_sp_kind_builder
  - p03_sp_type-def-builder
  - p03_sp_context_window_config_builder
  - bld_instruction_glossary_entry
  - p03_sp_signal_builder
  - p03_sp_input_schema_builder
  - p03_sp_few_shot_example_builder
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

## Orchestration Checklist

- Verify workflow topology matches dependency graph
- Validate handoff protocol between upstream and downstream
- Cross-reference with dispatch rules for routing correctness
- Test wave sequencing with dry-run before live dispatch

## Orchestration Pattern

```yaml
# Workflow validation
topology: verified
handoffs: validated
routing: checked
sequencing: tested
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope orchestration
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_glossary_entry_builder]] | upstream | 0.31 |
| [[p01_kc_glossary_entry]] | upstream | 0.27 |
| [[p03_sp_system-prompt-builder]] | upstream | 0.27 |
| [[p03_sp_kind_builder]] | upstream | 0.26 |
| [[p03_sp_type-def-builder]] | upstream | 0.25 |
| [[p03_sp_context_window_config_builder]] | upstream | 0.23 |
| [[bld_instruction_glossary_entry]] | upstream | 0.23 |
| [[p03_sp_signal_builder]] | upstream | 0.22 |
| [[p03_sp_input_schema_builder]] | upstream | 0.22 |
| [[p03_sp_few_shot_example_builder]] | upstream | 0.22 |
