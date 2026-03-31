---
id: bld_error_handling_supabase_data_layer
kind: error_handling
pillar: P02
title: "Error Handling — Supabase Data Layer Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: null
tags: [builder, supabase, data-layer, error-handling, rollback]
density_score: 0.90
---

# Error Handling

## Migration Errors
| Error | Cause | Recovery |
|-------|-------|----------|
| Migration fails on push | SQL syntax, constraint violation | Fix SQL, `db reset` local, re-push |
| Schema drift | Manual Dashboard changes | `db diff` → create corrective migration |
| Duplicate migration | Same timestamp collision | Rename with new timestamp |
| Extension not available | Unsupported on tier | Check tier limits, upgrade or remove |
| Rollback needed | Bad migration in prod | Create reverse migration (DROP/ALTER) |

## RLS Errors
| Error | Cause | Recovery |
|-------|-------|----------|
| Tenant data leak | Missing RLS policy | `ALTER TABLE t ENABLE RLS;` + add policy |
| Permission denied | Overly restrictive policy | Check `auth.uid()`, `auth.jwt()` claims |
| Infinite recursion | Policy references same table in subquery | Materialize membership, use JWT claims |
| Performance degradation | Policy with unindexed subquery | Add index on policy columns |

## Auth Errors
| Error | Cause | Recovery |
|-------|-------|----------|
| OAuth redirect fails | Wrong SITE_URL or redirect_urls | Update in Dashboard > Auth > URL Config |
| JWT expired | Token not refreshed | Client `onAuthStateChange` handles refresh |
| Custom claims missing | app_metadata not set | Admin API: `updateUserById({app_metadata})` |
| MFA enrollment fails | TOTP not configured | Enable MFA in Dashboard > Auth > MFA |

## Storage Errors
| Error | Cause | Recovery |
|-------|-------|----------|
| Upload rejected | Mime type not in allowed list | Update bucket `allowed_mime_types` |
| File too large | Exceeds `max_file_size` | Increase limit or use resumable upload |
| Policy denied | Missing storage RLS policy | Add policy on `storage.objects` |
| Transform timeout | Image too large for imgproxy | Pre-resize before upload |

## Realtime Errors
| Error | Cause | Recovery |
|-------|-------|----------|
| No changes received | Table not in publication | `ALTER PUBLICATION supabase_realtime ADD TABLE t;` |
| User sees other's data | RLS not applied to Realtime | Enable RLS on subscribed table |
| Connection limit hit | Too many concurrent WS | Upgrade tier or reduce subscriptions |

## Edge Function Errors
| Error | Cause | Recovery |
|-------|-------|----------|
| CPU timeout | Exceeds tier limit (2s/10s/150s) | Optimize or upgrade tier |
| Secret not found | `Deno.env.get()` returns null | `supabase secrets set KEY=val` |
| CORS blocked | Missing headers in response | Add corsHeaders to every response |
| Deploy fails | TypeScript error | Fix locally with `functions serve` |

## Circuit Breaker Pattern
```text
Error detected → log to monitoring table → check error count
  IF error_count > threshold (5 in 1min):
    → pause operation (circuit OPEN)
    → alert N05 via Realtime channel
    → N04 reviews and fixes
    → resume (circuit CLOSED)
```

## Quota Alerts
| Metric | Warning (75%) | Critical (90%) | Action |
|--------|--------------|-----------------|--------|
| DB storage | Alert N04 | Alert N04 + N07 | Cleanup or upgrade |
| Bandwidth | Alert N04 | Throttle non-critical | CDN + optimize |
| Edge invocations | Alert N04 | Cache results | Reduce frequency |
| Auth MAU | Alert N04 | Review signup flow | Plan upgrade |
