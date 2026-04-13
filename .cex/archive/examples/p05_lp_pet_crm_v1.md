---
id: p05_lp_pet_crm_v1
kind: landing_page
pillar: P05
title: "PetCRM — Organize, Fidelize, Cresça"
version: 1.0.0
created: 2026-04-12
author: landing-page-builder
quality: 9.1
tags: [landing-page, crm, pet-shop, pt-br, responsive, dark-mode, lead-capture]
stack: html-tailwind-cdn
sections_count: 7
responsive: true
dark_mode: true
a11y: AA
language: pt-BR
goal: lead_capture
target_audience: donos_de_pet_shop
cta_primary: "Comece Gratis"
seo:
  title: "PetCRM — O Sistema de Gestao para Pet Shops Modernos"
  description: "Agendamento online, ficha completa do pet, lembretes automaticos e relatorios de faturamento. Tudo em um lugar. Comece gratis hoje."
  og_image: "https://picsum.photos/seed/petcrm/1200/630"
density_score: 0.98
---

# Landing Page: PetCRM

## Design Tokens

| Token | Value |
|-------|-------|
| Primary | #0ea5e9 (sky-500) |
| Secondary | #f97316 (orange-500) |
| Background | #ffffff / #0f172a (dark) |
| Text | #0f172a / #f1f5f9 (dark) |
| Muted | #64748b |
| Font Heading | Inter (700) |
| Font Body | Inter (400/500) |
| Radius | rounded-2xl |

## Sections

- [x] HERO — headline + subheadline + CTA primario + imagem
- [x] DOR — 3 pain points com icones
- [x] FEATURES — 4 funcionalidades principais
- [x] COMO FUNCIONA — 3 passos
- [x] PROVA SOCIAL — 3 depoimentos
- [x] CTA FINAL — urgencia + conversao
- [x] FOOTER — links basicos

## Code

```html
<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>PetCRM — O Sistema de Gestao para Pet Shops Modernos</title>
  <meta name="description" content="Agendamento online, ficha completa do pet, lembretes automaticos e relatorios de faturamento. Tudo em um lugar. Comece gratis hoje." />
  <meta property="og:title" content="PetCRM — O Sistema de Gestao para Pet Shops Modernos" />
  <meta property="og:description" content="Organize seu pet shop, fidelize clientes e cresça com dados. Comece gratis, sem cartao de credito." />
  <meta property="og:image" content="https://picsum.photos/seed/petcrm/1200/630" />
  <meta property="og:type" content="website" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: { sans: ['Inter', 'sans-serif'] },
          colors: {
            brand: {
              50:  '#f0f9ff',
              100: '#e0f2fe',
              500: '#0ea5e9',
              600: '#0284c7',
              700: '#0369a1',
            },
            accent: {
              400: '#fb923c',
              500: '#f97316',
              600: '#ea580c',
            }
          }
        }
      }
    }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "PetCRM",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "description": "Sistema de gestao para pet shops com agendamento, ficha de pets e lembretes automaticos.",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "BRL",
      "description": "Plano gratuito disponivel"
    }
  }
  </script>
  <style>
    html { font-family: 'Inter', sans-serif; }
    .gradient-hero {
      background: linear-gradient(135deg, #0ea5e9 0%, #0369a1 50%, #1e3a5f 100%);
    }
    .dark .gradient-hero {
      background: linear-gradient(135deg, #0369a1 0%, #0f172a 50%, #020617 100%);
    }
    @media (prefers-color-scheme: dark) {
      html { color-scheme: dark; }
    }
  </style>
</head>
<body class="bg-white dark:bg-slate-950 text-slate-900 dark:text-slate-100 antialiased">

  <!-- NAV -->
  <nav aria-label="Navegacao principal" class="fixed top-0 left-0 right-0 z-50 bg-white/90 dark:bg-slate-950/90 backdrop-blur-sm border-b border-slate-100 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-lg bg-brand-500 flex items-center justify-center">
            <span class="text-white font-bold text-sm" aria-hidden="true">P</span>
          </div>
          <span class="font-bold text-lg text-slate-900 dark:text-white">PetCRM</span>
        </div>
        <div class="hidden md:flex items-center gap-8">
          <a href="#features" class="text-sm text-slate-600 dark:text-slate-400 hover:text-brand-500 transition-colors">Funcionalidades</a>
          <a href="#como-funciona" class="text-sm text-slate-600 dark:text-slate-400 hover:text-brand-500 transition-colors">Como Funciona</a>
          <a href="#depoimentos" class="text-sm text-slate-600 dark:text-slate-400 hover:text-brand-500 transition-colors">Depoimentos</a>
        </div>
        <div class="flex items-center gap-3">
          <a href="#cta" data-track="nav-login" class="hidden md:inline text-sm font-medium text-slate-600 dark:text-slate-400 hover:text-brand-500 transition-colors">Entrar</a>
          <a href="#cta" data-track="nav-cta" class="inline-flex items-center px-4 py-2 rounded-lg bg-brand-500 hover:bg-brand-600 text-white text-sm font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-brand-500 focus:ring-offset-2">
            Comece Gratis
          </a>
        </div>
        <button id="menu-toggle" aria-label="Abrir menu" aria-expanded="false" aria-controls="mobile-menu" class="md:hidden p-2 rounded-md text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
      </div>
    </div>
    <div id="mobile-menu" class="hidden md:hidden border-t border-slate-100 dark:border-slate-800 px-4 py-3 space-y-2">
      <a href="#features" class="block py-2 text-sm text-slate-700 dark:text-slate-300">Funcionalidades</a>
      <a href="#como-funciona" class="block py-2 text-sm text-slate-700 dark:text-slate-300">Como Funciona</a>
      <a href="#depoimentos" class="block py-2 text-sm text-slate-700 dark:text-slate-300">Depoimentos</a>
      <a href="#cta" data-track="mobile-cta" class="block w-full text-center py-2.5 rounded-lg bg-brand-500 text-white text-sm font-semibold">Comece Gratis</a>
    </div>
  </nav>

  <main>

    <!-- HERO -->
    <section id="hero" aria-label="Hero" class="gradient-hero pt-24 pb-20 md:pt-32 md:pb-28 overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-2 gap-12 items-center">
          <div class="text-center lg:text-left">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/20 text-white text-xs font-medium mb-6">
              <span class="w-1.5 h-1.5 rounded-full bg-green-400 inline-block" aria-hidden="true"></span>
              Mais de 1.200 pet shops ja confiam no PetCRM
            </div>
            <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-white leading-tight">
              Chega de agenda<br class="hidden sm:block" /> no caderno.
            </h1>
            <p class="mt-6 text-lg md:text-xl text-sky-100 max-w-lg mx-auto lg:mx-0">
              Gerencie agendamentos, fichas dos pets, lembretes automaticos e faturamento — tudo em um unico sistema feito para pet shops.
            </p>
            <div class="mt-8 flex flex-col sm:flex-row gap-3 justify-center lg:justify-start">
              <a href="#cta" data-track="hero-cta-primary" class="inline-flex items-center justify-center px-6 py-3.5 rounded-xl bg-accent-500 hover:bg-accent-600 text-white font-bold text-base transition-colors shadow-lg focus:outline-none focus:ring-2 focus:ring-accent-500 focus:ring-offset-2">
                Comece Gratis — sem cartao
              </a>
              <a href="#como-funciona" data-track="hero-cta-secondary" class="inline-flex items-center justify-center px-6 py-3.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-semibold text-base transition-colors border border-white/30 focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-brand-700">
                Ver como funciona
              </a>
            </div>
            <p class="mt-4 text-sky-200 text-sm">Gratis por 14 dias. Sem compromisso. Cancele quando quiser.</p>
          </div>
          <div class="relative lg:block" aria-hidden="true">
            <div class="rounded-2xl overflow-hidden shadow-2xl border border-white/20">
              <img
                src="https://picsum.photos/seed/petcrm-dash/700/480"
                alt="Dashboard do PetCRM mostrando agenda e fichas de pets"
                class="w-full object-cover"
                loading="eager"
              />
            </div>
            <div class="absolute -bottom-4 -left-4 bg-white dark:bg-slate-800 rounded-xl p-3 shadow-lg flex items-center gap-2">
              <div class="w-8 h-8 rounded-full bg-green-100 flex items-center justify-center">
                <svg class="w-4 h-4 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
              </div>
              <div>
                <p class="text-xs font-semibold text-slate-900 dark:text-white">Lembrete enviado</p>
                <p class="text-xs text-slate-500">Consulta do Rex amanha 14h</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- DOR / PAIN POINTS -->
    <section id="problemas" aria-label="Problemas que o PetCRM resolve" class="py-16 md:py-24 bg-slate-50 dark:bg-slate-900">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-12">
          <h2 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white">
            Reconhece algum desses problemas?
          </h2>
          <p class="mt-4 text-slate-600 dark:text-slate-400 text-lg">
            A maioria dos pet shops ainda opera no modo "apaga incendio". Isso custa clientes, tempo e dinheiro.
          </p>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
          <article class="bg-white dark:bg-slate-800 rounded-2xl p-6 border border-red-100 dark:border-red-900/30 shadow-sm">
            <div class="w-12 h-12 rounded-xl bg-red-100 dark:bg-red-900/30 flex items-center justify-center mb-4" aria-hidden="true">
              <svg class="w-6 h-6 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
            </div>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mb-2">Agenda bagunçada</h3>
            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
              Dois clientes no mesmo horario, compromisso esquecido, funcionario sem saber o que tem no dia. Agenda em caderno ou planilha nao escala.
            </p>
          </article>
          <article class="bg-white dark:bg-slate-800 rounded-2xl p-6 border border-orange-100 dark:border-orange-900/30 shadow-sm">
            <div class="w-12 h-12 rounded-xl bg-orange-100 dark:bg-orange-900/30 flex items-center justify-center mb-4" aria-hidden="true">
              <svg class="w-6 h-6 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
            </div>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mb-2">Historico perdido</h3>
            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
              "Qual vacina o Bolinha tomou mesmo?" Sem ficha digital, cada visita comeca do zero. Voce perde confiança — e o cliente percebe.
            </p>
          </article>
          <article class="bg-white dark:bg-slate-800 rounded-2xl p-6 border border-yellow-100 dark:border-yellow-900/30 shadow-sm">
            <div class="w-12 h-12 rounded-xl bg-yellow-100 dark:bg-yellow-900/30 flex items-center justify-center mb-4" aria-hidden="true">
              <svg class="w-6 h-6 text-yellow-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0"/></svg>
            </div>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mb-2">Clientes sumindo</h3>
            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
              Sem lembrete, o cliente esquece. Sem retorno automatico, ele vai no concorrente. Fidelidade nao acontece por acaso — ela e construida.
            </p>
          </article>
        </div>
      </div>
    </section>

    <!-- FEATURES -->
    <section id="features" aria-label="Funcionalidades do PetCRM" class="py-16 md:py-24 bg-white dark:bg-slate-950" style="scroll-margin-top: 4rem;">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-12">
          <h2 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white">
            Tudo que seu pet shop precisa
          </h2>
          <p class="mt-4 text-slate-600 dark:text-slate-400 text-lg">
            Do agendamento ao relatorio, o PetCRM cobre todos os pontos criticos da sua operacao.
          </p>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <article class="group p-6 rounded-2xl border border-slate-100 dark:border-slate-800 hover:border-brand-200 dark:hover:border-brand-800 hover:shadow-md transition-all">
            <div class="w-12 h-12 rounded-xl bg-brand-50 dark:bg-brand-900/30 flex items-center justify-center mb-4 group-hover:bg-brand-100 dark:group-hover:bg-brand-800/40 transition-colors" aria-hidden="true">
              <svg class="w-6 h-6 text-brand-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
            </div>
            <h3 class="font-bold text-slate-900 dark:text-white mb-2">Agendamento Online</h3>
            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
              Clientes agendam pelo link do seu pet shop, 24h por dia. Confirmacao automatica por WhatsApp ou e-mail.
            </p>
          </article>
          <article class="group p-6 rounded-2xl border border-slate-100 dark:border-slate-800 hover:border-brand-200 dark:hover:border-brand-800 hover:shadow-md transition-all">
            <div class="w-12 h-12 rounded-xl bg-green-50 dark:bg-green-900/30 flex items-center justify-center mb-4 group-hover:bg-green-100 dark:group-hover:bg-green-800/40 transition-colors" aria-hidden="true">
              <svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
            </div>
            <h3 class="font-bold text-slate-900 dark:text-white mb-2">Ficha Completa do Pet</h3>
            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
              Raca, idade, vacinas, alergias, historico de servicos e fotos. Tudo em um perfil digital acessivel em segundos.
            </p>
          </article>
          <article class="group p-6 rounded-2xl border border-slate-100 dark:border-slate-800 hover:border-brand-200 dark:hover:border-brand-800 hover:shadow-md transition-all">
            <div class="w-12 h-12 rounded-xl bg-purple-50 dark:bg-purple-900/30 flex items-center justify-center mb-4 group-hover:bg-purple-100 dark:group-hover:bg-purple-800/40 transition-colors" aria-hidden="true">
              <svg class="w-6 h-6 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/></svg>
            </div>
            <h3 class="font-bold text-slate-900 dark:text-white mb-2">Lembretes Automaticos</h3>
            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
              Envie lembretes de consulta, vacina em dia e retorno de banho pelo WhatsApp ou e-mail. Zero trabalho manual.
            </p>
          </article>
          <article class="group p-6 rounded-2xl border border-slate-100 dark:border-slate-800 hover:border-brand-200 dark:hover:border-brand-800 hover:shadow-md transition-all">
            <div class="w-12 h-12 rounded-xl bg-accent-50 dark:bg-accent-900/30 flex items-center justify-center mb-4 group-hover:bg-accent-100 dark:group-hover:bg-accent-800/40 transition-colors" aria-hidden="true">
              <svg class="w-6 h-6 text-accent-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
            </div>
            <h3 class="font-bold text-slate-900 dark:text-white mb-2">Relatorios de Faturamento</h3>
            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
              Veja servicos mais lucrativos, clientes mais frequentes e evolucao do faturamento. Tome decisoes com dados reais.
            </p>
          </article>
        </div>
      </div>
    </section>

    <!-- COMO FUNCIONA -->
    <section id="como-funciona" aria-label="Como funciona o PetCRM" class="py-16 md:py-24 bg-slate-50 dark:bg-slate-900" style="scroll-margin-top: 4rem;">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-12">
          <h2 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white">
            Comece em 3 passos simples
          </h2>
          <p class="mt-4 text-slate-600 dark:text-slate-400 text-lg">
            Sem instalacao, sem suporte tecnico, sem dor de cabeca. So abre e usa.
          </p>
        </div>
        <div class="grid md:grid-cols-3 gap-8">
          <div class="relative text-center">
            <div class="w-14 h-14 rounded-full bg-brand-500 text-white text-xl font-extrabold flex items-center justify-center mx-auto mb-5 shadow-lg" aria-hidden="true">1</div>
            <div class="hidden md:block absolute top-7 left-2/3 w-full h-0.5 bg-brand-100 dark:bg-brand-900" aria-hidden="true"></div>
            <h3 class="font-bold text-xl text-slate-900 dark:text-white mb-3">Cadastre seu pet shop</h3>
            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
              Crie sua conta gratis em 2 minutos. Sem cartao de credito. Configure o nome, servicos e horarios de funcionamento.
            </p>
          </div>
          <div class="relative text-center">
            <div class="w-14 h-14 rounded-full bg-brand-500 text-white text-xl font-extrabold flex items-center justify-center mx-auto mb-5 shadow-lg" aria-hidden="true">2</div>
            <div class="hidden md:block absolute top-7 left-2/3 w-full h-0.5 bg-brand-100 dark:bg-brand-900" aria-hidden="true"></div>
            <h3 class="font-bold text-xl text-slate-900 dark:text-white mb-3">Importe ou cadastre seus clientes</h3>
            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
              Adicione clientes e pets manualmente ou importe de uma planilha. Cada pet ganha sua propria ficha digital.
            </p>
          </div>
          <div class="text-center">
            <div class="w-14 h-14 rounded-full bg-brand-500 text-white text-xl font-extrabold flex items-center justify-center mx-auto mb-5 shadow-lg" aria-hidden="true">3</div>
            <h3 class="font-bold text-xl text-slate-900 dark:text-white mb-3">Gerencie e fidelize</h3>
            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
              Aceite agendamentos, envie lembretes e acompanhe o crescimento do seu negocio no painel de relatorios.
            </p>
          </div>
        </div>
        <div class="mt-12 text-center">
          <a href="#cta" data-track="como-funciona-cta" class="inline-flex items-center justify-center px-6 py-3.5 rounded-xl bg-brand-500 hover:bg-brand-600 text-white font-bold text-base transition-colors shadow focus:outline-none focus:ring-2 focus:ring-brand-500 focus:ring-offset-2">
            Quero comecar agora
          </a>
        </div>
      </div>
    </section>

    <!-- PROVA SOCIAL / DEPOIMENTOS -->
    <section id="depoimentos" aria-label="Depoimentos de clientes" class="py-16 md:py-24 bg-white dark:bg-slate-950" style="scroll-margin-top: 4rem;">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-12">
          <h2 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white">
            Pet shops que ja transformaram sua gestao
          </h2>
          <div class="flex items-center justify-center gap-1 mt-4" aria-label="Avaliacao media: 4.9 de 5 estrelas">
            <span class="text-amber-400 text-2xl" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
            <span class="ml-2 text-slate-600 dark:text-slate-400 text-sm font-medium">4.9 de 5 — baseado em 380+ avaliacoes</span>
          </div>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
          <blockquote class="bg-slate-50 dark:bg-slate-800 rounded-2xl p-6 border border-slate-100 dark:border-slate-700">
            <div class="flex items-center gap-1 mb-4" aria-label="5 estrelas" role="img">
              <span class="text-amber-400 text-sm" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
            </div>
            <p class="text-slate-700 dark:text-slate-300 text-sm leading-relaxed mb-5">
              "Antes eu perdia pelo menos um agendamento por semana por confusao na agenda. Desde que comecei a usar o PetCRM, zero conflitos. E os clientes adoram receber o lembrete no WhatsApp."
            </p>
            <footer class="flex items-center gap-3">
              <img src="https://ui-avatars.com/api/?name=Carla+Mendes&background=0ea5e9&color=fff&size=40" alt="" width="40" height="40" class="rounded-full" aria-hidden="true" loading="lazy" />
              <div>
                <cite class="not-italic font-semibold text-slate-900 dark:text-white text-sm">Carla Mendes</cite>
                <p class="text-xs text-slate-500 dark:text-slate-400">Pet Shop Patinhas Felizes — SP</p>
              </div>
            </footer>
          </blockquote>
          <blockquote class="bg-slate-50 dark:bg-slate-800 rounded-2xl p-6 border border-slate-100 dark:border-slate-700">
            <div class="flex items-center gap-1 mb-4" aria-label="5 estrelas" role="img">
              <span class="text-amber-400 text-sm" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
            </div>
            <p class="text-slate-700 dark:text-slate-300 text-sm leading-relaxed mb-5">
              "A ficha digital mudou tudo. Quando o cliente liga perguntando sobre o historico do pet, eu abro em 5 segundos. Antes ficava procurando em cadernos velhos. Parece besteira mas faz toda diferenca."
            </p>
            <footer class="flex items-center gap-3">
              <img src="https://ui-avatars.com/api/?name=Rodrigo+Silva&background=f97316&color=fff&size=40" alt="" width="40" height="40" class="rounded-full" aria-hidden="true" loading="lazy" />
              <div>
                <cite class="not-italic font-semibold text-slate-900 dark:text-white text-sm">Rodrigo Silva</cite>
                <p class="text-xs text-slate-500 dark:text-slate-400">Vet Amigo — BH</p>
              </div>
            </footer>
          </blockquote>
          <blockquote class="bg-slate-50 dark:bg-slate-800 rounded-2xl p-6 border border-slate-100 dark:border-slate-700">
            <div class="flex items-center gap-1 mb-4" aria-label="5 estrelas" role="img">
              <span class="text-amber-400 text-sm" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
            </div>
            <p class="text-slate-700 dark:text-slate-300 text-sm leading-relaxed mb-5">
              "Aumentei o retorno dos clientes em quase 40% so com os lembretes automaticos. Nao precisei contratar ninguem — o sistema faz esse trabalho por mim. Paga o investimento facil."
            </p>
            <footer class="flex items-center gap-3">
              <img src="https://ui-avatars.com/api/?name=Fernanda+Lima&background=22c55e&color=fff&size=40" alt="" width="40" height="40" class="rounded-full" aria-hidden="true" loading="lazy" />
              <div>
                <cite class="not-italic font-semibold text-slate-900 dark:text-white text-sm">Fernanda Lima</cite>
                <p class="text-xs text-slate-500 dark:text-slate-400">Mundo Animal — RJ</p>
              </div>
            </footer>
          </blockquote>
        </div>
      </div>
    </section>

    <!-- CTA FINAL -->
    <section id="cta" aria-label="Comece agora" class="py-16 md:py-24 bg-brand-600 dark:bg-brand-700" style="scroll-margin-top: 4rem;">
      <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl md:text-4xl font-extrabold text-white mb-4">
          Seu pet shop merece ferramentas profissionais.
        </h2>
        <p class="text-sky-100 text-lg mb-8 max-w-xl mx-auto">
          Comece gratis hoje. Sem cartao de credito, sem burocracia. Em 2 minutos voce ja tem uma agenda digital funcionando.
        </p>
        <form class="flex flex-col sm:flex-row gap-3 max-w-md mx-auto" aria-label="Formulario de cadastro" novalidate>
          <label for="email-cta" class="sr-only">Seu melhor e-mail</label>
          <input
            id="email-cta"
            type="email"
            placeholder="Seu melhor e-mail"
            autocomplete="email"
            class="flex-1 px-4 py-3.5 rounded-xl bg-white text-slate-900 placeholder-slate-400 text-sm font-medium focus:outline-none focus:ring-2 focus:ring-accent-400"
            required
            aria-required="true"
          />
          <button type="submit" data-track="cta-form-submit" class="px-6 py-3.5 rounded-xl bg-accent-500 hover:bg-accent-600 text-white font-bold text-sm transition-colors whitespace-nowrap shadow-lg focus:outline-none focus:ring-2 focus:ring-accent-400 focus:ring-offset-2 focus:ring-offset-brand-600">
            Comece Gratis
          </button>
        </form>
        <div class="mt-6 flex flex-wrap items-center justify-center gap-4 text-sky-100 text-xs">
          <span class="flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
            14 dias gratis
          </span>
          <span class="flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
            Sem cartao de credito
          </span>
          <span class="flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
            Cancele quando quiser
          </span>
          <span class="flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
            Suporte em portugues
          </span>
        </div>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer aria-label="Rodape" class="bg-slate-900 dark:bg-slate-950 text-slate-400 py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-3 gap-8 mb-8">
        <div>
          <div class="flex items-center gap-2 mb-3">
            <div class="w-7 h-7 rounded-md bg-brand-500 flex items-center justify-center" aria-hidden="true">
              <span class="text-white font-bold text-xs">P</span>
            </div>
            <span class="font-bold text-white text-base">PetCRM</span>
          </div>
          <p class="text-sm leading-relaxed">
            O sistema de gestao para pet shops que querem crescer com organizacao e dados.
          </p>
        </div>
        <div>
          <h3 class="text-white font-semibold text-sm mb-3">Produto</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="#features" class="hover:text-brand-400 transition-colors">Funcionalidades</a></li>
            <li><a href="#como-funciona" class="hover:text-brand-400 transition-colors">Como Funciona</a></li>
            <li><a href="#depoimentos" class="hover:text-brand-400 transition-colors">Depoimentos</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white font-semibold text-sm mb-3">Legal</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="#" class="hover:text-brand-400 transition-colors">Politica de Privacidade</a></li>
            <li><a href="#" class="hover:text-brand-400 transition-colors">Termos de Uso</a></li>
            <li><a href="mailto:contato@petcrm.com.br" class="hover:text-brand-400 transition-colors">Contato</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-slate-800 pt-6 flex flex-col sm:flex-row items-center justify-between gap-3">
        <p class="text-xs">&copy; 2026 PetCRM. Todos os direitos reservados.</p>
        <p class="text-xs">Feito com cuidado para quem cuida dos pets.</p>
      </div>
    </div>
  </footer>

  <script>
    // Mobile menu toggle
    var menuBtn = document.getElementById('menu-toggle');
    var mobileMenu = document.getElementById('mobile-menu');
    if (menuBtn && mobileMenu) {
      menuBtn.addEventListener('click', function() {
        var open = mobileMenu.classList.toggle('hidden');
        menuBtn.setAttribute('aria-expanded', String(!open));
      });
      mobileMenu.querySelectorAll('a').forEach(function(link) {
        link.addEventListener('click', function() {
          mobileMenu.classList.add('hidden');
          menuBtn.setAttribute('aria-expanded', 'false');
        });
      });
    }

    // Dark mode: respect OS preference
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      document.documentElement.classList.add('dark');
    }
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
      document.documentElement.classList.toggle('dark', e.matches);
    });

    // CTA form — placeholder submit handler
    var ctaForm = document.querySelector('form[aria-label="Formulario de cadastro"]');
    if (ctaForm) {
      ctaForm.addEventListener('submit', function(e) {
        e.preventDefault();
        var email = ctaForm.querySelector('input[type="email"]').value;
        if (email) {
          alert('Obrigado! Enviamos um link de acesso para ' + email);
        }
      });
    }

    // Analytics: track CTA clicks via data-track attribute
    document.querySelectorAll('[data-track]').forEach(function(el) {
      el.addEventListener('click', function() {
        var event = el.getAttribute('data-track');
        if (typeof gtag !== 'undefined') {
          gtag('event', 'click', { event_category: 'CTA', event_label: event });
        }
      });
    });
  </script>

</body>
</html>
```

## Deploy Instructions

1. Salve o bloco de codigo acima como `index.html`
2. Substitua as imagens `picsum.photos` por fotos reais do seu pet shop
3. Atualize os depoimentos com clientes reais (nome, foto, cidade)
4. Configure o formulario do `#cta` para seu provedor de e-mail (Mailchimp, RD Station, etc)
5. Adicione o Google Tag Manager ou GA4 antes de `</head>` para tracking
6. Deploy:
   - **Vercel**: `vercel deploy` (instante)
   - **Netlify**: arraste o arquivo para app.netlify.com
   - **GitHub Pages**: commit em `/docs/index.html`