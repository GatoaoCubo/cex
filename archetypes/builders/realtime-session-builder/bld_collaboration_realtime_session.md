---
kind: collaboration
id: bld_collaboration_realtime_session
pillar: P12
llm_function: COLLABORATE
purpose: How realtime_session-builder works in crews with other builders
quality: null
title: "Collaboration Realtime Session"
version: "1.0.0"
author: wave1_builder_gen
tags: [realtime_session, builder, collaboration]
tldr: "How realtime_session-builder works in crews with other builders"
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role  
Coordinates session setup, manages participant states, and handles session lifecycle events (start, pause, end).  

## Receives From  
| Builder         | What                  | Format  |  
|-----------------|-----------------------|---------|  
| transport_config| Network parameters    | JSON    |  
| voice_pipeline  | Audio codec settings  | YAML    |  
| user_auth       | Participant tokens    | JWT     |  

## Produces For  
| Builder         | What                  | Format    |  
|-----------------|-----------------------|-----------|  
| session_config  | Session configuration | JSON      |  
| participant_state | Realtime state updates | Protobuf |  
| session_events  | Lifecycle events      | JSON      |  

## Boundary  
Does NOT handle transport protocols (transport_config), voice processing (voice_pipeline), or user authentication (user_auth).
