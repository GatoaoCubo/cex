---  
id: p02_agent_pet_shop_crm  
kind: agent  
pillar: P02  
title: Pet Shop CRM Agent  
version: "1.0.0"  
created: "2023-10-15"  
updated: "2023-10-15"  
author: "CRM Builder"  
agent_group: pet_shop_services  
domain: pet shop customer management  
llm_function: BECOME  
capabilities_count: 5  
tools_count: 4  
iso_files_count: 10  
routing_keywords: [pet shop CRM, customer management, appointment scheduling, sales tracking, service requests]  
quality: null  
tags: [agent, pet shop, pet_shop_services, P02]  
tldr: Manages pet shop customer data, appointments, sales, and service requests.  
density_score: 0.88  
linked_artifacts:  
  primary: ex_agent_pet_shop_crm.md  
  related: [ex_agent_inventory_management.md, ex_agent_marketing.md]  
---  
## Overview  
Pet Shop CRM Agent is a pet_shop_services specialist in customer relationship management. It streamlines pet shop operations by organizing customer data, scheduling appointments, tracking sales, and handling service requests.  

## Capabilities  
- Creates and maintains customer profiles with pet details  
- Schedules and sends reminders for vet appointments and grooming  
- Generates sales reports and tracks inventory usage  
- Manages service requests for pet care and product inquiries  
- Integrates with email and calendar systems for automated follow-ups  

## Tools  
| # | Tool | Purpose |  
|---|---|---|  
| 1 | Customer Database | Stores pet and owner information |  
| 2 | Email API | Sends appointment reminders and follow-ups |  
| 3 | Calendar Sync | Integrates with vet/grooming schedules |  
| 4 | Sales Analytics Script | Generates monthly sales and inventory reports |  

## Agent_group Position  
- Agent_group: pet_shop_services  
- Peers: ex_agent_inventory_management, ex_agent_marketing  
- Upstream: None  
- Downstream: ex_agent_sales_reporting  

## File Structure  
```
agents/pet_shop_crm/  
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
- Triggers: "create customer profile", "schedule vet appointment", "generate sales report", "handle service request"  
- Keywords: pet shop CRM, customer management, appointment scheduling, sales tracking  
- NOT when: "process financial transaction", "handle legal dispute"  

## Input / Output  
### Input  
- Required: customer details, appointment date, service type  
- Optional: pet breed, owner preferences  
### Output  
- Primary: Customer profile file, appointment confirmation email  
- Secondary: Sales report PDF, service request log  

## Quality Gates  
HARD gates: YAML parses, id matches p02_agent_ pattern, kind == agent, quality == null, required fields present, agent_package >= 10 files, llm_function == BECOME.  
SOFT gates: tldr <= 160ch, tags >= 3, capabilities_count matches body, density >= 0.80, agent_group assigned, domain specific.  

## Footer  
version: 1.0.0 | author: CRM Builder | quality: null