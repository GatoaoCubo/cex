---
id: p01_kc_tailwind_patterns
kind: knowledge_card
pillar: P01
title: Tailwind CSS — Patterns Operacionais
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: shaka_research
domain: css-framework
quality: 9.0
tags: [knowledge_card, tailwind, css, responsive, dark-mode, utility-first, N02]
tldr: Patterns operacionais do Tailwind CSS — utility-first, breakpoints responsive, dark mode, customizacao de config, componentes puros, @apply vs inline, CDN vs build, group/peer modifiers e container queries.
when_to_use: Carregar antes de qualquer tarefa de styling com Tailwind. Referencia para breakpoints, dark mode, config customizada e padroes de componente sem libs externas.
keywords: [tailwind, utility-first, responsive, dark-mode, breakpoints, config, apply-directive, group, peer, container-queries, CDN, PostCSS]
long_tails:
  - Quando usar @apply vs classes inline no Tailwind
  - Como configurar dark mode class-based no Tailwind v4
  - Como criar um card responsivo so com Tailwind sem componentes externos
  - Diferenca entre CDN e build do Tailwind — quando usar cada
  - Como usar group e peer modifiers no Tailwind
axioms:
  - SEMPRE usar mobile-first — estilos base para mobile, prefixos para telas maiores
  - NUNCA usar @apply para criar abstractions genericas — apenas para classes com 5+ utilidades repetidas
  - SEMPRE preferir build (PostCSS/Vite) sobre CDN em producao — CDN inclui todas as classes (~3MB)
  - NUNCA misturar logica de layout e cor na mesma classe arbitraria — separar concerns
linked_artifacts:
  primary: p01_kc_shadcn_radix_patterns
  related: [p02_agent_marketing_nucleus]
density_score: 0.91
data_source: tailwind_docs_2026
---

# Tailwind CSS — Patterns Operacionais

## 1. Filosofia Utility-First

Tailwind substitui CSS customizado por classes atomicas diretamente no HTML/JSX:

```html
<!-- Tradicional: cria classe, vai pro CSS, define propriedades -->
<div class="chat-card">...</div>

<!-- Tailwind: aplica diretamente, sem sair do HTML -->
<div class="mx-auto flex max-w-sm items-center gap-x-4 rounded-xl bg-white p-6 shadow-lg">
  ...
</div>
```

**Vantagens chave:**
| Beneficio | Explicacao |
|----------|-----------|
| Velocidade | Sem naming, sem alternancia HTML/CSS |
| Seguranca | Mudanca em uma classe afeta so aquele elemento |
| CSS nao cresce | CSS resultante e pequeno e constante |
| Portabilidade | Copiar componente = copiar todo o estilo |
| Design system | Valores predefinidos evitam "magic numbers" |

**Resolucao de conflitos:** Quando duas classes afetam a mesma propriedade, a ultima no stylesheet vence (nao a ordem no HTML). Use `tailwind-merge` (cn()) para garantir comportamento previsivel.

---

## 2. Utilities Mais Usadas

### Layout
```html
<!-- Flexbox -->
<div class="flex items-center justify-between gap-4">
<div class="flex flex-col gap-2">
<div class="flex-1 min-w-0">                <!-- flex item que encolhe -->

<!-- Grid -->
<div class="grid grid-cols-3 gap-6">
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
<div class="col-span-2">                    <!-- ocupa 2 colunas -->

<!-- Posicionamento -->
<div class="relative">
  <div class="absolute top-0 right-0">     <!-- badge no canto -->
<div class="fixed inset-0 bg-black/50">   <!-- overlay fullscreen -->
<div class="sticky top-0 z-50">           <!-- navbar sticky -->
```

### Spacing (margin/padding)
```html
<!-- Escala: 1=4px, 2=8px, 4=16px, 6=24px, 8=32px, 12=48px, 16=64px -->
<div class="p-4">          <!-- padding 16px todos os lados -->
<div class="px-6 py-3">   <!-- horizontal 24px, vertical 12px -->
<div class="mt-8 mb-4">   <!-- margin top 32px, bottom 16px -->
<div class="mx-auto">     <!-- centralizar horizontalmente -->
<div class="space-y-4">   <!-- gap entre filhos diretos verticais -->
```

### Sizing
```html
<div class="w-full">           <!-- 100% -->
<div class="w-1/2">            <!-- 50% -->
<div class="w-[350px]">        <!-- valor arbitrario -->
<div class="max-w-sm">         <!-- max 384px -->
<div class="max-w-7xl mx-auto"> <!-- container padrao -->
<div class="h-screen">         <!-- 100vh -->
<div class="min-h-screen">     <!-- minimo 100vh -->
<img class="size-12">          <!-- width e height 48px simultaneos -->
```

### Tipografia
```html
<h1 class="text-4xl font-bold tracking-tight">     <!-- heading grande -->
<h2 class="text-2xl font-semibold">
<p class="text-base text-gray-600 leading-relaxed"> <!-- body text -->
<span class="text-sm text-muted-foreground">        <!-- label secundario -->
<p class="text-lg font-medium">                     <!-- destaque -->
<code class="font-mono text-sm">                    <!-- codigo -->
<p class="truncate">                               <!-- overflow ellipsis -->
<p class="line-clamp-2">                           <!-- max 2 linhas -->
```

### Cores e Bordas
```html
<div class="bg-white dark:bg-gray-900">
<div class="bg-blue-500 hover:bg-blue-600">
<div class="bg-blue-500/50">                    <!-- 50% opacity -->
<div class="border border-gray-200 rounded-lg">
<div class="rounded-full">                      <!-- circulo -->
<div class="shadow-sm">                         <!-- sombra leve -->
<div class="shadow-lg">                         <!-- sombra marcada -->
<div class="ring-2 ring-blue-500">              <!-- outline sem layout shift -->
```

---

## 3. Responsive Prefixes (Mobile-First)

| Prefix | Min Width | Pixels | Uso Tipico |
|--------|-----------|--------|-----------|
| (none) | 0 | — | Mobile base |
| `sm:` | 40rem | 640px | Tablet pequeno |
| `md:` | 48rem | 768px | Tablet |
| `lg:` | 64rem | 1024px | Desktop |
| `xl:` | 80rem | 1280px | Desktop largo |
| `2xl:` | 96rem | 1536px | Ultrawide |

```html
<!-- Layout responsivo: stack no mobile, grid no desktop -->
<div class="flex flex-col md:flex-row gap-6">
  <aside class="w-full md:w-64 shrink-0">Sidebar</aside>
  <main class="flex-1 min-w-0">Conteudo</main>
</div>

<!-- Tipografia responsiva -->
<h1 class="text-2xl sm:text-4xl lg:text-6xl font-bold">

<!-- Grid responsivo -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">

<!-- Ocultar em mobile, mostrar em desktop -->
<nav class="hidden md:flex items-center gap-4">

<!-- Mostrar em mobile, ocultar em desktop -->
<button class="md:hidden">Menu</button>
```

**Targeting ranges (max-*):**
```html
<!-- Aplica SOMENTE entre md e lg -->
<div class="md:max-lg:text-center">

<!-- Aplica apenas em mobile -->
<div class="max-sm:hidden">
```

**Breakpoints customizados:**
```css
@import "tailwindcss";
@theme {
  --breakpoint-xs: 30rem;    /* 480px */
  --breakpoint-3xl: 120rem;  /* 1920px */
}
```

---

## 4. Dark Mode

### Estrategia 1: Media Query (padrao)
Responde automaticamente ao sistema operacional:
```html
<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
```

### Estrategia 2: Class-Based (recomendado para apps)
Permite toggle manual pelo usuario:
```css
/* tailwind.config ou globals.css (v4) */
@import "tailwindcss";
@custom-variant dark (&:where(.dark, .dark *));
```
```html
<html class="dark">  <!-- JS adiciona/remove esta classe -->
```

```javascript
// Toggle theme com persistencia
function toggleTheme() {
  const isDark = document.documentElement.classList.toggle("dark")
  localStorage.theme = isDark ? "dark" : "light"
}

// Restaurar na carga (no <head>, antes do body)
const theme = localStorage.theme
const systemDark = window.matchMedia("(prefers-color-scheme: dark)").matches
if (theme === "dark" || (!theme && systemDark)) {
  document.documentElement.classList.add("dark")
}
```

### Estrategia 3: Data Attribute
```css
@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));
```
```html
<html data-theme="dark">
```

**Patterns dark mode em componentes:**
```html
<!-- Cartao -->
<div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg p-4">
  <h3 class="text-gray-900 dark:text-white font-semibold">Titulo</h3>
  <p class="text-gray-500 dark:text-gray-400 text-sm">Descricao</p>
</div>

<!-- Input -->
<input class="bg-white dark:bg-gray-900 border border-gray-300 dark:border-gray-600
              text-gray-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500
              focus:ring-2 focus:ring-blue-500 rounded-md px-3 py-2" />
```

---

## 5. Custom Config — Cores, Spacing, Fonts, Border Radius

### Cores customizadas
```css
@import "tailwindcss";
@theme {
  /* Adicionar novas cores */
  --color-brand: #0f172a;
  --color-brand-light: #1e293b;
  --color-accent: #3b82f6;

  /* Sobrescrever cor existente */
  --color-blue-500: oklch(55% 0.25 250);

  /* Remover cor que nao usa */
  --color-lime-*: initial;
}
```

### Spacing customizado
```css
@theme {
  --spacing-18: 4.5rem;   /* gap-18, p-18, etc. */
  --spacing-128: 32rem;   /* max-w-128 */
}
```

### Fonts
```css
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap");

@theme {
  --font-sans: "Inter", ui-sans-serif, system-ui, sans-serif;
  --font-heading: "Cal Sans", "Inter", sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;
}
```

### Border Radius
```css
@theme {
  /* Sobrescrever escala de radius */
  --radius: 0.5rem;     /* base — rounded-md */
  --radius-sm: 0.25rem; /* rounded-sm */
  --radius-lg: 0.75rem; /* rounded-lg */
  --radius-xl: 1rem;    /* rounded-xl */
  --radius-full: 9999px; /* rounded-full */
}
```

---

## 6. Componentes em Tailwind Puro

### Card
```html
<div class="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700
            shadow-sm overflow-hidden hover:shadow-md transition-shadow">
  <img src="/img.jpg" class="w-full h-48 object-cover" />
  <div class="p-5">
    <span class="text-xs font-medium text-blue-600 uppercase tracking-wide">Categoria</span>
    <h3 class="mt-1 text-lg font-semibold text-gray-900 dark:text-white">Titulo do Card</h3>
    <p class="mt-2 text-sm text-gray-500 dark:text-gray-400 line-clamp-2">
      Descricao do conteudo com maximo de duas linhas de texto visivel.
    </p>
    <button class="mt-4 w-full bg-blue-500 hover:bg-blue-600 text-white font-medium
                   py-2 px-4 rounded-lg transition-colors">
      Acao principal
    </button>
  </div>
</div>
```

### Navbar
```html
<nav class="bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800 sticky top-0 z-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <a href="/" class="font-bold text-xl text-gray-900 dark:text-white">Logo</a>
      <div class="hidden md:flex items-center gap-8">
        <a href="/produtos" class="text-gray-600 dark:text-gray-300 hover:text-gray-900
                                   dark:hover:text-white text-sm font-medium transition-colors">
          Produtos
        </a>
        <a href="/precos" class="text-gray-600 dark:text-gray-300 hover:text-gray-900
                                  dark:hover:text-white text-sm font-medium transition-colors">
          Precos
        </a>
      </div>
      <div class="flex items-center gap-3">
        <button class="text-sm font-medium text-gray-600 dark:text-gray-300
                       hover:text-gray-900 dark:hover:text-white transition-colors">
          Entrar
        </button>
        <button class="bg-blue-500 hover:bg-blue-600 text-white text-sm font-medium
                       px-4 py-2 rounded-lg transition-colors">
          Comecar
        </button>
      </div>
    </div>
  </div>
</nav>
```

### Hero
```html
<section class="py-20 sm:py-32 px-4">
  <div class="max-w-4xl mx-auto text-center">
    <span class="inline-block bg-blue-50 dark:bg-blue-900/30 text-blue-600 dark:text-blue-400
                 text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wide mb-4">
      Novidade
    </span>
    <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 dark:text-white
               tracking-tight leading-tight">
      Titulo principal<br class="hidden sm:block" />
      <span class="text-blue-500">com destaque</span>
    </h1>
    <p class="mt-6 text-lg sm:text-xl text-gray-500 dark:text-gray-400 max-w-2xl mx-auto leading-relaxed">
      Subtitulo com proposta de valor clara. Beneficio direto e especifico para o leitor.
    </p>
    <div class="mt-10 flex flex-col sm:flex-row gap-4 justify-center">
      <button class="bg-blue-500 hover:bg-blue-600 text-white font-semibold
                     px-8 py-3 rounded-lg text-base transition-colors">
        Comecar gratis
      </button>
      <button class="border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300
                     hover:bg-gray-50 dark:hover:bg-gray-800 font-semibold
                     px-8 py-3 rounded-lg text-base transition-colors">
        Ver demo
      </button>
    </div>
  </div>
</section>
```

### Footer
```html
<footer class="bg-gray-900 text-gray-400 py-12 px-4">
  <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8">
    <div>
      <h3 class="text-white font-bold text-lg mb-3">Logo</h3>
      <p class="text-sm leading-relaxed">Descricao curta da empresa em 2 linhas.</p>
    </div>
    <div>
      <h4 class="text-white font-semibold mb-3">Produto</h4>
      <ul class="space-y-2 text-sm">
        <li><a href="#" class="hover:text-white transition-colors">Features</a></li>
        <li><a href="#" class="hover:text-white transition-colors">Precos</a></li>
      </ul>
    </div>
    <div>
      <h4 class="text-white font-semibold mb-3">Empresa</h4>
      <ul class="space-y-2 text-sm">
        <li><a href="#" class="hover:text-white transition-colors">Sobre</a></li>
        <li><a href="#" class="hover:text-white transition-colors">Blog</a></li>
      </ul>
    </div>
    <div>
      <h4 class="text-white font-semibold mb-3">Suporte</h4>
      <ul class="space-y-2 text-sm">
        <li><a href="#" class="hover:text-white transition-colors">Docs</a></li>
        <li><a href="#" class="hover:text-white transition-colors">Contato</a></li>
      </ul>
    </div>
  </div>
  <div class="max-w-7xl mx-auto mt-8 pt-8 border-t border-gray-800 text-sm text-center">
    © 2026 Empresa. Todos os direitos reservados.
  </div>
</footer>
```

### Form
```html
<form class="space-y-6 max-w-md mx-auto">
  <div>
    <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
      Email
    </label>
    <input type="email"
           class="w-full px-3 py-2 rounded-lg border border-gray-300 dark:border-gray-600
                  bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100
                  placeholder-gray-400 dark:placeholder-gray-500
                  focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent
                  transition-colors" />
  </div>
  <div>
    <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
      Senha
    </label>
    <input type="password"
           class="w-full px-3 py-2 rounded-lg border border-gray-300 dark:border-gray-600
                  bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100
                  focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent
                  transition-colors" />
  </div>
  <button type="submit"
          class="w-full bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300
                 text-white font-semibold py-2.5 rounded-lg transition-colors">
    Entrar
  </button>
</form>
```

---

## 7. @apply vs Inline — Quando Usar Cada

| Criterio | @apply | Classes inline |
|---------|--------|---------------|
| Padrao Tailwind | Evitar | **Preferir sempre** |
| Quando usar | Classe repetida 5+ vezes, sem componente JS | Qualquer situacao normal |
| Vantagem | Extracao de pattern legivel em CSS | Colocalizacao — estilo junto da marcacao |
| Desvantagem | Quebra tree-shaking, dificulta leitura contextual | Verbose em elementos muito estilizados |
| Bom exemplo | `.btn-primary` em site estatico sem framework | Componente React/Vue reutilizavel |
| Mau exemplo | `.flex` — abstraction de 1 utilidade so | 15+ classes identicas repetidas 30x sem componente |

```css
/* Uso correto de @apply — padrao com 5+ classes, sem componente JS */
@layer components {
  .badge {
    @apply inline-flex items-center rounded-full px-2.5 py-0.5
           text-xs font-semibold border;
  }
  .badge-success {
    @apply badge bg-green-100 text-green-800 border-green-200
           dark:bg-green-900/30 dark:text-green-400 dark:border-green-800;
  }
}
```

---

## 8. Tailwind CDN vs Build

| Criterio | CDN | Build (PostCSS/Vite/Next) |
|---------|-----|--------------------------|
| Setup | 1 linha no `<head>` | npm install + config |
| Bundle size | ~3MB (todas as classes) | ~5-20KB (so classes usadas) |
| Performance | Lento (parse 3MB) | Rapido |
| Customizacao | Limitada (sem config) | Total (@theme, plugins) |
| Quando usar | Prototipos, demos rapidos, email HTML | **Qualquer projeto real** |
| Arbitrary values | Sim | Sim |
| Plugins (typography, forms) | Nao | Sim |

```html
<!-- CDN (apenas prototipo) -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- Config inline no CDN (limitado) -->
<script>
  tailwind.config = {
    theme: { extend: { colors: { brand: "#0f172a" } } }
  }
</script>
```

```js
// Build com Vite/Next — tailwind.config.js (v3) ou CSS v4
// v3: module.exports = { content: ["./src/**/*.{tsx,ts,jsx,js}"], theme: { extend: {} } }
// v4: so @import "tailwindcss" + @theme no CSS
```

---

## 9. Group, Peer Modifiers e Container Queries

### group — estilizar filho baseado no estado do pai
```html
<a href="#" class="group flex items-center gap-3 p-4 rounded-lg hover:bg-blue-50
                   dark:hover:bg-blue-900/20 transition-colors">
  <div class="p-2 rounded-full bg-gray-100 group-hover:bg-blue-100 transition-colors">
    <svg class="w-5 h-5 text-gray-500 group-hover:text-blue-500 transition-colors" .../>
  </div>
  <div>
    <p class="font-medium text-gray-900 dark:text-white group-hover:text-blue-600 transition-colors">
      Item do menu
    </p>
    <p class="text-sm text-gray-500 group-hover:text-blue-400 transition-colors">
      Descricao secundaria
    </p>
  </div>
  <svg class="ml-auto w-4 h-4 text-gray-400 group-hover:text-blue-500
              group-hover:translate-x-1 transition-all" .../>
</a>
```

### peer — estilizar irmao baseado no estado do elemento
```html
<!-- Mostrar mensagem de erro quando input e invalido -->
<input type="email" class="peer border rounded-lg px-3 py-2
                            invalid:border-red-500 focus:outline-none" />
<p class="mt-1 text-sm text-red-500 hidden peer-invalid:block">
  Email invalido
</p>

<!-- Label que sobe quando input tem foco (floating label) -->
<div class="relative">
  <input class="peer w-full border-b-2 border-gray-300 focus:border-blue-500
                bg-transparent py-2 placeholder-transparent focus:outline-none" />
  <label class="absolute left-0 -top-3.5 text-sm text-gray-500
                peer-placeholder-shown:text-base peer-placeholder-shown:top-2 peer-placeholder-shown:text-gray-400
                peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-blue-500 transition-all">
    Email
  </label>
</div>
```

### Container Queries — estilo baseado no container, nao viewport
```html
<!-- Instalar: @tailwindcss/container-queries -->
<div class="@container">
  <!-- Layout muda baseado no tamanho do container, nao da janela -->
  <div class="flex flex-col @md:flex-row gap-4">
    <img class="w-full @md:w-48 @md:shrink-0 rounded-lg object-cover" src="..." />
    <div>
      <h3 class="font-semibold @lg:text-xl">Titulo</h3>
      <p class="text-sm text-gray-500 @lg:text-base">Descricao</p>
    </div>
  </div>
</div>
```

| Breakpoint Container | Tamanho |
|---------------------|---------|
| `@3xs` | 256px |
| `@2xs` | 288px |
| `@xs` | 320px |
| `@sm` | 384px |
| `@md` | 448px |
| `@lg` | 512px |
| `@xl` | 576px |
| `@2xl` | 672px |
| `@3xl` | 768px |
| `@4xl` | 896px |
| `@5xl` | 1024px |
| `@6xl` | 1152px |
| `@7xl` | 1280px |
