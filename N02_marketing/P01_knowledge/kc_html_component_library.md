---
id: n02_kc_html_component_library
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "shadcn/ui & Radix UI Component Library"
version: 1.0.0
created: 2026-04-01
author: builder
domain: frontend
quality: 9.1
tags: [knowledge, frontend, components, radix, shadcn]
tldr: "shadcn/ui built on Radix primitives: unstyled components, variants, accessibility patterns"
density_score: 0.88
related:
  - p01_kc_html_component_library
  - p01_kc_shadcn_radix_patterns
  - n02_kc_shadcn_radix_patterns
  - spec_n02_visual_frontend_engineer
  - p01_kc_accessibility_a11y
  - p09_ct_component_template
  - p10_hos_html_output_visual_frontend
  - n02_kc_accessibility_a11y
  - p10_out_knowledge_card
---

# shadcn/ui & Radix UI Component Library

## Philosophy: Composition Over Configuration

**shadcn/ui**: Copy-paste components built on Radix UI primitives + Tailwind CSS + class-variance-authority (cva).

**Radix UI**: Unstyled, accessible UI primitives with proper focus management, keyboard navigation, and ARIA attributes.

## Class Variance Authority (cva) Patterns

```tsx
import { cva, type VariantProps } from "class-variance-authority"

const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline: "border border-input hover:bg-accent hover:text-accent-foreground",
        ghost: "hover:bg-accent hover:text-accent-foreground"
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10"
      }
    },
    defaultVariants: {
      variant: "default",
      size: "default"
    }
  }
)
```

## Core Radix Primitives

### Dialog System

```tsx
import * as Dialog from "@radix-ui/react-dialog"

<Dialog.Root>
  <Dialog.Trigger asChild>
    <button>Open Dialog</button>
  </Dialog.Trigger>
  
  <Dialog.Portal>
    <Dialog.Overlay className="fixed inset-0 bg-black/50" />
    <Dialog.Content className="fixed top-[50%] left-[50%] translate-x-[-50%] translate-y-[-50%] bg-white rounded-lg p-6">
      <Dialog.Title>Dialog Title</Dialog.Title>
      <Dialog.Description>Dialog content here</Dialog.Description>
      <Dialog.Close asChild>
        <button>Close</button>
      </Dialog.Close>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Dropdown Menu

```tsx
import * as DropdownMenu from "@radix-ui/react-dropdown-menu"

<DropdownMenu.Root>
  <DropdownMenu.Trigger asChild>
    <button>Options</button>
  </DropdownMenu.Trigger>
  
  <DropdownMenu.Portal>
    <DropdownMenu.Content className="bg-white rounded-md shadow-lg border">
      <DropdownMenu.Item className="px-3 py-2 hover:bg-gray-100">
        Profile
      </DropdownMenu.Item>
      <DropdownMenu.Separator className="h-px bg-gray-200" />
      <DropdownMenu.Item className="px-3 py-2 hover:bg-gray-100">
        Sign out
      </DropdownMenu.Item>
    </DropdownMenu.Content>
  </DropdownMenu.Portal>
</DropdownMenu.Root>
```

## Complete Radix Package List

### Navigation & Layout
- `@radix-ui/react-navigation-menu` - Complex navigation menus
- `@radix-ui/react-menubar` - Horizontal menu bar
- `@radix-ui/react-context-menu` - Right-click context menus
- `@radix-ui/react-tabs` - Tab panels
- `@radix-ui/react-accordion` - Expandable content sections
- `@radix-ui/react-collapsible` - Show/hide content
- `@radix-ui/react-separator` - Visual dividers
- `@radix-ui/react-scroll-area` - Custom scrollable areas

### Form Controls
- `@radix-ui/react-select` - Custom select dropdowns
- `@radix-ui/react-checkbox` - Enhanced checkboxes
- `@radix-ui/react-radio-group` - Radio button groups
- `@radix-ui/react-switch` - Toggle switches
- `@radix-ui/react-slider` - Range sliders
- `@radix-ui/react-label` - Enhanced labels
- `@radix-ui/react-toggle` - Toggle buttons
- `@radix-ui/react-toggle-group` - Grouped toggles

### Overlays & Feedback
- `@radix-ui/react-dialog` - Modal dialogs
- `@radix-ui/react-alert-dialog` - Confirmation dialogs
- `@radix-ui/react-popover` - Floating content
- `@radix-ui/react-tooltip` - Hover tooltips
- `@radix-ui/react-hover-card` - Rich hover previews
- `@radix-ui/react-toast` - Notification toasts

### Display & Media
- `@radix-ui/react-avatar` - Profile pictures with fallbacks
- `@radix-ui/react-aspect-ratio` - Responsive aspect ratios
- `@radix-ui/react-progress` - Progress indicators

## Data-State Styling Pattern

```css
/* Radix components expose state via data attributes */
[data-state="open"] {
  animation: slideDown 0.2s ease-out;
}

[data-state="closed"] {
  animation: slideUp 0.2s ease-in;
}

[data-disabled] {
  opacity: 0.5;
  pointer-events: none;
}

[data-highlighted] {
  background-color: rgba(0, 0, 0, 0.05);
}
```

## Portal Rendering & Focus Management

```tsx
// Portals render outside normal DOM hierarchy
<Dialog.Portal container={document.getElementById('modal-root')}>
  <Dialog.Content>
    {/* Focus is trapped here when open */}
    <input autoFocus />
  </Dialog.Content>
</Dialog.Portal>

// Focus returns to trigger when closed
// Escape key closes automatically
// Click outside closes (configurable)
```

## Anti-Patterns

| Don't Do | Why | Do Instead |
|----------|-----|------------|
| Mix Radix with Material-UI/Chakra | Style conflicts, bundle bloat | Stick to one system |
| Style Radix primitives directly | Loses unstyled benefits | Use shadcn/ui or custom wrapper |
| Forget `asChild` prop | Breaks composition, creates extra DOM | Always use `asChild` for triggers |
| Override focus management | Breaks accessibility | Trust Radix defaults |
| Use Radix for simple cases | Overkill for basic buttons | Use plain HTML/CSS first |

## shadcn/ui Installation & Usage

```bash
# Initialize shadcn/ui in project
npx shadcn-ui@latest init

# Add specific components
npx shadcn-ui@latest add button
npx shadcn-ui@latest add dialog
npx shadcn-ui@latest add dropdown-menu
```

```tsx
// Components are copied to your codebase, fully customizable
import { Button } from "@/components/ui/button"
import { Dialog, DialogContent, DialogTrigger } from "@/components/ui/dialog"

<Dialog>
  <DialogTrigger asChild>
    <Button variant="outline">Open</Button>
  </DialogTrigger>
  <DialogContent>
    Content here
  </DialogContent>
</Dialog>
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_html_component_library]] | sibling | 0.94 |
| [[p01_kc_shadcn_radix_patterns]] | sibling | 0.64 |
| [[n02_kc_shadcn_radix_patterns]] | sibling | 0.60 |
| [[spec_n02_visual_frontend_engineer]] | downstream | 0.22 |
| [[p01_kc_accessibility_a11y]] | sibling | 0.18 |
| [[p09_ct_component_template]] | downstream | 0.17 |
| [[p10_hos_html_output_visual_frontend]] | downstream | 0.17 |
| [[n02_kc_accessibility_a11y]] | sibling | 0.16 |
| [[p10_out_knowledge_card]] | downstream | 0.15 |
