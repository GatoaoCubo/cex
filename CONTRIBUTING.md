# Contributing to CEX

CEX follows the Shokunin standard: quality over speed, density over volume.
Every contribution must pass `cex_doctor` before merging.

---

## Prerequisites

- Python 3.10+
- Git with pre-commit hooks: `cd _tools && python setup_hooks.py`
- Read `archetypes/CODEX.md` (DNA, naming, density rules)
- Read `archetypes/MANDAMENTOS.md` (10 immutable laws)

---

## How to Add a Builder

Builders live in `archetypes/builders/` and consist of 13 ISO files.

### Step 1: Create Directory

```
archetypes/builders/{kind}-builder/
```

### Step 2: Create 13 Files

| # | File | Purpose |
|---|------|---------|
| 1 | `bld_system_prompt_{kind}.md` | Identity, role, constraints |
| 2 | `bld_instruction_{kind}.md` | Step-by-step execution protocol |
| 3 | `bld_quality_gate_{kind}.md` | Pass/fail criteria, density thresholds |
| 4 | `bld_knowledge_card_{kind}.md` | Domain knowledge (max 4KB) |
| 5 | `bld_architecture_{kind}.md` | Component map, data flow |
| 6 | `bld_collaboration_{kind}.md` | Inter-builder dependencies |
| 7 | `bld_memory_{kind}.md` | Learning record schema |
| 8 | `bld_examples_{kind}.md` | Input/output examples |
| 9 | `bld_schema_{kind}.md` | Input/output JSON/YAML schema |
| 10 | `bld_config_{kind}.md` | Builder configuration |
| 11 | `bld_manifest_{kind}.md` | Metadata: version, pillar, kind, tags |
| 12 | `bld_output_template_{kind}.md` | Output format template |
| 13 | `bld_tools_{kind}.md` | Available tools and integrations |

### Step 3: Validate

```bash
python _tools/cex_doctor.py
```

All checks must PASS: naming, density, 13-file completeness, frontmatter, size, schema compliance.

### Step 4: Submit PR

Title format: `archetype: {kind}-builder -- 13 ISO (P{NN})`

---

## How to Add a Template

Templates live in `P{NN}_{name}/templates/`.

1. Choose the correct pillar directory (`P01-P12`)
2. Name: `tpl_{kind}.md` (lowercase, snake_case, ASCII)
3. Include all required frontmatter fields (see Code Style below)
4. Density >= 0.80 mandatory
5. Add compiled counterpart in `compiled/` (`.yaml` or `.json`)
6. Run `python _tools/validate_schema.py` -- must PASS

---

## How to Add a New Kind

1. Open `P{NN}_{name}/_schema.yaml` — add kind under `types:`
2. Update `.cex/kinds_meta.json` — add kind entry
3. Update `archetypes/TYPE_TO_TEMPLATE.yaml` — map kind to template
4. Update `OBJECT_TO_KINDS` in `_tools/cex_8f_motor.py` — add lookup entry
5. Create template in `P{NN}/templates/tpl_{kind}.md`
6. Create builder: `archetypes/builders/{kind}-builder/` (13 ISOs)
7. Create kind KC: `P01_knowledge/library/kind/kc_{kind}.md`
8. Add at least 1 example in `P{NN}/examples/` meeting density >= 0.80
9. Run `python _tools/cex_doctor.py` -- must PASS

---

## Code Style

### Naming Convention

```
{layer}_{kind}_{topic}.{ext}

Rules:
- lowercase only
- snake_case (underscores, no hyphens in filenames)
- ASCII only (no accented chars)
- max 50 characters
- id in frontmatter == filename stem
```

### Density Rules

```
density = useful_tokens / total_tokens
```

| Tier | Score | Action |
|------|-------|--------|
| Elite | >= 0.90 | Golden candidate |
| High | 0.80-0.89 | Accept |
| Standard | 0.70-0.79 | Revise before merge |
| Low | < 0.70 | Reject -- rewrite required |

### Required Frontmatter

```yaml
---
id: p01_kc_topic_name
kind: knowledge_card
pillar: P01
title: "Descriptive title"
version: "1.0.0"
created: "2026-01-01"
updated: "2026-01-01"
author: "builder_agent"
domain: "topic_domain"
quality: null
tags: [tag1, tag2, tag3]
tldr: "One-line summary under 80 chars"
density_score: 0.88
---
```

### Body Rules

- Prose > 3 lines: PROHIBITED -- convert to bullets
- Max per-kind byte limits (see `_schema.yaml`)
- Headers must have content (no empty sections)
- Tables preferred over prose for structured data
- Dual output: every `.md` needs a `compiled/` counterpart

---

## Quality Gate

| Criteria | Threshold |
|----------|-----------|
| `cex_doctor` | 0 FAIL |
| Density score | >= 0.80 |
| Quality score | >= 8.0 (published), >= 7.0 (experimental) |
| Naming | v2.0 compliant |
| Frontmatter | All required fields present |
| Dual output | `.md` + compiled counterpart |

---

## Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| Prose paragraph > 3 lines | Convert to bullet list |
| Missing `density_score` | Estimate and declare |
| Filename with uppercase/hyphens | Rename: lowercase snake_case |
| `id` != filename stem | Fix `id` to match filename |
| File exceeds `max_bytes` | Compress or split |
| keywords < 3 | Add domain-specific retrieval keywords |
| No compiled counterpart | Run `cex_compile.py` |
| Builder with < 13 files | Complete all 13 ISO files |

---

*CEX CONTRIBUTING v3.0 | 2026-03-30 | Quality: Shokunin*
