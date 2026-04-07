---
id: n02_kc_shadcn_radix_patterns
kind: knowledge_card
pillar: P01
title: shadcn/ui + Radix Primitives — Component Patterns
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: shaka_research
domain: component-library
quality: 9.1
tags: [knowledge_card, shadcn, radix, react, components, ui, N02]
tldr: Patterns operacionais para shadcn/ui — catalogo de componentes, composicao com cn()/cva, Radix primitives, customizacao via CSS variables, e exemplos HTML prontos para hero/card/dialog/navbar.
when_to_use: Carregar antes de qualquer tarefa de build UI com shadcn. Referencia para escolha de componente, customizacao de tema e composicao de layouts.
keywords: [shadcn, radix-ui, tailwind, cn, cva, CSS variables, theming, dark-mode, copy-paste, npm, component-library]
long_tails:
  - Quando usar copy-paste vs npm install no shadcn
  - Como customizar cores e border-radius no shadcn via CSS variables
  - Como usar cva para criar variantes de componente
  - Quais Radix primitives estao por baixo de cada componente shadcn
  - Como compor hero, card, dialog e navbar com shadcn
axioms:
  - SEMPRE preferir shadcn copy-paste para componentes que precisam de customizacao profunda
  - SEMPRE usar cn() para merge de classes Tailwind (evita conflito de utilidades)
  - NUNCA sobrescrever estilos shadcn com CSS inline — usar CSS variables ou cva variants
  - SEMPRE definir tema em :root e .dark para suporte a dark mode automatico
linked_artifacts:
  primary: p01_kc_tailwind_patterns
  related: [p02_agent_marketing_nucleus]
density_score: 0.92
data_source: shadcn_docs_2026
---

# shadcn/ui + Radix Primitives — Component Patterns

## 1. Catalogo de Componentes (67 total)

### Layout & Estrutura
| Componente | Uso Recomendado |
|-----------|----------------|
| Card | Container de conteudo com header/body/footer — produto, post, stat |
| Separator | Divisor visual entre secoes (hr semantico) |
| Aspect Ratio | Wrappers de imagem/video com ratio fixo (16:9, 1:1, 4:3) |
| Accordion | FAQ, expandable sections, nested navigation |
| Collapsible | Sidebar colapsavel, filtros avancados |
| Resizable | Layouts split-pane (editor + preview) |
| Scroll Area | Scrollbars customizados cross-browser |
| Sidebar | Layout de app com sidebar composavel e themeable |

### Formularios
| Componente | Uso Recomendado |
|-----------|----------------|
| Input | Campo de texto — sempre par com Label |
| Textarea | Campos longos (bio, descricao, mensagem) |
| Select | Dropdown com poucas opcoes (<20 itens) |
| Combobox | Autocomplete/search em listas grandes |
| Input OTP | Verificacao de 2FA, codigo de convite |
| Checkbox | Multipla selecao, termos de uso |
| Switch | Toggle on/off — configuracoes, notificacoes |
| Radio Group | Selecao exclusiva (plano, tamanho, cor) |
| Slider | Range numerico (preco, volume, nivel) |
| Field | Compoe Label + Input + mensagem de erro acessivel |
| Button Group | Acoes relacionadas agrupadas (Salvar / Cancelar) |

### Dialogs & Overlays
| Componente | Uso Recomendado |
|-----------|----------------|
| Dialog | Modal generico — formularios, confirmacoes |
| Alert Dialog | Confirmacao destrutiva (deletar, sair sem salvar) |
| Sheet | Drawer lateral — detalhes, filtros, formulario mobile |
| Drawer | Drawer bottom — mobile-first, acoes contextuais |
| Popover | Rich content ao hover/click — date picker, color picker |
| Hover Card | Preview ao hover em link (perfil, produto) |
| Context Menu | Menu de botao direito |
| Dropdown Menu | Menu de acoes em botao (kebab menu, account) |
| Tooltip | Label descritivo em botoes de icone |

### Navegacao
| Componente | Uso Recomendado |
|-----------|----------------|
| Navigation Menu | Navbar horizontal com mega-menus |
| Breadcrumb | Hierarquia de paginas (Home > Categoria > Produto) |
| Tabs | Secoes alternadas na mesma pagina |
| Pagination | Navegacao em listas longas / tabelas |
| Menubar | Barra de menu estilo desktop (app editor) |
| Command | Palette de busca rapida (cmd+K) |

### Data Display
| Componente | Uso Recomendado |
|-----------|----------------|
| Table | Dados tabulares simples |
| Data Table | Tabelas com sort/filter/pagination (TanStack Table) |
| Badge | Status label, tag, contador |
| Avatar | Foto de usuario com fallback de iniciais |
| Chart | Graficos com Recharts (line, bar, pie, radar) |
| Progress | Barra de progresso (upload, onboarding) |
| Skeleton | Placeholder de loading (evita layout shift) |
| Spinner | Loading inline em botoes / acoes |
| Toast / Sonner | Feedback temporario pos-acao |
| Alert | Mensagem de atencao persistente (nao modal) |
| Empty | Estado vazio de lista/tabela |
| Item | Card flexivel com media + title + description |

### Data & Tempo
| Componente | Uso Recomendado |
|-----------|----------------|
| Calendar | Selecao de data com range |
| Date Picker | Composed de Calendar + Popover com presets |

---

## 2. Pattern de Composicao

### cn() — Class Name Merger
```tsx
import { cn } from "@/lib/utils"

// Merge condicional sem conflito de utilidades Tailwind
function Button({ className, variant, ...props }) {
  return (
    <button
      className={cn(
        "rounded-md px-4 py-2 font-medium",           // base
        variant === "destructive" && "bg-red-500",    // condicional
        className                                      // override externo
      )}
      {...props}
    />
  )
}
```
`cn()` usa `clsx` + `tailwind-merge` internamente. Resolve conflitos como `p-2 p-4` → `p-4`.

### cva — Class Variance Authority
```tsx
import { cva, type VariantProps } from "class-variance-authority"

const buttonVariants = cva(
  // base sempre aplicado
  "inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive: "bg-destructive text-white hover:bg-destructive/90",
        outline: "border border-input bg-background hover:bg-accent",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2",
        sm: "h-8 rounded-md px-3 text-xs",
        lg: "h-10 rounded-md px-8",
        icon: "h-9 w-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

// Uso
<Button variant="destructive" size="lg" />
```

---

## 3. Radix Primitives — O que estao por baixo

shadcn/ui e uma camada de estilos sobre **Radix UI** (primitives headless + acessiveis):

| shadcn Component | Radix Primitive | O que oferece |
|-----------------|-----------------|---------------|
| Dialog | `@radix-ui/react-dialog` | Focus trap, Esc close, aria-modal |
| Alert Dialog | `@radix-ui/react-alert-dialog` | Foco forcado no botao de acao |
| Select | `@radix-ui/react-select` | Keyboard nav, ARIA listbox |
| Dropdown Menu | `@radix-ui/react-dropdown-menu` | Submenus, keyboard nav |
| Tabs | `@radix-ui/react-tabs` | ARIA tabpanel, keyboard |
| Popover | `@radix-ui/react-popover` | Positioning (floating-ui), portal |
| Tooltip | `@radix-ui/react-tooltip` | Delay, portal, ARIA |
| Accordion | `@radix-ui/react-accordion` | Expand/collapse, single/multiple |
| Checkbox | `@radix-ui/react-checkbox` | Indeterminate state, ARIA |
| Switch | `@radix-ui/react-switch` | ARIA role=switch |
| Slider | `@radix-ui/react-slider` | Range, step, ARIA |
| Toggle | `@radix-ui/react-toggle` | aria-pressed |

**Como extender um primitivo:**
```tsx
import * as DialogPrimitive from "@radix-ui/react-dialog"

// Compoe novos elementos sobre o primitivo
const DialogCustomHeader = React.forwardRef(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex flex-col space-y-1.5 text-left", className)}
    {...props}
  />
))
```

---

## 4. Copy-Paste vs npm

| Criterio | Copy-Paste (shadcn add) | npm Package |
|---------|------------------------|-------------|
| Customizacao total | Sim — voce possui o codigo | Limitada — API publica |
| Updates automaticas | Nao — manual | Sim — `npm update` |
| Quando usar | UI precisa ser unica / temada | Logica reutilizavel (date-fns, clsx) |
| Overhead de bundle | Zero nao-utilizado (tree-shaking manual) | Tree-shaking automatico |
| Padrao shadcn | **Padrao para todos os componentes UI** | Dependencias (Radix, cva, etc.) |

**Regra pratica**: Componentes visuais → copy-paste. Utilitarios e logica → npm.

---

## 5. Customizacao via CSS Variables

O sistema de tema usa pares `token / token-foreground`:

```css
/* globals.css — definir tokens em :root e .dark */
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --primary: 221.2 83.2% 53.3%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96.1%;
    --secondary-foreground: 222.2 47.4% 11.2%;
    --muted: 210 40% 96.1%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --accent: 210 40% 96.1%;
    --accent-foreground: 222.2 47.4% 11.2%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 221.2 83.2% 53.3%;
    --radius: 0.5rem;
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    --primary: 217.2 91.2% 59.8%;
    --primary-foreground: 222.2 47.4% 11.2%;
    /* ... resto dos tokens */
  }
}
```

Tokens mapeiam para classes Tailwind via `tailwind.config`:
```js
colors: {
  background: "hsl(var(--background))",
  foreground: "hsl(var(--foreground))",
  primary: {
    DEFAULT: "hsl(var(--primary))",
    foreground: "hsl(var(--primary-foreground))",
  },
}
```

**Dark Mode Setup:**
```tsx
// Instalar: npm install next-themes
// providers.tsx
import { ThemeProvider } from "next-themes"

export function Providers({ children }) {
  return (
    <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
      {children}
    </ThemeProvider>
  )
}

// Botao toggle
import { useTheme } from "next-themes"
const { setTheme } = useTheme()
<button onClick={() => setTheme("dark")}>Dark</button>
```

---

## 6. HTML Output — Exemplos Prontos

### Hero Section
```tsx
<section className="py-20 px-4 text-center">
  <Badge variant="secondary" className="mb-4">Novo</Badge>
  <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-6xl">
    Titulo principal da hero
  </h1>
  <p className="mt-6 text-lg text-muted-foreground max-w-2xl mx-auto">
    Subtitulo com proposta de valor clara e beneficio principal do produto.
  </p>
  <div className="mt-10 flex gap-4 justify-center">
    <Button size="lg">Comecar agora</Button>
    <Button size="lg" variant="outline">Ver demo</Button>
  </div>
</section>
```

### Card de Produto
```tsx
<Card className="w-[350px]">
  <CardHeader>
    <img src="/product.jpg" className="rounded-md aspect-square object-cover" />
    <CardTitle className="mt-4">Nome do Produto</CardTitle>
    <CardDescription>Descricao curta do beneficio principal.</CardDescription>
  </CardHeader>
  <CardContent>
    <Badge variant="destructive">-20%</Badge>
    <span className="text-2xl font-bold ml-2">R$ 97,00</span>
    <span className="text-sm text-muted-foreground line-through ml-2">R$ 127,00</span>
  </CardContent>
  <CardFooter>
    <Button className="w-full">Adicionar ao carrinho</Button>
  </CardFooter>
</Card>
```

### Dialog de Confirmacao
```tsx
<Dialog>
  <DialogTrigger asChild>
    <Button variant="destructive">Deletar conta</Button>
  </DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Confirmar exclusao</DialogTitle>
      <DialogDescription>
        Esta acao e permanente. Todos os dados serao removidos.
      </DialogDescription>
    </DialogHeader>
    <DialogFooter>
      <Button variant="outline">Cancelar</Button>
      <Button variant="destructive" onClick={handleDelete}>Confirmar</Button>
    </DialogFooter>
  </DialogContent>
</Dialog>
```

### Navbar
```tsx
<nav className="border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
  <div className="container flex h-14 items-center justify-between">
    <a href="/" className="font-bold text-lg">Logo</a>
    <NavigationMenu>
      <NavigationMenuList>
        <NavigationMenuItem>
          <NavigationMenuLink href="/produtos">Produtos</NavigationMenuLink>
        </NavigationMenuItem>
        <NavigationMenuItem>
          <NavigationMenuLink href="/precos">Precos</NavigationMenuLink>
        </NavigationMenuItem>
      </NavigationMenuList>
    </NavigationMenu>
    <div className="flex gap-2">
      <Button variant="ghost" size="sm">Entrar</Button>
      <Button size="sm">Comecar gratis</Button>
    </div>
  </div>
</nav>
```
