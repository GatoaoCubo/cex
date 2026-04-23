---
id: p01_kc_skill
kind: knowledge_card
type: kind
pillar: P04
title: "Skill — Deep Knowledge for skill"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: skill
quality: 9.1
tags: [skill, p04, reusable, kind-kc]
tldr: "Reusable capability with structured phases, triggers, and lifecycle management for repeatable workflows"
when_to_use: "Building, reviewing, or reasoning about skill artifacts"
keywords: [skill, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [skill]
density_score: null
llm_function: REASON
related:
  - shared_skill_verification_protocol
  - bld_architecture_kind
  - bld_instruction_kind
  - plugin-builder
  - p03_ins_skill_builder
  - bld_output_template_kind
  - bld_collaboration_plugin
  - bld_architecture_skill
  - bld_schema_skill
  - p04_skill_verify
---
# Skill

This ISO defines a plugin contract: the extension surface a host uses to load, register, and invoke external capability.

## Spec
```yaml
kind: skill
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_skill_{{name}}.md + .yaml
core: true


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[shared_skill_verification_protocol]] | related | 0.27 |
| [[bld_architecture_kind]] | downstream | 0.22 |
| [[bld_instruction_kind]] | upstream | 0.22 |
| [[plugin-builder]] | related | 0.22 |
| [[p03_ins_skill_builder]] | upstream | 0.21 |
| [[bld_output_template_kind]] | downstream | 0.21 |
| [[bld_collaboration_plugin]] | related | 0.21 |
| [[bld_architecture_skill]] | downstream | 0.21 |
| [[bld_schema_skill]] | downstream | 0.20 |
| [[p04_skill_verify]] | related | 0.19 |
