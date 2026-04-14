---
id: kc_nucleus_def
kind: knowledge_card
title: Nucleus Definition (N00-N07)
version: 1.0.0
quality: null
pillar: P01
---

# CEX Nucleus Definition (N00-N07)

A CEX nucleus is a self-contained, fractal component of the system with:

## Nucleus Specifications
- **N00 Genesis**:  
  - role: System originator  
  - pillars_owned: All 12 pillars  
  - sin_lens: Archetypal patterns  
  - cli_binding: `boot/cex.ps1`  
  - model_tier: Opus  
  - boot_script: `boot/n00.ps1`  
  - agent_card_path: `N00_genesis/`  
  - crew_templates_exposed: 12  
  - domain_agents: N01-N07

- **N01 Analyst**:  
  - role: Research/analysis  
  - pillars_owned: P01-P03  
  - sin_lens: Evidence-based reasoning  
  - cli_binding: `dispatch.sh n01`  
  - model_tier: Sonnet  
  - boot_script: `boot/n01.ps1`  
  - agent_card_path: `N01_intelligence/`  
  - crew_templates_exposed: 3  
  - domain_agents: N01, N04, N05

- **N02 Copywriter**:  
  - role: Marketing/communication  
  - pillars_owned: P04-P06  
  - sin_lens: Audience alignment  
  - cli_binding: `dispatch.sh n02`  
  - model_tier: Sonnet  
  - boot_script: `boot/n02.ps1`  
  - agent_card_path: `N02_comms/`  
  - crew_templates_exposed: 2  
  - domain_agents: N02, N06

- **N03 Builder**:  
  - role: Artifact creation  
  - pillars_owned: P07-P09  
  - sin_lens: ISO compliance  
  - cli_binding: `dispatch.sh n03`  
  - model_tier: Opus  
  - boot_script: `boot/n03.ps1`  
  - agent_card_path: `N03_builder/`  
  - crew_templates_exposed: 5  
  - domain_agents: N03, N05, N07

- **N04 Librarian**:  
  - role: Knowledge management  
  - pillars_owned: P10-P12  
  - sin_lens: Taxonomy integrity  
  - cli_binding: `dispatch.sh n04`  
  - model_tier: Sonnet  
  - boot_script: `boot/n04.ps1`  
  - agent_card_path: `N04_knowledge/`  
  - crew_templates_exposed: 4  
  - domain_agents: N04, N01

- **N05 Operator**:  
  - role: Code/test/deploy  
  - pillars_owned: P13-P15  
  - sin_lens: Execution fidelity  
  - cli_binding: `dispatch.sh n05`  
  - model_tier: Sonnet  
  - boot_script: `boot/n05.ps1`  
  - agent_card_path: `N05_operations/`  
  - crew_templates_exposed: 3  
  - domain_agents: N05, N03

- **N06 Strategist**:  
  - role: Brand monetization  
  - pillars_owned: P16-P18  
  - sin_lens: ROI optimization  
  - cli_binding: `dispatch.sh n06`  
  - model_tier: Sonnet  
  - boot_script: `boot/n06.ps1`  
  - agent_card_path: `N06_monetization/`  
  - crew_templates_exposed: 2  
  - domain_agents: N06, N02

- **N07 Orchestrator**:  
  - role: System coordination  
  - pillars_owned: All 18 pillars  
  - sin_lens: Workflow optimization  
  - cli_binding: `dispatch.sh n07`  
  - model_tier: Opus  
  - boot_script: `boot/n07.ps1`  
  - agent_card_path: `N07_orchestrator/`  
  - crew_templates_exposed: 6  
  - domain_agents: N00-N06
```