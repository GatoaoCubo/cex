---
id: bld_tpl_domain_vocabulary
kind: prompt_template
pillar: P03
llm_function: PRODUCE
version: 1.0.0
quality: 8.1
tags: [domain_vocabulary, template, output]
title: "Output Template: domain_vocabulary"
author: builder
density_score: 1.0
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p01_kc_glossary_entry
  - p06_enum_def
  - bld_instruction_glossary_entry
  - bld_collaboration_glossary_entry
  - p03_sp_glossary_entry_builder
  - p03_sp_signal_builder
  - p01_gl_TERM_SLUG
  - bld_architecture_ecommerce_vertical
  - bld_collaboration_type_def
  - bld_architecture_graph_rag_config
---
# Output Template: domain_vocabulary
```markdown
---
id: dv_{{bounded_context_snake}}_vocabulary
kind: domain_vocabulary
pillar: P01
title: "{{BoundedContext}} Domain Vocabulary"
version: 1.0.0
quality: null
bounded_context: {{bounded_context}}
governed_agents: [{{agent_id_1}}, {{agent_id_2}}]
term_count: {{N}}
tags: [{{bounded_context}}, vocabulary, ubiquitous-language]
---

# {{BoundedContext}} Domain Vocabulary

## Overview
{{One sentence: what domain this vocabulary governs and why it exists.}}

## Terms

### {{TermName}}
| Field | Value |
|-------|-------|
| definition | {{canonical one-sentence definition}} |
| industry_standard | {{Evans DDD / NIST / ISO ref / "CEX-internal"}} |
| anti_patterns | [{{wrong_name_1}}, {{wrong_name_2}}] |
| status | active |
| replaces | null |

### {{TermName2}}
| Field | Value |
|-------|-------|
| definition | {{canonical definition}} |
| industry_standard | {{reference}} |
| anti_patterns | [{{wrong_names}}] |
| status | active |
| replaces | null |

## Deprecated Terms
| Old Term | Replaced By | Deprecated Date |
|----------|------------|-----------------|
| {{old}} | {{new}} | {{YYYY-MM-DD}} |

## Loading Instructions
Load this vocabulary at F2b SPEAK before producing any artifact in
the {{bounded_context}} bounded context.
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_glossary_entry]] | upstream | 0.22 |
| [[p06_enum_def]] | downstream | 0.21 |
| [[bld_instruction_glossary_entry]] | related | 0.21 |
| [[bld_collaboration_glossary_entry]] | downstream | 0.19 |
| [[p03_sp_glossary_entry_builder]] | related | 0.18 |
| [[p03_sp_signal_builder]] | related | 0.18 |
| [[p01_gl_TERM_SLUG]] | upstream | 0.17 |
| [[bld_architecture_ecommerce_vertical]] | downstream | 0.17 |
| [[bld_collaboration_type_def]] | downstream | 0.17 |
| [[bld_architecture_graph_rag_config]] | downstream | 0.16 |
