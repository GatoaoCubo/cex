---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for feature_flag production
sources: Martin Fowler feature toggles, LaunchDarkly patterns, feature flag best practices
---

# Domain Knowledge: feature_flag

## Foundational Concept
A feature_flag artifact defines a FEATURE TOGGLE CONTRACT. It specifies whether a feature
is on or off, for whom, with what rollout strategy, and what happens when toggled. Feature
flags follow the patterns defined by Martin Fowler (2017) in "Feature Toggles": release
toggles (ship incomplete code safely), experiment toggles (A/B tests), ops toggles (kill
switches), and permission toggles (premium features).

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Martin Fowler (2017) | 4 toggle categories: release, experiment, ops, permission | feature_flag category field |
| LaunchDarkly | Flag lifecycle: create, test, ramp, full, retire | Lifecycle section in artifact |
| Unleash | Strategies: gradual rollout, user IDs, IPs | rollout_percentage + targeting |
| Split.io | Treatments + traffic allocation | Maps to state + rollout_percentage |

## Key Patterns
- Default OFF for new features (safe deploy, enable when ready)
- Kill switches: ops flags that start ON, turn OFF to disable in emergency
- Stale flag cleanup: remove flags after full rollout (tech debt prevention)
- Percentage rollout: 0 -> 5 -> 25 -> 50 -> 100 (gradual confidence building)
- Cohort targeting: by user ID, region, plan tier (not random percentage)
- Flag naming: descriptive, includes domain (enable_dark_mode, use_new_search)

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT feature_flag |
|------|------------|---------------------------|
| env_config | System environment variables | env_config is data/values; feature_flag is on/off logic |
| permission | Access control (read/write/execute) | Permission is WHO can access; flag is WHETHER feature exists |
| path_config | Filesystem path definitions | path_config is location; feature_flag is toggle |
| runtime_rule | Timeouts, retries, limits | runtime_rule is behavior parameters; flag is on/off |
| boot_config | Per-provider startup config | boot_config is initialization; flag is runtime toggle |

## References
- Martin Fowler: Feature Toggles (martinfowler.com/articles/feature-toggles.html)
- LaunchDarkly: Feature Flag Best Practices
- Pete Hodgson: Feature Toggles (2017)
