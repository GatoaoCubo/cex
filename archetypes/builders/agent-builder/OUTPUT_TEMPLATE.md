---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an agent artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: agent

```yaml
---
id: p02_agent_{{agent_slug}}
kind: agent
pillar: P02
title: "{{human_readable_title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
satellite: "{{satellite_name_or_agnostic}}"
domain: "{{primary_domain}}"
llm_function: BECOME
capabilities_count: {{integer_matching_body}}
tools_count: {{integer_matching_body}}
iso_files_count: {{integer_10_or_more}}
routing_keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}, {{keyword_4}}]
quality: null
tags: [agent, {{tag_2}}, {{tag_3}}, {{pillar_tag}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
---
```

## Overview
{{agent_name}} is a {{satellite}} specialist in {{domain}}.
{{two_sentences_primary_function_and_value}}

## Architecture

### Capabilities
- {{capability_1}}
- {{capability_2}}
- {{capability_3}}
- {{capability_4}}

### Tools
- {{tool_1}}: {{tool_purpose_1}}
- {{tool_2}}: {{tool_purpose_2}}

### Satellite Position
Satellite: {{satellite_name}}
Peers: {{peer_agent_1}}, {{peer_agent_2}}
Upstream: {{upstream_agent_or_none}}
Downstream: {{downstream_agent_or_none}}

## File Structure

```
agents/{{agent_slug}}/
  iso_vectorstore/
    ISO_{{AGENT_UPPER}}_001_MANIFEST.md
    ISO_{{AGENT_UPPER}}_002_QUICK_START.md
    ISO_{{AGENT_UPPER}}_003_PRIME.md
    ISO_{{AGENT_UPPER}}_004_INSTRUCTIONS.md
    ISO_{{AGENT_UPPER}}_005_ARCHITECTURE.md
    ISO_{{AGENT_UPPER}}_006_OUTPUT_TEMPLATE.md
    ISO_{{AGENT_UPPER}}_007_EXAMPLES.md
    ISO_{{AGENT_UPPER}}_008_ERROR_HANDLING.md
    ISO_{{AGENT_UPPER}}_009_UPLOAD_KIT.md
    ISO_{{AGENT_UPPER}}_010_SYSTEM_INSTRUCTION.md
```

## When to Use
Triggers: {{trigger_phrase_1}}, {{trigger_phrase_2}}
Keywords: {{routing_keyword_1}}, {{routing_keyword_2}}, {{routing_keyword_3}}
NOT when: {{exclusion_scenario_1}}, {{exclusion_scenario_2}}

## Input / Output

### Input
- Required: {{required_input_1}}, {{required_input_2}}
- Optional: {{optional_input_1}}

### Output
- Primary: {{primary_output_artifact}}
- Secondary: {{secondary_output_or_none}}

## Integration
- Receives from: {{upstream_source}}
- Produces for: {{downstream_consumer}}
- Signal on complete: {{signal_type}}

## Quality Gates
HARD gates: YAML parses, id matches p02_agent_ pattern, kind == agent, quality == null,
required fields present, iso_vectorstore lists >= 10 files, llm_function == BECOME.
SOFT gates: tldr <= 160ch, tags >= 3, capabilities_count matches body,
density >= 0.80, satellite assigned, domain specific.

## Common Issues
1. {{issue_1}}: {{remediation_1}}
2. {{issue_2}}: {{remediation_2}}
3. {{issue_3}}: {{remediation_3}}

## Invocation
```bash
{{invocation_command_or_spawn_pattern}}
```

## Related Agents
- {{related_agent_1}}: {{relationship_1}}
- {{related_agent_2}}: {{relationship_2}}

## Footer
version: {{version}} | author: {{author}} | quality: null
