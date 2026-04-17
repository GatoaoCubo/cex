---
id: extraction_trust_tiers
kind: knowledge_card
pillar: P01
nucleus: N01
domain: security
title: "Extraction: Trust Tiers (R3 -- ruflo)"
version: 1.0
quality: 8.4
tags: [extraction, trust_tiers, security, agent_card, dispatch_guard, ruflo, port_plan]
created: 2026-04-17
source: C:/Users/CEX/Documents/GitHub/_external/ruflo/
source_files:
  - v3/@claude-flow/cli/src/transfer/types.ts (TrustLevel)
  - v3/@claude-flow/cli/src/plugins/store/types.ts (PluginEntry.trustLevel)
  - .agents/skills/claims/SKILL.md (Claims authorization)
port_priority: P0_HIGH
---

# Extraction: Trust Tiers (R3 -- ruflo)

> Source: `ruvnet/ruflo` | Priority: P0 HIGH | Effort: Low | Blocking: No (additive field)

## 1. What ruflo implements

Ruflo uses claims-based authorization at two levels:

1. **TrustLevel** (per-entity): a 5-value enum applied to plugins, patterns, and agents
2. **Claims** (per-operation): fine-grained capability grants with scope patterns

The trust tier governs which capabilities are available to each entity and whether dispatch
should proceed. N07 (dispatch guard) checks `minTrustLevel` against the caller's `trustLevel`
before spawning.

## 2. TrustLevel enum (source: `transfer/types.ts`)

```typescript
export type TrustLevel = 'official' | 'verified' | 'community' | 'unverified' | 'untrusted';
```

| Level | Meaning | CEX equivalent |
|-------|---------|----------------|
| `official` | Core team, cryptographically signed | N00_genesis builders, N07 orchestrator |
| `verified` | Third-party, audited by team | Peer-reviewed nuclei (N01-N06) |
| `community` | Public, user-contributed | External plugins, agentic RAG tools |
| `unverified` | Untested, not reviewed | Test environments, experimental |
| `untrusted` | Known bad or explicitly blocked | Reject immediately at dispatch |

## 3. Claims security levels (source: `claims/SKILL.md`)

| Level | Claims granted | CEX nucleus match |
|-------|---------------|------------------|
| `minimal` | read only | Sandboxed viewers / read-only agents |
| `standard` | read + write + execute | Standard nuclei (N01-N06) |
| `elevated` | + spawn + memory | N07 (orchestrator, spawns nuclei) |
| `admin` | all claims | Internal automation (cex_auto, test) |

### Claim types

| Claim | Meaning | Typical holder |
|-------|---------|---------------|
| `read` | Read files | All nuclei |
| `write` | Write files | All nuclei |
| `execute` | Shell commands | N03, N05 |
| `spawn` | Agent spawning | N07 |
| `memory` | Memory system access | N04, N07 |
| `network` | Network calls | N01 (research), N05 |
| `admin` | All operations | cex_auto.py, CI |

## 4. Enforcement pattern (from `plugins/store/types.ts`)

```typescript
interface PluginEntry {
  trustLevel: TrustLevel;       // entity's declared level
  securityAudit?: SecurityAudit; // optional audit record
}

interface PluginFilter {
  minTrustLevel: TrustLevel;    // caller's required minimum
}
```

Dispatch guard pseudo-code from ruflo:

```typescript
// Before spawning, check caller trust >= required trust
const TRUST_ORDER = ['untrusted', 'unverified', 'community', 'verified', 'official'];
function canDispatch(callerLevel: TrustLevel, requiredLevel: TrustLevel): boolean {
  return TRUST_ORDER.indexOf(callerLevel) >= TRUST_ORDER.indexOf(requiredLevel);
}
```

## 5. CEX integration plan

### Step 1: Extend `agent_card` kind schema

Add `trust_tier` field to the `agent_card` schema in `.cex/kinds_meta.json` and
`N00_genesis/P08_architecture/_schema.yaml`:

```yaml
# In agent_card frontmatter:
trust_tier: verified          # official | verified | community | unverified | untrusted
required_claims:              # list of claim types this agent needs
  - read
  - write
  - execute
dispatch_guard: true          # whether N07 must check trust before spawn
```

### Step 2: Add dispatch guard in N07 dispatch protocol

File: `.claude/rules/n07-orchestrator.md` -- append to Dispatch Workflow:

```markdown
## Dispatch Guard (trust_tier check)
Before any dispatch, verify:
1. Read target nucleus agent_card.trust_tier
2. Compare against handoff.required_trust (default: 'verified')
3. If nucleus.trust_tier < required: REJECT + log to incident_report
4. If nucleus.trust_tier == 'untrusted': BLOCK permanently
```

### Step 3: Apply tier to existing nuclei

| Nucleus | Recommended trust_tier | Rationale |
|---------|----------------------|-----------|
| N00_genesis | official | Core archetype, signed by team |
| N07 | official | Orchestrator, highest privilege |
| N01-N06 | verified | Peer-reviewed, in repo, tested |
| External plugins | community | User-added, not reviewed |
| Test harnesses | unverified | Not audited |

### Step 4: Enforcement in `cex_agent_spawn.py`

File: `_tools/cex_agent_spawn.py` -- add trust check:

```python
TRUST_ORDER = ['untrusted', 'unverified', 'community', 'verified', 'official']

def check_dispatch_trust(agent_card: dict, required: str = 'verified') -> bool:
    tier = agent_card.get('trust_tier', 'unverified')
    if tier == 'untrusted':
        raise DispatchBlocked(f"Agent {agent_card['id']} is untrusted -- dispatch blocked")
    return TRUST_ORDER.index(tier) >= TRUST_ORDER.index(required)
```

## 6. Comparison: CEX dispatch (current) vs Trust-Tier dispatch (proposed)

| Dimension | Current CEX | Trust-Tier extension |
|-----------|------------|---------------------|
| Who can dispatch | Anyone with nucleus boot script | Requires trust_tier >= required_level |
| Capability check | None (trust nucleus existence) | Per-nucleus claims list |
| Untrusted rejection | Manual (user judgment) | Automatic BLOCK at dispatch |
| Audit trail | git commit + signal | + trust check log in incident_report |
| Complexity cost | Zero | ~50 lines in agent_spawn.py + schema field |
| Security uplift | None | Prevents dispatch to corrupted/hijacked nuclei |

## 7. Estimated effort

| Task | Complexity | Lines |
|------|-----------|-------|
| Schema extension (`agent_card`, `kinds_meta.json`) | Low | ~30 |
| Guard in `cex_agent_spawn.py` | Low | ~50 |
| Backfill `trust_tier` on 8 nucleus agent_cards | Low | ~16 (2 fields x 8) |
| Update N07 dispatch rule doc | Low | ~20 |
| Tests | Low | ~50 |
| **Total** | **Low** | **~166** |

## 8. Risks

| Risk | Mitigation |
|------|-----------|
| Tier assignment is subjective initially | Start with `verified` for all N01-N06; refine post-audit |
| Trust drift (tier assigned but not re-audited) | Add `trust_tier_audited_at` timestamp; warn if >90 days |
| Claims not enforced at runtime | Phase 2: enforce at tool-call level via cex_hooks.py |
| Breaking change for existing dispatches | `trust_tier` field is optional; defaults to 'verified' when missing |
