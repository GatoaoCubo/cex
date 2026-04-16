---
kind: collaboration
id: bld_collaboration_webinar_script
pillar: P12
llm_function: COLLABORATE
purpose: Define crew role, handoff interfaces, and boundary for webinar_script builder in multi-nucleus workflows
quality: 9.1
title: "Webinar Script Collaboration"
version: "1.0.0"
author: n02_wave6
tags: [webinar_script, builder, collaboration]
tldr: "Webinar script builder crew role: receives brief from marketing/sales/design, produces to presenter/platform/email team."
domain: "webinar_script construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---
## Crew Role

Webinar content architect in the CEX multi-nucleus content pipeline. Responsible for producing complete, production-ready live session scripts with timed speaker narration, slide synchronization markers, and Q&A facilitation support. Operates within the N02 Marketing nucleus for copy and content tasks, or N03 Builder nucleus for artifact construction tasks.

**Primary output artifact type**: `webinar_script` (kind), `p03_ws_*.md` (naming pattern)
## Receives From

Inputs required before script production begins. Missing inputs block script construction.

| Source | Content Type | Format | Notes |
|--------|-------------|--------|-------|
| Marketing Team | Topic, target audience, webinar goal, key messages | Brief document or Markdown | GDP decision point: tone, audience, conversion goal |
| Sales / Product | Product demo points, demo environment URL, feature highlights | Notes or Markdown | Required for demo segment and seed Q&A answers |
| Design Team | Slide deck outline or section titles | Markdown or PDF | Required for [SLIDE X] cue alignment |
| Event Platform | Platform name, duration, registration URL | Config or brief | Required for schema fields: platform, duration_minutes |
| Previous Webinars | Past Q&A question logs, attendee feedback | Archive or CSV | Optional: improves seed question relevance |

**Handoff intake format**:
```
## Webinar Script Request
- Webinar Title: [title]
- Platform: [zoom | gotowebinar | teams]
- Duration: [45 | 60 | 90] minutes
- Target Audience: [persona description]
- Goal: [education | demo | lead-gen | upsell]
- Key Messages: [3 bullet points]
- Demo Assets: [URL or "none"]
- CTA Action: [trial | download | consultation | registration]
- CTA URL: [URL]
```
## Produces For

Downstream consumers of the webinar_script artifact.

| Consumer | What They Receive | Format | Handoff Method |
|---------|------------------|--------|---------------|
| Presenter / Speaker | Full speaker script with timestamps, slide cues, and speaker notes | Markdown .md file | Direct file delivery or N03 compile output |
| Event Platform (Zoom/GoToWebinar) | Structured agenda with timing for platform Q&A and poll setup | Extracted JSON or Markdown table | N05 can parse and push via platform API |
| Email Team | Post-webinar follow-up hook copy (CTA close section, key outcome lines) | Extracted Markdown section | Passed to N02 email-copy-builder as input brief |
| Recording Editor | Segment timestamps and slide transition markers | Timestamp list | Extracted from [MM:00] markers in script |
| Marketing Analytics | Webinar metadata (title, platform, audience, CTA URL) | YAML frontmatter | Extracted by cex_compile.py |
## Collaboration Signals

| Event | Signal Action | Target |
|-------|--------------|--------|
| Script draft complete | write_signal(n02, 'webinar_script_draft', score) | N07 orchestrator |
| Quality gate passed (>= 8.0) | write_signal(n02, 'webinar_script_published', score) | N07 + N05 for platform push |
| Quality gate failed | write_signal(n02, 'webinar_script_rejected', score) | N07 for review routing |
| Demo assets missing | write_signal(n02, 'needs_input', 'demo_assets') | N07 -> Sales team |
## Boundary

The webinar_script builder handles ONLY live session scripts. Adjacent content types route to specialized builders.

| Content Type | Correct Builder | Why NOT webinar_script |
|-------------|----------------|----------------------|
| Visual slide deck | pitch_deck-builder | webinar_script contains [SLIDE] cues only, not slide content |
| 1:1 sales call script | sales_playbook-builder | Different delivery format, no live audience mechanics |
| Recorded course module | online-course-builder | No live interaction layer, different pacing and structure |
| Post-webinar email sequence | email-copy-builder | webinar_script provides CTA hook only, not full sequence |
| Pre-webinar registration page | landing-page-builder | Separate artifact kind and conversion mechanics |
| Podcast script | podcast-script-builder | No visual platform, no slide cues, no Q&A facilitation structure |
