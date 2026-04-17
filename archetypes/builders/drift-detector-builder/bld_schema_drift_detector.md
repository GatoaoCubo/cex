---
kind: schema
id: bld_schema_drift_detector
pillar: P11
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for drift_detector
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 8.3
title: "Schema Drift Detector"
version: "1.0.0"
author: n03_builder
tags: [drift_detector, builder, schema]
tldr: "Frontmatter + body schema for drift_detector: detection_method, thresholds, window_config, alert_rule."
domain: "drift detector construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Schema: drift_detector

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p11_dd_{slug}) | YES | - | Namespace compliance |
| kind | literal "drift_detector" | YES | - | Type integrity |
| pillar | literal "P11" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| detection_method | enum: psi, ks, chi_square, js_divergence, embedding_distance, custom | YES | - | Statistical test |
| threshold | {warning: float, critical: float} | YES | - | Drift severity levels |
| features_monitored | list[string] | YES | - | Input/output dimensions |
| alert_rule | {destination, frequency} | YES | - | Alert routing |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "drift_detector" |
| tldr | string <= 160ch | YES | - | Dense summary |
| window_config | {reference, production} | REC | - | Baseline and comparison windows |
| platform | string | REC | - | Evidently, Arize, Whylogs, custom |
| drift_type | enum: data, concept, prediction, behavioral | REC | - | Type of drift being detected |
| enabled | bool | REC | true | Active/inactive state |
| sampling_rate | float 0.0-1.0 | REC | 1.0 | Fraction of traffic to sample |

## ID Pattern
Regex: `^p11_dd_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Overview` -- what this detector monitors, why, and when it fires
2. `## Detection Method` -- statistical test parameters and rationale
3. `## Window Config` -- reference and production window specifications
4. `## Thresholds` -- warning/critical levels with calibration rationale
5. `## Alert Rule` -- destination, frequency, suppression policy

## Constraints
- max_bytes: 3072 (monitor config is compact)
- naming: p11_dd_{scope}.md
- machine_format: yaml (compiled artifact)
- id == filename stem
- detection_method MUST be declared
- threshold MUST have at least one level
- features_monitored MUST be non-empty list
- quality: null always
