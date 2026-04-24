---
id: extraction_trust_tiers
kind: knowledge_card
8f: F3_inject
pillar: P01_knowledge
title: "Extraction: Trust Tiers (Capability-Based Access) from ruflo"
version: 1.1
quality: 8.9
tags: [extraction, trust, capability, access_control, ruflo, port]
created: 2026-04-12
updated: 2026-04-13
author: n01_intelligence
domain: dispatch security
source: ruvnet/ruflo v3.5
tldr: "ruflo has TWO trust systems: (a) agent capability claims system (AgentDB) and (b) CapabilityAlgebra typed permission objects with delegation, attestation, and constraint enforcement (guidance package). CEX should adopt simplified 3-tier model from (a), with optional CapabilityAlgebra concepts for future hardening."
related:
  - bld_collaboration_model_card
  - bld_architecture_capability_registry
  - bld_architecture_legal_vertical
  - port_plan_external_repos
  - bld_architecture_roi_calculator
  - spec_infinite_bootstrap_loop
  - kc_n07_orchestrator
  - bld_schema_procedural_memory
  - bld_architecture_fintech_vertical
  - bld_architecture_healthcare_vertical
---

# Extraction: Trust Tiers (R3) from ruflo

## 1. Key Finding: Capability-Based, Not Tier-Based

ruflo does **NOT** implement traditional fixed trust tiers (Tier 1/2/3).
Instead it uses a **gradient capability model** with 5 enforcement dimensions:

1. **Capabilities**: array of strings per agent
2. **Workload**: 0-100% capacity tracking
3. **Claim lifecycle**: state machine for task ownership
4. **Progress protection**: high-progress claims resist stealing
5. **Access levels**: private/team/swarm/public/system for memory

This is more flexible than fixed tiers but harder to reason about.
CEX should adopt a **simplified 3-tier model** inspired by ruflo's capability
checks but with explicit tier labels for dispatch clarity.

## 2. ruflo Implementation Details

### 2.1 Agent Capabilities (Agent.ts:17-186)

```typescript
// 7 capability types
const typeToCapability = {
  'code': 'code',
  'test': 'test',
  'review': 'review',
  'design': 'design',
  'deploy': 'deploy',
  'refactor': 'refactor',
  'debug': 'debug'
};

// Check before execution
canExecute(taskType: string): boolean {
  const required = typeToCapability[taskType];
  return this.hasCapability(required);
}
```

### 2.2 Claim Capacity Limits (rules.ts:50-265)

```typescript
// Capacity enforcement
const maxClaims = claimant.maxConcurrentClaims ?? 5;
const activeClaims = existingClaims.filter(
  c => c.claimant.id === claimant.id && isActiveClaim(c.status)
).length;

if (activeClaims >= maxClaims) {
  return ruleFailure('CLAIMANT_AT_CAPACITY');
}

if (workload >= 100) {
  return ruleFailure('CLAIMANT_AT_CAPACITY', 'At 100% capacity');
}
```

### 2.3 Claim Status Lifecycle (types.ts:32-41)

```
active -> pending_handoff | in_review | completed | released | paused | blocked | stealable
pending_handoff -> active | completed
in_review -> active | completed
paused -> active | blocked | stealable | completed
blocked -> active | paused | stealable | completed
stealable -> active | completed
completed -> (terminal)
released -> (terminal)
expired -> (terminal)
```

### 2.4 Work Stealing (rules.ts:180-286)

```typescript
type StealableReason = 'stale' | 'blocked' | 'overloaded' | 'manual' | 'timeout';

// Conditions for stealing
canStealClaim(claim, challenger, config, now):
  1. Claim must be in 'stealable' status
  2. Grace period must have elapsed (stealableAt timestamp)
  3. Progress below minProgressToProtect %
  4. Challenger != owner (no self-steal)
  5. No pending contest already
  6. Cross-type stealing allowed (if configured)
```

### 2.5 Memory Access Levels (types.ts:25-30)

```typescript
type AccessLevel = 'private' | 'team' | 'swarm' | 'public' | 'system';

// MemoryEntry includes:
interface MemoryEntry {
  accessLevel: AccessLevel;
  ownerId?: string;
}
```

### 2.6 Command Execution Security (safe-executor.ts:163-250)

```typescript
// Allowlist-only model
interface ExecutorConfig {
  allowedCommands: string[];     // ONLY these can execute
  blockedPatterns?: string[];    // injection prevention
  timeout?: number;              // default 30000ms
  maxBuffer?: number;            // default 10MB
  allowSudo?: boolean;           // default false
}

// Blocked patterns (injection prevention)
const DEFAULT_BLOCKED = [';', '&&', '||', '|', '`', '$(', '${', '>', '<', '>>', '&', '\n', '\r', '\0'];
```

## 3. CEX Integration Plan

### Current state

CEX has no trust/capability model. Any nucleus can be dispatched any task.
N07 uses routing rules (domain -> nucleus) but there's no enforcement --
nothing prevents dispatching a deploy task to N02 (marketing).

### Proposed: 3-tier trust model for agent_card

| Tier | Label | Capabilities | Example nuclei |
|------|-------|-------------|----------------|
| T1 | `sandboxed` | read, research, draft | N01 (research), N02 (marketing) |
| T2 | `audited` | T1 + build, modify artifacts, compile | N03 (builder), N04 (knowledge) |
| T3 | `privileged` | T2 + deploy, modify tools, modify rules | N05 (operations), N07 (orchestrator) |

### Schema extension for agent_card kind

Add to `P08_architecture/_schema.yaml` under `agent_card`:

```yaml
agent_card:
  frontmatter_required:
    # ... existing fields ...
    - trust_tier          # NEW: sandboxed | audited | privileged
    - capabilities        # NEW: array of capability strings
  constraints:
    trust_tiers: [sandboxed, audited, privileged]
    capability_values: [read, research, draft, build, compile, modify_artifacts, deploy, modify_tools, modify_rules]
```

### Dispatch guard in N07

Add to `_tools/cex_agent_spawn.py` or new `_tools/cex_trust_guard.py`:

```python
def check_trust(task_requirements: list[str], nucleus_card: dict) -> bool:
    """Verify nucleus has capabilities required by the task."""
    nucleus_caps = set(nucleus_card.get("capabilities", []))
    required = set(task_requirements)
    missing = required - nucleus_caps
    if missing:
        raise TrustViolation(
            f"Nucleus {nucleus_card['id']} lacks: {missing}. "
            f"Tier: {nucleus_card['trust_tier']}"
        )
    return True
```

### Files to create/modify

| File | Action | Lines est. |
|------|--------|-----------|
| `P08_architecture/_schema.yaml` | MODIFY -- add trust_tier + capabilities to agent_card | ~10 |
| `_tools/cex_trust_guard.py` | CREATE -- dispatch guard logic | ~80 |
| `_tools/cex_agent_spawn.py` | MODIFY -- call trust guard before spawn | ~15 |
| `N0{1-7}_*/agent_card_n0{1-7}.md` | MODIFY -- add trust_tier + capabilities fields | ~7 files x 3 lines |
| `.claude/rules/n07-orchestrator.md` | MODIFY -- document trust check in dispatch | ~10 |

### Estimated effort

- **Complexity**: Low (additive schema fields + one guard function)
- **Lines of code**: ~80 new + ~50 modified across 10 files
- **Dependencies**: None
- **Risk**: Low -- additive only, no existing behavior changes

## 4. Comparative Analysis

| Dimension | ruflo capability model | Proposed CEX trust tiers | Traditional RBAC |
|-----------|----------------------|-------------------------|-----------------|
| Granularity | Per-capability (7 types) | Per-tier (3 levels) | Per-role (N roles) |
| Complexity | High (5 enforcement dims) | Low (1 check at dispatch) | Medium |
| Work stealing | Yes (stealable state) | No (not needed -- N07 re-dispatches) | N/A |
| Workload tracking | Yes (0-100%) | No (PID-based liveness only) | N/A |
| Memory access control | 5 levels | Not needed (nuclei own their dirs) | N/A |
| Injection prevention | Allowlist + blocked patterns | Not needed (no shell exec in nuclei) | N/A |

### What NOT to port from ruflo

1. **Work stealing** -- CEX nuclei don't compete for tasks; N07 assigns
2. **Claim lifecycle** -- CEX uses signals (complete/fail), not claim states
3. **Workload percentage** -- CEX tracks PID liveness, not load
4. **Memory access levels** -- CEX nuclei own their N0x_*/ dirs; no cross-access needed
5. **Command injection prevention** -- CEX nuclei run in Claude Code sandbox

## 5. CapabilityAlgebra — Advanced Trust Model (v1.1 finding)

`v3/@claude-flow/guidance/src/capabilities.ts` contains a full typed capability
permission system going beyond simple capability arrays:

### Capability object structure

```typescript
// capabilities.ts:52-81 -- typed permission object
interface Capability {
  id: string;                         // UUID
  scope: CapabilityScope;             // 'tool' | 'memory' | 'network' | 'file' | 'model' | 'system'
  resource: string;                   // target (tool name, path pattern, namespace)
  actions: string[];                  // 'read' | 'write' | 'execute' | 'delete'
  constraints: CapabilityConstraint[]; // rate-limit | budget | time-window | condition | scope-restriction
  grantedBy: string;                  // agent or authority that issued it
  grantedTo: string;                  // agent it's granted to
  expiresAt: number | null;           // TTL for temporary grants
  delegatable: boolean;               // can sub-agents inherit this?
  revoked: boolean;
  attestations: Attestation[];        // cryptographic proof of audit/verification
  parentCapabilityId: string | null;  // delegation chain parent
}
```

### Authority levels (authority.ts:42)

```typescript
type AuthorityLevel = 'agent' | 'human' | 'institutional' | 'regulatory';
// Irreversibility classification for action safety:
type IrreversibilityClass = 'reversible' | 'costly-reversible' | 'irreversible';
type ProofLevel = 'standard' | 'elevated' | 'maximum';
```

### TrustLevel (transfer/types.ts:22)

```typescript
// Used for plugin marketplace trust rating:
type TrustLevel = 'official' | 'verified' | 'community' | 'unverified' | 'untrusted';
```

### What this means for CEX

| ruflo concept | CEX equivalent | Port? |
|---------------|---------------|-------|
| `CapabilityScope` (6 scopes) | Not needed — nuclei own dirs | Skip |
| `Attestation` (cryptographic proof) | Aligns with R5 proof chain | Wave 3 |
| `delegatable` flag | Relevant if sub-agents inherit caps | Future |
| `constraints` (rate-limit, budget) | aligns with `rate_limit_config` kind | Future |
| `AuthorityLevel` (agent/human) | Maps to CEX GDP (human decides WHAT) | Already implemented |
| `IrreversibilityClass` | Maps to CEX "risky actions" documentation | Partially implemented |
| `TrustLevel` (5-level marketplace) | Relevant only if CEX opens a plugin store | Wave 3 |

**Conclusion**: CapabilityAlgebra is more sophisticated than needed for CEX Wave 1.
Stick with 3-tier model (sandboxed/audited/privileged). Revisit in Wave 3.

## 6. Key Code References in ruflo

| File (relative to ruflo/) | What it contains |
|---------------------------|-----------------|
| `v3/src/agent-lifecycle/domain/Agent.ts` | Capability array, canExecute(), hasCapability() |
| `v3/@claude-flow/claims/src/domain/types.ts` | ClaimStatus lifecycle, Claimant interface |
| `v3/@claude-flow/claims/src/domain/rules.ts` | canClaimIssue(), canStealClaim(), capacity checks |
| `v3/@claude-flow/security/src/safe-executor.ts` | Allowlist model, blocked patterns, sudo prevention |
| `v3/@claude-flow/memory/src/types.ts` | AccessLevel enum (private/team/swarm/public/system) |
| `v3/@claude-flow/guidance/src/capabilities.ts` | CapabilityAlgebra, Capability interface, delegation |
| `v3/@claude-flow/guidance/src/authority.ts` | AuthorityLevel, IrreversibilityClass, ProofLevel |
| `v3/@claude-flow/cli/src/transfer/types.ts` | TrustLevel enum (5-level marketplace trust) |

## Boundary

Conhecimento destilado, estatico, versionado. NAO eh instrucao, template, ou configuracao.


## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_model_card]] | related | 0.19 |
| [[bld_architecture_capability_registry]] | related | 0.17 |
| [[bld_architecture_legal_vertical]] | related | 0.17 |
| [[port_plan_external_repos]] | related | 0.17 |
| [[bld_architecture_roi_calculator]] | related | 0.17 |
| [[spec_infinite_bootstrap_loop]] | related | 0.17 |
| [[kc_n07_orchestrator]] | sibling | 0.17 |
| [[bld_schema_procedural_memory]] | related | 0.16 |
| [[bld_architecture_fintech_vertical]] | related | 0.16 |
| [[bld_architecture_healthcare_vertical]] | related | 0.16 |
