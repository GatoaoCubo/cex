#!/usr/bin/env python3
# 05_grid_mission -- Write handoffs and dispatch 6 nuclei in parallel
# Shows the N07 orchestrator pattern: write handoffs -> dispatch grid.
# ASCII-only (CEX convention).

import os
import sys
import subprocess

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
MISSION = "DEVCOM"
HANDOFF_DIR = os.path.join(REPO_ROOT, ".cex", "runtime", "handoffs")

# -- Define what each nucleus should do --
TASKS = {
    "n01": "Research developer community platforms: Discord vs Slack vs custom. "
           "Produce a knowledge_card with comparison matrix.",
    "n02": "Write launch copy for a developer community: tagline, landing page "
           "hero text, 3 email subject lines.",
    "n03": "Design the agent architecture for a community bot: moderation, "
           "onboarding, FAQ. Produce an agent_card.",
    "n04": "Create a knowledge_card documenting community governance models: "
           "BDFL, council, meritocracy, DAO.",
    "n05": "Write deployment config for a Discord bot: env_config with "
           "required secrets, rate limits, health checks.",
    "n06": "Design pricing tiers for a developer community platform: "
           "free, pro, enterprise. Include feature gating.",
}

HANDOFF_TEMPLATE = """---
id: handoff_{mission}_{nucleus}
kind: handoff
mission: {mission}
nucleus: {nucleus}
---

# {mission} -- {nucleus.upper()} Task

## Task
{task}

## DECISIONS (from user)
See: .cex/runtime/decisions/decision_manifest.yaml

## Expected output
- Kind: as appropriate for the task
- Quality target: >= 8.0
- Signal on completion
"""

def write_handoffs():
    """Write handoff files for each nucleus."""
    os.makedirs(HANDOFF_DIR, exist_ok=True)
    for nucleus, task in TASKS.items():
        path = os.path.join(HANDOFF_DIR, f"{MISSION}_{nucleus}.md")
        content = HANDOFF_TEMPLATE.format(
            mission=MISSION, nucleus=nucleus, task=task
        )
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[Handoff] Wrote {path}")

if __name__ == "__main__":
    print(f"=== Grid Mission: {MISSION} ===\n")
    write_handoffs()

    print(f"\n[Dispatch] To launch the grid, run:")
    print(f"  bash _spawn/dispatch.sh grid {MISSION}")
    print(f"\n[Monitor] To check status:")
    print(f"  bash _spawn/dispatch.sh status")
    print(f"  git log --oneline --since='5 minutes ago'")
    print(f"\n[Stop] To kill completed nuclei:")
    print(f"  bash _spawn/dispatch.sh stop")
