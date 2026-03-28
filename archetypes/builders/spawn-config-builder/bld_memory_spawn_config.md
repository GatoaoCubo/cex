---
kind: memory
id: bld_memory_spawn_config
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for spawn_config artifact generation
---

# Memory: spawn-config-builder

## Summary

Spawn configs define how autonomous satellites are launched: CLI flags, MCP profiles, timeout policies, and handoff file references. The critical production lesson is prompt size limits — inline prompts exceeding 200 characters cause hangs in non-interactive mode. Complex task descriptions must be offloaded to handoff files referenced by the spawn config. The second lesson is MCP profile isolation: satellites sharing MCP configs cause connection conflicts when spawned concurrently.

## Pattern

- Keep inline prompts under 200 characters — offload complex instructions to handoff files
- Each satellite must have its own MCP config file — shared configs cause connection conflicts in parallel spawns
- Timeout policies must cover both task execution and idle detection — satellites without idle timeout hang indefinitely
- Interactive mode flag must be explicitly set: interactive (keeps terminal open) or batch (closes on completion)
- Spawn delay between concurrent satellites should be 3-5 seconds — simultaneous spawns cause resource contention
- Include workspace trust handling: non-interactive mode requires explicit trust bypass flag

## Anti-Pattern

- Inline prompts exceeding 200 characters — non-interactive mode hangs waiting for truncated input
- Shared MCP config across concurrent satellites — connection conflicts cause silent tool failures
- Missing idle timeout — satellite finishes tasks but terminal stays open consuming resources indefinitely
- Spawning more than 3 concurrent satellites without delay — causes memory exhaustion and system instability
- Confusing spawn_config (P12, launch parameters) with signal (P12, status event) or workflow (P12, multi-step orchestration)
- Absolute paths in MCP config that differ across machines — config fails on any machine except the original

## Context

Spawn configs operate in the P12 orchestration layer. They are consumed by PowerShell spawn scripts that create terminal processes for each satellite. In production, spawn configs enable automated satellite deployment in solo (single satellite), grid (multiple parallel), and continuous (queue-based refill) modes. The key constraint is that each spawned satellite is an independent process with its own resources.

## Impact

Prompt size enforcement (under 200 characters) eliminated 100% of non-interactive mode hangs. Per-satellite MCP profiles eliminated all concurrent connection conflicts. Idle timeout policies recovered 100% of zombie satellite processes within configured windows.

## Reproducibility

Reliable spawn config production: (1) define satellite-model pairing, (2) create isolated MCP config file, (3) keep inline prompt under 200 chars with handoff file reference, (4) set interactive/batch mode explicitly, (5) configure task and idle timeouts, (6) set spawn delay for concurrent launches, (7) handle workspace trust bypass, (8) validate against 8 HARD + 8 SOFT gates.

## References

- spawn-config-builder SCHEMA.md (19 frontmatter fields)
- P12 orchestration pillar specification
- Process management and satellite lifecycle patterns
