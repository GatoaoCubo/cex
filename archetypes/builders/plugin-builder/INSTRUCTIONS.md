---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for plugin artifact
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a plugin

## Phase 1: RESEARCH
1. Identify the interface contract the plugin implements
2. Define the API surface (methods, inputs, outputs)
3. Determine dependencies on other plugins or systems
4. Select isolation level (sandboxed, shared, privileged)
5. Determine lifecycle events (minimum: on_load, on_unload)
6. Design configuration schema with defaults
7. Search for existing plugins via brain_query [IF MCP] (avoid duplicates)
8. Determine version constraints for host compatibility
9. Evaluate hot-reload capability (requires on_config_change lifecycle)
10. Plan testing strategy (unit, integration, mocks)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Generate plugin_slug in snake_case (e.g., metrics_exporter)
4. Fill frontmatter: all 16 required fields (quality: null, never self-score)
5. Set interface to contract name
6. Set lifecycle with at least [on_load, on_unload]
7. Set api_surface_count to match methods in table
8. Write Interface Contract section: contract description and required methods
9. Write API Surface section: table with method, input, output, description
10. Write Configuration section: config schema with types and defaults
11. Write Lifecycle Hooks section: behavior for each lifecycle event
12. Write Dependencies section: required plugins with version constraints
13. Write Testing section: unit, integration, mock strategies
14. Check body <= 2048 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. Verify all 9 HARD gates pass
3. Score each SOFT gate against QUALITY_GATES.md
4. Confirm id matches p04_plug_ pattern
5. Confirm kind == plugin
6. Confirm quality == null
7. Confirm api_surface_count matches methods in table
8. Confirm lifecycle contains at least [on_load, on_unload]
9. Confirm dependencies use artifact IDs or system names
10. If hot_reload: true, confirm on_config_change in lifecycle
11. If score < 8.0: revise before outputting
