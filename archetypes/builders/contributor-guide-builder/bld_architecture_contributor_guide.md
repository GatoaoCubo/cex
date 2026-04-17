---
kind: architecture
id: bld_architecture_contributor_guide
pillar: P08
llm_function: CONSTRAIN
purpose: Component inventory, dependency map, and architectural position of the contributor_guide builder
quality: 9.1
title: "Contributor Guide Builder Architecture"
version: "1.1.0"
author: n02_hybrid_review7
tags: [contributor_guide, builder, architecture]
tldr: "13-ISO builder architecture for contributor_guide: component inventory, dependency graph, and P05 positioning as OSS onboarding production unit"
domain: "contributor_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory

All 13 ISOs of the contributor-guide-builder with role, pillar, llm_function, and status.

| ISO | File | Kind | Pillar | LLM Function | Role |
|-----|------|------|--------|-------------|------|
| 1 | bld_manifest_contributor_guide.md | type_builder | P05 | BECOME | Builder identity, capabilities, and routing signals |
| 2 | bld_instruction_contributor_guide.md | instruction | P03 | REASON | 3-phase production instructions: research, compose, validate |
| 3 | bld_system_prompt_contributor_guide.md | system_prompt | P03 | BECOME | Persona activation with OSS-specific quality rules |
| 4 | bld_schema_contributor_guide.md | schema | P06 | CONSTRAIN | Frontmatter field definitions, ID pattern, body section order |
| 5 | bld_quality_gate_contributor_guide.md | quality_gate | P11 | GOVERN | 8 hard gates + 7 scored dimensions, publish floor 8.0 |
| 6 | bld_output_template_contributor_guide.md | output_template | P05 | PRODUCE | Canonical contributor guide template with all section scaffolds |
| 7 | bld_examples_contributor_guide.md | examples | P07 | GOVERN | Reference examples and anti-examples with failure analysis |
| 8 | bld_knowledge_card_contributor_guide.md | knowledge_card | P01 | INJECT | Domain knowledge: GitHub workflows, DCO/CLA, Conventional Commits |
| 9 | bld_architecture_contributor_guide.md | architecture | P08 | CONSTRAIN | Component inventory, dependency map, system position |
| 10 | bld_collaboration_contributor_guide.md | collaboration | P12 | COLLABORATE | Crew roles, receives-from, produces-for, boundary |
| 11 | bld_config_contributor_guide.md | config | P09 | CONSTRAIN | Naming, paths, limits, hooks |
| 12 | bld_memory_contributor_guide.md | memory | P10 | INJECT | Observed patterns, evidence, and builder recommendations |
| 13 | bld_tools_contributor_guide.md | tools | P04 | CALL | Production tools, validation checks, external OSS references |

---

## Dependency Graph

| ISO | Depends On | Reason |
|-----|-----------|--------|
| manifest | config | Routing keywords aligned with naming convention |
| instruction | schema | Phase 2 section order follows schema body structure |
| instruction | system_prompt | Compose phase applies persona constraints from system prompt |
| output_template | schema | Template sections must match required body section spec |
| quality_gate | schema | H01-H03 gates enforce schema constraints |
| quality_gate | examples | Gate thresholds calibrated against golden example scores |
| collaboration | manifest | Crew role derived from builder identity |
| tools | quality_gate | Validation checks implement gate H04-H08 |
| memory | examples | Learning records derived from example pattern analysis |

**Load order for 8F pipeline**:
1. config (F1 CONSTRAIN -- naming, limits)
2. schema (F1 CONSTRAIN -- field validation)
3. manifest (F2 BECOME -- identity)
4. system_prompt (F2 BECOME -- persona)
5. knowledge_card (F3 INJECT -- domain knowledge)
6. memory (F3 INJECT -- learned patterns)
7. examples (F3 INJECT -- calibration)
8. instruction (F4 REASON -- production plan)
9. tools (F5 CALL -- available tools)
10. output_template (F6 PRODUCE -- scaffold)
11. quality_gate (F7 GOVERN -- validation)
12. collaboration (F8 COLLABORATE -- handoff routing)
13. architecture (reference -- used for system audits)

---

## Architectural Position

The contributor_guide builder is the OSS onboarding documentation unit within
CEX Pillar P05 (Output Artifacts). It occupies the community documentation zone:

```
P05 Output Layer
  |
  +-- contributor_guide builder    <-- this builder
  |     Produces: CONTRIBUTING.md artifacts
  |     Audience: open source contributors
  |     Format: structured Markdown with code blocks
  |
  +-- press_release builder
  |     Produces: wire-ready press releases
  |     Audience: journalists, newswire systems
  |
  +-- landing_page builder
        Produces: HTML conversion pages
        Audience: web visitors
```

**Upstream**: Project maintainer brief (repository URL, CLA policy, CI toolchain,
coding standards), brand_config for company identity.

**Downstream**: Repository CONTRIBUTING.md, GitHub repository community health
files, contributor onboarding flow.

**Boundary enforcement**: contributor_guide does NOT produce code of conduct
(normative behavior policy), integration guides (consumer-facing API docs),
or API reference documentation. Those require separate builders.

**Naming space**: All artifacts occupy `p05_cg_*.md` within `P05_output/`.

---

## Pillar Coverage

| Pillar | ISO | Purpose |
|--------|-----|---------|
| P01 Knowledge | knowledge_card | Domain knowledge injection: DCO/CLA, Conventional Commits, GitHub workflows |
| P03 Prompt | instruction, system_prompt | Persona and reasoning protocol |
| P04 Tools | tools | Production and validation tools |
| P05 Output | manifest, output_template | Primary artifact production |
| P06 Schema | schema | Structural constraints and ID pattern |
| P07 Evaluation | examples | Quality calibration |
| P08 Architecture | architecture | This file |
| P09 Config | config | Runtime settings |
| P10 Memory | memory | Learning and pattern retention |
| P11 Feedback | quality_gate | Quality enforcement |
| P12 Orchestration | collaboration | Cross-team handoffs |
