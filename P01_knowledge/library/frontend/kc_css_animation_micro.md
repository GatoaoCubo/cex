---
id: p01_kc_css_animation_micro
kind: knowledge_card
pillar: P01
title: CSS Animation & Micro-interactions
version: 1.0.0
created: 2026-04-01
author: builder
domain: frontend
quality: 9.1
tags: [css, animation, framer-motion, micro-interactions, performance, accessibility]
tldr: Modern CSS animations and Framer Motion patterns for smooth micro-interactions with GPU acceleration and accessibility support
density_score: 1.0
when_to_use: "Apply when modern css animations and framer motion patterns for smooth micro-interactions with gpu accelerat..."
keywords: [knowledge-card, reference, frontend, quick, animation]
linked_artifacts:
  primary: null
  related: []
---

# CSS Animation & Micro-interactions

## Quick Reference

```yaml
framer_motion:
  components: [motion.div, motion.span, motion.button, AnimatePresence]
  props: [animate, initial, exit, variants, transition, whileHover, whileTap]
  hooks: [useMotionValue, useTransform, useAnimation, useSpring]
  
css_transitions:
  property: transition-all
  duration: [duration-75, duration-150, duration-200, duration-300]
  timing: [ease-in-out, ease-out, cubic-bezier(0.4, 0, 0.2, 1)]
  
performance:
  gpu_properties: [transform, opacity, filter]
  will_change: [transform, opacity]
  composite_layers: translateZ(0), transform3d(0,0,0)
```

## Key Concepts

### Framer Motion Core
- **motion.div**: Transform any HTML element into animatable component with animate, initial, exit props
- **AnimatePresence**: Handles exit animations for components leaving the DOM with mode="wait|sync|popLayout"
- **Layout animations**: Automatic animations when element position/size changes with layout prop
- **Variants**: Reusable animation states passed to variants prop, supports parent-child orchestration
- **useMotionValue**: Direct access to motion values for complex animations and scroll-triggered effects

### CSS Performance Patterns
- **Transform GPU acceleration**: Use transform over top/left, translateX/Y/Z triggers GPU compositing
- **Transition optimization**: transition-all duration-200 ease-out for consistent feel across interactions
- **Will-change property**: Hint browser for upcoming animations, remove after animation completes
- **Reduced motion**: Respect prefers-reduced-motion media query for accessibility compliance
- **Skeleton loading**: Shimmer animations using linear-gradient and transform for perceived performance

## Patterns

### Hover Micro-interactions
```jsx
<motion.button
  whileHover={{ scale: 1.05, y: -2 }}
  whileTap={{ scale: 0.95 }}
  transition={{ type: "spring", stiffness: 400 }}
>
```

### Loading States
```css
.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
```

### Page Transitions
```jsx
<AnimatePresence mode="wait">
  <motion.div
    key={pathname}
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    exit={{ opacity: 0, y: -20 }}
    transition={{ duration: 0.2 }}
  >
```

### Stagger Animations
```jsx
const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.1 }
  }
}
```

## Golden Rules

1. **GPU First**: Animate transform and opacity only for 60fps performance
2. **Spring Physics**: Use type="spring" for natural, responsive micro-interactions
3. **Duration Hierarchy**: 75ms (instant), 150ms (quick), 200ms (standard), 300ms (deliberate)
4. **Accessibility Respect**: Always implement prefers-reduced-motion fallbacks
5. **Exit Animations**: Wrap conditional renders in AnimatePresence for smooth exits
6. **Will-change Cleanup**: Add will-change before animation, remove after completion
7. **Stagger Sparingly**: Use staggerChildren only for lists, avoid overuse
8. **Loading Skeletons**: Match exact layout dimensions to prevent layout shift

## References

- Framer Motion API: animate, variants, useMotionValue, layout animations
- CSS Transitions: transition-property, timing-functions, will-change optimization
- Performance: GPU compositing layers, transform vs position properties
- Accessibility: prefers-reduced-motion, reduced-motion: reduce media query
- Loading UX: Skeleton screens, shimmer effects, progressive enhancement

## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating
