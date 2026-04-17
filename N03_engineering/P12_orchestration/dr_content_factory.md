---
id: p12_dr_content_factory
kind: dispatch_rule
pillar: P12
version: "1.0.0"
created: "2026-04-08"
updated: "2026-04-08"
author: "n03_builder"
domain: "content_factory"
quality: 9.1
tags: [dispatch_rule, content-factory, routing, multi-nucleus]
tldr: "Routes content factory intents to nuclei: research->N01, copy->N02, build->N03, knowledge->N04, deploy->N05, monetize->N06"
scope: content_factory
keywords:
  - content factory
  - fabrica de conteudo
  - course
  - curso
  - video
  - ebook
  - presentation
  - apresentacao
  - podcast
  - social posts
  - landing page
  - multi-format
  - publish
  - publicar
agent_group: n07_admin
model: opus
priority: 8
confidence_threshold: 0.70
fallback: n03_engineering
conditions:
  requires_brand: true
  min_brief_length: 10
load_balance: true
routing_strategy: hybrid
density_score: 0.91
---

# Content Factory Dispatch Rule

## Purpose

Routes Content Factory pipeline intents to the appropriate nucleus based on content type
and production phase. This is the top-level routing policy for all content factory
operations -- it determines which nucleus handles which stage of the dag_cf_master
pipeline. The rule operates at the intent level (user says "create a course about X")
and decomposes into nucleus-specific dispatches via wf_content_factory_v1.

When a content factory intent is detected with confidence >= 0.70, N07 orchestrator
claims the task and dispatches to sub-nuclei according to the wave plan. Below threshold,
the intent falls through to N03 as a generic build request.

## Routing Matrix

| Content Type | Phase | Primary Nucleus | Rationale |
|-------------|-------|-----------------|-----------|
| Any | Research / analysis | N01 Intelligence | Deep topic research, competitor analysis, keyword discovery |
| Any | Brand injection | N06 Commercial | Brand config loading, voice/palette injection |
| Any | Strategy / copy | N02 Marketing | Content strategy, hooks, CTAs, social copy, email sequences |
| Course | Outline + scripts | N03 Engineering | Structured content production via prompt templates |
| Video | Script + assembly | N03 Engineering | Script authoring + FFmpeg/Remotion tool execution |
| eBook | Chapters + compile | N03 Engineering | Long-form writing + Typst/Pandoc compilation |
| Presentation | Slides + export | N03 Engineering | Slide content + Canva API / Marp execution |
| Podcast | Audio generation | N04 Knowledge | NotebookLM Audio Overview + ElevenLabs TTS |
| Flashcards / Quiz | Study materials | N04 Knowledge | NotebookLM Studio activation |
| Social posts | Multi-platform | N02 Marketing | Platform-specific copy + Ayrshare scheduling |
| Landing page | Page + checkout | N02 Marketing + N06 Commercial | Copy (N02) + pricing/checkout (N06) |
| Any | Publish (YouTube) | N05 Operations | YouTube API upload + metadata |
| Any | Publish (Hotmart) | N06 Commercial | Course upload + checkout config |
| Any | Publish (social) | N02 Marketing | Ayrshare multi-platform distribution |
| Any | Quality gate | N07 Admin | Brand consistency + constraint validation |

## Parallel vs Sequential Stages

| Stage | Execution | Nuclei Involved | Signal Dependency |
|-------|-----------|-----------------|-------------------|
| Research | Parallel with brand inject | N01 + N06 | None (Wave 2 start) |
| Strategy | Sequential after research | N02 | research_complete + brand_inject_complete |
| Authoring | Sequential after strategy | N03 | strategy_complete |
| Production | Parallel (all formats) | N03 + N02 + N04 | longform_complete |
| Media assembly | Parallel (all tools) | N03 | All format drafts complete |
| NotebookLM | Parallel with production | N04 | research_complete (independent of authoring) |
| Quality gate | Sequential barrier | N07 | media_assets_complete + notebooklm_complete |
| Publishing | Parallel (all channels) | N05 + N06 + N02 | quality_gate_complete |

## Quality Gates Between Stages

| Gate | Location | Threshold | Action on Fail |
|------|----------|-----------|----------------|
| Brief validation | After Wave 1 | Brief has topic + audience + >= 1 format | Abort, request resubmit |
| Brand check | After Wave 2 | brand_config.yaml passes brand_validate.py | Abort, run /init |
| Content coherence | After Wave 3 | Strategy aligns with research findings | Re-dispatch N02 with additional context |
| Format compliance | After Wave 4 | Each format meets constraint spec limits | Re-dispatch failing format nucleus |
| Brand consistency | After Wave 4 | All outputs match brand voice/colors | Flag deviations, re-dispatch if critical |
| Final gate | Before publish | All outputs quality >= 8.5 | Hold publication, report to user |

## Keyword Rationale

Keywords cover both PT and EN variants of content factory intents. "fabrica de conteudo"
and "content factory" trigger direct recognition. Individual format keywords (curso, video,
ebook, apresentacao, podcast) trigger when combined with production-intent verbs (criar,
gerar, produzir, build, create, generate). The hybrid routing strategy combines keyword
matching with semantic similarity for ambiguous intents like "make something about X"
which should route to content factory if format plurality is implied.

## Fallback Logic

When confidence falls below 0.70, the intent is too ambiguous for full pipeline activation.
Fallback routes to N03 (engineering) as a single-artifact build request. This handles cases
like "write an article about X" (single format, no pipeline needed) or "fix the video script"
(edit, not produce). N03 then applies its own 8F pipeline for the specific artifact without
activating the full multi-wave content factory workflow.

## References

1. `N03_engineering/workflows/wf_content_factory_v1.md` -- runtime workflow this rule feeds
2. `N03_engineering/chains/ch_brief_to_multiformat.md` -- prompt chain for content transformation
3. `P12_orchestration/dags/content_factory/dag_cf_master.md` -- dependency graph
4. `_docs/specs/spec_content_factory_v1.md` -- master spec
5. `.claude/rules/n07-input-transmutation.md` -- intent resolution protocol
