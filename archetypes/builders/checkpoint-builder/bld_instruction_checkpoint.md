---
kind: instruction
id: bld_instruction_checkpoint
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for checkpoint
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Checkpoint"
version: "1.0.0"
author: n03_builder
tags: [checkpoint, builder, examples]
tldr: "Golden and anti-examples for checkpoint construction, demonstrating ideal structure and common pitfalls."
domain: "checkpoint construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce a checkpoint
## Phase 1: RESEARCH
1. Identify the workflow artifact (workflow_ref) this checkpoint belongs to
2. Identify the step name — the exact named step in the workflow where state is captured
3. List all state keys needed to resume from this step (minimize to resumption-critical only)
4. Determine TTL based on workflow duration: 1h (interactive), 24h (batch), 7d (multi-day), 30d (compliance)
5. Check for existing checkpoints in the same workflow to set parent_checkpoint correctly
6. Determine if the checkpoint is resumable (most are; terminal checkpoints may not be)
7. Document prerequisites for resume: external services, auth tokens, idempotency guarantees
8. Confirm step slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write ## Overview: 1-2 sentences — which workflow, which step, why this checkpoint matters
5. Write ## State: table of state keys with type, size hint, and description
   - Include only resumption-critical keys (not derived or recomputable values)
   - Declare serialization format: yaml or json
   - State total byte budget
6. Write ## Resume: numbered steps to re-enter workflow from this checkpoint
   - List prerequisites (external dependencies, auth, resource availability)
   - Name the exact re-entry point (step name)
   - Declare idempotency: yes/no with reason
7. Write ## Lifecycle: TTL value + justification, cleanup policy, archival path, chain linkage
8. Verify body <= 2048 bytes
9. Verify id matches `^p12_ck_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p12_ck_` prefix
4. Confirm kind == checkpoint
5. Confirm workflow_ref and step are non-empty strings
6. Confirm tags includes "checkpoint" and has >= 3 items
7. Confirm body has all 4 sections: Overview, State, Resume, Lifecycle
8. HARD gates: frontmatter valid, id pattern matches, workflow_ref present, step present, quality null
9. SOFT gates: score against QUALITY_GATES.md
10. Cross-check: is this a checkpoint (state + workflow_ref) and not a signal (no state), session_state (no workflow_ref), or the workflow definition itself?
11. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify checkpoint
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | checkpoint construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
