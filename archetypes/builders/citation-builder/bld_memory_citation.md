---
id: p10_lr_citation_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n04_knowledge
observation: "Citations without excerpts are the most common failure — a URL alone provides no context if the link rots. Reliability tier misclassification (blog as tier_1) undermines trust. Missing date_accessed makes temporal validity impossible to assess."
pattern: "Always include 1-3 sentence excerpt with concrete data (numbers, dates, named entities). Classify tier_1=peer-reviewed/primary only, tier_2=official docs, tier_3=blogs/tutorials. Record date_accessed on every citation. Set quality: null always."
evidence: "Initial pattern from KC analysis — no production log yet."
confidence: 0.70
outcome: PENDING
domain: citation
tags: [citation, provenance, reliability, excerpt, temporal]
tldr: "Excerpt is mandatory (URL rots). Tier classification must be strict. date_accessed always present. quality:null always."
impact_score: 7.0
decay_rate: 0.05
agent_group: n04_knowledge
keywords: [citation, excerpt, reliability_tier, date_accessed, provenance, url]
memory_scope: project
observation_types: [user, feedback, project, reference]
llm_function: INJECT
quality: 8.8
title: Memory ISO - citation
density_score: 0.97
related:
  - p01_kc_citation
  - bld_knowledge_card_citation
  - p03_sp_citation_builder
  - bld_instruction_citation
  - p11_qg_citation
  - citation-builder
  - bld_output_template_citation
  - bld_architecture_citation
  - bld_schema_citation
  - bld_collaboration_citation
---
## Summary
Citations ground LLM outputs in verifiable external evidence. The primary failure mode is URL-only citations without context, excerpt, or reliability assessment.
## Pattern
1. **Always excerpt** — 1-3 sentences with specific data from the source
2. **Strict tier classification** — tier_1 only for peer-reviewed/primary research
3. **Temporal tracking** — date_accessed on every citation, freshness policy when time-sensitive
4. **Relevance mapping** — specify which domains/kinds the citation supports
## Anti-Pattern
- URL-only citation: no context if URL breaks
- Blog as tier_1: overestimates reliability
- No date_accessed: cannot assess temporal validity
- No excerpt: reader must visit source to understand relevance

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_citation]] | upstream | 0.55 |
| [[bld_knowledge_card_citation]] | upstream | 0.54 |
| [[p03_sp_citation_builder]] | upstream | 0.54 |
| [[bld_instruction_citation]] | upstream | 0.44 |
| [[p11_qg_citation]] | downstream | 0.44 |
| [[citation-builder]] | upstream | 0.39 |
| [[bld_output_template_citation]] | upstream | 0.38 |
| [[bld_architecture_citation]] | upstream | 0.38 |
| [[bld_schema_citation]] | upstream | 0.33 |
| [[bld_collaboration_citation]] | downstream | 0.32 |
