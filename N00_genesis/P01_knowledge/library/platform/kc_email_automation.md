---
id: kc_email_automation
kind: knowledge_card
8f: F3_inject
pillar: P01
quality: 9.1
tldr: "Design patterns for transactional and marketing email automation — template dictionaries, BRL formatting, sequential launch sequences, and provider abstraction."
tags: ["email", "automation", "transactional", "marketing", "templates", "BRL"]
when_to_use: "Apply when design patterns for transactional and marketing email automation — template dictionaries, brl for..."
keywords: [knowledge-card, dictionary, separation, email, transactional]
linked_artifacts:
  primary: null
  related: []
density_score: 0.99
related:
  - p12_wf_cf_email_launch
  - p01_kc_pydantic_patterns
  - SPEC_05_skills_runtime
  - n02_kc_email_sequence
  - email_sequence_template
  - bld_examples_repo_map
  - kc_course_generation
  - bld_knowledge_card_notifier
  - n02_leverage_map_v2_iteration2
  - p04_ex_content_monetization_infoproduct
---

# Email Automation Patterns

Patterns for implementing email systems that handle both transactional (purchase confirmations, alerts) and marketing (launch sequences, nurturing) flows in a content monetization context.

## 1. Template Dictionary Pattern

Store all email templates in a centralized dictionary keyed by `email_type`. Each entry contains subject, body template, and metadata — never hardcode email content inline.

```python
TEMPLATES = {
    "purchase_confirmation": {
        "subject": "Compra confirmada — {pack_name}",
        "body": "Olá {name}, seus {credits} créditos já estão disponíveis...",
        "category": "transactional",
        "priority": "high"
    },
    "credit_low_alert": {
        "subject": "Seus créditos estão acabando",
        "body": "Você tem apenas {balance} créditos restantes...",
        "category": "transactional",
        "priority": "medium"
    },
    "course_launch": {
        "subject": "Novo curso: {course_title}",
        "body": "Descubra como {course_benefit}...",
        "category": "marketing",
        "priority": "normal"
    }
}
```

**Benefit**: Single source of truth for all email content. Easy to audit, localize, and A/B test.

## 2. Transactional vs Marketing Separation

These two categories have fundamentally different requirements and must be treated differently at every layer.

| Dimension | Transactional | Marketing |
|-----------|--------------|-----------|
| Trigger | User action (purchase, alert) | Scheduled / campaign |
| Opt-out | Cannot unsubscribe | Must have unsubscribe link |
| Delivery SLA | < 30 seconds | Best effort |
| Provider | Dedicated IP / high-priority queue | Shared pool |
| Legal (LGPD) | Legitimate interest | Requires explicit consent |
| Rate limit | Per-event (1:1) | Batch (bulk send) |

**Rule**: Never send marketing emails through the transactional pipeline. Providers like SendGrid and Amazon SES enforce separate sending domains for each category.

## 3. BRL Currency Formatting

All monetary values in emails must be formatted from integer centavos to human-readable BRL strings. This is a common source of display bugs.

```python
def format_brl(centavos: int) -> str:
    """Convert integer centavos to BRL display string."""
    reais = centavos / 100
    return f"R${reais:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
```

- `1050` → `R$10,50`
- `260000` → `R$2.600,00`

**Rule**: Never format currency in the email template itself — always pre-format in the rendering function and pass as a ready string. This prevents locale-dependent bugs.

## 4. Sequential Launch Sequence

For product launches (courses, new features), implement a timed email sequence that builds anticipation:

| Day | Email | Goal |
|-----|-------|------|
| D-7 | Teaser | Awareness — "algo novo está chegando" |
| D-3 | Preview | Interest — preview content, testimonials |
| D-1 | Reminder | Urgency — "amanhã abre" |
| D+0 | Launch | Action — CTA to purchase |
| D+1 | Social proof | Trust — early buyer testimonials |
| D+3 | Last chance | Scarcity — "encerra em 24h" |

Each email references the previous one ("como falamos ontem...") to create narrative continuity.

**Implementation**: Store sequence definitions as a list of `(offset_days, email_type, condition)` tuples. A scheduler cron checks daily which users should receive which step.

## 5. Provider Abstraction Layer

Abstract the email sending behind an interface so the provider can be swapped without touching business logic.

```python
class EmailSender(Protocol):
    def send(self, to: str, subject: str, body_html: str, category: str) -> str: ...
    def send_batch(self, recipients: list[str], subject: str, body_html: str) -> list[str]: ...
```

Implementations: `SendGridSender`, `SESSender`, `SMTPSender`, `MockSender`.

**MockSender** is mandatory for tests — records all sent emails in memory for assertion:
```python
mock_sender.send("user@test.com", "Compra", "<p>OK</p>", "transactional")
assert len(mock_sender.sent) == 1
assert mock_sender.sent[0]["to"] == "user@test.com"
```

## 6. Personalization Pipeline

Before sending, every email passes through a personalization pipeline:

1. **Template selection** — lookup `TEMPLATES[email_type]`
2. **Variable injection** — `template.format(**user_context)`
3. **Currency formatting** — all `{amount}` fields pre-formatted via `format_brl()`
4. **Link tracking** — append UTM params for marketing emails
5. **Unsubscribe injection** — add footer link for marketing category only
6. **HTML rendering** — wrap in responsive email template (MJML or inline CSS)

## Regras de Ouro

1. **Never inline email content** — always use the template dictionary.
2. **Transactional ≠ marketing** — separate pipelines, separate providers, separate consent.
3. **BRL from centavos** — format once in the renderer, never in templates.
4. **MockSender in CI** — zero real emails sent during test runs.
5. **Sequential sequences** — each email references the previous for narrative continuity.
6. **LGPD compliance** — marketing requires explicit opt-in; transactional uses legitimate interest basis.


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_cf_email_launch]] | downstream | 0.34 |
| [[p01_kc_pydantic_patterns]] | sibling | 0.24 |
| [[SPEC_05_skills_runtime]] | related | 0.24 |
| [[n02_kc_email_sequence]] | sibling | 0.23 |
| [[email_sequence_template]] | downstream | 0.21 |
| [[bld_examples_repo_map]] | downstream | 0.19 |
| [[kc_course_generation]] | sibling | 0.19 |
| [[bld_knowledge_card_notifier]] | sibling | 0.18 |
| [[n02_leverage_map_v2_iteration2]] | downstream | 0.18 |
| [[p04_ex_content_monetization_infoproduct]] | downstream | 0.18 |
