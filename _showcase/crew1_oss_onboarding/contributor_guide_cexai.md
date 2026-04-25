---
id: p05_cg_cexai_showcase
kind: contributor_guide
pillar: P05
title: "Contributing to CEXAI"
version: "1.0.0"
created: "2026-04-22"
updated: "2026-04-22"
author: contributor-guide-builder
domain: contributor guide
quality: 9.1
tags: [contributor_guide, cexai, oss, builders, kinds, 8f]
tldr: "CEXAI contributor guide: setup, 4 paths, 8F gates, PR process, DCO."
contribution_types: [builder, knowledge_card, sdk_provider, vertical_nucleus]
onboarding_steps: [fork, clone, pip_install_dev, install_hooks, doctor, pick_path, pr]
review_process: "1 maintainer approval; initial feedback within 7 business days"
related:
  - bld_architecture_kind
  - kind-builder
  - bld_instruction_kind
  - bld_eval_contributor_guide
  - bld_output_template_contributor_guide
  - p03_sp_kind_builder
  - ctx_cex_new_dev_guide
  - p11_qg_knowledge
  - bld_memory_contributor_guide
  - p05_cg_cex
density_score: 1.0
---

# Contributing to CEXAI

CEXAI: open-source typed knowledge system, 300 kinds, 301 builders, 8 nuclei, 12 pillars, 8F pipeline. This guide covers four contribution paths, quality gates, and PR process.

---

## Getting Started

Requirements: Python 3.10+, git 2.38+.

```bash
git clone https://github.com/<you>/cex.git && cd cex
git remote add upstream https://github.com/GatoaoCubo/cex.git
python -m venv .venv && source .venv/bin/activate && pip install -e ".[dev]"
python _tools/cex_hooks.py install && python _tools/cex_doctor.py
```

---

## Contribution Workflow

Sync -> branch (`feat/<name>`) -> build -> doctor (0 FAIL) -> score (>= 0.80) -> commit -> PR against `main`. Fill `.github/pull_request_template.md` completely.

---

## The Four Paths

### Path 1: Builder (recommended)

12 ISO files, one per pillar (P01-P12). Unoverridden files inherit from `archetypes/builders/_shared/`.

```bash
# Find unbuilt kinds
python -c "import json;from pathlib import Path;meta=json.loads(Path('.cex/kinds_meta.json').read_text(encoding='utf-8'));built={p.name.replace('-builder','') for p in Path('archetypes/builders').iterdir() if p.is_dir()};[print(k) for k in sorted(meta) if k not in built]"
# Bootstrap
cp -r archetypes/builders/knowledge_card-builder archetypes/builders/{kind}-builder
```

**5 required overrides (rest inherit _shared defaults):**

| File | Pillar | Purpose |
|------|--------|---------|
| `bld_knowledge_{kind}.md` | P01 | Domain expertise (F3 INJECT) |
| `bld_model_{kind}.md` | P02 | Identity + persona |
| `bld_prompt_{kind}.md` | P03 | Step-by-step execution |
| `bld_output_{kind}.md` | P05 | Output template (F6 PRODUCE) |
| `bld_eval_{kind}.md` | P07 | HARD gates + scoring (F7) |

### Path 2: Knowledge Card

File: `N00_genesis/P01_knowledge/library/kind/kc_{kind}.md`. Frontmatter: `kind: knowledge_card`, `pillar: P01`, `quality: null`. Density >= 0.80. Max 4 KB.

### Path 3: SDK Provider

Implement `ProviderBase` in `cex_sdk/providers/`. Add routing to `.cex/config/nucleus_models.yaml` under `fallback_chain:`. Verify: `python _tools/cex_showoff.py --wave 1` (6 nuclei, 0 crashes).

### Path 4: Vertical Nucleus

5 required files: `rules/n{xx}-{domain}.md` (identity + sin lens), `P02_model/nucleus_def_n{xx}.md`, `P01_knowledge/kc_{domain}_vocabulary.md`, `P08_architecture/agent_card_n{xx}.md`, `P08_architecture/component_map_n{xx}.md`. All 12 pillar dirs required. Choose sin lens from `N0{1-7}_*/P08_architecture/nucleus_def_n0*.md` examples. Verify: `python _tools/cex_sanitize.py --check --scope N{XX}_{domain}/`

---

## Quality Gates and Coding Standards

| Gate | Threshold | Command |
|------|-----------|---------|
| Doctor | 0 FAIL | `python _tools/cex_doctor.py` |
| Density | >= 0.80 | `python _tools/cex_score.py {file}` |
| Quality field | `null` | never self-score |
| ASCII in code | 0 violations | `python _tools/cex_sanitize.py --check` |
| Naming | snake_case, ASCII, <= 50 chars | pre-commit (auto) |
| 8F F1 | frontmatter valid | `kind`, `pillar`, `id` match schema |
| 8F F7 | bld_eval present | HARD gates with pass conditions |
| 8F F8 | compiled YAML | `.yaml` present in `compiled/` |

ASCII-only in `.py`, `.ps1`, `.sh` (pre-commit enforced). Replacements: `[OK]` `->` `--`. Fix: `python _tools/cex_sanitize.py --fix --scope _tools/`.

---

## Commit Messages

Format: `[{scope}] {action}: {description}`. Scopes: `[builder]` `[knowledge]` `[nucleus]` `[sdk]` `[fix]`. Example: `[builder] add changelog-builder (12 ISOs, pillar P01)`

---

## Pull Request Process and Review

1. `python _tools/cex_doctor.py` (0 FAIL) + `python _tools/cex_score.py {file}` (>= 0.80)
2. Fill PR template; reference `Relates to #N`; request maintainer review
3. Respond to feedback within **5 business days**

Merge: squash after 1 maintainer approval. Initial review within **7 business days**.

| Check | Criterion |
|-------|-----------|
| Schema | Frontmatter matches `bld_schema_{kind}.md` |
| Density | Tables > prose; no block > 3 lines |
| Cross-refs | `related:` >= 3 entries |
| ASCII | 0 non-ASCII in code files |
| Quality | `null` -- self-scored PRs returned |


---

## DCO (Developer Certificate of Origin)

CEXAI uses DCO. Sign every commit with `git commit -s`. This adds `Signed-off-by: Name <email>`. Full text: https://developercertificate.org/

---

## Anti-Patterns

- `quality: 9.0` in frontmatter -- self-scoring, PR returned
- Fewer than 5 builder ISOs -- not merged
- Non-ASCII in code files -- crashes Windows, pre-commit blocks
- PR before `cex_doctor` passes -- returned without review
- Secrets or `.env` in any file -- immediate reject

---

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.49 |
| [[kind-builder]] | downstream | 0.42 |
| [[bld_instruction_kind]] | upstream | 0.42 |
| [[bld_eval_contributor_guide]] | sibling | 0.40 |
| [[bld_output_template_contributor_guide]] | upstream | 0.38 |
| [[p03_sp_kind_builder]] | upstream | 0.35 |
| [[bld_memory_contributor_guide]] | sibling | 0.33 |
| [[ctx_cex_new_dev_guide]] | related | 0.30 |
| [[p11_qg_knowledge]] | downstream | 0.28 |
| [[p05_cg_cex]] | sibling | 0.27 |
