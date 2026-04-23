---
kind: architecture
id: bld_architecture_prompt_template
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of prompt_template — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Prompt Template"
version: "1.0.0"
author: n03_builder
tags: [prompt_template, builder, examples]
tldr: "Golden and anti-examples for prompt template construction, demonstrating ideal structure and common pitfalls."
domain: "prompt template construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - prompt-template-builder
  - bld_knowledge_card_prompt_template
  - p03_sp_prompt_template_builder
  - bld_memory_prompt_template
  - p03_ins_prompt_template
  - bld_collaboration_prompt_template
  - p01_kc_prompt_template
  - p11_qg_prompt_template
  - schema_prompt_template_builder
  - tools_prompt_template_builder
---

# Architecture: prompt_template in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, variables, syntax_tier, etc.) | prompt-template-builder | active |
| variable_declarations | Typed variable slots with names, types, defaults, and descriptions | author | active |
| template_body | Parameterized text with `{{variable}}` or [VAR] placeholders | author | active |
| syntax_tier | Interpolation syntax level (tier-1 Mustache, tier-2 bracket) | author | active |
| rendering_context | Runtime context required to fill variables (data sources, APIs) | author | active |
| example_fills | Concrete variable fills demonstrating valid template usage | author | active |
## Dependency Graph
```
type_def        --produces-->  prompt_template  --consumed_by-->  renderer
knowledge_card  --produces-->  prompt_template  --produces-->     filled_prompt
prompt_template --signals-->   render_error
```
| From | To | Type | Data |
|------|----|------|------|
| type_def (P06) | prompt_template | data_flow | type definitions for variable constraints |
| knowledge_card (P01) | prompt_template | data_flow | domain facts injected as variable values |
| prompt_template | renderer (LangChain/DSPy/Mustache) | consumes | template consumed by rendering engine |
| prompt_template | filled_prompt | produces | concrete prompt after variable substitution |
| prompt_template | render_error (P12) | signals | emitted when variable fill fails validation |
| system_prompt (P03) | prompt_template | dependency | system identity may constrain template scope |
## Boundary Table
| prompt_template IS | prompt_template IS NOT |
|--------------------|------------------------|
| A reusable mold with `{{variable}}` slots for multiple invocations | A one-time task instruction (action_prompt P03) |
| Structure separated from content via parameterization | A fixed system identity definition (system_prompt P03) |
| Rendered by LangChain, DSPy, Mustache, or Jinja2 engines | A step-by-step recipe without variables (instruction P03) |
| Variable-typed with defaults and validation constraints | A raw user message without structure |
| Invoked multiple times with different variable fills | A single-use prompt discarded after execution |
| Produces filled prompts — not direct LLM responses | A meta-prompt that generates other prompts |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Types | type_def | Supply type definitions for variable constraints |
| Definition | frontmatter, variable_declarations, syntax_tier | Specify template identity and variable slots |
| Template | template_body, example_fills | The parameterized text and usage examples |
| Rendering | rendering_context, renderer | Runtime fill and template engine execution |
| Output | filled_prompt, render_error | Concrete prompt produced or error signaled |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[prompt-template-builder]] | upstream | 0.55 |
| [[bld_knowledge_card_prompt_template]] | upstream | 0.52 |
| [[p03_sp_prompt_template_builder]] | upstream | 0.51 |
| [[bld_memory_prompt_template]] | downstream | 0.49 |
| [[p03_ins_prompt_template]] | upstream | 0.47 |
| [[bld_collaboration_prompt_template]] | upstream | 0.43 |
| [[p01_kc_prompt_template]] | upstream | 0.40 |
| [[p11_qg_prompt_template]] | downstream | 0.37 |
| [[schema_prompt_template_builder]] | upstream | 0.37 |
| [[tools_prompt_template_builder]] | upstream | 0.36 |
