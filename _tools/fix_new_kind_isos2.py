"""Fix remaining doctor issues: remove bld_scoring_rubric + densify bld_tools."""
import re
from pathlib import Path

ROOT = Path("C:/Users/CEX/Documents/GitHub/cex")
BUILDERS = ROOT / "archetypes" / "builders"

FAILING = [
    "aggregate-root", "alert-rule", "bounded-context", "canary-config",
    "constitutional-rule", "data-contract", "deployment-manifest",
    "domain-event", "domain-vocabulary", "event-stream", "lineage-record",
    "process-manager", "saga", "slo-definition", "value-object",
]

KIND_META = {
    "aggregate_root":      ("P06", "DDD entry point entity that enforces invariants", "N03", "domain model entity"),
    "alert_rule":          ("P09", "Observable threshold condition triggering notification", "N05", "monitoring observability"),
    "bounded_context":     ("P08", "Explicit DDD boundary where a model applies", "N03", "domain architecture"),
    "canary_config":       ("P09", "Gradual traffic rollout with automatic rollback", "N05", "deployment resilience"),
    "constitutional_rule": ("P11", "Absolute agent behavioral constraint, non-overridable", "N07", "safety alignment"),
    "data_contract":       ("P06", "Schema agreement between producer and consumer", "N03", "data governance"),
    "deployment_manifest": ("P09", "Artifact deploy specification for an environment", "N05", "release management"),
    "domain_event":        ("P12", "Immutable record of a significant domain occurrence", "N03", "event-driven architecture"),
    "domain_vocabulary":   ("P01", "Governed canonical term registry for a bounded context", "N04", "ubiquitous language"),
    "event_stream":        ("P04", "Real-time ordered event sequence configuration", "N05", "streaming infrastructure"),
    "lineage_record":      ("P01", "Provenance chain of a knowledge artifact derivation", "N04", "data lineage"),
    "process_manager":     ("P12", "Event-driven multi-step process coordinator", "N07", "distributed orchestration"),
    "saga":                ("P12", "Distributed transaction with compensating actions", "N07", "distributed systems"),
    "slo_definition":      ("P09", "Measurable service level objective with error budget", "N05", "SRE reliability"),
    "value_object":        ("P06", "Immutable typed value defined by attributes alone", "N03", "domain model type"),
}

def make_tools_content(kind, pillar, desc, nucleus, domain):
    title = kind.replace("_", " ").title()
    hyphen = kind.replace("_", "-")
    return (
        f"---\n"
        f"id: bld_tools_{kind}\n"
        f"kind: knowledge_card\n"
        f"pillar: {pillar}\n"
        f"title: \"{title} Builder -- Tools\"\n"
        f"version: 1.0.0\n"
        f"quality: null\n"
        f"tags: [builder, {kind}, tools]\n"
        f"---\n\n"
        f"# {title} Builder -- Tools\n\n"
        f"Builder domain: {domain}. Primary nucleus: {nucleus}.\n\n"
        f"## Runtime Tools\n\n"
        f"| Tool | Function | Stage |\n"
        f"|------|----------|-------|\n"
        f"| `cex_compile.py {{path}}` | Compile artifact to YAML | F8 COLLABORATE |\n"
        f"| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |\n"
        f"| `cex_retriever.py --query {{intent}}` | Find similar {kind} artifacts | F5 CALL |\n"
        f"| `cex_score.py {{path}}` | Peer-review quality scoring | F7 GOVERN |\n"
        f"| `cex_hooks.py validate {{path}}` | Frontmatter + field validation | F7 GOVERN |\n\n"
        f"## Context Sources\n\n"
        f"| Source | Content | Stage |\n"
        f"|--------|---------|-------|\n"
        f"| `N00_genesis/P01_knowledge/library/kind/kc_{kind}.md` | Primary domain KC | F3 INJECT |\n"
        f"| `.cex/kinds_meta.json` (key: `{kind}`) | Boundary, pillar, naming | F1 CONSTRAIN |\n"
        f"| `archetypes/builders/{hyphen}-builder/bld_examples_{kind}.md` | Reference examples | F3 INJECT |\n"
        f"| `archetypes/builders/{hyphen}-builder/bld_schema_{kind}.md` | Output schema | F2 BECOME |\n\n"
        f"## Discovery\n\n"
        f"```bash\n"
        f"# Find existing {kind} artifacts\n"
        f"python _tools/cex_retriever.py --query \"{desc}\"\n\n"
        f"# Validate a new artifact\n"
        f"python _tools/cex_hooks.py validate path/to/artifact.md\n\n"
        f"# Compile after writing\n"
        f"python _tools/cex_compile.py path/to/artifact.md\n"
        f"```\n"
    )

removed = created = 0

for builder_slug in FAILING:
    kind = builder_slug.replace("-", "_")
    bdir = BUILDERS / f"{builder_slug}-builder"
    if not bdir.exists():
        print(f"SKIP (no dir): {kind}")
        continue

    # Remove bld_scoring_rubric
    rubric = bdir / f"bld_scoring_rubric_{kind}.md"
    if rubric.exists():
        rubric.unlink()
        print(f"REMOVED: bld_scoring_rubric_{kind}.md")
        removed += 1

    # Densify bld_tools
    pillar, desc, nucleus, domain = KIND_META.get(kind, ("P01", kind, "N03", "general"))
    tools_file = bdir / f"bld_tools_{kind}.md"
    tools_file.write_text(make_tools_content(kind, pillar, desc, nucleus, domain), encoding="utf-8")
    print(f"DENSIFIED: bld_tools_{kind}.md")
    created += 1

print(f"\nRemoved: {removed} | Densified: {created}")
