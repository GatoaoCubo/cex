---
id: spec_exchange_protocol
kind: constraint_spec
pillar: P06
title: "Exchange Protocol -- Sharing Typed Cognition Across CEXAI Instances"
version: 1.0.0
created: 2026-04-21
updated: 2026-04-21
author: n03_engineering
domain: exchange
quality: 8.3
quality_target: 9.0
status: SPEC
scope: cross-nucleus
tags: [exchange, protocol, sharing, community, nucleus, spec]
tldr: "Defines how CEXAI instances share typed artifacts and vertical nuclei via git-based pull model with quality gates on import."
density_score: null
related:
  - kc_artificial_sins
  - kc_cex_as_digital_asset
  - contributor_guide_cex
  - spec_cexai_rebrand
---

# Exchange Protocol -- Sharing Typed Cognition Across CEXAI Instances

## 1. THE PROBLEM

Each CEXAI instance is sovereign: your repo, your git, your brand. Sovereignty is
non-negotiable -- brand_config, memory, secrets never leave the instance. But
intelligence compounds faster when shared. A healthcare nucleus (N08) built by a
medical AI team benefits every CEXAI instance that imports it, and the importing
instance makes the ecosystem smarter by scoring, improving, and contributing back.

No specification exists for how instances exchange typed artifacts safely. Without
one, sharing is ad-hoc: copy-paste, manual validation, broken frontmatter,
vocabulary conflicts, untested schema compatibility. The exchange dimension -- the
reason "Exchange" is in the name -- needs an architectural contract.

Three gaps this spec closes:

| Gap | Risk without spec | Resolution |
|-----|-------------------|------------|
| No exchange unit definition | Contributors share files, not typed artifacts | Artifact = .md + YAML frontmatter (self-describing) |
| No quality gate on import | Imported artifacts degrade the instance | cex_doctor + cex_score + cex_compile validate on import |
| No compatibility contract | Vertical nuclei break in foreign instances | N00 schemas = universal compatibility layer |

## 2. THE EXCHANGE MODEL

### 2.1 What IS Exchangeable

| Exchange unit | Scope | Example | Brand-safe? |
|---------------|-------|---------|-------------|
| N00 artifact | Universal kind definition, schema, builder | `kc_agent.md`, `agent-builder/` (12 ISOs) | Yes -- N00 is brand-agnostic by design |
| Vertical nucleus (N08+) | Full 12-pillar domain department | `N08_healthcare/` with FHIR KCs, clinical workflows | Yes -- contributor's brand, not importer's |
| Knowledge card | Single typed fact or domain brief | `kc_fhir_resources.md` | Yes -- data, not brand voice |
| Builder | 12 ISOs teaching 8F how to produce a kind | `changelog-builder/` | Yes -- structural, not voice |
| SDK provider | Runtime adapter | `cex_sdk/providers/mistral.py` | Yes -- infrastructure |

### 2.2 What is NOT Exchangeable

| Artifact | Why excluded | Risk if shared |
|----------|-------------|----------------|
| `brand_config.yaml` | Contains brand identity, voice, colors | Overwrites importer's brand -- destructive |
| P10 memory artifacts | Instance-specific entity/episodic memory | Contaminates importer's context |
| `.cex/runtime/` state | Ephemeral PIDs, signals, handoffs | Meaningless outside originating instance |
| P09 secret_config | API keys, credentials | Security breach |
| `compiled/` YAMLs | Auto-generated from source .md | Regenerated locally by cex_compile |

### 2.3 The Artifact as Exchange Unit

Every CEXAI artifact is a `.md` file with YAML frontmatter. This is the exchange
unit because it is self-describing:

```yaml
---
id: kc_fhir_resources        # unique identifier
kind: knowledge_card          # type -> schema validation
pillar: P01                   # domain classification
quality: null                 # null on import, peer-assigned later
tags: [fhir, healthcare, hl7] # discovery metadata
version: 1.0.0                # SemVer for compatibility
---
# Content follows...
```

**Self-describing properties that enable exchange:**

| Field | Exchange function |
|-------|-------------------|
| `kind` | Importer validates against `kinds_meta.json` -- unknown kinds rejected |
| `pillar` | Routes to correct directory in importer's fractal structure |
| `quality` | Reset to `null` on import -- importer's peer review scores independently |
| `version` | SemVer enables compatibility checks against importer's N00 schemas |
| `tags` | Discovery via `cex_retriever.py` after import |

### 2.4 The Vertical Nucleus as Exchange Unit

A vertical nucleus is a complete 12-pillar domain department. It is the highest-value
exchange unit because it brings an entire domain expertise package:

```
N08_healthcare/
  P01_knowledge/         # Domain KCs (FHIR, HL7, clinical terms)
  P02_model/             # nucleus_def, agent assignments
  P03_prompt/            # Domain-specific prompts, system prompts
  P04_tools/             # Tool configs (EHR connectors, FHIR APIs)
  P05_output/            # Templates (clinical notes, discharge summaries)
  P06_schema/            # Domain data contracts (FHIR resource schemas)
  P07_evals/             # Domain benchmarks, scoring rubrics
  P08_architecture/      # agent_card, component_map
  P09_config/            # Domain configs (rate limits, endpoints)
  P10_memory/            # (empty on export -- instance-specific)
  P11_feedback/          # Quality gates, domain regression checks
  P12_orchestration/     # Crew templates, domain workflows
  rules/                 # Nucleus identity, sin lens, domain scope
  compiled/              # (gitignored -- regenerated locally)
```

**Minimum viable nucleus (5 required files):**

| # | File | Purpose | Validates against |
|---|------|---------|-------------------|
| 1 | `rules/n{xx}-{domain}.md` | Identity + sin lens + scope | N/A (freeform, reviewed) |
| 2 | `P02_model/nucleus_def_n{xx}.md` | Machine-readable identity | `N00_genesis/P02_model/_schema.yaml` |
| 3 | `P01_knowledge/kc_{domain}_vocabulary.md` | Controlled vocabulary | `p03_pc_cex_universal.md` (no conflicts) |
| 4 | `P08_architecture/agent_card_n{xx}.md` | Capabilities declaration | agent_card schema |
| 5 | `P08_architecture/component_map_n{xx}.md` | What this nucleus builds | component_map schema |

## 3. EXCHANGE MECHANICS

### 3.1 Pull Model (Git-Based, Decentralized)

CEXAI exchanges follow a pull model -- the importer decides what enters their
instance, not the exporter. This preserves sovereignty.

```
EXPORTER                         IMPORTER
(contributor)                    (adopter)
    |                                |
    |  1. Push nucleus to public     |
    |     repo / fork                |
    |                                |
    |  2. -------[discover]--------> |  importer finds via GitHub search,
    |                                |  community index, or direct link
    |                                |
    |  3. <------[cherry-pick]------ |  importer pulls specific artifacts
    |                                |  (not the whole repo)
    |                                |
    |                                |  4. cex_doctor validates
    |                                |  5. cex_score assigns quality: null
    |                                |  6. cex_compile integrates into index
    |                                |  7. cex_intent_resolver adapts
```

**Import commands:**

```bash
# Add a community remote
git remote add community https://github.com/{user}/cexai

# Import a vertical nucleus
git checkout community/main -- N08_healthcare/

# Import a single KC
git checkout community/main -- N00_genesis/P01_knowledge/library/kind/kc_fhir_resources.md

# Import a builder
git checkout community/main -- archetypes/builders/clinical_note-builder/
```

**N00 as compatibility layer:** All instances share the same N00_genesis schemas
(12 pillar `_schema.yaml` files). An artifact that validates against N00 in the
exporter's instance will validate in the importer's instance. N00 is the universal
contract.

### 3.2 Quality Gates on Import

Imported artifacts enter with `quality: null` regardless of their score in the
source instance. The importer's quality pipeline re-evaluates independently.

| Gate | Tool | Pass condition | On failure |
|------|------|----------------|------------|
| Structural validity | `cex_doctor.py` | 0 FAIL for imported paths | Reject import, report errors |
| Kind recognition | `kinds_meta.json` lookup | `kind` field matches known kind | Reject or register new kind |
| Schema compliance | `_schema.yaml` per pillar | Frontmatter fields match schema | Reject, list missing fields |
| Vocabulary conflict | `p03_pc_cex_universal.md` diff | No term redefinition conflicts | Flag conflicts for manual resolution |
| Non-ASCII compliance | `cex_sanitize.py --check` | 0 violations in `.py`/`.ps1`/`.sh` | Reject code files with non-ASCII |
| Compilation | `cex_compile.py {path}` | Compiles without error | Fix or reject |
| Index integration | `cex_retriever.py --rebuild` | Artifact appears in search results | Debug indexing |

```bash
# Full import validation pipeline
python _tools/cex_doctor.py                        # structural
python _tools/cex_sanitize.py --check --scope N08_healthcare/  # ASCII
python _tools/cex_compile.py N08_healthcare/       # compilation
python _tools/cex_retriever.py --rebuild           # index
```

### 3.3 Security Model

| Principle | Implementation | Enforcement |
|-----------|----------------|-------------|
| Private by default | Repo is private; nothing shared unless contributor opts in | Git visibility settings |
| Brand never leaves | `brand_config.yaml` is in `.gitignore` for public forks | `.gitignore` + pre-commit hook |
| Memory is instance-local | P10 artifacts excluded from public branches | Export script strips P10 |
| Secrets never shared | P09 `secret_config` excluded | `.gitignore` + `cex_export_public.sh` |
| Audit trail | Every import is a git commit with provenance | `git log --oneline` |
| Quality re-evaluation | `quality: null` on import | cex_score.py resets score |

## 4. ANTI-FRAGILE BY DESIGN

### 4.1 Runtime Agnosticism

Exchanged artifacts are runtime-agnostic. The artifact is the contract, not the
runtime executing it. This means:

| Property | Implication for exchange |
|----------|------------------------|
| Same .md format across runtimes | Artifact produced on Claude works on Gemini/Ollama |
| 8F pipeline is universal | Quality gates produce consistent results regardless of runtime |
| Kind schemas are model-independent | Validation uses YAML structure, not LLM judgment |
| Builder ISOs are prompt-based | Any LLM that reads Markdown can execute them |

A nucleus built on Claude Opus can be imported and operated on Ollama's Qwen3
(with expected quality variance in generation, but identical structural validation).

### 4.2 Neuroplastic Assimilation

When a new nucleus is imported, the system adapts:

```
IMPORT N08_healthcare/
    |
    v
cex_intent_resolver.py            # Registers new domain vocabulary
    |
    v
p03_pc_cex_universal.md           # Prompt compiler adds new kind mappings
    |
    v
kinds_meta.json                   # New kinds registered (if contributed)
    |
    v
cex_retriever.py --rebuild        # New artifacts in search index
    |
    v
System is smarter                 # User says "FHIR resource" -> resolves to
                                  # kind=knowledge_card, domain=healthcare,
                                  # nucleus=N08, pillar=P01
```

Each import makes the system more capable. The retriever index grows. The intent
resolver recognizes more phrases. The prompt compiler handles more domains. This is
not additive -- it is compound. Domain A's vocabulary enriches context for Domain B.

### 4.3 Degradation Resistance

| Failure mode | Protection |
|--------------|------------|
| Bad artifact imported | Quality gates reject or flag; `quality: null` prevents score inflation |
| Vocabulary conflict | cex_doctor detects; manual resolution required before merge |
| Schema version mismatch | SemVer in frontmatter; incompatible versions rejected at validation |
| Malicious content | Pre-commit hook blocks non-ASCII in code; manual review for KCs |
| Orphan references | cex_doctor cross-reference check finds broken links |

## 5. CONTRIBUTOR ON-RAMP

The 4 paths from CONTRIBUTING.md map directly to exchange granularity:

| Path | What you share | Exchange scope | Time to first PR | Complexity |
|------|---------------|----------------|-------------------|------------|
| Knowledge Card | 1 typed artifact | Micro -- single fact or domain brief | 30 min | Low |
| Builder | 12 ISOs for 1 kind | Meso -- production capability for 1 artifact type | 2 hrs | Medium |
| SDK Provider | 1 runtime adapter | Infra -- new runtime for all artifacts | 4 hrs | Medium-High |
| Vertical Nucleus | Full 12P department | Macro -- entire domain expertise | 8 hrs | High |

**Path 4 (Vertical Nucleus) is the exchange's highest-leverage contribution.** One
contributor's 8-hour investment creates a domain department that every CEXAI
instance can import. A healthcare team builds N08 once; 1000 instances benefit.

**Incentive alignment:** Contributors benefit from the exchange because:
1. Their artifacts get peer-reviewed (quality improvement)
2. Their nucleus appears in the community index (visibility)
3. Improvements from importers flow back via PRs (compounding)
4. The 8F pipeline + quality gates ensure their work is taken seriously

## 6. VERSIONING + COMPATIBILITY

### 6.1 Schema Compatibility Contract

N00_genesis pillar schemas (`P{01-12}/_schema.yaml`) define the compatibility
surface. An artifact is compatible with any CEXAI instance that shares the same
N00 schema version.

| Version field | Scope | Example |
|---------------|-------|---------|
| Artifact `version` | Individual artifact SemVer | `1.0.0`, `1.1.0`, `2.0.0` |
| N00 schema `version` | Pillar-level compatibility | `_schema.yaml` version field |
| `kinds_meta.json` version | Kind registry compatibility | New kinds require registry update |

### 6.2 Conflict Resolution

| Conflict type | Detection | Resolution |
|---------------|-----------|------------|
| Same `id` in two artifacts | cex_doctor duplicate check | Importer renames with namespace prefix |
| Vocabulary term redefined | diff against `p03_pc_cex_universal.md` | Contributor adjusts to canonical term |
| Schema field added | N00 schema diff | Backward-compatible if optional; breaking if required |
| Kind name collision | `kinds_meta.json` lookup | Contributor uses domain-prefixed kind name |

### 6.3 Backward Compatibility Rule

N00 schema changes follow a strict contract:
- **MINOR** (1.x.0): New optional fields, new kinds -- backward compatible
- **MAJOR** (x.0.0): Required field changes, kind renames -- breaking, migration script required
- **PATCH** (1.0.x): Documentation, examples -- no structural change

Importers pin to an N00 schema version. Upgrades are opt-in with migration tooling.

## 7. FUTURE: EXCHANGE REGISTRY (TODO)

> **Status: Vision. Not built. Marked for post-launch implementation.**

A community index where contributors register their nuclei, builders, and KCs for
discovery. Analogous to npm/PyPI but for typed cognition.

| Feature | Purpose | Priority |
|---------|---------|----------|
| Registry API | List/search published nuclei and builders | P1 |
| Quality badge | Display peer-reviewed quality score | P1 |
| Compatibility matrix | Show which N00 schema versions are supported | P2 |
| Download stats | Track adoption for contributor visibility | P2 |
| Dependency graph | Show which nuclei depend on which builders/KCs | P3 |
| Auto-update notification | Alert importers when upstream nucleus updates | P3 |

**Implementation constraint:** The registry is read-only metadata. Actual artifact
transfer remains git-based (pull model). The registry indexes; it does not host.

## 8. REFERENCE IMPLEMENTATION

### Import a vertical nucleus (full workflow)

```bash
# 1. Add community source
git remote add healthcare-team https://github.com/healthcare-team/cexai

# 2. Fetch without merging
git fetch healthcare-team

# 3. Import the nucleus directory
git checkout healthcare-team/main -- N08_healthcare/

# 4. Validate
python _tools/cex_doctor.py
python _tools/cex_sanitize.py --check --scope N08_healthcare/
python _tools/cex_compile.py N08_healthcare/

# 5. Register new kinds (if any)
# Edit .cex/kinds_meta.json to add healthcare-specific kinds

# 6. Rebuild index
python _tools/cex_retriever.py --rebuild

# 7. Commit
git add N08_healthcare/ .cex/kinds_meta.json
git commit -m "[N08] import healthcare nucleus from healthcare-team"

# 8. Test intent resolution
python _tools/cex_intent_resolver.py "FHIR patient resource"
# Expected: kind=knowledge_card, domain=healthcare, nucleus=N08
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_artificial_sins]] | upstream | -- |
| [[kc_cex_as_digital_asset]] | upstream | -- |
| [[contributor_guide_cex]] | downstream | -- |
| [[spec_cexai_rebrand]] | parent | -- |
| [[kc_contributor_nucleus_standard]] | downstream | -- |
