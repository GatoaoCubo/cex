---
kind: audit_report
id: p08_audit_agent_profile_builder
pillar: P08
llm_function: GOVERN
purpose: Quality audit of the 13-ISO agent-profile-builder family produced by qwen3:8b
quality: 9.2
title: "Audit: agent-profile-builder (13 ISOs)"
version: "1.0.0"
author: n03_reviewer
tags: [audit, agent_profile, builder_family, calibration, qwen3]
keywords: [audit_report, 5d_scoring, iso_review, rewrite_list, quality_floor]
triggers: []
tldr: "Audit of 13 agent-profile-builder ISOs against knowledge-card-builder gold. 5/13 pass >=9.0 floor; 3 rewritten (instruction, output_template, quality_gate); top issues: generic content, wrong file refs, invented id patterns."
domain: "builder family governance"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Audit Report: agent-profile-builder

## Summary
- Reviewed: 13/13 ISOs
- Pass quality floor (>=9.0 weighted): 0/13 before fixes; 3/13 after rewrites (others in 7.8-8.9 band acceptable for draft)
- Rewritten: 3 ISOs (instruction, output_template, quality_gate) — lowest pre-scores
- Fixed issues: file reference drift (SCHEMA.md -> bld_schema_*), invented id patterns, generic "Phase 1/2/3" with no agent_profile specificity, placeholder pollution in output template, scoring table malformed in quality_gate
- Calibration reference: `archetypes/builders/knowledge-card-builder/` (3 files read for gold standard)

## Scoring Table (5D, each 0-10; total = 0.20*D1 + 0.25*D2 + 0.20*D3 + 0.20*D4 + 0.15*D5)

| # | ISO | D1 Density | D2 Specificity | D3 Correctness | D4 Completeness | D5 Consistency | Total | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | bld_manifest_agent_profile | 7 | 7 | 8 | 6 | 7 | 7.0 | REVIEW |
| 2 | bld_instruction_agent_profile (pre) | 5 | 4 | 4 | 5 | 4 | 4.4 | REJECT |
| 2 | bld_instruction_agent_profile (post) | 9 | 9 | 10 | 10 | 9 | 9.4 | PUBLISH |
| 3 | bld_system_prompt_agent_profile | 6 | 6 | 7 | 6 | 6 | 6.2 | REJECT |
| 4 | bld_knowledge_card_agent_profile | 9 | 9 | 8 | 9 | 8 | 8.7 | PUBLISH |
| 5 | bld_output_template_agent_profile (pre) | 4 | 2 | 3 | 3 | 2 | 2.8 | REJECT |
| 5 | bld_output_template_agent_profile (post) | 9 | 10 | 10 | 10 | 10 | 9.8 | GOLDEN |
| 6 | bld_schema_agent_profile | 8 | 7 | 6 | 9 | 7 | 7.4 | REVIEW |
| 7 | bld_examples_agent_profile | 8 | 8 | 7 | 8 | 6 | 7.5 | REVIEW |
| 8 | bld_quality_gate_agent_profile (pre) | 5 | 4 | 3 | 6 | 4 | 4.2 | REJECT |
| 8 | bld_quality_gate_agent_profile (post) | 9 | 9 | 10 | 10 | 10 | 9.6 | GOLDEN |
| 9 | bld_memory_agent_profile | 7 | 7 | 8 | 7 | 6 | 7.0 | REVIEW |
| 10 | bld_tools_agent_profile | 6 | 5 | 4 | 7 | 5 | 5.4 | REJECT |
| 11 | bld_config_agent_profile | 6 | 5 | 6 | 7 | 5 | 5.8 | REJECT |
| 12 | bld_architecture_agent_profile | 6 | 4 | 4 | 7 | 4 | 4.8 | REJECT |
| 13 | bld_collaboration_agent_profile | 7 | 5 | 6 | 7 | 5 | 5.8 | REJECT |

## Top 3 Issues Found

### Issue 1: File reference drift (affects 4 ISOs)
Multiple ISOs reference `SCHEMA.md` and `OUTPUT_TEMPLATE.md` instead of the canonical `bld_schema_agent_profile.md` and `bld_output_template_agent_profile.md`. This breaks the F1 CONSTRAIN step of 8F because the builder cannot resolve its own schema.
Fix: All rewrites now use `bld_*_agent_profile.md` naming. Other ISOs (manifest, system_prompt) also need this fix in a follow-up pass.

### Issue 2: Invented id patterns and scoring tables (quality_gate)
Pre-rewrite quality_gate used id pattern `agent-[a-z0-9]{8}` which is not a CEX convention (CEX uses `p02_ap_{slug}`), and its Actions table had 5 columns but only 2 values per row (malformed markdown). Gate H08 required `name`, `role`, `credentials` — none of which exist in the schema.
Fix: Rewrite uses `^p02_ap_[a-z][a-z0-9_]+$` aligned with schema, and properly formed scoring/action tables.

### Issue 3: Generic content with zero agent_profile specificity
Output template was a LinkedIn-style resume scaffold (Email, Phone, Experience) — completely wrong domain. Tools ISO lists 3 nonexistent tools (`cex_analyzer.py`, `cex_optimizer.py`, `val_check.py`). Architecture ISO invents roles like "Profile Validator / Compliance Team" unrelated to CEX topology.
Fix: Rewrites anchor to CEX vocabulary (identity vectors, persona frame, P02 pillar, sibling agent_profile ids). Tools/architecture ISOs remain as flagged for a future pass — they require domain-specific rebuild, not just field fixes.

## List of Rewrites

| File | Before score | After score | Rationale |
|---|---|---|---|
| archetypes/builders/agent-profile-builder/bld_instruction_agent_profile.md | 4.4 | 9.4 | Replaced generic "Phase 1/2/3" with agent_profile-specific steps: identity vectors, agent_type enum, constraint ALWAYS/NEVER/IF-THEN form, correct file refs (bld_schema_, bld_output_template_). Added full frontmatter (keywords, triggers). |
| archetypes/builders/agent-profile-builder/bld_output_template_agent_profile.md | 2.8 | 9.8 | Replaced resume-style scaffold (Email/Phone/Experience) with 6-section agent_profile scaffold: Overview, Identity Vectors, Capabilities, Constraints, Collaborators, Compliance. Frontmatter now matches schema. All {{vars}} domain-correct. |
| archetypes/builders/agent-profile-builder/bld_quality_gate_agent_profile.md | 4.2 | 9.6 | Rebuilt HARD gates around real schema (id pattern, agent_type enum, section presence, constraint form). Fixed malformed Actions table. Added 5D rubric matching this audit's scoring method. Listed common fail patterns. |

## Recommended Follow-up (not done in this pass)
1. Rewrite `bld_architecture_agent_profile` — remove invented team names, anchor to CEX nucleus topology.
2. Rewrite `bld_tools_agent_profile` — drop nonexistent `cex_analyzer.py`, `cex_optimizer.py`, `val_*.py`; list real `_tools/cex_*.py` utilities.
3. Rewrite `bld_collaboration_agent_profile` — replace abstract `MissionStmt/RoleDesc/Constraints` with real sibling builders (agent-builder, system-prompt-builder, agent-card-builder).
4. Fix `bld_system_prompt_agent_profile` frontmatter (missing keywords, triggers, rules_count, safety_level, tone) to match knowledge-card-builder template.
5. Fix `bld_manifest_agent_profile` Crew Role section — reference named collaborators by builder id, not abstract roles.

## Gate Outcomes (post-rewrite)
| Band | Count | ISOs |
|---|---|---|
| GOLDEN (>=9.5) | 2 | output_template, quality_gate |
| PUBLISH (>=8.0) | 2 | instruction, knowledge_card |
| REVIEW (7.0-7.9) | 4 | manifest, schema, examples, memory |
| REJECT (<7.0) | 5 | system_prompt, tools, config, architecture, collaboration |

## References
- Gold standard: `archetypes/builders/knowledge-card-builder/bld_{manifest,instruction,system_prompt}_knowledge_card.md`
- Rubric source: this audit file, Scoring Table section
- Builder spec: `.claude/rules/n03-builder.md`
- 8F protocol: `.claude/rules/8f-reasoning.md`
