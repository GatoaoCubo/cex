---
id: showcase_quickstart_guide_cexai
kind: quickstart_guide
pillar: P05
title: "CEXAI: Build Your First Artifact in 5 Minutes"
version: "1.0.0"
created: "2026-04-22"
updated: "2026-04-22"
author: quickstart-guide-builder
domain: open-source onboarding
quality: 8.8
tags: [quickstart, cexai, onboarding, 8f-pipeline, first-artifact]
tldr: "Clone the repo, run setup, issue one /build command, and receive a validated knowledge artifact in under 5 minutes."
prerequisites: [Python 3.12+, git 2.40+, Claude Code 2.x or Anthropic API key]
audience: developer who just cloned the CEXAI repo
tools: [cex_setup_validator.py, cex_doctor.py, cex_8f_runner.py, cex_compile.py]
related:
  - p05_qs_first_builder
  - bld_instruction_kind
  - p01_kc_8f_pipeline
  - bld_architecture_kind
  - bld_schema_kind
  - bld_collaboration_kind
  - p03_sp_builder_nucleus
  - bld_output_template_builder
  - p12_wf_spec_to_code
  - p03_sp_kind_builder
density_score: 1.0
---

## Overview

CEXAI is a typed knowledge system for LLM agents: 300 artifact kinds, 301 builders,
12 pillars, and an 8-function pipeline (8F) that converts a natural-language intent
into a validated, structured markdown artifact. This guide gets you to your first
artifact in 5 minutes using only the CLI -- no framework knowledge required upfront.

---

## Prerequisites

| Item | Min Version | Obtain |
|------|-------------|--------|
| Python | 3.12+ | python.org or `winget install Python.Python.3.12` |
| git | 2.40+ | git-scm.com |
| pip | 22+ | bundled with Python |
| LLM provider | any one | Anthropic API key OR Ollama running locally |

**Provider setup (pick one):**

| Provider | Env var | Notes |
|----------|---------|-------|
| Anthropic (Claude) | `ANTHROPIC_API_KEY` | Recommended for full 8F quality |
| Ollama (local) | none | Run `ollama pull llama3.1:8b` first |
| OpenAI | `OPENAI_API_KEY` | Works with cex_router_v2 fallback chain |

---

## Step 1 -- Clone and Install (2 min)

```bash
git clone https://github.com/GatoaoCubo/cex.git
cd cex
pip install -r requirements.txt
pip install -e .
python _tools/cex_hooks.py install
```

**Expected outcome:** the last line prints `[OK] pre-commit hook installed`.

---

## Step 2 -- Validate Your Setup (1 min)

```bash
python _tools/cex_setup_validator.py
```

All checks should show `[OK]`. The validator covers:

| Category | What it checks |
|----------|----------------|
| RUNTIME | Python >= 3.12, git >= 2.40, Node >= 18 |
| PACKAGES | pyyaml, tiktoken, numpy, scikit-learn |
| GIT_HOOKS | pre-commit hook installed |
| SYSTEM | disk space, ASCII compliance in _tools/ |

If any check shows `[FAIL]`: run `python _tools/cex_setup_validator.py --fix` for
auto-remediation, or see the Troubleshooting section below.

---

## Step 3 -- Build Your First Artifact (1 min)

**Option A -- Claude Code (interactive, recommended)**

Open a terminal at the repo root and start Claude Code. Then type:

```
/build create a knowledge card about the 8F pipeline
```

The 8F pipeline resolves: `kind=knowledge_card, pillar=P01, nucleus=N04`.
It loads builder ISOs, injects knowledge context, generates a structured artifact,
validates it, saves it, and compiles it to YAML -- all automatically.

**Option B -- CLI (no Claude Code)**

```bash
python _tools/cex_8f_runner.py \
    "create knowledge card about the 8F pipeline" \
    --kind knowledge_card \
    --execute
```

**Option C -- Python SDK**

```python
from cex_sdk import CEXAgent

agent = CEXAgent(nucleus="n03", kind="knowledge_card")
result = agent.build("the 8F pipeline")
print(result.artifact)  # full markdown
print(result.passed)    # True if score >= 8.0
print(result.trace)     # F1:knowledge_card/P01 | F3:2srcs(...)
```

---

## Step 4 -- Verify the Output (30 sec)

After the build completes, confirm the artifact exists and is healthy:

```bash
python _tools/cex_doctor.py
```

**Success indicators:**

| Signal | What it means |
|--------|---------------|
| `0 FAIL` in doctor summary | All builder ISOs and artifacts valid |
| New `.md` file in `N04_knowledge/P01_knowledge/` | Artifact saved to correct pillar |
| Compiled `.yaml` in `N04_knowledge/compiled/` | cex_compile.py ran automatically |
| Frontmatter contains `quality: null` | Peer review gate intact |

---

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `pip install -e .` fails with `No module named setuptools` | Outdated pip | `pip install --upgrade pip setuptools wheel` |
| `cex_doctor.py` shows `FAIL: missing frontmatter field: quality` | File self-scored | Change `quality: 8.x` to `quality: null` |
| `cex_doctor.py` shows `FAIL: non-ASCII` | Emoji or accented char in code | `python _tools/cex_sanitize.py --fix --scope _tools/` |
| `/build` command not recognized in Claude Code | CLAUDE.md not loaded | Start Claude Code at the repo root (not a subdirectory) |
| `cex_8f_runner.py` produces empty output | Missing API key | Set `ANTHROPIC_API_KEY` or start Ollama service |
| `density below 0.80` warning in doctor | Too much prose | Replace paragraphs with tables or bullet lists |
| `cex_setup_validator.py` shows MCP_SERVERS FAIL | MCP servers not installed | Run `python _tools/cex_setup_validator.py --fix` |

---

## Architecture: What Just Happened

The `/build` command activated the 8F pipeline:

| Stage | Function | What it did |
|-------|----------|-------------|
| F1 | CONSTRAIN | Resolved `kind=knowledge_card`, loaded `P01/_schema.yaml` |
| F2 | BECOME | Loaded 12 builder ISOs from `archetypes/builders/knowledge-card-builder/` |
| F3 | INJECT | Pulled KC library, examples, brand context from `.cex/brand/brand_config.yaml` |
| F4 | REASON | Planned 5 sections using template-first approach (match >= 60%) |
| F5 | CALL | Ran `cex_retriever.py` to find similar artifacts |
| F6 | PRODUCE | Generated full markdown with valid YAML frontmatter |
| F7 | GOVERN | Validated H01-H07 gates; score >= 8.0 required to pass |
| F8 | COLLABORATE | Saved to pillar dir, compiled to YAML, committed, sent signal |

Every artifact kind (300 total) follows this same 8F path.

---

## Next Steps

| Goal | Path |
|------|------|
| Understand the full architecture | `docs/concepts.md` + `.claude/rules/8f-reasoning.md` |
| Build a new artifact kind (contributor) | `N04_knowledge/P01_knowledge/quickstart_guide_first_builder.md` |
| Run the full CLI reference | `docs/cli-reference.md` |
| Use the Python SDK | `docs/sdk-reference.md` |
| Explore available kinds | `python _tools/cex_8f_runner.py --list-kinds` |
| Run system tests | `python _tools/cex_system_test.py` |
| Bootstrap brand context | `python _tools/cex_bootstrap.py` |
| Check all builders healthy | `python _tools/cex_doctor.py` |

---

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_qs_first_builder]] | sibling | 0.85 |
| [[bld_instruction_kind]] | upstream | 0.72 |
| [[p01_kc_8f_pipeline]] | upstream | 0.68 |
| [[bld_architecture_kind]] | related | 0.61 |
| [[bld_schema_kind]] | related | 0.58 |
| [[bld_collaboration_kind]] | downstream | 0.54 |
| [[p03_sp_builder_nucleus]] | related | 0.48 |
| [[bld_output_template_builder]] | upstream | 0.45 |
| [[p12_wf_spec_to_code]] | downstream | 0.41 |
| [[p03_sp_kind_builder]] | upstream | 0.38 |
