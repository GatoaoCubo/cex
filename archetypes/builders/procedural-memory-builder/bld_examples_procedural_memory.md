---
kind: examples
id: bld_examples_procedural_memory
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of procedural_memory artifacts
quality: null
title: "Examples Procedural Memory"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [procedural_memory, builder, examples]
tldr: "Golden and anti-examples of procedural_memory artifacts"
domain: "procedural_memory construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example  
```yaml  
cex_kind: procedural_memory  
name: "Microsoft Power Automate Flow for Invoice Processing"  
description: "Automates invoice data extraction and accounting entry creation."  
body:  
  - trigger: "Email received in 'Invoices' folder"  
  - action: "Extract PDF text using Azure Cognitive Services"  
  - action: "Parse structured data with Power Automate's AI Builder"  
  - action: "Create accounting entry in Dynamics 365"  
  - validation: "Send confirmation email with parsed data summary"  
```  

## Anti-Example 1: Confusing with declarative knowledge  
```yaml  
cex_kind: procedural_memory  
name: "Salesforce Object Schema"  
description: "Stores CRM entity definitions and field relationships."  
body:  
  - entity: "Account"  
  - fields: "Name, Industry, Revenue"  
  - relationships: "Account -> Contact (one-to-many)"  
```  
## Why it fails  
Stores static entity definitions (declarative knowledge), not procedures or skills. Violates boundary by focusing on entity_memory.  

## Anti-Example 2: Vague, unstructured steps  
```yaml  
cex_kind: procedural_memory  
name: "Generic Task Management"  
description: "Tracks user tasks without defined workflows."  
body:  
  - step: "User adds task"  
  - step: "System assigns task"  
  - step: "Task completed"  
```  
## Why it fails  
Lacks specificity in actions, tools, or validation. No concrete procedures or automation logic, making retrieval ineffective.
