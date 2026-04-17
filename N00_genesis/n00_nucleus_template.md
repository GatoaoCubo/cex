---
id: n00_nucleus_template
kind: nucleus_def
pillar: P02
nucleus: n00
title: "N00 Nucleus Template -- Blank Instantiation Contract"
version: 1.0
quality: null
tags: [n00, template, nucleus_def, archetype, instantiation]
---

<!-- 8F: F1=nucleus_def P02 F2=nucleus-def-builder F3=kinds_meta+nucleus_defs F4=plan F5=scan F6=produce F7=gate F8=save -->

# Nucleus Definition Template

> Fill all `{{VARIABLE}}` placeholders before deploying a new nucleus.
> Reference: `N00_genesis/n00_README.md` for instantiation guide.

---

## Identity

```yaml
nucleus_id: "{{NUCLEUS_ID}}"          # n08, n09, n10 ... (sequential after N07)
role_name: "{{ROLE_NAME}}"            # e.g., "sales", "legal", "research"
sin_lens: "{{SIN_LENS}}"              # one of: envy, lust, pride, gluttony, wrath, greed, sloth
sin_label: "{{SIN_LABEL}}"           # e.g., "Analytical Envy", "Creative Lust"
model_tier: "{{MODEL_TIER}}"         # sonnet | opus | haiku
model_id: "{{MODEL_ID}}"             # e.g., claude-sonnet-4-6
context_window: {{CONTEXT_WINDOW}}   # 200000 | 1000000
```

---

## Role Description

**What this nucleus does:**
{{ROLE_DESCRIPTION}}

**What it does NOT do (boundary):**
{{ROLE_BOUNDARY}}

**When N07 dispatches to this nucleus:**
- {{DISPATCH_TRIGGER_1}}
- {{DISPATCH_TRIGGER_2}}
- {{DISPATCH_TRIGGER_3}}

---

## Sin Lens Injection

The sin lens is the nucleus's cultural DNA. It determines the optimization pressure
applied to all ambiguous decisions.

```
Sin: {{SIN_LENS}}
Label: {{SIN_LABEL}}
Optimizes for: {{SIN_OPTIMIZATION}}
Under ambiguity, prefers: {{SIN_PREFERENCE}}
Avoids: {{SIN_AVOIDANCE}}
```

**Sin lens examples from active nuclei:**

| Nucleus | Sin | Behavior under ambiguity |
|---------|-----|--------------------------|
| N01 | Analytical Envy | Chooses depth over speed; seeks more data |
| N02 | Creative Lust | Chooses seduction over accuracy; tries bolder copy |
| N03 | Inventive Pride | Chooses elegance over pragmatism; refactors |
| N04 | Knowledge Gluttony | Ingests more sources; indexes deeper |
| N05 | Gating Wrath | Fails fast; strict quality enforcement |
| N06 | Strategic Greed | Maximizes revenue signal; monetizes edge cases |
| N07 | Orchestrating Sloth | Delegates everything; orchestrates, never builds |

---

## Primary Pillars

```yaml
primary_pillars:
  - "{{PRIMARY_PILLAR_1}}"   # e.g., P01 -- where this nucleus produces most artifacts
  - "{{PRIMARY_PILLAR_2}}"   # e.g., P07 -- secondary domain
secondary_pillars:
  - "{{SECONDARY_PILLAR_1}}" # supported but not primary
reads_from:
  - P01_knowledge             # all nuclei read P01 (KCs + context)
  - P08_architecture          # all nuclei read P08 (agent cards + nucleus defs)
```

---

## Capabilities

### Core kinds produced

| Kind | Pillar | Frequency | Purpose |
|------|--------|-----------|---------|
| `{{KIND_1}}` | `{{PILLAR_1}}` | primary | {{KIND_1_PURPOSE}} |
| `{{KIND_2}}` | `{{PILLAR_2}}` | primary | {{KIND_2_PURPOSE}} |
| `{{KIND_3}}` | `{{PILLAR_3}}` | secondary | {{KIND_3_PURPOSE}} |

### Tools available

```yaml
tools:
  - name: "{{TOOL_1}}"
    purpose: "{{TOOL_1_PURPOSE}}"
  - name: "cex_8f_runner.py"
    purpose: "8F pipeline execution"
  - name: "cex_retriever.py"
    purpose: "Artifact similarity search"
  - name: "cex_compile.py"
    purpose: "Artifact compilation"
```

---

## Files to Create

The following files are required at minimum for a functional nucleus.
Create them in order (each depends on the prior).

```
N{{NUCLEUS_ID}}_{{ROLE_NAME}}/
  rules/
    n{{NUCLEUS_ID}}-{{ROLE_NAME}}.md          # 1. Identity + 8F rules + routing
  P08_architecture/
    nucleus_def_n{{NUCLEUS_ID}}.md            # 2. This file (filled)
    agent_card_n{{NUCLEUS_ID}}.md             # 3. Deployment spec
  P03_prompt/
    system_prompt_n{{NUCLEUS_ID}}.md          # 4. Voice + constraints + sin lens
  P02_model/
    agent_n{{NUCLEUS_ID}}.md                  # 5. Agent persona definition
  P10_memory/
    memory_scope_n{{NUCLEUS_ID}}.md           # 6. What this nucleus remembers
  P01_knowledge/
    kc_{{ROLE_NAME}}_domain.md               # 7. Core domain knowledge card
```

Boot script (required):
```
boot/
  n{{NUCLEUS_ID}}.ps1                        # 8. PowerShell boot wrapper
```

---

## Boot Script Template

Save as `boot/n{{NUCLEUS_ID}}.ps1`:

```powershell
# N{{NUCLEUS_ID}} Boot -- {{SIN_LABEL}}
# Model: {{MODEL_ID}} | Context: {{CONTEXT_WINDOW}}

$env:CEX_NUCLEUS = "n{{NUCLEUS_ID}}"
$env:CEX_ROLE = "{{ROLE_NAME}}"
$env:CEX_SIN = "{{SIN_LENS}}"
$env:CEX_MODEL = "{{MODEL_ID}}"

# Load task from handoff file (never pass as CLI arg)
$taskFile = ".cex\runtime\handoffs\n{{NUCLEUS_ID}}_task.md"
if (-not (Test-Path $taskFile)) {
    Write-Error "No handoff found: $taskFile"
    exit 1
}

# Boot Claude with nucleus rules pre-loaded
claude --model $env:CEX_MODEL `
    --add-dir "N{{NUCLEUS_ID}}_{{ROLE_NAME}}" `
    --system-prompt "N{{NUCLEUS_ID}}_{{ROLE_NAME}}/P03_prompt/system_prompt_n{{NUCLEUS_ID}}.md"
```

---

## nucleus_models.yaml Entry

Add to `.cex/P09_config/nucleus_models.yaml`:

```yaml
n{{NUCLEUS_ID}}:
  role: "{{ROLE_NAME}}"
  sin_lens: "{{SIN_LENS}}"
  model: "{{MODEL_ID}}"
  context: {{CONTEXT_WINDOW}}
  tier: "{{MODEL_TIER}}"
  fallback_chain:
    - claude
    - gemini
    - ollama
  primary_pillars:
    - "{{PRIMARY_PILLAR_1}}"
    - "{{PRIMARY_PILLAR_2}}"
  boot_script: "boot/n{{NUCLEUS_ID}}.ps1"
  agent_card: "N{{NUCLEUS_ID}}_{{ROLE_NAME}}/P08_architecture/agent_card_n{{NUCLEUS_ID}}.md"
```

---

## 12 Pillar Directory Structure

Every nucleus inherits the N00 12-pillar structure.
Create these directories:

```
N{{NUCLEUS_ID}}_{{ROLE_NAME}}/
  P01_knowledge/       # facts, domain KCs, RAG sources
  P02_model/           # agent definitions, model config
  P03_prompt/          # system prompt, templates, chains
  P04_tools/           # external tool wrappers
  P05_output/          # production artifacts (guides, pages)
  P06_schema/          # data contracts, input validation
  P07_evals/           # quality gates, benchmarks, tests
  P08_architecture/    # nucleus_def, agent_card, ADRs
  P09_config/          # runtime config, env, secrets
  P10_memory/          # entity memory, session state
  P11_feedback/        # quality signals, compliance
  P12_orchestration/   # workflows, crew templates
  rules/               # nucleus identity rules (n0X-*.md)
  crews/               # composable crew templates
  reports/             # analysis outputs
```

---

## Convention-Over-Configuration Variables

These variables are filled when instantiating from N00:

| Variable | Example (N01) | Example (N04) | Description |
|----------|---------------|---------------|-------------|
| `{{NUCLEUS_ID}}` | `01` | `04` | Sequential ID after N00 |
| `{{ROLE_NAME}}` | `intelligence` | `knowledge` | Nucleus operational role |
| `{{SIN_LENS}}` | `envy` | `gluttony` | Cultural DNA sin |
| `{{SIN_LABEL}}` | `Analytical Envy` | `Knowledge Gluttony` | Human-readable sin label |
| `{{MODEL_ID}}` | `claude-sonnet-4-6` | `claude-sonnet-4-6` | LLM model identifier |
| `{{MODEL_TIER}}` | `sonnet` | `sonnet` | Budget tier |
| `{{CONTEXT_WINDOW}}` | `200000` | `200000` | Max token context |
| `{{PRIMARY_PILLAR_1}}` | `P01` | `P01` | Main artifact pillar |
| `{{PRIMARY_PILLAR_2}}` | `P07` | `P10` | Secondary pillar |

---

## Quality Gate

Before a new nucleus is considered operational, it must pass:

- [ ] `nucleus_def_n0X.md` exists and has all required fields
- [ ] `agent_card_n0X.md` exists and references correct model
- [ ] `system_prompt_n0X.md` contains sin lens injection
- [ ] `rules/n0X-*.md` exists and defines routing rules
- [ ] `boot/n0X.ps1` exists and boots successfully
- [ ] First artifact produced scores >= 8.0
- [ ] Registered in `nucleus_models.yaml`
- [ ] `dispatch.sh solo n0X "test task"` succeeds

```bash
# Validate new nucleus
python _tools/cex_doctor.py --nucleus n0X
python _tools/cex_setup_validator.py --check
bash _spawn/dispatch.sh solo n0X "produce a test knowledge_card about your domain"
```

---

## References

| Resource | Path |
|----------|------|
| Instantiation guide | `N00_genesis/n00_README.md` |
| Active nucleus examples | `N01_intelligence/` through `N07_admin/` |
| Nucleus model config | `.cex/P09_config/nucleus_models.yaml` |
| Dispatch protocol | `.claude/rules/n07-orchestrator.md` |
| 8F pipeline | `.claude/rules/8f-reasoning.md` |
| Sin lens definitions | `N0{1-7}_*/P08_architecture/nucleus_def_n0{1-7}.md` |
| New nucleus checklist | `.claude/rules/new-nucleus-bootstrap.md` |
