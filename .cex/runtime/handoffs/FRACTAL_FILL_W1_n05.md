---
mission: FRACTAL_FILL_W1
nucleus: n05
wave: W1_FOUNDATIONS
created: 2026-04-16
model: gpt-5-codex
pillars: [P06, P09]
artifact_count: 8
---

# N05 -- Wave 1 FOUNDATIONS (8 artifacts: schemas + config)

## Mission

You are N05_operations (Gating Wrath sin lens). Fill the P06 (schemas) and P09 (config)
pillars of your nucleus by producing 8 artifacts following the CEX 8F
pipeline and ASCII-only rule (see .claude/rules/8f-reasoning.md and
.claude/rules/ascii-code-rule.md).

## Context (READ THESE FIRST)

1. `N05_operations/architecture/nucleus_def_n05.md` -- your identity + sin lens
2. `N05_operations/rules/` -- your nucleus rules
3. `archetypes/builders/{kind}-builder/bld_manifest_{kind}.md` -- per-kind builder
4. `P01_knowledge/library/kind/kc_{kind}.md` -- kind knowledge cards (when present)
5. `P06_schema/_schema.yaml`, `P09_config/_schema.yaml` -- pillar schemas
6. Similar artifacts in other nuclei: `N0*/schemas/`, `N0*/config/` (read 2-3 as examples)

## Deliverables (exact paths)

### P06 (schemas) -- 2 artifacts

1. `N05_operations/schemas/sch_enum_def_n05.md` -- kind=`enum_def` -- Enumeracao reutilizavel
2. `N05_operations/schemas/sch_type_def_n05.md` -- kind=`type_def` -- Custom type definition

### P09 (config) -- 6 artifacts

3. `N05_operations/config/con_env_config_n05.md` -- kind=`env_config` -- Environment variables
4. `N05_operations/config/con_feature_flag_n05.md` -- kind=`feature_flag` -- Feature flag (on/off, gradual rollout)
5. `N05_operations/config/con_path_config_n05.md` -- kind=`path_config` -- System paths
6. `N05_operations/config/con_permission_n05.md` -- kind=`permission` -- Permission rule (read/write/execute)
7. `N05_operations/config/con_rate_limit_config_n05.md` -- kind=`rate_limit_config` -- Rate limiting: RPM, TPM, budget
8. `N05_operations/config/con_secret_config_n05.md` -- kind=`secret_config` -- Secret management

## Format (every file)

```yaml
---
id: {subdir_prefix}_{kind}_n05
kind: {kind}
pillar: {pillar}
nucleus: n05
title: <short Title Case>
version: 1.0
quality: null   # NEVER self-score
tags: [<3-5 tags>]
---
```

Body: structured markdown (tables > prose). Minimum 80 lines. Density >= 0.85.
MUST include: Purpose, Schema (if P06) or Values (if P09), Rationale, Example,
and a Properties table. Apply the **Gating Wrath** lens to every design choice.

## 8F trace (show evidence at the top of each file as HTML comment)

```html
<!-- 8F: F1 constrain=<pillar/kind> F2 become=<builder> F3 inject=<refs>
     F4 reason=<approach> F5 call=<tools> F6 produce=<N bytes>
     F7 govern=<self-check> F8 collaborate=<save path> -->
```

## ASCII rule (MANDATORY)

- Markdown files: ASCII + basic Unicode punctuation OK.
- NEVER use emoji in code blocks or structured fields.
- Portuguese: use unaccented forms in identifiers (missao, acao, visao).

## On completion

1. Save all files.
2. Print: `=== COMPLETE === nucleus={nuc} wave=W1 count={total} ===`
3. DO NOT commit (N07 commits after verifying deliverables).
4. Exit cleanly.

## Anti-patterns (BLOCKED)

- Skipping frontmatter.
- Self-scoring quality (must be `null`).
- Generic boilerplate without sin lens.
- Non-ASCII in identifiers.
- Fewer deliverables than listed.
