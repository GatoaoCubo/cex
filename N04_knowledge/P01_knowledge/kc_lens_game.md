---
quality: 9.1
quality: 7.9
id: kc_lens_game
kind: knowledge_card
kc_type: meta_kc
pillar: P01
nucleus: n04
version: 1.0.0
created: "2026-04-19"
updated: "2026-04-19"
author: n04_knowledge
title: "Lens: Game -- CEX as a Tabletop/Video Game World"
domain: didactic_engine
subdomain: lens_system
tags: [lens, game, rpg, metaphor, teaching, mentor, didactic, analogy]
tldr: "Complete mapping of CEX concepts to a game (RPG/tabletop/video) metaphor. 8F=quest stages, nuclei=character classes, kinds=item types, N07=dungeon master. Expands the existing spec_metaphor_dictionary game architecture section. For /mentor teaching to gamers and creative audiences."
density_score: null
related:
  - n07_memory_terminology
  - ctx_cex_new_dev_guide
  - n07_taught_terms_registry
  - spec_metaphor_dictionary
  - p03_sp_cex_core_identity
  - p10_out_swot_analysis
  - p03_sp_knowledge_card_builder
  - report_intent_resolution_value_prop
---

# Lens: Game

> Every CEX concept has a game equivalent. This lens expands the existing game metaphors from spec_metaphor_dictionary.md into a full RPG/tabletop/video game world. Use it with gamers, creative builders, and anyone who thinks in quests, characters, and loot.

## Core Mapping (expanded from spec_metaphor_dictionary)

| CEX Concept | Game Metaphor | One-line Explanation |
|-------------|--------------|---------------------|
| CEX system | The game world | The entire universe: zones, quests, NPCs, items, mechanics |
| 8F pipeline | Quest execution flow | 8 mandatory stages every quest passes through from acceptance to completion |
| 12 pillars | Game world zones / biomes | Each zone has its own rules, resources, and quest types |
| nucleus | Character class | Fighter, Mage, Rogue... each class has a unique skill tree and cannot use all items |
| N07 orchestrator | Dungeon Master / Game Master | Designs the world, assigns quests, never plays a character |
| kind | Item type / item schema | "Sword, Shield, Potion" -- defines what an item IS, not a specific weapon instance |
| builder | Crafting station | Each station specializes in one item type; a forge makes weapons, not potions |
| ISO | Crafting recipe card | The 12 recipe steps loaded into a crafting station for one specific item type |
| artifact | Crafted item (in inventory) | The actual sword that now exists and can be equipped or used |
| GDP | Pre-quest dialogue | "Do you want to save the village or find the treasure?" -- player decides goal before quest starts |
| sin lens | Character alignment / motivation | Lawful Envy, Chaotic Lust, Neutral Greed... each class plays differently |
| quality gate (F7) | Item quality check (common/rare/legendary) | Crafted item is inspected: below green quality = scrap, try again (max 2 retries) |
| signal (F8) | Quest complete notification | The "QUEST COMPLETE" banner + XP reward sent to Game Master's log |
| handoff | Quest briefing scroll | The detailed quest scroll the GM writes and gives to each character |
| dispatch | Quest board posting | GM pins the quest; character accepts it and starts |
| wave | Dungeon floor / act | Floor 1 cleared before Floor 2 unlocks -- waves gate progress |
| grid | Party split (dungeon run) | Party splits into 6 groups, each clearing a different room simultaneously |
| RAG | Inventory check + loot pickup | Before crafting, verify required materials are in inventory; gather what's missing |

## Existing Metaphors (from spec_metaphor_dictionary -- maintained here for completeness)

| User says | Game meaning | CEX meaning |
|-----------|-------------|------------|
| card | item card | artifact (.md file) |
| deck (file) | character sheet | agent card |
| deck (concept) | hand of cards | context assembly |
| hand | cards currently held | working context |
| draw | drawing a card | F3 INJECT (retrieval) |
| play | playing a card | F6 PRODUCE (generation) |
| round | one game turn | 8F pipeline run |
| table | game table | grid dispatch |
| dealer | dealer | N07 orchestrator |
| slot | card slot / variable | template variable |
| combo | card combo | prompt composition |
| library | card library | CEX repository |

## Extended Mapping: Top 20 Kinds

| Kind | Game Metaphor | Teaching Story Seed |
|------|--------------|---------------------|
| `knowledge_card` | Lore scroll / encyclopedia entry | "The tavern keeper's lore book: every known fact, indexed by topic and location" |
| `agent` | Character profile (character sheet) | "Name, class, stats, special abilities, what they CAN and CANNOT equip" |
| `prompt_template` | Spell scroll (template) | "One scroll you can cast many times with different targets: Fireball hits anyone" |
| `system_prompt` | Character backstory + alignment | "Defines who the character IS: their code, their oath, their limits" |
| `workflow` | Quest sequence / story arc | "Main quest: talk to blacksmith -> retrieve ore -> forge sword -> return: locked sequence" |
| `quality_gate` | Item quality inspection | "Gray = garbage, Green = common, Blue = rare, Purple = epic. Below green: scrap it." |
| `knowledge_index` | World map with legend | "Every zone mapped, every chest marked, every NPC cataloged with their quests" |
| `embedding_config` | Search mechanic (fuzzy matching loot) | "How the game engine matches 'find sword' to all sword-type items nearby" |
| `guardrail` | Zone restriction (level gate) | "You must be level 20 to enter this dungeon. Rule enforced by the game engine, not the player." |
| `env_config` | World settings / game rules | "Starting gold, respawn timer, max party size -- the rules of the game world" |
| `api_client` | NPC vendor / trade route | "The merchant who connects this town to the external economy (external API)" |
| `learning_record` | Achievement log | "A permanent record of every dungeon cleared, every skill learned, every mistake made" |
| `entity_memory` | NPC relationship tracker | "Quest givers remember if you helped or betrayed them; affects future quests" |
| `crew_template` | Party composition blueprint | "Healer + Tank + DPS + Scout: defined roles, defined handoffs, defined victory condition" |
| `decision_record` | Dialogue choice archive | "Every major choice the party made, saved to the game log with timestamp and consequence" |
| `benchmark` | Speed run leaderboard criteria | "The exact rules for what counts as a valid speed run for this dungeon" |
| `context_doc` | Quest briefing (before dungeon entry) | "The lore dump before the final boss: what you NEED to know to understand what follows" |
| `chain` | Combo system | "Attack -> stagger -> critical strike -> execute: each move triggers the next automatically" |
| `router` | Guild assignment system | "Incoming quest requests automatically routed to the correct character class" |
| `scoring_rubric` | Judge's scorecard (PvP tournament) | "The exact criteria: execution speed, accuracy, creativity -- each weighted" |

## 8F as Quest Execution Flow

| Quest Stage | 8F Step | What the player does |
|------------|---------|---------------------|
| Accept quest | F1 CONSTRAIN | Read the quest scroll: confirm item type, zone, constraints, rewards |
| Character prep | F2 BECOME | Equip correct gear, load relevant spell set, read class abilities for this quest type |
| Gather materials | F3 INJECT | Collect required crafting materials: KCs, examples, lore scrolls, party memory |
| Plan approach | F4 REASON | Review the dungeon map: how many rooms, which order, estimated time |
| Check inventory | F5 CALL | Verify all tools equipped: compiler wand, linter staff, index compass |
| Craft the item | F6 PRODUCE | Approach the crafting station, execute the recipe, produce the artifact |
| Quality check | F7 GOVERN | Appraise the item: 7 quality checkpoints. Below green quality = destroy and retry. |
| Turn in quest | F8 COLLABORATE | Deliver the item, collect XP, update quest log, notify GM. |

## 12 Pillars as Game World Zones

| Zone | Pillar | What you find there |
|------|--------|-------------------|
| Ancient Library (lore vault) | P01 | All knowledge scrolls, lore books, search indexing |
| Character Creation Chamber | P02 | Agent profiles, class definitions, ability trees |
| Arcane Workshop (spellcrafting) | P03 | Spell templates, prompt scrolls, action prompts |
| Tool Forge (weapons + gadgets) | P04 | External tools, API weapons, CLI daggers |
| Trophy Room (output gallery) | P05 | Completed artifacts, landing pages, diagrams |
| Contract Hall (legal + schemas) | P06 | Data contracts, interface specs, type definitions |
| Proving Grounds (testing) | P07 | Benchmarks, scoring, evaluation arenas |
| Architect's Tower (design) | P08 | System diagrams, decision records, naming scrolls |
| Utility Vault (config + secrets) | P09 | Environment settings, rate limits, secret keys |
| Memory Palace (state + history) | P10 | Entity memories, session state, knowledge index |
| Feedback Chamber (learning) | P11 | Quality signals, bug reports, improvement loops |
| Command Center (orchestration) | P12 | Quest board, dispatch orders, crew scheduling |

## 8 Nuclei as Character Classes

| Class | Nucleus | Sin Lens (Motivation) | Specialty |
|-------|---------|----------------------|---------|
| Scholar / Intelligence Agent | N01 | Analytical Envy | Researches everything, publishes intelligence |
| Bard / Marketing Agent | N02 | Creative Lust | Crafts persuasive content, manages brand voice |
| Artificer / Builder | N03 | Inventive Pride | Crafts the actual artifacts (never delegates) |
| Sage / Knowledge Keeper | N04 | Knowledge Gluttony | Indexes all lore, answers any question instantly |
| Paladin / QA Enforcer | N05 | Gating Wrath | Tests deployments, blocks bad code, enforces law |
| Merchant / Commercial Agent | N06 | Strategic Greed | Monetizes, prices, builds revenue structures |
| Dungeon Master / Orchestrator | N07 | Orchestrating Sloth | Designs quests, never enters the dungeon |
| Ancestor / Genesis Template | N00 | Pre-sin archetype | The primordial class template all others derived from |

## Discovery Questions (Socratic Seeds)

1. A Dungeon Master (N07) who starts playing their own character stops running the game. In CEX, if N07 builds an artifact directly, what breaks and why?
2. Every character class (nucleus) has the same 8 quest stages (8F), but their specializations are completely different. How does the "same pipeline, different content" principle apply in a crafting system you know?
3. When a crafted item fails quality inspection (F7), it goes back to the crafting station for one more try (max 2). What game mechanic does this most resemble, and why is there a maximum retry limit?
4. The Dungeon Master writes a quest scroll (handoff) that includes everything a character needs: zone, materials, victory condition. Why is it critical that the scroll be complete BEFORE the character starts, rather than asking questions mid-dungeon?
5. In a party split (grid dispatch), 6 characters clear 6 rooms simultaneously. What coordination mechanism ensures they all finish before the final boss room unlocks (wave gate)?

## Quick Reference

```yaml
topic: game_lens
scope: CEX to RPG/tabletop/video game metaphor translation
owner: n04_knowledge
criticality: high
audience: non_dev_solo_builders
lens: game
covers: 8F_pipeline, 12_pillars, 8_nuclei, top_20_kinds
extends: spec_metaphor_dictionary_game_architecture_section
```

## Sources

- CEX spec_metaphor_dictionary.md: existing game architecture metaphors (canonical source)
- CEX CLAUDE.md: nucleus definitions, 8F pipeline, pillar structure
- RPG mechanics: D&D 5e class/skill system, WoW item quality tiers, crafting station pattern
- Party composition: CrewAI role model (https://docs.crewai.com)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n07_memory_terminology]] | downstream | 0.20 |
| [[ctx_cex_new_dev_guide]] | related | 0.18 |
| [[n07_taught_terms_registry]] | downstream | 0.18 |
| [[spec_metaphor_dictionary]] | related | 0.18 |
| [[p03_sp_cex_core_identity]] | downstream | 0.16 |
| [[p10_out_swot_analysis]] | downstream | 0.16 |
| [[p03_sp_knowledge_card_builder]] | downstream | 0.16 |
| [[report_intent_resolution_value_prop]] | related | 0.16 |
