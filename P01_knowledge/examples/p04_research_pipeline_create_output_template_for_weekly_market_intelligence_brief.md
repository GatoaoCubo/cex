---
id: p04_research_pipeline_weekly_intelligence_template
kind: research_pipeline
pillar: P04
title: "Weekly Market Intelligence Brief - Output Template Pipeline"
version: 1.0.0
created: 2026-04-02
author: research-pipeline-builder
domain: market_intelligence
quality: 8.8
tags: [research-pipeline, weekly-brief, intelligence, template, STORM, CRAG, CRITIC]
tldr: "7-stage research pipeline with standardized output templates for weekly market intelligence briefs across multiple domains and formats"
density_score: 0.91
---
# Weekly Market Intelligence Brief - Output Template Pipeline

## Pipeline Architecture (7 Stages)

### Stage 1: INTENT Classification
**Model**: Fast classifier (Gemini Flash)
**Input**: Research query + domain + timeframe (weekly)
**Output**: Classified intent with brief type routing
```yaml
intent_types:
  competitive_brief: competitor moves, pricing changes, product launches
  market_trend: demand shifts, seasonal patterns, emerging segments
  regulatory_brief: policy changes, compliance updates, industry standards
  consumer_sentiment: reviews, social mentions, satisfaction trends
  pricing_intelligence: price movements, promotional patterns, value perception
```

### Stage 2: PLAN (STORM Multi-Perspective)
**Model**: Reasoning model (GPT-4o mini)
**Input**: Classified intent + weekly timeframe
**Output**: 5 expert perspectives × 6-8 time-bounded sub-questions
```yaml
perspectives:
  market_analyst:
    focus: "volume trends, growth metrics, market share shifts this week"
    questions: ["What volume changes occurred in top 3 categories?", "Which competitors gained/lost share?", "What pricing adjustments were made?"]
  consumer_researcher:
    focus: "sentiment shifts, review patterns, social mentions this week"  
    questions: ["What sentiment changes occurred?", "Which products got negative reviews?", "What social trends emerged?"]
  competitive_intelligence:
    focus: "competitor moves, product launches, strategic changes this week"
    questions: ["What new products launched?", "Which competitors changed pricing?", "What marketing campaigns started?"]
  regulatory_monitor:
    focus: "policy updates, compliance changes, industry standards this week"
    questions: ["What regulations were announced?", "Which compliance deadlines approached?", "What industry standards updated?"]
  business_strategist:
    focus: "opportunities, threats, strategic implications for this week"
    questions: ["What opportunities opened?", "Which threats materialized?", "What strategic responses are needed?"]
```

### Stage 3: RETRIEVE (CRAG with Quality Gates)
**Model**: API orchestrator + Gemini Flash for quality scoring
**Input**: 30-40 sub-questions from STORM planning
**Output**: Scored, filtered results (≥0.7 quality threshold)
```yaml
source_categories:
  inbound_marketplaces: [mercadolivre, shopee, amazon, magalu, americanas]
  outbound_social: [youtube, reddit, twitter, tiktok, reclameaqui]  
  search_engines: [serper, exa, gemini_search, brave]
  trend_platforms: [pytrends, keepa, semrush, similar_web]
  news_feeds: [google_news, bing_news, reuters, industry_pubs]

quality_gates:
  marketplace_data: 0.8  # high precision needed for pricing
  social_mentions: 0.6   # social data naturally noisy
  news_articles: 0.7     # medium precision for trends  
  search_results: 0.7    # web search quality varies
```

### Stage 4: RESOLVE (Entity Deduplication)
**Model**: Deterministic + embedding similarity
**Input**: Raw scored results from multiple sources
**Output**: Deduplicated entities with source attribution
```yaml
resolution_strategy:
  products: EAN/GTIN matching + title similarity (>0.85)
  companies: name normalization + domain matching
  news_events: timestamp clustering + headline similarity
  social_mentions: author dedup + content hash matching
```

### Stage 5: SCORE (Gartner 7-Dimension Intelligence Scoring)
**Model**: Gemini Flash for rapid scoring
**Input**: Deduplicated entities
**Output**: Multi-dimensional scores per entity
```yaml
scoring_dimensions:
  relevance: 0.0-1.0     # how relevant to research query
  impact: 0.0-1.0        # potential business impact
  urgency: 0.0-1.0       # time sensitivity for response
  confidence: 0.0-1.0    # data quality and source reliability
  actionability: 0.0-1.0 # how actionable the insight is
  novelty: 0.0-1.0       # how new/unexpected the information
  strategic_value: 0.0-1.0 # long-term strategic importance
```

### Stage 6: SYNTHESIZE (Graph-of-Thoughts Multi-Model)
**Model**: Domain-specific model routing
**Input**: Scored, prioritized intelligence data
**Output**: Structured weekly brief sections
```yaml
synthesis_models:
  executive_summary: claude-3-sonnet    # concise, business-focused
  competitive_analysis: gpt-4o         # analytical depth
  market_trends: gemini-2.5-pro        # pattern recognition
  consumer_insights: claude-3-sonnet    # human behavior understanding
  recommendations: gpt-4o              # strategic reasoning
```

### Stage 7: VERIFY (CRITIC Self-Correction)
**Model**: Thinking model (o1-mini)
**Input**: Synthesized brief + source data
**Output**: Verified, corrected brief (max 3 iterations)
```yaml
verification_checks:
  factual_accuracy: cross-reference numbers with sources
  logical_consistency: ensure conclusions follow from data
  completeness: verify all STORM perspectives addressed
  bias_detection: flag potential analytical bias
  recommendation_quality: assess actionability and specificity
```

## Output Template Structure

### Weekly Brief Template (HTML + PPTX + JSON)
```yaml
template_sections:
  header:
    title: "Weekly Market Intelligence Brief - {{domain}} - Week {{week_number}}"
    date_range: "{{start_date}} to {{end_date}}"
    analyst: "{{analyst_name}}"
    confidence_score: "{{overall_confidence}}/10"
    
  executive_summary:
    key_insights: "{{top_3_insights}}"
    impact_assessment: "{{business_impact_summary}}"
    urgency_flags: "{{immediate_action_items}}"
    
  competitive_landscape:
    new_entrants: "{{new_competitors_this_week}}"
    pricing_moves: "{{pricing_changes_table}}"
    product_launches: "{{new_products_with_impact}}"
    market_share_shifts: "{{share_change_visualization}}"
    
  market_trends:
    demand_patterns: "{{volume_trend_charts}}"
    seasonal_factors: "{{seasonality_analysis}}"
    emerging_segments: "{{new_categories_or_niches}}"
    consumer_behavior: "{{behavior_shift_indicators}}"
    
  regulatory_updates:
    policy_changes: "{{new_regulations_this_week}}"
    compliance_deadlines: "{{upcoming_compliance_dates}}"
    industry_standards: "{{standards_updates}}"
    
  consumer_insights:
    sentiment_analysis: "{{sentiment_score_changes}}"
    review_patterns: "{{review_trend_analysis}}"
    social_mentions: "{{social_media_intelligence}}"
    pain_points: "{{emerging_customer_issues}}"
    
  strategic_recommendations:
    immediate_actions: "{{this_week_action_items}}"
    short_term_opportunities: "{{2_4_week_opportunities}}"
    risk_mitigation: "{{identified_threats_and_responses}}"
    monitoring_priorities: "{{what_to_watch_next_week}}"
    
  appendix:
    data_sources: "{{source_list_with_confidence}}"
    methodology: "{{STORM_CRAG_CRITIC_summary}}"
    confidence_intervals: "{{uncertainty_ranges}}"
```

## Multi-Format Output Specifications

### HTML Report Template
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{brief_title}}</title>
    <style>
        .confidence-high { color: #2E7D32; }
        .confidence-medium { color: #F57F17; }
        .confidence-low { color: #C62828; }
        .urgent { border-left: 4px solid #FF5722; }
    </style>
</head>
<body>
    <header class="brief-header">
        <h1>{{title}}</h1>
        <div class="metadata">
            <span>{{date_range}}</span>
            <span>Confidence: {{confidence}}/10</span>
        </div>
    </header>
    
    <section class="executive-summary urgent">
        <h2>Executive Summary</h2>
        {{#each key_insights}}
        <div class="insight confidence-{{this.confidence_level}}">
            {{this.text}}
        </div>
        {{/each}}
    </section>
    
    <!-- Additional sections follow template structure -->
</body>
</html>
```

### PPTX Template Structure
```yaml
slide_structure:
  slide_1_cover:
    title: "Weekly Intelligence Brief"
    subtitle: "{{domain}} - {{date_range}}"
    confidence_indicator: "Overall Confidence: {{confidence}}/10"
    
  slide_2_summary:
    title: "Executive Summary - Top 3 Insights"
    bullets: "{{key_insights_formatted}}"
    urgency_callouts: "{{urgent_items_highlighted}}"
    
  slide_3_competitive:
    title: "Competitive Moves This Week"
    table: "{{competitor_activity_table}}"
    chart: "{{market_share_changes}}"
    
  slide_4_trends:
    title: "Market Trends & Consumer Behavior" 
    charts: ["{{demand_chart}}", "{{sentiment_chart}}"]
    insights: "{{trend_bullets}}"
    
  slide_5_actions:
    title: "Recommended Actions"
    immediate: "{{this_week_actions}}"
    short_term: "{{2_4_week_opportunities}}"
    watch_list: "{{monitoring_priorities}}"
```

### JSON Data Export
```json
{
  "brief_metadata": {
    "id": "{{brief_id}}",
    "domain": "{{domain}}",
    "week": "{{week_number}}",
    "date_range": {"start": "{{start_date}}", "end": "{{end_date}}"},
    "confidence_score": {{overall_confidence}},
    "analyst": "{{analyst_name}}"
  },
  "insights": [
    {
      "category": "competitive|trend|regulatory|consumer",
      "text": "{{insight_text}}",
      "confidence": {{0.0_to_1.0}},
      "impact": {{0.0_to_1.0}}, 
      "urgency": {{0.0_to_1.0}},
      "sources": ["{{source_1}}", "{{source_2}}"],
      "evidence": [
        {"type": "data_point", "value": "{{metric}}", "source": "{{source}}"},
        {"type": "quote", "text": "{{quote}}", "source": "{{source}}"}
      ]
    }
  ],
  "recommendations": [
    {
      "timeframe": "immediate|short_term|long_term",
      "action": "{{action_description}}",
      "rationale": "{{why_recommended}}",
      "success_metrics": ["{{metric_1}}", "{{metric_2}}"],
      "resources_needed": ["{{resource_1}}", "{{resource_2}}"]
    }
  ],
  "data_quality": {
    "sources_used": {{source_count}},
    "crag_pass_rate": {{percentage}},
    "critic_iterations": {{iteration_count}},
    "confidence_distribution": {
      "high": {{percentage}},
      "medium": {{percentage}}, 
      "low": {{percentage}}
    }
  }
}
```

## Configuration Schema

### Weekly Brief Config
```yaml
brief_config:
  schedule: weekly
  delivery_day: friday
  lookback_period: 7_days
  format_priority: [html, pptx, json]
  
  content_requirements:
    max_insights: 5
    max_recommendations: 8
    executive_summary_words: 150
    confidence_threshold: 0.6
    
  distribution:
    internal_stakeholders: ["{{email_list}}"]
    external_clients: ["{{client_email_list}}"]
    archive_location: "{{s3_bucket_or_folder}}"}
    
quality_gates:
  min_sources_per_insight: 2
  min_confidence_for_urgent: 0.8
  max_uncertainty_range: 0.3
  required_perspectives: 4  # out of 5 STORM perspectives
```

## Budget Controls
```yaml
weekly_budget:
  serper_queries: 50        # web search budget per week
  firecrawl_pages: 25       # content crawling budget
  social_api_calls: 200     # social platform API usage
  llm_tokens: 100000        # total LLM token budget
  
cost_optimization:
  cache_duration: 24_hours  # cache results within week
  batch_processing: true    # batch similar queries
  fallback_free_sources: [pytrends, reddit_free, youtube_free]
```

## Quality Metrics
```yaml
success_metrics:
  insight_accuracy: target_85_percent
  recommendation_adoption: target_60_percent  
  stakeholder_satisfaction: target_4_of_5
  time_to_delivery: target_24_hours
  
monitoring:
  crag_quality_trends: track_weekly
  critic_correction_rate: track_weekly
  source_reliability: track_monthly
  confidence_calibration: track_monthly
```