---
id: ex_input_schema_partner_registration
kind: input_schema
pillar: P06
version: 1.0.0
title: "Input Schema -- B2B Partner Registration Form"
description: "Validation schema for B2B partner registration. CNPJ validation, field constraints, error messages, and multi-step form flow spec."
domain: crm
nucleus: N06
quality: 9.1
tags: [input-schema, partner-registration, b2b, cnpj, validation, form]
brand_placeholders:
  - BRAND_NAME
  - BRAND_PARTNER_EMAIL
  - BRAND_DOMAIN
density_score: 1.0
---

# Input Schema -- B2B Partner Registration Form

> Validates new partner registration submissions. CNPJ checked via external API
> (ReceitaWS or equivalent). All fields have client + server validation.

---

## 1. Form Steps

```
Step 1: Company Info   ->   Step 2: Contact Info   ->   Step 3: Confirm + Submit
  cnpj, company_name         contact_name, email          Review + LGPD consent
  state, region              whatsapp, role               [Submit for review]
```

---

## 2. Field Definitions

### Step 1: Company Info

| Field | Type | Required | Rules | Error message |
|-------|------|----------|-------|---------------|
| cnpj | string | YES | 14 digits, format XX.XXX.XXX/XXXX-XX, valid via ReceitaWS | "CNPJ invalido ou nao encontrado na Receita Federal" |
| company_name | string | YES | 2-200 chars | "Razao social obrigatoria (2-200 caracteres)" |
| trade_name | string | NO | max 200 chars | -- |
| state | enum | YES | BR state codes (2 chars) | "Selecione o estado" |
| city | string | YES | 2-100 chars | "Cidade obrigatoria" |
| monthly_volume_estimate | enum | YES | "1-20", "21-100", "101-500", "500+" | "Selecione o volume estimado" |

### Step 2: Contact Info

| Field | Type | Required | Rules | Error message |
|-------|------|----------|-------|---------------|
| contact_name | string | YES | 2-100 chars | "Nome do contato obrigatorio" |
| email | email | YES | valid email, unique in system | "Email invalido ou ja cadastrado" |
| whatsapp | string | YES | E.164 or BR format (+55XXXXXXXXXXX) | "WhatsApp invalido (ex: 11999887766)" |
| role | string | NO | max 100 chars | -- |
| how_did_you_hear | enum | NO | instagram, google, indicacao, evento, outro | -- |

### Step 3: Confirm

| Field | Type | Required | Rules |
|-------|------|----------|-------|
| lgpd_consent | boolean | YES | must be true | "Aceite os termos para continuar" |
| marketing_consent | boolean | NO | optional opt-in | -- |

---

## 3. CNPJ Validation Flow

```
1. User types CNPJ (client-side format mask)
2. Client validates format (14 digits, valid check digit)
3. On blur: POST /api/validate-cnpj?cnpj={value}
4. Server calls ReceitaWS API
5. If valid: auto-fill company_name, state (if available)
6. If invalid: show error + block form progression
7. If API down: allow submission, flag for manual review
```

### CNPJ Validation Endpoint Contract

```typescript
// POST /api/validate-cnpj
// Request
{ cnpj: string }

// Response (success)
{
  valid: true,
  cnpj: "12.345.678/0001-90",
  company_name: "EMPRESA MODELO LTDA",
  status: "ATIVA",
  state: "SP"
}

// Response (invalid)
{ valid: false, error: "CNPJ nao encontrado" }
```

---

## 4. Server-Side Validation (edge function)

```typescript
import { z } from 'zod'

const partnerRegistrationSchema = z.object({
  cnpj: z.string().regex(/^\d{14}$/, "CNPJ deve ter 14 digitos"),
  company_name: z.string().min(2).max(200),
  trade_name: z.string().max(200).optional(),
  state: z.string().length(2),
  city: z.string().min(2).max(100),
  monthly_volume_estimate: z.enum(["1-20", "21-100", "101-500", "500+"]),
  contact_name: z.string().min(2).max(100),
  email: z.string().email(),
  whatsapp: z.string().regex(/^(\+55)?\d{10,11}$/),
  role: z.string().max(100).optional(),
  how_did_you_hear: z.enum(["instagram","google","indicacao","evento","outro"]).optional(),
  lgpd_consent: z.literal(true, { errorMap: () => ({ message: "Consentimento obrigatorio" }) }),
  marketing_consent: z.boolean().optional()
})

type PartnerRegistration = z.infer<typeof partnerRegistrationSchema>
```

---

## 5. Post-Submission Flow

```
Submit
  |
  v
Server validates schema
  |-- FAIL -> 422 with field errors
  |
  v
CNPJ uniqueness check (DB)
  |-- DUPLICATE -> 409 "CNPJ ja cadastrado. Contato: {{BRAND_PARTNER_EMAIL}}"
  |
  v
Insert partner record (status=pending)
  |
  v
Send confirmation email to partner
Send notification to admin
  |
  v
200 -> /b2b/cadastro/confirmacao
```

---

## 6. Error Code Map

| Code | Scenario | User message |
|------|----------|-------------|
| 422 | Validation failed | Show field errors |
| 409 | CNPJ already registered | "CNPJ ja cadastrado. Contato: {{BRAND_PARTNER_EMAIL}}" |
| 503 | ReceitaWS API down | "Validacao automatica indisponivel. Enviaremos confirmacao manual em 24h." |
| 500 | DB error | "Erro interno. Tente novamente ou contate {{BRAND_PARTNER_EMAIL}}" |
