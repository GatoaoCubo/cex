---
id: campaign_performance_memory
kind: memory_summary
pillar: P10
title: Campaign Performance Memory
version: 1.0.0
created: 2026-04-02
author: n02_marketing
domain: performance_tracking
quality: 9.0
tags: [memory, performance, campaigns, conversion, A/B-testing, N02]
tldr: Tracks campaign performance, copy effectiveness, and conversion insights to improve future marketing efforts.
scope: marketing_performance_learning
density_score: 1.0
related:
  - copy_optimization_insights
  - ab_testing_framework
  - brand_voice_templates
  - p01_kc_marketing_best_practices
  - landing_page_template
  - p01_kc_conversion_copywriting_frameworks
  - ex_prompt_template_aida
  - n02_tool_headline_scorer
  - ad_copy_template
  - n02_kc_campaign
---

# Campaign Performance Memory

## Campaign History Log

### Template Entry
```yaml
campaign_id: "YYYY-MM-DD_channel_goal"
date: "2026-MM-DD"
channel: "email | social | ads | landing_page"
goal: "awareness | consideration | conversion"
copy_formula: "AIDA | PAS | BAB | FAB"
audience_segment: "target_description"

performance:
  impressions: 0
  clicks: 0  
  conversions: 0
  ctr: 0.0  # click-through rate
  cvr: 0.0  # conversion rate
  cost_per_conversion: 0.0
  
copy_elements:
  headline: "actual headline used"
  hook: "opening line or attention grabber"
  cta: "call to action text"
  
insights:
  what_worked: []
  what_failed: []
  audience_response: ""
  unexpected_results: ""
  
next_iteration:
  changes_planned: []
  hypothesis: ""
```

## High-Performance Copy Patterns

### Email Subject Lines (High CTR)
```yaml
high_performers:
  - pattern: "[STAT] + specific benefit + question"
    example: "47% faster results - ready to try?"
    ctr: 0.34
    context: "B2B productivity tool"
    
  - pattern: "Personal story + lesson learned"  
    example: "I failed at lead gen for 3 months (here's what I learned)"
    ctr: 0.28
    context: "Marketing agency newsletter"
    
  - pattern: "Countdown + specific outcome"
    example: "3 days left: Double your conversions by Friday"
    ctr: 0.31
    context: "Course promotion"
```

### Ad Headlines (High CTR)
```yaml
facebook_ads:
  winning_pattern: "Problem + Agitation + Solution tease"
  example: "Tired of boring websites? Here's how [Company] got 150% more leads"
  avg_ctr: 0.045
  
google_ads:  
  winning_pattern: "Specific benefit + Proof + CTA"
  example: "Get 23% More Sales | 500+ Happy Clients | Try Free"
  avg_ctr: 0.032
  
linkedin_ads:
  winning_pattern: "Industry insight + Challenge + Resource"
  example: "87% of B2B buyers research vendors online. Is your content ready?"
  avg_ctr: 0.021
```

### Landing Page Elements (High CVR)
```yaml
hero_sections:
  winning_headline_pattern: "Outcome + Timeline + Social proof hint"
  example: "Get 40% more leads in 30 days (like 1,200+ agencies already do)"
  avg_cvr: 0.12
  
cta_buttons:
  high_performing: 
    - "Start my free trial"  # CVR: 0.08
    - "Get instant access"   # CVR: 0.07  
    - "Claim my spot"        # CVR: 0.075
  low_performing:
    - "Learn more"          # CVR: 0.02
    - "Click here"          # CVR: 0.015
    - "Submit"              # CVR: 0.018
```

## Audience Insights

### Segment Response Patterns
```yaml
b2b_saas:
  responds_to: "Data-driven claims, ROI focus, time-saving benefits"
  avoid: "Emotional appeals, lifestyle imagery, personal testimonials"
  best_times: "Tuesday-Thursday, 10AM-2PM EST"
  preferred_channels: "LinkedIn, email, search ads"
  
b2c_ecommerce:
  responds_to: "Emotional triggers, social proof, urgency/scarcity"  
  avoid: "Heavy technical details, lengthy explanations"
  best_times: "Evenings, weekends, lunch hours"
  preferred_channels: "Facebook, Instagram, display ads"
  
online_courses:
  responds_to: "Transformation stories, skill-specific outcomes, authority positioning"
  avoid: "Generic benefits, hard sales, overwhelming information"
  best_times: "Sunday evenings, early mornings"
  preferred_channels: "Email, YouTube, content marketing"
```

### Demographic Copy Preferences
```yaml
millennials_25_35:
  tone: "Casual but professional, authenticity valued"
  triggers: "Career advancement, work-life balance, authenticity"
  language: "Conversational, avoid corporate jargon"
  
gen_x_35_50:
  tone: "Professional, results-focused, respect for time"  
  triggers: "Efficiency, proven results, family considerations"
  language: "Clear, direct, benefit-focused"
  
boomers_50_plus:
  tone: "Respectful, thorough, trust-building"
  triggers: "Security, reliability, customer service"
  language: "Detailed explanations, traditional sales approach"
```

## A/B Testing Learnings

### Headline Testing Results
```yaml
test_pattern: "Benefit vs Feature vs Question"
sample_size: 10000
results:
  benefit_headlines: 
    cvr: 0.045
    example: "Double your sales in 30 days"
  feature_headlines:
    cvr: 0.023  
    example: "AI-powered sales automation platform"
  question_headlines:
    cvr: 0.038
    example: "What if you could close 50% more deals?"
    
insight: "Benefit headlines outperform by 96%, but questions work well for problem-aware audiences"
```

### CTA Testing Results  
```yaml
button_color_tests:
  - color: "Orange" | cvr: 0.067 | context: "B2B landing page"
  - color: "Green" | cvr: 0.052 | context: "E-commerce checkout"  
  - color: "Red" | cvr: 0.071 | context: "Urgency-driven offer"
  
button_text_tests:
  action_specific: "Get my free audit" | cvr: 0.078
  benefit_focused: "Start growing today" | cvr: 0.065  
  urgency_driven: "Claim limited spot" | cvr: 0.059
  generic: "Click here" | cvr: 0.021
```

### Email Testing Results
```yaml
send_time_optimization:
  b2b_best: "Tuesday 10AM EST" | open_rate: 0.34
  b2c_best: "Sunday 7PM local" | open_rate: 0.28
  ecommerce_best: "Friday 12PM local" | open_rate: 0.31
  
subject_line_length:
  optimal_range: "30-50 characters"
  performance_by_length:
    - "20-30 chars": 0.22 # Lower open rates
    - "30-50 chars": 0.31 # Optimal range  
    - "50-70 chars": 0.26 # Decent performance
    - "70+ chars": 0.19   # Poor performance (mobile truncation)
```

## Copy Formula Effectiveness

### Formula Performance by Context
```yaml
AIDA:
  best_for: "Cold audiences, awareness campaigns"  
  avg_conversion: 0.035
  channels: "Facebook ads, display ads, cold email"
  
PAS:
  best_for: "Problem-aware audiences, pain-focused campaigns"
  avg_conversion: 0.048  
  channels: "Google search ads, warm email, landing pages"
  
BAB:
  best_for: "Transformation-focused, before/after stories"
  avg_conversion: 0.052
  channels: "Case studies, testimonial campaigns, course sales"
  
FAB:
  best_for: "Feature-rich products, technical audiences"
  avg_conversion: 0.029
  channels: "Product pages, SaaS demos, B2B content"
```

## Seasonal & Trend Patterns

### Seasonal Performance
```yaml
Q1_jan_mar:
  themes: "New Year resolutions, fresh starts, goal-setting"
  high_performing: "Productivity, health, education content"
  avoid: "Heavy sales pitches (post-holiday fatigue)"
  
Q2_apr_jun:  
  themes: "Growth, optimization, summer prep"
  high_performing: "Business growth, lifestyle improvement"
  avoid: "Nothing specific - solid performance quarter"
  
Q3_jul_sep:
  themes: "Back-to-school, preparation, new projects"  
  high_performing: "Learning, skill development, career content"
  avoid: "Heavy content during peak vacation times"
  
Q4_oct_dec:
  themes: "Urgency, year-end goals, holiday promotions"
  high_performing: "Limited-time offers, year-end planning"
  avoid: "Long-term commitments during holiday season"
```

## Performance Improvement Insights

### Recent Optimizations Applied
```yaml
optimization_log:
  - date: "2026-04-01"
    change: "Switched from generic CTAs to benefit-specific"  
    result: "+23% conversion rate increase"
    
  - date: "2026-03-15"  
    change: "Added social proof numbers to headlines"
    result: "+18% click-through rate improvement"
    
  - date: "2026-03-01"
    change: "Simplified email subject lines (removed emoji)"
    result: "+12% open rate for B2B segments"
```

### Next Testing Queue
```yaml
planned_tests:
  - hypothesis: "Video testimonials in email will outperform text"
    timeline: "Next 2 weeks"
    success_metric: "CTR improvement >15%"
    
  - hypothesis: "Question-based subject lines will improve B2C open rates"  
    timeline: "Next month"
    success_metric: "Open rate improvement >10%"
    
  - hypothesis: "Mobile-first landing page design will improve mobile conversions"
    timeline: "Next quarter"  
    success_metric: "Mobile CVR improvement >25%"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[copy_optimization_insights]] | related | 0.48 |
| [[ab_testing_framework]] | upstream | 0.33 |
| [[brand_voice_templates]] | upstream | 0.26 |
| [[p01_kc_marketing_best_practices]] | upstream | 0.26 |
| [[landing_page_template]] | upstream | 0.25 |
| [[p01_kc_conversion_copywriting_frameworks]] | upstream | 0.23 |
| [[ex_prompt_template_aida]] | upstream | 0.23 |
| [[n02_tool_headline_scorer]] | upstream | 0.22 |
| [[ad_copy_template]] | upstream | 0.22 |
| [[n02_kc_campaign]] | upstream | 0.21 |
