---
id: cross_nucleus_handoffs
kind: handoff_protocol
pillar: P12
title: "Cross-Nucleus Handoff Protocols for N02 Marketing"
version: 2.0.0
created: 2026-04-02
updated: 2026-04-07
author: n02_marketing
domain: nucleus_coordination
quality: null
tags: [handoff, coordination, N01, N02, N03, N04, N05, N06, cross-nucleus, signal-writer]
tldr: "Defines handoff protocols between N02 Marketing and all nuclei — signal_writer integration, retry strategies, GATO³ brand injection rules, and quality gates at every handoff boundary."
handoff_types: [research_to_copy, copy_to_deployment, copy_to_commercial, copy_to_knowledge, feedback_loop]
density_score: 1.0
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

## 7. Signal Writer Integration

### Standard Signal Protocol for N02 Handoffs

Every N02 handoff completion MUST emit a signal. This enables N07 orchestrator polling and prevents lost handoffs.

```python
# On handoff completion — N02 emits signal
from _tools.signal_writer import write_signal

# After completing copy for N05 deployment
write_signal('n02', 'handoff_n05_complete', 9.0, 'COPY_DEPLOYMENT_READY')

# After receiving research from N01
write_signal('n02', 'handoff_n01_received', None, 'RESEARCH_BRIEF_INGESTED')

# After aligning with N06 commercial
write_signal('n02', 'handoff_n06_aligned', None, 'COMMERCIAL_COPY_READY')
```

### Signal-Based Handoff Flow
```yaml
handoff_signals:
  n01_to_n02:
    trigger_signal: "n01.research_complete"
    n02_acknowledges: "n02.research_received"
    n02_completes: "n02.copy_from_research_done"
    timeout_ms: 1800000
    on_timeout: "n07_escalation"

  n02_to_n05:
    trigger_signal: "n02.copy_ready"
    n05_acknowledges: "n05.copy_received"
    n05_completes: "n05.deployment_live"
    timeout_ms: 3600000
    on_timeout: "n07_escalation"

  n02_to_n06:
    trigger_signal: "n02.commercial_copy_draft"
    n06_acknowledges: "n06.copy_review_started"
    n06_completes: "n06.copy_approved"
    timeout_ms: 1200000
    on_timeout: "n02_proceeds_with_draft"

  n02_to_n03:
    trigger_signal: "n02.visual_brief_ready"
    n03_acknowledges: "n03.design_started"
    n03_completes: "n03.visual_assets_delivered"
    timeout_ms: 2400000
    on_timeout: "n02_uses_template_fallback"

  n02_to_n04:
    trigger_signal: "n02.kc_update_request"
    n04_acknowledges: "n04.kc_review_started"
    n04_completes: "n04.kc_published"
    timeout_ms: 1800000
    on_timeout: "n02_proceeds_without_kc"
```

## 8. Retry & Failure Strategies

### Handoff Failure Taxonomy
```yaml
failure_types:
  timeout:
    definition: "Receiving nucleus doesn't acknowledge within timeout_ms"
    strategy: "Retry once → escalate to N07 → continue with degraded mode"
    degraded_mode: "N02 self-serves (e.g., uses template instead of N03 custom design)"

  quality_rejection:
    definition: "Receiving nucleus rejects deliverable (quality < 8.0)"
    strategy: "N02 re-runs artifact through 8F pipeline → resubmit"
    max_retries: 2
    escalation: "After 2 rejections → N07 mediates requirements alignment"

  context_loss:
    definition: "Handoff file missing critical context (brand, audience, etc.)"
    strategy: "Auto-inject brand_config.yaml → retry with enriched context"
    prevention: "All handoff files MUST include brand_context reference"

  signal_failure:
    definition: "signal_writer fails (file permissions, path error)"
    strategy: "Fallback to .cex/runtime/handoffs/n02_status.md manual update"
    prevention: "Pre-flight check signal_writer path on nucleus boot"
```

### Retry Decision Matrix
```yaml
retry_matrix:
  should_retry:
    - "Timeout (network/scheduling issue, not content issue)"
    - "Quality 7.5-7.9 (close to threshold, small fix likely)"
    - "Signal failure (transient error)"
  should_NOT_retry:
    - "Quality < 7.0 (fundamental misunderstanding, needs human)"
    - "3rd consecutive failure (systemic issue)"
    - "Brand violation detected (Ro anti-patterns present)"
  should_escalate:
    - "Cross-nucleus disagreement on requirements"
    - "GDP decision needed (subjective, user must decide)"
    - "Budget exhaustion (no tokens left for retry)"
```

## 9. GATO³ Brand Injection at Handoff Boundaries

### Mandatory Brand Context in Every Handoff

```yaml
gato3_handoff_rules:
  outgoing_handoffs:
    always_include:
      - "brand_config_path: .cex/brand/brand_config.yaml"
      - "persona: Ro"
      - "voice: sofisticado-acolhedor"
      - "language: pt-BR"
      - "forbidden_words: [gatinho, garantido, compre agora, dono]"
    validation: "brand_validate.py must pass before handoff emitted"

  incoming_handoffs:
    always_verify:
      - "Does incoming content respect GATO³ brand voice?"
      - "Are BRAND_* variables populated (not placeholder)?"
      - "Is language pt-BR (not EN defaults)?"
    on_violation: "N02 sanitizes before processing, logs violation"
```

This handoff protocol ensures seamless coordination between N02 and other nuclei, preventing information loss and enabling compound effectiveness across the CEX system.