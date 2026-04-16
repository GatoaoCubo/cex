---
kind: instruction
id: bld_instruction_white_label_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for white_label_config
quality: 8.8
title: "Instruction White Label Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [white_label_config, builder, instruction]
tldr: "Step-by-step production process for white_label_config"
domain: "white_label_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify branding requirements (logos, color codes, legal disclaimers).  
2. Map reseller-specific constraints (custom domain limits, API rate caps).  
3. Audit compliance needs (data residency, GDPR/CCPA alignment).  
4. Document stakeholder input (marketing, legal, engineering teams).  
5. Analyze competitor configurations for feature parity benchmarks.  
6. Validate technical feasibility (infrastructure, CMS, analytics tooling).  

## Phase 2: COMPOSE  
1. Set up working directory with SCHEMA.md and OUTPUT_TEMPLATE.md.  
2. Define configuration schema (JSON/YAML structure, required fields).  
3. Map reseller-specific parameters to schema (e.g., `branding.logo_url`).  
4. Populate default values from OUTPUT_TEMPLATE.md placeholders.  
5. Apply constraints (e.g., `max_domains_per_reseller: 5`).  
6. Cross-reference schema with legal/compliance requirements.  
7. Generate artifact using template engine (Jinja2, Mustache).  
8. Embed versioning metadata (artifact version, last updated).  
9. Export as `.yaml` with checksum for integrity verification.  

## Phase 3: VALIDATE  
- [ ] Schema matches SCHEMA.md (using JSON Schema validator).  
- [ ] All constraints enforced (e.g., domain limits, branding rules).  
- [ ] Output conforms to OUTPUT_TEMPLATE.md structure.  
- [ ] Legal/compliance team approves final artifact.  
- [ ] Stakeholders confirm alignment with reseller agreements.
