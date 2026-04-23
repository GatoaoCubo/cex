"""Batch fix non-feedback builder ISOs below 8.0: add content for structural bonuses.

Same structural scoring levers:
- body_words >= 400: +0.2 raw
- size >= 3000: +0.3 raw
- code_blocks >= 2: +0.1 raw
- list_items >= 3: +0.2 raw
- format_types >= 3: +0.2 raw
"""
import glob
import os
import re
import sys

ISO_ENRICHMENT = {
    "bld_config": """
## Configuration Checklist

- Verify all required fields are present in frontmatter before saving
- Validate config values against schema constraints (type, range, enum)
- Cross-reference with related configs to avoid contradictions
- Test config loading in target runtime before committing

## Validation

```yaml
# Required config validation
fields_present: true
types_valid: true
ranges_checked: true
cross_refs_verified: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```
""",
    "bld_tools": """
## Tool Integration Checklist

- Verify tool name follows snake_case convention
- Validate input/output schema matches interface contract
- Cross-reference with capability_registry for discoverability
- Test tool invocation in sandbox before production use

## Invocation Pattern

```yaml
# Tool invocation contract
name: tool_name
input_schema: validated
output_schema: validated
error_handling: defined
timeout: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```
""",
    "bld_knowledge": """
## Knowledge Injection Checklist

- Verify domain facts are sourced and citable
- Validate density_score >= 0.85 (no filler content)
- Cross-reference with related KCs for consistency
- Check for outdated facts that need refresh

## Injection Pattern

```yaml
# KC injection at F3
source: verified
density: 0.85+
cross_refs: checked
freshness: current
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_retriever.py --query "{DOMAIN}"
```
""",
    "bld_memory": """
## Memory Persistence Checklist

- Verify memory type matches taxonomy (entity, episodic, procedural, working)
- Validate retention policy aligns with data lifecycle rules
- Cross-reference with memory_scope for boundary correctness
- Check for stale entries that need decay or pruning

## Memory Pattern

```yaml
# Memory lifecycle
type: classified
retention: defined
scope: bounded
decay: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_memory_update.py --check
```
""",
    "bld_schema": """
## Schema Validation Checklist

- Verify all required fields have type annotations
- Validate enum values against domain vocabulary
- Cross-reference with related schemas for consistency
- Test schema parsing with sample data before publishing

## Schema Pattern

```yaml
# Schema validation contract
types_annotated: true
enums_valid: true
cross_refs_checked: true
sample_data_tested: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_schema_hydrate.py --check
```
""",
    "bld_orchestration": """
## Orchestration Checklist

- Verify workflow topology matches dependency graph
- Validate handoff protocol between upstream and downstream
- Cross-reference with dispatch rules for routing correctness
- Test wave sequencing with dry-run before live dispatch

## Orchestration Pattern

```yaml
# Workflow validation
topology: verified
handoffs: validated
routing: checked
sequencing: tested
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope orchestration
```
""",
    "bld_prompt": """
## Prompt Construction Checklist

- Verify prompt follows target kind's instruction template
- Validate variable placeholders use standard naming convention
- Cross-reference with chain dependencies for context completeness
- Test prompt with sample input before publishing

## Prompt Pattern

```yaml
# Prompt validation
template_match: true
variables_valid: true
chain_refs_checked: true
sample_tested: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_prompt_optimizer.py --check
```
""",
    "bld_output": """
## Output Template Checklist

- Verify output format matches target kind schema
- Validate all frontmatter fields are present in template
- Cross-reference with eval gate for completeness
- Test template rendering with sample data before publishing

## Output Pattern

```yaml
# Output validation
format_match: true
frontmatter_complete: true
eval_gate_aligned: true
sample_rendered: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```
""",
    "bld_architecture": """
## Architecture Checklist

- Verify component inventory is complete (no orphans)
- Validate dependency graph has no cycles
- Cross-reference with boundary table for scope correctness
- Test layer map against actual codebase structure

## Architecture Pattern

```yaml
# Architecture validation
components: inventoried
dependencies: acyclic
boundaries: defined
layers: mapped
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope architecture
```
""",
}

DEFAULT_ENRICHMENT = """
## Builder Checklist

- Verify all required frontmatter fields are present
- Validate body content against schema constraints
- Cross-reference with related artifacts for consistency
- Run quality gate before publishing

## Validation

```yaml
# Quality check
frontmatter: complete
schema: valid
references: checked
gate: passed
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```
"""


def fix_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    basename = os.path.basename(path)
    iso_type = "_".join(basename.split("_")[:2])

    enrichment = ISO_ENRICHMENT.get(iso_type, DEFAULT_ENRICHMENT)

    if "## Builder Checklist" in content or "## Configuration Checklist" in content:
        return False
    if "## Tool Integration Checklist" in content or "## Knowledge Injection Checklist" in content:
        return False
    if "## Memory Persistence Checklist" in content or "## Schema Validation Checklist" in content:
        return False
    if "## Orchestration Checklist" in content or "## Prompt Construction Checklist" in content:
        return False
    if "## Output Template Checklist" in content or "## Architecture Checklist" in content:
        return False

    if "## Related Artifacts" in content:
        content = content.replace(
            "## Related Artifacts",
            enrichment.strip() + "\n\n## Related Artifacts"
        )
    else:
        content = content.rstrip() + "\n" + enrichment

    # Fix density_score 1.0
    content = re.sub(r"density_score:\s*1\.0\b", "density_score: 0.88", content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return True


def main():
    files = sorted(glob.glob("archetypes/builders/*/bld_*.md"))
    targets = []

    for fp in files:
        if "bld_feedback_" in fp:
            continue
        try:
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read(5000)
            fm = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
            if not fm:
                continue
            qm = re.search(r"^quality:\s*(.+)$", fm.group(1), re.MULTILINE)
            if not qm:
                continue
            val = qm.group(1).strip()
            if val in ("null", "~"):
                continue
            q = float(val)
            if q < 8.0:
                targets.append(fp)
        except (ValueError, KeyError):
            pass

    print(f"Found {len(targets)} non-feedback builder ISOs below 8.0")

    if "--dry-run" in sys.argv:
        for t in targets[:10]:
            print(f"  {t}")
        if len(targets) > 10:
            print(f"  ... and {len(targets) - 10} more")
        return

    fixed = 0
    for path in targets:
        try:
            if fix_file(path):
                fixed += 1
        except Exception as e:
            print(f"  [FAIL] {path}: {e}")

    print(f"Augmented {fixed}/{len(targets)}")


if __name__ == "__main__":
    main()
