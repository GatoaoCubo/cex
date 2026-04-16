---
kind: collaboration
id: bld_collaboration_partner_listing
pillar: P12
llm_function: COLLABORATE
purpose: How partner_listing-builder works in crews with other builders
quality: 8.9
title: "Collaboration Partner Listing"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [partner_listing, builder, collaboration]
tldr: "How partner_listing-builder works in crews with other builders"
domain: "partner_listing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Curates and standardizes partner listing content, ensuring compliance with brand guidelines and data accuracy.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| CRM System    | Partner data          | JSON        |  
| Designer      | Formatting guidelines | Markdown    |  
| Manager       | Approval status       | Boolean     |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Content Team  | Partner listing doc   | Markdown    |  
| Website Team  | Summary card          | HTML        |  
| Database      | Structured partner data| CSV         |  

## Boundary  
Does NOT handle case studies (handled by `case_study-builder`) or app directory entries (handled by `app_directory_entry-builder`). Legal reviews and compliance checks are managed by the Legal Team.
