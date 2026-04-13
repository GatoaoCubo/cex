---
kind: architecture
id: bld_architecture_vad_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of vad_config -- inventory, dependencies
quality: null
title: "Architecture Vad Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [vad_config, builder, architecture]
tldr: "Component map of vad_config -- inventory, dependencies"
domain: "vad_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Component Inventory  
| Name | Role | Owner | Status |  
|------|------|-------|--------|  
| Config Validator | Validates VAD schema integrity | DevOps | Active |  
| Builder Engine | Generates configuration files | Engineering | Active |  
| Schema Manager | Maintains versioned schema definitions | QA | Active |  
| Version Controller | Tracks config history and rollbacks | DevOps | Active |  
| Deployment Interface | Integrates with CEX deployment pipelines | Deployment | Active |  
| Audit Logger | Records config changes for compliance | Security | Active |  
| Dependency Resolver | Manages external config references | Engineering | Under Review |  

## Dependencies  
| From | To | Type |  
|------|----|------|  
| Builder Engine | Schema Manager | Data |  
| Config Validator | Builder Engine | Validation |  
| Deployment Interface | Version Controller | Control |  
| Audit Logger | Config Validator | Logging |  
| Dependency Resolver | Builder Engine | Reference |  

## Architectural Position  
vad_config resides in the audio preprocessing layer of the CEX ecosystem, defining detection thresholds and sensitivity settings that gate audio into downstream STT providers. It acts as the first filter in voice pipelines -- separating speech from silence/noise -- and interfaces with stt_provider_builder (downstream consumer) and voice_pipeline_builder (orchestrator) while enforcing P09 configuration standards.
