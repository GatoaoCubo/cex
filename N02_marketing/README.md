---
id: n02_marketing_readme
kind: context_doc
pillar: P08
title: "N02 Marketing Nucleus — Creative Lust Engine"
nucleus: N02
sin: Luxúria Criativa
version: 2.0.0
quality: 9.1
created: 2026-04-06T12:00:00-03:00
updated: 2026-04-07T15:44:00-03:00
tags: [nucleus, marketing, n02, readme, fractal]
density_score: 1.0
---

# N02 Marketing — Creative Lust Engine

> Every word a whisper. Every headline a hook. N02 doesn't inform — it *seduces*.

**Sin:** Luxúria Criativa · **Domain:** Copy, ads, campaigns, brand voice, content
**CLI:** `bash _spawn/dispatch.sh solo n02 "task"` · **Model:** opus-4-6 (1M ctx)

## Mission

N02 exists to make audiences **want**, not merely **know**. It transforms dry specs into magnetic copy, bland features into irresistible benefits, and passive content into conversion machines. Every output drips with intent — calibrated desire that moves people to act.

## Fractal Structure (mirrors 12 pillars)

| Subdir | Pillar | Verb | Contents |
|--------|--------|------|----------|
| `knowledge/` | P01 | INJECT | 11 knowledge cards — Tailwind, typography, color theory, a11y, responsive, HTML components, Shadcn/Radix, visual hierarchy, email HTML, CSS animation |
| `agents/` | P02 | BECOME | `agent_marketing.md` — full identity, tool bindings, sin calibration |
| `prompts/` | P03 | REASON | System prompt, action prompt, brand voice templates, prompt template |
| `tools/` | P04 | CALL | Social publisher tool |
| `output/` | P05 | PRODUCE | 13 output templates — landing pages, emails, social cards, dashboards, style guides, visual reports, competitive positioning |
| `schemas/` | P06 | CONSTRAIN | 5 schemas — a11y checklist, design tokens, HTML output, responsive breakpoints, Tailwind palette |
| `quality/` | P07 | GOVERN | Scoring rubric for marketing artifacts |
| `architecture/` | P08 | GOVERN | Agent card, component maps |
| `config/` | P09 | GOVERN | A/B testing framework, brand override config |
| `memory/` | P10 | INJECT | Campaign performance memory, copy optimization insights |
| `feedback/` | P11 | GOVERN | Quality gate for marketing |
| `orchestration/` | P12 | COLLABORATE | Dispatch rules, cross-nucleus handoffs, weekly fashion content workflow |

## Artifact Count

| Category | Count |
|----------|-------|
| Knowledge cards | 11 |
| Output templates | 13 |
| Prompts | 4 |
| Schemas | 5 |
| Config | 2 |
| Memory | 2 |
| Orchestration | 5 |
| Quality / Feedback | 2 |
| Architecture / Agents | 3 |
| **Total** | **52** |

## Key Capabilities

1. **Brand Voice Injection** — Reads `.cex/brand/brand_config.yaml`, adapts tone/personality across all outputs
2. **Multi-Format Output** — Landing pages, email sequences, social cards, dashboards, visual reports
3. **A/B Testing Framework** — Structured hypothesis → variant → metric loops
4. **Cross-Nucleus Handoffs** — Receives briefs from N01 (research), feeds assets to N03 (build), coordinates with N06 (monetization)
5. **Social Publishing Pipeline** — Content creation → scheduling → distribution workflow
6. **Design System Compliance** — Tailwind palette contracts, responsive breakpoints, design tokens

## Integration Points

| From | To N02 | Purpose |
|------|--------|---------|
| N01 | Research briefs | Market data, competitive analysis → copy angles |
| N06 | Brand strategy | Positioning, pricing psychology → landing copy |
| N03 | Build requests | N02 produces copy/design specs → N03 implements |
| N04 | Knowledge cards | Domain expertise → accurate claims in copy |
| N07 | Dispatch | Grid tasks, mission waves |

## Quality Gate

All N02 outputs must score **≥ 8.0** to ship. Peer review by N07 or sibling nuclei assigns final quality.
Rubric: `quality/scoring_rubric_marketing.md`

## Quick Commands

```bash
# Dispatch a copy task
bash _spawn/dispatch.sh solo n02 "Write launch email for feature X"

# Score all N02 artifacts
python _tools/cex_score.py N02_marketing/**/*.md

# Evolve a specific artifact
python _tools/cex_evolve.py heuristic N02_marketing/output/landing_page_template.md
```

## Links

- Source mold: `N00_genesis/`
- Architecture map: `_docs/architecture/cex_architecture_map.md`
- Pipeline: `CLAUDE.md`
- Agent card: `agent_card_n02.md`
