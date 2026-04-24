---
id: p12_wf_cf_email_launch
kind: workflow
8f: F8_collaborate
pillar: P12
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n02_marketing"
title: "Email Launch Sequence for Content"
steps_count: 4
execution: sequential
agent_groups: [n02_marketing, n05_operations]
timeout: 240
retry_policy: per_step
depends_on: []
signals: [complete, error]
spawn_configs: []
domain: "content_factory"
quality: 9.0
tags: [workflow, content_factory, email, launch, automation]
tldr: "Generate 5-email launch sequence, configure automation triggers, schedule and activate — 4 sequential steps"
density_score: 0.90
related:
  - p12_wf_builder_8f_pipeline
  - p12_wf_cf_promote
  - p12_wf_content_factory_v1
  - p12_wf_cf_publish_hotmart
  - kc_email_automation
  - p12_wf_engineering_pipeline
  - p12_wf_brand_pipeline
  - p12_wf_cf_publish_social
  - email_sequence_template
  - bld_architecture_chain
---

## Purpose
Creates and activates a 5-email launch sequence for any content factory product (course,
ebook, webinar). Generates the email copy (subject lines, body, CTAs), configures automation
triggers (signup, open, click), schedules the sequence over 5 days, and activates. Designed
for product launches, lead magnet delivery, and nurture sequences.

## Steps

### Step 1: Generate Email Sequence [n02_marketing]
- **Agent**: n02_marketing
- **Action**: Write 5-email sequence with subject lines, body copy, and CTAs following launch arc
- **Input**: content description + brand_config + launch_date
- **Output**: 5 email objects (subject, preview_text, body_html, cta_text, cta_url, send_day)
- **Signal**: generate_emails_complete
- **Depends on**: none
- **Timeout**: 90s
- **On failure**: abort (no emails = no sequence)

Email arc:
- Day 0: Announcement + early access
- Day 1: Value preview + social proof
- Day 2: Deep dive on one benefit
- Day 3: Objection handling + FAQ
- Day 4: Urgency + final CTA

### Step 2: Configure Automation [n05_operations]
- **Agent**: n05_operations
- **Action**: Set up email automation triggers (list signup, tag application, date-based sends)
- **Input**: email sequence from Step 1 + subscriber list/tag targeting
- **Output**: automation ID + trigger configuration confirmation
- **Signal**: automation_config_complete
- **Depends on**: Step 1
- **Timeout**: 60s
- **On failure**: retry (max 1, email provider API)

### Step 3: Schedule Sequence [n05_operations]
- **Agent**: n05_operations
- **Action**: Schedule all 5 emails at optimal send times (9:00 AM recipient timezone)
- **Input**: automation ID + email objects with send_day offsets
- **Output**: schedule confirmation with exact send timestamps
- **Signal**: schedule_sequence_complete
- **Depends on**: Step 2
- **Timeout**: 30s
- **On failure**: retry (max 1, scheduling conflicts)

### Step 4: Activate and Verify [n05_operations]
- **Agent**: n05_operations
- **Action**: Activate automation, send test email to brand owner, verify deliverability
- **Input**: automation ID + brand_config.email (test recipient)
- **Output**: activation status + test email delivery confirmation
- **Signal**: wf_cf_email_launch_complete
- **Depends on**: Step 3
- **Timeout**: 60s
- **On failure**: abort (activation failure needs manual email provider review)

## Dependencies
- Content product must be ready (course URL, ebook download link, webinar registration)
- Email provider API credentials (Mailchimp, ConvertKit, or ActiveCampaign)
- Subscriber list or tag for targeting
- brand_config.email for test sends

## Signals
- **On step complete**: {step_name}_complete per step
- **On workflow complete**: wf_cf_email_launch_complete with automation ID + first send date
- **On error**: wf_cf_email_launch_error with step ID + email provider error detail

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_builder_8f_pipeline]] | sibling | 0.34 |
| [[p12_wf_cf_promote]] | sibling | 0.31 |
| [[p12_wf_content_factory_v1]] | sibling | 0.29 |
| [[p12_wf_cf_publish_hotmart]] | sibling | 0.28 |
| [[kc_email_automation]] | upstream | 0.28 |
| [[p12_wf_engineering_pipeline]] | sibling | 0.28 |
| [[p12_wf_brand_pipeline]] | sibling | 0.26 |
| [[p12_wf_cf_publish_social]] | sibling | 0.25 |
| [[email_sequence_template]] | upstream | 0.25 |
| [[bld_architecture_chain]] | upstream | 0.25 |
