---
id: p12_dag_cf_course
kind: dag
pillar: P12
lp: P12
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n01_intelligence"
pipeline: "content_factory_course"
nodes:
  - id: "receive_longform"
    label: "Receive master longform draft and brand context from dag_cf_master"
    agent_group: "n07_orchestrator"
  - id: "define_outline"
    label: "Structure course outline: modules, lessons per module, learning objectives"
    agent_group: "n01_research"
  - id: "write_lesson_scripts"
    label: "Write lesson scripts from longform + outline (one per lesson)"
    agent_group: "n03_builder"
  - id: "generate_tts"
    label: "Convert lesson scripts to audio via TTS (ElevenLabs/OpenAI)"
    agent_group: "n05_operations"
  - id: "create_slides"
    label: "Generate slide decks per module via Canva/PPTX templates"
    agent_group: "n03_builder"
  - id: "generate_quizzes"
    label: "Generate quizzes per module from learning objectives (MCQ + open)"
    agent_group: "n04_knowledge"
  - id: "create_supplementary"
    label: "Generate workbooks, checklists, and resource lists per module"
    agent_group: "n03_builder"
  - id: "package_modules"
    label: "Assemble each module: audio + slides + quiz + supplements into SCORM/LMS bundle"
    agent_group: "n05_operations"
  - id: "add_branding"
    label: "Apply brand styling to all materials (cover, colors, logo, certificates)"
    agent_group: "n06_brand"
  - id: "quality_check"
    label: "Validate against cs_cf_course constraints (module count, lesson length, quiz rules)"
    agent_group: "n04_knowledge"
  - id: "lms_upload"
    label: "Upload packaged course to LMS platform and return enrollment URL"
    agent_group: "n05_operations"
edges:
  - from: "receive_longform"
    to: "define_outline"
  - from: "define_outline"
    to: "write_lesson_scripts"
  - from: "write_lesson_scripts"
    to: "generate_tts"
  - from: "write_lesson_scripts"
    to: "create_slides"
  - from: "write_lesson_scripts"
    to: "generate_quizzes"
  - from: "write_lesson_scripts"
    to: "create_supplementary"
  - from: "generate_tts"
    to: "package_modules"
  - from: "create_slides"
    to: "package_modules"
  - from: "generate_quizzes"
    to: "package_modules"
  - from: "create_supplementary"
    to: "package_modules"
  - from: "package_modules"
    to: "add_branding"
  - from: "add_branding"
    to: "quality_check"
  - from: "quality_check"
    to: "lms_upload"
domain: "orchestration"
quality: 9.0
tags: [dag, content-factory, course-pipeline, lms, tts, education]
tldr: "11-node course DAG: longform→outline→scripts→parallel(TTS+slides+quizzes+supplements)→package→brand→QA→LMS"
execution_order:
  - ["receive_longform"]
  - ["define_outline"]
  - ["write_lesson_scripts"]
  - ["generate_tts", "create_slides", "generate_quizzes", "create_supplementary"]
  - ["package_modules"]
  - ["add_branding"]
  - ["quality_check"]
  - ["lms_upload"]
parallel_groups:
  - ["generate_tts", "create_slides", "generate_quizzes", "create_supplementary"]
critical_path: ["receive_longform", "define_outline", "write_lesson_scripts", "generate_tts", "package_modules", "add_branding", "quality_check", "lms_upload"]
estimated_duration: "90min"
node_count: 11
edge_count: 13
max_parallelism: 4
keywords: [course, lms, education, tts, scorm, content-factory]
linked_artifacts:
  primary: "P12_orchestration/dags/content_factory/dag_cf_master.md"
  related:
    - "P03_prompts/constraints/content_factory/p03_constraint_cf_course.md"
density_score: 1.0
related:
  - p12_dag_cf_video
  - p12_dag_cf_presentation
  - p12_dag_cf_social
  - p12_dag_cf_ebook
  - p12_dag_cf_master
  - wave2_quality_report
  - n04_output_monetization_curriculum
  - n01_output_cf_dags_and_specs
  - p12_wf_content_factory_v1
  - commercial_readiness_20260414c
---

## Nodes

| ID | Label | Agent | Type |
|----|-------|-------|------|
| receive_longform | Receive longform draft + brand context | n07_orchestrator | input |
| define_outline | Structure course: modules, lessons, objectives | n01_research | compute |
| write_lesson_scripts | Write per-lesson scripts from longform+outline | n03_builder | compute |
| generate_tts | TTS conversion for all lesson scripts | n05_operations | compute |
| create_slides | Generate slide decks per module | n03_builder | compute |
| generate_quizzes | Generate MCQ + open quizzes per module | n04_knowledge | compute |
| create_supplementary | Generate workbooks, checklists, resources | n03_builder | compute |
| package_modules | Assemble SCORM/LMS bundles per module | n05_operations | join |
| add_branding | Brand styling: cover, colors, logo, certs | n06_brand | transform |
| quality_check | Validate against cs_cf_course constraints | n04_knowledge | gate |
| lms_upload | Upload to LMS, return enrollment URL | n05_operations | output |

## Edges

| From | To | Type |
|------|----|------|
| receive_longform | define_outline | data |
| define_outline | write_lesson_scripts | data |
| write_lesson_scripts | generate_tts | data |
| write_lesson_scripts | create_slides | data |
| write_lesson_scripts | generate_quizzes | data |
| write_lesson_scripts | create_supplementary | data |
| generate_tts | package_modules | data |
| create_slides | package_modules | data |
| generate_quizzes | package_modules | data |
| create_supplementary | package_modules | data |
| package_modules | add_branding | data |
| add_branding | quality_check | control |
| quality_check | lms_upload | control |

## Topological Order

receive_longform → define_outline → write_lesson_scripts → generate_tts → create_slides → generate_quizzes → create_supplementary → package_modules → add_branding → quality_check → lms_upload

## Parallel Groups

- **Wave 1**: receive_longform
- **Wave 2**: define_outline
- **Wave 3**: write_lesson_scripts
- **Wave 4**: generate_tts, create_slides, generate_quizzes, create_supplementary (max parallelism = 4)
- **Wave 5**: package_modules (join barrier — waits for all 4)
- **Wave 6**: add_branding
- **Wave 7**: quality_check
- **Wave 8**: lms_upload

## Critical Path

receive_longform (1min) → define_outline (10min) → write_lesson_scripts (25min) → generate_tts (20min) → package_modules (15min) → add_branding (5min) → quality_check (3min) → lms_upload (5min) = **84min**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dag_cf_video]] | sibling | 0.67 |
| [[p12_dag_cf_presentation]] | sibling | 0.67 |
| [[p12_dag_cf_social]] | sibling | 0.56 |
| [[p12_dag_cf_ebook]] | sibling | 0.53 |
| [[p12_dag_cf_master]] | sibling | 0.22 |
| [[wave2_quality_report]] | upstream | 0.19 |
| [[n04_output_monetization_curriculum]] | upstream | 0.18 |
| [[n01_output_cf_dags_and_specs]] | upstream | 0.18 |
| [[p12_wf_content_factory_v1]] | related | 0.16 |
| [[commercial_readiness_20260414c]] | upstream | 0.16 |
