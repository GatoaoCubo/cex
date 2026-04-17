---
id: "p03_ap_{{ACTION_SLUG}}"
kind: action_prompt
pillar: P03
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
| Pillar | P03 |
| Domain | prompt engineering |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## System Context

This artifact participates in the CEX typed knowledge system, a fractal
architecture with 12 pillars, 8 nuclei, and 125 specialized builders.
Artifacts flow through the 8F pipeline: Focus, Frame, Fetch, Filter,
Format, Forge, Furnish, and Feedback.

Quality is enforced via 3-layer scoring: structural (30%), rubric (30%),
and semantic (40%). All artifacts target quality >= 9.0.

| Layer | Weight | Method |
|-------|--------|--------|
| Structural | 30% | Automated count-based checks |
| Rubric | 30% | Quality gate dimension scoring |
| Semantic | 40% | LLM evaluation (when L1+L2 >= 8.5) |
