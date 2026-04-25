# CEX Hierarchy: Functions > Pillars > Kinds > Nuclei

## 5 Layers

```
L0  8 FUNCTIONS      HOW anything gets made (universal pipeline)
 |  CONSTRAIN > BECOME > INJECT > REASON > CALL > PRODUCE > GOVERN > COLLABORATE
 |
L1  12 PILLARS       WHAT categories exist (taxonomy structure)
 |  P01 Knowledge .. P12 Orchestration
 |
L2  123 KINDS        WHAT types exist per pillar (genesis definitions)
 |  agent, knowledge_card, workflow, quality_gate, agent_card, mcp_server, ...
 |
L3  123 BUILDERS     HOW to make each kind (factory, 13 ISOs each)
 |  bld_schema, bld_manifest, bld_instruction, ...
 |
L4  8 NUCLEI         Instances -- genesis FILLED with domain content
    N00 (genesis) + N01..N07, each mirrors L1 with domain-specific artifacts
```

## Layer Mapping

| Layer | Analogy | CEX Implementation |
|-------|---------|-------------------|
| L0 Functions | The machine | 8F Runner pipeline (cex_8f_runner.py) |
| L1 Pillars | The blueprint | P01-P12 schemas (_schema.yaml) |
| L2 Kinds | The type catalog | 123 kind definitions (kinds_meta.json) |
| L3 Builders | The factory | 123 x 13 = 1,599 ISO files |
| L4 Nuclei | The instances | N00-N07 filled with domain content |

## Genesis = L1 + L2 + L3

The genesis (N00) is the MOLD -- it defines what CAN be built.
It contains no domain content, only structure and instructions.

## Nucleus = Genesis filled with domain

Each nucleus mirrors the 12 pillars via subdirectories with domain-specific instances:

```
N03_engineering/          (Engineering nucleus -- 47 .md files)
  agents/                 mirrors P02 (agent, model_card kinds)
  architecture/           mirrors P08 (agent_card, pattern, diagram kinds)
  config/                 mirrors P09 (env_config, path_config kinds)
  feedback/               mirrors P11 (quality_gate, bugloop kinds)
  knowledge/              mirrors P01 (knowledge_card, context_doc kinds)
  memory/                 mirrors P10 (learning_record, runtime_state kinds)
  orchestration/          mirrors P12 (workflow, dispatch_rule kinds)
  output/                 mirrors P05 (response_format, formatter kinds)
  prompts/                mirrors P03 (system_prompt, instruction kinds)
  quality/                mirrors P07 (scoring_rubric, benchmark kinds)
  schemas/                mirrors P06 (input_schema, type_def kinds)
  tools/                  mirrors P04 (cli_tool, mcp_server kinds)
  compiled/               compiled .yaml output
```

## Nucleus Roster

| ID | Directory | Domain | .md Files | CLI | Model |
|----|-----------|--------|-----------|-----|-------|
| N00 | N00_genesis/ | Archetype (mold) | 1 | -- | -- |
| N01 | N01_intelligence/ | Research & Intelligence | 55 | claude | opus-4-6 1M |
| N02 | N02_marketing/ | Marketing & Creative | 58 | claude | opus-4-6 1M |
| N03 | N03_engineering/ | Engineering & Build | 47 | claude | opus-4-6 1M |
| N04 | N04_knowledge/ | Knowledge & Indexing | 67 | claude | opus-4-6 1M |
| N05 | N05_operations/ | Operations & DevOps | 56 | claude | opus-4-6 1M |
| N06 | N06_commercial/ | Commercial & Monetization | 58 | claude | opus-4-6 1M |
| N07 | N07_admin/ | Orchestration & Admin | 39 | claude | opus-4-6 1M |

All nuclei run via Claude Code CLI. Boot scripts in `boot/`.
N07 orchestrates and dispatches. N01-N06 build autonomously.

## Nucleus Drive (User-Defined)

Each nucleus can have a DRIVE -- a motivation that shapes its behavior.
This is an OPTIONAL personality layer. Users fill it via `/init` or leave generic.

| # | Domain | Default Drive | Configurable via |
|---|--------|---------------|-----------------|
| N01 | Research & Intelligence | {{DRIVE}} | .cex/brand/brand_config.yaml |
| N02 | Marketing & Copy | {{DRIVE}} | .cex/brand/brand_config.yaml |
| N03 | Engineering & Build | {{DRIVE}} | .cex/brand/brand_config.yaml |
| N04 | Knowledge & Indexing | {{DRIVE}} | .cex/brand/brand_config.yaml |
| N05 | Operations & Execution | {{DRIVE}} | .cex/brand/brand_config.yaml |
| N06 | Commercial & Monetization | {{DRIVE}} | .cex/brand/brand_config.yaml |
| N07 | Orchestration & Admin | {{DRIVE}} | .cex/brand/brand_config.yaml |

> **Example**: One organization uses 7 deadly sins (ENVY, LUST, PRIDE, GLUTTONY, WRATH, GREED, SLOTH) as drives.

## Build Order (Wave Pattern)

N07 (Orchestrator) dispatches nuclei in dependency-aware waves:

```
Wave 1: N03 Engineering (bootstrap proof -- builds itself)
Wave 2: N07 Admin (orchestrator completes)
Wave 3: N04 Knowledge + N01 Research (foundation)
Wave 4: N02 Marketing + N05 Operations + N06 Commercial (parallel)
```

Dispatch: `bash _spawn/dispatch.sh grid MISSION`

## Core Kind Set (minimum viable nucleus)

Every nucleus needs at least 7 artifacts:

| Kind | Pillar | Subdir | Purpose |
|------|--------|--------|---------|
| agent_card | P08 | architecture/ | Deployment spec (identity + model + tools) |
| agent | P02 | agents/ | Persona + capabilities |
| system_prompt | P03 | prompts/ | Voice and operating rules |
| dispatch_rule | P12 | orchestration/ | How work reaches this nucleus |
| knowledge_card | P01 | knowledge/ | Domain knowledge |
| workflow | P12 | orchestration/ | Execution pipeline |
| quality_gate | P11 | feedback/ | Domain quality standards |

---

*Hierarchy v3.0 -- 8 nuclei, 12 pillars, 300 kinds. Claude Code native. 2026-04-08.*
