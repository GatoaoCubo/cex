---
kind: output_template
id: bld_output_template_computer_use
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a computer_use artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: computer_use
```yaml
id: p04_cu_{{target_slug}}
kind: computer_use
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_tool_name}}"
target: {{desktop|browser|mobile|terminal}}
resolution: "{{width}}x{{height}}"
actions_supported:
  - {{click|type|scroll|key_press|drag|double_click|screenshot}}
  - {{action_2}}
coordinate_system: {{absolute|relative}}
screenshot_mode: {{before_action|on_demand|continuous}}
safety_constraints:
  - "{{constraint_1}}"
  - "{{constraint_2}}"
quality: null
tags: [computer_use, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_tool_does_max_200ch}}"
```
## Overview
{{what_this_tool_controls_1_to_2_sentences}}
{{observe_act_loop_description}}
## Actions
### {{action_name_1}} (e.g., click)
Parameters: {{x: int, y: int, button: left|right|middle}}
Behavior: {{what_happens_when_action_executes}}
### {{action_name_2}} (e.g., type)
Parameters: {{text: string}}
Behavior: {{what_happens_when_action_executes}}
### {{action_name_3}} (e.g., screenshot)
Parameters: {{none or region: {x, y, w, h}}}
Returns: {{base64 image or file path}}
## Coordinate System
Origin: {{top-left (0,0)}}
Direction: {{x increases right, y increases down}}
Units: {{pixels}}
Resolution: {{width}}x{{height}} — all coordinates within this space
## Safety
- {{safety_constraint_1}}
- {{safety_constraint_2}}
- Sandbox: {{sandboxing_requirement}}
