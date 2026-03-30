---
id: p08_pat_builder_construction
kind: pattern
pillar: P08
title: Pattern -- Builder Construction
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [pattern, builder, N03]
tldr: 3 construction patterns -- direct build, crew composition, nucleus bootstrap.
density_score: 0.88
---

# Pattern: Builder Construction

## P1: Direct Build (Single Kind)

Most common. One intent, one kind, one artifact.
Intent > Motor > Kind > 8F Pipeline > Artifact
When: explicit kind request, examples available.
Model: sonnet default. Time: 10-60s.

## P2: Crew Composition (Multi-Kind)

Intent requires multiple related artifacts in dependency order.
Intent > Motor > [Kind1, Kind2, Kind3] > Select crew > Build sequentially
When: build agent end-to-end (agent + SP + boot_config + ...).
Model: opus. Time: 2-10 min.

## P3: Nucleus Bootstrap (Full N0x)

Build entire nucleus with 7+ core artifacts.
Seed > cex_nucleus_builder.py > agent_card > agent > SP > ...
Each artifact gets context from previously built ones.
Model: opus + xthinking. Time: 10-30 min.

## Selection

| Intent Signal | Pattern |
|---------------|---------|
| create a {{kind}} | P1 Direct |
| build {{thing}} with {{deps}} | P2 Crew |
| scaffold nucleus N0x | P3 Bootstrap |
| ambiguous | P1 via Motor |