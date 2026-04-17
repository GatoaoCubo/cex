---
id: kc_nucleus_def
kind: knowledge_card
title: CEX Nucleus Definition (N00-N07)
version: 1.0.0
quality: 8.9
pillar: P01
density_score: 1.0
---

# CEX Nucleus Definition (N00-N07)

A CEX nucleus is a specialized functional unit in the CEX architecture, operating as a fractal component with defined roles, responsibilities, and interdependencies. Each nucleus embodies a specific domain of expertise, with explicit ownership of 12 pillars and 8F pipeline integration.

## Nucleus Definitions

### N00 - Genesis
- **Role**: System originator and archetype generator
- **Pillars Owned**: All 12 pillars (P01-P12)
- **Sin Lens**: None (root node)
- **CLI Binding**: `boot/cex.ps1`
- **Model Tier**: Opus
- **Boot Script**: `boot/cex.ps1`
- **Agent Card Path**: `N00_genesis/`
- **Crew Templates Exposed**: All
- **Domain Agents**: N01-N07

### N01 - Analyst
- **Role**: Research & analysis
- **Pillars Owned**: P01 (Intelligence), P02 (Discovery)
- **Sin Lens**: Truth-seeking
- **CLI Binding**: `bash _spawn/dispatch.sh n01`
- **Model Tier**: Sonnet
- **Boot Script**: `boot/n01.ps1`
- **Agent Card Path**: `N01_intelligence/`
- **Crew Templates Exposed**: P01, P02
- **Domain Agents**: N01, N02, N04

### N02 - Copywriter
- **Role**: Marketing & communication
- **Pillars Owned**: P03 (Prompts), P04 (Documentation)
- **Sin Lens**: Persuasion
- **CLI Binding**: `bash _spawn/dispatch.sh n02`
- **Model Tier**: Sonnet
- **Boot Script**: `boot/n02.ps1`
- **Agent Card Path**: `N02_comms/`
- **Crew Templates Exposed**: P03, P04
- **Domain Agents**: N02, N03, N06

### N03 - Builder
- **Role**: Artifact creation
- **Pillars Owned**: P05 (Code), P06 (Testing)
- **Sin Lens**: Innovation
- **CLI Binding**: `bash _spawn/dispatch.sh n03`
- **Model Tier**: Opus
- **Boot Script**: `boot/n03.ps1`
- **Agent Card Path**: `N03_builder/`
- **Crew Templates Exposed**: P05, P06
- **Domain Agents**: N03, N05, N07

### N04 - Librarian
- **Role**: Knowledge management
- **Pillars Owned**: P07 (Taxonomy), P08 (Audit)
- **Sin Lens**: Accuracy
- **CLI Binding**: `bash _spawn/dispatch.sh n04`
- **Model Tier**: Sonnet
- **Boot Script**: `boot/n04.ps1`
- **Agent Card Path**: `N04_knowledge/`
- **Crew Templates Exposed**: P07, P08
- **Domain Agents**: N04, N01, N02

### N05 - Operator
- **Role**: Code execution
- **Pillars Owned**: P09 (Deployment), P10 (Monitoring)
- **Sin Lens**: Reliability
- **CLI Binding**: `bash _spawn/dispatch.sh n05`
- **Model Tier**: Sonnet
- **Boot Script**: `boot/n05.ps1`
- **Agent Card Path**: `N05_operations/`
- **Crew Templates Exposed**: P09, P10
- **Domain Agents**: N05, N03, N07

### N06 - Strategist
- **Role**: Business optimization
- **Pillars Owned**: P11 (Monetization), P12 (Sustainability)
- **Sin Lens**: Profitability
- **CLI Binding**: `bash _spawn/dispatch.sh n06`
- **Model Tier**: Sonnet
- **Boot Script**: `boot/n06.ps1`
- **Agent Card Path**: `N06_strategy/`
- **Crew Templates Exposed**: P11, P12
- **Domain Agents**: N06, N02, N07

### N07 - Orchestrator
- **Role**: System coordination
- **Pillars Owned**: All 12 pillars (P01-P12)
- **Sin Lens**: Systemic harmony
- **CLI Binding**: `bash _spawn/dispatch.sh n07`
- **Model Tier**: Opus
- **Boot Script**: `boot/n07.ps1`
- **Agent Card Path**: `N07_orchestrator/`
- **Crew Templates Exposed**: All
- **Domain Agents**: N00-N06
```