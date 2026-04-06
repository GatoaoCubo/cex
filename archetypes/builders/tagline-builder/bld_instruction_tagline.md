---
id: bld_instruction_tagline
kind: instruction
pillar: P03
builder: tagline-builder
version: 1.0.0
---
# Instruction: Tagline Creation Pipeline

## Steps
1. **DISCOVER** — Read brand_config.yaml OR ask user for: brand name, industry, target audience, tone, key differentiator, competitor taglines to avoid
2. **EXTRACT** — Identify the core USP in one sentence. What does this brand do that nobody else does?
3. **GENERATE** — Produce 10+ variants across 5 approaches:
   - **Emotional**: triggers feeling (fear, aspiration, belonging, pride)
   - **Functional**: states the benefit clearly ("X that does Y")
   - **Aspirational**: paints the future state ("Become X", "The world where Y")
   - **Provocative**: challenges assumptions ("Why X when Y?", "Stop doing X")
   - **Minimal**: fewest words possible (2-4 words, Nike "Just Do It" style)
4. **FILTER** — Apply 3 tests to each variant:
   - Billboard test (3-second comprehension)
   - Competitor swap test (unique to this brand)
   - Memory test (sticky after 24h)
5. **RANK** — Score surviving variants 1-10 on: memorability, clarity, differentiation, emotional impact, versatility
6. **ADAPT** — For top 3: produce context variants (hero, social bio, email subject, ad, pitch deck)
7. **DELIVER** — Structured output with recommended + reasoning

## Anti-Patterns
- Generic lines that fit any brand ("Innovation meets excellence")
- Puns that don't translate across markets
- Taglines longer than 15 words
- Copying competitor patterns too closely
