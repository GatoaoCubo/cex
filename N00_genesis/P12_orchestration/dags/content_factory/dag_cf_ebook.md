---
id: p12_dag_cf_ebook
kind: dag
pillar: P12
lp: P12
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n01_intelligence"
pipeline: "content_factory_ebook"
nodes:
  - id: "receive_longform"
    label: "Receive master longform draft and brand context from dag_cf_master"
    agent_group: "n07_orchestrator"
  - id: "define_outline"
    label: "Structure eBook: chapters, sections, target word count per chapter"
    agent_group: "n01_research"
  - id: "write_chapters"
    label: "Expand longform into full chapters with transitions and examples"
    agent_group: "n03_builder"
  - id: "editorial_review"
    label: "Review chapters for coherence, flow, grammar, and brand voice"
    agent_group: "n02_marketing"
  - id: "generate_illustrations"
    label: "Create chapter illustrations, diagrams, and infographics"
    agent_group: "n03_builder"
  - id: "design_cover"
    label: "Design eBook cover with brand palette, title, and author"
    agent_group: "n06_brand"
  - id: "typeset"
    label: "Apply typography, margins, headers, TOC, page numbers via template"
    agent_group: "n05_operations"
  - id: "assemble_ebook"
    label: "Merge chapters + illustrations + cover into single manuscript"
    agent_group: "n05_operations"
  - id: "quality_check"
    label: "Validate against cs_cf_ebook constraints (chapters, word count, format)"
    agent_group: "n04_knowledge"
  - id: "export"
    label: "Export to PDF + EPUB + MOBI and upload to CDN staging"
    agent_group: "n05_operations"
edges:
  - from: "receive_longform"
    to: "define_outline"
  - from: "define_outline"
    to: "write_chapters"
  - from: "write_chapters"
    to: "editorial_review"
  - from: "write_chapters"
    to: "generate_illustrations"
  - from: "editorial_review"
    to: "typeset"
  - from: "generate_illustrations"
    to: "typeset"
  - from: "receive_longform"
    to: "design_cover"
  - from: "typeset"
    to: "assemble_ebook"
  - from: "design_cover"
    to: "assemble_ebook"
  - from: "assemble_ebook"
    to: "quality_check"
  - from: "quality_check"
    to: "export"
domain: "orchestration"
quality: 9.0
tags: [dag, content-factory, ebook-pipeline, pdf, epub, publishing]
tldr: "10-node eBook DAG: longform→outline→chapters→parallel(review+illustrations)+cover→typeset→assemble→QA→export"
execution_order:
  - ["receive_longform"]
  - ["define_outline", "design_cover"]
  - ["write_chapters"]
  - ["editorial_review", "generate_illustrations"]
  - ["typeset"]
  - ["assemble_ebook"]
  - ["quality_check"]
  - ["export"]
parallel_groups:
  - ["define_outline", "design_cover"]
  - ["editorial_review", "generate_illustrations"]
critical_path: ["receive_longform", "define_outline", "write_chapters", "editorial_review", "typeset", "assemble_ebook", "quality_check", "export"]
estimated_duration: "75min"
node_count: 10
edge_count: 11
max_parallelism: 2
keywords: [ebook, pdf, epub, publishing, typography, content-factory]
linked_artifacts:
  primary: "P12_orchestration/dags/content_factory/dag_cf_master.md"
  related:
    - "P03_prompts/constraints/content_factory/p03_constraint_cf_ebook.md"
density_score: 1.0
related:
  - p12_dag_cf_presentation
  - p12_dag_cf_course
  - p12_dag_cf_video
  - p12_dag_cf_social
  - p12_dag_cf_master
  - n01_output_cf_dags_and_specs
  - wave2_quality_report
  - n04_output_monetization_curriculum
  - p04_fn_cf_ebook_compile
  - p12_wf_content_factory_v1
---

## Nodes

| ID | Label | Agent | Type |
|----|-------|-------|------|
| receive_longform | Receive longform draft + brand context | n07_orchestrator | input |
| define_outline | Structure eBook: chapters, sections, word targets | n01_research | compute |
| write_chapters | Expand longform into full chapters | n03_builder | compute |
| editorial_review | Review coherence, flow, grammar, brand voice | n02_marketing | compute |
| generate_illustrations | Create diagrams, infographics, chapter art | n03_builder | compute |
| design_cover | Design cover with brand palette and title | n06_brand | compute |
| typeset | Apply typography, margins, TOC, page numbers | n05_operations | compute |
| assemble_ebook | Merge chapters + illustrations + cover | n05_operations | join |
| quality_check | Validate against cs_cf_ebook constraints | n04_knowledge | gate |
| export | Export PDF + EPUB + MOBI to CDN staging | n05_operations | output |

## Edges

| From | To | Type |
|------|----|------|
| receive_longform | define_outline | data |
| receive_longform | design_cover | data |
| define_outline | write_chapters | data |
| write_chapters | editorial_review | data |
| write_chapters | generate_illustrations | data |
| editorial_review | typeset | data |
| generate_illustrations | typeset | data |
| typeset | assemble_ebook | data |
| design_cover | assemble_ebook | data |
| assemble_ebook | quality_check | control |
| quality_check | export | control |

## Topological Order

receive_longform → define_outline → design_cover → write_chapters → editorial_review → generate_illustrations → typeset → assemble_ebook → quality_check → export

## Parallel Groups

- **Wave 1**: receive_longform
- **Wave 2**: define_outline, design_cover (independent after longform)
- **Wave 3**: write_chapters
- **Wave 4**: editorial_review, generate_illustrations (parallel from chapters)
- **Wave 5**: typeset (join barrier — needs review + illustrations)
- **Wave 6**: assemble_ebook (join — needs typeset + cover)
- **Wave 7**: quality_check
- **Wave 8**: export

## Critical Path

receive_longform (1min) → define_outline (8min) → write_chapters (25min) → editorial_review (15min) → typeset (10min) → assemble_ebook (5min) → quality_check (3min) → export (3min) = **70min**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dag_cf_presentation]] | sibling | 0.72 |
| [[p12_dag_cf_course]] | sibling | 0.61 |
| [[p12_dag_cf_video]] | sibling | 0.61 |
| [[p12_dag_cf_social]] | sibling | 0.55 |
| [[p12_dag_cf_master]] | sibling | 0.21 |
| [[n01_output_cf_dags_and_specs]] | upstream | 0.19 |
| [[wave2_quality_report]] | upstream | 0.19 |
| [[n04_output_monetization_curriculum]] | upstream | 0.17 |
| [[p04_fn_cf_ebook_compile]] | upstream | 0.17 |
| [[p12_wf_content_factory_v1]] | related | 0.16 |
