---
id: p12_dag_cf_master
kind: dag
pillar: P12
lp: P12
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n01_intelligence"
pipeline: "content_factory_master"
nodes:
  - id: "ingest_brief"
    label: "Parse and validate content brief (topic, audience, formats, brand_ref)"
    agent_group: "n01_research"
  - id: "brand_inject"
    label: "Load brand_config.yaml and inject voice, palette, logo into context"
    agent_group: "n06_brand"
  - id: "research"
    label: "Deep research on topic: competitors, trends, keywords, sources"
    agent_group: "n01_research"
  - id: "strategy"
    label: "Define content strategy: angle, hook, CTA, distribution channels"
    agent_group: "n02_marketing"
  - id: "author_longform"
    label: "Write master longform draft (article/script) from research + strategy"
    agent_group: "n03_builder"
  - id: "fork_video"
    label: "Trigger video pipeline (dag_cf_video) with longform as input"
    agent_group: "n07_orchestrator"
  - id: "fork_course"
    label: "Trigger course pipeline (dag_cf_course) with longform as input"
    agent_group: "n07_orchestrator"
  - id: "fork_ebook"
    label: "Trigger eBook pipeline (dag_cf_ebook) with longform as input"
    agent_group: "n07_orchestrator"
  - id: "fork_presentation"
    label: "Trigger presentation pipeline (dag_cf_presentation) with longform as input"
    agent_group: "n07_orchestrator"
  - id: "fork_social"
    label: "Trigger social campaign pipeline (dag_cf_social) with longform as input"
    agent_group: "n07_orchestrator"
  - id: "collect_outputs"
    label: "Aggregate all format outputs into unified content package"
    agent_group: "n07_orchestrator"
  - id: "quality_gate"
    label: "Run brand consistency check + constraint validation on all outputs"
    agent_group: "n04_knowledge"
  - id: "publish"
    label: "Distribute approved content to target channels (CMS, LMS, social, CDN)"
    agent_group: "n05_operations"
edges:
  - from: "ingest_brief"
    to: "brand_inject"
  - from: "ingest_brief"
    to: "research"
  - from: "brand_inject"
    to: "strategy"
  - from: "research"
    to: "strategy"
  - from: "strategy"
    to: "author_longform"
  - from: "author_longform"
    to: "fork_video"
  - from: "author_longform"
    to: "fork_course"
  - from: "author_longform"
    to: "fork_ebook"
  - from: "author_longform"
    to: "fork_presentation"
  - from: "author_longform"
    to: "fork_social"
  - from: "fork_video"
    to: "collect_outputs"
  - from: "fork_course"
    to: "collect_outputs"
  - from: "fork_ebook"
    to: "collect_outputs"
  - from: "fork_presentation"
    to: "collect_outputs"
  - from: "fork_social"
    to: "collect_outputs"
  - from: "collect_outputs"
    to: "quality_gate"
  - from: "quality_gate"
    to: "publish"
domain: "orchestration"
quality: 9.0
tags: [dag, content-factory, master-pipeline, multi-format, orchestration]
tldr: "13-node master DAG: brief→research→strategy→author→fan-out 5 format pipelines→collect→quality gate→publish"
execution_order:
  - ["ingest_brief"]
  - ["brand_inject", "research"]
  - ["strategy"]
  - ["author_longform"]
  - ["fork_video", "fork_course", "fork_ebook", "fork_presentation", "fork_social"]
  - ["collect_outputs"]
  - ["quality_gate"]
  - ["publish"]
parallel_groups:
  - ["brand_inject", "research"]
  - ["fork_video", "fork_course", "fork_ebook", "fork_presentation", "fork_social"]
critical_path: ["ingest_brief", "research", "strategy", "author_longform", "fork_video", "collect_outputs", "quality_gate", "publish"]
estimated_duration: "120min"
node_count: 13
edge_count: 17
max_parallelism: 5
keywords: [content-factory, master, pipeline, multi-format, fan-out]
linked_artifacts:
  primary: "P12_orchestration/dags/content_factory/"
  related:
    - "P12_orchestration/dags/content_factory/dag_cf_video.md"
    - "P12_orchestration/dags/content_factory/dag_cf_course.md"
    - "P12_orchestration/dags/content_factory/dag_cf_ebook.md"
    - "P12_orchestration/dags/content_factory/dag_cf_presentation.md"
    - "P12_orchestration/dags/content_factory/dag_cf_social.md"
density_score: 1.0
related:
  - p12_dag_cf_social
  - p12_dag_cf_video
  - p12_dag_cf_presentation
  - p12_dag_cf_course
  - n01_output_cf_dags_and_specs
  - bld_collaboration_research_pipeline
  - p12_wf_content_factory_v1
  - p12_dag_cf_ebook
  - p12_dr_content_factory
  - p12_wf_marketing_pipeline
---

## Nodes

| ID | Label | Agent | Type |
|----|-------|-------|------|
| ingest_brief | Parse and validate content brief | n01_research | input |
| brand_inject | Load brand context into pipeline | n06_brand | transform |
| research | Deep topic research (competitors, keywords, sources) | n01_research | compute |
| strategy | Define angle, hook, CTA, distribution plan | n02_marketing | compute |
| author_longform | Write master longform draft from research+strategy | n03_builder | compute |
| fork_video | Trigger dag_cf_video sub-pipeline | n07_orchestrator | fork |
| fork_course | Trigger dag_cf_course sub-pipeline | n07_orchestrator | fork |
| fork_ebook | Trigger dag_cf_ebook sub-pipeline | n07_orchestrator | fork |
| fork_presentation | Trigger dag_cf_presentation sub-pipeline | n07_orchestrator | fork |
| fork_social | Trigger dag_cf_social sub-pipeline | n07_orchestrator | fork |
| collect_outputs | Aggregate all format outputs | n07_orchestrator | join |
| quality_gate | Brand consistency + constraint validation | n04_knowledge | gate |
| publish | Distribute to target channels | n05_operations | output |

## Edges

| From | To | Type |
|------|----|------|
| ingest_brief | brand_inject | data |
| ingest_brief | research | data |
| brand_inject | strategy | data |
| research | strategy | data |
| strategy | author_longform | data |
| author_longform | fork_video | trigger |
| author_longform | fork_course | trigger |
| author_longform | fork_ebook | trigger |
| author_longform | fork_presentation | trigger |
| author_longform | fork_social | trigger |
| fork_video | collect_outputs | data |
| fork_course | collect_outputs | data |
| fork_ebook | collect_outputs | data |
| fork_presentation | collect_outputs | data |
| fork_social | collect_outputs | data |
| collect_outputs | quality_gate | control |
| quality_gate | publish | control |

## Topological Order

ingest_brief → brand_inject → research → strategy → author_longform → fork_video → fork_course → fork_ebook → fork_presentation → fork_social → collect_outputs → quality_gate → publish

## Parallel Groups

- **Wave 1**: ingest_brief
- **Wave 2**: brand_inject, research (independent after brief)
- **Wave 3**: strategy (needs both brand + research)
- **Wave 4**: author_longform
- **Wave 5**: fork_video, fork_course, fork_ebook, fork_presentation, fork_social (max parallelism = 5)
- **Wave 6**: collect_outputs (join barrier)
- **Wave 7**: quality_gate
- **Wave 8**: publish

## Critical Path

ingest_brief (5min) → research (30min) → strategy (15min) → author_longform (30min) → fork_video (25min) → collect_outputs (5min) → quality_gate (5min) → publish (5min) = **120min**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dag_cf_social]] | sibling | 0.28 |
| [[p12_dag_cf_video]] | sibling | 0.25 |
| [[p12_dag_cf_presentation]] | sibling | 0.23 |
| [[p12_dag_cf_course]] | sibling | 0.23 |
| [[n01_output_cf_dags_and_specs]] | upstream | 0.23 |
| [[bld_collaboration_research_pipeline]] | related | 0.22 |
| [[p12_wf_content_factory_v1]] | related | 0.20 |
| [[p12_dag_cf_ebook]] | sibling | 0.19 |
| [[p12_dr_content_factory]] | related | 0.18 |
| [[p12_wf_marketing_pipeline]] | related | 0.17 |
