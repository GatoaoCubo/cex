---
id: p05_qs_first_builder
kind: quickstart_guide
pillar: P05
title: "Your First CEX Builder in 30 Minutes"
version: "1.0.0"
created: "2026-04-19"
updated: "2026-04-19"
author: N04_knowledge
domain: contributor onboarding
quality: 8.7
tags: [quickstart, builder, onboarding, contributor]
tldr: "Clone, install, pick a kind, fill 13 ISOs, pass doctor, open a PR -- done in 30 minutes."
prerequisites: [Python 3.10+, git, pip]
related:
  - bld_architecture_kind
  - bld_instruction_kind
  - kind-builder
  - bld_collaboration_kind
  - bld_schema_kind
  - bld_output_template_builder
  - p03_sp_kind_builder
  - bld_tools_kind
  - p12_wf_spec_to_code
  - wave2_quality_report
density_score: 0.99
---

## Overview

This guide takes you from zero to a merged CEX builder contribution in 30 minutes.
A builder is 13 markdown files that teach the LLM pipeline how to produce one artifact kind.
You will find an unbuild kind, fill all 13 ISOs, validate, and open a PR.

---

## Prerequisites

| Item | Required Version | Install |
|------|-----------------|---------|
| Python | 3.10+ | python.org or `winget install Python.Python.3.12` |
| git | any modern | git-scm.com |
| pip | 22+ | comes with Python |

---

## Step 1 -- Fork and Clone (3 min)

Fork the repo on GitHub, then:

```bash
git clone https://github.com/<your-username>/cex.git
cd cex
git remote add upstream https://github.com/gato3/cex.git
pip install -e ".[dev]"
python _tools/cex_hooks.py install
```

**Expected outcome:** no errors. The pre-commit hook is now active.

---

## Step 2 -- Health Check (1 min)

```bash
python _tools/cex_doctor.py
```

**Expected outcome:** `0 FAIL` in the summary line. If you see FAILs on a fresh clone,
open an issue with your OS and Python version.

---

## Step 3 -- Find Your Kind (2 min)

```bash
python -c "
import json; from pathlib import Path
meta = json.loads(Path('.cex/kinds_meta.json').read_text(encoding='utf-8'))
built = {p.name.replace('-builder','') for p in Path('archetypes/builders').iterdir() if p.is_dir()}
missing = sorted(k for k in meta if k not in built)
print(f'{len(missing)} kinds without builders:')
[print(f'  {k}') for k in missing[:15]]
"
```

Pick one from the output. Good first choices from `CONTRIBUTING.md`:

| Kind | Description |
|------|-------------|
| `ab_test_config` | A/B test experiment configuration |
| `action_prompt` | Task prompt from human/orchestrator to agent |
| `agent_computer_interface` | GUI/terminal interaction protocol for agents |

Claim it: open a GitHub issue using the **New Builder** template before starting so
two contributors don't duplicate work.

---

## Step 4 -- Copy the Reference Builder (1 min)

```bash
# Replace {kind} with your chosen kind, e.g., action_prompt
cp -r archetypes/builders/agent-builder archetypes/builders/{kind}-builder
```

You now have 13 placeholder ISO files to fill.

---

## Step 5 -- Fill the 13 ISOs (20 min)

Open each file and replace the agent-specific content with content for your kind.
The 13 files and their jobs:

| File | What to write | Time |
|------|--------------|------|
| `bld_system_prompt_{kind}.md` | "You are a {kind} builder. Your role is..." | 3 min |
| `bld_instruction_{kind}.md` | Step-by-step: F1 read schema, F2 load examples, F6 produce | 4 min |
| `bld_quality_gate_{kind}.md` | 5-7 pass/fail criteria for this kind | 2 min |
| `bld_knowledge_card_{kind}.md` | What is this kind? When is it used? What fields must it have? | 3 min |
| `bld_architecture_{kind}.md` | Input -> processing -> output diagram (ASCII ok) | 2 min |
| `bld_collaboration_{kind}.md` | Which other builders consume or produce this kind? | 1 min |
| `bld_memory_{kind}.md` | What should be remembered across sessions for this kind? | 1 min |
| `bld_examples_{kind}.md` | 2-3 concrete input/output pairs | 3 min |
| `bld_schema_{kind}.md` | YAML schema for frontmatter + body fields | 2 min |
| `bld_config_{kind}.md` | Builder configuration options | 1 min |
| `bld_manifest_{kind}.md` | `id`, `kind`, `pillar`, `version`, `tags`, `tldr` | 1 min |
| `bld_output_template_{kind}.md` | Full markdown template with `{{token}}` placeholders | 3 min |
| `bld_tools_{kind}.md` | Which tools (compile, doctor, index) this builder uses | 1 min |

**Critical rules for all files:**

- Keep `quality: null` -- never self-score
- ASCII only in code blocks and technical strings
- Use snake_case for all ids and filenames
- Each file must have valid YAML frontmatter

---

## Step 6 -- Validate (2 min)

```bash
python _tools/cex_doctor.py
```

**Expected outcome:** `0 FAIL`. Common failures and fixes:

| Error | Fix |
|-------|-----|
| `missing frontmatter field: quality` | Add `quality: null` to the file's frontmatter |
| `non-ASCII in code file` | Replace emoji/accented chars with ASCII equivalents |
| `density below 0.80` | Replace prose paragraphs with tables or bullet lists |
| `missing ISO: bld_schema_{kind}.md` | You forgot to rename one of the 13 files |

---

## Step 7 -- Branch and Commit (1 min)

```bash
git checkout -b builder/{kind}
git add archetypes/builders/{kind}-builder/
git commit -m "[builder] add {kind}-builder (13 ISOs, pillar {pillar})"
git push origin builder/{kind}
```

---

## Step 8 -- Open PR (1 min)

On GitHub, open a PR from `builder/{kind}` to `main`.

- Title: `[builder] add {kind}-builder`
- Body: fill the PR template (what kind, which pillar, doctor output)
- Reference your issue: `Closes #NN`

**Expected outcome:** CI runs `cex_doctor.py`. If it passes, a maintainer reviews within 5 business days.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `pip install -e ".[dev]"` fails | Missing build tools | `pip install --upgrade pip setuptools wheel` first |
| `cex_doctor.py` shows FAIL on fresh clone | Environment issue | Check Python version (`3.10+`), re-run install |
| Pre-commit hook blocks commit | Non-ASCII in `.py` file | Run `python _tools/cex_sanitize.py --fix --scope archetypes/` |
| Doctor passes locally but CI fails | Different Python version | Check pyproject.toml for version constraint |

---

## Next Steps

- Read the full [Contributor Guide](contributor_guide_cex.md) for PR process details
- Browse [FAQ](faq_entry_cex_common_questions.md) for common questions
- Check `CONTRIBUTING.md` for Paths 2-4 (Knowledge Cards, SDK Providers, Vertical Nuclei)
- Join GitHub Discussions for architecture questions

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.41 |
| [[bld_instruction_kind]] | upstream | 0.37 |
| [[kind-builder]] | downstream | 0.37 |
| [[bld_collaboration_kind]] | downstream | 0.33 |
| [[bld_schema_kind]] | downstream | 0.32 |
| [[bld_output_template_builder]] | upstream | 0.32 |
| [[p03_sp_kind_builder]] | upstream | 0.31 |
| [[bld_tools_kind]] | upstream | 0.30 |
| [[p12_wf_spec_to_code]] | downstream | 0.26 |
| [[wave2_quality_report]] | downstream | 0.26 |
