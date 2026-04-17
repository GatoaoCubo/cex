---
id: bld_tpl_domain_vocabulary
kind: prompt_template
pillar: P03
llm_function: PRODUCE
version: 1.0.0
quality: 6.5
tags: [domain_vocabulary, template, output]
title: "Output Template: domain_vocabulary"
density_score: 1.0
updated: "2026-04-17"
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
