---
kind: examples
id: bld_examples_agent
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of agent artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: agent-builder
## Golden Example
INPUT: "Create agent definition for a knowledge-card-builder agent"
OUTPUT:
```yaml
id: p02_agent_knowledge_card_builder
kind: agent
pillar: P02
title: "Knowledge Card Builder Agent"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
agent_node: "knowledge-engine"
domain: "knowledge_distillation"
llm_function: BECOME
capabilities_count: 5
tools_count: 2
iso_files_count: 10
routing_keywords: [knowledge-card, distillation, atomic-facts, density, P01]
quality: null
tags: [agent, knowledge, distillation, P02, P01]
tldr: "Distills raw sources into atomic searchable knowledge_card artifacts with density >= 0.80"
density_score: 0.87
```
## Overview
knowledge-card-builder is a knowledge-engine specialist in knowledge distillation.
Converts raw sources into atomic searchable knowledge_card artifacts with density >= 0.80.
## Architecture
Capabilities: distill raw text to atomic facts, score density, produce P01 frontmatter,
validate sources, detect boundary (knowledge_card vs context_doc vs glossary_entry).
Tools: brain_query [MCP] (dedup check), validate_artifact.py [PLANNED].
Satellite: knowledge-engine | Upstream: researcher | Downstream: knowledge-index-builder.
## File Structure
```
agents/knowledge_card_builder/agent_package/
  ISO_KNOWLEDGE_CARD_BUILDER_001_MANIFEST.md
  ISO_KNOWLEDGE_CARD_BUILDER_002_QUICK_START.md
  ISO_KNOWLEDGE_CARD_BUILDER_003_PRIME.md
  ISO_KNOWLEDGE_CARD_BUILDER_004_INSTRUCTIONS.md
  ISO_KNOWLEDGE_CARD_BUILDER_005_ARCHITECTURE.md
  ISO_KNOWLEDGE_CARD_BUILDER_006_OUTPUT_TEMPLATE.md
  ISO_KNOWLEDGE_CARD_BUILDER_007_EXAMPLES.md
  ISO_KNOWLEDGE_CARD_BUILDER_008_ERROR_HANDLING.md
  ISO_KNOWLEDGE_CARD_BUILDER_009_UPLOAD_KIT.md
  ISO_KNOWLEDGE_CARD_BUILDER_010_SYSTEM_INSTRUCTION.md
```
## When to Use
Triggers: "create knowledge card for X", "distill research into atomic facts"
NOT when: full narrative needed (context_doc), term definition only (glossary_entry)
## Input / Output
Input: raw_source (text/URL/file), domain. Output: p01_kc_{slug}.md + density report.
Receives from: researcher. Produces for: knowledge_index, pool (quality >= 8.0).
## Common Issues
1. Generic bullets: compress to concrete data, remove filler
2. Missing source: verify before citing
3. Boundary: narrative -> context-doc-builder
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p02_agent_ pattern (H02 pass) | kind: agent (H04 pass)
- 19 fields (H06 pass) | llm_function: BECOME (H07 pass) | agent_node: knowledge-engine (H08 pass)
- agent_package 10 files (S05 pass) | capabilities_count: 5 matches body (S06 pass)
- tldr: 71ch (S01 pass) | density: 0.87 (S09 pass) | no filler (S10 pass)
## Anti-Example
INPUT: "Create agent for a helper bot"
BAD OUTPUT:
```yaml
id: helper_agent
kind: bot
pillar: assistant
title: Helper
agent_node: none
quality: 8.0
tags: [helper]
tldr: "This is a helpful agent that can assist users with various tasks and provide support."
```
You are a helpful assistant. I can help you with many things.
FAILURES:
1. id: no `p02_agent_` prefix -> H02 FAIL
2. kind: "bot" not "agent" -> H04 FAIL
3. pillar: "assistant" not "P02" -> H06 FAIL
4. quality: 8.0 (not null) -> H05 FAIL
5. agent_node: "none" — must be real agent_node name or "agnostic" -> H08 FAIL
6. Missing fields: version, created, updated, author, domain, llm_function, capabilities_count, tools_count, iso_files_count, routing_keywords -> H06 FAIL
7. tags: only 1 item, missing "agent" -> S02 FAIL
8. tldr: 87 chars but is filler ("This is a helpful agent...") -> S10 FAIL
9. No agent_package section in body -> S05 FAIL
10. No capabilities list — "can help with many things" is not a capability -> S06 FAIL
11. Missing ## Architecture, ## File Structure, ## When to Use sections -> H09 FAIL
12. llm_function missing (defaults are not acceptable) -> H07 FAIL
