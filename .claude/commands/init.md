---
description: "Initialize CEX for your brand. First-time setup. Usage: /init"
---

# /init — Bootstrap Your Brand

The X in CEX is YOUR brand. This command fills it.

## Steps

1. Check if already bootstrapped:
   ```bash
   python _tools/cex_bootstrap.py --check
   ```

2. If already bootstrapped, show status:
   ```bash
   python _tools/cex_bootstrap.py --status
   ```
   Ask user if they want to re-bootstrap with `--reset`.

3. If NOT bootstrapped, conduct the Brand Discovery Interview CONVERSATIONALLY:

   Ask these questions ONE AT A TIME in natural language. Wait for each answer.

   **Round 1 — Who are you?**
   - "What's your company/brand name?"
   - "In one sentence, what do you do? (this becomes your tagline)"
   - "Why does your company exist? What problem made you start?" (mission)
   - "What are your 3-5 core values? Things you'd never compromise."

   **Round 2 — Personality**
   - "If your brand were a person at a party, how would they talk? Formal or casual? Funny or serious?"
   - Present the 12 Jungian archetypes as simple options and ask which fits best.

   **Round 3 — For whom?**
   - "Describe your ideal customer — not demographics, but their daily frustrations and dreams."
   - "What changes in their life after using your product? From ___ to ___ through ___."

   **Round 4 — Market**
   - "What category are you in? What makes you different from competitors?"
   - "How do you make money? (subscription, one-time, courses, etc.)"
   - "What currency and market? (BRL/Brazil, USD/global, etc.)"

4. After collecting answers, create a YAML file with all values and run:
   ```bash
   python _tools/cex_bootstrap.py --from-file /tmp/brand_answers.yaml
   ```

5. Verify:
   ```bash
   python _tools/brand_validate.py
   python _tools/brand_audit.py --json
   ```

6. Tell the user: "Done! CEX is now the brain of [BRAND_NAME]. Every output from now on will use your brand voice, colors, and identity."

## If user gives minimal input

If user just says "/init" with a company name, ask the minimum 6 questions:
1. Name + tagline
2. Mission
3. Values (3+)
4. Archetype (present options)
5. Ideal customer + transformation
6. Category + pricing model + currency

Fill reasonable defaults for everything else based on context.

## For advanced users

They can also run directly:
```bash
python _tools/cex_bootstrap.py              # interactive CLI
python _tools/cex_bootstrap.py --from-file brand.yaml  # import
```
