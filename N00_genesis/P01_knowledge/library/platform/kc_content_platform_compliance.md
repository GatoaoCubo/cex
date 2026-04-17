---
id: kc_content_platform_compliance
kind: knowledge_card
pillar: P01
version: 1.0.0
created: 2026-03-31
author: n03_builder
domain: legal_compliance
quality: 9.1
tldr: "EU and BR compliance for digital content sales — GDPR, Widerrufsrecht, Impressum, EU VAT, CDC consumer rights, and platform-specific requirements."
tags: [compliance, gdpr, eu-vat, widerrufsrecht, impressum, brazil, cdc, hotmart, digistore24]
density_score: 1.0
when_to_use: "Apply when eu and br compliance for digital content sales — gdpr, widerrufsrecht, impressum, eu vat, cdc con..."
keywords: [knowledge-card, compliance, platform, region, general]
linked_artifacts:
  primary: null
  related: []
---

# Content Platform Compliance — EU & BR

Selling digital content internationally requires compliance with multiple legal frameworks. This KC covers the critical requirements for selling via Hotmart (BR) and Digistore24 (EU), the two primary platforms in a multi-market content monetization strategy.

## 1. Compliance Matrix by Region

| Requirement | EU/DACH (DS24) | Brazil (Hotmart) | Global |
|-------------|---------------|-----------------|--------|
| Data protection | GDPR | LGPD | Varies by country |
| Consumer rights | Widerrufsrecht (14-day) | CDC (7-day regret) | Varies |
| Tax | EU VAT (auto via DS24 MoR) | ICMS/ISS + NF | Seller responsibility |
| Legal identity | Impressum (DACH) | CNPJ/CPF | Business registration |
| Email consent | Double opt-in (GDPR) | Opt-in (LGPD) | CAN-SPAM (US) |
| Cookie consent | Explicit opt-in before tracking | LGPD consent | Varies |
| Payment security | PSD2/SCA | PCI-DSS | PCI-DSS |

## 2. GDPR (EU General Data Protection Regulation)

### Core Principles
| Principle | Requirement | Implementation |
|-----------|------------|----------------|
| Lawfulness | Legal basis for processing | Consent or contract performance |
| Purpose limitation | Only collect for stated purpose | Define in privacy policy |
| Data minimization | Only collect what's needed | Minimum fields at checkout |
| Accuracy | Keep data correct and up-to-date | Allow profile edits |
| Storage limitation | Don't keep data forever | Define retention periods |
| Integrity | Protect against unauthorized access | Encryption, access controls |
| Accountability | Demonstrate compliance | Document processes |

### Practical Requirements for Content Sellers

**Double Opt-in for Email Collection**
```
Step 1: User enters email on landing page
Step 2: Confirmation email sent automatically
Step 3: User clicks confirmation link
Step 4: ONLY THEN added to email list
```
**Rule**: Single opt-in is NOT compliant in the EU. Every email capture must use double opt-in. Most email providers (Resend, SendGrid, Mailchimp) support this natively.

**Privacy Policy** (mandatory)
Must include:
- What data you collect and why
- Legal basis (consent, contract)
- How long you retain data
- Third parties who receive data (DS24, email provider, analytics)
- Right to access, rectify, erase, port data
- Contact details for data controller
- Right to lodge complaint with supervisory authority

**Data Processing Agreement (DPA)**
- Required with every processor (DS24, email provider, analytics tool).
- DS24 provides a standard DPA — sign it during vendor onboarding.
- Your email provider must also have a DPA signed.

**Right to Erasure (Right to be Forgotten)**
- Must have a process to delete all user data on request.
- Timeline: respond within 30 days.
- Covers: email lists, purchase history, course progress, analytics data.
- **Gotcha**: DS24 retains transaction data for tax/legal obligations. Your erasure covers YOUR systems only.

### Cookie Consent
```
Before ANY tracking fires:
    ├── Show cookie banner with opt-in checkboxes
    │   ├── Essential (always on, no consent needed)
    │   ├── Analytics (requires opt-in)
    │   ├── Marketing (requires opt-in)
    │   └── Preferences (requires opt-in)
    ├── User accepts → load tracking pixels
    └── User rejects → NO tracking pixels loaded
```

**Tools**: Cookiebot, OneTrust, Osano, or custom implementation.
**Rule**: Pre-checked boxes are NOT valid consent. User must actively opt-in.

## 3. Widerrufsrecht (EU Right of Withdrawal)

The 14-day cooling-off period is mandatory for EU consumer contracts, including digital products.

### For Digital Products (Special Rules)
| Scenario | Widerrufsrecht Applies? |
|----------|------------------------|
| Physical product | Yes — 14 days from delivery |
| Digital product (not yet accessed) | Yes — 14 days from purchase |
| Digital product (accessed immediately) | Can be waived with explicit consent |
| Subscription (not yet used) | Yes — 14 days from first payment |
| Live event / webinar (past date) | No — service already performed |

### Waiver for Immediate Digital Access
You CAN waive Widerrufsrecht if the buyer explicitly consents:

```
Checkbox at checkout (must be unchecked by default):
[ ] "I agree that [product] will be made available immediately,
     and I acknowledge that I lose my right of withdrawal
     once the download/access begins."
```

**DS24 handles this**: DS24 includes this waiver in their checkout flow for digital products. As MoR, DS24 manages the legal text. Vendor must ensure their product is correctly categorized as "digital."

**Hotmart**: Brazilian CDC gives 7-day regret right for digital products. Cannot be waived. Budget for ~5% refund rate.

## 4. Impressum (Legal Notice)

**Mandatory in**: Germany, Austria, Switzerland (DACH region). Also recommended for EU in general.

### Required Content
| Field | Example |
|-------|---------|
| Full legal name | Max Mustermann / Firma GmbH |
| Address | Musterstr. 1, 12345 Berlin, Germany |
| Contact | Email + phone (or contact form) |
| Tax ID | USt-IdNr: DE123456789 |
| Trade register | HRB 12345, Amtsgericht Berlin |
| Responsible for content | Name of responsible person |

**Where to publish**: Dedicated /impressum page, linked from every page footer. Must be reachable within 2 clicks from any page.

**Non-DACH vendors**: If you sell into DACH via DS24 but are not based in EU, you should still have an Impressum with your business details. DS24's checkout has DS24's Impressum (as MoR), but your sales page needs yours.

## 5. EU VAT for Digital Products

### DS24 as Merchant of Record
DS24 handles EU VAT completely:
- Collects correct VAT rate per buyer's country.
- Issues VAT-compliant invoice to buyer.
- Remits VAT to relevant tax authorities.
- Vendor receives payout net of VAT.

| Country | Standard VAT Rate |
|---------|------------------|
| Germany | 19% |
| France | 20% |
| Italy | 22% |
| Spain | 21% |
| Netherlands | 21% |
| Poland | 23% |
| Austria | 20% |
| Switzerland | 8.1% (non-EU, separate rules) |

**Vendor action required**: NONE for EU VAT when using DS24. This is the primary reason to use DS24 for EU sales.

### Without MoR (Hotmart, Stripe)
If selling into EU without a MoR:
1. Register for VAT OSS (One-Stop Shop) in one EU country.
2. Collect VAT at buyer's country rate.
3. File quarterly VAT OSS returns.
4. Alternative: register for VAT in each country where you sell.

**Rule**: For EU sales, always use a MoR (DS24) unless you have established EU tax infrastructure.

## 6. Brazil — CDC Consumer Rights

### 7-Day Regret Right (Direito de Arrependimento)
Art. 49 of CDC (Codigo de Defesa do Consumidor):
- Consumer can return ANY product bought online within 7 days.
- No reason required.
- Full refund including shipping.
- **Cannot be waived** (unlike EU Widerrufsrecht for digital products).
- Applies to digital products sold via Hotmart.

### LGPD (Lei Geral de Protecao de Dados)
Brazil's data protection law, similar to GDPR:
- Consent required for data processing.
- Right to access, correction, deletion.
- Data Protection Officer (DPO) recommended for companies.
- Penalties up to 2% of revenue (max R$50M per violation).

### Nota Fiscal
For B2C digital sales in Brazil:
| Scenario | NF Required? |
|----------|-------------|
| Hotmart handles | Hotmart issues NF for their fee; you issue for your revenue |
| Direct sales | Yes, always (NFSe for services) |
| < MEI limit | Simplified (MEI NF) |

## 7. Email Compliance by Region

| Regulation | Region | Key Requirement |
|------------|--------|----------------|
| GDPR | EU | Double opt-in, explicit consent |
| LGPD | Brazil | Opt-in consent (single OK but double recommended) |
| CAN-SPAM | US | Opt-out (unsubscribe link), no double opt-in required |
| CASL | Canada | Express consent (similar to GDPR) |

**Universal rule**: Always include unsubscribe link. Always honor unsubscribe within 10 business days. Log consent timestamps.

### Multi-Region Email Strategy
```yaml
email_compliance:
  eu_subscribers:
    optin_type: double
    consent_text: "I agree to receive marketing emails..."
    unsubscribe: one_click
    data_retention: "2 years after last engagement"
  br_subscribers:
    optin_type: single  # double recommended
    consent_text: "Aceito receber emails..."
    unsubscribe: one_click
    data_retention: "2 years after last engagement"
```

## 8. Platform-Specific Compliance Summary

| Requirement | Hotmart (BR) | DS24 (EU) |
|-------------|-------------|-----------|
| Refund period | 7 days (CDC, cannot waive) | 14 days (Widerrufsrecht, waivable for digital) |
| Tax handling | Seller responsibility (NF) | DS24 handles (MoR) |
| Data protection | LGPD | GDPR (DPA required) |
| Legal identity | CPF/CNPJ | Impressum (DACH) |
| Email consent | Single opt-in OK | Double opt-in required |
| Cookie consent | LGPD consent banner | GDPR explicit opt-in |
| Payment security | PCI-DSS (Hotmart handles) | PSD2/SCA (DS24 handles) |

## 9. Compliance Checklist

### Before Launch
- [ ] Privacy policy published (covers GDPR + LGPD)
- [ ] Cookie consent banner with opt-in (not pre-checked)
- [ ] Double opt-in for EU email collection
- [ ] Impressum page (if selling into DACH)
- [ ] DPA signed with DS24
- [ ] DPA signed with email provider
- [ ] Refund policy published (7 days BR, 14 days EU)
- [ ] Widerrufsrecht waiver for digital products (DS24 handles)
- [ ] Unsubscribe link in every email
- [ ] Data erasure process documented

### Ongoing
- [ ] Quarterly review of privacy policy
- [ ] Annual DPA review with all processors
- [ ] Monitor refund rates (< 5% BR, < 8% EU)
- [ ] Respond to data access/erasure requests within 30 days
- [ ] Update cookie consent for new tracking tools

## Regras de Ouro

1. **DS24 for EU VAT** — MoR model eliminates VAT registration headaches.
2. **Double opt-in for EU** — single opt-in is GDPR non-compliant.
3. **7-day refund in BR is absolute** — cannot be waived; budget for it.
4. **Impressum for DACH** — required by German law, 2-click reachable.
5. **DPAs with every processor** — DS24, email provider, analytics tool.
6. **Cookie opt-in before tracking** — pre-checked boxes are illegal in EU.


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating
