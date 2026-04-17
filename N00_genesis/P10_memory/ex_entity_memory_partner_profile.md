---
id: ex_entity_memory_partner_profile
kind: entity_memory
pillar: P10
version: 1.0.0
title: "Entity Memory -- B2B Partner Profile"
description: "Entity memory schema for B2B partner profiles. Captures registration data, tier, activity history, and commercial signals for CRM and AI-assisted sales workflows."
domain: crm
nucleus: N06
quality: 9.0
tags: [entity-memory, crm, b2b, partner, profile, commercial]
brand_placeholders:
  - BRAND_NAME
  - BRAND_CRM_TABLE_PREFIX
  - BRAND_VERTICAL
density_score: 1.0
---

# Entity Memory -- B2B Partner Profile

> One entity per registered B2B partner. Used by AI sales assistant and CRM dashboard.
> Replace `{{BRAND_CRM_TABLE_PREFIX}}` with your table prefix.

---

## 1. Entity Schema

```yaml
entity_type: b2b_partner
version: 1.0.0
storage: supabase.{{BRAND_CRM_TABLE_PREFIX}}_partners

fields:
  # Identity
  id:           uuid       # system-generated
  cnpj:         string     # Brazilian company ID (unique)
  company_name: string     # Legal or trade name
  contact_name: string     # Primary contact full name
  email:        string     # Primary email
  whatsapp:     string     # WhatsApp number (with country code)
  region:       string     # State or city

  # Commercial
  tier:         enum       # starter | pro | enterprise
  status:       enum       # pending | active | suspended | cancelled
  discount_pct: float      # Current negotiated discount (%)
  monthly_volume: integer  # Average monthly units ordered (last 3 months)

  # Engagement
  last_order_at:  datetime
  last_login_at:  datetime
  total_orders:   integer
  lifetime_value: decimal  # Total GMV in {{BRAND_CURRENCY}}

  # Signals
  churn_risk:    enum      # low | medium | high
  growth_signal: enum      # stable | growing | declining
  notes:         text      # Free-form CRM notes
```

---

## 2. Entity Lifecycle

```
REGISTRATION                                            ACTIVE PARTNER
     |                                                       |
  pending  -> (CNPJ validated + manual review) ->  active  <-> suspended -> cancelled
     |
  auto-reject if CNPJ invalid
```

---

## 3. Memory Operations

### 3.1 Create

Triggered by: partner registration form submission.

```python
# Pseudocode
partner = {
    "cnpj": validated_cnpj,
    "company_name": form.company,
    "contact_name": form.contact,
    "email": form.email,
    "whatsapp": form.whatsapp,
    "tier": "starter",
    "status": "pending"
}
supabase.table("{{BRAND_CRM_TABLE_PREFIX}}_partners").insert(partner)
notify_admin(partner)
```

### 3.2 Update (Approval)

```python
supabase.table("{{BRAND_CRM_TABLE_PREFIX}}_partners")
  .update({"status": "active", "approved_at": now()})
  .eq("id", partner_id)
notify_partner("approval_email", partner)
```

### 3.3 Query (AI Sales Assistant)

```python
# Load partner context for AI sales message generation
def load_partner_context(partner_id):
    partner = get_partner(partner_id)
    recent_orders = get_orders(partner_id, limit=5)
    return {
        "name": partner.contact_name,
        "company": partner.company_name,
        "tier": partner.tier,
        "discount": partner.discount_pct,
        "last_order": recent_orders[0] if recent_orders else None,
        "growth_signal": partner.growth_signal
    }
```

---

## 4. CRM Dashboard Signals

| Signal | Logic | Action |
|--------|-------|--------|
| Churn risk HIGH | No orders in (30+ days) AND tier=starter | Flag for outreach |
| Growth signal GROWING | Orders +20% MoM for 2+ months | Upsell to Pro tier |
| Volume threshold | monthly_volume crosses tier minimum | Upgrade prompt |
| CNPJ expiry | CNPJ status check via API | Alert partner |

---

## 5. Integration Points

| Consumer | How it uses this entity |
|----------|------------------------|
| B2B dashboard | Read partner profile + orders |
| AI sales assistant | Context injection for message generation |
| Admin CRM | Full CRUD + approval workflow |
| Email/WhatsApp automation | Event-triggered notifications |
| {{BRAND_ERP}} | Partner ID linkage for wholesale orders |

---

## 6. Privacy + Compliance

- CNPJ is PII -- encrypted at rest in Supabase
- Emails not shared with third parties without consent
- LGPD consent captured at registration form
- Partner can request data deletion via {{BRAND_PARTNER_EMAIL}}
