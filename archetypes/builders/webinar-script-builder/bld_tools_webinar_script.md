---
kind: tools
id: bld_tools_webinar_script
pillar: P04
llm_function: CALL
purpose: Production tools, validation utilities, and external platform references for webinar_script builder
quality: 9.1
title: "Webinar Script Builder Tools"
version: "1.0.0"
author: n02_wave6
tags: [webinar_script, builder, tools]
tldr: "CEX production tools, time-budget calculator, Q&A validators, and Zoom/GoToWebinar/Teams platform references."
domain: "webinar_script construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_webinar_script_builder
  - bld_instruction_webinar_script
  - bld_tools_contributor_guide
  - bld_schema_webinar_script
  - bld_collaboration_webinar_script
  - p10_lr_webinar_script_builder
  - webinar-script-builder
  - bld_architecture_webinar_script
  - bld_knowledge_card_webinar_script
  - p03_qg_webinar_script
---
## Production Tools

CEX internal tools used during and after webinar_script artifact construction.

| Tool | Command | When to Use | Output |
|------|---------|-------------|--------|
| cex_compile.py | `python _tools/cex_compile.py {path}` | F8 COLLABORATE -- after saving .md file | Compiled .yaml in archetypes/builders/compiled/ |
| cex_score.py | `python _tools/cex_score.py --apply {path}` | F7 GOVERN -- peer scoring on publish | Quality score applied to frontmatter |
| cex_retriever.py | `python _tools/cex_retriever.py --query "webinar script hook demo Q&A"` | F3 INJECT -- find similar scripts | Top-N similar artifacts with similarity scores |
| cex_doctor.py | `python _tools/cex_doctor.py` | F8 COLLABORATE -- post-build system health check | PASS/FAIL report across all builders |
| cex_hygiene.py | `python _tools/cex_hygiene.py --check {path}` | F7 GOVERN -- frontmatter completeness check | List of missing or malformed fields |

## Validation Tools

Checks specific to webinar_script quality gates.

| Validator | Purpose | Check Method | Pass Condition |
|----------|---------|-------------|---------------|
| Word count / time budget | Verify script fits duration_minutes at 150 wpm | `wc -w {script_file}` / 150 <= duration_minutes | Word count / 150 <= duration_minutes |
| Slide cue checker | Verify [SLIDE X] cues are present and sequential | Grep `[SLIDE [0-9]` from script body | Min 1 cue per major section |
| Q&A seed counter | Verify minimum 3 seed questions in Q&A section | Grep `Seed Q[0-9]` from Q&A section | Count >= 3 |
| CTA validator | Verify CTA action + URL in closing section | Grep for http in closing section | Both action verb and URL present |
| Speaker note checker | Verify [SPEAKER NOTE] in every segment | Grep `[SPEAKER NOTE` from each segment | Min 1 per segment |

## External References

| Platform | Reference | Relevance |
|---------|-----------|----------|
| Zoom Webinar API | https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars | Webinar creation, Q&A feed, recording retrieval |
| GoToWebinar Engagement Guidelines | https://support.goto.com/webinar | Polls, Q&A moderation, attendee engagement scoring |
| ON24 Platform | https://on24.com/resources/ | Enterprise webinar automation, CRM integration |
| Teams Live Events API | https://learn.microsoft.com/en-us/microsoftteams/teams-live-events | Teams live event creation and Q&A moderation |
| GoToWebinar REST API | https://developer.goto.com/GoToWebinarV2 | Programmatic scheduling and attendee registration |

## Tool Execution Order (F5 CALL)

| Step | Tool | Purpose |
|------|------|---------|
| 1 | cex_retriever.py | Find similar webinar scripts to inform approach |
| 2 | (manual) word count estimate | Set segment word count budgets before writing |
| 3 | cex_hygiene.py --check | Verify frontmatter after F6 draft |
| 4 | slide cue checker | Verify [SLIDE X] completeness after F6 draft |
| 5 | seed question counter | Verify Q&A gate before F7 |
| 6 | CTA validator | Verify CTA section before F7 |
| 7 | cex_score.py | Run quality scoring in F7 GOVERN |
| 8 | cex_compile.py | Compile in F8 COLLABORATE |
| 9 | cex_doctor.py | System health check in F8 COLLABORATE |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_webinar_script_builder]] | upstream | 0.41 |
| [[bld_instruction_webinar_script]] | upstream | 0.40 |
| [[bld_tools_contributor_guide]] | sibling | 0.36 |
| [[bld_schema_webinar_script]] | downstream | 0.36 |
| [[bld_collaboration_webinar_script]] | downstream | 0.35 |
| [[p10_lr_webinar_script_builder]] | downstream | 0.31 |
| [[webinar-script-builder]] | upstream | 0.31 |
| [[bld_architecture_webinar_script]] | downstream | 0.31 |
| [[bld_knowledge_card_webinar_script]] | upstream | 0.31 |
| [[p03_qg_webinar_script]] | downstream | 0.30 |
