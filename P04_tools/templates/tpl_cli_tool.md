---
# TEMPLATE: CLI Tool (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.cli_tool)
# Max 1024 bytes

id: p04_cli_{{TOOL_SLUG}}
kind: cli_tool
pillar: P04
title: "CLI Tool: {{TOOL_NAME}}"
quality: {{QUALITY_7_TO_10}}
---

# CLI Tool: {{TOOL_NAME}}

## Purpose
{{ONE_SENTENCE_ON_WHAT_THIS_COMMAND_DOES}}

## Usage
```bash
{{TOOL_NAME}} {{COMMAND}} {{FLAGS}}
```

## Inputs / Outputs
- Input: {{EXPECTED_INPUT}}
- Output: {{EXPECTED_OUTPUT}}
- Exit codes: {{EXIT_CODE_RULES}}

## Guardrails
- Safe default: {{DEFAULT_BEHAVIOR}}
- Dangerous flag: {{FLAG_TO_AVOID_OR_CONFIRM}}
