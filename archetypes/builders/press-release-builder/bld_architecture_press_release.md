---
kind: architecture
id: bld_architecture_press_release
pillar: P08
llm_function: CONSTRAIN
purpose: Component inventory, dependency map, and architectural position of the press_release builder
quality: 9.1
title: "Press Release Builder Architecture"
version: "1.0.0"
author: n02_wave6
tags: [press_release, builder, architecture]
tldr: "13-ISO builder architecture for press_release; serves as earned media production unit within CEX P05"
domain: "press_release construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_contributor_guide
  - bld_architecture_dataset_card
  - bld_architecture_legal_vertical
  - bld_architecture_fintech_vertical
  - bld_architecture_experiment_tracker
  - bld_architecture_webinar_script
  - bld_architecture_healthcare_vertical
  - bld_architecture_conformity_assessment
  - bld_architecture_app_directory_entry
  - bld_knowledge_card_kind
---

## Component Inventory

| ISO | File | Kind | Pillar | llm_function | Status |
|---|---|---|---|---|---|
| Manifest | bld_manifest_press_release.md | type_builder | P05 | BECOME | active |
| Instruction | bld_instruction_press_release.md | instruction | P03 | REASON | active |
| System Prompt | bld_system_prompt_press_release.md | system_prompt | P03 | BECOME | active |
| Schema | bld_schema_press_release.md | schema | P06 | CONSTRAIN | active |
| Quality Gate | bld_quality_gate_press_release.md | quality_gate | P11 | GOVERN | active |
| Output Template | bld_output_template_press_release.md | output_template | P05 | PRODUCE | active |
| Examples | bld_examples_press_release.md | examples | P07 | GOVERN | active |
| Knowledge Card | bld_knowledge_card_press_release.md | knowledge_card | P01 | INJECT | active |
| Architecture | bld_architecture_press_release.md | architecture | P08 | CONSTRAIN | active |
| Collaboration | bld_collaboration_press_release.md | collaboration | P12 | COLLABORATE | active |
| Config | bld_config_press_release.md | config | P09 | CONSTRAIN | active |
| Memory | bld_memory_press_release.md | memory | P10 | INJECT | active |
| Tools | bld_tools_press_release.md | tools | P04 | CALL | active |

## Dependencies

| Component | Depends on | Dependency type |
|---|---|---|
| manifest | config | reads naming convention and path config |
| instruction | system_prompt | system_prompt defines persona instruction uses |
| output_template | schema | template fields must match schema frontmatter spec |
| quality_gate | examples | golden example calibrates soft scoring dimensions |
| collaboration | memory | past pickup rate data informs handoff decisions |
| tools | external wire API | PR Newswire and BusinessWire APIs for submission |
| knowledge_card | AP Stylebook | external authority for all style decisions |
| examples | quality_gate | golden threshold (9.5) determines exemplar eligibility |

## Architectural Position

The press_release builder is the earned media production unit within CEX Pillar
P05 (Output Artifacts). It occupies a specific zone in the CEX output layer:

```
P05 Output Layer
  |
  +-- press_release builder    <-- this builder
  |     Produces: wire-ready press releases
  |     Audience: journalists, newswire systems
  |     Format: AP-style Markdown, plain text for wire
  |
  +-- blog_post builder
  |     Produces: long-form editorial content
  |     Audience: blog readers, SEO
  |
  +-- pitch_deck builder
        Produces: visual slide decks
        Audience: investors, partners
```

## Data Flow

```
Brand Team / PR Agency
  |
  | (messaging brief, quotes, boilerplate, embargo date)
  v
press_release builder
  |
  |-- F1 CONSTRAIN: schema + config (kind, pillar, limits)
  |-- F2 BECOME: manifest + system_prompt (persona)
  |-- F3 INJECT: knowledge_card + examples + memory (context)
  |-- F4 REASON: instruction (research -> compose -> validate)
  |-- F5 CALL: tools (compile, score, AP checker)
  |-- F6 PRODUCE: output_template (wire-ready release)
  |-- F7 GOVERN: quality_gate (H01-H08 + D01-D05)
  |-- F8 COLLABORATE: collaboration (handoff to wire service)
  |
  v
Wire Service (PR Newswire / BusinessWire)
  |
  v
Journalist Inbox / Newsroom Database
```

## Pillar Coverage

| Pillar | ISOs | Purpose |
|---|---|---|
| P01 Knowledge | knowledge_card | Domain knowledge injection |
| P03 Prompt | instruction, system_prompt | Persona and reasoning protocol |
| P04 Tools | tools | Production and validation tools |
| P05 Output | manifest, output_template | Primary artifact production |
| P06 Schema | schema | Structural constraints |
| P07 Evaluation | examples | Quality calibration |
| P08 Architecture | architecture | This file |
| P09 Config | config | Runtime settings |
| P10 Memory | memory | Learning and pattern retention |
| P11 Feedback | quality_gate | Quality enforcement |
| P12 Orchestration | collaboration | Cross-team handoffs |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_contributor_guide]] | sibling | 0.53 |
| [[bld_architecture_dataset_card]] | sibling | 0.51 |
| [[bld_architecture_legal_vertical]] | sibling | 0.45 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.45 |
| [[bld_architecture_experiment_tracker]] | sibling | 0.44 |
| [[bld_architecture_webinar_script]] | sibling | 0.44 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.43 |
| [[bld_architecture_conformity_assessment]] | sibling | 0.41 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.39 |
| [[bld_knowledge_card_kind]] | upstream | 0.39 |
