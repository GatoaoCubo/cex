---
glob: "**"
alwaysApply: true
description: "Brand bootstrap detection — trigger brand setup on first interaction"
---

# Brand Bootstrap Detection

## CHECK ON EVERY SESSION START

Before executing ANY user request, check if CEX has been bootstrapped:

```bash
python _tools/cex_bootstrap.py --check
```

### If NOT bootstrapped (exit code 1):

**DO NOT proceed with the user's request.** Instead:

1. Explain briefly:
   > "I notice this CEX instance hasn't been configured for your brand yet.
   > The X in CEX is a variable — let me fill it with YOUR identity.
   > This takes about 2 minutes and makes everything I produce match your brand."

2. Ask the MINIMUM questions in natural conversation:
   - "What's your company/brand name?"
   - "What do you do in one sentence?"
   - "What are your 3 core values?"
   - "How would you describe your brand's personality — more formal or casual? Technical or friendly?"
   - "Who is your ideal customer?"
   - "How do you make money — subscription, one-time sales, courses?"

3. From the answers, write a YAML file and bootstrap:
   ```bash
   python _tools/cex_bootstrap.py --from-file /tmp/brand_init.yaml
   ```

4. Confirm: "Done! CEX is now configured for [BRAND_NAME]. Let's get to work."

5. THEN proceed with the user's original request.

### If ALREADY bootstrapped (exit code 0):

Proceed normally. The brand context is auto-injected into all prompts.

## WHY THIS MATTERS

Without brand_config.yaml, every nucleus produces GENERIC output.
With it, every output matches the user's voice, colors, and identity.
The 2-minute investment saves hours of "make it sound more like us" revisions.
