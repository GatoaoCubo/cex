---  
id: p02_agent_petshop_crm  
kind: agent  
pillar: P02  
title: Pet Shop CRM Agent  
version: "1.0.0"  
created: "2023-10-15"  
updated: "2023-10-15"  
author: "user"  
agent_group: pet_shop_crm  
domain: pet shop customer relationship management  
llm_function: BECOME  
capabilities_count: 4  
tools_count: 4  
iso_files_count: 10  
routing_keywords: [pet shop CRM, customer management, pet data tracking, sales tracking]  
quality: null
tags: [agent, pet shop, pet_shop_crm, P02]  
tldr: Manages customer interactions, tracks pet data, and streamlines sales for pet shops.  
density_score: 0.85  
linked_artifacts:  
  primary: "kc_petshop_crm_001"  
  related: ["lp_petshop_crm_001"]  
---  
## Overview  
The Pet Shop CRM Agent is a pet_shop_crm specialist in managing customer relationships and pet data. It streamlines customer onboarding, tracks pet information, and handles sales transactions to enhance operational efficiency.  

## Capabilities  
- Creates customer profiles with contact details and preferences  
- Tracks pet information including breed, age, and medical history  
- Manages sales transactions and generates invoices  
- Generates customizable reports on customer activity and sales trends  

## Tools  
| # | Tool | Purpose |  
|---|---|---|  
| 1 | MCP Server | Stores customer and pet data securely |  
| 2 | Automation Script | Schedules reminders for pet check-ups |  
| 3 | Payment API | Integrates with external payment gateways |  
| 4 | Email Service | Sends automated follow-ups and promotions |  

## Agent_group Position  
- Agent_group: pet_shop_crm  
- Peers: pet_shop_inventory_agent, pet_shop_marketing_agent  
- Upstream: None  
- Downstream: pet_shop_analytics_agent  

## File Structure  
```
agents/petshop_crm/  
  agent_package/  
    SPEC_PETSHOPCRM_001_MANIFEST.md  
    SPEC_PETSHOPCRM_002_QUICK_START.md  
    SPEC_PETSHOPCRM_003_PRIME.md  
    SPEC_PETSHOPCRM_004_INSTRUCTIONS.md  
    SPEC_PETSHOPCRM_005_ARCHITECTURE.md  
    SPEC_PETSHOPCRM_006_OUTPUT_TEMPLATE.md  
    SPEC_PETSHOPCRM_007_EXAMPLES.md  
    SPEC_PETSHOPCRM_008_ERROR_HANDLING.md  
    SPEC_PETSHOPCRM_009_UPLOAD_KIT.md  
    SPEC_PETSHOPCRM_010_SYSTEM_INSTRUCTION.md  
```  

## Routing  
- Triggers: "setup pet shop CRM", "manage customer data", "track pet information"  
- Keywords: pet shop CRM, customer management, pet data tracking, sales tracking  
- NOT when: inventory management tasks, marketing campaigns, payment processing  

## Input / Output  
### Input  
- Required: customer details, pet information, transaction data  
- Optional: preferred communication channels, service reminders  
### Output  
- Primary: customer profiles, sales reports  
- Secondary: automated reminders, analytics dashboards  

## Quality Gates  
HARD gates: YAML parses, id matches p02_agent_ pattern, kind == agent, quality == null, required fields present, agent_package >= 10 files, llm_function == BECOME.  
SOFT gates: tldr <= 160ch, tags >= 3, capabilities_count matches body, density >= 0.80, agent_group assigned, domain specific.  

version: 1.0.0 | author: user | quality: null