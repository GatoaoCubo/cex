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
   Each binds `role_name -> agent_id` with goal/backstory/tools/delegation.
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
