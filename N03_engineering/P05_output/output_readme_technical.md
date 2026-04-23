---
id: n03_readme_technical
kind: output_template
pillar: P05
title: "CEX Public README — Architecture & Quickstart"
version: 1.0.0
created: 2026-04-02
author: n03_builder
domain: engineering
quality: 9.1
tags: [readme, architecture, quickstart, public, onboarding]
tldr: "Architecture diagram, 5-step quickstart, and directory map for the CEX public README."
density_score: 0.91
related:
  - ctx_cex_new_dev_guide
  - p01_kc_cex_project_overview
  - spec_cex_system_map
  - p01_ctx_cex_project
  - p03_sp_n03_creation_nucleus
  - p03_sp_cex_core_identity
  - p01_kg_cex_system_architecture
  - skill
  - index
  - dispatch
---

# Architecture & Quickstart

## Architecture

```
                         ┌──────────────┐
                         │  Human Goal  │
                         └──────┬───────┘
                                │
                         ┌──────▼───────┐
                         │ N07 Orchestr │  /plan → /guide → /spec → /grid
                         └──────┬───────┘
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                  ▼
   ┌──────────────┐  ┌──────────────┐   ┌──────────────┐
   │ N01 Intel    │  │ N03 Builder  │   │ N02 Market   │
   │ N04 Knowledge│  │ N05 Ops      │   │ N06 Commerce │
   └──────┬───────┘  └──────┬───────┘   └──────┬───────┘
          │                 │                   │
          ▼                 ▼                   ▼
   ┌────────────────────────────────────────────────┐
   │              8F Pipeline (per artifact)         │
   │  F1 Constrain → F2 Become → F3 Inject →       │
   │  F4 Reason   → F5 Call   → F6 Produce →       │
   │  F7 Govern   → F8 Collaborate                  │
   └──────────────────────┬─────────────────────────┘
                          ▼
   ┌────────────────────────────────────────────────┐
   │            12 Pillars (artifact storage)        │
   │  P01 Knowledge  P02 Model    P03 Prompt        │
   │  P04 Tools      P05 Output   P06 Schema        │
   │  P07 Evals      P08 Arch     P09 Config        │
   │  P10 Memory     P11 Feedback P12 Orchestration │
   └────────────────────────────────────────────────┘
```

**114 artifact kinds** · **107 builder archetypes** · **8 nuclei** · **12 pillars**

Each builder loads 13 ISOs (manifest, instruction, system prompt, schema, examples, quality gates, etc.)
and produces validated artifacts through the 8F pipeline with 18-gate quality enforcement.

---

## Quickstart

```bash
# 1. Clone
git clone https://github.com/your-org/cex.git && cd cex

# 2. Install
pip install -r requirements.txt

# 3. Bootstrap your brand identity (~2 min)
claude                          # opens Claude Code
> /init                         # answers 6 questions → brand_config.yaml

# 4. Build your first artifact
> /build knowledge card about React patterns

# 5. Run a full mission (parallel nuclei)
> /mission build landing page for my SaaS
```

---

## Directory Structure

```
cex/
├── archetypes/builders/    # 107 builder archetypes (13 ISOs each)
├── P01-P12_*/              # 12 pillars — artifact storage by domain
├── N00_genesis/            # Template nucleus (fractal mold)
├── N01-N07_*/              # 7 nuclei — each mirrors 12 pillars
├── _tools/                 # 25 Python tools (10K+ lines)
├── _spawn/                 # Dispatch scripts (solo/grid)
├── .cex/                   # Runtime state, signals, handoffs
├── boot/                   # Nucleus boot scripts (n01-n07)
├── cex_sdk/                # Python SDK (78 files, 4.5K lines)
└── CLAUDE.md               # System entry point
```

| Layer | Count | Purpose |
|-------|-------|---------|
| Kinds | 114 | Typed artifact categories |
| Builders | 107 | Specialized artifact factories |
| Pillars | 12 | Domain-organized storage |
| Nuclei | 8 | Autonomous agent clusters |
| Tools | 25 | Pipeline, quality, indexing |
| Quality gates | 18 | 8 hard + 10 soft validation |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[ctx_cex_new_dev_guide]] | related | 0.48 |
| [[p01_kc_cex_project_overview]] | upstream | 0.47 |
| [[spec_cex_system_map]] | upstream | 0.43 |
| [[p01_ctx_cex_project]] | upstream | 0.41 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.36 |
| [[p03_sp_cex_core_identity]] | upstream | 0.33 |
| [[p01_kg_cex_system_architecture]] | upstream | 0.32 |
| [[skill]] | downstream | 0.32 |
| [[index]] | downstream | 0.31 |
| [[dispatch]] | downstream | 0.30 |
