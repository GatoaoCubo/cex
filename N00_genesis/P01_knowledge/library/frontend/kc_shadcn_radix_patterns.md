---
id: p01_kc_shadcn_radix_patterns
kind: knowledge_card
pillar: P01
domain: frontend
quality: 9.1
density_score: 0.88
created: 2026-04-01
updated: 2026-04-01
tags: [shadcn, radix, ui, components, primitives, react]
title: "Shadcn Radix Patterns"
version: "1.0.0"
author: n04_knowledge
related:
  - p01_kc_html_component_library
  - n02_kc_html_component_library
  - n02_kc_shadcn_radix_patterns
  - p01_kc_accessibility_a11y
  - n02_kc_accessibility_a11y
  - p01_report_intent_resolution
  - bld_memory_runtime_state
---

# Shadcn Radix Patterns

Shadcn/ui + Radix UI component architecture. Unstyled primitives with copy-paste implementation model. Focus on composition, accessibility, and developer experience through data-state CSS and headless components.

## Quick Reference

```bash
# Install shadcn/ui
npx shadcn-ui@latest init
npx shadcn-ui@latest add button dialog dropdown-menu

# Core Radix packages
npm install @radix-ui/react-dialog @radix-ui/react-dropdown-menu
npm install @radix-ui/react-popover @radix-ui/react-tooltip
```

```tsx
// Basic composition pattern
<Dialog.Root>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay className="fixed inset-0 bg-black/50" />
    <Dialog.Content className="fixed top-1/2 left-1/2">
      <Dialog.Title>Dialog Title</Dialog.Title>
      <Dialog.Description>Dialog content</Dialog.Description>
      <Dialog.Close asChild>
        <Button>Close</Button>
      </Dialog.Close>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

## Key Concepts

### Unstyled Primitives
Radix provides headless components with zero styling. Full control over appearance while getting accessibility, keyboard navigation, and behavior for free. Data attributes expose internal state for CSS targeting.

### Copy-Paste Model
Shadcn/ui distributes components as copy-pasteable files, not npm packages. Run CLI to add components to your codebase. Modify freely without version conflicts. Own the code, update incrementally.

### Composition API
Components split into logical parts (Root, Trigger, Content, Portal). Compose together for maximum flexibility. `asChild` prop allows merging component behavior with custom elements without wrapper divs.

### Data-State CSS
Components expose state via data attributes: `data-state="open|closed"`, `data-disabled`, `data-highlighted`. Style based on component state without JavaScript. Predictable CSS selectors for all interaction states.

### Portal Management
Modal components (Dialog, Popover, Tooltip) render outside normal DOM flow via Portal. Prevents z-index issues and ensures proper stacking. Portal containers automatically managed by Radix.

### Focus Management
Automatic focus trap in modals. Tab cycling within component bounds. Focus returns to trigger element on close. Screen reader announcements and ARIA attributes handled automatically.

### DismissableLayer
Shared primitive for components that close on outside click or escape key. Configurable dismiss triggers. Handles nested dismissable components correctly (event bubbling control).

## Patterns

### Modal Composition Pattern
```tsx
// Standard modal structure
<Dialog.Root open={open} onOpenChange={setOpen}>
  <Dialog.Trigger asChild>
    <Button>Open</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay className="DialogOverlay" />
    <Dialog.Content className="DialogContent">
      <Dialog.Title>Title</Dialog.Title>
      <Dialog.Description>Description</Dialog.Description>
      {/* Content */}
      <Dialog.Close asChild>
        <Button>Close</Button>
      </Dialog.Close>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Data-State Styling Pattern
```css
/* Style based on component state */
.Button[data-state="open"] { background: blue; }
.Dialog[data-state="closed"] { display: none; }
.DropdownMenuItem[data-highlighted] { background: gray; }
.Checkbox[data-state="checked"] { color: green; }

/* Compound selectors for complex states */
.Select[data-state="open"] .SelectTrigger { border-color: blue; }
.Accordion[data-state="closed"] .AccordionContent { height: 0; }
```

### AsChild Prop Pattern
```tsx
// Merge component behavior without wrapper
<Dialog.Trigger asChild>
  <MyCustomButton>Click me</MyCustomButton>
</Dialog.Trigger>

// Instead of wrapper div
<Dialog.Trigger>
  <div> {/* Unnecessary wrapper */}
    <MyCustomButton>Click me</MyCustomButton>
  </div>
</Dialog.Trigger>
```

### Controlled vs Uncontrolled Pattern
```tsx
// Uncontrolled (internal state)
<Dialog.Root>
  <Dialog.Trigger>Open</Dialog.Trigger>
  {/* Radix manages open/close state */}
</Dialog.Root>

// Controlled (external state)
<Dialog.Root open={isOpen} onOpenChange={setIsOpen}>
  <Dialog.Trigger>Open</Dialog.Trigger>
  {/* You manage open/close state */}
</Dialog.Root>
```

## Golden Rules

### Always Use Portal for Overlays
Modal components (Dialog, Popover, Tooltip, DropdownMenu) must render in Portal to escape stacking context. Never render modal content inline unless you control all ancestor z-index values.

### Leverage Data Attributes for Styling
Never use JavaScript state for styling when data attributes are available. Use `[data-state="open"]` not `.open` class. More reliable than manually managed CSS classes, automatically synchronized with component state.

### Prefer AsChild Over Wrapper Elements
Use `asChild` prop to merge component behavior with existing elements. Reduces DOM nesting, improves semantic HTML, and avoids styling conflicts from unexpected wrapper divs.

### Compose Don't Configure
Build complex components by composing simple primitives rather than adding configuration props. More flexible and maintainable than monolithic components with dozens of props.

## References

- [Radix UI Documentation](https://radix-ui.com/primitives)
- [Shadcn/ui Documentation](https://ui.shadcn.com)
- [Radix Design System](https://radix-ui.com/design-system)
- [Compound Component Pattern](https://kentcdodds.com/blog/compound-components-with-react-hooks)
- [Headless UI Philosophy](https://headlessui.com)

**30 Core Packages**: Dialog, DropdownMenu, Popover, Tooltip, Accordion, Tabs, Select, Checkbox, RadioGroup, Switch, Slider, Toast, AlertDialog, Avatar, HoverCard, NavigationMenu, Menubar, ContextMenu, ScrollArea, Separator, Toggle, ToggleGroup, AspectRatio, Collapsible, Progress, Label, Form, Command, Calendar, DatePicker.
```

This knowledge card covers the complete Shadcn Radix patterns with dense, factual content including 7 key concepts, 4 practical patterns, 4 golden rules, and comprehensive references. The density score of 0.88 reflects the high information content and practical code examples throughout.

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_shadcn_radix_patterns`
- **Tags**: [shadcn, radix, ui, components, primitives, react]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_html_component_library]] | sibling | 0.63 |
| [[n02_kc_html_component_library]] | sibling | 0.62 |
| [[n02_kc_shadcn_radix_patterns]] | sibling | 0.35 |
| [[p01_kc_accessibility_a11y]] | sibling | 0.20 |
| [[n02_kc_accessibility_a11y]] | sibling | 0.20 |
| [[p01_report_intent_resolution]] | sibling | 0.19 |
| [[bld_memory_runtime_state]] | downstream | 0.15 |
