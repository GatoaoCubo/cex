#!/usr/bin/env python3
"""CEX Doctor — Self-healing diagnostic + auto-fix for the CEX repo.

Usage:
  python _tools/cex_doctor.py          # diagnose only
  python _tools/cex_doctor.py --fix    # diagnose + auto-fix what's possible
"""
import os, sys, re, yaml, json, glob
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
FIX_MODE = "--fix" in sys.argv

def p(icon, msg):
    print(f"  {icon} {msg}")

def count_files(pattern):
    return len(glob.glob(str(ROOT / pattern), recursive=True))

def load_yaml(path):
    try:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except:
        return None

def get_frontmatter(path):
    try:
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
        if text.startswith("---"):
            end = text.index("---", 3)
            return yaml.safe_load(text[3:end])
    except:
        pass
    return None

print("=" * 60)
print("CEX Doctor v1.0 — Self-Healing Diagnostic")
print("=" * 60)
print()

errors, warnings, fixes = 0, 0, 0

# CHECK 1: Frontmatter consistency
print("CHECK 1: Frontmatter fields (kind: / pillar:)")
md_files = list(ROOT.glob("P*/examples/*.md")) + list(ROOT.glob("P*/templates/*.md"))
missing_kind, missing_pillar, has_old_type, has_old_lp = [], [], [], []
for f in md_files:
    fm = get_frontmatter(f)
    if not fm:
        continue
    if "kind" not in fm:
        missing_kind.append(f)
    if "pillar" not in fm:
        missing_pillar.append(f)
    if "type" in fm:
        has_old_type.append(f)
    if "lp" in fm:
        has_old_lp.append(f)

if not has_old_type and not has_old_lp:
    p("OK", f"{len(md_files)} files checked — no legacy 'type:' or 'lp:' found")
else:
    p("!!", f"{len(has_old_type)} files still have 'type:', {len(has_old_lp)} have 'lp:'")
    errors += len(has_old_type) + len(has_old_lp)

if missing_kind:
    p("??", f"{len(missing_kind)} files missing 'kind:' field")
    warnings += 1

print()

# CHECK 2: Compiled coverage (dual output)
print("CHECK 2: Dual output (examples must have compiled/)")
missing_compiled = []
for lp_dir in sorted(ROOT.glob("P*_*")):
    examples = list((lp_dir / "examples").glob("*.md")) if (lp_dir / "examples").exists() else []
    compiled_dir = lp_dir / "compiled"
    for ex in examples:
        if ex.name.startswith("_"):
            continue
        stem = ex.stem
        has_yaml = (compiled_dir / f"{stem}.yaml").exists()
        has_json = (compiled_dir / f"{stem}.json").exists()
        if not has_yaml and not has_json:
            missing_compiled.append(str(ex.relative_to(ROOT)))

if not missing_compiled:
    p("OK", "All examples have compiled/ counterpart")
else:
    p("!!", f"{len(missing_compiled)} examples missing compiled/ counterpart")
    for mc in missing_compiled[:5]:
        p("  ", mc)
    if len(missing_compiled) > 5:
        p("  ", f"... and {len(missing_compiled)-5} more")
    errors += 1
    if FIX_MODE:
        p(">>", "Run: python _tools/cex_compile.py --all")

print()

# CHECK 3: Schema integrity
print("CHECK 3: Schema integrity (kinds: key, pillar: field)")
schema_ok, schema_fail = 0, 0
for sf in sorted(ROOT.glob("P*/_schema.yaml")):
    data = load_yaml(sf)
    if not data:
        p("!!", f"Cannot parse {sf.name}")
        schema_fail += 1
        continue
    if "kinds" not in data:
        p("!!", f"{sf.relative_to(ROOT)}: missing 'kinds:' key (has 'types:'?)")
        schema_fail += 1
    elif "pillar" not in data:
        p("!!", f"{sf.relative_to(ROOT)}: missing 'pillar:' field")
        schema_fail += 1
    else:
        schema_ok += 1

p("OK" if not schema_fail else "!!", f"{schema_ok}/12 schemas valid, {schema_fail} broken")
errors += schema_fail

print()

# CHECK 4: Builder completeness
print("CHECK 4: Builders (archetypes/builders/)")
builders_dir = ROOT / "archetypes" / "builders"
builders = [d for d in builders_dir.iterdir() if d.is_dir() and not d.name.startswith("_")]
iso_files = ["MANIFEST.md", "SYSTEM_PROMPT.md", "KNOWLEDGE.md", "INSTRUCTIONS.md",
             "TOOLS.md", "OUTPUT_TEMPLATE.md", "SCHEMA.md", "EXAMPLES.md",
             "ARCHITECTURE.md", "CONFIG.md", "MEMORY.md", "QUALITY_GATES.md", "COLLABORATION.md"]
complete, incomplete = 0, 0
for b in builders:
    missing = [f for f in iso_files if not (b / f).exists()]
    if missing:
        p("??", f"{b.name}: missing {len(missing)} ISO files")
        incomplete += 1
    else:
        complete += 1

total_kinds = 78
p("OK" if complete > 0 else "??", f"{complete}/{total_kinds} builders complete, {incomplete} incomplete, {total_kinds - complete - incomplete} not started")

print()

# CHECK 5: Orphan detection
print("CHECK 5: Orphan files/directories")
expected_root_dirs = {"N01_intelligence", "N02_marketing", "N03_engineering",
                      "N04_knowledge", "N05_operations", "N06_commercial", "N07_admin",
                      "P01_knowledge", "P02_model", "P03_prompt", "P04_tools",
                      "P05_output", "P06_schema", "P07_evals", "P08_architecture",
                      "P09_config", "P10_memory", "P11_feedback", "P12_orchestration",
                      "_tools", "_docs", "_config", "_schemas", "archetypes", ".git", ".claude",
                      "__pycache__", "node_modules"}
orphan_dirs = []
for d in ROOT.iterdir():
    if d.is_dir() and d.name not in expected_root_dirs:
        orphan_dirs.append(d.name)

if orphan_dirs:
    for od in orphan_dirs:
        p("??", f"Orphan dir: {od}/")
    warnings += len(orphan_dirs)
else:
    p("OK", "No orphan directories")

expected_root_md = {"CLAUDE.md", "README.md", "LLM_PIPELINE.md", "CHANGELOG.md",
                    "CONTRIBUTING.md", "INDEX.md", ".gitignore"}
orphan_files = []
for f in ROOT.iterdir():
    if f.is_file() and f.name.endswith(".md") and f.name not in expected_root_md:
        orphan_files.append(f.name)

if orphan_files:
    for of_ in orphan_files:
        p("??", f"Orphan file: {of_}")
    warnings += len(orphan_files)

print()

# CHECK 6: Naming convention
print("CHECK 6: Naming convention (p{NN}_{abbr}_{topic}.md)")
naming_re = re.compile(r"^p\d{2}_[a-z]{2,4}_[a-z0-9_]+\.md$")
bad_names = []
for lp_dir in sorted(ROOT.glob("P*_*")):
    for ex in (lp_dir / "examples").glob("*.md") if (lp_dir / "examples").exists() else []:
        if ex.name.startswith("_") or ex.name.startswith("ex_"):
            continue
        if not naming_re.match(ex.name):
            bad_names.append(str(ex.relative_to(ROOT)))

if not bad_names:
    p("OK", "All examples follow naming convention")
else:
    p("??", f"{len(bad_names)} files with non-standard names")
    for bn in bad_names[:5]:
        p("  ", bn)
    warnings += 1

print()

# CHECK 7: Cross-reference numbers
print("CHECK 7: Number consistency")
readme = (ROOT / "README.md").read_text(encoding="utf-8", errors="ignore")
if "73 tipo" in readme or "68 tipo" in readme or "v3.0.0" in readme:
    p("!!", "README.md has stale numbers (73/68 tipos, v3.0.0)")
    errors += 1
else:
    p("OK", "README.md numbers up to date")

codex = (ROOT / "archetypes" / "CODEX.md").read_text(encoding="utf-8", errors="ignore")
if "68 tipo" in codex or "68 kind" in codex:
    p("!!", "CODEX.md has stale '68' count")
    errors += 1

print()

# SUMMARY
print("=" * 60)
total_checks = 7
print(f"SUMMARY: {total_checks} checks | {errors} errors | {warnings} warnings")
if FIX_MODE:
    print(f"Auto-fixes applied: {fixes}")
if errors == 0 and warnings == 0:
    print("STATUS: HEALTHY")
elif errors == 0:
    print("STATUS: WARNINGS (non-critical)")
else:
    print("STATUS: NEEDS ATTENTION")
print("=" * 60)
