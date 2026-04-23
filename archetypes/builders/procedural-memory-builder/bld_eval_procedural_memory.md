---
kind: quality_gate
id: p10_qg_procedural_memory
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for procedural_memory
quality: 9.0
title: "Quality Gate: procedural_memory"
version: "2.0.0"
author: n06_commercial
tags: [procedural_memory, builder, quality_gate]
tldr: "HARD gates enforce artifact structure (schema, ID, skill_format, tier). SOFT scoring weights domain accuracy, skill completeness, commercial differentiation, and verification coverage."
domain: "LLM agent procedural memory"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_examples_procedural_memory
  - bld_instruction_procedural_memory
  - bld_output_template_procedural_memory
  - bld_schema_procedural_memory
  - p03_sp_procedural_memory_builder
  - p10_qg_consolidation_policy
  - p10_qg_memory_architecture
  - bld_tools_procedural_memory
  - p10_mem_procedural_memory_builder
  - procedural-memory-builder
---

## Quality Gate

## Definition

| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Required frontmatter fields | 100% | == | Artifact |
| skill_format field present | true | == | Artifact |
| tier field present | true | == | Artifact |
| Skills section present | true | == | Artifact |

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|---------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches `^p10_pm_[a-z][a-z0-9_]+$` | ID absent or does not match pattern |
| H03 | kind field equals `procedural_memory` | kind field absent, wrong, or misspelled |
| H04 | `skill_format` field present | Field absent |
| H05 | `tier` field present | Field absent |
| H06 | Skills section present in body | Section absent or empty |
| H07 | Verification strategy defined or explicitly excluded | No mention of skill verification |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|--------------|
| D1 | Domain accuracy | 0.25 | 1.0 = LLM agent skills; 0.0 = hardware/robotics motor schemas without LLM context |
| D2 | Skill coverage | 0.20 | 1.0 = namespace + format + storage + retrieval defined; 0.5 = partial; 0.0 = absent |
| D3 | Commercial differentiation | 0.20 | 1.0 = FREE/PRO/ENTERPRISE matrix with 5+ features; 0.5 = partial; 0.0 = absent |
| D4 | Verification strategy | 0.20 | 1.0 = test-case gating or CI pipeline defined; 0.5 = mentioned; 0.0 = absent |
| D5 | Industry grounding | 0.15 | 1.0 = Voyager/ExpeL/Reflexion cited; 0.5 = 1 citation; 0.0 = none |

## Actions

| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN -- archive as gold standard example |
| >= 8.0 | PUBLISH -- merge to main |
| >= 7.0 | REVIEW -- surgical fix before merge |
| < 7.0 | REJECT -- rebuild required |

## Bypass

| Condition | Approver | Audit Trail |
|-----------|----------|------------|
| Free tier artifact with no skills (correct behavior) | N06 | Tier=free annotation in frontmatter |
| Prototype with unverified skills in dev environment | N07 | Prototype annotation + dev-only tag |

## Examples

## Golden Example: Coding Assistant (PRO tier)

```yaml
---
id: p10_pm_coding_assistant_pro
kind: procedural_memory
pillar: P10
title: "Procedural Memory: Coding Assistant Agent (PRO)"
version: "1.0.0"
created: "2026-04-14"
author: n06_commercial
domain: coding-assistant
quality: null
tags: [procedural_memory, coding, pro, voyager_style]
tldr: "PRO skill library for coding agent: 8 verified Python skills with test-case gating, namespace coding.*, Redis KV backend."
tier: pro
skill_format: code
skill_count: 8
verification: unit_test
namespace_pattern: "coding.{task}"
storage_backend: redis
reflexion_enabled: true
---
```

**Why golden**: all required frontmatter, tier=pro, skill_format=code, verification=unit_test.
Body includes Skill Definitions table with 8 skills, hierarchical namespace `coding.*`,
Redis backend config, test-case gating (Voyager verify-before-store), Reflexion notes section,
and FREE/PRO/ENTERPRISE tier matrix. References Voyager (Wang 2023).

## Anti-Example 1: Declarative Memory Stored in Procedural Kind (Wrong Kind)

```yaml
---
id: p10_pm_salesforce_schema
kind: procedural_memory
title: "Salesforce CRM Entity Definitions"
body:
  - entity: Account
    fields: [Name, Industry, Revenue]
    relationships: "Account -> Contact (one-to-many)"
---
```

**Why it fails**:
- Stores entity definitions (declarative/semantic memory) not skills or procedures
- This belongs in `entity_memory` or `knowledge_card` kind, not `procedural_memory`
- No `skill_format`, no `tier`, no `verification`
- No Skill Definitions table, no Namespace, no Tier Matrix
- Missing all required frontmatter fields

## Anti-Example 2: Enterprise Automation Platform (Wrong Domain)

```yaml
---
id: p10_pm_power_automate_invoice
kind: procedural_memory
name: "Microsoft Power Automate Flow for Invoice Processing"
description: "Azure Cognitive Services + Dynamics 365 invoice workflow"
body:
  - trigger: "Email received in Invoices folder"
  - action: "Extract PDF with Azure Cognitive Services"
  - action: "Create accounting entry in Dynamics 365"
---
```

**Why it fails**:
- Describes enterprise software automation (Power Automate), not LLM agent skills
- No LLM agent context: no prompts, no skill retrieval, no agent execution
- `name` instead of `id`, missing `kind`, `pillar`, `tier`, `skill_format`
- No Voyager/Reflexion references, wrong domain entirely
- Would fail H01 (missing required fields), H02 (no ID), H04 (no skill_format)

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
