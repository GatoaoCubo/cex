---
kind: config
id: bld_config_pitch_deck
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for pitch_deck production
quality: 8.6
title: "Config Pitch Deck"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [pitch_deck, builder, config]
tldr: "Naming, paths, limits for pitch_deck production"
domain: "pitch_deck construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention (pitch deck artifacts)
Pattern: p05_pd_<project_name>.md (e.g., p05_pd_innovateX.md, p05_pd_neuroFlow.md) for each pitch deck

## Paths
/artifacts/p05/pd/<project_name>/output.md

## Limits
max_bytes: 6144
max_turns: 5
effort_level: high

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
