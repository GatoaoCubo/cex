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

Builders live in `archetypes/` and consist of 13 ISO files.

### Step 1: Create Directory

```
archetypes/{kind}-builder/
```

### Step 2: Create 13 Files

| # | File | Purpose |
|---|------|---------|
| 1 | `SYSTEM_PROMPT.md` | Identity, role, constraints |
| 2 | `INSTRUCTIONS.md` | Step-by-step execution protocol |
| 3 | `QUALITY_GATES.md` | Pass/fail criteria, density thresholds |
| 4 | `KNOWLEDGE.md` | Domain knowledge (max 4KB) |
| 5 | `ARCHITECTURE.md` | Component map, data flow |
| 6 | `COLLABORATION.md` | Inter-builder dependencies |
| 7 | `MEMORY.md` | Learning record schema |
| 8 | `FEW_SHOT_1.md` | Input/output example 1 |
| 9 | `FEW_SHOT_2.md` | Input/output example 2 |
| 10 | `FEW_SHOT_3.md` | Input/output example 3 |
| 11 | `SCHEMA.yaml` | Input/output JSON/YAML schema |
| 12 | `VALIDATION.md` | Self-check checklist |
| 13 | `MANIFEST.yaml` | Metadata: version, pillar, kind, tags |

### Step 3: Validate

```bash
python _tools/cex_doctor.py archetypes/{kind}-builder/
```

All 7 checks must PASS: naming, density, 13-file completeness, frontmatter, size, schema compliance, cross-references.

### Step 4: Submit PR

Title format: `archetype: {kind}-builder -- 13 ISO (P{NN}, Wave {N})`

---

## How to Add a Template

Templates live in `P{NN}_{name}/templates/`.

1. Choose the correct pillar directory (`P01-P12`)
2. Name: `{lp}_{type}_{topic}_template.md` (lowercase, snake_case, ASCII, max 50 chars)
3. Include all required frontmatter fields (see Code Style below)
4. Density >= 0.80 mandatory
5. Derive from `archetypes/META_TEMPLATE.md` for consistency
6. Add compiled counterpart in `compiled/` (`.yaml` or `.json` per `machine_format`)
7. Run `python _tools/validate_schema.py` -- must PASS

---

## How to Add a New LP Type

1. Open `P{NN}_{name}/_schema.yaml`
2. Add type under `types:` with required fields:
   ```yaml
   - name: your_type
     description: one-line description
     frontmatter_required: [id, type, lp, quality, tags, tldr, keywords, long_tails, bullets, axioms]
     constraints:
       max_bytes: 4096
       quality_min: 7.0
       density_min: 0.80
   ```
3. Update generator (`_generator.md`) with new section for the type
4. Add at least 1 example in `examples/` meeting density >= 0.80
5. Run `python _tools/validate_schema.py` -- must PASS

---

## How to Migrate an Artifact

1. Check `archetypes/MIGRATION_MAP.md` for LP bucket
2. Identify target: KC > P01, Agent > P02, Prompt > P03, Tool > P04, Workflow > P12
3. Strip prose > 3 lines -- convert to bullets
4. Add YAML frontmatter (all required fields)
5. Ensure density >= 0.80 (compress if needed)
6. Add compiled counterpart
7. Run validators, fix errors, submit

---

## Code Style

### Naming Convention

```
{lp}_{type}_{topic}.md

Rules:
- lowercase only
- snake_case (underscores, no hyphens)
- ASCII only (no accented chars in filename)
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
kind: domain_kc
pillar: P01
quality: 8.5
tags: [tag1, tag2, tag3]
tldr: "One-line summary under 80 chars"
keywords: [keyword1, keyword2, keyword3]
long_tails:
  - "Question this artifact answers?"
bullets:
  - "Key fact 1 (max 80 chars)"
  - "Key fact 2"
  - "Key fact 3"
axioms:
  - "Immutable truth this artifact encodes"
density_score: 0.88
---
```

### Body Rules

- Prose > 3 lines: PROHIBITED -- convert to bullets
- Max 4KB per file
- Headers must have content (no empty sections)
- Tables preferred over prose for structured data
- Dual output: every `.md` needs a `compiled/` counterpart

---

## Review Process

### Automated Checks (pre-commit)

```bash
python _tools/cex_doctor.py [path]        # 7-check suite
python _tools/validate_schema.py           # Schema compliance
python _tools/validate_generators.py       # Generator coverage
python _tools/validate_examples.py         # Density + frontmatter
```

All validators must PASS. Failures are blocking.

### Quality Gate

| Criteria | Threshold |
|----------|-----------|
| `cex_doctor` | 7/7 checks PASS |
| Density score | >= 0.80 |
| Quality score | >= 8.0 |
| File size | <= 4KB |
| Naming | v2.0 compliant |
| Frontmatter | All required fields present |
| Dual output | `.md` + compiled counterpart |

### PR Checklist

- [ ] Artifact in correct directory (`P01-P12/` or `archetypes/`)
- [ ] Filename follows naming v2.0 (`{lp}_{type}_{topic}.md`)
- [ ] YAML frontmatter complete (all required fields)
- [ ] `density_score` >= 0.80 declared and accurate
- [ ] `quality` >= 8.0 declared
- [ ] File size <= 4KB
- [ ] No prose blocks > 3 lines
- [ ] Compiled counterpart exists
- [ ] `python _tools/cex_doctor.py` -- PASS
- [ ] `python _tools/validate_schema.py` -- PASS
- [ ] PR title: `{LP}[{type}]: brief description`

---

## Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| Prose paragraph > 3 lines | Convert to bullet list |
| Missing `density_score` | Estimate and declare |
| Filename with uppercase/hyphens | Rename: lowercase snake_case |
| `id` != filename stem | Fix `id` to match filename |
| File > 4KB | Compress or split into 2 artifacts |
| keywords < 3 | Add domain-specific retrieval keywords |
| No compiled counterpart | Run `cex_compile.py` |
| Builder with < 13 files | Complete all 13 ISO files |
| Generic tldr | Make specific: include LP, type, topic |

---

*CEX CONTRIBUTING v2.0 | 2026-03-27 | Quality: Shokunin*
