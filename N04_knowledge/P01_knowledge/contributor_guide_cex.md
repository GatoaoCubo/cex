---
id: p05_cg_cex
kind: contributor_guide
8f: F8_collaborate
pillar: P05
title: "Contributing to CEX"
version: 1.0.0
created: "2026-04-19"
updated: "2026-04-19"
author: N04_knowledge
domain: contributor guide
quality: 8.8
tags: [contributor_guide, cex, oss, builders, nuclei]
tldr: "How to contribute to CEX: setup, four contribution paths, quality gates, and PR process."
related:
  - bld_architecture_kind
  - kind-builder
  - bld_instruction_kind
  - bld_tools_kind
  - bld_collaboration_kind
  - bld_output_template_builder
  - bld_schema_kind
  - p03_sp_kind_builder
  - ctx_cex_new_dev_guide
  - p11_qg_knowledge
density_score: 1.0
---

# Contributing to CEX

CEXAI is an open-source AI brain for LLM agents: 300 kinds, 301 builders, 8 nuclei, and a
self-assimilating 8F pipeline. Contributions add new builders, knowledge cards, SDK providers,
or domain-specialized nuclei. Every contribution passes the same quality gates as internal work.
This guide covers everything from environment setup to a merged PR.

---

## Getting Started

### Prerequisites

| Item | Minimum Version | How to Verify |
|------|----------------|---------------|
| Python | 3.10+ | `python --version` |
| pip | 22+ | `pip --version` |
| git | 2.38+ | `git --version` |
| Node.js (MCP tools only) | 18+ | `node --version` |

### Installation

```bash
# 1. Fork on GitHub, then clone your fork
git clone https://github.com/<your-username>/cex.git
cd cex

# 2. Add upstream
git remote add upstream https://github.com/gato3/cex.git

# 3. Install in editable mode with dev deps
pip install -e ".[dev]"

# 4. Install pre-commit hooks
python _tools/cex_hooks.py install

# 5. Run health check -- must show 0 FAIL before any code change
python _tools/cex_doctor.py
```

If setup fails, open an issue with `python _tools/cex_doctor.py` output and your OS version.

---

## The Four Contribution Paths

### Path 1: New Builder (Recommended for First Contribution)

A builder is 13 ISO files in `archetypes/builders/{kind}-builder/`. Builders teach the LLM
pipeline how to produce a specific kind of artifact.

**Step 1 — Find an unbuild kind:**

```bash
python -c "
import json; from pathlib import Path
meta = json.loads(Path('.cex/kinds_meta.json').read_text(encoding='utf-8'))
built = {p.name.replace('-builder','') for p in Path('archetypes/builders').iterdir() if p.is_dir()}
[print(k) for k in sorted(meta) if k not in built]
"
```

**Step 2 — Copy the reference builder:**

```bash
cp -r archetypes/builders/agent-builder archetypes/builders/{kind}-builder
```

**Step 3 — Fill all 13 ISOs:**

| # | File | Purpose | Size Target |
|---|------|---------|-------------|
| 1 | `bld_system_prompt_{kind}.md` | Identity, role, constraints | 500-800 B |
| 2 | `bld_instruction_{kind}.md` | Step-by-step execution | 1-2 KB |
| 3 | `bld_quality_gate_{kind}.md` | Pass/fail criteria | 600-900 B |
| 4 | `bld_knowledge_card_{kind}.md` | Domain knowledge | max 4 KB |
| 5 | `bld_architecture_{kind}.md` | Component map, data flow | 600-900 B |
| 6 | `bld_collaboration_{kind}.md` | Inter-builder dependencies | 400-600 B |
| 7 | `bld_memory_{kind}.md` | Learning record schema | 400-600 B |
| 8 | `bld_examples_{kind}.md` | Input/output examples | 1-2 KB |
| 9 | `bld_schema_{kind}.md` | Input/output JSON/YAML schema | 600-900 B |
| 10 | `bld_config_{kind}.md` | Builder configuration | 400-600 B |
| 11 | `bld_manifest_{kind}.md` | Metadata: version, pillar, kind, tags | 400-600 B |
| 12 | `bld_output_template_{kind}.md` | Output format template | 1-3 KB |
| 13 | `bld_tools_{kind}.md` | Available tools and integrations | 400-600 B |

**Step 4 — Validate and PR:**

```bash
python _tools/cex_doctor.py        # must show 0 FAIL
python _tools/cex_score.py archetypes/builders/{kind}-builder/   # must show density >= 0.80
```

PR title: `[builder] add {kind}-builder`

---

### Path 2: Knowledge Card

Knowledge cards are domain encyclopedias for LLM context injection. They live in
`N00_genesis/P01_knowledge/library/kind/kc_{kind}.md`.

**Rules:**

- Frontmatter: `kind: knowledge_card`, `pillar: P01`, `quality: null`
- Density >= 0.80: tables and bullets preferred over prose blocks > 3 lines
- Max 4 KB per card (context window budget)
- One card per topic: no duplicates

**Walkthrough:**

```bash
# 1. Check no KC exists for your topic
ls N00_genesis/P01_knowledge/library/kind/ | grep kc_{topic}

# 2. Copy structure from an existing KC
cat N00_genesis/P01_knowledge/library/kind/kc_agent.md

# 3. Write your KC following the frontmatter schema
# 4. Score it
python _tools/cex_score.py N00_genesis/P01_knowledge/library/kind/kc_{topic}.md
```

PR title: `[knowledge] add kc_{topic}`

---

### Path 3: SDK Provider

CEX routes LLM calls across Claude, Codex, Gemini, and Ollama. A new provider extends this
routing to additional models or inference services.

**Steps:**

1. Read `cex_sdk/providers/` for existing provider implementations
2. Implement the `ProviderBase` interface in `cex_sdk/interfaces.py`
3. Add your provider to `.cex/config/nucleus_models.yaml` under `fallback_chain:`
4. Run the cross-runtime smoke test:

```bash
python _tools/cex_showoff.py --wave 1
```

5. All 6 nuclei must boot and signal; 0 crashes.

PR title: `[sdk] add {provider}-provider`

---

### Path 4: Vertical Nucleus

A vertical nucleus is a domain-specialized CEX fractal (N08+). Examples: N08_healthcare,
N09_fintech, N10_edtech. Each brings domain expertise the core team lacks.

**Minimum viable nucleus (5 required files):**

| # | File | Purpose |
|---|------|---------|
| 1 | `rules/n{xx}-{domain}.md` | Identity, sin lens, domain scope |
| 2 | `P02_model/nucleus_def_n{xx}.md` | Machine-readable identity |
| 3 | `P01_knowledge/kc_{domain}_vocabulary.md` | Controlled vocabulary |
| 4 | `P08_architecture/agent_card_n{xx}.md` | Capabilities declaration |
| 5 | `P08_architecture/component_map_n{xx}.md` | What this nucleus builds |

**Directory structure:**

```
N08_healthcare/
  P01_knowledge/
  P02_model/
  P03_prompt/
  P04_tools/
  P05_output/
  P06_schema/
  P07_evals/
  P08_architecture/
  P09_config/
  P10_memory/
  P11_feedback/
  P12_orchestration/
  rules/
  compiled/
```

**Assimilation review checks:**

- All 12 pillar dirs exist (fractal compliance)
- Vocabulary terms do not conflict with `p03_pc_cex_universal.md` canonical terms
- `nucleus_def` follows `N00_genesis/P02_model/_schema.yaml`
- No non-ASCII in `.py`, `.ps1`, `.sh` files

PR title: `[nucleus] add N{XX}_{domain}`

---

## Quality Gates

All contributions must pass these gates before a PR can be reviewed:

| Gate | Threshold | How to run |
|------|-----------|-----------|
| Doctor | 0 FAIL | `python _tools/cex_doctor.py` |
| Density | >= 0.80 | `python _tools/cex_score.py {file}` |
| Quality | `null` in frontmatter | Peer review assigns score -- never self-score |
| Naming | snake_case, ASCII, <= 50 chars | Pre-commit hook (auto-runs on commit) |
| Frontmatter | All required fields present | Pre-commit hook |
| Non-ASCII in code | 0 violations | `python _tools/cex_sanitize.py --check` |

---

## Commit Messages

Format: `[{scope}] {action}: {description}`

| Scope | When |
|-------|------|
| `[builder]` | Adding or modifying a builder ISO |
| `[knowledge]` | Knowledge card changes |
| `[nucleus]` | Nucleus-level changes |
| `[sdk]` | SDK or provider changes |
| `[tools]` | `_tools/` scripts |
| `[docs]` | Documentation only |
| `[fix]` | Bug fix |

Examples:
```
[builder] add changelog-builder (13 ISOs, pillar P01)
[knowledge] add kc_fhir_resources -- FHIR R4 resource taxonomy
[fix] cex_doctor: handle empty pillar directory gracefully
```

---

## Pull Request Process

1. Run `python _tools/cex_doctor.py` -- must show 0 FAIL.
2. Self-score: `python _tools/cex_score.py {your_file}` -- density >= 0.80.
3. Fill the PR template completely. Incomplete PRs will be returned without review.
4. Reference the related issue: `Relates to #{{issue_number}}`.
5. Request review from a maintainer via GitHub.
6. Respond to review feedback within 5 business days.

**Merge policy:** PRs are squash-merged after 1 maintainer approval. The PR author writes
the squash commit message using the format above.

---

## Review Process

Maintainers aim to provide initial review within **5 business days**.

Reviews assess:
- Correctness: does the artifact follow its kind's schema?
- Density: tables and bullets, no prose walls
- Cross-references: does it link to related artifacts correctly?
- Non-ASCII compliance in code files
- 13 ISO completeness for builder PRs

**Re-review:** after addressing feedback, re-request review via the GitHub button.
Do not open a new PR for revisions.

---

## What NOT to Do

- Do not self-score quality -- leave `quality: null` in frontmatter
- Do not submit a builder with fewer than 13 ISO files
- Do not use Portuguese, emoji, or non-ASCII in code files (`.py`, `.ps1`, `.sh`)
- Do not open a PR without running `cex_doctor` first
- Do not put credentials, API keys, or `.env` contents in any file
- Do not add features beyond what the task requires (no speculative abstraction)

---

## Getting Help

- **GitHub Discussions** for questions about how CEX works
- **Issues** for bugs and tracked work only (use issue templates)
- **SECURITY.md** for security vulnerabilities -- never in public issues

See also: [Quickstart Guide](quickstart_guide_first_builder.md) | [FAQ](faq_entry_cex_common_questions.md)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.49 |
| [[kind-builder]] | downstream | 0.42 |
| [[bld_instruction_kind]] | upstream | 0.42 |
| [[bld_tools_kind]] | upstream | 0.41 |
| [[bld_collaboration_kind]] | downstream | 0.39 |
| [[bld_output_template_builder]] | upstream | 0.36 |
| [[bld_schema_kind]] | downstream | 0.33 |
| [[p03_sp_kind_builder]] | upstream | 0.29 |
| [[ctx_cex_new_dev_guide]] | related | 0.27 |
| [[p11_qg_knowledge]] | downstream | 0.26 |
