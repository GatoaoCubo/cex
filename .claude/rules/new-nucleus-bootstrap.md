# New Nucleus Bootstrap Rule (N08+)

## When This Fires

Any request to create, scaffold, or bootstrap a new nucleus beyond N07.
Trigger phrases: "new nucleus", "add N08", "healthcare nucleus", "create vertical".

## Prerequisites

Before bootstrapping, verify:
1. The domain is NOT already covered by N01-N06 (check nucleus_def files)
2. The contributor chose a sin lens (one of the seven deadly sins)
3. The domain has a clear vocabulary boundary (does not conflict with existing canonical terms)

## Directory Structure (Mandatory)

```
N{XX}_{domain}/
  P01_knowledge/
    kc_{domain}_vocabulary.md      # controlled vocabulary (REQUIRED)
  P02_model/
    nucleus_def_n{xx}.md           # machine-readable identity (REQUIRED)
  P03_prompt/
  P04_tools/
  P05_output/
  P06_schema/
  P07_evals/
  P08_architecture/
    agent_card_n{xx}.md            # capability declaration (REQUIRED)
    component_map_n{xx}.md         # what this nucleus builds (REQUIRED)
  P09_config/
  P10_memory/
  P11_feedback/
  P12_orchestration/
    crews/                         # crew templates go here
  rules/
    n{xx}-{domain}.md              # nucleus identity + sin lens (REQUIRED)
  compiled/                        # gitignored, auto-generated
```

All 12 pillar directories MUST exist (fractal compliance).

## 9 Required Assets

| # | Asset | Path | Purpose |
|---|-------|------|---------|
| 1 | Rule file | `N{XX}_{domain}/rules/n{xx}-{domain}.md` | Identity, sin lens, domain scope, 8F customizations |
| 2 | Nucleus def | `N{XX}_{domain}/P02_model/nucleus_def_n{xx}.md` | Machine-readable identity (kind: nucleus_def) |
| 3 | Agent card | `N{XX}_{domain}/P08_architecture/agent_card_n{xx}.md` | Capability declaration for A2A |
| 4 | Domain vocabulary | `N{XX}_{domain}/P01_knowledge/kc_{domain}_vocabulary.md` | Controlled vocabulary KC |
| 5 | Component map | `N{XX}_{domain}/P08_architecture/component_map_n{xx}.md` | What this nucleus builds |
| 6 | System prompt | `.claude/agents/n{xx}-{domain}.md` | Claude Code sub-agent definition |
| 7 | Boot script (Claude) | `boot/n{xx}.ps1` | PowerShell launcher for Claude runtime |
| 8 | Boot script (codex) | `boot/n{xx}_codex.ps1` | PowerShell launcher for Codex runtime |
| 9 | Permissions | `.claude/nucleus-settings/n{xx}.json` | Scoped permission set (copy from _template.json) |

## Bootstrap Steps

### Step 1: Create directory tree

```bash
for p in P01_knowledge P02_model P03_prompt P04_tools P05_output P06_schema P07_evals P08_architecture P09_config P10_memory P11_feedback P12_orchestration; do
  mkdir -p "N{XX}_{domain}/$p"
done
mkdir -p "N{XX}_{domain}/rules" "N{XX}_{domain}/compiled" "N{XX}_{domain}/P12_orchestration/crews"
```

### Step 2: Create 5 minimum viable nucleus files

Use existing nucleus_def files as templates:
- `N01_intelligence/P08_architecture/nucleus_def_n01.md` (research domain)
- `N02_marketing/P08_architecture/nucleus_def_n02.md` (creative domain)
- `N05_operations/P08_architecture/nucleus_def_n05.md` (ops domain)

Each file follows N00_genesis schemas in `N00_genesis/P{XX}_*/_schema.yaml`.

### Step 3: Create boot scripts

Copy `boot/n01.ps1` and adapt:
- Change `$NucleusId` to `n{xx}`
- Change `$NucleusName` to the domain name
- Change agent card path to the new nucleus
- Ensure `-WorktreeDir`, `-Task`, `-AutoAccept` parameters work

### Step 4: Create permissions

```bash
cp .claude/nucleus-settings/_template.json .claude/nucleus-settings/n{xx}.json
```

New nuclei start SCOPED (not trusted). Only add permissions as needed.

### Step 5: Register routing

Add entry to `.cex/config/nucleus_models.yaml`:
```yaml
n{xx}:
  model: sonnet-4-6
  context: 200000
  fallback_chain: [claude, ollama]
```

### Step 6: Validate

```bash
python _tools/cex_doctor.py
python _tools/cex_sanitize.py --check --scope N{XX}_{domain}/
ls N{XX}_{domain}/P{01..12}*/
```

### Step 7: Signal completion

```python
from _tools.signal_writer import write_signal
write_signal('n{xx}', 'complete', 9.0)
```

## Sin Lens Selection Guide

| Sin | Optimization Bias | Best For |
|-----|-------------------|----------|
| Envy | Competitive analysis, benchmarking | Research, intelligence |
| Lust | Creative output, aesthetic | Marketing, design |
| Pride | Technical excellence, precision | Engineering, code |
| Gluttony | Volume, completeness, depth | Knowledge, documentation |
| Wrath | Quality gating, enforcement | Operations, testing |
| Greed | Revenue, monetization | Commercial, sales |
| Sloth | Delegation, efficiency | Orchestration |

## Anti-Patterns

- Creating a nucleus for a subdomain already covered (use a kind instead)
- Skipping the vocabulary KC (leads to semantic drift with existing nuclei)
- Using trusted permissions (new nuclei start scoped)
- Hardcoding model in boot script (use nucleus_models.yaml)
- Missing any of the 12 pillar directories (breaks fractal compliance)

## Vertical Examples

| Nucleus | Domain | Sin | Key Kinds |
|---------|--------|-----|-----------|
| N08_healthcare | FHIR, HL7, clinical | Gluttony (clinical data completeness) | fhir_agent_capability, healthcare_vertical |
| N09_fintech | PCI-DSS, payments, risk | Greed (revenue optimization) | fintech_vertical |
| N10_edtech | LMS, SCORM, adaptive | Pride (pedagogical precision) | edtech_vertical, course_module |
| N11_legal | Contracts, compliance | Wrath (regulatory enforcement) | legal_vertical, compliance_framework |
| N12_govtech | Public services, policy | Envy (benchmark against peers) | govtech_vertical |
