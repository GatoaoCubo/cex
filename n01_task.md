---
id: kc_nucleus_def
kind: knowledge_card
title: Nucleus Definition (N00-N07)
version: 1.0.0
quality: null
pillar: P01
---

# CEX Nucleus Definition (N00-N07)

A CEX nucleus is a specialized autonomous agent with fractal architecture, responsible for specific domains and pillars. Each nucleus operates with its own sin lens, CLI binding, and model tier, while sharing common infrastructure and context.

## Nucleus Specifications

| Nucleus | Role               | Pillars Owned       | Sin Lens           | CLI Binding       | Model Tier | Boot Script         | Agent Card Path       | Crew Templates Exposed | Domain Agents           |
|--------|--------------------|---------------------|--------------------|-------------------|------------|---------------------|------------------------|------------------------|-------------------------|
| N00    | Genesis            | P01-P12             | Core Integrity     | `n00-genesis`     | Opus       | `boot/n00.ps1`      | `agents/n00-genesis.md` | `templates/n00-*`      | `n00-genesis`           |
| N01    | Research/Analysis  | P01-P04             | Analytical Envy    | `n01-analyst`     | Opus       | `boot/n01.ps1`      | `agents/n01-analyst.md` | `templates/n01-*`      | `n01-analyst`           |
| N02    | Marketing/Copy     | P05-P08             | Creative Lust      | `n02-copywriter`  | Sonnet     | `boot/n02.ps1`      | `agents/n02-copywriter.md` | `templates/n02-*`      | `n02-copywriter`        |
| N03    | Build/Create       | P09-P12             | Inventive Pride    | `n03-builder`     | Opus       | `boot/n03.ps1`      | `agents/n03-builder.md` | `templates/n03-*`      | `n03-builder`           |
| N04    | Knowledge/Docs     | P01-P04             | Knowledge Gluttony | `n04-librarian`   | Sonnet     | `boot/n04.ps1`      | `agents/n04-librarian.md` | `templates/n04-*`      | `n04-librarian`         |
| N05    | Code/Test/Deploy   | P05-P08             | Gating Wrath       | `n05-operator`    | Sonnet     | `boot/n05.ps1`      | `agents/n05-operator.md` | `templates/n05-*`      | `n05-operator`          |
| N06    | Brand/Monetization | P09-P12             | Strategic Greed    | `n06-strategist`  | Sonnet     | `boot/n06.ps1`      | `agents/n06-strategist.md` | `templates/n06-*`      | `n06-strategist`        |
| N07    | Orchestration      | P01-P12             | System Integrity   | `n07-orchestrator`| Opus       | `boot/n07.ps1`      | `agents/n07-orchestrator.md` | `templates/n07-*`      | `n07-orchestrator`      |
