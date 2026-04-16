---
kind: quality_gate
id: p03_qg_webinar_script
pillar: P11
llm_function: GOVERN
purpose: Define HARD gates and SOFT scoring dimensions for webinar_script quality enforcement
quality: 9.2
title: "Webinar Script Quality Gate"
version: "1.0.0"
author: n02_wave6
tags: [webinar_script, builder, quality_gate]
tldr: "8 hard gates and 5 scored dimensions for webinar_script artifacts. Minimum publish score: 8.0."
domain: "webinar_script construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---
## Definition

| Property | Value |
|---------|-------|
| Kind | quality_gate |
| Target kind | webinar_script |
| Gate count | 8 HARD + 5 SOFT dimensions |
| Publish floor | 8.0 / 10.0 |
| Golden threshold | 9.5 / 10.0 |
| Scorer | cex_score.py |
| Retry limit | 2 retries before REJECT |

## HARD Gates (all must pass -- any failure = BLOCK)

| Gate | ID | Check | Pass Condition | Failure Action |
|------|----|-------|---------------|---------------|
| YAML valid | H01 | frontmatter parses without error | All fields present and typed correctly | Return to F6 |
| ID pattern | H02 | id field matches regex | ^p03_ws_[a-z][a-z0-9_]+$ | Return to F6 |
| Kind correct | H03 | kind field value | Exactly "webinar_script" | Return to F6 |
| Hook present | H04 | First section contains hook | Hook statement in section 1, <= 150 words | Return to F6 |
| Agenda section | H05 | Second section exists | Contains 3+ agenda items and Q&A timing | Return to F6 |
| Value segment | H06 | At least one content segment | Contains speaker content + [SLIDE X] cue | Return to F6 |
| Q&A seeds | H07 | Q&A section seed count | >= 3 seed questions numbered or labeled | Return to F6 |
| CTA explicit | H08 | Closing section CTA | Action + URL both present in closing | Return to F6 |

## SOFT Scoring Dimensions (weighted to 10.0)

| Dimension | ID | Weight | What Is Scored | Score Criteria |
|-----------|-----|--------|---------------|---------------|
| Hook strength | D01 | 0.25 | Attention capture in first 60 sec | 10=benefit stated in sentence 1, hook framework applied; 7=benefit stated but no framework; 5=vague opener; 3=company bio opener |
| Segment structure | D02 | 0.20 | Timed clarity and flow across segments | 10=all segments timed, [SLIDE] and [SPEAKER NOTE] in every segment; 7=most cues present; 5=some cues missing; 3=unstructured prose |
| Demo narration | D03 | 0.20 | Slide cue completeness and demo precision | 10=step-by-step cues, fallback note, screen cues present; 7=steps present, no fallback; 5=demo section present but vague; 3=no demo narration |
| Q&A preparation | D04 | 0.15 | Seed question quality and facilitator script | 10=3+ seeds, moderator intro, graceful close line; 7=3 seeds, no moderator intro; 5=2 seeds only; 3=no seeds |
| CTA clarity | D05 | 0.20 | Conversion strength of closing CTA | 10=action named, URL present, benefit restated, urgency element; 7=action and URL, no benefit; 5=action only, no URL; 3=vague close |

**Formula**: `score = (D01 * 0.25) + (D02 * 0.20) + (D03 * 0.20) + (D04 * 0.15) + (D05 * 0.20)`

## Actions Table

| Score | Label | Action |
|-------|-------|--------|
| >= 9.5 | GOLDEN | Publish + add to examples as golden reference |
| >= 8.0 | PUBLISH | Publish to artifacts directory |
| >= 7.0 | REVIEW | Return to builder with specific feedback |
| < 7.0 | REJECT | Block publish, mandatory rebuild |

## Bypass Table

Bypass is not available for webinar scripts. Live delivery stakes require all gates.

| Gate | Bypassable | Reason |
|------|-----------|--------|
| H01 YAML | NO | Structural integrity |
| H02 ID | NO | Naming convention |
| H03 Kind | NO | Type safety |
| H04 Hook | NO | Audience retention critical |
| H05 Agenda | NO | Attendee orientation critical |
| H06 Segment | NO | Content delivery required |
| H07 Q&A | NO | Dead air prevention critical |
| H08 CTA | NO | Conversion goal required |

## Retry Protocol

1. First failure: return to F6 with specific gate failure listed.
2. Second failure: return to F4 REASON -- rebuild plan may be flawed.
3. Third failure: escalate to REJECT. Do not publish below floor.