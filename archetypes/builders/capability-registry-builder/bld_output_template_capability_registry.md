---
kind: output_template
id: bld_output_template_capability_registry
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for capability_registry production
quality: 9.1
title: "Output Template Capability Registry"
version: "1.0.0"
author: n04_wave8
tags: [capability_registry, builder, output_template, agent-discovery]
tldr: "Template with vars for capability_registry production"
domain: "capability_registry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
---
id: p08_cr_{{registry_name}}.md
kind: capability_registry
pillar: P08
title: "{{title}}"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{scope_description}}"
quality: null
tags: [capability_registry, {{primary_domain}}, agent-discovery]
tldr: "{{one_line_summary}}"
registry_scope: {{scope}}   # builder_sub_agents | nucleus_domain_agents | nucleus_cards | full
entry_count: {{N}}
index_date: "{{date}}"
query_interface: "python _tools/cex_query.py --registry p08_cr_{{registry_name}}.md --query 'who can X'"
---

## Registry Overview
| Field           | Value |
|-----------------|-------|
| Scope           | {{scope}} |
| Total Entries   | {{N}} |
| Index Date      | {{date}} |
| Coverage Domains| {{domain_list}} |
| Query Interface | `cex_query.py --registry {{registry_name}}` |

## Builder Sub-Agent Index
<!-- One row per .claude/agents/*-builder.md -->
| capability_name | provider_agent | input_schema | output_schema | cost_tokens | quality_baseline | availability | keyword_index |
|----------------|----------------|--------------|---------------|-------------|-----------------|--------------|---------------|
| {{cap_name}}   | .claude/agents/{{agent_id}}-builder.md | {{input}} | {{output}} | {{cost}} | {{quality}} | active | {{keywords}} |

## Nucleus Domain Agent Index
<!-- One row per N0x_*/agents/agent_*.md -->
| capability_name | provider_agent | domain | cost_tokens | quality_baseline | availability | ranked_for |
|----------------|----------------|--------|-------------|-----------------|--------------|-----------|
| {{cap_name}}   | {{nucleus_path}} | {{domain}} | {{cost}} | {{quality}} | active | {{query_categories}} |

## Nucleus Card Index
<!-- One row per N0x_*/agent_card_n0x.md -->
| nucleus | provider_agent | primary_domain | capabilities_count | quality_baseline | availability |
|---------|----------------|---------------|--------------------|-----------------|--------------|
| {{N0x}} | {{card_path}}  | {{domain}}    | {{count}}          | {{quality}}     | active |

## Query Examples
| Query | Top Candidate | Quality | Why |
|-------|--------------|---------|-----|
| "who can build a landing page?" | landing-page-builder | {{score}} | domain=landing_page, pillar=P05 |
| "who can configure RAG?" | retriever-config-builder | {{score}} | domain=RAG, pillar=P01 |
| "who handles orchestration?" | N07 agent card | {{score}} | domain=orchestration, pillar=P12 |

## Coverage Gaps
| Domain | Gap Description | Recommended Action |
|--------|----------------|-------------------|
| {{gap_domain}} | No agent registered for {{capability}} | Create {{suggested_kind}}-builder |
```
