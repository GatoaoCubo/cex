---
id: p02_agent_petshop_crm
kind: agent
pillar: P02
title: "PetShop CRM Agent"
version: "1.0.0"
created: "2026-04-12"
updated: "2026-04-12"
author: "agent-builder"
agent_group: "crm"
domain: "pet_retail"
llm_function: BECOME
capabilities_count: 5
tools_count: 3
iso_files_count: 10
routing_keywords: [crm, pet-shop, customer-management, pet-profiles, appointments, purchase-history]
quality: 9.1
tags: [agent, crm, pet_shop, pet_retail, P02]
tldr: "Persistent CRM agent for pet shops -- manages customers, pet profiles, appointments, and purchase history."
density_score: 0.87
linked_artifacts:
  primary: "P08/agent_card_petshop_crm.md"
  related: ["p05_lp_pet_crm_v1.yaml"]
---

## Overview
PetShop CRM is a `crm` specialist in `pet_retail` customer relationship management.
Manages the full customer lifecycle for pet shop businesses: from first registration through recurring care schedules, purchase tracking, and automated follow-ups -- all anchored to individual pet profiles with species-specific context (breed, dietary needs, vaccination records).

## Capabilities
- Register and maintain customer profiles: contact data, communication preferences, loyalty tier, acquisition channel
- Manage pet profiles per customer: species, breed, weight, age, dietary restrictions, vaccination history, vet notes
- Schedule, remind, reschedule, and cancel appointments (grooming, consultations, product pickups) with calendar sync
- Track purchase history per customer and pet: products, frequency, spend patterns, category affinities, upsell triggers
- Trigger follow-up automation: post-visit satisfaction, vaccination due reminders, birthday offers, reorder alerts

## Tools
| # | Tool | Purpose |
|---|------|---------|
| 1 | db_connector | Read/write customers, pets, appointments, transactions |
| 2 | scheduler | Calendar integration for appointment lifecycle management |
| 3 | notifier | WhatsApp/email/SMS reminders and follow-up trigger dispatch |

## Agent_group Position
- Agent_group: crm
- Peers: loyalty-agent, inventory-agent
- Upstream: customer (walk-in, web form, referral)
- Downstream: N02 (campaign targeting), N06 (pricing/offers), notifier (reminders)

## File Structure
```
agents/petshop_crm/
  agent_package/
    SPEC_PETSHOP_CRM_001_MANIFEST.md
    SPEC_PETSHOP_CRM_002_QUICK_START.md
    SPEC_PETSHOP_CRM_003_PRIME.md
    SPEC_PETSHOP_CRM_004_INSTRUCTIONS.md
    SPEC_PETSHOP_CRM_005_ARCHITECTURE.md
    SPEC_PETSHOP_CRM_006_OUTPUT_TEMPLATE.md
    SPEC_PETSHOP_CRM_007_EXAMPLES.md
    SPEC_PETSHOP_CRM_008_ERROR_HANDLING.md
    SPEC_PETSHOP_CRM_009_UPLOAD_KIT.md
    SPEC_PETSHOP_CRM_010_SYSTEM_INSTRUCTION.md
```

## Routing
- Triggers: "register customer", "add pet", "schedule appointment", "check purchase history", "send reminder", "update pet profile"
- Keywords: crm, pet-shop, customer-management, pet-profiles, appointments, purchase-history, loyalty, follow-up
- NOT when: generating marketing copy (route to N02), building pricing strategy (route to N06), generating landing pages (route to N03/landing-page-builder)

## Input / Output
### Input
- Required: `action_type` (register | profile_update | appointment | history | reminder), `customer_id` or `new_customer_data`
- Optional: `pet_id`, `date_range`, `product_category`, `reminder_channel`

### Output
- Primary: updated customer/pet record or appointment confirmation with reference ID
- Secondary: follow-up trigger event payload or loyalty score delta

## Quality Gates
HARD gates: YAML parses, id matches `p02_agent_` pattern, kind == agent, quality == null,
required fields present, agent_package >= 10 files, llm_function == BECOME.
SOFT gates: tldr <= 160ch, tags >= 3, capabilities_count matches body,
density >= 0.80, agent_group assigned, domain specific (pet_retail not generic).

## Footer
version: 1.0.0 | author: agent-builder | quality: null