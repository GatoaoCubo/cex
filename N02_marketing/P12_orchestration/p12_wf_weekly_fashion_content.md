---
id: p12_wf_weekly_fashion_content
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "workflow-builder"
title: "Weekly Fashion Content Publisher"
steps_count: 6
execution: mixed
agent_groups: [fashion_trends, content_creator, visual_designer]
timeout: 7200
retry_policy: per_step
depends_on: []
signals: [content_ready, published, error]
spawn_configs: [p12_spawn_trends_analyst, p12_spawn_content_writer, p12_spawn_visual_creator]
domain: "copywriting"
quality: 9.1
tags: [workflow, fashion, content, weekly, automation]
tldr: "6-step weekly fashion content workflow: trend analysis, educational content creation, visual design, and multi-channel publishing"
density_score: 0.92

---

## Purpose
Automates weekly fashion content production combining trend analysis with educational content for e-commerce conversion. Produces blog posts, social content, and email campaigns that balance trend awareness with practical styling education.

## Steps

### Step 1: Trend Research [fashion_trends]
| Field | Value |
|-------|-------|
| **Agent** | fashion_trends (claude-3-sonnet) |
| **Action** | Analyze fashion platforms, social signals, and trend data |
| **Input** | Weekly trend monitoring brief |
| **Output** | Trend analysis report with 5 top trends |
| **Signal** | trends_analyzed |
| **Depends on** | none |

### Step 2: Inventory Check [content_creator]
| Field | Value |
|-------|-------|
| **Agent** | content_creator (gpt-4) |
| **Action** | Match trends to available inventory, identify featured products |
| **Input** | Trend report from Step 1, current inventory data |
| **Output** | Product-trend mapping with stock levels |
| **Signal** | inventory_mapped |
| **Depends on** | Step 1 |

### Step 3: Educational Content [content_creator]
| Field | Value |
|-------|-------|
| **Agent** | content_creator (gpt-4) |
| **Action** | Create styling guides, sizing tips, care instructions |
| **Input** | Product categories and customer FAQ data |
| **Output** | 3 educational blog posts with CTAs |
| **Signal** | educational_ready |
| **Depends on** | none |

### Step 4: Trend Content [content_creator]
| Field | Value |
|-------|-------|
| **Agent** | content_creator (gpt-4) |
| **Action** | Write trend-focused posts and social captions |
| **Input** | Inventory mapping from Step 2 |
| **Output** | 5 trend posts with product links |
| **Signal** | trend_content_ready |
| **Depends on** | Step 2 |

### Step 5: Visual Assets [visual_designer]
| Field | Value |
|-------|-------|
| **Agent** | visual_designer (claude-3-haiku) |
| **Action** | Generate social graphics, outfit layouts, size guides |
| **Input** | All content from Steps 3-4 |
| **Output** | 20 visual assets for multi-channel use |
| **Signal** | visuals_complete |
| **Depends on** | Steps 3, 4 |

### Step 6: Publishing [content_creator]
| Field | Value |
|-------|-------|
| **Agent** | content_creator (gpt-4) |
| **Action** | Schedule and publish across blog, Instagram, email |
| **Input** | Content and visuals from Steps 3-5 |
| **Output** | Published content with analytics tracking |
| **Signal** | content_published |
| **Depends on** | Step 5 |

## Usage Guidelines

**When to use:**
- E-commerce fashion brands with 50+ SKUs and weekly inventory turnover
- Content teams producing 15+ pieces per week across multiple channels
- Brands targeting trend-conscious customers who need styling education

**When NOT to use:**
- Luxury brands focusing on timeless pieces over trends
- Seasonal businesses with quarterly content cycles
- Teams without real-time inventory data integration

**Anti-patterns:**
- Running without inventory API connection (produces broken product links)
- Skipping educational content for pure trend-chasing (reduces conversion)
- Publishing without visual assets (severely impacts engagement rates)

## Dependencies
- Active fashion trend monitoring tools and data sources
- E-commerce inventory API with real-time stock levels
- Publishing platform credentials for blog, social, email

## Signals
- **On step complete**: Agent-specific completion signals with quality scores
- **On workflow complete**: content_published with engagement baseline
- **On error**: Per-step retry (max 2), fallback to evergreen content library