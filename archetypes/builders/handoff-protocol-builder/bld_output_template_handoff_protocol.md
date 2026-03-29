---
kind: output_template
id: bld_output_template_handoff_protocol
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a handoff_protocol artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: handoff_protocol
```yaml
id: p02_handoff_{{slug}}
kind: handoff_protocol
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{name}}}}"
trigger: "{{trigger}}}}"
context_passed: "{{context_passed}}}}"
return_contract: "{{return_contract}}}}"
quality: null
tags: [handoff_protocol, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{description}}}}"
source_agent: "{{source_agent}}}}"
target_agent: "{{target_agent}}}}"
timeout: "{{timeout}}}}"
retry_policy: "{{retry_policy}}}}"
escalation: "{{escalation}}}}"
```
## Overview
{{overview_content}}
## Trigger
{{trigger_content}}
## Context Transfer
{{context_transfer_content}}
## Return Contract
{{return_contract_content}}

