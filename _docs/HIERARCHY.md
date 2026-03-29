# CEX Hierarchy: Functions > Pillars > Kinds > Nuclei

## 5 Layers

```
L0  8 FUNCTIONS      HOW anything gets made (universal pipeline)
 |  CONSTRAIN > BECOME > INJECT > REASON > CALL > PRODUCE > GOVERN > COLLABORATE
 |
L1  12 PILLARS       WHAT categories exist (taxonomy structure)
 |  P01 Knowledge .. P12 Orchestration
 |
L2  99 KINDS         WHAT types exist per pillar (genesis definitions)
 |  agent, knowledge_card, workflow, quality_gate, agent_card, ...
 |
L3  99 BUILDERS      HOW to make each kind (factory, 13 ISOs each)
 |  bld_schema, bld_manifest, bld_instruction, ...
 |
L4  7 NUCLEI         Instances — genesis FILLED with domain content
    N01..N07, each mirrors L1 with domain-specific artifacts
```

## Metaphor

| Layer | Metaphor | CEX |
|-------|----------|-----|
| L0 Functions | The machine | 8F Runner pipeline |
| L1 Pillars | The blueprint | P01-P12 schemas |
| L2 Kinds | The mold catalog | 99 type definitions |
| L3 Builders | The factory | 99 x 13 ISO files |
| L4 Nuclei | The castings | N01-N07 filled instances |
| Seeds | The material | _seeds/ domain knowledge |

## Genesis = L1 + L2 + L3

The genesis is the MOLD — it defines what CAN be built.
It contains no domain content, only structure and instructions.

## Nucleus = Genesis filled with domain

Each nucleus mirrors the 12 pillars but contains domain-specific instances:

```
N03_engineering/          (EDISON nucleus)
  agents/                 mirrors P02 (agent kind)
  architecture/           mirrors P08 (agent_card, pattern kinds)
  config/                 mirrors P09 (env_config kind)
  feedback/               mirrors P11 (quality_gate kind)
  knowledge/              mirrors P01 (knowledge_card kind)
  memory/                 mirrors P10 (learning_record kind)
  orchestration/          mirrors P12 (workflow, dispatch_rule kinds)
  output/                 mirrors P05 (response_format kind)
  prompts/                mirrors P03 (system_prompt, instruction kinds)
  quality/                mirrors P07 (scoring_rubric kind)
  schemas/                mirrors P06 (input_schema kind)
  tools/                  mirrors P04 (skill, mcp_server kinds)
```

## 7 Deadly Sins (Nucleus Drive)

Each nucleus is driven by a productive sin — a channeled vice that becomes a virtue:

| # | Nucleus | Sin | Drive | Lens |
|---|---------|-----|-------|------|
| N01 | SHAKA | ENVY | Analytical | "What do they know that I don't?" |
| N02 | LILY | LUST | Strategic | "What desire don't they know they have?" |
| N03 | EDISON | PRIDE | Inventive | "Is this the best ever produced?" |
| N04 | PYTHA | GLUTTONY | Systematic | "What haven't I consumed yet?" |
| N05 | ATLAS | WRATH | Achieving | "Why isn't this running RIGHT NOW?" |
| N06 | YORK | GREED | Visionary | "What value is nobody capturing?" |
| N07 | STELLA | SLOTH | Productive | "Who should do this instead of me?" |

## Build Order (PRIDE builds everything)

EDISON (N03/PRIDE) constructs all nuclei using the genesis as mold:

```
Wave 1: N03 self-completes (bootstrap proof)
Wave 2: N07 STELLA completes (orchestrator)
Wave 3: N04 PYTHA + N01 SHAKA (knowledge + research)
Wave 4: N02 LILY + N05 ATLAS + N06 YORK (remaining)
```

Command: `bash _tools/build_all_nuclei.sh`
Dry-run: `bash _tools/build_all_nuclei.sh --dry-run`

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
