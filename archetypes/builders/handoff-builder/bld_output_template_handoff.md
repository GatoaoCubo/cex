---
kind: output_template
id: bld_output_template_handoff
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a handoff
pattern: every field here exists in SCHEMA.md; template derives, never invents
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
agent_node: "{{target_agent_node}}"
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
# {{SATELLITE}} — {{MISSION}}: {{Title}}
**{{Autonomy}} Autonomy** | **Quality {{quality_target}}+**
**REGRA: Commit and signal ANTES de qualquer pausa.**
## Context
{{why_this_work_is_needed}}
{{relevant_background}}
## Tasks
### Step 1: {{ACTION_VERB}}
{{specific_actionable_instruction}}
### Step 2: {{ACTION_VERB}}
{{specific_actionable_instruction}}
## Scope Fence
- SOMENTE: {{allowed_paths}}
- NAO TOQUE: {{forbidden_paths}}
## Commit
```bash
git add {{paths}}
git commit -m "{{agent_node}}[{{mission}}]: {{description}}"
```
## Signal
```bash
python -c "from records.core.python.signal_writer import write_signal; write_signal('{{agent_node}}', 'complete', {{quality_score}})"
```
## Derivation Notes
- Frontmatter fields are the machine-readable contract from SCHEMA.md
- Body sections are the human-readable execution brief
- Omit absent optional frontmatter fields instead of using placeholders
- Tasks must be specific: each step = one action verb
