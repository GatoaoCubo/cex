---
kind: knowledge_card
id: bld_knowledge_card_context_doc
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for context_doc production — domain background for prompt hydration
sources: consulting discovery docs, technical context memos, onboarding packets
quality: 9.1
title: "Knowledge Card Context Doc"
version: "1.0.0"
author: n03_builder
tags: [context_doc, builder, examples]
tldr: "Golden and anti-examples for context doc construction, demonstrating ideal structure and common pitfalls."
domain: "context doc construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_context_doc
  - context-doc-builder
  - p03_sp_context_doc_builder
  - bld_instruction_context_doc
  - p01_kc_context_doc
  - kc_model_context_protocol
  - bld_output_template_context_doc
  - p10_lr_context_doc_builder
  - p11_qg_context_doc
  - bld_architecture_context_doc
---

# Domain Knowledge: context_doc
## Executive Summary
Context docs are domain background documents injected into agent context before task execution. They provide situational awareness — stakeholders, constraints, assumptions, dependencies — without the density requirements of knowledge cards or the step-by-step structure of instructions. Context docs answer "what is the background?" before the agent answers "what do I do?"
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge) |
| llm_function | INJECT (loaded into context) |
| Max size | 2048 bytes |
| Density gate | None (narrative allowed) |
| Quality gates | 7 HARD + 8 SOFT |
| Output format | .md + optional .yaml pair |
| Key fields | domain, scope, stakeholders, constraints |
## Patterns
- **Scope-first writing**: define boundaries before content — what domain, what time horizon, what is excluded
- **Stakeholder focus**: tailor precision to who consumes this context and what decisions they make
- **Constraint documentation**: list what CANNOT change — constraints bound the problem space more than features
- **Time-bounded context**: include timeline and dates — context ages; stale context causes wrong decisions
- **Consumption chain**: context_docs feed into system_prompts and action_prompts as background injection
| Analog | Source | Shared pattern |
|--------|--------|----------------|
| README context | Software repos | Background before instructions |
| Project brief | Consulting | Scope, constraints, stakeholders |
| SITREP | Operations | Current state + key constraints |
| Onboarding packet | Teams | Domain background for newcomers |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No scope boundary | Document grows unbounded; includes irrelevant context |
| Duplicating knowledge cards | Context doc has no density gate; use KC for atomic facts |
| Including step-by-step instructions | That is an instruction artifact, not context |
| Missing constraints section | Agent has background but no boundaries; overreaches |
| Stale dates | Outdated context causes wrong assumptions |
| Over 2048 bytes | Exceeds token budget for injection; split or compress |
## Application
1. Define scope: one sentence — what domain, what time horizon, what is excluded
2. Identify stakeholders: who consumes this context and for what decisions
3. Document constraints: what CANNOT change in this domain
4. List assumptions: what is taken as true without verification
5. Map dependencies: what other artifacts consume this context
6. Validate: <= 2048 bytes, scope is one sentence, constraints are concrete
## References
- Consulting discovery documents: scope and constraint patterns
- Technical writing: context memos and background sections
- Agile: Definition of Done context documentation
- Prompt engineering: context injection for LLM task performance

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_context_doc]] | downstream | 0.41 |
| [[context-doc-builder]] | related | 0.40 |
| [[p03_sp_context_doc_builder]] | related | 0.39 |
| [[bld_instruction_context_doc]] | downstream | 0.35 |
| [[p01_kc_context_doc]] | sibling | 0.33 |
| [[kc_model_context_protocol]] | sibling | 0.31 |
| [[bld_output_template_context_doc]] | downstream | 0.29 |
| [[p10_lr_context_doc_builder]] | downstream | 0.26 |
| [[p11_qg_context_doc]] | downstream | 0.26 |
| [[bld_architecture_context_doc]] | downstream | 0.21 |
