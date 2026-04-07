---
id: "p03_ap_"PLACEHOLDER""
kind: action_prompt
version: 1.0.0
title: Template - Action Prompt
tags: [template, action, prompt, tool-use, execution]
tldr: Prompt that triggers tool calls. Defines trigger patterns, action mapping, param extraction, confirmation.
quality: 9.0
action: PLACEHOLDER
input_required: ['PLACEHOLDER', 'PLACEHOLDER', 'PLACEHOLDER']
output_expected: PLACEHOLDER
updated: "2026-04-07"
domain: "prompt engineering"
author: n03_builder
created: "2026-04-07"
density_score: 1.0
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
1. **Destructive** (delete, overwrite): Always confirm
2. **Creative** (create, generate): Execute immediately
3. **Query** (list, score): Execute immediately
## Quality Gate
1. [ ] At least 2 trigger patterns
2. [ ] Actions map to real tools
3. [ ] Parameters extractable from NL
4. [ ] Destructive actions need confirmation

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `action_prompt` |
| Pillar |  |
| Domain | prompt engineering |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |
