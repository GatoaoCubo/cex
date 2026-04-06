---
kind: output_template
id: bld_output_template_toolkit
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a toolkit
pattern: every field here exists in the schema; template derives, never invents
---

# Output Template: toolkit
Naming pattern: `p04_tk_{name}.yaml`
Filename: `p04_tk_{{name}}.yaml`
```yaml
---
id: p04_tk_{{name}}
kind: toolkit
pillar: P04
quality: null
tags: [toolkit, {{category}}, P04]
---

name: "{{toolkit_name_snake_case}}"
category: "{{file_ops|git_ops|search|web|system|build|analysis}}"
requires_confirmation: {{true|false}}
scope: "{{nucleus|global|agent}}"
target_agent: "{{agent_or_nucleus_slug_or_omit}}"
mcp_server: "{{mcp_server_name_or_omit}}"
tools:
  - name: "{{tool_name_snake_case}}"
    description: "{{one_line_purpose_max_80_chars}}"
    confirmation: "{{auto|confirm|deny}}"
    mcp_endpoint: "{{/path/to/endpoint_or_omit}}"
    denied_for: [{{agent_slugs_or_omit}}]
    risk_level: "{{read|write|delete|dangerous_or_omit}}"
  - name: "{{tool_name_2}}"
    description: "{{one_line_purpose}}"
    confirmation: "{{auto|confirm|deny}}"
deny_list:
  - tool: "{{tool_name}}"
    denied_for: [{{agent_slugs}}]
    reason: "{{justification_for_denial_or_omit}}"
review_date: "{{ISO_8601_date_or_omit}}"
```
## Derivation Notes
- The four top-level fields (name, tools, category, requires_confirmation) are required
- Each tool MUST have name, description, and confirmation
- `mcp_endpoint`, `denied_for`, `risk_level` are per-tool optional fields
- `scope`, `target_agent`, `mcp_server`, `deny_list`, `review_date` are top-level optional
- Omit absent optional fields instead of filling with placeholder strings
- Read tools: confirmation = auto. Write tools: confirmation = confirm. Dangerous: deny.
- Maximum 15 tools per toolkit — split by category if more are needed
