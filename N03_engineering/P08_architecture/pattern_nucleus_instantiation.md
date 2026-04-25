---
id: p08_pat_nucleus_instantiation
kind: pattern
8f: F4_reason
pillar: P08
title: "Pattern -- Nucleus Instantiation from N00 Archetype"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: nucleus-construction
quality: 8.7
tags: [pattern, nucleus, instantiation, N00, archetype, convention-over-configuration, coc, new-nucleus-bootstrap]
tldr: "Convention-over-Configuration pattern for creating a new nucleus (N08+) from the N00_genesis archetype. 9-step protocol with explicit file list, naming rules, and CoC compliance checks."
density_score: 0.92
related:
  - p08_pat_nucleus_fractal
  - bld_knowledge_card_nucleus_def
  - bld_collaboration_nucleus_def
  - bld_system_prompt_nucleus_def
  - nucleus-def-builder
  - p12_wf_orchestration_pipeline
  - p12_wf_create_orchestration_agent
  - p02_nd_n03.md
  - bld_architecture_kind
  - p01_kg_cex_system_architecture
---

# Pattern: Nucleus Instantiation from N00 Archetype

> **Industry equivalent:** class instantiation (N00 = class definition, N0X = instance)

## Purpose

N00_genesis is the archetype (industry: abstract base class). Creating a new nucleus (N08, N09, ...) means INSTANTIATING the archetype with domain-specific content, not reimplementing the base contract from scratch.

CoC rule: every nucleus has the same 13 subdirectory structure. A nucleus that deviates from this structure is NOT a nucleus — it is a collection of files.

## Preconditions

| Check | Command | Expected |
|-------|---------|---------|
| N00_genesis exists | `ls N00_genesis/` | 12 pillar dirs + README.md |
| kinds_meta.json current | `python _tools/cex_doctor.py --kinds` | 300 kinds |
| No existing nucleus at target slot | `ls N0{X}_*/` | does not exist |
| nucleus_sins.yaml has slot | `grep "n0{X}" .cex/config/nucleus_sins.yaml` | sin defined |

## Instantiation Protocol (9 Steps)

### Step 1: Claim the sin

Read `.cex/config/nucleus_sins.yaml`. Pick the sin for the new nucleus.
Write `N0{X}_{domain}/P08_architecture/nucleus_def_n0{X}.md`:

```yaml
id: p08_nd_n0{X}
kind: nucleus_def
nucleus: n0{X}
domain: {domain}
sin: {sin_name}
sin_pt: {sin_in_portuguese}
model_tier: sonnet|opus
```

### Step 2: Mirror P01-P12 structure

```bash
for P in P01_knowledge P02_model P03_prompt P04_tools P05_output \
         P06_schema P07_evals P08_architecture P09_config \
         P10_memory P11_feedback P12_orchestration; do
  mkdir -p N0{X}_{domain}/$P
  cp N00_genesis/$P/README.md N0{X}_{domain}/$P/README.md
done
```

CoC: directories must match this exact list. No additional pillars. No renamed pillars.

### Step 3: Write the agent identity (P02)

File: `N0{X}_{domain}/P02_model/agent_{domain}.md`
Kind: `agent`
Required fields: id, kind, nucleus, sin, domain, capabilities[], tools[]

Source: copy `N00_genesis/P02_model/` pattern, inject domain-specific capabilities.

### Step 4: Write the system prompt (P03)

File: `N0{X}_{domain}/P03_prompt/system_prompt_{domain}.md`
Kind: `system_prompt`
Required: sin_lens paragraph, F2b SPEAK activation, 8F protocol reference

Pattern:
```
You are N0{X}, the {domain} nucleus of CEX.
Your sin: {sin}. Your lens: {sin_behavioral_description}.
Load controlled vocabulary: N0{X}_{domain}/P01_knowledge/kc_{domain}_vocabulary.md
Follow 8F pipeline: .claude/rules/8f-reasoning.md
```

### Step 5: Write boot config (P09)

File: `N0{X}_{domain}/P09_config/boot_config_{domain}.md`
Kind: `boot_config`
Required: cli (claude|codex|gemini|ollama), model, context_window, fallback_chain[]

Boot scripts are PowerShell (see `boot/n0{X}.ps1` template from `.claude/rules/new-nucleus-bootstrap.md`).

### Step 6: Write nucleus rules

File: `N0{X}_{domain}/rules/n0{X}-{domain}.md`
Pattern: copy `N03_engineering/rules/n03-builder.md`, adapt sin, domain, routing rules.

CoC: exactly one rules file per nucleus. File name must match `n0{X}-*.md`.

### Step 7: Write agent card (P08)

File: `N0{X}_{domain}/P08_architecture/agent_card_{domain}.md`
Kind: `agent_card`
Required: capabilities[], input_schema, output_schema, quality_target, routing_rules[]

### Step 8: Write vocabulary KC (P01)

File: `N0{X}_{domain}/P01_knowledge/kc_{domain}_vocabulary.md`
Kind: `knowledge_card`
Required: canonical_terms table, anti-patterns table, cross-nucleus shared terms (never redefine)

### Step 9: Validate and register

```bash
# Validate structure
python _tools/cex_doctor.py --nucleus n0{X}

# Run system test
python _tools/cex_system_test.py --nucleus n0{X}

# Register in boot scripts
# Add to _spawn/dispatch.sh nucleus_list

# Signal ready
python -c "from _tools.signal_writer import write_signal; write_signal('n0{X}', 'bootstrapped', 9.0)"
```

## File Inventory (minimum viable nucleus)

| File | Kind | Step |
|------|------|------|
| `N0{X}_{domain}/P08_architecture/nucleus_def_n0{X}.md` | nucleus_def | 1 |
| `N0{X}_{domain}/P02_model/agent_{domain}.md` | agent | 3 |
| `N0{X}_{domain}/P03_prompt/system_prompt_{domain}.md` | system_prompt | 4 |
| `N0{X}_{domain}/P09_config/boot_config_{domain}.md` | boot_config | 5 |
| `N0{X}_{domain}/rules/n0{X}-{domain}.md` | rule | 6 |
| `N0{X}_{domain}/P08_architecture/agent_card_{domain}.md` | agent_card | 7 |
| `N0{X}_{domain}/P01_knowledge/kc_{domain}_vocabulary.md` | knowledge_card | 8 |
| `boot/n0{X}.ps1` | (external) | 5 |

## CoC Compliance Checks

| Check | Rule | Violation Consequence |
|-------|------|-----------------------|
| 13-subdir structure | Must match N00_genesis | cex_doctor.py FAIL |
| Nucleus slot | N08 follows N07, no gaps | dispatch.sh routing broken |
| Sin uniqueness | Each nucleus has unique sin | Identity collision |
| Vocabulary KC | Must exist before first dispatch | F2b SPEAK crashes |
| rules file | Exactly 1, named `n0{X}-*.md` | Lazy-load at boot fails |
| boot_config | cli field from allowed values | Routing fails at boot |

## What CoC Gives You

| Without CoC | With CoC (this pattern) |
|-------------|------------------------|
| Each nucleus invents its own structure | All nuclei share one known layout |
| Discovery requires manual inspection | `ls N0X_*/P{xx}/` works for any nucleus |
| N07 dispatch needs custom routing | Uniform routing: nuclei are interchangeable |
| New nucleus takes 2 hours | New nucleus takes 20 minutes |
| Agent card format varies | agent_card_{domain}.md is always the entry point |

## Cross-References

- `.claude/rules/new-nucleus-bootstrap.md` — 9-file minimum checklist (authoritative)
- `N00_genesis/P08_architecture/nucleus_def_n00.md` — archetype definition
- `N03_engineering/P08_architecture/nucleus_def_n03.md` — N03 as instantiation example
- `N03_engineering/P08_architecture/pattern_8f_full_trace.md` — trace convention loaded by new nuclei

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_pat_nucleus_fractal]] | sibling | 0.39 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.32 |
| [[bld_collaboration_nucleus_def]] | downstream | 0.29 |
| [[bld_system_prompt_nucleus_def]] | upstream | 0.29 |
| [[nucleus-def-builder]] | upstream | 0.25 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.25 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.23 |
| [[p02_nd_n03.md]] | upstream | 0.23 |
| [[bld_architecture_kind]] | related | 0.22 |
| [[p01_kg_cex_system_architecture]] | upstream | 0.22 |
