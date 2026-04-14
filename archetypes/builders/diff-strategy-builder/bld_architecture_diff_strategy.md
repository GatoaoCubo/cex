---
kind: architecture
id: bld_architecture_diff_strategy
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of diff_strategy -- inventory, dependencies
quality: null
title: "Architecture Diff Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [diff_strategy, builder, architecture]
tldr: "Component map of diff_strategy -- inventory, dependencies"
domain: "diff_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Component Inventory
| Name | Role | Owner | Status |
| :--- | :--- | :--- | :--- |
| Logic Core | Strategy generation | Quant | Active |
| Param Store | Config management | DevOps | Active |
| Data Ingest | Market feed sync | Data Eng | Beta |
| Risk Validator | Constraint checking | Risk | Active |
| Output Adapter | Signal formatting | Core | Active |
| Monitor | Health tracking | SRE | Active |

## Dependencies
| From | To | Type |
| :--- | :--- | :--- |
| Builder | Market Data API | Inbound |
| Builder | Risk Engine | Validation |
| Builder | Config DB | State |
| Builder | Execution Engine | Downstream |

## Architectural Position
The diff_strategy-builder acts as a middle-tier orchestration layer within the CEX ecosystem. It sits between raw market data ingestion and the downstream execution engine, transforming price discrepancies and volatility signals into actionable, risk-validated trading instructions.
