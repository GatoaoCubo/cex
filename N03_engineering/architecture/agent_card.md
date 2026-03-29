---
id: "{{PILLAR}}_ac_{{AGENT_ID}}"
kind: agent_card
pillar: "{{PILLAR}}"
version: "1.0.0"
created: "{{DATE}}"
updated: "{{DATE}}"
author: "{{AUTHOR}}"
name: "{{AGENT_NAME}}"
role: "{{ROLE_DESCRIPTION}}"
model: "{{MODEL}}"
mcps: [{{MCPS}}]
domain_area: "{{DOMAIN}}"
boot_sequence: [{{BOOT_STEPS}}]
capabilities: [{{CAPABILITIES}}]
constraints: [{{CONSTRAINTS}}]
quality: null
tags: [{{TAGS}}]
tldr: "{{ONE_LINE_DESCRIPTION}}"
---
## Identity
{{AGENT_NAME}} is the {{DOMAIN}} nucleus agent.
Role: {{ROLE_DESCRIPTION}}

## Model & Tools
- Model: {{MODEL}}
- MCPs: {{MCPS}}
- Boot: {{BOOT_TIME}}

## Capabilities
{{CAPABILITIES_DETAIL}}

## Constraints
{{CONSTRAINTS_DETAIL}}
