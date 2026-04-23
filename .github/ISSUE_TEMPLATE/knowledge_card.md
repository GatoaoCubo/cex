---
name: Knowledge Card
about: Propose a new knowledge card for a domain gap
labels: "good first issue, knowledge"
related:
  - bld_examples_naming_rule
  - examples_prompt_template_builder
  - p06_schema_taxonomy
  - p01_kc_qa_validation
  - bld_collaboration_knowledge_card
  - knowledge-card-builder
  - bld_examples_few_shot_example
  - bld_knowledge_card_knowledge_card
  - p01_kc_input_hydration
  - bld_examples_response_format
---

## Topic

<!-- What domain or concept needs a knowledge card? -->

## Target pillar

<!-- P01-P12 -- which pillar does this knowledge belong to? -->

**Pillar:** 

## Why it's missing

<!-- One sentence: what confusion or gap does this KC resolve? -->

## Pre-flight checklist

- [ ] No existing KC at `N00_genesis/P01_knowledge/library/kind/kc_{topic}.md`
- [ ] Frontmatter includes: `kind: knowledge_card`, `pillar: P01`, `quality: null`
- [ ] Density >= 0.80 (tables and bullets, no prose blocks over 3 lines)
- [ ] `python _tools/cex_doctor.py` shows 0 FAIL
- [ ] PR title follows format: `[knowledge] add kc_{topic}`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_naming_rule]] | related | 0.23 |
| [[examples_prompt_template_builder]] | related | 0.23 |
| [[p06_schema_taxonomy]] | related | 0.23 |
| [[p01_kc_qa_validation]] | related | 0.23 |
| [[bld_collaboration_knowledge_card]] | related | 0.22 |
| [[knowledge-card-builder]] | related | 0.22 |
| [[bld_examples_few_shot_example]] | related | 0.22 |
| [[bld_knowledge_card_knowledge_card]] | related | 0.22 |
| [[p01_kc_input_hydration]] | related | 0.21 |
| [[bld_examples_response_format]] | related | 0.21 |
