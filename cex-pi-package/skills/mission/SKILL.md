---
description: "Decompose goal into waves of nucleus work. Usage: /mission <goal>"
---

# /mission

Decompose the goal into a multi-wave execution plan.

## Steps
1. Kill any idle processes first (always)
2. Identify which nuclei are needed (N01-N06)
3. Group into waves (parallel within wave, sequential between waves)
4. Write handoffs to `.cex/runtime/handoffs/`
5. Dispatch each nucleus via `bash _spawn/dispatch.sh solo`
6. Poll for signals every 90s, kill on complete (taskkill /F /PID /T)
7. Synthesize between waves (read results, create specific specs)
8. Consolidate: doctor + flywheel + commit

## Nucleus routing
| Domain | Nucleus |
|--------|---------|
| Research/analysis | N01 |
| Marketing/copy | N02 |
| Build/create | N03 |
| Knowledge/docs | N04 |
| Code/test/deploy | N05 |
| Brand/monetization | N06 |

## Rules
- N07 never builds directly -- dispatch only
- GDP before subjective decisions
- Kill before spawn (principle #6)
- Synthesize between waves (principle #7)
