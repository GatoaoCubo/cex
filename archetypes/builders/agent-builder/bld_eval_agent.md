---
kind: quality_gate
id: p11_qg_agent
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of agent artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: agent"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, agent, P11, P02, governance, identity, agent-package]
tldr: "Gates for agent artifacts — persona + capabilities + agent_package packages ready for deploy."
domain: agent
created: "2026-03-27"
updated: "2026-03-27"
last_reviewed: "2026-04-18"
density_score: 0.90
related:
  - bld_examples_agent
  - agent-builder
  - bld_collaboration_agent
  - bld_instruction_agent
  - p11_qg_builder
  - bld_architecture_agent
  - p03_sp_agent_builder
  - p11_qg_boot_config
  - bld_collaboration_knowledge_card
  - p01_kc_agent
---

## Quality Gate

# Gate: agent
## Definition
| Field     | Value                                               |
|-----------|-----------------------------------------------------|
| metric    | identity completeness + agent_package navigability |
| threshold | 8.0                                                 |
| operator  | >=                                                  |
| scope     | all agent artifacts (P02)                           |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = broken agent boot |
| H02 | id matches `^p02_agent_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "agent" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All 10 required fields present: id, kind, pillar, title, version, agent_group, domain, quality, tags, tldr | Completeness |
| H07 | llm_function == "BECOME" | Agent is identity construct, not callable |
| H08 | agent_group field is set (not blank or null) | Every agent belongs to a agent_group |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 |
| S02 | tags is list, len >= 3, includes "agent" | 0.5 |
| S03 | agent_package section lists >= 10 spec files | 1.0 |
| S04 | routing_keywords is list, len >= 4 | 0.5 |
| S05 | body has ## File Structure with correct spec naming convention | 1.0 |
| S06 | capabilities_count matches actual bullets in Architecture section | 1.0 |
| S07 | domain is specific (not "general" or "everything") | 0.5 |
| S08 | body has ## When to Use with explicit NOT-when exclusions | 0.5 |
| S09 | density_score >= 0.80 | 0.5 |
| S10 | No filler phrases ("this document", "in summary", "can help with") | 1.0 |
Weights sum: 7.5. Normalize: divide each by 7.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference agent definition |
| >= 8.0 | PUBLISH — register in routing index, deploy agent_package |
| >= 7.0 | REVIEW — complete agent_package or sharpen domain boundary |
| < 7.0  | REJECT — rework identity and capability scope |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Critical agent_group gap requiring immediate agent deploy |
| approver | p02-chief |
| audit_trail | Log in records/audits/ with justification and timestamp |
| expiry | 72h — full gate pass required before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |

## Examples

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
agent_group: "knowledge-engine"
domain: "knowledge_distillation"
llm_function: BECOME
capabilities_count: 5
tools_count: 2
iso_files_count: 10
routing_keywords: [knowledge-card, distillation, atomic-facts, density, P01]
quality: 8.8
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
Agent_group: knowledge-engine | Upstream: researcher | Downstream: knowledge-index-builder.
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
- 19 fields (H06 pass) | llm_function: BECOME (H07 pass) | agent_group: knowledge-engine (H08 pass)
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
agent_group: none
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
5. agent_group: "none" — must be real agent_group name or "agnostic" -> H08 FAIL
6. Missing fields: version, created, updated, author, domain, llm_function, capabilities_count, tools_count, iso_files_count, routing_keywords -> H06 FAIL
7. tags: only 1 item, missing "agent" -> S02 FAIL
8. tldr: 87 chars but is filler ("This is a helpful agent...") -> S10 FAIL
9. No agent_package section in body -> S05 FAIL
10. No capabilities list — "can help with many things" is not a capability -> S06 FAIL
11. Missing ## Architecture, ## File Structure, ## When to Use sections -> H09 FAIL
12. llm_function missing (defaults are not acceptable) -> H07 FAIL

## Golden Example 2 (HERMES — Agent with thinking_budget)
INPUT: "Create agent definition for a deep-research agent that uses extended thinking for competitive analysis"
OUTPUT:
```yaml
id: p02_agent_competitive_intelligence
kind: agent
pillar: P02
title: "Competitive Intelligence Agent"
version: "1.0.0"
created: "2026-04-18"
updated: "2026-04-18"
author: "n03_builder"
agent_group: "intelligence-engine"
domain: "competitive_analysis"
llm_function: BECOME
capabilities_count: 6
tools_count: 4
iso_files_count: 13
routing_keywords: [competitive, market-research, intelligence, analysis, P01, N01]
quality: null
tags: [agent, intelligence, competitive, thinking, P02]
tldr: "Deep competitive analysis agent using extended thinking to produce structured market intelligence"
density_score: 0.89
thinking_budget: xhigh
```
## Overview
competitive-intelligence is an intelligence-engine specialist in competitive analysis.
Uses extended thinking (xhigh budget) to synthesize market signals into structured intelligence
briefs with source provenance and confidence scoring.
## Architecture
Capabilities: web research synthesis, competitor profiling, pricing analysis, feature gap mapping,
trend identification, SWOT generation.
Tools: browser_tool [MCP], knowledge_graph [MCP], retrieve_kc.py [PLANNED], score_source.py [PLANNED].
Agent_group: intelligence-engine | Upstream: n07_orchestrator | Downstream: knowledge-card-builder.
## When to Use
Triggers: "research competitor X", "analyze market Y", "deep dive on Z pricing"
NOT when: shallow FAQ answers needed (knowledge_card retrieval), real-time data not critical.

WHY THINKING_BUDGET=XHIGH:
- Competitive analysis requires multi-step causal reasoning across many sources
- xhigh unlocks Claude's extended thinking for deeper inference chains
- Use `medium` (default) for routine tasks; `xhigh` reserved for synthesis-heavy domains
- OpenCode-Hermes pattern: declare budget explicitly so routing layer can allocate compute

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
