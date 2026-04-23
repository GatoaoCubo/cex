# Contributing to CEXAI

The X in CEXAI stands for **Exchange**. Intelligence compounds when shared. Every contribution -- a knowledge card, a builder, a provider, a vertical nucleus -- adds typed cognition to the exchange. Your artifacts improve everyone's retriever index. Their artifacts improve yours.

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).
Security issues go through [SECURITY.md](SECURITY.md) -- never in public issues.

---

## Quick Start

**Requirements:** Python 3.10+ · Git 2.30+

```bash
git fork + clone
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
python _tools/cex_hooks.py install   # pre-commit hooks
python _tools/cex_doctor.py          # must show 0 FAIL before you start
```

Pick a **Good First Issue** below, build it, run `cex_doctor`, open a PR.

| Path | Estimated time to first merged PR |
|------|----------------------------------|
| Path 2: Knowledge Card | 30-60 minutes |
| Path 1: Builder (12 ISO files) | 1-2 hours |
| Path 3: SDK Provider | 2-6 hours |
| Path 4: Vertical Nucleus | 4-8 hours |

---

## Four Contribution Paths

### Path 1: New Builder (recommended)

A builder is 12 ISO files in `archetypes/builders/{kind}-builder/`, each mapping to one
of the 12 CEX pillars (P01-P12). Simple builders override 4-5 ISOs; the rest are
inherited from `archetypes/builders/_shared/` defaults.

1. Find a kind without a builder -- run:
   ```bash
   python -c "
   import json; from pathlib import Path
   meta = json.loads(Path('.cex/kinds_meta.json').read_text(encoding='utf-8'))
   built = {p.name.replace('-builder','') for p in Path('archetypes/builders').iterdir() if p.is_dir()}
   [print(k) for k in sorted(meta) if k not in built]
   "
   ```
2. Copy the reference builder: `cp -r archetypes/builders/knowledge_card-builder archetypes/builders/{kind}-builder`
3. Fill the ISOs you need to override (shared defaults cover the rest):

| # | File | Pillar | Purpose |
|---|------|--------|---------|
| 1 | `bld_knowledge_{kind}.md` | P01 | Domain expertise |
| 2 | `bld_model_{kind}.md` | P02 | Identity + persona + metadata |
| 3 | `bld_prompt_{kind}.md` | P03 | Step-by-step execution |
| 4 | `bld_tools_{kind}.md` | P04 | Available tools |
| 5 | `bld_output_{kind}.md` | P05 | Output format template |
| 6 | `bld_schema_{kind}.md` | P06 | Input/output validation |
| 7 | `bld_eval_{kind}.md` | P07 | Quality gate + examples |
| 8 | `bld_architecture_{kind}.md` | P08 | Component map, dependencies |
| 9 | `bld_config_{kind}.md` | P09 | Builder tunables |
| 10 | `bld_memory_{kind}.md` | P10 | Learning record schema |
| 11 | `bld_feedback_{kind}.md` | P11 | Anti-patterns + improvement signals |
| 12 | `bld_orchestration_{kind}.md` | P12 | Handoffs, signals, collaboration |

ISOs not present in the kind directory are loaded from `_shared/` automatically.
Write only the overrides -- do not duplicate shared defaults.

4. Validate: `python _tools/cex_doctor.py` -- must show 0 FAIL
5. PR title: `[builder] add {kind}-builder`

### Path 2: Knowledge Card

Knowledge cards live in `N00_genesis/P01_knowledge/library/kind/kc_{kind}.md`.

1. Find a kind without a KC:
   ```bash
   python -c "
   from pathlib import Path; import json
   existing = {p.stem for p in Path('N00_genesis/P01_knowledge/library/kind').glob('kc_*.md')}
   meta = json.loads(Path('.cex/kinds_meta.json').read_text(encoding='utf-8'))
   [print(k) for k in sorted(meta) if f'kc_{k}' not in existing]
   "
   ```
2. Use frontmatter: `kind: knowledge_card`, `pillar: P01`, `quality: null`
3. Density >= 0.80: tables and bullets, no prose blocks over 3 lines
4. PR title: `[knowledge] add kc_{topic}`

### Path 3: SDK Provider

CEX runs on Claude, Codex, Gemini, and Ollama. Add a new provider in `cex_sdk/`.

1. Read `cex_sdk/providers/` for existing examples
2. Implement the provider interface (see `cex_sdk/interfaces.py`)
3. Add routing entry in `.cex/config/nucleus_models.yaml`
4. Run cross-runtime smoke: `python _tools/cex_showoff.py --wave 1`
5. PR title: `[sdk] add {provider}-provider`

### Path 4: Vertical Nucleus

A vertical nucleus is a domain-specialized CEXAI fractal (N08+). Each brings domain
expertise the core team lacks -- healthcare, fintech, legal, edtech, etc.

**This is the exchange's killer feature.** A contributed nucleus is a full AI department:
12 pillars of specialized knowledge, its own sin lens, its own vocabulary, its own builders.
Import it into any CEXAI instance and you get instant expertise in that domain -- typed,
scored, runtime-agnostic. See [Exchange Protocol](docs/specs/spec_exchange_protocol.md).

1. Fork the repo
2. Create `N{XX}_{domain}/` with all 12 pillar subdirs + `rules/` + `compiled/`:
   ```
   N08_healthcare/
     P01_knowledge/
     P02_model/
     ...
     P12_orchestration/
     rules/
     compiled/          # gitignored, auto-generated
   ```
3. Populate the **5 required files** (minimum viable nucleus):

| # | File | Purpose |
|---|------|---------|
| 1 | `rules/n{xx}-{domain}.md` | Nucleus identity, sin lens, domain scope |
| 2 | `P02_model/nucleus_def_n{xx}.md` | Machine-readable identity (kind: `nucleus_def`) |
| 3 | `P01_knowledge/kc_{domain}_vocabulary.md` | Domain controlled vocabulary |
| 4 | `P08_architecture/agent_card_n{xx}.md` | Capabilities declaration |
| 5 | `P08_architecture/component_map_n{xx}.md` | What this nucleus builds |

4. Choose a **sin lens** -- one of the seven deadly sins that drives your nucleus's
   optimization bias. Declare it in `nucleus_def_n{xx}.md`. See existing nucleus defs
   in `N0{1-7}_*/P08_architecture/nucleus_def_n0*.md` for examples.
5. Recommended extras:
   - `P12_orchestration/` -- crew_templates for domain-specific workflows
   - `P01_knowledge/` -- domain KCs (FHIR resources, PCI controls, SCORM objects, etc.)
   - `archetypes/builders/` -- domain-specific builders with 12-ISO sets
6. PR title: `[nucleus] add N{XX}_{domain}`

**Self-validate before opening a PR:**

```bash
python _tools/cex_doctor.py          # 0 FAIL required
ls N{XX}_{domain}/P{01..12}*/        # all 12 pillar dirs must exist
python _tools/cex_sanitize.py --check --scope N{XX}_{domain}/   # 0 non-ASCII in code
```

**Assimilation review checks:**

- All 12 pillar dirs exist (fractal compliance)
- Vocabulary terms in `kc_{domain}_vocabulary.md` do not conflict with existing canonical terms
- `nucleus_def` follows the schema in `N00_genesis/P02_model/_schema.yaml`
- No non-ASCII in code files (`.py`, `.ps1`, `.sh`)

---

## Quality Gates

| Gate | Threshold | How to run |
|------|-----------|-----------|
| Doctor | 0 FAIL | `python _tools/cex_doctor.py` |
| Density | >= 0.80 | `python _tools/cex_score.py {file}` |
| Quality | `null` in frontmatter | Peer review assigns score -- never self-score |
| Naming | snake_case, ASCII, <= 50 chars | Pre-commit hook |
| Frontmatter | All required fields | Pre-commit hook |

---

## Good First Issues

**300 registered kinds** -- the contribution surface is large. Some kinds still lack full builder coverage.
Run `python -c "import json; from pathlib import Path; meta=json.loads(Path('.cex/kinds_meta.json').read_text(encoding='utf-8')); built={p.name.replace('-builder','') for p in Path('archetypes/builders').iterdir() if p.is_dir()}; [print(k) for k in sorted(meta) if k not in built]"` to see the full list.

Selected starter picks:

| Kind | Description | Difficulty |
|------|-------------|------------|
| `ab_test_config` | A/B test experiment configuration for conversion optimization | Beginner |
| `action_paradigm` | How agents execute actions in environments | Beginner |
| `action_prompt` | Task prompt sent by human/orchestrator to the agent | Beginner |
| `agent_card` | Deployment spec for autonomous agent -- identity, model, tools, boot | Beginner |
| `agent_computer_interface` | GUI/terminal interaction protocol for agents | Beginner |
| `alert_rule` | Observable threshold condition with PromQL-style expression and routing | Beginner |
| `analyst_briefing` | Structured intelligence brief for stakeholder consumption | Beginner |
| `api_reference` | Auto-generated API documentation artifact | Beginner |
| `audit_log` | Immutable event log with actor, action, resource, outcome fields | Beginner |
| `axiom` | Foundational rule or principle that is not derived from other artifacts | Beginner |
| `benchmark_suite` | Collection of benchmarks with shared config and scoring criteria | Intermediate |
| `circuit_breaker` | Fault-tolerance pattern with state machine (closed/open/half-open) | Intermediate |
| `N08_healthcare` | Vertical nucleus -- FHIR, HL7, clinical workflows | Intermediate |
| `N09_fintech` | Vertical nucleus -- PCI-DSS, payment flows, risk models | Intermediate |
| `N10_edtech` | Vertical nucleus -- LMS, SCORM, adaptive learning | Intermediate |

Open an issue using the **New Builder** template to claim one before starting.

---

## After Your PR

1. A maintainer will review within **7-14 days** -- watch for review comments.
2. The reviewer assigns the quality score (you leave `quality: null`).
3. PRs that pass `cex_doctor` with 0 FAIL merge faster -- fix tool errors before requesting review.
4. For builders: all overridden ISOs must be non-empty. Partial builders are not merged.

---

## The Exchange

When you contribute to CEXAI, you are not just adding files to a repo. You are adding **typed cognition** to a shared knowledge system.

| What you contribute | What the exchange gives back |
|--------------------|-----------------------------|
| Knowledge Card | Your fact enters every instance's retriever index |
| Builder | Every CEXAI user can now produce your artifact kind |
| SDK Provider | The entire system gains a new runtime option |
| Vertical Nucleus | Everyone gets a new AI department for free |

**What stays private**: your brand config, memory, runtime state, and secrets never leave your instance. The exchange is about cognition, not identity.

---

## Questions?

Post in **GitHub Discussions** -- not in issues. Issues are for bugs and tracked work only.

---

## What NOT to Do

- Do not self-score quality -- leave `quality: null` in frontmatter
- Do not submit a builder with fewer than 4 ISO files (minimum: bld_knowledge, bld_model, bld_prompt, bld_eval)
- Do not use Portuguese, emoji, or non-ASCII in code files (`.py`, `.ps1`, `.sh`)
- Do not open a PR without running `cex_doctor` first
- Do not put credentials, API keys, or `.env` contents in any file
