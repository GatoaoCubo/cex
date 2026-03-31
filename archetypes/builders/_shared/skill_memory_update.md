---
id: skill_memory_update
kind: instruction
scope: shared
purpose: Teach builders to reflect and record learnings after execution
---
# Skill: Memory Update After Execution

## When to Use
After EVERY build session, before signaling complete.

## What to Record
One structured observation per session. Focus on **reusable patterns**, not obvious facts.

### Good Observations
- "Splitting handler into validate+process+respond reduced errors 40%"
- "Builders with >3 tools need explicit tool-selection criteria"
- "ISO files >4KB overflow small model context — split into sections"

### Bad Observations (DO NOT record)
- "The schema was followed" (obvious)
- "The file was saved" (mechanical)
- "Quality was high" (vague)

## How to Record

```bash
python _tools/cex_memory_update.py \
  --builder <your-builder-id> \
  --type feedback \
  --observation "what you learned" \
  --pattern "generalizable rule" \
  --evidence "data that supports it" \
  --confidence 0.8 \
  --outcome SUCCESS
```

## Observation Types
| Type | Decay | When to Use |
|------|-------|-------------|
| user | 0.02/day | User preference or style |
| feedback | 0.00 | Quality feedback (NEVER decays) |
| project | 0.05/day | Project-specific context |
| reference | 0.03/day | External knowledge or docs |

## Rules
1. ONE observation per session (quality > quantity)
2. Confidence 0.0-1.0 (be honest, 0.6-0.8 is normal)
3. Pattern must be ACTIONABLE (someone else can apply it)
4. Evidence must be MEASURABLE when possible
5. If nothing was learned, don't force an observation
