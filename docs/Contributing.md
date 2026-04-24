# Contributing

This guide covers how to extend CEXAI: adding new kinds, bootstrapping new nuclei, writing builder ISOs, and following code standards.

## Adding a New Kind

A kind is the atomic artifact type in CEXAI. Adding one requires creating assets across multiple locations.

### Step 1: Define the kind

Determine which [[Architecture|pillar]] (P01-P12) the kind belongs to. Every kind maps to exactly one pillar.

### Step 2: Create the knowledge card

```
N00_genesis/P01_knowledge/library/kind/kc_{kind}.md
```

The KC defines what this kind IS: its purpose, structure, relationships, and examples. Use existing KCs as templates.

### Step 3: Create the builder

```
archetypes/builders/{kind}-builder/
```

Each builder has 12 ISOs, one per pillar:

| File | Pillar | Purpose |
|------|--------|---------|
| `bld_knowledge_{kind}.md` | P01 | Domain knowledge |
| `bld_model_{kind}.md` | P02 | Builder identity and role |
| `bld_prompt_{kind}.md` | P03 | Prompt engineering |
| `bld_tools_{kind}.md` | P04 | Tool usage |
| `bld_output_{kind}.md` | P05 | Output format |
| `bld_schema_{kind}.md` | P06 | Schema and validation |
| `bld_eval_{kind}.md` | P07 | Quality evaluation |
| `bld_architecture_{kind}.md` | P08 | Structural patterns |
| `bld_config_{kind}.md` | P09 | Configuration |
| `bld_memory_{kind}.md` | P10 | Memory handling |
| `bld_feedback_{kind}.md` | P11 | Feedback and learning |
| `bld_orchestration_{kind}.md` | P12 | Orchestration |

### Step 4: Create the sub-agent

```
.claude/agents/{kind}-builder.md
```

This is the Claude Code sub-agent definition that references the builder ISOs.

### Step 5: Register in kinds_meta.json

Add an entry to `.cex/kinds_meta.json`:

```json
{
  "kind": "my_new_kind",
  "pillar": "P05",
  "nucleus": "n03",
  "requires_external_context": false
}
```

### Step 6: Add to pillar schema

Update the relevant `N00_genesis/P{xx}_*/_schema.yaml` to include the new kind.

### Step 7: Add to the kind index

Update `N00_genesis/P01_knowledge/library/kind/kind_index.md` with the new entry.

### Step 8: Validate

```bash
python _tools/cex_doctor.py
python _tools/cex_compile.py archetypes/builders/{kind}-builder/
```

## Adding a New Nucleus (N08+)

New nuclei extend CEXAI into vertical domains (healthcare, fintech, legal, etc.). This is a significant addition with 9 required assets.

### Prerequisites

Before bootstrapping:

1. Verify the domain is NOT already covered by N01-N06 (check `nucleus_def` files)
2. Choose a sin lens (one of the seven deadly sins)
3. Confirm the domain has a clear vocabulary boundary

### Sin Lens Selection

| Sin | Optimization Bias | Best For |
|-----|-------------------|----------|
| Envy | Competitive analysis, benchmarking | Research, intelligence |
| Lust | Creative output, aesthetic | Marketing, design |
| Pride | Technical excellence, precision | Engineering, code |
| Gluttony | Volume, completeness, depth | Knowledge, documentation |
| Wrath | Quality gating, enforcement | Operations, testing |
| Greed | Revenue, monetization | Commercial, sales |
| Sloth | Delegation, efficiency | Orchestration |

### Directory Structure

Create the full fractal directory tree with all 12 pillar subdirectories:

```
N{XX}_{domain}/
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
    crews/
  rules/
  compiled/
```

All 12 pillar directories MUST exist (fractal compliance).

### 9 Required Assets

| # | Asset | Path |
|---|-------|------|
| 1 | Rule file | `N{XX}_{domain}/rules/n{xx}-{domain}.md` |
| 2 | Nucleus definition | `N{XX}_{domain}/P02_model/nucleus_def_n{xx}.md` |
| 3 | Agent card | `N{XX}_{domain}/P08_architecture/agent_card_n{xx}.md` |
| 4 | Domain vocabulary KC | `N{XX}_{domain}/P01_knowledge/kc_{domain}_vocabulary.md` |
| 5 | Component map | `N{XX}_{domain}/P08_architecture/component_map_n{xx}.md` |
| 6 | System prompt | `.claude/agents/n{xx}-{domain}.md` |
| 7 | Boot script (Claude) | `boot/n{xx}.ps1` |
| 8 | Boot script (Codex) | `boot/n{xx}_codex.ps1` |
| 9 | Permissions | `.claude/nucleus-settings/n{xx}.json` |

### Registration

Add the new nucleus to `.cex/config/nucleus_models.yaml`:

```yaml
n{xx}:
  model: sonnet-4-6
  context: 200000
  fallback_chain: [claude, ollama]
```

New nuclei start with scoped permissions (not trusted). Only add permissions as needed.

### Vertical Examples

| Nucleus | Domain | Sin | Key Kinds |
|---------|--------|-----|-----------|
| N08 | Healthcare (FHIR, HL7) | Gluttony | `healthcare_vertical` |
| N09 | Fintech (PCI-DSS, payments) | Greed | `fintech_vertical` |
| N10 | EdTech (LMS, SCORM) | Pride | `edtech_vertical` |
| N11 | Legal (contracts, compliance) | Wrath | `legal_vertical` |
| N12 | GovTech (public services) | Envy | `govtech_vertical` |

## Writing Builder ISOs

Builder ISOs are the specialized knowledge units that teach a builder how to produce a specific kind. Each builder has 12 ISOs, mapped 1:1 to the 12 pillars.

### ISO Mapping Rules

These ISOs have special 8F function mappings:

| ISO | 8F Function |
|-----|-------------|
| `bld_model_{kind}.md` | F2 BECOME (builder identity) |
| `bld_architecture_{kind}.md` | F1 CONSTRAIN (structural rules) |
| `bld_manifest_{kind}.md` | F2 BECOME (builder manifest) |
| `bld_examples_{kind}.md` | F7 GOVERN (quality examples) |

### ISO Structure

Every ISO follows this structure:

```markdown
---
id: bld_{pillar_short}_{kind}
kind: builder_iso
pillar: P{xx}
builder: {kind}-builder
version: 1.0.0
quality: null
---

# {Pillar Name} ISO for {Kind} Builder

## Purpose
What this ISO teaches the builder about this pillar's domain.

## Instructions
Specific instructions for the builder when operating in this pillar.

## Patterns
Reusable patterns and templates.

## Anti-Patterns
What to avoid.
```

### Shared Defaults

Common patterns live in `archetypes/builders/_shared/`. When a kind-specific ISO does not exist, the shared default is used.

## Code Standards

### ASCII-Only for Executable Code

All executable code (`.py`, `.ps1`, `.sh`, `.cmd`, `.bat`) MUST be ASCII-only (bytes 0x00-0x7F).

**Why:** Python `print()` uses the terminal codec. Windows defaults to cp1252. Non-ASCII in output causes `UnicodeEncodeError` crashes.

**Exceptions:**
- `.ps1` files may have a UTF-8 BOM at byte 0
- `.py` files may use `\uXXXX` escape sequences for functional i18n strings

**Replacements:**

| Non-ASCII | ASCII Replacement |
|-----------|-------------------|
| Em-dash | `--` |
| Smart quotes | Straight quotes `"` `'` |
| Check mark | `[OK]` |
| Cross mark | `[FAIL]` |
| Warning | `[WARN]` |
| Emoji | `[!!]` `[>>]` `[i]` |

Non-ASCII IS allowed in `.md` content files, `.yaml` data values, and user-facing templates.

**Enforcement:**
1. Pre-commit hook: `cex_hooks.py pre-commit`
2. Sanitizer check: `python _tools/cex_sanitize.py --check --scope _tools/`
3. Auto-fix: `python _tools/cex_sanitize.py --fix --scope _tools/`

### 8F Is Mandatory

Every artifact passes through the [[8F Pipeline]]. No exceptions. This applies to contributed artifacts as well.

### Frontmatter Required

Every artifact must have YAML frontmatter:

```yaml
---
id: unique_identifier
kind: the_kind_name
title: Human-Readable Title
version: 1.0.0
quality: null
tags: [relevant, tags]
---
```

The `quality: null` field is mandatory -- artifacts never self-score. Quality is assigned by peer review via `cex_score.py`.

### Artifact Naming

Files follow the pattern: `{pillar_prefix}_{artifact_type}_{name}.md`

Examples:
- `p01_kc_prompt_engineering.md` (P01, knowledge card)
- `p02_agent_customer_support.md` (P02, agent)
- `p08_ac_n03.md` (P08, agent card)

## Validation Checklist

Before submitting:

- [ ] `python _tools/cex_doctor.py` -- all checks pass
- [ ] `python _tools/cex_sanitize.py --check` -- no non-ASCII in code
- [ ] `python _tools/cex_compile.py {path}` -- artifact compiles
- [ ] Frontmatter present with `quality: null`
- [ ] Kind registered in `.cex/kinds_meta.json`
- [ ] Builder has all 12 ISOs
- [ ] Sub-agent exists in `.claude/agents/`

## Related Pages

- [[Architecture]] -- System structure and nucleus overview
- [[8F Pipeline]] -- The mandatory reasoning protocol
- [[Kinds]] -- Full kind taxonomy
- [[Commands]] -- `/build` and `/validate` for testing contributions
