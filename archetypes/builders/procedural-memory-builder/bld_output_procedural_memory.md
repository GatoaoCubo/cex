---
kind: output_template
id: bld_output_template_procedural_memory
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for procedural_memory production
quality: 9.1
title: "Output Template: procedural_memory"
version: "2.0.0"
author: n06_commercial
tags: [procedural_memory, builder, output_template]
tldr: "Template for LLM agent procedural memory artifacts: skill definitions table, namespace, backend, verification, reflexion notes, tier matrix"
domain: "LLM agent procedural memory"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_schema_procedural_memory
  - bld_instruction_procedural_memory
  - procedural-memory-builder
  - bld_knowledge_card_procedural_memory
  - bld_examples_procedural_memory
  - p03_sp_procedural_memory_builder
  - p10_qg_procedural_memory
  - bld_collaboration_procedural_memory
  - p10_mem_procedural_memory_builder
  - bld_collaboration_skill
---

```yaml
---
id: p10_pm_{{agent_slug}}
kind: procedural_memory
pillar: P10
title: "Procedural Memory: {{agent_name}}"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{agent_domain}}"
quality: null
tags: [procedural_memory, {{agent_slug}}, {{tier}}]
tldr: "{{one_sentence_summary}}"
tier: "{{tier}}"
skill_format: "{{skill_format}}"
skill_count: {{skill_count}}
verification: "{{verification}}"
namespace_pattern: "{{namespace_pattern}}"
storage_backend: "{{storage_backend}}"
reflexion_enabled: {{true_or_false}}
---
```

<!-- id: Unique identifier following ^p10_pm_[a-z][a-z0-9_]+ -->
<!-- agent_slug: snake_case agent name (e.g., coding_assistant_v2) -->
<!-- tier: free | pro | enterprise -->
<!-- skill_format: code | yaml | natural_language | json | mixed -->
<!-- skill_count: integer count of skills defined (0 for free tier) -->
<!-- verification: unit_test | test_case | human_review | ci_pipeline | none -->
<!-- namespace_pattern: key hierarchy (e.g., "coding.{task}") -->
<!-- storage_backend: redis | postgresql | filesystem | in_memory -->

## Overview

{{agent_name}} procedural memory for {{agent_domain}}. Tier: {{tier}}.
Skill format: {{skill_format}}. Reference design: Voyager (Wang 2023) skill library.
{{free_tier_note}}

<!-- free_tier_note: For free tier only: "Free tier: no procedural memory. Agent reasons from scratch on each task." -->
<!-- For PRO/ENTERPRISE: remove free_tier_note and proceed with sections below. -->

## Skill Definitions

| Skill ID | Name | Format | Storage Key | Verification | Tier Required |
|----------|------|--------|-------------|-------------|---------------|
| {{skill_id_1}} | {{skill_name_1}} | {{skill_format}} | {{namespace_pattern}}.{{task_1}} | {{verification}} | {{tier_req_1}} |
| {{skill_id_2}} | {{skill_name_2}} | {{skill_format}} | {{namespace_pattern}}.{{task_2}} | {{verification}} | {{tier_req_2}} |

<!-- Add rows per skill. Remove section entirely for free tier. -->

## Skill Namespace

- Pattern: `{{namespace_pattern}}`
- Example keys: `{{example_key_1}}`, `{{example_key_2}}`
- Lookup method: {{lookup_method}} (exact | semantic | hybrid)
- Conflict resolution: latest_wins | version_pinned | manual_review

## Storage Backend

- Backend: {{storage_backend}}
- Encoding: {{encoding}} (e.g., JSON, YAML, raw code string)
- Key expiry: {{ttl_days}} days (or null for persistent)
- Max skills: {{max_skills}} (null = unlimited for enterprise)

## Verification Strategy

Reference: Voyager (Wang 2023) verify-before-store pattern.
- Method: {{verification}}
- On failure: {{failure_action}} (reject | quarantine | human_review)
- Test coverage target: {{test_coverage}}%
- Sandbox: {{sandbox_type}} (e.g., Docker, E2B, none)

## Reflexion Notes

<!-- Optional section. Include if reflexion_enabled: true -->
- Storage: co-located with skill in {{storage_backend}}, key suffix `.reflexion`
- Format: natural language paragraph describing past failures and lessons
- Retrieval: retrieved alongside the skill on every invocation
- Max length: {{reflexion_max_chars}} characters

## Commercial Tier Matrix

| Feature | Free | Pro | Enterprise |
|---------|------|-----|------------|
| Skill library | None | Up to {{pro_skill_limit}} skills | Unlimited |
| Skill format | N/A | {{pro_skill_format}} | {{enterprise_skill_format}} |
| Verification | N/A | {{pro_verification}} | CI pipeline + audit |
| Cross-agent sharing | N/A | Within workspace | Cross-org with ACL |
| Skill versioning | N/A | Latest only | Full history + rollback |
| Reflexion notes | None | Per-session | Persistent + searchable |
| Access control | N/A | None | Role-based skill ACL |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_procedural_memory]] | downstream | 0.63 |
| [[bld_instruction_procedural_memory]] | upstream | 0.59 |
| [[procedural-memory-builder]] | downstream | 0.49 |
| [[bld_knowledge_card_procedural_memory]] | upstream | 0.49 |
| [[bld_examples_procedural_memory]] | downstream | 0.48 |
| [[p03_sp_procedural_memory_builder]] | upstream | 0.45 |
| [[p10_qg_procedural_memory]] | downstream | 0.40 |
| [[bld_collaboration_procedural_memory]] | downstream | 0.40 |
| [[p10_mem_procedural_memory_builder]] | downstream | 0.38 |
| [[bld_collaboration_skill]] | downstream | 0.37 |
