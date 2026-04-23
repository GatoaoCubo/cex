---
kind: instruction
id: bld_instruction_citation
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for citation
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Citation"
version: "1.0.0"
author: n03_builder
tags: [citation, builder, examples]
tldr: "Golden and anti-examples for citation construction, demonstrating ideal structure and common pitfalls."
domain: "citation construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_citation
  - bld_output_template_citation
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - p03_sp_citation_builder
  - bld_instruction_chunk_strategy
  - bld_instruction_prompt_version
  - p11_qg_citation
  - bld_instruction_handoff_protocol
---

# Instructions: How to Produce a citation
## Phase 1: RESEARCH
1. Identify the source: what external or internal knowledge source needs attribution?
2. Classify source_type: web, paper, book, internal, api
3. Assess reliability: tier_1 (peer-reviewed, primary), tier_2 (official docs), tier_3 (blog, tutorial)
4. Extract key excerpt: 1-3 sentences that capture the relevant claim
5. Record URL and date_accessed for verification
6. Check existing citations to avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all frontmatter fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill frontmatter: all required fields including source_type, reliability_tier, url, excerpt
4. Set quality: null — never self-score
5. Write body sections: Source, Excerpt, Relevance, Verification, Related
6. Map relevance_scope: which domains/kinds does this citation support?
7. Keep body under 2048 bytes
## Phase 3: VALIDATE
1. Verify all required frontmatter fields present
2. Check id matches pattern `p01_cit_[a-z][a-z0-9_]+`
3. Confirm source_type is valid enum value
4. Confirm reliability_tier is valid enum value
5. Verify excerpt is 1-3 sentences (not empty, not entire source)
6. Verify url format is valid
7. Verify date_accessed is present
8. Check total file under 2048 bytes
9. If any gate fails: fix immediately and re-validate

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify citation
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | citation construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_citation]] | upstream | 0.41 |
| [[bld_output_template_citation]] | downstream | 0.41 |
| [[bld_instruction_output_validator]] | sibling | 0.40 |
| [[bld_instruction_retriever_config]] | sibling | 0.39 |
| [[bld_instruction_memory_scope]] | sibling | 0.39 |
| [[p03_sp_citation_builder]] | related | 0.38 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.37 |
| [[bld_instruction_prompt_version]] | sibling | 0.37 |
| [[p11_qg_citation]] | downstream | 0.37 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.37 |
