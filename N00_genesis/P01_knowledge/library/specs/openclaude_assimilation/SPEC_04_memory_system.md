---
id: spec_04_memory_system
kind: spec
pillar: P01
title: "SPEC_04: Memory Aging/Relevance → cex_memory"
version: 1.0.0
status: active
created: 2026-04-05
quality: 9.0
depends_on: []
target_files:
  - _tools/cex_memory_select.py
  - _tools/cex_memory_update.py
  - _tools/cex_memory_age.py (NEW)
  - _tools/cex_memory_types.py (NEW)
---

# SPEC_04: Memory Aging/Relevance → cex_memory

## Pattern Harvested

OpenClaude's memdir system is a **4-type, age-aware, LLM-selected memory** with:
- Structured taxonomy (user, feedback, project, reference)
- Freshness-aware recall with staleness caveats
- Background extraction (auto-save observations)
- Memory drift detection (verify before asserting)

### Memory Type Taxonomy (from memoryTypes.ts)

```pseudocode
TYPES = ["user", "feedback", "project", "reference"]

user:      role, goals, preferences → slow decay, private
feedback:  corrections + confirmations → NO decay, permanent
project:   ongoing work, deadlines → fast decay, convert relative dates
reference: external system pointers → moderate decay

# Critical: record from FAILURE *and* SUCCESS
# "If you only save corrections, you drift away from validated approaches"
```

### Memory Aging (from memoryAge.ts)

```pseudocode
function memoryAgeDays(mtime_ms):
    return max(0, floor((now() - mtime_ms) / 86_400_000))

function memoryAge(mtime_ms) -> str:
    days = memoryAgeDays(mtime_ms)
    if days == 0: return "today"
    if days == 1: return "yesterday"
    return f"{days} days ago"

function memoryFreshnessText(mtime_ms) -> str:
    days = memoryAgeDays(mtime_ms)
    if days <= 1: return ""  # No warning for fresh memories
    return (
        f"This memory is {days} days old. "
        "Memories are point-in-time observations, not live state — "
        "claims about code behavior may be outdated. "
        "Verify against current state before asserting as fact."
    )
```

### LLM-Selected Recall (from findRelevantMemories.ts)

```pseudocode
# 1. Scan directory for .md files
headers = scanMemoryFiles(dir)  # Returns: filename, mtime, description, type

# 2. Format as manifest
manifest = headers.map(h => f"- [{h.type}] {h.filename} ({h.timestamp}): {h.description}")

# 3. LLM selects top-5 relevant
selected = sideQuery(
    model=sonnet,
    system="You are selecting memories useful for processing a user's query...",
    user=f"Query: {query}\n\nAvailable memories:\n{manifest}",
    max_tokens=256,
    output_format=json_schema({selected_memories: [string]})
)

# 4. Filter recently-used tools (avoid re-surfacing active knowledge)
# 5. Filter already-surfaced (avoid re-picking across turns)
```

### Key Anti-Patterns

```
WHAT NOT TO SAVE:
- Code patterns (derivable from grep)
- Git history (derivable from git log)  
- Debugging solutions (the fix is in the code)
- Anything in CLAUDE.md
- Ephemeral task details

BEFORE RECOMMENDING FROM MEMORY:
- If names a file path → check it exists
- If names a function → grep for it
- "The memory says X exists" ≠ "X exists now"
```

## CEX Adaptation

### What Changes

| Component | Current CEX | After |
|-----------|-------------|-------|
| Memory types | Untyped observations | 4-type taxonomy (user/feedback/project/reference) |
| Aging | Binary decay rate per type | Human-readable age + staleness caveats |
| Selection | Keyword + LLM (basic) | Manifest-based LLM selection (structured) |
| Anti-patterns | Not enforced | Save-guard + recall-guard |
| What-not-to-save | Not defined | Explicit exclusion list |

### New: `_tools/cex_memory_types.py`

```python
"""CEX Memory Types — 4-type taxonomy with decay rates."""

from enum import Enum
from dataclasses import dataclass

class MemoryType(str, Enum):
    USER = "user"           # Role, goals, preferences
    FEEDBACK = "feedback"   # Corrections + confirmations (permanent)
    PROJECT = "project"     # Ongoing work, deadlines (fast decay)
    REFERENCE = "reference" # External system pointers

# Decay rates per update cycle
DECAY_RATES = {
    MemoryType.USER: 0.02,
    MemoryType.FEEDBACK: 0.00,     # PERMANENT — never decay
    MemoryType.PROJECT: 0.05,
    MemoryType.REFERENCE: 0.03,
}

# What NOT to save (rejection patterns)
SAVE_EXCLUSIONS = [
    "code pattern",
    "git history",
    "debugging solution",
    "file structure",
    "architecture",
]

def should_save(observation: str, existing_claudemd: str = "") -> tuple[bool, str]:
    """Guard: reject observations that belong in code, not memory."""
    obs_lower = observation.lower()
    
    for exclusion in SAVE_EXCLUSIONS:
        if exclusion in obs_lower:
            return False, f"Rejected: '{exclusion}' is derivable, not memory-worthy"
    
    if existing_claudemd and observation.strip() in existing_claudemd:
        return False, "Rejected: already documented in CLAUDE.md"
    
    return True, "OK"

@dataclass
class MemoryFrontmatter:
    """Required frontmatter for memory files."""
    name: str
    description: str   # Used for relevance matching
    type: MemoryType
    
    def to_yaml(self) -> str:
        return f"""---
name: {self.name}
description: {self.description}
type: {self.type.value}
---"""
```

### New: `_tools/cex_memory_age.py`

```python
"""CEX Memory Aging — human-readable freshness + staleness caveats."""

import time
from pathlib import Path

def memory_age_days(mtime: float) -> int:
    """Days since memory was last modified. 0 = today."""
    return max(0, int((time.time() - mtime) / 86400))

def memory_age_label(mtime: float) -> str:
    """Human-readable age: 'today', 'yesterday', '47 days ago'."""
    days = memory_age_days(mtime)
    if days == 0:
        return "today"
    if days == 1:
        return "yesterday"
    return f"{days} days ago"

def memory_freshness_caveat(mtime: float) -> str:
    """Staleness warning for memories >1 day old. Empty for fresh."""
    days = memory_age_days(mtime)
    if days <= 1:
        return ""
    return (
        f"⚠ This memory is {days} days old. "
        "It is a point-in-time observation, not live state. "
        "Claims about file paths, function names, or behavior may be outdated. "
        "Verify against current code before asserting as fact."
    )

def format_memory_manifest(memories: list[dict]) -> str:
    """Format memory headers as selectable manifest.
    
    Each entry: - [type] filename (age): description
    """
    lines = []
    for m in memories:
        tag = f"[{m['type']}] " if m.get('type') else ""
        age = memory_age_label(m.get('mtime', 0))
        desc = m.get('description', '')
        line = f"- {tag}{m['filename']} ({age})"
        if desc:
            line += f": {desc}"
        lines.append(line)
    return "\n".join(lines)
```

### Modified: `_tools/cex_memory_select.py`

Upgrade LLM selection to use manifest format + staleness:

```python
# Replace flat keyword matching with manifest-based selection

SELECTOR_SYSTEM_PROMPT = """You are selecting memories useful for a CEX builder.
Return filenames for memories that will clearly help process this task (up to 5).
- Be selective: only include clearly relevant memories.
- If recently-used builders are listed, skip their reference docs (already loaded).
- DO include warnings/gotchas about those builders.
If nothing is clearly relevant, return an empty list."""

def select_memories_structured(query: str, memories: list[MemoryHeader],
                                recent_builders: list[str] = []) -> list[str]:
    """LLM-powered memory selection using manifest format."""
    manifest = format_memory_manifest([
        {"filename": m.filename, "type": m.type, 
         "mtime": m.mtime, "description": m.description}
        for m in memories
    ])
    
    builders_note = ""
    if recent_builders:
        builders_note = f"\n\nRecently active builders: {', '.join(recent_builders)}"
    
    prompt = f"Task: {query}\n\nAvailable memories:\n{manifest}{builders_note}"
    
    # Call LLM for selection (existing pattern, upgraded prompt)
    result = call_llm_selector(SELECTOR_SYSTEM_PROMPT, prompt)
    return result.get("selected_memories", [])
```

### Modified: `_tools/cex_memory_update.py`

Add save-guard + feedback confirmation tracking:

```python
# Add to existing update flow

def record_observation(builder_id, obs_type, observation, **kwargs):
    """Record observation with save-guard."""
    from cex_memory_types import should_save, MemoryType
    
    # Guard: reject non-memory-worthy observations
    ok, reason = should_save(observation)
    if not ok:
        return {"status": "rejected", "reason": reason}
    
    # Record BOTH corrections AND confirmations
    # "If you only save corrections, you drift from validated approaches"
    if obs_type == "feedback" and kwargs.get("outcome") == "SUCCESS":
        kwargs["note"] = "Confirmed approach — keep doing this"
    
    # Proceed with existing save logic...
    return _save_observation(builder_id, obs_type, observation, **kwargs)
```

## Acceptance Criteria

1. ✅ 4-type taxonomy (user/feedback/project/reference) replaces untyped
2. ✅ Human-readable age labels ("47 days ago" not ISO timestamp)
3. ✅ Staleness caveats injected for memories >1 day old
4. ✅ Save-guard rejects code patterns, git history, etc.
5. ✅ Feedback type records confirmations (not just corrections)
6. ✅ Manifest-based LLM selection replaces flat keyword matching
7. ✅ Backward compatible: existing memory files still load
8. ✅ `format_memory_manifest()` used by both select and coordinator

## 8F Impact

- **F3 INJECT**: Smarter memory selection = higher relevance, less noise
- **F7 GOVERN**: Memory age included in quality assessment
- **F2 BECOME**: Builder memories now typed — feedback is permanent
