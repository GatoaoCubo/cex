---
kind: output_template
id: bld_output_template_handoff
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a handoff
pattern: every field here exists in SCHEMA.md; template derives, never invents
quality: 9.1
title: "Output Template Handoff"
version: "1.0.0"
author: n03_builder
tags: [handoff, builder, examples]
tldr: "Golden and anti-examples for handoff construction, demonstrating ideal structure and common pitfalls."
domain: "handoff construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p12_ho_admin_template
  - bld_schema_handoff
  - bld_knowledge_card_handoff
  - bld_config_handoff
  - p01_kc_handoff
  - bld_examples_handoff
  - bld_instruction_handoff
  - p06_iface_agent_group_handoff
  - p03_sp_handoff_builder
  - handoff-builder
---

# Output Template: handoff
Naming pattern: `p12_ho_{task}.md`
Filename: `p12_ho_{{task_slug}}.md`
```yaml
id: p12_ho_{{task_slug}}
kind: handoff
lp: P12

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

agent_group: "{{target_agent_group}}"
mission: "{{mission_name}}"
autonomy: "{{full|supervised|assisted}}"
quality_target: {{7.0_to_10.0}}

domain: "{{domain_value}}"
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"

dependencies: [{{dep_handoff_ids_or_omit}}]
seeds: [{{seed_1}}, {{seed_2}}, {{seed_3}}]
agent: "{{agent_name_or_omit}}"
skill: "{{skill_name_or_omit}}"

batch: "{{batch_id_or_omit}}"
wave: {{wave_number_or_omit}}
keywords: [{{keyword_1}}, {{keyword_2}}]
linked_artifacts:

  primary: "{{primary_ref_or_omit}}"
  related: [{{related_refs_or_omit}}]
```
# `{{AGENT_GROUP}}` — {{MISSION}}: `{{Title}}`
**`{{Autonomy}}` Autonomy** | **Quality `{{quality_target}}`+**
**REGRA: Commit and signal ANTES de qualquer pausa.**
## Context
`{{why_this_work_is_needed}}`
`{{relevant_background}}`
## Tasks
### Step 1: `{{ACTION_VERB}}`
`{{specific_actionable_instruction}}`
### Step 2: `{{ACTION_VERB}}`
`{{specific_actionable_instruction}}`
## Scope Fence
1. SOMENTE: `{{allowed_paths}}`
2. NAO TOQUE: `{{forbidden_paths}}`
## Commit
```bash
git add {{paths}}
git commit -m "{{agent_group}}[{{mission}}]: {{description}}"
```
## Signal
```bash
python -c "from records.core.python.signal_writer import write_signal; write_signal('{{agent_group}}', 'complete', {{quality_score}})"
```
## Derivation Notes
1. Frontmatter fields are the machine-readable contract from SCHEMA.md
2. Body sections are the human-readable execution brief
3. Omit absent optional frontmatter fields instead of using placeholders
4. Tasks must be specific: each step = one action verb

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | handoff construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_ho_admin_template]] | downstream | 0.42 |
| [[bld_schema_handoff]] | downstream | 0.41 |
| [[bld_knowledge_card_handoff]] | upstream | 0.41 |
| [[bld_config_handoff]] | downstream | 0.39 |
| [[p01_kc_handoff]] | downstream | 0.38 |
| [[bld_examples_handoff]] | downstream | 0.33 |
| [[bld_instruction_handoff]] | upstream | 0.31 |
| [[p06_iface_agent_group_handoff]] | downstream | 0.31 |
| [[p03_sp_handoff_builder]] | upstream | 0.31 |
| [[handoff-builder]] | downstream | 0.30 |
