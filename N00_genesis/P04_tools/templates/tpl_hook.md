---
id: p04_hook_NAME
kind: hook
pillar: P04
version: 1.0.0
title: "Template — Hook"
tags: [template, hook, lifecycle, event, trigger]
tldr: "A hook is a lifecycle callback triggered by system events. Runs at defined points in the 8F pipeline (pre-commit, post-build, on-error) to enforce rules or transform output."
event: "[pre_commit | post_build | on_error | on_signal]"
quality: 9.0
domain: "tool integration"
density_score: 0.86
author: "n03_builder"
created: "2026-04-07"
updated: "2026-04-07"
---

# Hook: [NAME]

## Purpose
[WHAT this hook does — validate, transform, notify, or block]

## Trigger Configuration
```yaml
event: [pre_commit | post_build | post_compile | on_error | on_signal]
filter:
  kinds: [knowledge_card, agent]  # Only trigger for these kinds
  pillars: [P01, P03]             # Only trigger for these pillars
  paths: ["N03_engineering/**"]   # Glob pattern
priority: [10 | 50 | 90]          # Lower = runs first
blocking: [true | false]          # If true, failure aborts pipeline
```

## Lifecycle Points

| Event | When | Common Use |
|-------|------|-----------|
| pre_commit | Before git commit | Validate frontmatter, lint |
| post_build | After F8 saves file | Compile, index, notify |
| post_compile | After .md → .yaml | Verify YAML integrity |
| on_error | Any pipeline error | Log, alert, retry |
| on_signal | Signal file created | Trigger next nucleus |

## Hook Implementation
```python
def hook(event, context):
    """
    Args:
        event: {type, timestamp, source}
        context: {path, kind, pillar, artifact, frontmatter}
    Returns:
        {"allow": True/False, "message": "...", "modified": None/artifact}
    """
    if not context.get("frontmatter", {}).get("id"):
        return {"allow": False, "message": "Missing id field"}
    return {"allow": True}
```

## Error Handling
- **Hook crashes**: Log error, allow pipeline to continue (unless `blocking: true`)
- **Hook timeout**: Kill after [5s], log, continue
- **Hook modifies artifact**: Must return valid artifact (re-validate)

## Quality Gate
- [ ] Event type specified
- [ ] Filter narrows scope (not all artifacts)
- [ ] Blocking vs non-blocking explicitly set
- [ ] Error handling: what happens if hook itself fails
