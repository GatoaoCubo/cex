# CEX -- Company Experience X

> Universal framework for organizing enterprise AI knowledge.
> 8 Functions. 12 Pillars. 78 Kinds. 7 Nuclei.

![version](https://img.shields.io/badge/version-v5.0.0-blue)
![pillars](https://img.shields.io/badge/pillars-12-green)
![kinds](https://img.shields.io/badge/kinds-78-orange)
![nuclei](https://img.shields.io/badge/nuclei-7-purple)

**Status**: v5.0.0 | 12 pillars | 78 kinds | 179 examples | 85 templates | 121 compiled | 4/78 builders

---

## What is CEX

CEX organizes everything an AI-assisted company knows, does, and decides
into a fractal structure navigable by humans and LLMs.

## Architecture

```
8 Functions     BECOME > INJECT > REASON > CALL > PRODUCE > CONSTRAIN > GOVERN > COLLABORATE
12 Pillars      P01 Knowledge ... P12 Orchestration
78 Kinds        knowledge_card, agent, skill, workflow...
7 Nuclei        N01 Intelligence ... N07 Admin
```

## Quick Stats

| Item | Count |
|------|-------|
| Pillars | 12 |
| Kinds | 78 |
| Nuclei | 7 |
| Examples | 179 |
| Compiled | 121 |
| Templates | 85 |
| Builders | 4/78 |
| Validators | 7 + cex_doctor.py |

## Frontmatter (every artifact)

```yaml
---
id: p01_kc_example
kind: knowledge_card
pillar: P01
title: Example
---
```

`kind:` = what shape (78). `pillar:` = which pillar (P01-P12).

## Navigation

| Want to... | Read |
|-----------|------|
| Understand CEX | _docs/WHITEPAPER_CEX.md |
| See the rules | _docs/ARCHITECTURE.md |
| See 8 functions | LLM_PIPELINE.md |
| Find everything | INDEX.md |
| Check health | python _tools/cex_doctor.py |
| Create artifact | _docs/QUICKSTART.md |

---

*CEX v5.0.0 | 2026-03-26 | MIT License*