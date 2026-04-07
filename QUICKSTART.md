# CEX Quickstart (5 minutes)

## Prerequisites

- Python 3.10+
- Git
- One of: Claude Code CLI, Gemini CLI, or Ollama (for local)

## 1. Clone and install

```bash
git clone https://github.com/user/cex.git
cd cex
pip install -r requirements.txt
```

## 2. Set up your API key

```bash
cp .env.example .env
# Edit .env and add at least one API key:
# ANTHROPIC_API_KEY=sk-ant-...    (for Claude)
# or install Ollama for free local models
```

## 3. Bootstrap your brand

```bash
python _tools/cex_bootstrap.py
```

Answer ~6 questions: company name, domain, product, audience, tone, archetype.
This generates your brand config and propagates it to all nuclei.

**Alternative**: In any Claude session with CEX loaded, just type `/init`.

## 4. Verify system health

```bash
python _tools/cex_doctor.py          # Builder integrity
python _tools/cex_hooks.py validate-all  # Frontmatter validation
python _tools/cex_flywheel_audit.py audit  # Full system audit
```

Expected: 0 FAIL on doctor, 0 Errors on hooks, 100% WIRED on audit.

## 5. Build your first artifact

```bash
# Dry run (no LLM cost, shows pipeline)
python _tools/cex_8f_runner.py "create knowledge card about our product" \
  --kind knowledge_card --dry-run --verbose

# Real build (requires API key or Ollama)
python _tools/cex_8f_runner.py "create knowledge card about our product" \
  --kind knowledge_card --execute
```

## 6. Compile and export

```bash
# Compile all .md to .yaml
python _tools/cex_compile.py --all

# Export to CLAUDE.md format
python _tools/cex_compile.py --target claude-md --output CLAUDE_GENERATED.md
```

## What next?

| Goal | Command |
|------|---------|
| Build multiple artifacts at once | `python _tools/cex_mission.py "launch product X"` |
| Check model versions | `python _tools/cex_model_updater.py --check` |
| Autonomous improvement | `python _tools/cex_auto.py cycle --max 5` |
| Launch multi-nucleus grid | `bash _spawn/dispatch.sh grid MISSION_NAME` |
| Full system diagnostic | `python _tools/cex_system_test.py --quick` |

## Folder map

```
You edit:        .cex/config/nucleus_models.yaml  (which LLM per nucleus)
                 .cex/brand/brand_config.yaml      (your brand identity)
                 .env                               (API keys)

CEX manages:     archetypes/builders/   (109 builder factories)
                 P01-P12_*/            (12 knowledge pillars)
                 N01-N07_*/            (7 business nuclei)
                 _tools/               (51 CLI tools)
```
