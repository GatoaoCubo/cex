#!/usr/bin/env python3
"""ISO Hydration Tool -- enrich thin ISOs with domain-specific content.

Reads thin ISOs (under a byte threshold), enriches:
1. tldr field (kind-specific, not generic)
2. Body sections (domain-specific tables/sections per ISO type)

Usage:
    python _tools/cex_iso_hydrate.py --list          # show targets
    python _tools/cex_iso_hydrate.py --dry-run       # preview changes
    python _tools/cex_iso_hydrate.py --execute       # write changes
    python _tools/cex_iso_hydrate.py --execute --threshold 2500  # custom threshold
"""
import os
import sys
import json
import re
import argparse
from pathlib import Path

BUILDERS_DIR = "archetypes/builders"
KINDS_META = ".cex/kinds_meta.json"
DEFAULT_THRESHOLD = 2210

# ISO type -> pillar mapping
ISO_PILLAR = {
    "config": "P09",
    "tools": "P04",
    "memory": "P10",
    "output": "P05",
    "orchestration": "P12",
    "feedback": "P11",
    "eval": "P07",
    "architecture": "P08",
    "prompt": "P03",
    "model": "P02",
    "knowledge": "P01",
    "schema": "P06",
}

# ISO type -> llm_function mapping
ISO_LLM_FUNCTION = {
    "config": "CONSTRAIN",
    "tools": "CALL",
    "memory": "INJECT",
    "output": "PRODUCE",
    "orchestration": "COLLABORATE",
    "feedback": "LEARN",
    "eval": "GOVERN",
    "architecture": "CONSTRAIN",
    "prompt": "INJECT",
    "model": "BECOME",
    "knowledge": "INJECT",
    "schema": "CONSTRAIN",
}


def load_kinds_meta():
    with open(KINDS_META, "r", encoding="utf-8") as f:
        return json.load(f)


def find_thin_isos(threshold):
    """Find ISO files under byte threshold."""
    results = []
    for root, dirs, files in os.walk(BUILDERS_DIR):
        for fname in files:
            if fname.startswith("bld_") and fname.endswith(".md"):
                fpath = os.path.join(root, fname)
                size = os.path.getsize(fpath)
                if size < threshold:
                    results.append((fpath, size))
    results.sort(key=lambda x: x[0])
    return results


def extract_kind_from_path(fpath):
    """archetypes/builders/ab-test-config-builder/bld_X.md -> ab_test_config"""
    parts = Path(fpath).parts
    for p in parts:
        if p.endswith("-builder"):
            return p.replace("-builder", "").replace("-", "_")
    return None


def extract_iso_type(fname):
    """bld_config_ab_test_config.md -> config"""
    m = re.match(r"bld_([a-z]+)_", fname)
    return m.group(1) if m else None


def parse_file(fpath):
    """Parse frontmatter + body from markdown file."""
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return "", content, content

    end_idx = content.find("---", 3)
    if end_idx == -1:
        return "", content, content

    fm_raw = content[3:end_idx].strip()
    body = content[end_idx + 3:].strip()
    return fm_raw, body, content


def get_fm_field(fm_raw, field):
    """Extract a field value from raw frontmatter text."""
    for line in fm_raw.split("\n"):
        if line.startswith(field + ":"):
            val = line[len(field) + 1:].strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            return val
    return None


def set_fm_field(fm_raw, field, new_value):
    """Replace a field value in raw frontmatter text."""
    lines = fm_raw.split("\n")
    new_lines = []
    replaced = False
    for line in lines:
        if line.startswith(field + ":"):
            # Preserve indentation
            new_lines.append('%s: "%s"' % (field, new_value))
            replaced = True
        else:
            new_lines.append(line)
    if not replaced:
        new_lines.append('%s: "%s"' % (field, new_value))
    return "\n".join(new_lines)


def generate_tldr(iso_type, kind, meta):
    """Generate kind-specific tldr based on ISO type and metadata."""
    desc = meta.get("description", kind.replace("_", " "))
    boundary = meta.get("boundary", "")
    naming = meta.get("naming", "")
    max_bytes = meta.get("max_bytes", 4096)
    pillar = meta.get("pillar", "")
    depends = meta.get("depends_on", [])

    # First sentence of boundary (most useful)
    boundary_short = boundary.split(".")[0].strip() if boundary else ""

    templates = {
        "config": (
            "Production constraints for %s: naming (%s), "
            "output paths (%s/), size limit %dB. %s."
            % (kind.replace("_", " "), naming or "standard", pillar, max_bytes, boundary_short)
        ),
        "tools": (
            "Tool registry for %s builder: CEX pipeline tools (compile, score, retrieve), "
            "file system ops (Read/Write/Edit/Glob/Grep), and domain-specific automation for %s."
            % (kind.replace("_", " "), desc.lower())
        ),
        "memory": (
            "Accumulated production experience for %s: golden patterns, anti-patterns, "
            "common pitfalls, and evidence-backed guidance for %s."
            % (kind.replace("_", " "), desc.lower())
        ),
        "output": (
            "Output template for %s: frontmatter field guide, required body sections, "
            "filled example, and quality gate checklist for %s."
            % (kind.replace("_", " "), desc.lower())
        ),
        "orchestration": (
            "Orchestration protocol for %s: workflow integration, handoff signals, "
            "dependency management, and cross-nucleus coordination for %s."
            % (kind.replace("_", " "), desc.lower())
        ),
        "feedback": (
            "Feedback loop for %s: quality dimensions, improvement signals, "
            "regression indicators, and scoring guidance for %s."
            % (kind.replace("_", " "), desc.lower())
        ),
        "eval": (
            "Evaluation criteria for %s: quality gates (H01-H07), scoring rubric, "
            "pass/fail thresholds, and validation checklist for %s."
            % (kind.replace("_", " "), desc.lower())
        ),
        "architecture": (
            "Architecture constraints for %s: component boundaries, "
            "interface contracts, and structural patterns for %s."
            % (kind.replace("_", " "), desc.lower())
        ),
        "prompt": (
            "Prompt engineering for %s: structure template, token budget, "
            "style constraints, and role framing for %s."
            % (kind.replace("_", " "), desc.lower())
        ),
        "model": (
            "Model definition for %s: identity fields, capability matrix, "
            "behavioral constraints, and sin lens application for %s."
            % (kind.replace("_", " "), desc.lower())
        ),
        "knowledge": (
            "Domain knowledge for %s: key concepts, industry standards, "
            "common patterns, and pitfalls for %s."
            % (kind.replace("_", " "), desc.lower())
        ),
        "schema": (
            "Schema definition for %s: required/optional fields, type constraints, "
            "validation rules, and structural patterns for %s."
            % (kind.replace("_", " "), desc.lower())
        ),
    }
    return templates.get(iso_type, "Builder ISO for %s: %s." % (kind.replace("_", " "), desc))


def generate_body_enrichment(iso_type, kind, meta, existing_body):
    """Generate additional body sections based on ISO type."""
    desc = meta.get("description", kind.replace("_", " "))
    boundary = meta.get("boundary", "")
    naming = meta.get("naming", "")
    max_bytes = meta.get("max_bytes", 4096)
    pillar = meta.get("pillar", "")
    depends = meta.get("depends_on", [])
    llm_func = meta.get("llm_function", "")
    kind_display = kind.replace("_", " ")

    sections = []

    if iso_type == "config":
        # Add domain-specific constraints if missing
        if "Domain-Specific Constraints" not in existing_body and "Constraints" not in existing_body.split("##")[-1] if "##" in existing_body else True:
            boundary_sentences = [s.strip() for s in boundary.split(".") if s.strip()] if boundary else []
            constraints = []
            if boundary_sentences:
                constraints.append("Boundary: %s" % boundary_sentences[0])
            if depends:
                constraints.append("Dependencies: %s" % ", ".join(depends))
            constraints.append("Primary 8F function: %s" % (meta.get("primary_8f", "F1_constrain")))
            constraints.append("Max artifact size: %d bytes" % max_bytes)

            sections.append("\n## Domain-Specific Constraints\n")
            sections.append("| Constraint | Value |")
            sections.append("|-----------|-------|")
            for c in constraints:
                parts = c.split(": ", 1)
                if len(parts) == 2:
                    sections.append("| %s | %s |" % (parts[0], parts[1]))
                else:
                    sections.append("| %s | -- |" % c)

        # Add edge cases if missing
        if "Edge Case" not in existing_body:
            sections.append("\n## Edge Cases\n")
            sections.append("| Scenario | Handling |")
            sections.append("|----------|---------|")
            sections.append("| Missing required frontmatter field | Fail H01 gate; return to F6 |")
            sections.append("| ID collision with existing artifact | Append version suffix (_v2) |")
            sections.append("| Body exceeds %d bytes | Trim prose sections; preserve tables |" % max_bytes)
            if depends:
                sections.append("| Dependency %s not found | Warn; proceed with defaults |" % depends[0])

    elif iso_type == "tools":
        if "CEX Pipeline Tools" not in existing_body:
            sections.append("\n## CEX Pipeline Tools\n")
            sections.append("| Tool | Purpose | When |")
            sections.append("|------|---------|------|")
            sections.append("| cex_compile.py | Compile .md artifact to .yaml | After Write (F8) |")
            sections.append("| cex_score.py | Peer-review quality scoring | After production (F7) |")
            sections.append("| cex_retriever.py | Discover similar artifacts by TF-IDF | During F3 INJECT |")
            sections.append("| cex_doctor.py | Health check builder ISOs | Before dispatch |")

        if "Data Sources" not in existing_body:
            sections.append("\n## Data Sources\n")
            sections.append("| Source | Content | When to use |")
            sections.append("|--------|---------|-------------|")
            sections.append("| SCHEMA.md | Field definitions, ID pattern, constraints | Every production run |")
            sections.append("| OUTPUT_TEMPLATE.md | Exact frontmatter + body structure | Every production run |")
            sections.append("| QUALITY_GATES.md | H01-H08 HARD gates | Every validation run |")
            sections.append("| KNOWLEDGE.md | Domain concepts for %s | When designing structure |" % kind_display)
            sections.append("| MEMORY.md | Common mistakes, anti-patterns | When stuck or producing a variant |")

        if "Tool Permissions" not in existing_body:
            sections.append("\n## Tool Permissions\n")
            sections.append("| Category | Tools | Status |")
            sections.append("|----------|-------|--------|")
            sections.append("| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |")
            sections.append("| DENIED | (none) | Explicitly blocked |")
            sections.append("| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |")

    elif iso_type == "memory":
        if "Evidence" not in existing_body:
            sections.append("\n## Evidence\n")
            sections.append(
                "Production experience from %s artifact generation. " % kind_display
            )
            if boundary:
                sections.append("%s " % boundary.split(".")[0])
            sections.append(
                "Patterns derived from builder runs, quality gate failures, and peer review feedback."
            )

        if "Pitfalls" not in existing_body and "Pitfall" not in existing_body:
            sections.append("\n## Pitfalls\n")
            sections.append("- **Missing frontmatter fields**: omitting required fields causes H01 gate failure.")
            sections.append("- **Generic descriptions**: vague purpose/tldr reduces retrieval accuracy.")
            sections.append("- **Ignoring boundary**: %s." % (boundary.split(".")[0] if boundary else "overstepping kind scope"))
            if depends:
                sections.append(
                    "- **Orphaned dependencies**: referencing %s without verifying it exists." % depends[0]
                )

    elif iso_type == "output":
        if "Quality Gate Checklist" not in existing_body:
            sections.append("\n## Quality Gate Checklist\n")
            sections.append("| Gate | Check | Pass Condition |")
            sections.append("|------|-------|---------------|")
            sections.append("| H01 | Frontmatter complete | All required fields present with valid types |")
            sections.append("| H02 | ID matches filename | id field equals filename stem |")
            sections.append("| H03 | Naming convention | Follows %s pattern |" % (naming or "standard"))
            sections.append("| H04 | Body sections present | All required sections non-empty |")
            sections.append("| H05 | Size within limits | Total <= %d bytes |" % max_bytes)
            sections.append("| H06 | No placeholder text | No {{var}} unreplaced |")
            sections.append("| H07 | quality: null | Never self-scored |")

    elif iso_type == "orchestration":
        if "Integration Points" not in existing_body:
            sections.append("\n## Integration Points\n")
            sections.append("| Point | Direction | Protocol |")
            sections.append("|-------|-----------|----------|")
            sections.append("| F8 COLLABORATE | outbound | signal_writer.write_signal() |")
            sections.append("| F3 INJECT | inbound | Receives upstream artifacts via handoff |")
            if depends:
                for dep in depends[:3]:
                    sections.append(
                        "| %s | upstream | Must exist before %s production |"
                        % (dep, kind_display)
                    )

        if "Dependencies" not in existing_body and depends:
            sections.append("\n## Dependencies\n")
            sections.append("| Dependency | Required | Purpose |")
            sections.append("|-----------|----------|---------|")
            for dep in depends:
                sections.append("| %s | yes | Upstream artifact for %s |" % (dep, kind_display))

    elif iso_type == "feedback":
        if "Quality Dimensions" not in existing_body and "Scoring" not in existing_body:
            sections.append("\n## Quality Dimensions\n")
            sections.append("| Dimension | Weight | Criteria |")
            sections.append("|-----------|--------|----------|")
            sections.append("| D1 Structural completeness | 20%% | All required sections present |")
            sections.append("| D2 Domain accuracy | 25%% | Content matches %s domain |" % kind_display)
            sections.append("| D3 Density | 20%% | >= 0.85 information density |")
            sections.append("| D4 Cross-references | 15%% | Valid links to related artifacts |")
            sections.append("| D5 Actionability | 20%% | Builder can produce from this alone |")

        if "Common Failures" not in existing_body:
            sections.append("\n## Common Failures\n")
            sections.append("| Failure | Frequency | Fix |")
            sections.append("|---------|-----------|-----|")
            sections.append("| Generic content | High | Add domain-specific examples |")
            sections.append("| Missing boundary adherence | Medium | Check kinds_meta.json boundary |")
            sections.append("| Low density score | Medium | Replace prose with tables |")

    elif iso_type == "eval":
        if "Scoring Rubric" not in existing_body and "Scoring" not in existing_body:
            sections.append("\n## Scoring Rubric\n")
            sections.append("| Score Range | Label | Criteria |")
            sections.append("|-----------|-------|----------|")
            sections.append("| 9.0-10.0 | Excellent | All gates pass, high density, domain-accurate |")
            sections.append("| 8.0-8.9 | Good | All hard gates pass, minor density gaps |")
            sections.append("| 7.0-7.9 | Acceptable | 1 soft gate fail, needs revision |")
            sections.append("| < 7.0 | Reject | Hard gate failure, return to F6 |")

        if "Validation Checklist" not in existing_body:
            sections.append("\n## Validation Checklist\n")
            sections.append("| Check | Method | Automated |")
            sections.append("|-------|--------|-----------|")
            sections.append("| Frontmatter schema | cex_compile.py --validate | Yes |")
            sections.append("| Naming convention | Regex match against %s | Yes |" % (naming or "pattern"))
            sections.append("| Size limit | Byte count <= %d | Yes |" % max_bytes)
            sections.append("| Density score | Token/byte ratio >= 0.85 | Yes |")
            sections.append("| Cross-references valid | Link resolution check | Partial |")

    elif iso_type == "architecture":
        if "Component Boundaries" not in existing_body and "Boundaries" not in existing_body:
            sections.append("\n## Component Boundaries\n")
            if boundary:
                sections.append(boundary)
            sections.append("\n| Boundary | In Scope | Out of Scope |")
            sections.append("|----------|----------|-------------|")
            sections.append("| Kind scope | %s | Adjacent kinds |" % kind_display)
            if depends:
                sections.append("| Dependencies | %s | Transitive deps |" % ", ".join(depends[:3]))

        if "Interface" not in existing_body:
            sections.append("\n## Interfaces\n")
            sections.append("| Interface | Direction | Contract |")
            sections.append("|-----------|-----------|----------|")
            sections.append("| Schema (P06) | upstream | Validates structure |")
            sections.append("| Output (P05) | downstream | Produces artifacts |")
            sections.append("| Config (P09) | lateral | Constrains production |")

    elif iso_type == "prompt":
        if "Token Budget" not in existing_body:
            sections.append("\n## Token Budget\n")
            sections.append("| Component | Allocation | Notes |")
            sections.append("|-----------|-----------|-------|")
            sections.append("| System prompt | 15%% | Builder identity + sin lens |")
            sections.append("| Context (ISOs) | 40%% | 12 ISOs loaded per builder |")
            sections.append("| Domain knowledge | 25%% | KCs + examples + memory |")
            sections.append("| Generation headroom | 20%% | Artifact output space |")

        if "Style" not in existing_body and "Tone" not in existing_body:
            sections.append("\n## Style Constraints\n")
            sections.append("| Dimension | Guideline |")
            sections.append("|-----------|-----------|")
            sections.append("| Voice | Technical, precise, builder-appropriate |")
            sections.append("| Structure | Tables over prose; data over description |")
            sections.append("| Density | >= 0.85; every sentence adds information |")
            sections.append("| References | Use canonical kind names, not synonyms |")

    elif iso_type == "model":
        if "Capability" not in existing_body:
            sections.append("\n## Capability Matrix\n")
            sections.append("| Capability | Level | Evidence |")
            sections.append("|-----------|-------|---------|")
            sections.append("| %s production | Primary | Builder-specific |" % kind_display)
            sections.append("| 8F pipeline execution | Required | All builders |")
            sections.append("| Quality self-assessment | Prohibited | quality: null enforced |")
            sections.append("| Cross-reference resolution | Required | Related artifacts table |")

    # Add Properties table if missing (all types)
    if "Properties" not in existing_body and "## Properties" not in existing_body:
        iso_pillar = ISO_PILLAR.get(iso_type, pillar)
        sections.append("\n## Properties\n")
        sections.append("| Property | Value |")
        sections.append("|----------|-------|")
        sections.append("| Kind | `%s` |" % iso_type)
        sections.append("| Pillar | %s |" % iso_pillar)
        sections.append("| Domain | %s construction |" % kind_display)
        sections.append("| Pipeline | 8F (F1-F8) |")
        sections.append("| Scorer | cex_score.py |")
        sections.append("| Compiler | cex_compile.py |")
        sections.append("| Retriever | cex_retriever.py |")
        sections.append("| Quality target | 9.0+ |")
        sections.append("| Density target | 0.85+ |")

    return "\n".join(sections) if sections else ""


def hydrate_file(fpath, kinds_meta, dry_run=False):
    """Hydrate a single thin ISO file."""
    fname = os.path.basename(fpath)
    kind = extract_kind_from_path(fpath)
    iso_type = extract_iso_type(fname)

    if not kind or not iso_type:
        return False, "Could not extract kind/iso_type from %s" % fpath

    meta = kinds_meta.get(kind, {})
    if not meta:
        return False, "Kind '%s' not found in kinds_meta.json" % kind

    fm_raw, body, original = parse_file(fpath)
    if not fm_raw:
        return False, "No frontmatter in %s" % fpath

    # 1. Enrich tldr
    old_tldr = get_fm_field(fm_raw, "tldr")
    purpose = get_fm_field(fm_raw, "purpose")
    new_tldr = generate_tldr(iso_type, kind, meta)

    # Only replace if current tldr is generic (matches purpose or is very short)
    if old_tldr and old_tldr != purpose and len(old_tldr) > 60:
        # tldr is already enriched, keep it
        pass
    else:
        fm_raw = set_fm_field(fm_raw, "tldr", new_tldr)

    # 2. Generate body enrichment
    enrichment = generate_body_enrichment(iso_type, kind, meta, body)

    if not enrichment and old_tldr and old_tldr != purpose:
        return False, "Already enriched: %s" % fpath

    # 3. Assemble new content
    # Insert enrichment before Related Artifacts section if it exists
    if enrichment:
        if "## Related Artifacts" in body:
            related_idx = body.index("## Related Artifacts")
            new_body = body[:related_idx].rstrip() + "\n" + enrichment + "\n\n" + body[related_idx:]
        else:
            new_body = body.rstrip() + "\n" + enrichment
    else:
        new_body = body

    new_content = "---\n%s\n---\n\n%s\n" % (fm_raw, new_body)

    if dry_run:
        old_size = len(original.encode("utf-8"))
        new_size = len(new_content.encode("utf-8"))
        return True, "+%d bytes (%d -> %d) %s" % (new_size - old_size, old_size, new_size, fpath)

    # Write
    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_content)

    return True, fpath


def main():
    parser = argparse.ArgumentParser(description="ISO Hydration Tool")
    parser.add_argument("--list", action="store_true", help="List thin ISOs")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes")
    parser.add_argument("--execute", action="store_true", help="Write changes")
    parser.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD, help="Byte threshold")
    args = parser.parse_args()

    if not any([args.list, args.dry_run, args.execute]):
        parser.print_help()
        sys.exit(1)

    kinds_meta = load_kinds_meta()
    thin_isos = find_thin_isos(args.threshold)

    if args.list:
        print("[ISO-HYDRATE] %d thin ISOs under %d bytes" % (len(thin_isos), args.threshold))
        by_type = {}
        for fpath, size in thin_isos:
            iso_type = extract_iso_type(os.path.basename(fpath)) or "unknown"
            by_type.setdefault(iso_type, []).append((fpath, size))
        for itype, files in sorted(by_type.items(), key=lambda x: -len(x[1])):
            print("  %s: %d files (avg %d bytes)" % (
                itype, len(files), sum(s for _, s in files) // len(files)
            ))
        return

    success = 0
    skipped = 0
    errors = 0

    for fpath, size in thin_isos:
        try:
            ok, msg = hydrate_file(fpath, kinds_meta, dry_run=args.dry_run)
            if ok:
                success += 1
                if args.dry_run:
                    print("[DRY] %s" % msg)
            else:
                skipped += 1
                if args.dry_run:
                    print("[SKIP] %s" % msg)
        except Exception as e:
            errors += 1
            print("[ERR] %s: %s" % (fpath, str(e)))

    print("\n[ISO-HYDRATE] Done: %d enriched, %d skipped, %d errors (of %d total)" % (
        success, skipped, errors, len(thin_isos)
    ))


if __name__ == "__main__":
    main()
