---
kind: collaboration
id: bld_collaboration_roi_calculator
pillar: P12
llm_function: COLLABORATE
purpose: How roi_calculator-builder works in crews with other builders
quality: 8.9
title: "Collaboration Roi Calculator"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [roi_calculator, builder, collaboration]
tldr: "How roi_calculator-builder works in crews with other builders"
domain: "roi_calculator construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Calculates ROI metrics using investment, revenue, and time-frame inputs. Translates raw data into actionable ROI insights for decision-making.  

## Receives From  
| Builder       | What                  | Format     |  
|---------------|-----------------------|------------|  
| data_collector| Investment data       | JSON       |  
| revenue_tracker| Revenue figures      | CSV        |  
| time_frame_provider| Time period       | API call   |  

## Produces For  
| Builder       | What                  | Format     |  
|---------------|-----------------------|------------|  
| reporting     | ROI summary report    | PDF        |  
| dashboard     | Visual ROI metrics    | API call   |  
| analytics     | ROI dataset           | JSON       |  

## Boundary  
Does NOT handle cost budgeting (ops team) or actual usage tracking (usage_report module).
