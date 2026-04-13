---
id: tpl_crm_admin_spec
kind: template
pillar: P12
title: "CRM Admin Panel — Specification Template"
version: 1.0.0
quality: 9.1
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo commit 1744e921 (CRM_ADMIN mission)
variables: [BRAND_NAME, DB_PROVIDER, TABLES, MAP_PROVIDER, AUTH_METHOD, FRAMEWORK, REGION]
density_score: 0.95
tags: [template, crm, admin, specification, fullstack, instance-extraction]
tldr: "CRM admin panel spec — database schema, frontend components, map integration, auth. Any brand fills slots."
updated: "2026-04-13"
---

# CRM Admin Panel — {{BRAND_NAME}}

## Architecture Decision Record

| Decision | Choice | Alternatives Considered |
|----------|--------|------------------------|
| Database | {{DB_PROVIDER | default: 'Supabase'}} | Firebase, PlanetScale, Neon, self-hosted Postgres |
| Frontend | {{FRAMEWORK | default: 'React + Vite'}} | Next.js, SvelteKit, Astro |
| Map | {{MAP_PROVIDER | default: 'Leaflet + OpenStreetMap'}} | Google Maps API, Mapbox |
| Auth | {{AUTH_METHOD | default: 'Row-Level Security'}} | JWT, NextAuth, Clerk |
| Styling | Tailwind CSS + shadcn/ui | MUI, Chakra, Ant Design |

---

## Database Schema

### {{TABLES.contacts | default: 'crm_contacts'}}

```sql
CREATE TABLE {{TABLES.contacts | default: 'crm_contacts'}} (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  cnpj TEXT,
  razao_social TEXT,
  nome_fantasia TEXT NOT NULL,
  segmento TEXT NOT NULL,
  sub_segmento TEXT,
  endereco TEXT,
  cidade TEXT NOT NULL,
  uf TEXT DEFAULT '{{STATE | default: 'SP'}}',
  cep TEXT,
  telefone TEXT,
  whatsapp TEXT,
  email TEXT,
  website TEXT,
  instagram TEXT,
  google_maps_url TEXT,
  google_rating NUMERIC(2,1),
  google_reviews INTEGER DEFAULT 0,
  lat NUMERIC(10,7),
  lng NUMERIC(10,7),
  porte TEXT CHECK (porte IN ('MEI','ME','EPP','medio','grande')),
  potencial_b2b TEXT CHECK (potencial_b2b IN ('S+','S','A','B','C')),
  status TEXT DEFAULT 'prospect' CHECK (status IN ('prospect','contacted','negotiating','partner','inactive')),
  fonte TEXT,
  notas TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for common queries
CREATE INDEX idx_contacts_cidade ON {{TABLES.contacts}}(cidade);
CREATE INDEX idx_contacts_segmento ON {{TABLES.contacts}}(segmento);
CREATE INDEX idx_contacts_status ON {{TABLES.contacts}}(status);
CREATE INDEX idx_contacts_potencial ON {{TABLES.contacts}}(potencial_b2b);

-- Row-Level Security
ALTER TABLE {{TABLES.contacts}} ENABLE ROW LEVEL SECURITY;

CREATE POLICY "team_read" ON {{TABLES.contacts}}
  FOR SELECT USING (auth.role() = 'authenticated');

CREATE POLICY "team_write" ON {{TABLES.contacts}}
  FOR ALL USING (auth.role() = 'authenticated');
```

---

## Frontend Components

### Tab Structure

| Tab | Component | Description |
|-----|-----------|-------------|
| Dashboard | `<CRMDashboard />` | KPIs, charts, pipeline funnel |
| Contacts | `<CRMContacts />` | Table + filters + detail panel |
| Map | `<CRMMap />` | Leaflet map with clustered markers |

### Dashboard Tab

```
┌─────────────────────────────────────────┐
│  KPI Cards (6): Total │ Phone │ Email │ │
│  │ Address │ Partners │ Prospects       │
├─────────────────────────────────────────┤
│  Chart: Contacts by City (bar)          │
│  Chart: Pipeline Funnel (horizontal)    │
│  Chart: Segment Distribution (donut)    │
└─────────────────────────────────────────┘
```

### Contacts Tab

```
┌─────────────────────────────────────────┐
│  Search │ Filter: City │ Segment │Status│
├─────────────────────────────────────────┤
│  Table: sortable, paginated             │
│  Click row → Detail Panel (slide-in)    │
│    → Edit fields inline                 │
│    → Add notes                          │
│    → Change status                      │
└─────────────────────────────────────────┘
```

### Map Tab

```
┌─────────────────────────────────────────┐
│  Leaflet Map                            │
│  Center: {{MAP_CENTER_LAT}}, {{MAP_CENTER_LNG}} │
│  Zoom: {{MAP_ZOOM | default: '12'}}     │
│  Markers: clustered by proximity        │
│  Click marker → popup with contact info │
│  Color by: segment or status            │
└─────────────────────────────────────────┘
```

---

## Hooks (React)

| Hook | Purpose |
|------|---------|
| `useCRMContacts()` | Fetch + filter + paginate contacts |
| `useCRMStats()` | Aggregate KPIs and chart data |
| `useCRMUpdate()` | Optimistic update + revalidation |

---

## Seed Migration

```sql
-- Seed from JSON export
-- Generate via: python _build_crm_seed.py > seed.sql
INSERT INTO {{TABLES.contacts}} (nome_fantasia, segmento, cidade, uf, telefone, lat, lng, fonte)
VALUES
  ('Example Business', '{{INDUSTRY}}', '{{CITY}}', '{{STATE}}', '+55 11 99999-0000', -23.62, -46.55, 'seed');
```

---

## Route Configuration

```
/admin/crm           → CRM page (protected)
/admin/crm/dashboard → Dashboard tab (default)
/admin/crm/contacts  → Contacts tab
/admin/crm/map       → Map tab
```

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| react-leaflet | ^4.x | Map component |
| leaflet | ^1.9.x | Map engine |
| leaflet.markercluster | ^1.5.x | Marker clustering |
| recharts | ^2.x | Charts |
| @supabase/supabase-js | ^2.x | Database client |
