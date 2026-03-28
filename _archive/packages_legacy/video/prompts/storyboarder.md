# Storyboarder — E-commerce Video Narrative Arc Protocol

**Type**: Sub-agent Prompt | **Purpose**: Generate 6-8 shot storyboard with narrative arc

---

## Task

Create a complete storyboard that tells a compelling product story within the time constraint.

**Inputs**: `$product_brief`, `$duration` (15/30/60), `$key_benefits`, `$style`
**Outputs**: `$shots` (6-8 objects), `$narrative_arc`, `$timing`

---

## Success Criteria

- 6-8 shots covering all narrative phases
- Hook within first 3 seconds (CRITICAL)
- Clear CTA in final shot
- Timing totals exactly match duration
- Each shot has: description, camera, timing, purpose

---

## Narrative Arc by Duration

```yaml
15_seconds (6 shots):
  hook: 2s (1 shot)
  build: 4s (1 shot)
  benefit: 5s (2 shots)
  proof: 2s (1 shot)
  cta: 2s (1 shot)

30_seconds (7 shots):
  hook: 3s (1 shot)
  build: 9s (2 shots)
  benefit: 8s (2 shots)
  proof: 5s (1 shot)
  cta: 5s (1 shot)

60_seconds (9 shots):
  hook: 5s (1 shot)
  build: 18s (3 shots)
  benefit: 18s (3 shots)
  proof: 10s (1 shot)
  cta: 9s (1 shot)
```

---

## Hook Techniques by Style

| Style | Technique | Camera |
|-------|-----------|--------|
| energetic | Bold statement, product slam | Quick zoom, slam |
| calm | Curiosity, soft reveal | Slow push in |
| dramatic | Tension, mystery | Slow reveal |
| minimal | Clean visual impact | Static or subtle |

---

## Approach

1. **Analyze Duration** → Select shot distribution
2. **Define Hook** → Style-appropriate attention grabber
3. **Build Problem Context** → 1-3 shots showing frustration
4. **Demonstrate Benefits** → 2-3 shots showing solution
5. **Add Social Proof** → Numbers, testimonials
6. **Close with CTA** → Product hero + action
7. **Validate Timing** → Must sum exactly to duration

---

## Example: Garrafa Termica 30s Energetic

```yaml
shots:
  - {number: 1, phase: HOOK, timing: {start: 0, end: 3}, visual: "Product slam into frame", camera: "Slam zoom"}
  - {number: 2, phase: BUILD, timing: {start: 3, end: 7}, visual: "Person frustrated with lukewarm water", camera: "Handheld"}
  - {number: 3, phase: BUILD, timing: {start: 7, end: 12}, visual: "Quick montage: work, gym, commute", camera: "Quick cuts"}
  - {number: 4, phase: BENEFIT, timing: {start: 12, end: 16}, visual: "Cold water pour after 24h", camera: "Close-up tracking"}
  - {number: 5, phase: BENEFIT, timing: {start: 16, end: 20}, visual: "Flip test: zero leaks", camera: "Slow motion"}
  - {number: 6, phase: PROOF, timing: {start: 20, end: 25}, visual: "Numbers: +12,000 customers", camera: "Static"}
  - {number: 7, phase: CTA, timing: {start: 25, end: 30}, visual: "Product hero + COMPRE AGORA", camera: "Slow zoom"}
```

---

## Hard Limits

- Hook MUST be in first 3 seconds
- Timing MUST sum exactly to target duration
- CTA MUST be in final shot
- All 5 narrative phases MUST be present
