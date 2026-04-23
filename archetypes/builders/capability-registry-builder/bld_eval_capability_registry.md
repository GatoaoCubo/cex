---
kind: quality_gate
id: p08_qg_capability_registry
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for capability_registry
quality: 9.1
title: "Quality Gate Capability Registry"
version: "1.0.0"
author: n04_wave8
tags: [capability_registry, builder, quality_gate, agent-discovery]
tldr: "Quality gate with HARD and SOFT scoring for capability_registry"
domain: "capability_registry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_capability_registry
  - bld_schema_capability_registry
  - bld_output_template_capability_registry
  - bld_instruction_capability_registry
  - p03_sp_capability_registry_builder
  - p11_qg_ai_rmf_profile
  - p12_qg_team_charter
  - p01_qg_faq_entry
  - p11_qg_audit_log
  - p09_qg_marketplace_app_manifest
---

## Quality Gate

## Definition
| Metric                          | Threshold | Operator | Scope                         |
|---------------------------------|-----------|----------|-------------------------------|
| Provider agent path validity    | 100%      | equals   | All registry entries          |
| Required field completeness     | 100%      | equals   | All registry entries          |
| Keyword index non-empty         | 100%      | equals   | All registry entries          |

## HARD Gates
| ID  | Check                                               | Fail Condition                                    |
|-----|-----------------------------------------------------|---------------------------------------------------|
| H01 | YAML frontmatter valid                              | Invalid YAML syntax or missing required fields    |
| H02 | ID matches pattern `^p08_cr_[a-z][a-z0-9_]+\.md$`  | ID format mismatch                                |
| H03 | kind field = "capability_registry"                  | Kind field incorrect or missing                   |
| H04 | registry_scope is valid enum                        | Not one of: builder_sub_agents / nucleus_domain_agents / nucleus_cards / full |
| H05 | entry_count matches actual entries                  | Declared count != real row count                  |
| H06 | All provider_agent paths resolvable                 | Any path points to non-existent file              |
| H07 | availability enum valid for all entries             | Not one of: active / deprecated / experimental    |

## SOFT Scoring
| Dim | Dimension                                         | Weight | Scoring Guide |
|-----|---------------------------------------------------|--------|---------------|
| D01 | Entry completeness (all 8 required fields)        | 0.30   | All fields present = 1.0, 7/8 = 0.7, <7 = 0.3 |
| D02 | Keyword index richness (>= 5 terms per entry)     | 0.20   | Avg >= 5 terms = 1.0, 3-4 terms = 0.6, <3 = 0.2 |
| D03 | Quality baseline accuracy (no invented scores)    | 0.20   | All sourced or "unscored" = 1.0, any invented = 0 |
| D04 | Coverage (all 3 layers represented)               | 0.20   | All 3 layers = 1.0, 2 layers = 0.6, 1 layer = 0.2 |
| D05 | Coverage gaps documented                          | 0.10   | Gaps section present and non-empty = 1.0, present but empty = 0.5, absent = 0 |

## Actions
| Label   | Score  | Action                                           |
|---------|--------|--------------------------------------------------|
| GOLDEN  | >=9.5  | Auto-publish, trigger re-index in cex_query.py   |
| PUBLISH | >=8.0  | Auto-publish after validation                    |
| REVIEW  | >=7.0  | Require N04 manual review                        |
| REJECT  | <7.0   | Reject, flag phantom references and missing fields |

## Bypass
| Condition                   | Approver    | Audit Trail                        |
|-----------------------------|-------------|------------------------------------|
| Emergency crew dispatch     | N07         | Dispatch log + signal with score   |

## Examples

## Golden Example

```markdown
---
id: p08_cr_builder_sub_agents.md
kind: capability_registry
pillar: P08
title: "CEX Builder Sub-Agent Registry"
registry_scope: builder_sub_agents
entry_count: 3
index_date: "2026-04-14"
quality: null
---

## Builder Sub-Agent Index
| capability_name | provider_agent | input_schema | output_schema | cost_tokens | quality_baseline | availability | keyword_index |
|----------------|----------------|--------------|---------------|-------------|-----------------|--------------|---------------|
| Build landing page | .claude/agents/landing-page-builder.md | intent string, brand_config | landing_page (P05 .md) | medium | unscored | active | landing page, html, conversion, marketing, P05 |
| Build knowledge card | .claude/agents/knowledge-card-builder.md | topic, domain, sources | knowledge_card (P01 .md) | low | unscored | active | knowledge card, KC, P01, documentation, RAG |
| Build agent card | .claude/agents/agent-card-builder.md | nucleus id, capabilities list | agent_card (P08 .md) | low | unscored | active | agent card, A2A, capability declaration, P08 |

## Query Examples
| Query | Top Candidate | Why |
|-------|--------------|-----|
| "who can build conversion pages?" | landing-page-builder | keyword: conversion, marketing |
| "who documents domain knowledge?" | knowledge-card-builder | keyword: knowledge card, KC, documentation |
```

## Anti-Example 1: Missing Required Fields

```markdown
| capability_name | provider_agent |
|----------------|----------------|
| Build reports  | some-builder   |
```

### Why it fails:
Missing input_schema, output_schema, cost_tokens, quality_baseline, availability, and keyword_index. Unusable for ranked candidate selection -- N07 cannot determine if the agent is appropriate for a given query.

## Anti-Example 2: Phantom Agent Reference

```markdown
| capability_name | provider_agent | ...
|----------------|----------------|
| Build dashboards | .claude/P02_model/dashboard-builder.md | ...
```

### Why it fails:
`dashboard-builder.md` does not exist in `.claude/agents/`. Registry entries with phantom paths corrupt the discovery index and cause dispatch failures. Every `provider_agent` must be validated as an existing file.

## Anti-Example 3: Invented Quality Scores

```markdown
| capability_name | quality_baseline |
|----------------|-----------------|
| Build landing page | 8.5 |
```

### Why it fails:
The landing-page-builder has `quality: null` (unscored). Inventing a score of 8.5 misleads N07 into preferring this builder over genuinely scored alternatives. Use "unscored" when source has null.

## Anti-Example 4: Flat List Without Layer Separation

```markdown
| capability_name | provider_agent | availability |
|----------------|----------------|--------------|
| Build landing page | .claude/P02_model/landing-page-builder.md | active |
| Knowledge management | N04_knowledge/P02_model/agent_knowledge.md | active |
| Orchestration | N07_admin/agent_card_n07.md | active |
```

### Why it fails:
All three agent layers mixed in one flat table. Builder sub-agents, nucleus domain agents, and nucleus cards have different invocation paths: sub-agents are invoked as Claude Code sub-agents; domain agents via dispatch.sh; nucleus cards describe the nucleus itself. Mixing them causes routing errors where N07 attempts to dispatch a builder sub-agent path as a nucleus boot.

## Key Distinctions
| Aspect | Good Registry Entry | Bad Registry Entry |
|--------|--------------------|--------------------|
| provider_agent | Validated path to existing file | Path to non-existent file |
| quality_baseline | "unscored" when source is null | Invented numeric score |
| keyword_index | >= 5 domain-derived terms | 1-2 generic terms |
| availability | "active" / "deprecated" / "experimental" | Missing or free-text |
| layer | Entries in correct section (builder / nucleus / card) | Mixed flat list |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
