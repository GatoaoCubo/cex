---
kind: schema
id: bld_schema_realtime_session
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for realtime_session
quality: null
title: "Schema Realtime Session"
version: "1.0.0"
author: wave1_builder_gen
tags: [realtime_session, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for realtime_session"
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field      | Type   | Required | Default | Notes |  
|------------|--------|----------|---------|-------|  
| id         | string | yes      | -       | Unique identifier |  
| kind       | string | yes      | "realtime_session" | CEX type |  
| pillar     | string | yes      | "P09"    | Pillar classification |  
| title      | string | yes      | -       | Session title |  
| version    | string | yes      | "1.0"   | Schema version |  
| created    | date   | yes      | -       | Creation timestamp |  
| updated    | date   | yes      | -       | Last update timestamp |  
| author     | string | yes      | -       | Creator |  
| domain     | string | yes      | "realtime" | Domain context |  
| quality    | string | yes      | "draft" | Quality status |  
| tags       | array  | yes      | []      | Keywords |  
| tldr       | string | yes      | -       | Summary |  
| session_id | string | yes      | -       | Unique session ID |  
| start_time | date   | yes      | -       | Session start |  

### Recommended  
| Field          | Type   | Notes |  
|----------------|--------|-------|  
| session_type   | string | e.g., "live", "demo" |  
| recording_url  | string | Optional recording link |  
| max_participants | integer | Maximum attendees |  
| status         | string | "active", "archived" |  

## ID Pattern  
^p09_rs_[a-zA-Z0-9_]+\.md$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and context of the session.  
2. **Session Details**  
   - Start/end times, session type, and domain-specific parameters.  
3. **Participants**  
   - List of attendees, roles, and engagement metrics.  
4. **Timeline**  
   - Key events, milestones, and session phases.  
5. **Quality Metrics**  
   - Performance indicators (latency, drop rates, etc.).  
6. **Session Status**  
   - Current state and resolution notes.  

## Constraints  
- Session ID must be unique across all records.  
- Start time must precede end time.  
- Quality must be one of: "draft", "review", "final".  
- Tags must be lowercase and alphanumeric.  
- Max participants must be ≥ 1.  
- Recording URL must be valid if provided.
