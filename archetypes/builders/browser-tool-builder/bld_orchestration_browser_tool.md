---
kind: collaboration
id: bld_collaboration_browser_tool
pillar: P12
llm_function: COLLABORATE
purpose: How browser-tool-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Browser Tool"
version: "1.0.0"
author: n03_builder
tags: [browser_tool, builder, examples]
tldr: "Golden and anti-examples for browser tool construction, demonstrating ideal structure and common pitfalls."
domain: "browser tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_builder
  - bld_collaboration_vision_tool
  - bld_collaboration_search_tool
  - browser-tool-builder
  - bld_collaboration_agent_computer_interface
  - bld_collaboration_golden_test
  - bld_collaboration_agent
  - bld_architecture_kind
  - bld_collaboration_response_format
  - bld_collaboration_computer_use
---

# Collaboration: browser-tool-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what browser actions does this tool perform, and how does it select and interact with DOM elements?"
I do not analyze images. I do not wrap search APIs. I do not control generic screen pixels.
I specify DOM-based browser automation so agents and pipelines can extract web data, interact with forms, and capture screenshots in a reproducible, engine-declared way.
## Crew Compositions
### Crew: "Web Data Extraction"
```
  1. browser-tool-builder -> "browser automation spec (navigate, extract, output schema)"
  2. input-schema-builder -> "input validation for URLs and extraction params"
  3. formatter-builder -> "output formatting (json normalization, field mapping)"
```
### Crew: "Research Pipeline"
```
  1. search-tool-builder -> "discover URLs via search API"
  2. browser-tool-builder -> "extract structured data from each URL via DOM"
  3. knowledge-card-builder -> "package extracted data as knowledge cards"
```
### Crew: "E2E Test Automation"
```
  1. browser-tool-builder -> "define page interaction sequence"
  2. golden-test-builder -> "define expected outputs per action"
  3. smoke-eval-builder -> "validate tool behavior against golden outputs"
```
### Crew: "Autonomous Web Agent"
```
  1. browser-tool-builder -> "DOM interaction spec (click, type, navigate)"
  2. agent-builder -> "agent that reads spec and drives browser_use engine"
  3. signal-builder -> "completion signals after extraction"
```
## Handoff Protocol
### I Receive
- seeds: target URL pattern, data fields to extract, interaction sequence
- optional: engine preference, stealth requirements, output schema, viewport config
### I Produce
- browser_tool artifact (.md + .yaml frontmatter)
- committed to: `cex/P04_tools/examples/p04_browser_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Browser tools can be defined standalone.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder | Agents invoke browser_tools to gather web data |
| instruction-builder | Recipes reference browser_tools as data-collection steps |
| hook-builder | Hooks may trigger browser_tools on URL discovery events |
| workflow-builder | Workflows chain browser_tools in multi-step extraction pipelines |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_builder]] | sibling | 0.41 |
| [[bld_collaboration_vision_tool]] | sibling | 0.40 |
| [[bld_collaboration_search_tool]] | sibling | 0.39 |
| [[browser-tool-builder]] | upstream | 0.38 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.38 |
| [[bld_collaboration_golden_test]] | sibling | 0.37 |
| [[bld_collaboration_agent]] | sibling | 0.36 |
| [[bld_architecture_kind]] | upstream | 0.35 |
| [[bld_collaboration_response_format]] | sibling | 0.35 |
| [[bld_collaboration_computer_use]] | sibling | 0.35 |
