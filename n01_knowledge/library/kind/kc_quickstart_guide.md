---
id: kc_quickstart_guide
kind: knowledge_card
title: Quickstart Guide Knowledge Card
version: 1.0.0
quality: null
pillar: P01
---

# Quickstart Guide Specification

This knowledge card defines the structure and requirements for creating concise onboarding guides for products/APIs. Guides should follow these specifications:

1. **Structure Requirements**:
   - Maximum 5 steps with clear visual hierarchy
   - Each step must include:
     - Step number and title
     - Brief instructional text (1-2 sentences)
     - Visual cue (icon/arrow)
     - Optional: Keyboard shortcut

2. **Content Guidelines**:
   - Use imperative tone ("Do this", "Click here")
   - Include progress indicator (e.g., "Step 2 of 5")
   - Add "Got It" confirmation with optional skip option
   - Provide exit pathway to main interface

3. **Visual Design**:
   - Step indicators with color coding (green for completed, gray for pending)
   - Tooltip support for all interactive elements
   - Responsive layout for all device sizes
   - Accessibility labels for screen readers

4. **Performance**:
   - Load time < 300ms
   - No layout shifts during tour
   - Graceful degradation for disabled features

5. **Analytics**:
   - Track completion rate
   - Monitor drop-off points
   - Record user interaction patterns

All quickstart guides must include:
- A welcome message with value proposition
- A progress tracker
- A "Skip Tour" option
- A "Need Help?" support link
- A "Revisit Later" bookmark option

Example format:
```
1. [Feature A] - "Create your first project"
   → Click the "New Project" button in the top menu
   → (Ctrl+Shift+N)

2. [Feature B] - "Invite team members"
   → Use the "Share" button to send invites
   → (Ctrl+Shift+S)
```
