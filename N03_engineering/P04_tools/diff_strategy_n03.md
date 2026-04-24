---
id: p04_ds_n03
kind: diff_strategy
8f: F6_produce
pillar: P04
title: "Diff Strategy -- N03 Smart Patch Application"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 9.1
tags: [diff-strategy, N03, patch, rewrite, migrate, smart-diff, 8F]
tldr: "Smart diff and patch application strategy for N03 REWRITE and MIGRATE operations. Defines when to patch (targeted change), when to rewrite (structural change), and how to apply both safely with git-based rollback."
density_score: 0.89
updated: "2026-04-17"
related:
  - bld_tools_diff_strategy
  - p01_kc_prompt_evolution
  - bld_output_template_kind
  - bld_instruction_input_schema
  - bld_knowledge_card_edit_format
  - bld_examples_changelog
  - bld_instruction_changelog
  - p03_sp_n03_creation_nucleus
  - bld_examples_edit_format
  - bld_instruction_interface
---

# Diff Strategy: N03 Smart Patch Application

## Purpose

N03 handles 3 build verbs that modify EXISTING artifacts: REWRITE, MIGRATE, IMPROVE.
Each requires a different diff strategy. Wrong strategy = data loss or incoherent artifacts.

**Inventive Pride rule:** never overwrite without knowing what you're replacing.

## Strategy Selection Matrix

| Verb | Change Size | Structure Change | Strategy |
|------|-------------|-----------------|---------|
| IMPROVE | < 30% of body | no | targeted_patch |
| REWRITE | any | possible | section_by_section |
| MIGRATE | < 50% | yes (schema change) | schema_migration |
| REWRITE | > 70% different | yes | full_rewrite |

## Strategy 1: Targeted Patch

**When:** IMPROVE verb + change confined to 1-2 sections

**Protocol:**
1. Load existing artifact (git HEAD version)
2. Identify target sections from improvement rationale
3. Generate replacement content for ONLY those sections
4. Apply using sed-equivalent: match H2 heading -> replace until next H2
5. Verify: diff --unified shows only intended sections changed
6. Run cex_compile.py + quality_gate check

**Safety:** `git stash` before patching; restore if compile fails

```python
def targeted_patch(artifact_path: str, target_sections: list[str], new_content: dict) -> str:
    """Replace specific H2 sections while preserving the rest."""
    with open(artifact_path) as f:
        original = f.read()
    
    result = original
    for section_title in target_sections:
        pattern = rf'(## {re.escape(section_title)}\n)(.*?)(?=\n## |\Z)'
        replacement = f'## {section_title}\n{new_content[section_title]}'
        result = re.sub(pattern, replacement, result, flags=re.DOTALL)
    
    return result
```

## Strategy 2: Section-by-Section Rewrite

**When:** REWRITE verb OR > 30% change with no structural migration

**Protocol:**
1. Load existing artifact + F4 plan for new version
2. Map old sections -> new sections (keep/adapt/drop/add)
3. For each new section: keep if unchanged, write if changed, skip if dropped
4. Frontmatter: preserve all existing fields; update only `updated` date and modified fields
5. Write full artifact
6. Run full F7 GOVERN (not just compile)

**Section mapping:**
```yaml
section_map:
  "## Purpose":        keep          # stable sections preserved
  "## Fields":         adapt         # table updated
  "## Validation":     rewrite       # logic changed
  "## Examples":       add           # new section added
  "## Legacy Notes":   drop          # removed from spec
```

## Strategy 3: Schema Migration

**When:** MIGRATE verb (schema version bump, frontmatter field changes)

**Protocol:**
1. Load old artifact (current)
2. Load new schema (validation_schema_artifact.md)
3. Apply migration script:
   - Add new required fields with defaults
   - Rename fields per migration map
   - Remove deprecated fields
   - Update `version` in frontmatter
4. Preserve body content unchanged
5. Run L1 hard gates ONLY (body is trusted; frontmatter changed)

**Migration map format:**
```yaml
migration_v1_to_v2:
  add:
    - field: density_score
      default: 0.85
  rename:
    - from: updated_at
      to: updated
  remove:
    - field: legacy_id
  version_bump: minor  # 1.0.0 -> 1.1.0
```

## Rollback Protocol

Every modification is protected by git:

```bash
# Before any patch/rewrite:
git stash push -m "pre-patch backup: {artifact_id}"

# After successful patch:
git stash drop

# On failure (compile error or gate failure):
git stash pop    # restore original
# Then: apply bugloop or escalate
```

## Diff Output Format

```yaml
diff_result:
  strategy: targeted_patch
  artifact: N03_engineering/P06_schema/input_schema_build_contract.md
  sections_changed: ["## Validation Rules"]
  sections_added: []
  sections_removed: []
  lines_changed: 8
  lines_added: 3
  lines_removed: 2
  frontmatter_fields_changed: ["updated"]
  compile_result: pass
  quality_gate_result: pass
  rollback_available: true
  stash_ref: "stash@{0}"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_diff_strategy]] | related | 0.22 |
| [[p01_kc_prompt_evolution]] | upstream | 0.21 |
| [[bld_output_template_kind]] | downstream | 0.20 |
| [[bld_instruction_input_schema]] | upstream | 0.19 |
| [[bld_knowledge_card_edit_format]] | upstream | 0.19 |
| [[bld_examples_changelog]] | downstream | 0.18 |
| [[bld_instruction_changelog]] | upstream | 0.18 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.18 |
| [[bld_examples_edit_format]] | downstream | 0.18 |
| [[bld_instruction_interface]] | upstream | 0.17 |
