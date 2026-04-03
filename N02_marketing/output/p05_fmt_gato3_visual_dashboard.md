---
id: p05_fmt_gato3_visual_dashboard
kind: formatter
pillar: P05
title: "Dashboard Visual GATO³ — Interface de Gestão Felina"
version: 1.0.0
created: 2026-04-03
updated: 2026-04-03
author: n02_marketing
target_format: html
input_type: structured_data
rule_count: 12
domain: brand_dashboard
quality: null
tags: [formatter, html, dashboard, gato3, felino, gestao, brand]
tldr: "Dashboard HTML específico para GATO³ com métricas de bem-estar felino, branding PB minimalista, vendas por região ABC, e interface em pt-BR"
template_engine: string_template
pretty_print: true
escaping: html_entities
encoding: utf8
locale: pt-BR
streaming: false
keywords: [gato3, dashboard, felino, bem-estar, abc-paulista, pet, tutor]
density_score: 0.87
---

# Dashboard Visual GATO³

## Purpose
Interface de gestão visual específica para GATO³, com métricas de curadoria felina, vendas por região (ABC → Grande SP), satisfação de tutores, e branding PB minimalista. Focado no negócio de bem-estar felino com dados em pt-BR.

## Input Schema
```yaml
brand_data:
  name: string (GATO³)
  tagline: string 
  colors: object (primary, secondary, accent)
metrics:
  revenue: number (BRL)
  active_tutors: number
  products_sold: number  
  satisfaction_rate: number (0-100)
sales_by_category:
  - category: string
    value: number
    growth: string
regions:
  - name: string (ABC, Grande SP, etc)
    orders: number
    revenue: number
recent_activity:
  - tutor: string
    action: string  
    status: string
    timestamp: string
```

## Transform Rules

| Field | Transform | Rule/Template | Escape | Locale |
|-------|-----------|---------------|--------|---------|
| brand_name | template | `<span class="text-2xl font-bold">{{value}}</span>` | html | pt-BR |
| brand_tagline | template | `<span class="text-sm text-gray-500">{{value}}</span>` | html | pt-BR |
| revenue | stringify | `R$ {{value|number:2}}` | none | pt-BR |
| active_tutors | stringify | `{{value|number:0}} tutores` | none | pt-BR |  
| products_sold | stringify | `{{value|number:0}} produtos` | none | pt-BR |
| satisfaction_rate | stringify | `{{value}}% satisfação` | none | pt-BR |
| category_name | template | `<td class="px-4 py-3">{{value}}</td>` | html | pt-BR |
| category_value | template | `<td class="px-4 py-3 font-semibold">R$ {{value|number:2}}</td>` | html | pt-BR |
| region_name | template | `<td class="px-4 py-3">{{value}}</td>` | html | pt-BR |
| activity_tutor | template | `<td class="px-4 py-3">{{value}}</td>` | html | pt-BR |
| activity_status | template | `<span class="px-2 py-1 rounded-full text-xs bg-green-500/20 text-green-400">{{value}}</span>` | html | pt-BR |
| timestamp | stringify | `{{value|date:'dd/MM/yyyy HH:mm'}}` | none | pt-BR |

## HTML Template

```html
<!DOCTYPE html>
<html lang="pt-BR" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard — {{brand_name}}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --gato3-primary: #000000;
      --gato3-secondary: #1F1F1F; 
      --gato3-accent: #7A7A7A;
      --gato3-background: #FFFFFF;
      --gato3-surface: #D1D1D1;
      --gato3-text-primary: #000000;
      --gato3-text-secondary: #7A7A7A;
      --gato3-border: #D1D1D1;
    }
    body { font-family: 'Inter', sans-serif; }
  </style>
</head>
<body class="bg-white text-black">

  <!-- SIDEBAR -->
  <aside id="sidebar" class="fixed inset-y-0 left-0 z-30 w-64 bg-[var(--gato3-secondary)]
         border-r border-[var(--gato3-border)] transform -translate-x-full lg:translate-x-0
         transition-transform duration-200">
    <!-- Logo GATO³ -->
    <div class="h-16 flex items-center px-6 border-b border-[var(--gato3-border)]">
      <div class="text-2xl font-bold text-white">{{brand_name}}</div>
      <div class="ml-2 text-xs text-gray-400">³</div>
    </div>
    <!-- Navegação Pet Business -->
    <nav class="p-4 space-y-1">
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg bg-[var(--gato3-accent)]
         text-white">
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
        </svg>
        Dashboard Felino
      </a>
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-400
         hover:bg-[var(--gato3-accent)] hover:text-white transition-colors">
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
          <path d="M16 6V4c0-1.11-.89-2-2-2h-4c-1.11 0-2 .89-2 2v2H4v2h2v11c0 1.11.89 2 2 2h8c1.11 0 2-.89 2-2V8h2V6h-4zM8 4h8v2H8V4zm8 15H8V8h8v11z"/>
        </svg>
        Produtos Curados
      </a>
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-400
         hover:bg-[var(--gato3-accent)] hover:text-white transition-colors">
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
          <path d="M16 4c0-1.11.89-2 2-2s2 .89 2 2-.89 2-2 2-2-.89-2-2zm4 18v-6h2.5l-2.54-7.63A1.5 1.5 0 0 0 18.54 7H16c-.8 0-1.54.5-1.85 1.26l-1.92 5.77A2 2 0 0 0 14.12 16H16v6h4z"/>
        </svg>
        Tutores Ativos  
      </a>
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-400
         hover:bg-[var(--gato3-accent)] hover:text-white transition-colors">
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
        </svg>
        Avaliações
      </a>
    </nav>
  </aside>

  <!-- CONTEÚDO PRINCIPAL -->
  <div class="lg:ml-64 min-h-screen">
    <!-- Barra Superior -->
    <header class="h-16 border-b border-[var(--gato3-border)] flex items-center justify-between px-6 bg-white">
      <div class="flex items-center gap-4">
        <button onclick="document.getElementById('sidebar').classList.toggle('-translate-x-full')"
                class="lg:hidden p-2 rounded-lg hover:bg-gray-100">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
        </button>
        <div>
          <h1 class="font-semibold text-black">Bem-estar Felino</h1>
          <p class="text-sm text-[var(--gato3-text-secondary)]">{{brand_tagline}}</p>
        </div>
      </div>
      <div class="text-sm text-[var(--gato3-text-secondary)]">ABC Paulista → Brasil</div>
    </header>

    <!-- Métricas Principais -->
    <main class="p-6">
      <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4 mb-8">
        <div class="p-6 rounded-xl bg-white border border-[var(--gato3-border)] shadow-sm">
          <p class="text-sm text-[var(--gato3-text-secondary)]">Receita Total</p>
          <p class="text-2xl font-bold mt-1 text-black">{{revenue}}</p>
          <p class="text-sm mt-2 text-green-600">+15% vs mês anterior</p>
        </div>
        <div class="p-6 rounded-xl bg-white border border-[var(--gato3-border)] shadow-sm">
          <p class="text-sm text-[var(--gato3-text-secondary)]">Tutores Ativos</p>
          <p class="text-2xl font-bold mt-1 text-black">{{active_tutors}}</p>
          <p class="text-sm mt-2 text-green-600">+42 esta semana</p>
        </div>
        <div class="p-6 rounded-xl bg-white border border-[var(--gato3-border)] shadow-sm">
          <p class="text-sm text-[var(--gato3-text-secondary)]">Produtos Vendidos</p>
          <p class="text-2xl font-bold mt-1 text-black">{{products_sold}}</p>
          <p class="text-sm mt-2 text-orange-500">Tapetes gelados em alta</p>
        </div>
        <div class="p-6 rounded-xl bg-white border border-[var(--gato3-border)] shadow-sm">
          <p class="text-sm text-[var(--gato3-text-secondary)]">Satisfação</p>
          <p class="text-2xl font-bold mt-1 text-black">{{satisfaction_rate}}</p>
          <p class="text-sm mt-2 text-green-600">NPS: Zona de Excelência</p>
        </div>
      </div>

      <!-- Tabela de Vendas por Categoria -->
      <div class="grid lg:grid-cols-2 gap-6 mb-8">
        <div class="rounded-xl bg-white border border-[var(--gato3-border)] shadow-sm overflow-hidden">
          <div class="p-4 border-b border-[var(--gato3-border)]">
            <h2 class="text-lg font-semibold text-black">Vendas por Categoria</h2>
          </div>
          <table class="w-full text-sm">
            <thead>
              <tr class="border-b border-[var(--gato3-border)] text-left text-[var(--gato3-text-secondary)]">
                <th class="px-4 py-3 font-medium">Categoria</th>
                <th class="px-4 py-3 font-medium">Valor</th>
                <th class="px-4 py-3 font-medium">Crescimento</th>
              </tr>
            </thead>
            <tbody class="text-sm">
              {{#each sales_by_category}}
              <tr class="border-b border-[var(--gato3-border)] hover:bg-gray-50 transition-colors">
                <td class="px-4 py-3 text-black">{{category}}</td>
                <td class="px-4 py-3 font-semibold text-black">{{value}}</td>
                <td class="px-4 py-3 text-green-600">{{growth}}</td>
              </tr>
              {{/each}}
            </tbody>
          </table>
        </div>

        <!-- Expansão Regional -->
        <div class="rounded-xl bg-white border border-[var(--gato3-border)] shadow-sm overflow-hidden">
          <div class="p-4 border-b border-[var(--gato3-border)]">
            <h2 class="text-lg font-semibold text-black">Expansão Regional</h2>
          </div>
          <table class="w-full text-sm">
            <thead>
              <tr class="border-b border-[var(--gato3-border)] text-left text-[var(--gato3-text-secondary)]">
                <th class="px-4 py-3 font-medium">Região</th>
                <th class="px-4 py-3 font-medium">Pedidos</th>
                <th class="px-4 py-3 font-medium">Receita</th>
              </tr>
            </thead>
            <tbody class="text-sm">
              {{#each regions}}
              <tr class="border-b border-[var(--gato3-border)] hover:bg-gray-50 transition-colors">
                <td class="px-4 py-3 text-black">{{name}}</td>
                <td class="px-4 py-3 text-black">{{orders}}</td>
                <td class="px-4 py-3 font-semibold text-black">R$ {{revenue}}</td>
              </tr>
              {{/each}}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Atividade Recente -->
      <div class="rounded-xl bg-white border border-[var(--gato3-border)] shadow-sm overflow-hidden">
        <div class="p-4 border-b border-[var(--gato3-border)]">
          <h2 class="text-lg font-semibold text-black">Atividade Recente</h2>
        </div>
        <table class="w-full text-sm">
          <thead>
            <tr class="border-b border-[var(--gato3-border)] text-left text-[var(--gato3-text-secondary)]">
              <th class="px-4 py-3 font-medium">Tutor</th>
              <th class="px-4 py-3 font-medium">Ação</th>
              <th class="px-4 py-3 font-medium">Status</th>
              <th class="px-4 py-3 font-medium">Data</th>
            </tr>
          </thead>
          <tbody class="text-sm">
            {{#each recent_activity}}
            <tr class="border-b border-[var(--gato3-border)] hover:bg-gray-50 transition-colors">
              <td class="px-4 py-3 text-black">{{tutor}}</td>
              <td class="px-4 py-3 text-[var(--gato3-text-secondary)]">{{action}}</td>
              <td class="px-4 py-3">{{status}}</td>
              <td class="px-4 py-3 text-[var(--gato3-text-secondary)]">{{timestamp}}</td>
            </tr>
            {{/each}}
          </tbody>
        </table>
      </div>
    </main>
  </div>

</body>
</html>
```

## Escaping Rules
- HTML entities para todos os campos de texto user-generated
- Valores monetários formatados com locale pt-BR (R$ X.XXX,XX)
- Datas formatadas como dd/MM/yyyy HH:mm
- Status badges com classes CSS seguras (green-400, orange-500, etc)

## Sample Output
**Input:**
```json
{
  "brand_name": "GATO³",
  "brand_tagline": "Educação que acalma, soluções que funcionam.",
  "revenue": 45231.50,
  "active_tutors": 1847,
  "products_sold": 3429,
  "satisfaction_rate": 94.2,
  "sales_by_category": [
    {"category": "Tapetes Gelados", "value": "R$ 18.400", "growth": "+28%"},
    {"category": "Camas de Janela", "value": "R$ 12.800", "growth": "+15%"}
  ]
}
```

**Output:** Dashboard HTML completo com métricas GATO³, branding PB minimalista, navegação pet-business, tabelas responsivas, e dados localizados em pt-BR.