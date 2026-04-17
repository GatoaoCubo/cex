---
id: n02_kc_css_animation_micro
kind: knowledge_card
pillar: P01
title: CSS Animation & Micro-interactions
domain: N02_marketing / Frontend
tags: [css, animation, transitions, framer-motion, accessibility, micro-interactions, gpu]
quality: 9.1
density_score: 1.0
source: motion.dev, joshwcomeau.com, web.dev
created: 2026-04-01
---

# KC: CSS Animation & Micro-interactions

## Core Mental Model

Animation serves communication, not decoration. Every animation should:
1. Guide attention to something meaningful
2. Provide feedback (action confirmed)
3. Establish spatial relationships (where did this element go?)
4. Always respect `prefers-reduced-motion`.

---

## CSS Transitions

### Syntax
```css
/* transition: property duration timing-function delay */
.btn {
  transition: background-color 150ms ease-out,
              transform 150ms ease-out,
              box-shadow 150ms ease-out;
}
```

### Timing Functions
```css
/* Built-in */
transition-timing-function: ease;         /* slow-fast-slow (default) */
transition-timing-function: ease-in;      /* slow start */
transition-timing-function: ease-out;     /* slow end — best for exits */
transition-timing-function: ease-in-out;  /* slow start and end */
transition-timing-function: linear;       /* constant — good for spinners */

/* Custom cubic-bezier */
transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1); /* spring bounce */
transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);      /* Material Design standard */
transition-timing-function: cubic-bezier(0, 0, 0.2, 1);         /* Material decelerate */
transition-timing-function: cubic-bezier(0.4, 0, 1, 1);         /* Material accelerate */
```

**Rule**: Entrances = ease-out (fast start). Exits = ease-in (fast end). Interactions = spring.

### Duration Guidelines
| Interaction | Duration |
|---|---|
| Hover state change | 100–150ms |
| Button press feedback | 80–120ms |
| Tooltip appear | 150–200ms |
| Modal/drawer open | 250–350ms |
| Page transitions | 300–500ms |
| Skeleton to content | 200–300ms |

---

## GPU-Accelerated Transforms

### Properties that trigger GPU compositing
```css
/* GPU-accelerated (do not cause reflow) */
transform: translateX(100px);
transform: translateY(50px);
transform: scale(1.05);
transform: rotate(45deg);
opacity: 0;

/* Force GPU layer (use sparingly) */
will-change: transform, opacity;
transform: translateZ(0);   /* hack for older browsers */
```

### NEVER animate (causes layout reflow — expensive)
```css
/* BAD: triggers layout */
transition: width 300ms;
transition: height 300ms;
transition: top 300ms;
transition: left 300ms;
transition: margin 300ms;
transition: padding 300ms;

/* GOOD: equivalent, GPU only */
transition: transform 300ms;   /* use translate instead of top/left */
transition: opacity 300ms;     /* use opacity instead of display */
```

---

## Common Patterns

### Fade In/Out
```css
.element {
  opacity: 0;
  transition: opacity 200ms ease-out;
}
.element.visible {
  opacity: 1;
}

/* Fade + slide up */
.card {
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 250ms ease-out, transform 250ms ease-out;
}
.card.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Scale on Hover (cards, images)
```css
.card {
  overflow: hidden;
  border-radius: 8px;
  transition: box-shadow 200ms ease-out, transform 200ms ease-out;
}
.card:hover {
  transform: translateY(-4px) scale(1.01);
  box-shadow: 0 12px 24px rgba(0,0,0,0.12);
}

/* Image zoom inside card */
.card img {
  transition: transform 400ms ease-out;
}
.card:hover img {
  transform: scale(1.05);
}
```

### Button Press Feedback
```css
.btn {
  transition: transform 80ms ease-out, background-color 150ms ease-out;
}
.btn:hover {
  background-color: color-mix(in srgb, var(--btn-color) 85%, black);
}
.btn:active {
  transform: scale(0.97) translateY(1px);
}
```

### Slide In (drawer/modal)
```css
.drawer {
  transform: translateX(100%);
  transition: transform 300ms cubic-bezier(0.4, 0, 0.2, 1);
}
.drawer.open {
  transform: translateX(0);
}

/* Modal fade + scale */
.modal-backdrop {
  opacity: 0;
  transition: opacity 200ms ease-out;
}
.modal-backdrop.open { opacity: 1; }

.modal {
  opacity: 0;
  transform: scale(0.95) translateY(8px);
  transition: opacity 250ms ease-out, transform 250ms ease-out;
}
.modal.open {
  opacity: 1;
  transform: scale(1) translateY(0);
}
```

---

## Hover States

```css
/* Link underline animation */
.link {
  text-decoration: none;
  background-image: linear-gradient(currentColor, currentColor);
  background-position: 0% 100%;
  background-repeat: no-repeat;
  background-size: 0% 2px;
  transition: background-size 250ms ease-out;
}
.link:hover { background-size: 100% 2px; }

/* Icon button */
.icon-btn {
  color: #666;
  transition: color 150ms ease-out, background-color 150ms ease-out;
  border-radius: 50%;
  padding: 8px;
}
.icon-btn:hover {
  color: #007bff;
  background-color: rgba(0, 123, 255, 0.08);
}
```

---

## Focus Rings (a11y)

```css
/* Custom focus ring — NEVER remove outline, replace it */
:focus-visible {
  outline: 2px solid #007bff;
  outline-offset: 2px;
  border-radius: 4px;
}

/* Remove only mouse focus, keep keyboard */
:focus:not(:focus-visible) {
  outline: none;
}

/* High contrast friendly */
@media (forced-colors: active) {
  :focus-visible {
    outline: 3px solid ButtonText;
  }
}

/* Animated focus ring */
.btn:focus-visible {
  outline: none;
  box-shadow:
    0 0 0 2px white,
    0 0 0 4px #007bff;
  transition: box-shadow 150ms ease-out;
}
```

---

## Skeleton Loading

```css
/* Base skeleton shimmer */
@keyframes shimmer {
  0%   { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.skeleton {
  background: linear-gradient(
    90deg,
    #f0f0f0 25%,
    #e0e0e0 50%,
    #f0f0f0 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 4px;
}

/* Dark mode skeleton */
@media (prefers-color-scheme: dark) {
  .skeleton {
    background: linear-gradient(
      90deg,
      #2a2a2a 25%,
      #3a3a3a 50%,
      #2a2a2a 75%
    );
    background-size: 200% 100%;
  }
}

/* Usage */
.skeleton-text   { height: 1rem; width: 80%; margin-bottom: 0.5rem; }
.skeleton-title  { height: 1.5rem; width: 60%; margin-bottom: 1rem; }
.skeleton-image  { height: 200px; width: 100%; }
.skeleton-avatar { height: 48px; width: 48px; border-radius: 50%; }
```

---

## Reduced Motion

```css
/* Respect user preference — MANDATORY */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* Or per component — more control */
.animated-element {
  transition: transform 300ms ease-out;
}
@media (prefers-reduced-motion: reduce) {
  .animated-element {
    transition: opacity 150ms ease-out;  /* keep subtle fade, remove movement */
  }
}
```

---

## Framer Motion (React)

### Basic variants
```tsx
import { motion } from 'framer-motion';

// Fade in
const fadeIn = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { duration: 0.3 } },
};

// Slide up
const slideUp = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.4, ease: 'easeOut' } },
};

// Spring scale
const spring = {
  hidden: { scale: 0.8, opacity: 0 },
  visible: { scale: 1, opacity: 1, transition: { type: 'spring', stiffness: 300, damping: 24 } },
};

// Usage
<motion.div variants={fadeIn} initial="hidden" animate="visible">
  Content
</motion.div>
```

### Stagger children
```tsx
const container = {
  hidden: {},
  visible: {
    transition: { staggerChildren: 0.1, delayChildren: 0.2 },
  },
};

const item = {
  hidden: { opacity: 0, y: 16 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.4, ease: 'easeOut' } },
};

<motion.ul variants={container} initial="hidden" animate="visible">
  {items.map((item) => (
    <motion.li key={item.id} variants={item}>{item.label}</motion.li>
  ))}
</motion.ul>
```

### AnimatePresence (mount/unmount)
```tsx
import { AnimatePresence, motion } from 'framer-motion';

<AnimatePresence>
  {isOpen && (
    <motion.div
      key="modal"
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.95 }}
      transition={{ duration: 0.2 }}
    >
      <Modal />
    </motion.div>
  )}
</AnimatePresence>
```

### Reduced motion in Framer
```tsx
import { useReducedMotion, motion } from 'framer-motion';

function AnimatedCard() {
  const prefersReduced = useReducedMotion();
  return (
    <motion.div
      initial={{ opacity: 0, y: prefersReduced ? 0 : 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: prefersReduced ? 0.1 : 0.4 }}
    >
      Content
    </motion.div>
  );
}
```

### Scroll animations
```tsx
import { motion, useInView } from 'framer-motion';
import { useRef } from 'react';

function Section({ children }) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-100px' });

  return (
    <motion.section
      ref={ref}
      initial={{ opacity: 0, y: 40 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.6, ease: 'easeOut' }}
    >
      {children}
    </motion.section>
  );
}
```

---

## Keyframe Animations

```css
/* Pulse (attention) */
@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50%       { transform: scale(1.05); }
}
.pulse { animation: pulse 2s ease-in-out infinite; }

/* Spin (loading) */
@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
.spinner { animation: spin 0.8s linear infinite; }

/* Shake (error) */
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25%       { transform: translateX(-8px); }
  75%       { transform: translateX(8px); }
}
.error { animation: shake 0.4s ease-in-out; }

/* Bounce in */
@keyframes bounceIn {
  0%   { transform: scale(0.3); opacity: 0; }
  50%  { transform: scale(1.05); opacity: 1; }
  70%  { transform: scale(0.9); }
  100% { transform: scale(1); }
}
.bounce-in { animation: bounceIn 0.5s cubic-bezier(0.34, 1.56, 0.64, 1); }
```

---

## Checklist

- [ ] Transitions use `transform` and `opacity` only (no width/height/top/left)
- [ ] Duration: 100-150ms hover, 250-350ms modals
- [ ] `ease-out` for entrances, `ease-in` for exits
- [ ] `will-change: transform` only on elements that will animate
- [ ] Focus rings: visible on `:focus-visible`, not removed on `:focus`
- [ ] `prefers-reduced-motion` media query respected
- [ ] Skeleton shimmer uses GPU-friendly `background-position` animation
- [ ] Framer Motion: `useReducedMotion()` hook on significant animations
- [ ] `AnimatePresence` for mount/unmount animations
