---  
id: p02_agent_pet_shop_crm  
kind: agent  
pillar: P02  
title: Pet Shop CRM Agent  
version: "1.0.0"  
created: "2023-10-15"  
updated: "2023-10-15"  
author: "user"  
agent_group: "P02"  
domain: "pet shop customer relationship management"  
llm_function: BECOME  
capabilities_count: 6  
tools_count: 4  
iso_files_count: 10  
routing_keywords: ["pet shop", "customer", "appointment", "sales"]  
quality: null
tags: [agent, pet shop, P02, CRM]  
tldr: "A CRM tool for managing pet shop customer data, pet records, appointments, and sales transactions."  
density_score: 0.85  
linked_artifacts:  
  primary: "[[p02_agent_pet_shop_crm]]"  
  related: ["[[bld_instruction_boot_config]]", "[[p01_kc_agent]]"]  
---  
## Overview  
The **Pet Shop CRM Agent** is a P02 specialist in pet shop customer relationship management. It streamlines customer data tracking, pet records, appointment scheduling, and sales processing to enhance operational efficiency.  

## Capabilities  
- Manages customer profiles and purchase history  
- Tracks pet medical records and vaccination schedules  
- Schedules and reminders for vet appointments  
- Processes sales transactions and inventory updates  
- Generates monthly sales reports and customer insights  
- Sends automated follow-ups for service reminders  

## Tools  
| # | Tool | Purpose |  
|---|---|---|  
| 1 | MCP Server | Handles real-time data synchronization across systems |  
| 2 | Appointment Scheduler Script | Automates booking and reminder notifications |  
| 3 | Payment Gateway API | Processes transactions securely |  
| 4 | Customer Data Export Tool | Generates downloadable reports for analysis |  

## Agent_group Position  
- Agent_group: **P02**  
- Peers: **[p02_agent_pet_ownership]**, **[p02_agent_vet_services]**  
- Upstream: **[p01_kc_agent]**  
- Downstream: **[p11_qg_agent]**  

## File Structure  
```
agents/p02_agent_pet_shop_crm/  
  agent_package/  
    SPEC_P02_AGENT_PET_SHOP_CRM_001_MANIFEST.md  
    SPEC_P02_AGENT_PET_SHOP_CRM_002_QUICK_START.md  
    SPEC_P02_AGENT_PET_SHOP_CRM_003_PRIME.md  
    SPEC_P02_AGENT_PET_SHOP_CRM_004_INSTRUCTIONS.md  
    SPEC_P02_AGENT_PET_SHOP_CRM_005_ARCHITECTURE.md  
    SPEC_P02_AGENT_PET_SHOP_CRM_006_OUTPUT_TEMPLATE.md  
    SPEC_P02_AGENT_PET_SHOP_CRM_007_EXAMPLES.md  
    SPEC_P02_AGENT_PET_SHOP_CRM_008_ERROR_HANDLING.md  
    SPEC_P02_AGENT_PET_SHOP_CRM_009_UPLOAD_KIT.md  
    SPEC_P02_AGENT_PET_SHOP_CRM_010_SYSTEM_INSTRUCTION.md  
```  

## Routing  
- Triggers: "manage customer data", "schedule pet appointment", "process sale", "generate report"  
- Keywords: **pet shop**, **customer**, **appointment**, **sales**  
- NOT when: "inventory management", "marketing campaigns", "financial auditing"  

## Input / Output  
### Input  
- Required: **customer ID**, **pet details**, **appointment date**, **transaction data**  
- Optional: **custom reminder preferences**  
### Output  
- Primary: **customer profile update**, **appointment confirmation**, **sales receipt**  
- Secondary: **monthly sales summary**, **pet health alert**  

## Quality Gates  
HARD gates: YAML parses, id matches p02_agent_ pattern, kind == agent, quality == null, required fields present, agent_package >= 10 files, llm_function == BECOME.  
SOFT gates: tldr <= 160ch, tags >= 3, capabilities_count matches body, density >= 0.80, agent_group assigned, domain specific.  

## Footer  
version: "1.0.0" | author: "user" | quality: null