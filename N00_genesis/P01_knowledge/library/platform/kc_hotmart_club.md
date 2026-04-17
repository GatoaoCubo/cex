---
id: kc_hotmart_club
kind: knowledge_card
pillar: P01
version: 1.0.0
created: 2026-03-31
author: n03_builder
domain: course_delivery
quality: 9.1
tldr: "Hotmart Club — native member area for course delivery, drip content, progress tracking, and community features."
tags: [hotmart, club, course, member-area, drip, infoproduct, brazil]
density_score: 1.0
when_to_use: "Apply when hotmart club — native member area for course delivery, drip content, progress tracking, and commu..."
keywords: [knowledge-card, course, platform, delivery, structure]
linked_artifacts:
  primary: null
  related: []
---

# Hotmart Club — Course Delivery Platform

Hotmart Club is Hotmart's native member area for delivering digital courses, communities, and drip content. It is tightly integrated with Hotmart's checkout and payment system, requiring zero additional integration for content delivery after purchase.

## 1. Architecture Overview

```
Hotmart Checkout (purchase)
    │
    ▼
Hotmart Club (auto-provisioned access)
    ├── Modules (ordered sections)
    │   ├── Lessons (video, text, PDF, quiz)
    │   └── Drip schedule (time-gated release)
    ├── Community (comments, Q&A per lesson)
    ├── Progress tracking (completion %, certificates)
    └── Member dashboard (all enrolled courses)
```

**Key benefit**: Purchase on Hotmart automatically grants Club access. No webhook-to-LMS integration needed for basic course delivery.

## 2. Content Structure

### Modules
Top-level organizational units. Each module contains lessons and an optional drip schedule.

| Field | Type | Description |
|-------|------|-------------|
| title | string | Module name (e.g., "Modulo 1: Fundamentos") |
| position | integer | Display order (1-based) |
| drip_days | integer | Days after purchase before module unlocks (0 = immediate) |
| is_published | boolean | Visible to students |

### Lessons
Individual content pieces within a module.

| Field | Type | Description |
|-------|------|-------------|
| title | string | Lesson name |
| type | enum | video, text, pdf, quiz, audio |
| duration_minutes | integer | Estimated time (displayed to student) |
| position | integer | Order within module |
| is_free_preview | boolean | Accessible without purchase (lead magnet) |

### Content Types
| Type | Format | Hosting | Max Size |
|------|--------|---------|----------|
| Video | MP4, MOV | Hotmart CDN (auto-transcoded) | 4 GB per file |
| Text | HTML editor (WYSIWYG) | Inline | No limit |
| PDF | .pdf attachment | Hotmart CDN | 100 MB |
| Quiz | Multiple choice (native) | Inline | 50 questions |
| Audio | MP3, WAV | Hotmart CDN | 500 MB |

## 3. Drip Content Strategy

Drip content releases modules on a schedule relative to the student's purchase date.

```yaml
drip_schedule:
  - module: "Fundamentos"
    drip_days: 0        # Immediate access
  - module: "Intermediario"
    drip_days: 7        # 1 week after purchase
  - module: "Avancado"
    drip_days: 14       # 2 weeks after purchase
  - module: "Certificacao"
    drip_days: 21       # 3 weeks, after completing exercises
```

**Why drip**: Prevents overwhelm, increases engagement, reduces refund rates (students who start are less likely to refund within the 7-day guarantee period).

**Gotcha**: Drip is per-student based on their purchase date, not a global calendar. A student buying on day 30 gets module 2 on day 37.

## 4. Club API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/club/api/v1/modules` | GET | List all modules |
| `/club/api/v1/modules/{id}` | GET | Module details |
| `/club/api/v1/modules/{id}/pages` | GET | Lessons in module |
| `/club/api/v1/pages/{id}` | GET | Single lesson details |
| `/club/api/v1/users` | GET | Enrolled students list |
| `/club/api/v1/users/{id}/progress` | GET | Student progress |

**Auth**: Same OAuth2 Bearer token as the main Hotmart API. The Club API is a separate base path but shares authentication.

**Rate limits**: Same 60 req/min as main API.

## 5. Progress Tracking & Certificates

### Completion Model
- Each lesson has a `completed` boolean per student.
- Module completion = all lessons completed.
- Course completion = all modules completed.
- Completion percentage displayed on student dashboard.

### Certificates
| Setting | Options |
|---------|---------|
| Enabled | true/false per product |
| Threshold | % completion required (default 80%) |
| Template | Hotmart default or custom upload (PDF template) |
| Fields | Student name, course name, date, instructor name |
| Download | PDF auto-generated, shareable link |

**Gotcha**: Certificates only count published lessons. If you add new lessons after launch, existing "completed" students may drop below threshold.

## 6. Community Features

- Per-lesson comment threads (Q&A style).
- Instructor can pin, reply, or delete comments.
- No real-time chat — asynchronous only.
- Student can mention other students (@name).
- Email notifications for replies (configurable by student).

**Limitation**: No dedicated community space (like Discord/Circle). For active communities, pair Club with an external community platform and link from lessons.

## 7. Integration Patterns

### Pattern A: Club-Only (Simplest)
```
Hotmart Checkout → Club auto-access → Student watches content
```
Best for: Simple courses, low-touch delivery, solo creators.

### Pattern B: Club + External Tools
```
Hotmart Checkout → Webhook → Your backend
    │                              │
    ▼                              ▼
Club (content delivery)    CRM + Email sequences
```
Best for: Courses with email nurture, upsell sequences, or credit-based features.

### Pattern C: Club as Lead Magnet + Premium
```
Free module (is_free_preview=true) → Capture email
    │
    ▼
Nurture sequence → Upsell to full course
    │
    ▼
Purchase → Full Club access (dripped)
```
Best for: Funnels using free content to drive paid conversions.

## 8. Hotmart Club vs External LMS

| Aspect | Hotmart Club | External LMS (Teachable, etc.) |
|--------|-------------|-------------------------------|
| Setup cost | Free (included with Hotmart) | $39-$119/month |
| Integration | Zero (auto-provisioned) | Webhook → API provisioning |
| Customization | Limited (template themes) | High (custom domains, CSS) |
| Community | Basic comments | Varies (some have forums) |
| Certificates | Native | Native or via Zapier |
| Drip content | Native | Native |
| Analytics | Basic (completion %) | Detailed (engagement, retention) |
| Multi-language | PT-BR focused | Multi-language native |

**Decision rule**: Use Club for BR-market courses where simplicity matters. Use external LMS when you need custom branding, advanced analytics, or international multi-language support.

## 9. Common Gotchas

| Gotcha | Impact | Fix |
|--------|--------|-----|
| Club URL not custom domain | Less professional appearance | Use Hotmart's custom domain feature (paid) |
| Video transcoding delay | New uploads unavailable for hours | Upload 24h before publishing |
| No bulk lesson import | Manual upload per lesson | Use API for programmatic creation |
| Free preview = indexed by Google | SEO benefit but content exposed | Only preview non-core introductions |
| Student list API paginated | Slow for large audiences | Cache student data, poll periodically |

## Regras de Ouro

1. **Drip for engagement** — never dump all content at once; 7-day intervals reduce refunds.
2. **Free preview for funnel** — use first module as lead magnet to capture emails.
3. **Club for BR, external for INT** — Club is optimized for Portuguese; use DS24 member area or Teachable for international.
4. **Certificate at 80%** — encourages completion without being punitive.
5. **API for automation** — use Club API to sync progress with your CRM/email provider.


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating
