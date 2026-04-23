---
id: brand_voice_templates
kind: prompt_template
pillar: P03
title: Brand Voice Templates — Tone & Messaging Calibration
version: 1.0.0
created: 2026-04-02
author: n02_marketing
domain: brand_voice_copywriting
quality: 9.0
tags: [prompt_template, brand_voice, tone, messaging, audience, N02]
tldr: Brand voice calibration templates for different audiences, channels, and funnel stages — ensures consistent brand personality across all marketing copy.
voice_dimensions: [tone, formality, personality, energy, perspective]
density_score: 1.0
related:
  - brand_override_config
  - p01_kc_brand_voice_consistency_channels
  - ex_prompt_template_aida
  - ad_copy_template
  - landing_page_template
  - copy_optimization_insights
  - p03_brand_discovery_interview
  - p07_sr_5d_marketing
  - n06_kc_icp_frameworks
  - ex_feedback_tone_correction
---

# Brand Voice Templates — Tone & Messaging Calibration

## 1. Voice Dimension Framework

### Core Brand Voice Variables
```yaml
brand_voice_config:
  tone:
    scale: "professional ←→ conversational ←→ casual"
    position: "{{BRAND_TONE_POSITION | default: '60% conversational'}}"
    
  formality:
    scale: "formal ←→ semi-formal ←→ informal"  
    position: "{{BRAND_FORMALITY | default: '70% semi-formal'}}"
    
  personality:
    primary: "{{BRAND_PERSONALITY_PRIMARY | default: 'confident'}}"  # confident | humble | bold | thoughtful
    secondary: "{{BRAND_PERSONALITY_SECONDARY | default: 'helpful'}}"  # helpful | witty | authoritative | friendly
    
  energy:
    level: "{{BRAND_ENERGY_LEVEL | default: 'moderate'}}"  # calm | moderate | energetic | high-intensity
    expression: "{{BRAND_ENERGY_EXPRESSION | default: 'steady'}}"  # steady | bursts | building | varied
    
  perspective:
    person: "{{BRAND_PERSON | default: '2nd_person'}}"  # 1st (we) | 2nd (you) | 3rd (customers)
    relationship: "{{BRAND_RELATIONSHIP | default: 'peer'}}"  # expert | peer | guide | coach
```

---

## 2. Audience-Specific Voice Adaptations

### B2B Professional Audience
```yaml
b2b_professional_voice:
  tone_adjustment: "+20% professional, +10% authoritative"
  language_preferences:
    vocabulary: "Industry terminology acceptable, avoid overly casual"
    sentence_structure: "Slightly longer sentences, complex ideas welcome"
    examples: "Business case studies, ROI-focused, data-driven"
    
  messaging_framework:
    opening_style: "Industry insight or business challenge"
    benefit_focus: "Efficiency, cost savings, competitive advantage"
    proof_format: "Case studies, statistics, testimonials from similar businesses"
    cta_style: "Professional action-oriented (Schedule demo, Get proposal)"
    
  template_example: |
    "For [INDUSTRY] leaders managing [CHALLENGE], [SOLUTION] delivers [SPECIFIC_OUTCOME].
    
    Companies like [CUSTOMER_EXAMPLE] have seen [QUANTIFIED_RESULT] in just [TIMEFRAME].
    
    [CTA: Get your custom ROI analysis]"
```

### B2C Consumer Audience  
```yaml
b2c_consumer_voice:
  tone_adjustment: "+30% conversational, +20% relatable"
  language_preferences:
    vocabulary: "Simple, everyday language, emotional resonance"
    sentence_structure: "Shorter sentences, easy scanning"
    examples: "Personal stories, lifestyle benefits, transformation"
    
  messaging_framework:
    opening_style: "Personal question or relatable scenario"
    benefit_focus: "Lifestyle improvement, emotional satisfaction, convenience"
    proof_format: "Customer stories, before/after, social proof"
    cta_style: "Benefit-focused (Start feeling better today, Get instant access)"
    
  template_example: |
    "Tired of [RELATABLE_PROBLEM]? You're not alone.
    
    [CUSTOMER_NAME] felt the same way until they discovered [SOLUTION].
    
    Now they're [POSITIVE_OUTCOME] and couldn't be happier.
    
    [CTA: Start your transformation today]"
```

### Technical/Developer Audience
```yaml
technical_audience_voice:
  tone_adjustment: "+40% technical precision, +20% direct"
  language_preferences:
    vocabulary: "Technical accuracy critical, industry jargon expected"
    sentence_structure: "Precise, logical flow, specifications welcome"
    examples: "Code snippets, architecture diagrams, implementation details"
    
  messaging_framework:
    opening_style: "Technical problem or inefficiency statement"
    benefit_focus: "Performance, scalability, maintainability, developer experience"
    proof_format: "Benchmarks, technical specs, community adoption"
    cta_style: "Action-specific (View documentation, Try the API, Download SDK)"
    
  template_example: |
    "[TECHNICAL_CHALLENGE] is slowing down your development cycle.
    
    [SOLUTION] reduces [SPECIFIC_METRIC] by [PERCENTAGE] while maintaining [QUALITY_STANDARD].
    
    Join [NUMBER] developers already using [PRODUCT] in production.
    
    [CTA: Start with our 5-minute quickstart]"
```

---

## 3. Channel-Specific Voice Calibration

### Email Marketing Voice
```yaml
email_voice_settings:
  subject_lines:
    tone: "{{BRAND_EMAIL_SUBJECT_TONE | default: 'curiosity-driven'}}"  # benefit-focused | curiosity-driven | direct
    length: "{{BRAND_EMAIL_SUBJECT_LENGTH | default: '30-50_chars'}}"
    personalization: "{{BRAND_EMAIL_PERSONALIZATION | default: 'first_name'}}"
    
  body_copy:
    greeting: "{{BRAND_EMAIL_GREETING | default: 'Hi [FIRST_NAME]'}}"  # Hi | Hey | Hello | [FIRST_NAME]
    tone_shift: "+10% personal, +15% conversational"
    paragraph_length: "2-4 sentences maximum"
    closing: "{{BRAND_EMAIL_CLOSING | default: 'Best'}}"  # Best | Cheers | Thanks | [SENDER_NAME]
    
  template_structure: |
    "[GREETING],
    
    [HOOK - personal or relevant opening]
    
    [VALUE - main message or content]
    
    [CTA - clear next step]
    
    [CLOSING],
    [SENDER_NAME]
    
    P.S. [ADDITIONAL_VALUE or URGENCY]"
```

### Social Media Voice
```yaml
social_media_voice:
  platform_adaptations:
    linkedin:
      tone_adjustment: "+20% professional, +10% thought-leadership"
      content_style: "Industry insights, professional growth, business value"
      hashtag_strategy: "{{BRAND_LINKEDIN_HASHTAGS | default: '3-5_industry_specific'}}"
      
    instagram:
      tone_adjustment: "+40% visual-storytelling, +30% lifestyle"
      content_style: "Behind-scenes, visual stories, lifestyle integration" 
      hashtag_strategy: "{{BRAND_INSTAGRAM_HASHTAGS | default: '10-15_mixed'}}"
      
    twitter_x:
      tone_adjustment: "+50% conversational, +20% timely"
      content_style: "Quick insights, industry commentary, real-time engagement"
      hashtag_strategy: "{{BRAND_TWITTER_HASHTAGS | default: '1-3_trending'}}"
      
  universal_guidelines:
    response_time: "Within 2 hours during business hours"
    engagement_style: "{{BRAND_SOCIAL_ENGAGEMENT | default: 'helpful_and_genuine'}}"
    controversy_handling: "{{BRAND_CONTROVERSY_APPROACH | default: 'acknowledge_and_redirect'}}"
```

### Advertising Copy Voice
```yaml
advertising_voice:
  attention_getting:
    hook_style: "{{BRAND_AD_HOOK_STYLE | default: 'problem_agitation'}}"  # curiosity_gap | problem_agitation | benefit_promise
    urgency_level: "{{BRAND_AD_URGENCY | default: 'moderate'}}"  # low | moderate | high
    
  persuasion_approach:
    proof_preference: "{{BRAND_AD_PROOF | default: 'social_statistics'}}"  # social_proof | statistics | authority | testimonials
    objection_handling: "{{BRAND_AD_OBJECTIONS | default: 'address_directly'}}"  # address_directly | implicit_reassurance | ignore
    
  channel_specifics:
    facebook_ads:
      tone: "+20% social, +15% storytelling"
      format: "Hook → Story → Offer → CTA"
      
    google_ads:
      tone: "+30% direct, +20% benefit-focused"
      format: "Benefit → Proof → CTA"
      
    linkedin_ads:
      tone: "+25% professional, +15% authority"
      format: "Industry insight → Solution → CTA"
```

---

## 4. Funnel Stage Voice Progression

### Awareness Stage Voice
```yaml
awareness_voice:
  primary_goal: "Stop the scroll, create interest"
  tone_characteristics: "Intriguing, educational, non-threatening"
  
  messaging_approach:
    problem_identification: "Help them recognize challenge they face"
    education_focus: "Provide valuable insights without selling"
    trust_building: "Establish credibility and expertise"
    
  copy_formulas: "AIDA (Attention + Interest focus)"
  cta_style: "Soft (Learn more, Discover, Explore)"
  
  template: |
    "[ATTENTION_GRABBING_STAT or QUESTION]
    
    [INSIGHT that reframes their thinking]
    
    [VALUE_CONTENT that helps immediately]
    
    [SOFT_CTA to continue learning]"
```

### Consideration Stage Voice
```yaml
consideration_voice:
  primary_goal: "Build preference, address objections"
  tone_characteristics: "Confident, helpful, comparison-friendly"
  
  messaging_approach:
    solution_positioning: "Present your approach vs alternatives"
    benefit_stacking: "Layer multiple value propositions"
    risk_reduction: "Address concerns and objections"
    
  copy_formulas: "PAS (Problem + Agitation + Solution) or BAB (Before + After + Bridge)"
  cta_style: "Medium pressure (See how, Compare options, Try free)"
  
  template: |
    "Looking for [SOLUTION_CATEGORY]? Here's what sets [BRAND] apart:
    
    ✓ [UNIQUE_ADVANTAGE_1]
    ✓ [UNIQUE_ADVANTAGE_2]  
    ✓ [UNIQUE_ADVANTAGE_3]
    
    Plus, [RISK_REDUCER like guarantee or trial]
    
    [MEDIUM_PRESSURE_CTA]"
```

### Decision Stage Voice
```yaml
decision_voice:
  primary_goal: "Remove final objections, drive action"
  tone_characteristics: "Confident, urgent, reassuring"
  
  messaging_approach:
    urgency_creation: "Time-sensitive reasons to act now"
    final_objection_handling: "Address last hesitations"
    action_simplification: "Make next step easy and clear"
    
  copy_formulas: "Offer + Urgency + Guarantee + Strong CTA"
  cta_style: "Strong action (Buy now, Start today, Get instant access)"
  
  template: |
    "Ready to [ACHIEVE_DESIRED_OUTCOME]?
    
    [COMPELLING_OFFER with clear value]
    
    [URGENCY_ELEMENT - limited time/quantity/bonus]
    
    [GUARANTEE or RISK_REVERSAL]
    
    [STRONG_CTA_WITH_URGENCY]"
```

---

## 5. Voice Quality Assurance

### Voice Consistency Checklist
```yaml
consistency_audit:
  tone_alignment:
    - "Does copy match brand tone position on scale?"
    - "Is formality level appropriate for audience?"
    - "Does personality come through in word choice?"
    
  audience_appropriateness:
    - "Language complexity matches audience sophistication?"
    - "Examples and references resonate with target?"
    - "Cultural sensitivity and inclusivity maintained?"
    
  channel_optimization:
    - "Format optimized for channel constraints?"
    - "Engagement style matches platform norms?"
    - "CTA strength appropriate for channel context?"
```

### Voice Testing Framework
```yaml
voice_testing:
  a_b_test_scenarios:
    - "Formal vs conversational tone"
    - "Expert vs peer positioning"
    - "Feature-focused vs benefit-focused language"
    - "Direct vs storytelling approach"
    
  measurement_criteria:
    primary: "Engagement rate (CTR, open rate, etc.)"
    secondary: "Brand perception survey responses"
    qualitative: "Customer feedback and comments analysis"
```

---

## 6. Dynamic Voice Adaptation

### Contextual Voice Modifiers
```yaml
situational_adjustments:
  crisis_communication:
    tone_shift: "+40% empathetic, +30% direct, -20% promotional"
    messaging_focus: "Acknowledgment, support, clear action steps"
    
  product_launch:
    tone_shift: "+30% excited, +20% confident, +10% urgent"
    messaging_focus: "Innovation, benefits, early adopter advantage"
    
  customer_service:
    tone_shift: "+50% helpful, +30% patient, +20% solution-focused"
    messaging_focus: "Understanding, resolution, relationship preservation"
    
  seasonal_campaigns:
    holiday_periods: "+20% celebratory, +15% urgent (gift-giving)"
    new_year: "+25% motivational, +20% fresh-start"
    summer: "+20% relaxed, +15% lifestyle-focused"
```

### Personalization Variables
```yaml
dynamic_personalization:
  customer_lifecycle:
    new_subscriber: "Welcome tone, educational focus"
    engaged_customer: "Peer tone, advanced content"
    at_risk_customer: "Concerned tone, value reinforcement"
    
  behavioral_triggers:
    high_engagement: "Insider tone, exclusive content"
    low_engagement: "Re-engagement tone, simplified messaging"
    purchase_intent: "Confident tone, decision support"
```

This brand voice template system ensures consistent, audience-appropriate messaging across all marketing touchpoints while maintaining the flexibility to optimize for different contexts and objectives.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[brand_override_config]] | downstream | 0.36 |
| [[p01_kc_brand_voice_consistency_channels]] | upstream | 0.24 |
| [[ex_prompt_template_aida]] | sibling | 0.19 |
| [[ad_copy_template]] | sibling | 0.19 |
| [[landing_page_template]] | sibling | 0.19 |
| [[copy_optimization_insights]] | downstream | 0.19 |
| [[p03_brand_discovery_interview]] | sibling | 0.18 |
| [[p07_sr_5d_marketing]] | downstream | 0.18 |
| [[n06_kc_icp_frameworks]] | upstream | 0.17 |
| [[ex_feedback_tone_correction]] | downstream | 0.16 |
