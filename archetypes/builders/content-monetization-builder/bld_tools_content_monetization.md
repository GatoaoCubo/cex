---
kind: tools
id: bld_tools_content_monetization
pillar: P04
llm_function: CALL
purpose: Tools, APIs, and data sources for content monetization pipeline
---

# Tools: content-monetization-builder

## Payment Providers
| Provider | API | Auth | Cost | Market |
|----------|-----|------|------|--------|
| Stripe | REST + webhooks | STRIPE_SECRET_KEY | 2.9% + $0.30/tx | Global |
| Hotmart | REST v2 | HOTMART_TOKEN | varies by product | BR infoproducts |
| Kiwify | REST | KIWIFY_API_KEY | 8.99% per sale | BR infoproducts |
| Monetizze | REST | MONETIZZE_TOKEN | varies | BR health/finance |
| Eduzz | REST | EDUZZ_API_KEY | varies | BR digital+physical |

## Email Providers
| Provider | API | Auth | Cost | Specialty |
|----------|-----|------|------|-----------|
| Resend | REST | RESEND_API_KEY | Free 3K/mo, $20/50K | Dev-friendly, React Email |
| SendGrid | REST | SENDGRID_API_KEY | Free 100/day, $19.95/50K | Scale, templates |
| AWS SES | REST/SMTP | AWS_ACCESS_KEY_ID | $0.10/1K emails | Cost-effective at scale |
| Mailchimp | REST | MAILCHIMP_API_KEY | Free 500 contacts | No-code, automations |

## Ad Platforms
| Platform | API | Auth | Min Budget | Best For |
|----------|-----|------|-----------|----------|
| Meta Ads | Marketing API | META_ACCESS_TOKEN | R$20/day | B2C awareness, retargeting |
| Google Ads | REST | GOOGLE_ADS_TOKEN | R$10/day | Intent capture, search |
| TikTok Ads | Marketing API | TIKTOK_ACCESS_TOKEN | R$50/day | Gen-Z, viral content |
| LinkedIn Ads | Marketing API | LINKEDIN_TOKEN | $10/day | B2B, professional |

## LLM Cost Reference (for credit pricing)
| Model | Input $/1K tok | Output $/1K tok | Best For |
|-------|---------------|-----------------|----------|
| Claude Sonnet 4 | $0.003 | $0.015 | Content generation |
| GPT-4o-mini | $0.00015 | $0.0006 | Classification, extraction |
| Gemini 2.5 Flash | $0.00015 | $0.0035 | Bulk processing |
| Claude Opus 4 | $0.015 | $0.075 | Complex reasoning |

## Course Platforms
| Platform | Integration | Auth | Features |
|----------|------------|------|----------|
| Hotmart Club | Hotmart API | HOTMART_TOKEN | Native to Hotmart checkout |
| Teachable | REST API | TEACHABLE_API_KEY | Standalone, customizable |
| Thinkific | REST API | THINKIFIC_API_KEY | Standalone, communities |
| Custom LMS | Direct DB | DB connection | Full control, self-hosted |

## CEX Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | .md → .yaml compilation | After save |
| cex_hooks.py | Pre/post validation | Before commit |
| cex_doctor.py | Builder health check | After build |
| cex_score.py | 5D quality scoring | Peer review |
| signal_writer.py | Inter-nucleus signals | After complete |

## Data Sources
| Source | Path | Data |
|--------|------|------|
| Schema | P06/_schema.yaml | Field definitions |
| Kind KC | P01_knowledge/library/kind/ | Domain knowledge |
| Examples | P04_tools/examples/ | Reference configs |
| SEED_BANK | archetypes/SEED_BANK.yaml | Builder seeds |
