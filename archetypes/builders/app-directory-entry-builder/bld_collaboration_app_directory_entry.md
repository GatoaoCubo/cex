---
kind: collaboration
id: bld_collaboration_app_directory_entry
pillar: P12
llm_function: COLLABORATE
purpose: How app_directory_entry-builder works in crews with other builders
quality: 8.9
title: "Collaboration App Directory Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [app_directory_entry, builder, collaboration]
tldr: "How app_directory_entry-builder works in crews with other builders"
domain: "app_directory_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Constructs and validates app directory entries, ensuring metadata consistency, format compliance, and readiness for public listing.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| App Dev       | App metadata          | JSON        |  
| QA Team       | Validation results    | CSV         |  
| CMS           | Marketing content     | Markdown    |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| App Directory | Entry ready for listing | JSON        |  
| Analytics     | Usage stats           | CSV         |  
| API Gateway   | API spec              | YAML        |  

## Boundary  
Does NOT handle marketplace app manifests (handled by `marketplace_app_manifest-builder`) or partner listings (handled by `partner_listing-builder`). Sales, pricing, and distribution are managed by the sales team, not this builder.
