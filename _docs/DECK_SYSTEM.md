# Deck System — Satellite Agent Manifests

> A deck is a curated manifest of agents for a specific satellite.
> Boot loads the deck → satellite knows its agent fleet → routes tasks correctly.

---

## What Is a Deck

A **deck** is a YAML file that declares which ISO packages a satellite loads at boot.
It defines:
- Which agents are available to the satellite
- Agent roles (primary vs secondary)
- Agent tiers (whitelabel / complete / standard)
- Concurrency limits

**Analogy**: A deck is like a `package.json` — it declares dependencies, not implementations.
The actual agent logic lives in `packages/{name}/`.

---

## Deck Format

```yaml
# decks/{satellite}.yaml
satellite: lily
domain: marketing
version: "1.0.0"
description: "Marketing, copy, visual content, and brand agents"

agents:
  - name: anuncio
    role: primary
    tier: whitelabel
  - name: photo
    role: primary
    tier: whitelabel
  - name: marca
    role: primary
    tier: whitelabel
  - name: seo
    role: secondary
    tier: complete

max_concurrent: 3
boot_priority: [anuncio, marca, photo]   # loaded first at boot
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `satellite` | string | YES | Satellite name (lowercase: lily, shaka, ...) |
| `domain` | string | YES | Primary domain of this satellite |
| `version` | semver | YES | Deck version (bump on any agent change) |
| `description` | string | YES | One-line description |
| `agents` | list | YES | Agent entries (see below) |
| `max_concurrent` | int | YES | Max agents running simultaneously |
| `boot_priority` | list | NO | Agents pre-loaded at satellite boot |

### Agent Entry Fields

| Field | Type | Required | Values |
|-------|------|----------|--------|
| `name` | string | YES | Must match `packages/{name}/` folder |
| `role` | string | YES | `primary` or `secondary` |
| `tier` | string | YES | `whitelabel`, `complete`, `standard`, `minimal` |

---

## Role Definitions

| Role | Description | Usage |
|------|-------------|-------|
| `primary` | Core agent for this satellite's domain | Always available, pre-loaded in boot_priority |
| `secondary` | Supporting agent, cross-domain utility | Available on demand, not pre-loaded |

**Rules**:
- Each agent has exactly 1 primary deck assignment
- An agent can appear as secondary in multiple decks
- Max 20 primary agents per deck
- No hard limit on secondary agents

---

## How Boot Loads a Deck

```
Satellite starts
  └─ Read decks/{satellite}.yaml
       └─ For each agent in boot_priority:
            └─ Load packages/{name}/manifest.yaml    # identity + capabilities
            └─ Load packages/{name}/system_instruction.md  # system prompt
       └─ Register all agents in satellite routing table
       └─ Ready to accept tasks
```

**Lazy loading**: Non-priority agents are loaded on first use, not at boot.
This keeps boot time < 15s for decks with 20+ agents.

### Boot Code Pattern

```python
import yaml
from pathlib import Path

def load_deck(satellite: str, packages_root: Path) -> dict:
    deck_path = Path(f"decks/{satellite}.yaml")
    deck = yaml.safe_load(deck_path.read_text())

    agents = {}
    for entry in deck["agents"]:
        pkg_path = packages_root / entry["name"]
        manifest = yaml.safe_load((pkg_path / "manifest.yaml").read_text())
        system = (pkg_path / "system_instruction.md").read_text()
        agents[entry["name"]] = {
            "manifest": manifest,
            "system": system,
            "role": entry["role"],
            "tier": entry["tier"],
        }
    return agents
```

---

## Composing Custom Decks

For special missions (sprints, campaigns, audits), compose a custom deck:

```yaml
# decks/custom/black_friday_campaign.yaml
satellite: custom
domain: campaign
version: "1.0.0"
description: "Black Friday 2026 campaign deck"

agents:
  - name: anuncio
    role: primary
    tier: whitelabel
  - name: pricing
    role: primary
    tier: complete
  - name: amazon-ads-agent
    role: primary
    tier: whitelabel
  - name: performance_predictor
    role: secondary
    tier: complete

max_concurrent: 4
boot_priority: [anuncio, pricing, amazon-ads-agent]
```

**Rules for custom decks**:
1. Store in `decks/custom/` (not `decks/` root)
2. `satellite` field = `custom` (not a real satellite name)
3. Any agent from `packages/` can be included
4. Max 20 primary + 10 secondary per custom deck
5. Document the mission in `description` field

---

## Deck Rules

| Rule | Value | Rationale |
|------|-------|-----------|
| Max primary agents | 20 | RAM limit: 20 agents × ~50MB context = ~1GB |
| Max secondary agents | unlimited | Lazy-loaded, no boot overhead |
| Max concurrent | 3 (default) | Prevents context window overflow |
| boot_priority max | 5 | Boot time target < 15s |
| Version bump | On any agent add/remove/tier change | Enables cache invalidation |

---

## Satellite Deck Index

| Deck | Satellite | Domain | Primary Agents | Secondary Agents |
|------|-----------|--------|---------------|-----------------|
| `lily.yaml` | LILY | Marketing | 13 | 2 |
| `shaka.yaml` | SHAKA | Research | 20 | 0 |
| `edison.yaml` | EDISON | Build | 20 | 0 |
| `york.yaml` | YORK | Commerce | 18 | 0 |
| `atlas.yaml` | ATLAS | Ops | 20 | 0 |
| `pytha.yaml` | PYTHA | Knowledge | 20 | 7 |

Total: 118 agents assigned (111 primary + 7 secondary cross-deck)

---

## Validation

Before using a deck, validate with:
```bash
python _tools/validate_iso.py --deck decks/lily.yaml
```

Checks:
1. All named agents exist in `packages/`
2. Each agent has `manifest.yaml` + `system_instruction.md`
3. No duplicate primary assignments within deck
4. `max_concurrent` <= len(boot_priority) + 2
5. Version is valid semver

---

*Deck System v1.0 | CEX Framework | 2026-03-23*
