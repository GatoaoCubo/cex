---

id: p12_dr_engineering
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2023-10-05
updated: 2023-10-05
author: dispatch_rule_builder
domain: engineering
quality: null
tags: [dispatch, engineering, apollo]
tldr: Route engineering tasks like calibration and failure analysis to engineering satellite
scope: engineering
keywords: [calibrar, calibrate, revisão de design, design review, análise de falhas, failure analysis, construção, build, manutenção, maintenance]
satellite: apollo
model: opus
priority: 8
confidence_threshold: 0.70
fallback: atlas

---

# Engineering Dispatch Rule

## Purpose
This rule routes tasks related to engineering activities, such as calibration, design review, and failure analysis, to the Apollo satellite, ensuring that engineering operations are handled efficiently.

## Keyword Rationale
Keywords are selected to trigger on commonly used terms in both Portuguese and English within the engineering domain. This includes essential engineering tasks such as "calibrate," "design review," and "failure analysis."

## Fallback Logic
When the confidence of keyword matching falls below the set threshold or if the Apollo satellite is unavailable, tasks default to the Atlas satellite to ensure continuity and task completion.