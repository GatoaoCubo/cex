---
id: cross_nucleus_handoffs
kind: handoff_protocol
pillar: P12
title: Cross-Nucleus Handoff Protocols for N02 Marketing  
version: 1.0.0
created: 2026-04-02
author: n02_marketing
domain: nucleus_coordination
quality: 9.0
tags: [handoff, coordination, N01, N02, N05, N06, cross-nucleus]
tldr: Defines handoff protocols between N02 Marketing and other nuclei for seamless research→copy→deployment→commercial workflows.
handoff_types: [research_to_copy, copy_to_deployment, copy_to_commercial, feedback_loop]
density_score: 1.0
related:
  - n02_self_review_2026-04-02
  - n02_leverage_map_v2_verification
  - p12_wf_visual_frontend_marketing
  - p12_dr_visual_frontend_marketing
  - p08_ac_visual_frontend_marketing
  - p03_sp_marketing_nucleus
  - n02_leverage_map_v2_iteration2
  - n02_tool_copy_analyzer
  - p02_nd_n02.md
  - p08_ac_n02
---

# Cross-Nucleus Handoff Protocols — N02 Marketing

## 1. N01 Research → N02 Marketing

### Handoff: Research Insights to Marketing Angles

**When**: N01 completes market research, competitive analysis, or audience insights  
**Purpose**: Transform research findings into actionable marketing copy briefs  
**Format**: `research_to_copy_brief.md`

#### Input from N01
```yaml
research_brief:
  research_type: "market_analysis | competitive_intel | audience_research | trend_analysis"
  target_audience:
    primary_segment: ""
    demographics: {}
    psychographics: {}
    pain_points: []
    desires: []
    
  key_findings:
    insights: []
    opportunities: []
    threats: []
    gaps_in_market: []
    
  competitive_landscape:
    direct_competitors: []
    messaging_analysis: {}
    positioning_gaps: []
    
  recommendations:
    positioning_strategy: ""
    messaging_priorities: []
    channel_recommendations: []
```

#### N02 Processing
```yaml
marketing_translation:
  copy_angles:
    primary_angle: ""  # Main value proposition
    supporting_angles: []  # Secondary benefits
    emotional_triggers: []  # Fear, desire, aspiration
    
  messaging_framework:
    headline_directions: []
    hook_concepts: []
    benefit_stack: []
    objection_handles: []
    
  channel_adaptations:
    email: "messaging_adaptation"
    social: "messaging_adaptation"  
    ads: "messaging_adaptation"
    landing_pages: "messaging_adaptation"
    
  copy_formula_selection:
    primary_formula: "AIDA | PAS | BAB | FAB"
    rationale: ""
```

#### Output to Campaign
```yaml
campaign_brief:
  campaign_goal: ""
  target_audience: ""  # From research
  key_message: ""  # Core value prop
  copy_strategy: ""  # Formula + approach
  channel_mix: []  # Priority channels
  success_metrics: []
```

---

## 2. N02 Marketing → N05 Operations (Deployment)

### Handoff: Copy Deployment Package

**When**: N02 completes copy creation and needs technical deployment  
**Purpose**: Provide N05 with everything needed for copy deployment  
**Format**: `copy_deployment_package.md`

#### Input from N02
```yaml
copy_deliverables:
  final_copy:
    headlines: []
    body_copy: ""
    cta_text: ""
    meta_descriptions: []  # For web deployment
    
  a_b_variants:
    variant_a: {}
    variant_b: {}
    test_hypothesis: ""
    success_metric: ""
    
  technical_requirements:
    deployment_channels: []  # email, web, social, ads
    timing_requirements: ""
    personalization_variables: []
    tracking_parameters: []
    
  brand_assets_needed:
    images: []
    videos: []  
    fonts: []
    color_codes: []
```

#### N05 Requirements
```yaml
deployment_checklist:
  technical_setup:
    - "Copy uploaded to platform"
    - "A/B testing configured"  
    - "Tracking pixels implemented"
    - "Personalization tokens mapped"
    
  quality_assurance:
    - "Responsive display testing"
    - "Cross-browser compatibility"
    - "Mobile optimization verified"
    - "Link functionality confirmed"
    
  go_live:
    - "Launch date confirmed"
    - "Backup/rollback plan ready"
    - "Performance monitoring activated"
```

#### Success Handoff Criteria
```yaml
deployment_complete:
  deliverables:
    - "Live copy with tracking"
    - "A/B test running"  
    - "Performance dashboard active"
    - "Issue escalation path defined"
    
  performance_expectations:
    baseline_metrics: {}
    target_improvements: {}
    review_schedule: ""
```

---

## 3. N02 Marketing ↔ N06 Commercial

### Handoff: Copy-Commercial Alignment

**When**: Copy involves pricing, offers, or sales messaging  
**Purpose**: Ensure copy aligns with commercial strategy and pricing  
**Format**: `copy_commercial_alignment.md`

#### N02 → N06: Copy with Commercial Implications
```yaml
commercial_copy_brief:
  copy_type: "pricing_page | sales_email | offer_landing_page | upsell_sequence"
  
  pricing_elements:
    price_points_mentioned: []
    value_propositions: []
    comparison_frameworks: []  # vs competitors
    
  offer_structure:
    primary_offer: ""
    bonuses_mentioned: []
    guarantees: []
    scarcity_elements: []
    
  objection_handling:
    price_objections: []
    value_objections: []  
    trust_objections: []
```

#### N06 → N02: Commercial Strategy Input
```yaml
commercial_guidance:
  pricing_strategy:
    price_positioning: "premium | mid_market | value | penetration"
    messaging_priorities: []
    avoid_comparisons: []
    
  offer_optimization:
    strongest_benefits: []  # Lead with these
    proof_points: []  # Use for credibility
    urgency_elements: []  # When appropriate
    
  sales_process_alignment:
    funnel_stage: "awareness | consideration | decision"
    next_step_goal: ""
    handoff_to_sales: "yes | no"
```

#### Coordinated Output
```yaml
aligned_copy:
  messaging: "Commercial strategy + copy expertise"
  pricing_communication: "Clear, confident, value-focused"
  sales_enablement: "Copy supports sales process"
  performance_tracking: "Commercial + marketing metrics"
```

---

## 4. Performance Feedback Loops

### N05 → N02: Performance Data Handoff

**When**: Copy has been live for sufficient time to gather data  
**Purpose**: Provide performance insights to improve future copy  
**Format**: `copy_performance_feedback.md`

#### Performance Data from N05
```yaml
performance_results:
  channel_performance:
    email:
      open_rate: 0.0
      click_rate: 0.0
      conversion_rate: 0.0
      
    landing_pages:
      traffic: 0
      bounce_rate: 0.0
      conversion_rate: 0.0
      time_on_page: 0
      
    ads:
      impressions: 0  
      ctr: 0.0
      cpc: 0.0
      conversion_rate: 0.0
      
  a_b_test_results:
    winning_variant: ""
    performance_difference: ""
    statistical_significance: true/false
    
  user_behavior:
    heat_maps: "link_to_data"
    scroll_depth: {}
    click_patterns: {}
```

#### N02 Learning Integration
```yaml
copy_insights:
  what_worked:
    headlines: []
    hooks: []
    ctas: []
    
  what_failed:
    low_performing_elements: []
    hypotheses_disproven: []
    
  optimization_opportunities:
    immediate_fixes: []
    test_ideas: []
    strategic_pivots: []
    
  memory_updates:
    pattern_additions: []
    audience_insights: []
    formula_effectiveness: {}
```

---

## 5. Handoff Workflow Process

### Standard Operating Procedure

#### Step 1: Handoff Request
```bash
# N02 requests handoff to another nucleus
# Create handoff file in .cex/runtime/handoffs/
echo "Creating handoff: N02 → N0X"
cp templates/handoff_template.md .cex/runtime/handoffs/N02_to_N0X_$(date +%Y%m%d).md
```

#### Step 2: Receiving Nucleus Processing
```bash
# Receiving nucleus processes handoff
# Updates handoff file with acceptance + timeline
echo "N0X accepting handoff from N02"
# Begin processing with full context
```

#### Step 3: Completion & Feedback
```bash
# Receiving nucleus completes work
# Signals completion + provides feedback
python _tools/signal_writer.py n0x complete 8.5 "HANDOFF_N02_COMPLETE"
```

#### Step 4: Loop Closure  
```bash
# N02 integrates feedback into memory
# Updates performance tracking
# Improves future handoff quality
```

### Emergency Handoff Protocol

#### When Standard Handoff Fails
```yaml
escalation_path:
  level_1: "Retry with clarified requirements"
  level_2: "N07 orchestrator mediation"  
  level_3: "Manual coordination call"
  level_4: "Task restructuring"
```

#### Quality Gates for Handoffs
```yaml
handoff_quality_checks:
  completeness: "All required fields filled"
  clarity: "Requirements unambiguous"  
  actionability: "Receiving nucleus can execute immediately"
  trackability: "Success metrics defined"
```

## 6. Templates & Checklists

### Research → Marketing Brief Template
```markdown
# Research to Marketing Brief

## Research Summary
- **Research Type**: [type]
- **Key Finding**: [most important insight]
- **Target Audience**: [primary segment]

## Marketing Translation
- **Core Message**: [value proposition]  
- **Emotional Hook**: [primary trigger]
- **Copy Formula**: [AIDA/PAS/BAB/FAB + rationale]
- **Channel Priority**: [ranked list]

## Success Metrics
- **Primary KPI**: [main goal]
- **Supporting Metrics**: [secondary measurements]
- **Review Timeline**: [when to assess]
```

### Copy → Deployment Checklist
```markdown  
# Copy Deployment Checklist

## Copy Assets Ready
- [ ] Final headlines (3 variants)
- [ ] Body copy (A/B versions)  
- [ ] CTAs (2-3 options)
- [ ] Meta data (titles, descriptions)

## Technical Requirements
- [ ] Deployment channels confirmed
- [ ] Tracking parameters defined
- [ ] Personalization variables mapped
- [ ] A/B testing configured

## Launch Coordination  
- [ ] Go-live date confirmed
- [ ] Performance monitoring ready
- [ ] Issue escalation path defined
- [ ] Success criteria agreed upon
```

This handoff protocol ensures seamless coordination between N02 and other nuclei, preventing information loss and enabling compound effectiveness across the CEX system.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n02_self_review_2026-04-02]] | upstream | 0.44 |
| [[n02_leverage_map_v2_verification]] | upstream | 0.38 |
| [[p12_wf_visual_frontend_marketing]] | related | 0.34 |
| [[p12_dr_visual_frontend_marketing]] | related | 0.33 |
| [[p08_ac_visual_frontend_marketing]] | upstream | 0.32 |
| [[p03_sp_marketing_nucleus]] | upstream | 0.30 |
| [[n02_leverage_map_v2_iteration2]] | related | 0.29 |
| [[n02_tool_copy_analyzer]] | upstream | 0.29 |
| [[p02_nd_n02.md]] | upstream | 0.28 |
| [[p08_ac_n02]] | upstream | 0.27 |
