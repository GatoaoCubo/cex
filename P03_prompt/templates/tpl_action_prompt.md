---
id: "p03_ap_"PLACEHOLDER""
kind: action_prompt
version: 1.0.0
title: Template - Action Prompt
tags: [template, action, prompt, tool-use, execution]
tldr: Prompt that triggers tool calls. Defines trigger patterns, action mapping, param extraction, confirmation.
quality: 8.6
action: PLACEHOLDER
input_required: ['PLACEHOLDER', 'PLACEHOLDER', 'PLACEHOLDER']
output_expected: PLACEHOLDER
---

# Action Prompt: [NAME]

## Purpose
[WHAT this action_prompt does]
## Trigger Patterns
```yaml
patterns:
  - "create {kind} about {topic}"
  - "build {kind} for {domain}"
  - "list {kind}"
  - "score {path}"
```
## Action Mapping
| Pattern | Action | Parameters |
|---------|--------|-----------|
| "create {kind}" | create_artifact | kind, topic |
| "build {kind}" | build_artifact | kind, domain |
| "list {kind}" | list_artifacts | kind, filter |
| "score {path}" | score_artifact | path |
## Confirmation Rules
- **Destructive** (delete, overwrite): Always confirm
- **Creative** (create, generate): Execute immediately
- **Query** (list, score): Execute immediately
## Quality Gate
- [ ] At least 2 trigger patterns
- [ ] Actions map to real tools
- [ ] Parameters extractable from NL
- [ ] Destructive actions need confirmation
