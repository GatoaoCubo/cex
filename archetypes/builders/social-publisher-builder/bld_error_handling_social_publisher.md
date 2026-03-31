---
kind: error_handling
id: bld_error_handling_social_publisher
pillar: P11
llm_function: GOVERN
purpose: Failure modes, retry logic, fallbacks for social publisher pipeline
---

# Error Handling: social_publisher

## Pipeline Failure Matrix
| Step | Error | Severity | Recovery | Fallback |
|------|-------|----------|----------|----------|
| 1. LOAD | Config file not found | FATAL | Abort with clear error message | None — config is required |
| 1. LOAD | Invalid YAML syntax | FATAL | Parse error with line number | None — fix config |
| 1. LOAD | Missing required section | FATAL | List missing sections | None — fix config |
| 2. FETCH | Catalog API timeout | HIGH | Retry 3x with exponential backoff | Use cached catalog |
| 2. FETCH | Catalog API auth failure | FATAL | Log + notify | None — fix credentials |
| 2. FETCH | Empty catalog | MEDIUM | Skip cycle, log warning | Schedule retry in 1h |
| 3. SELECT | All items in cooldown | LOW | Skip cycle, log "nothing to post" | Extend cooldown window |
| 3. SELECT | Rotation state corrupted | MEDIUM | Rebuild state from logs | Clear state, start fresh |
| 4. GENERATE | LLM API timeout | HIGH | Retry 2x | Use fallback template caption |
| 4. GENERATE | LLM returns empty/invalid | MEDIUM | Retry with stronger prompt | Use fallback template |
| 4. GENERATE | Caption exceeds platform limit | LOW | Truncate intelligently | Hard truncate at limit |
| 5. OPTIMIZE | No time data for platform | LOW | Use default time (12:00 local) | Post immediately |
| 6. HASHTAGS | Over platform hashtag limit | LOW | Truncate to limit (brand first) | Use brand tags only |
| 7. PUBLISH | API rate limit (429) | HIGH | Backoff per Retry-After header | Queue for next cycle |
| 7. PUBLISH | API auth failure (401/403) | FATAL | Log + notify admin | None — fix API key |
| 7. PUBLISH | API server error (500) | HIGH | Retry 3x with backoff | Queue for next cycle |
| 7. PUBLISH | Network timeout | HIGH | Retry 3x | Queue for next cycle |
| 7. PUBLISH | Media upload failure | MEDIUM | Retry with smaller image | Post text-only |
| 8. LOG | Log write failure | LOW | stderr fallback | Continue pipeline |
| 9. NOTIFY | Webhook failure | LOW | Log warning, continue | Skip notification |
| 10. ROTATE | State write failure | MEDIUM | Retry once | Log warning, continue |

## Retry Policy
```yaml
retry:
  default:
    max_attempts: 3
    backoff: exponential
    base_seconds: 30
    max_seconds: 300
  api_publish:
    max_attempts: 3
    backoff: exponential
    base_seconds: 30
    respect_retry_after: true
  llm_generate:
    max_attempts: 2
    backoff: fixed
    base_seconds: 5
    fallback: template_caption
```

## Circuit Breaker
If 3 consecutive publish attempts fail across cycles:
1. Set circuit = OPEN
2. Notify admin via all channels
3. Wait 30 minutes
4. Attempt 1 test post (circuit = HALF-OPEN)
5. If success → circuit = CLOSED, resume normal
6. If fail → circuit = OPEN, wait 1 hour, repeat

## Alerting Levels
| Level | Trigger | Action |
|-------|---------|--------|
| INFO | Successful post | Log only |
| WARN | Retry succeeded | Log + optional notify |
| ERROR | Step failed after retries | Log + notify admin |
| FATAL | Config invalid or auth failure | Log + notify + halt pipeline |
