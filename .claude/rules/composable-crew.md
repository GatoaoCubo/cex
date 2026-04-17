# Composable Crew Protocol

**The 5th wiring rule.** Alongside 8F (how to think), GDP (who decides), dispatch-depth (how deep), and shared-file-proposal (how to merge), composable-crew is how CEX assembles **multi-role teams** for work that single builders cannot cover.

## When to use a crew (vs. solo builder vs. grid)

| Scenario | Use | Why |
|----------|-----|-----|
| Produce 1 artifact of 1 kind | **solo builder** | 8F pipeline is enough |
| Produce N artifacts in parallel, independent | **grid dispatch** | Nuclei handle their own scopes |
| Produce 1 coherent deliverable that requires N roles with handoffs | **crew** | Roles depend on each other; process matters |

Crews are the right tool when the **output is a package** (e.g. launch kit, RFP response, incident postmortem) that requires multiple specialties in a defined topology.

## The 5 WAVE8 primitives

| Kind | Pillar | Function | Purpose |
|------|--------|----------|---------|
| `crew_template` | P12 | CALL | Reusable recipe -- roles table + process topology + handoff protocol |
| `role_assignment` | P02 | CONSTRAIN | Binds a role_name to an agent_id with goal/backstory/tools |
| `capability_registry` | P08 | CONSTRAIN | Index of all spawnable agents (282 today); crew planner queries it |
| `nucleus_def` | P02 | CONSTRAIN | Machine-readable nucleus identity + capabilities (1 per nucleus) |
| `team_charter` | P12 | GOVERN | Mission contract per crew instance (budget, deadline, gate) |

## Topology (process types)

| Process | Semantics | When |
|---------|-----------|------|
| `sequential` | Role N waits for Role N-1's artifact | When each step strictly depends on the prior |
| `hierarchical` | Manager role coordinates workers; may delegate | When coordination overhead is worth it (>= 5 roles) |
| `consensus` | All roles work in parallel, vote on final | When diverse perspectives reduce risk (review / audit) |

## How to instantiate a crew (end-to-end)

```bash
# 1. Discover available crews
python _tools/cex_crew.py list

# 2. Inspect the plan (dry)
python _tools/cex_crew.py show product_launch

# 3. Dry-run (generates prompts under .cex/runtime/crews/{name}/)
python _tools/cex_crew.py run product_launch \
    --charter N02_marketing/crews/team_charter_launch_demo.md

# 4. Real execution (LLM calls + artifacts)
python _tools/cex_crew.py run product_launch \
    --charter N02_marketing/crews/team_charter_launch_demo.md \
    --execute
```

## Authoring a new crew

1. **Pick an agent set** -- query `capability_registry.json` for candidates:
   ```bash
   python _tools/cex_capability_index.py --query "research"
   ```
2. **Write role_assignments** (one per role) in `N0x/crews/p02_ra_{role}.md`.
   Each binds `role_name -> agent_id` with goal/backstory/P04_tools/delegation.
3. **Write crew_template** in `N0x/crews/p12_ct_{name}.md` with the Roles
   table referencing your role_assignments and a `process:` topology.
4. **Write team_charter** (instance-specific) with mission/budget/deadline/gate.
5. **Validate** -- `python _tools/cex_crew.py show {name}` prints the resolved plan.

## Integration with 8F

A crew run is a specialization of F6 PRODUCE that expands into N sub-F6 runs,
one per role. Each role still executes F1..F8 internally (it's a full builder).
The crew layer adds:
- **F3 INJECT augmentation**: each role receives the upstream role's artifact
- **F7 GOVERN coordination**: a charter-level quality gate runs after all roles complete
- **F8 COLLABORATE coordination**: role handoffs go through a2a Task signals

## Grid + Crew composition

The three dispatch modes stack:

| Layer | What it runs | Parallelism |
|-------|--------------|-------------|
| **solo** | One builder, one artifact | none |
| **crew** | N roles with handoffs (sequential / hierarchical / consensus) | intra-crew only |
| **grid** | N solo builders OR N crew instances | full cross-cell |
| **grid of crews** | N parallel crew instances, each with its own charter | crews run in parallel; roles inside each crew follow their topology |

Example -- ship 3 product launches on the same day:

```
N07 dispatches a grid with 3 cells:
  cell_1: cex_crew.py run product_launch --charter charter_prod_A.md --execute
  cell_2: cex_crew.py run product_launch --charter charter_prod_B.md --execute
  cell_3: cex_crew.py run product_launch --charter charter_prod_C.md --execute

Each cell runs the same 4-role sequential crew (research -> copy -> design -> QA)
but grounded on a different charter (different product, deadline, budget).

Total concurrency: 3 crews x (1 active role at a time each) = 3 LLM calls in flight.
If you switch the crew to `process: consensus`, concurrency becomes 3 x 4 = 12.
```

Grid+crew is the highest-leverage composition CEX offers: you parallelize
entire packages, not just individual artifacts, while keeping coherence
within each package via the crew's handoff protocol.

## Swarm mode (BORIS_MERGE D5)

When you need **N parallel builders of the same kind** (not N different roles,
not a full crew with handoffs), use swarm instead of crew. Swarm trades
coherence for breadth:

```bash
bash _spawn/dispatch.sh swarm agent 5 "scaffold 5 niche sales agents"
# Spawns 5 agent-builders in parallel worktrees, each produces one artifact.
```

Contrast:
- **crew** -- 4 roles, 1 coherent deliverable, handoffs between roles
- **swarm** -- N builders, N independent deliverables of same kind, isolated worktrees
- **grid** -- heterogeneous nuclei, arbitrary handoffs, mission-scoped

Swarm is the right tool when the goal is **coverage** (explore a kind-space by
generating variants) rather than **integration** (roles depend on each other).

## When crews are NOT the answer

- **1 artifact, 1 kind** -> solo builder, not a crew
- **Independent parallel production** -> grid dispatch, not a crew
- **Pure research** -> N01 alone; the crew pattern adds no value
- **No handoffs needed** -> if roles never consume each other's output, grid is cheaper

## Properties

| Property | Value |
|----------|-------|
| Kind | `rule` |
| Pillar | cross-cutting |
| Domain | crew orchestration |
| Pipeline | 8F with F6 crew expansion |
| Quality target | 9.0+ |
| Density target | 0.85+ |
