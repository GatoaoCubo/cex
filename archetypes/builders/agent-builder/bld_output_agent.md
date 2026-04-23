---
kind: output_template
id: bld_output_template_agent
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for agent artifact production
pattern: derives from SCHEMA.md — no extra fields
quality: 9.0
title: "Output Template Agent"
version: "1.0.0"
author: n03_builder
tags: [agent, builder, examples]
tldr: "Golden and anti-examples for agent construction, demonstrating ideal structure and common pitfalls."
domain: "agent construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_agent
  - bld_schema_agent
  - p11_qg_agent
  - bld_examples_agent
  - bld_instruction_agent
  - bld_knowledge_card_agent
  - agent-builder
  - bld_collaboration_agent_card
  - p01_kc_agent
  - p11_qg_agent-card
---

# Output Template: agent
```yaml
id: p02_agent_{{agent_slug}}
kind: agent
pillar: P02
title: "{{human_readable_title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
agent_group: "{{agent_group_name_or_agnostic}}"
domain: "{{primary_domain}}"
llm_function: BECOME
capabilities_count: {{integer_matching_body}}
tools_count: {{integer_matching_body}}
iso_files_count: {{integer_10_or_more}}
routing_keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}, {{keyword_4}}]
quality: null
tags: [agent, {{domain}}, {{agent_group}}, {{pillar_tag}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
linked_artifacts:
  primary: "{{parent_agent_card}}"
  related: [{{related_artifact_refs}}]
```
## Overview
`{{agent_name}}` is a {{agent_group}} specialist in `{{domain}}`.
`{{two_sentences_primary_function_and_value}}`
## Capabilities
- `{{capability_1}}`
- `{{capability_2}}`
- `{{capability_3}}`
- `{{capability_4}}`
## Tools
| # | Tool | Purpose |
|---|------|---------|
| 1 | `{{tool_1}}` | `{{tool_purpose_1}}` |
| 2 | `{{tool_2}}` | `{{tool_purpose_2}}` |
## Agent_group Position
- Agent_group: `{{agent_group_name}}`
- Peers: `{{peer_agent_1}}`, `{{peer_agent_2}}`
- Upstream: `{{upstream_agent_or_none}}`
- Downstream: `{{downstream_agent_or_none}}`
## File Structure
```
agents/{{agent_slug}}/
  agent_package/
    SPEC_{{AGENT_UPPER}}_001_MANIFEST.md
    SPEC_{{AGENT_UPPER}}_002_QUICK_START.md
    SPEC_{{AGENT_UPPER}}_003_PRIME.md
    SPEC_{{AGENT_UPPER}}_004_INSTRUCTIONS.md
    SPEC_{{AGENT_UPPER}}_005_ARCHITECTURE.md
    SPEC_{{AGENT_UPPER}}_006_OUTPUT_TEMPLATE.md
    SPEC_{{AGENT_UPPER}}_007_EXAMPLES.md
    SPEC_{{AGENT_UPPER}}_008_ERROR_HANDLING.md
    SPEC_{{AGENT_UPPER}}_009_UPLOAD_KIT.md
    SPEC_{{AGENT_UPPER}}_010_SYSTEM_INSTRUCTION.md
```
## Routing
- Triggers: `{{trigger_phrase_1}}`, `{{trigger_phrase_2}}`
- Keywords: `{{routing_keyword_1}}`, {{routing_keyword_2}}, `{{routing_keyword_3}}`
- NOT when: `{{exclusion_scenario_1}}`, `{{exclusion_scenario_2}}`
## Input / Output
### Input
- Required: `{{required_input_1}}`, `{{required_input_2}}`
- Optional: `{{optional_input_1}}`
### Output
- Primary: `{{primary_output_artifact}}`
- Secondary: `{{secondary_output_or_none}}`
## Quality Gates
HARD gates: YAML parses, id matches p02_agent_ pattern, kind == agent, quality == null,
required fields present, agent_package >= 10 files, llm_function == BECOME.
SOFT gates: tldr <= 160ch, tags >= 3, capabilities_count matches body,
density >= 0.80, agent_group assigned, domain specific.
## Footer
version: `{{version}}` | author: `{{author}}` | quality: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_agent]] | downstream | 0.34 |
| [[bld_schema_agent]] | downstream | 0.29 |
| [[p11_qg_agent]] | downstream | 0.28 |
| [[bld_examples_agent]] | downstream | 0.27 |
| [[bld_instruction_agent]] | upstream | 0.27 |
| [[bld_knowledge_card_agent]] | upstream | 0.26 |
| [[agent-builder]] | upstream | 0.25 |
| [[bld_collaboration_agent_card]] | downstream | 0.22 |
| [[p01_kc_agent]] | upstream | 0.21 |
| [[p11_qg_agent-card]] | downstream | 0.21 |
