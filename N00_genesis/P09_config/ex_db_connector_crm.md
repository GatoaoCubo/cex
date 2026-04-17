---
id: ex_db_connector_crm
kind: db_connector
pillar: P09
version: 1.0.0
title: "CRM DB Connector Template -- Supabase B2B Partner Tables"
description: "Supabase database connector for B2B CRM. Partner registration, contacts, orders, and activity log tables with RLS policies and type-safe client patterns."
domain: crm
nucleus: N06
quality: 9.0
tags: [db-connector, crm, supabase, b2b, partner, rls, typescript]
brand_placeholders:
  - BRAND_NAME
  - BRAND_CRM_TABLE_PREFIX
  - BRAND_SUPABASE_URL
  - BRAND_SUPABASE_ANON_KEY
density_score: 1.0
---

# CRM DB Connector -- Supabase B2B Partner Tables

> Replace `{{BRAND_CRM_TABLE_PREFIX}}` with your Supabase table prefix.
> Example: `brand` -> tables named `brand_partners`, `brand_contacts`, etc.

---

## 1. Schema Definition

### 1.1 Partners Table

```sql
create table {{BRAND_CRM_TABLE_PREFIX}}_partners (
  id          uuid primary key default gen_random_uuid(),
  cnpj        text unique not null,
  company     text not null,
  contact_name text not null,
  email       text not null,
  whatsapp    text,
  region      text,
  tier        text default 'starter' check (tier in ('starter', 'pro', 'enterprise')),
  status      text default 'pending' check (status in ('pending', 'active', 'suspended', 'cancelled')),
  approved_at timestamp with time zone,
  created_at  timestamp with time zone default now(),
  updated_at  timestamp with time zone default now()
);
```

### 1.2 Partner Contacts Table

```sql
create table {{BRAND_CRM_TABLE_PREFIX}}_partner_contacts (
  id          uuid primary key default gen_random_uuid(),
  partner_id  uuid references {{BRAND_CRM_TABLE_PREFIX}}_partners(id) on delete cascade,
  name        text not null,
  email       text,
  phone       text,
  role        text,
  is_primary  boolean default false,
  created_at  timestamp with time zone default now()
);
```

### 1.3 Partner Orders Table

```sql
create table {{BRAND_CRM_TABLE_PREFIX}}_b2b_orders (
  id          uuid primary key default gen_random_uuid(),
  partner_id  uuid references {{BRAND_CRM_TABLE_PREFIX}}_partners(id),
  order_ref   text unique,
  status      text default 'draft',
  total_amount decimal(10,2),
  discount_pct decimal(5,2),
  notes       text,
  created_at  timestamp with time zone default now(),
  fulfilled_at timestamp with time zone
);
```

### 1.4 Activity Log Table

```sql
create table {{BRAND_CRM_TABLE_PREFIX}}_partner_activity (
  id          uuid primary key default gen_random_uuid(),
  partner_id  uuid references {{BRAND_CRM_TABLE_PREFIX}}_partners(id),
  event_type  text not null,
  payload     jsonb,
  created_at  timestamp with time zone default now()
);
```

---

## 2. Row Level Security (RLS)

```sql
-- Partners: read own record only
alter table {{BRAND_CRM_TABLE_PREFIX}}_partners enable row level security;

create policy "partners_read_own"
  on {{BRAND_CRM_TABLE_PREFIX}}_partners
  for select using (auth.uid() = id);

-- Admin: full access via service_role key
-- Use SUPABASE_SERVICE_ROLE_KEY (not anon) for admin operations
```

---

## 3. TypeScript Client Pattern

```typescript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.BRAND_SUPABASE_URL!,
  process.env.BRAND_SUPABASE_ANON_KEY!
)

// Read partner by CNPJ
async function getPartnerByCnpj(cnpj: string) {
  const { data, error } = await supabase
    .from('{{BRAND_CRM_TABLE_PREFIX}}_partners')
    .select('*')
    .eq('cnpj', cnpj)
    .single()
  if (error) throw error
  return data
}

// Create partner record
async function createPartner(partner: PartnerInsert) {
  const { data, error } = await supabase
    .from('{{BRAND_CRM_TABLE_PREFIX}}_partners')
    .insert(partner)
    .select()
    .single()
  if (error) throw error
  return data
}

// Update partner status
async function approvePartner(id: string) {
  const { error } = await supabase
    .from('{{BRAND_CRM_TABLE_PREFIX}}_partners')
    .update({ status: 'active', approved_at: new Date().toISOString() })
    .eq('id', id)
  if (error) throw error
}
```

---

## 4. Integration Points

| System | Direction | Trigger | Notes |
|--------|-----------|---------|-------|
| CNPJ validation API | inbound | On registration | ReceitaWS or equivalent |
| {{BRAND_ERP}} | outbound | On order creation | Push B2B order to ERP |
| Email/WhatsApp | outbound | On status change | Notify partner of approval |
| Admin dashboard | read | On demand | CRM tab in admin panel |

---

## 5. Environment Variables

```bash
BRAND_SUPABASE_URL=https://your-project.supabase.co
BRAND_SUPABASE_ANON_KEY=eyJ...    # public anon key (safe for frontend)
SUPABASE_SERVICE_ROLE_KEY=eyJ...  # private (server/edge functions only)
```

---

## New Brand Variables

- `BRAND_CRM_TABLE_PREFIX` -- Supabase table prefix (e.g. "brand", "myco", "acme")
- `BRAND_SUPABASE_URL` -- Supabase project URL
- `BRAND_SUPABASE_ANON_KEY` -- Supabase anon key
