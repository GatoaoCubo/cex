---
kind: output_template
id: bld_output_template_webinar_script
pillar: P05
llm_function: PRODUCE
purpose: Canonical output template for webinar_script artifacts with all required sections and placeholders
quality: 9.1
title: "Webinar Script Output Template"
version: "1.0.0"
author: n02_wave6
tags: [webinar_script, builder, output_template]
tldr: "Full markdown template for webinar scripts: hook, agenda, segments, demo, Q&A, CTA with all cue formats."
domain: "webinar_script construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---
## Template Usage

Copy the block below. Replace all `{{placeholder}}` tokens with actual content. Do not remove any [SLIDE X], [SPEAKER NOTE], or [SCREEN] markers -- these are required structural elements.

**Time budget formula**: Total content words = ({{duration_minutes}} - 12) * 150

```markdown
---
kind: webinar_script
id: p03_ws_{{name}}
pillar: P03
title: "{{webinar_title}}"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: {{author}}
domain: "webinar_script construction"
quality: null
tags: [webinar_script, {{topic_tag}}]
tldr: "{{one_sentence_summary}}"
webinar_title: "{{webinar_title}}"
duration_minutes: {{duration_minutes}}
platform: {{platform}}
target_audience: "{{target_audience}}"
registration_url: "{{registration_url}}"
cta_url: "{{cta_url}}"
---
# {{webinar_title}}
**Platform**: {{platform}} | **Duration**: {{duration_minutes}} min | **Audience**: {{target_audience}}
---
## [0:00] HOOK / OPENING (60 sec)
[SLIDE 1: Title Slide]
Speaker: "{{opening_hook}} -- by the end of this session, you will know {{key_outcome_1}},
{{key_outcome_2}}, and {{key_outcome_3}}. Let's get into it."
[SPEAKER NOTE: High energy. Do not read from notes. Make eye contact with camera. Pause after stating outcomes.]
---
## [1:00] AGENDA PREVIEW (2 min)
[SLIDE 2: Agenda]
Speaker: "Here is exactly what we will cover today: {{agenda_item_1}}, {{agenda_item_2}},
and {{agenda_item_3}}. We will not cover {{out_of_scope_item}} -- that is a topic for
a separate session. We will open Q&A in the final 10 minutes. Drop your questions
in the chat any time and our moderator will queue them up."
[SPEAKER NOTE: Keep this brisk. Two minutes maximum. Audience is still deciding whether to stay.]
---
## [3:00] SEGMENT 1: {{segment_1_title}} ({{seg1_minutes}} min)
[SLIDE 3: {{segment_1_slide_title}}]
Speaker: "{{segment_1_problem_statement}} Most {{target_audience}} we talk to tell us
{{pain_point_quote}}. Here is what the data shows: {{key_stat_1}}."
[SLIDE 4: {{segment_1_evidence_slide}}]
Speaker: "{{segment_1_solution_statement}} The key insight is {{insight}}. Let me give
you a concrete example: {{example_story}}."
[SPEAKER NOTE: {{seg1_speaker_note}}. Target: {{seg1_minutes}} minutes. Watch the clock.]
---
## [{{seg2_start}}:00] SEGMENT 2: {{segment_2_title}} ({{seg2_minutes}} min)
[SLIDE {{slide_num_seg2}}: {{segment_2_slide_title}}]
Speaker: "{{segment_2_content}}"
[SPEAKER NOTE: {{seg2_speaker_note}}]
---
## [{{demo_start}}:00] DEMO: {{demo_title}} ({{demo_minutes}} min)
[SLIDE {{slide_num_demo}}: Live Demo]
Speaker: "Now let me show you exactly how this works in practice. I am going to walk
you through {{demo_scenario}} step by step."
[SCREEN: Navigate to {{demo_url}} or open {{demo_app}}]
Speaker: "Step 1 -- {{demo_step_1}}."
[SCREEN: {{demo_step_1_action}}]
Speaker: "Step 2 -- {{demo_step_2}}."
[SCREEN: {{demo_step_2_action}}]
Speaker: "Step 3 -- {{demo_step_3}}. And that is it. What you just saw was {{demo_outcome_summary}}."
[SPEAKER NOTE: If live demo fails, say "Let me pull up the recording" and switch to {{recording_url}}. Do not apologize -- just keep moving.]
---
## [{{qa_start}}:00] Q&A FACILITATION (10 min)
[SLIDE {{slide_num_qa}}: Q&A]
Moderator: "We are opening Q&A now. {{presenter_name}}, I have a few questions from the chat.
First question from the audience --"
**Seed Question 1**: "{{seed_question_1}}"
*Suggested answer direction*: {{seed_answer_direction_1}}
**Seed Question 2**: "{{seed_question_2}}"
*Suggested answer direction*: {{seed_answer_direction_2}}
**Seed Question 3**: "{{seed_question_3}}"
*Suggested answer direction*: {{seed_answer_direction_3}}
Moderator (time close): "We have time for one more question. After this we will wrap up."
[SPEAKER NOTE: If no audience questions in first 60 seconds, moderator reads Seed Question 1 immediately. Do not wait for the audience to break the silence.]
---
## [{{cta_start}}:00] CTA CLOSE (2 min)
[SLIDE {{slide_num_cta}}: {{cta_slide_title}}]
Speaker: "Before we close, here is what I want you to do right now. {{cta_action_sentence}}.
You can do that at {{cta_url}}. I will also send that link in the follow-up email
along with the recording."
Speaker: "{{closing_value_restatement}} -- that is why {{cta_benefit_statement}}."
Speaker: "Thank you for joining {{webinar_title}} today. I appreciate your time and attention.
See you next session."
[SPEAKER NOTE: Smile. Pause after stating the URL. Repeat it once. End on high energy.]
```

## Placeholder Reference

| Placeholder | Type | Notes |
|------------|------|-------|
| {{name}} | slug | Lowercase, underscores only, used in filename |
| {{webinar_title}} | string | Display title of the webinar event |
| {{duration_minutes}} | integer | 30, 45, 60, or 90 |
| {{platform}} | string | zoom, gotowebinar, teams |
| {{target_audience}} | string | Job title or persona description |
| {{opening_hook}} | string | First sentence of hook, states attendee benefit |
| {{key_outcome_N}} | string | 3 outcomes attendees will leave with |
| {{agenda_item_N}} | string | 3 agenda items previewed upfront |
| {{seed_question_N}} | string | 3 Q&A seed questions for dead-air prevention |
| {{cta_url}} | URL | Full URL for the CTA action |
| {{cta_action_sentence}} | string | Imperative: "Start your free trial" |