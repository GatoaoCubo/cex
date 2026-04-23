#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Memory Types -- 4-type taxonomy with decay rates + save guards.

Pattern: OpenClaude memdir/memoryTypes.ts
Adapted for CEX builder memory system.

Types:
  user      -- Role, goals, preferences (slow decay)
  feedback  -- Corrections + confirmations (PERMANENT, no decay)
  project   -- Ongoing work, deadlines (fast decay)
  reference -- External system pointers (moderate decay)

Usage:
    from cex_memory_types import MemoryType, DECAY_RATES, should_save
"""

from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class MemoryType(str, Enum):
    """Memory observation types -- constrained to 4 categories."""
    USER = "user"           # Role, goals, preferences
    FEEDBACK = "feedback"   # Corrections + confirmed approaches (PERMANENT)
    PROJECT = "project"     # Ongoing work, deadlines, context
    REFERENCE = "reference" # External system pointers


# Decay rates per update cycle
# feedback = 0.00 (permanent -- corrective knowledge never decays)
DECAY_RATES = {
    MemoryType.USER: 0.02,       # Slow -- preferences evolve slowly
    MemoryType.FEEDBACK: 0.00,   # PERMANENT -- corrections are gold
    MemoryType.PROJECT: 0.05,    # Fast -- project context changes quickly
    MemoryType.REFERENCE: 0.03,  # Moderate -- external pointers shift
}


# Patterns that should NOT be saved as memory (derivable from code/git)
SAVE_EXCLUSIONS = [
    "code pattern",
    "code convention",
    "architecture",
    "file structure",
    "directory structure",
    "git history",
    "git log",
    "recent changes",
    "debugging solution",
    "fix recipe",
]


def should_save(observation: str, existing_docs: str = "") -> Tuple[bool, str]:
    """Guard: reject observations that belong in code, not memory.

    Returns (should_save, reason).

    Follows OpenClaude's WHAT_NOT_TO_SAVE rules:
    - Code patterns -> derivable from grep
    - Git history -> derivable from git log
    - Debugging solutions -> the fix is in the code
    - Anything in CLAUDE.md -> already documented
    - Ephemeral task details -> temporary state
    """
    obs_lower = observation.lower()

    for exclusion in SAVE_EXCLUSIONS:
        if exclusion in obs_lower:
            return False, f"Rejected: '{exclusion}' is derivable from code/git, not memory-worthy"

    if existing_docs and observation.strip() in existing_docs:
        return False, "Rejected: already documented in project docs"

    # Reject very short observations (< 10 chars = likely noise)
    if len(observation.strip()) < 10:
        return False, "Rejected: too short to be useful memory"

    return True, "OK"


def parse_memory_type(raw: str) -> MemoryType:
    """Parse a raw string into a MemoryType. Defaults to PROJECT."""
    try:
        return MemoryType(raw.lower())
    except ValueError:
        return MemoryType.PROJECT


@dataclass
class MemoryFrontmatter:
    """Required frontmatter for memory files.

    Memory files are .md with YAML frontmatter:
    ---
    name: descriptive-name
    description: one-line description for relevance matching
    type: user|feedback|project|reference
    ---
    """
    name: str
    description: str
    type: MemoryType

    def to_yaml(self) -> str:
        return (
            f"---\n"
            f"name: {self.name}\n"
            f"description: {self.description}\n"
            f"type: {self.type.value}\n"
            "---"
        )


# Body structure guidance per type (for LLM prompts)
BODY_STRUCTURE = {
    MemoryType.USER: "Profile information: what the user does, their expertise, preferences.",
    MemoryType.FEEDBACK: (
        "Lead with the rule itself, then:\n"
        "**Why:** (the reason -- past incident, strong preference)\n"
        "**How to apply:** (when/where this guidance kicks in)"
    ),
    MemoryType.PROJECT: (
        "Lead with the fact or decision, then:\n"
        "**Why:** (motivation -- constraint, deadline, stakeholder)\n"
        "**How to apply:** (how this shapes suggestions)\n"
        "Always convert relative dates to absolute dates."
    ),
    MemoryType.REFERENCE: "Pointer to external system + its purpose. Include URL if available.",
}
