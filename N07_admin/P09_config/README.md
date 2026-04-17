# P09 Config — N07 Admin

> Orchestrating Sloth · configuration for orchestration, dispatch, routing

## Scope in N07
Runtime settings for the orchestrator: dispatch routing rules,
nucleus fallback chains, session defaults, rate limits on spawn
operations, wave timeouts. Sloth drives maximum leverage — configs
here let N07 delegate without re-asking.

## Kinds that live here
- `env_config` — env vars for orchestrator (CEX_NUCLEUS, PATHs)
- `rate_limit_config` — throttles on dispatch/spawn operations
- `feature_flag` — orchestrator toggles (auto-consolidate, grid-of-crews)
- `path_config` — handoff/signal/PID directory layout

## Related
- `orchestration/` — the workflows and dispatch rules this config governs
- `architecture/` — decision records referencing config choices
