---
id: ex_response_format_ad_copy
kind: response_format
pillar: P05
title: Ad Copy Output Format
tags: [output, format, ad, copy]
references:
  - tpl_response_format
  - ex_agent_copywriter
  - ex_quality_gate_copy
---

# Ad Copy Output Format

> Skeleton: response_format kind

```yaml
headline: string (max 60 chars)
body: string (max 2200 chars)
cta: string (max 30 chars)
hashtags: list (max 5)
emoji_count: int (max 3)
```

## Links

- Used by: [[ex_agent_copywriter]]
- Validated by: [[ex_quality_gate_copy]]
- Function: PRODUCE (what the AI outputs)
