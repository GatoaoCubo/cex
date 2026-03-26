# Contributing to CEX

CEX follows the Shokunin standard: quality over speed, density over volume.
Every contribution must pass the quality gate before merging.

---

## Quick Start

1. Read `archetypes/CODEX.md` (DNA, naming, density rules)
2. Read `archetypes/MANDAMENTOS.md` (10 immutable laws)
3. Choose your LP, read its `_generator.md`
4. Fill a template, validate, submit

---

## How to Add a New LP Type

When adding a new artifact type not yet in a `_schema.yaml`:

1. Open the relevant `P{NN}_{name}/_schema.yaml`
2. Add the new type under `types:` with at minimum:
   ```yaml
   - name: your_type
     description: one-line description
     frontmatter_required: [id, type, lp, quality, tags, tldr, keywords, long_tails, bullets, axioms]
     constraints:
       max_bytes: 4096
       quality_min: 7.0
       density_min: 0.80
   ```
3. Update the generator (`_generator.md`) with a new section for the type
4. Add at least 1 example in `examples/` meeting density >= 0.80
5. Run `python _tools/validate_schema.py` — must PASS

---

## How to Create a Generator for an Existing Type

If a type exists in `_schema.yaml` but has no generator coverage:

1. Read the `_generator.md` of the LP — understand the existing pattern
2. Add a new section `## Type: {type_name}` with:
   - Step-by-step authoring (numbered list)
   - At least 3 anti-patterns with correction
   - Density checklist
3. Run `python _tools/validate_generators.py` — must PASS

---

## How to Migrate an Artifact from Another Framework

For migrating existing artifacts (e.g., from codexa-core, LangChain, etc.):

1. Check `archetypes/MIGRATION_MAP.md` — find the LP bucket for your artifact type
2. Identify the target LP and type:
   - Knowledge document → P01 (domain_kc or meta_kc)
   - Agent definition → P02 (agent)
   - System prompt / HOP → P03 (prompt_template or action_prompt)
   - Skill / tool → P04 (skill or mcp_server)
   - Workflow → P12 (workflow)
3. Strip all prose > 3 lines — convert to bullets
4. Add YAML frontmatter (all required fields)
5. Calculate density estimate (useful tokens / total tokens)
6. If density < 0.80: compress, remove filler, add tables
7. Run validators, fix all errors, then submit

---

## Quality Standards

### Density Score

```
density = useful_tokens / total_tokens
```

| Tier | Score | Action |
|------|-------|--------|
| Elite | >= 0.90 | Golden candidate — add to GOLDEN_CANDIDATES.md |
| High | 0.80-0.89 | Accept — meets standard |
| Standard | 0.70-0.79 | Revise before merge |
| Low | < 0.70 | Reject — rewrite required |

### Naming Convention

```
{lp}_{type}_{topic}.md

Rules:
- lowercase only
- snake_case (underscores, no hyphens)
- ASCII only (no accented chars in filename)
- max 50 characters
- id in frontmatter == filename stem

Examples:
  p01_kc_ecommerce_br.md
  p02_agent_gateway.md
  p03_pt_action_prompt.md
  p04_skill_ml_ads.md
```

### Required Frontmatter

Every artifact must include:

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
  - "Another retrieval question?"
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

- Prosa > 3 linhas: PROIBIDO — convert to bullets
- Max 4KB per file
- Headers must have content (no empty sections)
- Tables preferred over prose for structured data
- ASCII diagrams preferred over descriptions for architecture

---

## PR Checklist

Before submitting a PR, confirm all items:

- [ ] Read `archetypes/CODEX.md` and `archetypes/MANDAMENTOS.md`
- [ ] Artifact placed in correct LP directory (`P01-P12/`)
- [ ] Filename follows naming convention (`{lp}_{type}_{topic}.md`)
- [ ] YAML frontmatter complete (all required fields present)
- [ ] `density_score` declared in frontmatter (accurate estimate)
- [ ] Density >= 0.80 (run `_tools/validate_examples.py` to check)
- [ ] Quality >= 7.0 declared in frontmatter
- [ ] File size <= 4KB
- [ ] No prose blocks > 3 lines
- [ ] `python _tools/validate_schema.py` — PASS
- [ ] `python _tools/validate_examples.py` — PASS
- [ ] Dual output: both `.md` and `.yaml` present (if applicable)
- [ ] PR title: `{LP}[{type}]: brief description` (e.g., `P01[kc]: ecommerce BR catalog`)

---

## Validators

```bash
# Validate all schemas
python _tools/validate_schema.py

# Validate generators (coverage check)
python _tools/validate_generators.py

# Validate examples (density + frontmatter)
python _tools/validate_examples.py
```

All validators must pass before merge. Failures are blocking.

---

## Anti-Patterns (Common Mistakes)

| Anti-Pattern | Fix |
|-------------|-----|
| Prose paragraph > 3 lines | Convert to bullet list |
| Missing `density_score` in frontmatter | Estimate and declare |
| Filename with uppercase or hyphens | Rename: lowercase snake_case |
| `id` != filename stem | Fix `id` to match filename |
| "TBD" or empty fields in frontmatter | Fill or remove the field |
| File > 4KB | Compress: remove filler, split into 2 artifacts |
| keywords < 3 | Add domain-specific retrieval keywords |
| No `axioms` | Distill 1 immutable truth from the artifact |
| Generic tldr | Make specific: include LP, type, topic |

---

*CEX CONTRIBUTING v1.0 | 2026-03-22 | Quality: Shokunin*
