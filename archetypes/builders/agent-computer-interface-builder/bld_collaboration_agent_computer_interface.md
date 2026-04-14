---
kind: collaboration
id: bld_collaboration_agent_computer_interface
pillar: P12
llm_function: COLLABORATE
purpose: How agent_computer_interface-builder works in crews with other builders
quality: null
title: "Collaboration Agent Computer Interface"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_computer_interface, builder, collaboration]
tldr: "How agent_computer_interface-builder works in crews with other builders"
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role
Architects the structured communication protocol and schema that enables an agent to interact with a specific software environment via defined commands and state updates.

## Receives From
| Builder | What | Format |
| :--- | :--- | :--- |
| System Architect | System capabilities | JSON/Spec |
| Domain Expert | Functional requirements | Markdown |
| Security Auditor | Access constraints | YAML/Policy |

## Produces For
| Builder | What | Format |
| :--- | :--- | :--- |
| Agent Developer | Interface definition | OpenAPI/Schema |
| Integration Engineer | Implementation glue | Python/TS |
| Testing Agent | Mock response sets | JSON/CSV |

## Boundary
Does NOT perform web automation or DOM scraping (handled by browser_tool).
Does NOT perform visual/pixel-based screen control (handled by computer_use).
Does NOT implement the underlying business logic (handled by domain_logic_agent).
