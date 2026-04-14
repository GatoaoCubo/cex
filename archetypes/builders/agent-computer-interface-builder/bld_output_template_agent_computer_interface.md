---
kind: output_template
id: bld_output_template_agent_computer_interface
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for agent_computer_interface production
quality: null
title: "Output Template Agent Computer Interface"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_computer_interface, builder, output_template]
tldr: "Template with vars for agent_computer_interface production"
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

```yaml
id: {{aci_id}}
name: {{aci_name}}
version: {{aci_version}}
pillar: P08
type: agent_computer_interface
description: {{aci_description}}
protocol: {{aci_protocol}}
capabilities:
  - {{capability_1}}
  - {{capability_2}}
auth_method: {{auth_method}}
```

# {{aci_name}} Interface Specification

## Overview
{{aci_summary}}

## Protocol & Communication
{{aci_protocol_details}}

## Functional Capabilities
{{aci_capabilities_list}}

## Endpoint Mapping
{{aci_endpoint_definitions}}

## Security & Authentication
{{aci_security_implementation}}

## Error Handling
{{aci_error_codes}}
