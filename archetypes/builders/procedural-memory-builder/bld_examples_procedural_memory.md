---
kind: examples
id: bld_examples_procedural_memory
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of procedural_memory artifacts
quality: 9.0
title: "Examples: procedural_memory artifacts"
version: "2.0.0"
author: n06_commercial
tags: [procedural_memory, builder, examples]
tldr: "Golden example: Voyager-style skill library with verification. Anti-examples: declarative memory (wrong kind) and enterprise automation platform (wrong domain)."
domain: "LLM agent procedural memory"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

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
