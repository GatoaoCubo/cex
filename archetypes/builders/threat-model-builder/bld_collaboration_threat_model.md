---
kind: collaboration
id: bld_collaboration_threat_model
pillar: P12
llm_function: COLLABORATE
purpose: How threat_model-builder works in crews with other builders
quality: 8.9
title: "Collaboration Threat Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [threat_model, builder, collaboration]
tldr: "How threat_model-builder works in crews with other builders"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role  

This ISO records a threat model: the assets worth protecting and the attacker profiles that target them.
Identifies potential threats, maps attack vectors, and models risk scenarios to inform security design and mitigation strategies.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| System Design | Architecture diagrams | JSON        |  
| Compliance    | Regulatory requirements | CSV         |  
| Threat Intel  | External threat data  | API         |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Security Team | Threat model          | JSON        |  
| Risk Team     | Risk assessment       | Markdown    |  
| Design Team   | Mitigation roadmap    | Custom      |  

## Boundary  
Does NOT enforce safety policies (handled by safety_policy) or implement runtime filters (handled by guardrail). Focuses solely on pre-deployment threat/risk analysis.
