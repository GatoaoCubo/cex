---
id: tpl_research_batch_social
kind: template
pillar: P12
title: "Research Batch — Social Media Discovery"
version: 1.0.0
quality: 9.0
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo/crm_mission/batch_c_social_discovery.md
variables: [INDUSTRY, PLATFORMS, HASHTAGS, REGION, CITIES, OUTPUT_FILE, SIGNAL_TAG]
density_score: 0.95
tags: [template, research-batch, social-media, instagram, facebook, crm, instance-extraction]
tldr: "Social media business discovery — find informal and micro businesses via hashtag mining and profile scraping."
updated: "2026-04-13"
---

# BATCH C — Social Media Discovery

**Output**: `N01_research/P05_output/data/{{OUTPUT_FILE | default: 'crm_batch_c_social.json'}}`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 {{SIGNAL_TAG | default: 'BATCH_C_SOCIAL'}}`

---

## Prerequisites

1. `P05_output/p05_rf_crm_output_standard.md` — JSON output format
2. `P06_schema/p06_val_business_contact_quality.md` — anti-fake validation
3. Existing CRM data file (for dedup)

---

## Objective

Discover **informal and micro businesses** that don't appear in formal directories: home-based services, independent professionals, micro-entrepreneurs. Social media is where these businesses live.

---

## Platform 1: Instagram Hashtag Mining

### Hashtag Matrix by City

{{#CITIES}}
#### {{name}}

```
{{#hashtags}}
site:instagram.com {{tag}}
{{/hashtags}}
```
{{/CITIES}}

#### Region-wide

```
{{#HASHTAGS.regional}}
site:instagram.com {{tag}}
{{/HASHTAGS.regional}}
```

### Per Profile Found

```
IF public profile:
  - Display name (business name)
  - Bio → extract phone/WhatsApp/address/link
  - City from bio or posts
  - Category (if business profile)
  - Follower count (influence signal)
  - Post frequency (activity signal)
```

---

## Platform 2: Facebook Pages / Groups

### Search Strategy

```
{{#CITIES}}
SERPER: site:facebook.com "{{INDUSTRY}}" "{{city_name}}"
SERPER: site:facebook.com/pages "{{INDUSTRY}}" "{{city_name}}"
{{/CITIES}}
```

### Groups (discovery only — don't scrape members)

```
SERPER: site:facebook.com/groups "{{INDUSTRY}}" "{{REGION}}"
```

Look for businesses that **post in groups** (self-promotion = active business).

---

## Platform 3: LinkedIn (B2B variant)

```
{{#CITIES}}
SERPER: site:linkedin.com/company "{{INDUSTRY}}" "{{city_name}}"
{{/CITIES}}
```

---

## Data Schema

```json
{
  "nome_fantasia": "string (display name)",
  "cidade": "string (from bio/posts)",
  "uf": "string",
  "telefone": "string (from bio)",
  "whatsapp": "string (from bio link)",
  "instagram": "string (@handle)",
  "facebook": "string (page URL)",
  "website": "string (from bio link)",
  "segmento": "string",
  "sub_segmento": "string",
  "porte": "MEI | micro | pequeno",
  "fonte": "instagram | facebook | linkedin",
  "notas": "string (activity notes)"
}
```

---

## Quality Rules

1. **Business profiles only** — skip personal accounts
2. **Active in last 90 days** — check last post date
3. **Location confirmed** — city must be verifiable from bio/posts
4. **No DM scraping** — public data only
