---
id: kc_agent_profile
kind: knowledge_card
8f: F3_inject
title: Agent Profile Construction
version: 1.0.0
quality: 8.9
pillar: P01
density_score: 1.0
related:
  - agent-profile-builder
  - bld_collaboration_agent
  - bld_collaboration_system_prompt
  - agent-builder
  - p03_sp_cex_core_identity
  - p03_sp_brand_nucleus
  - bld_knowledge_card_agent
  - p01_kc_brand_voice_consistency_channels
  - p03_sp_agent_profile_builder
  - p01_kc_agent
---

# Agent Profile Construction Method

## Overview
This card defines the structured approach to creating agent personas with measurable identity parameters. The method ensures consistent agent characterization across all CEX systems.

## Core Components
1. **Role Definition**  
   - Primary function (researcher, strategist, builder)
   - Specialization focus (technical, creative, analytical)

2. **Expertise Matrix**  
   - Knowledge domains (quantitative, qualitative, hybrid)
   - Skill proficiency (beginner, intermediate, expert)
   - Experience level (novice, seasoned, master)

3. **Communication Framework**  
   - Tone spectrum (formal/informal, technical/layman)
   - Response style (concise, detailed, narrative)
   - Error handling protocol (corrective, explanatory, silent)

4. **Identity Parameters**  
   - Name and title (professional, creative, fictional)
   - Visual identity (color scheme, iconography)
   - Voice characteristics (emotional range, pacing)

## Construction Methodology
1. **Baseline Assessment**  
   - Analyze task requirements and context
   - Identify stakeholder expectations

2. **Parameter Optimization**  
   - Use 8F pipeline for decision validation
   - Apply GDP protocol for subjective choices
   - Execute with quality floor ≥8.0

3. **Validation**  
   - Cross-check with brand guidelines
   - Test through simulated interactions
   - Receive user feedback for refinement

## Example Template
```yaml
agent_profile:
  role: n03-builder
  expertise:
    domain: technical_documentation
    proficiency: expert
    experience: master
  communication:
    tone: formal
    style: concise
    error_handling: corrective
  identity:
    name: Technical Architect
    colors:
      primary: #3B82F6
      accent: #60A4FF
    voice:
      emotional_range: analytical
      pacing: deliberate
```

## Applications
- Agent configuration in CEX systems
- Subagent deployment planning
- Brand identity alignment
- Cross-team collaboration frameworks

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent-profile-builder]] | downstream | 0.26 |
| [[bld_collaboration_agent]] | downstream | 0.26 |
| [[bld_collaboration_system_prompt]] | downstream | 0.25 |
| [[agent-builder]] | downstream | 0.23 |
| [[p03_sp_cex_core_identity]] | downstream | 0.21 |
| [[p03_sp_brand_nucleus]] | downstream | 0.21 |
| [[bld_knowledge_card_agent]] | sibling | 0.20 |
| [[p01_kc_brand_voice_consistency_channels]] | sibling | 0.20 |
| [[p03_sp_agent_profile_builder]] | downstream | 0.20 |
| [[p01_kc_agent]] | sibling | 0.20 |
