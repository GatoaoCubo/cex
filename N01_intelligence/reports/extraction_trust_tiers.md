---
quality: 8.0
id: extraction_trust_tiers
kind: knowledge_card
pillar: P01
nucleus: N01
title: "R3 Extraction: Trust Tiers -- ruflo Claims-Based Authorization"
version: 1.0
tags: [extraction, trust_tiers, claims, authorization, ruflo, agent_card, dispatch]
created: 2026-04-19
domain: competitive-intelligence
source: ruvnet/ruflo (SPARC 3.0 agent runtime)
related:
  - spec_infinite_bootstrap_loop
  - port_plan_external_repos
  - p01_kc_agent
  - p01_kc_agent_card
  - p12_wf_create_orchestration_agent
  - bld_knowledge_card_nucleus_def
  - bld_collaboration_agent
  - self_audit_n03_builder_20260408
  - bld_collaboration_capability_registry
  - bld_instruction_agent
density_score: 1.0
updated: "2026-04-22"
---

# R3 Extraction: Trust Tiers

> **Pattern**: Each agent capability has a trust level. N07 validates trust tier before dispatch.
> ruflo calls this "claims-based authorization" (ADR-016). CEX maps it to `agent_card` kind.

## Competitive Baseline

| System | Access Control | Granularity | Enforcement Point |
|--------|---------------|-------------|------------------|
| CEX (current) | Permission allowlist (settings.json) | Tool-level | Pre-tool-use hook |
| ruflo claims | Claims (read/write/execute/spawn/memory/network/admin) | Resource-scoped | Claim check before agent action |
| ruflo ADR-016 | Extended: work-stealing, load-balancing, handoff rules | Work-unit-level | Domain events + status transitions |

**Gap**: CEX has tool-level permissions for the human (settings.json) but no capability-level trust for agents. An N03 nucleus cannot declare "I require privileged memory access"; N07 cannot reject dispatch if trust is insufficient.

## Two Trust Systems Found in ruflo

### System 1 -- Claims Skill (operational, relevant to CEX)

**Source file**: `_external/ruflo/.agents/skills/claims/SKILL.md`

**Claim types**:
| Claim | Capability |
|-------|-----------|
| `read` | File read access |
| `write` | File write access |
| `execute` | Command execution |
| `spawn` | Agent spawning |
| `memory` | Memory access |
| `network` | Network access |
| `admin` | Administrative operations |

**Security levels** (pre-defined bundles):
| Level | Claims Included | CEX Mapping |
|-------|----------------|-------------|
| `minimal` | read | sandboxed |
| `standard` | read, write, execute | audited |
| `elevated` | read, write, execute, spawn, memory | privileged |
| `admin` | all claims | N07 only |

**Scope patterns**:
| Pattern | Description |
|---------|-------------|
| `*` | All resources |
| `/src/**` | All files under src |
| `/config/*.toml` | TOML files in config |
| `memory:patterns` | Patterns namespace only |

**CLI commands**:
```bash
npx claude-flow claims check  --agent agent-123 --claim write
npx claude-flow claims grant  --agent agent-123 --claim write --scope "/src/**"
npx claude-flow claims revoke --agent agent-123 --claim write
npx claude-flow claims list   --agent agent-123
```

### System 2 -- ADR-016 Domain Model (complex, for reference only)

**Source file**: `_external/ruflo/v3/@claude-flow/claims/src/domain/index.ts`

This is work-claiming (who picks up which issue), not capability-claiming. It includes:
- Work stealing (overloaded agent yields claims to underloaded agents)
- Load balancing (auto-rebalance claim distribution)
- Handoff protocol (claim transfer between agents)

**Not recommended for CEX port**: too much complexity for what CEX needs. CEX trust tiers are about capability declaration, not work distribution. Use System 1 only.

## CEX Integration Plan

### Step 1 -- Extend `agent_card` schema

**Target**: add `trust_tier` field to `agent_card` kind frontmatter.

**Tier definitions** (mapped from ruflo security levels):

| Tier | Description | Capabilities | CEX Nuclei |
|------|-------------|-------------|------------|
| `sandboxed` | Read-only, no external calls | read | N04 (knowledge), N01 (intel) |
| `audited` | Standard -- file I/O + tools | read, write, execute | N02, N05, N06 |
| `privileged` | Spawn + memory + network | + spawn, memory, network | N03 (builder), N07 (orchestrator) |

**Schema extension** (additive, no breaking change):
```yaml
# agent_card frontmatter -- new field
trust_tier: sandboxed   # sandboxed | audited | privileged
required_claims:
  - write
  - execute
claim_scope: "/N03_engineering/**"
```

### Step 2 -- N07 dispatch guard

**Location**: `_spawn/dispatch.sh` or `_tools/cex_agent_spawn.py`

```python
# In cex_agent_spawn.py, before spawning a nucleus
def validate_trust(handoff_path: str, nucleus: str) -> bool:
    agent_card = load_agent_card(nucleus)
    required_tier = agent_card.get("trust_tier", "audited")
    task_sensitivity = infer_task_sensitivity(handoff_path)

    tier_order = ["sandboxed", "audited", "privileged"]
    if tier_order.index(task_sensitivity) > tier_order.index(required_tier):
        raise DispatchError(
            f"Task requires '{task_sensitivity}' but {nucleus} "
            f"is only '{required_tier}'"
        )
    return True
```

### Step 3 -- Trust tier in handoff header

Every handoff file must declare its required trust:
```markdown
## Trust Requirements
- tier: audited
- claims: [write, execute]
- scope: N03_engineering/
```

N07 reads this before dispatch. If nucleus tier < required, N07 either escalates
(upgrades scope) or rejects and asks the user (GDP).

## Estimated Effort

| Task | LoC | Complexity | Time |
|------|-----|------------|------|
| `agent_card` schema extension | ~10 | Trivial | 30min |
| `cex_agent_spawn.py` guard | ~40 | Low | 1h |
| Update existing agent_cards (N01-N07) | ~70 (10 each) | Low | 2h |
| N07 handoff template update | ~20 | Low | 30min |
| Test: reject underprivileged dispatch | ~30 | Low | 1h |
| **Total** | **~170** | **Low** | **~5h** |

## Files to Modify

| File | Change |
|------|--------|
| `N00_genesis/P08_architecture/_schema.yaml` | Add `trust_tier` to agent_card schema |
| `archetypes/builders/agent-card-builder/` | Add trust_tier to builder ISOs |
| `N0[1-7]_*/P08_architecture/agent_card_n0[1-7].md` | Add trust_tier field to each |
| `_tools/cex_agent_spawn.py` | NEW guard: validate trust before spawn |
| `.claude/rules/n07-orchestrator.md` | Document trust check in dispatch workflow |

## Source References

- Claims skill: `_external/ruflo/.agents/skills/claims/SKILL.md`
- ADR-016 domain model: `_external/ruflo/v3/@claude-flow/claims/src/domain/index.ts`
- Security levels: SKILL.md lines 59-65
- Claim types: SKILL.md lines 18-30
- Port plan: `_docs/specs/port_plan_external_repos.md` pattern R3

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_infinite_bootstrap_loop]] | related | 0.26 |
| [[port_plan_external_repos]] | related | 0.26 |
| [[p01_kc_agent]] | sibling | 0.25 |
| [[p01_kc_agent_card]] | sibling | 0.24 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.23 |
| [[bld_knowledge_card_nucleus_def]] | sibling | 0.23 |
| [[bld_collaboration_agent]] | downstream | 0.22 |
| [[self_audit_n03_builder_20260408]] | sibling | 0.22 |
| [[bld_collaboration_capability_registry]] | downstream | 0.22 |
| [[bld_instruction_agent]] | downstream | 0.22 |
