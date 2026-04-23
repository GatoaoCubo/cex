---
id: p03_ins_learning_record
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Learning Record Builder Execution Protocol
target: learning-record-builder agent
phases_count: 4
prerequisites:
  - An experience to capture exists (completed task, failed attempt, or observed pattern)
  - The experience has a discernible outcome (success, failure, or partial)
  - Enough context is available to assess reproducibility
validation_method: checklist
domain: learning_record
quality: 9.1
tags: [instruction, learning-record, memory, P10, experience-capture]
idempotent: true
atomic: false
rollback: "Discard generated artifact; source experience is unchanged"
dependencies: []
logging: true
tldr: Capture a success or failure experience as a structured learning record with patterns, anti-patterns, impact score, and reproducibility rating.
density_score: 0.88
llm_function: REASON
related:
  - p03_sp_learning_record_builder
  - bld_knowledge_card_learning_record
  - p11_qg_learning_record
  - bld_instruction_input_schema
  - bld_collaboration_learning_record
  - bld_memory_learning_record
  - bld_instruction_action_prompt
  - p01_kc_learning_record
  - p03_ins_mental_model
  - p03_ins_law
---
## Context
The learning-record-builder produces `learning_record` artifacts (P10) — persistent, structured captures of experience that accumulate into system memory. Learning records differ from knowledge cards (atomic external facts), session state (ephemeral runtime data), and axioms (abstract truths): a learning record encodes what was tried, what happened, and what to do or avoid next time.
**Inputs:**
- `$experience_description (required) - string - "What was attempted — the task, action, or scenario"`
- `$outcome (required) - string - "What happened — success, failure, or partial result with observable evidence"`
- `$context (required) - string - "Domain, component, or workflow where this experience occurred"`
- `$patterns_observed (optional) - list[string] - "Behaviors or approaches that produced good results"`
- `$antipatterns_observed (optional) - list[string] - "Behaviors or approaches that caused problems"`
- `$score (optional) - float[0.0-10.0] - "Objective impact score; 0.0-10.0 scale"`
**Output:** A single `learning_record` artifact, max 3KB, density >= 0.80, with 15 required + 7 extended frontmatter fields and body sections covering summary, pattern, anti-pattern, context, impact, and reproducibility.
**Boundary check before proceeding:**
- Content is a factual external reference (API spec, research finding) → route to knowledge-card-builder
- Content is transient runtime state → do not persist, discard
- Content is experiential and worth retaining across sessions → proceed
## Phases
### Phase 1: Analyze
**Action:** Parse the raw experience into classified, structured components.
1. Identify the **task or scenario**: what was attempted, not just what happened.
2. Classify `outcome` as exactly one of: `SUCCESS`, `PARTIAL`, `FAILURE`.
3. Extract **evidence**: the concrete observable signal that defines the outcome (error message, metric delta, test result, human judgment). Evidence must be observable, not interpretive.
4. Assign `score` 0.0–10.0 based on objective impact:
   - 9.0–10.0: prevents critical system failure or major data loss
   - 7.0–8.9: improves significant workflows, substantial time saved
   - 5.0–6.9: useful optimization, limited scope
   - 0.0–4.9: minor note, narrow applicability
5. Identify `patterns`: concrete reproducible steps that led to success.
6. Identify `anti_patterns`: specific failures with observable symptoms.
7. Check for existing learning records covering the same experience to avoid duplicates.
8. Determine `reproducibility`: `HIGH` (same inputs reliably produce same outcome), `MEDIUM` (likely but context-dependent), `LOW` (situational, unlikely to recur identically).
**Verification:** Complete this sentence: "[Actor] attempted [action] in [context] and observed [outcome evidence] resulting in score [N]."
### Phase 2: Compose
**Action:** Write all frontmatter fields and body sections within the 3KB size limit.
1. Read `SCHEMA.md` — source of truth for all 15 required + 7 extended fields.
2. Read `OUTPUT_TEMPLATE.md` — fill every `{{var}}` following SCHEMA constraints.
3. Fill frontmatter: all 15 required + 7 extended fields (`null` is valid for optional extended fields).
4. Set `quality`: literal `null` — never a number.
5. Set `outcome`: one of `SUCCESS`, `PARTIAL`, `FAILURE` (uppercase).
6. Set `score`: float 0.0–10.0.
7. Write `## Summary` — dense 2-3 sentence overview of the full experience and outcome.
8. Write `## Pattern` — concrete reproducible steps that worked; each step is actionable ("do X").
9. Write `## Anti-Pattern` — specific failures with observable symptoms; each states the failure mode ("avoid X because it causes Y").
10. Write `## Context` — environment, agent_group/agent, timing, constraints that bound this experience.
11. Write `## Impact` — measurable outcomes: time saved/lost, error rates, score deltas.
12. Write `## Reproducibility` — conditions that must hold for reproduction, confidence level, caveats.
Density check pseudocode:
```
useful_items = count(pattern_steps) + count(antipattern_steps)
total_sentences = count_sentences(body)
density = useful_items / total_sentences
# if density < 0.80: remove filler sentences, consolidate redundant items
```
**Verification:** Every pattern step says what to do. Every anti-pattern step states the failure mode it causes. Total artifact <= 3KB.
### Phase 3: Validate
**Action:** Run all HARD gates from `QUALITY_GATES.md`. Fix any failure before output.
| Gate | Check |
|------|-------|
| H01 | YAML frontmatter parses without error |
| H02 | `id` matches expected pattern for learning_record |
| H03 | `kind` is literal string `learning_record` |
| H04 | `quality` is `null` |
| H05 | All 15 required fields present and non-empty |
| H06 | `outcome` is one of: SUCCESS, PARTIAL, FAILURE |
| H07 | `score` is a float in range 0.0–10.0 |
| H08 | Artifact body is <= 3KB |
| H09 | `## Pattern` contains at least one actionable step |
Score SOFT gates from `QUALITY_GATES.md`. If soft score < 8.0, revise in the same pass.
**Cross-check:** Is every pattern concrete (not vague advice)? Is every anti-pattern specific with a named failure mode?
### Phase 4: Output


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_learning_record_builder]] | related | 0.42 |
| [[bld_knowledge_card_learning_record]] | downstream | 0.34 |
| [[p11_qg_learning_record]] | downstream | 0.32 |
| [[bld_instruction_input_schema]] | sibling | 0.30 |
| [[bld_collaboration_learning_record]] | downstream | 0.30 |
| [[bld_memory_learning_record]] | downstream | 0.29 |
| [[bld_instruction_action_prompt]] | sibling | 0.28 |
| [[p01_kc_learning_record]] | downstream | 0.28 |
| [[p03_ins_mental_model]] | sibling | 0.27 |
| [[p03_ins_law]] | sibling | 0.26 |
