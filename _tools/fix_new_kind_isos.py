"""Fix new kind builder ISOs: rename wrong names + create missing bld_tools_*.md"""
import re, shutil
from pathlib import Path

ROOT = Path("C:/Users/CEX/Documents/GitHub/cex")
BUILDERS = ROOT / "archetypes" / "builders"

FAILING = [
    "aggregate-root", "alert-rule", "bounded-context", "canary-config",
    "constitutional-rule", "data-contract", "deployment-manifest",
    "domain-event", "domain-vocabulary", "event-stream", "lineage-record",
    "process-manager", "saga", "slo-definition", "value-object",
]

RENAMES = {
    "bld_context_sources_{kind}.md": "bld_config_{kind}.md",
    "bld_rules_{kind}.md": "bld_collaboration_{kind}.md",
}

def kind_from_dir(builder_dir):
    return builder_dir.name.replace("-builder", "").replace("-", "_")

fixed = 0
for builder_slug in FAILING:
    bdir = BUILDERS / f"{builder_slug}-builder"
    kind = builder_slug.replace("-", "_")
    if not bdir.exists():
        print(f"MISSING DIR: {bdir}")
        continue

    # Rename wrong ISO names
    for old_pat, new_pat in RENAMES.items():
        old = bdir / old_pat.replace("{kind}", kind)
        new = bdir / new_pat.replace("{kind}", kind)
        if old.exists() and not new.exists():
            shutil.move(str(old), str(new))
            print(f"RENAMED: {old.name} -> {new.name} [{kind}]")
            fixed += 1
        elif old.exists() and new.exists():
            old.unlink()
            print(f"REMOVED dup: {old.name} [{kind}]")

    # Create bld_tools_{kind}.md if missing
    tools_file = bdir / f"bld_tools_{kind}.md"
    if not tools_file.exists():
        pillar = None
        manifest = bdir / f"bld_manifest_{kind}.md"
        if manifest.exists():
            content = manifest.read_text(encoding="utf-8", errors="ignore")
            m = re.search(r"^pillar:\s*(\S+)", content, re.MULTILINE)
            if m:
                pillar = m.group(1)
        pillar = pillar or "P01"
        tools_file.write_text(
            f"---\nid: bld_tools_{kind}\nkind: knowledge_card\npillar: {pillar}\n"
            f"title: \"{kind.replace('_',' ').title()} Builder -- Tools\"\n"
            f"version: 1.0.0\nquality: null\ntags: [builder, {kind}, tools]\n---\n\n"
            f"# {kind.replace('_',' ').title()} Builder Tools\n\n"
            f"## Primary Tools\n\n"
            f"| Tool | Purpose | When Used |\n"
            f"|------|---------|-----------|\n"
            f"| cex_compile.py | Compile artifact YAML | F8 COLLABORATE |\n"
            f"| cex_doctor.py | Validate builder integrity | F7 GOVERN |\n"
            f"| cex_retriever.py | Find similar artifacts | F5 CALL |\n\n"
            f"## Context Sources\n\n"
            f"- `N00_genesis/P01_knowledge/library/kind/kc_{kind}.md` (primary KC)\n"
            f"- `.cex/kinds_meta.json` (kind boundary definition)\n"
            f"- `archetypes/builders/{kind.replace('_','-')}-builder/` (13 ISOs)\n",
            encoding="utf-8"
        )
        print(f"CREATED: bld_tools_{kind}.md [{kind}]")
        fixed += 1

print(f"\nTotal changes: {fixed}")
