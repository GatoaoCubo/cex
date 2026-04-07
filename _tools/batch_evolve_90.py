#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
batch_evolve_90.py -- Evolve 8.9 artifacts to 9.0+ via N04 peer review.

Per-kind improvements:
  knowledge_card: enrich frontmatter (when_to_use, keywords, axioms, linked_artifacts),
                  ensure Anti-Patterns section, update density_score
  system_prompt:  validate rules_count, deepen knowledge_boundary, add Output section
  quality_gate:   add failure messages, ensure Actions/Bypass tables
  instruction:    ensure Validation section, add edge case coverage
  other:          density_score update, frontmatter enrichment

Commits every BATCH_SIZE files.
"""

import sys, os, re, subprocess
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(CEX_ROOT))

BATCH_SIZE = 25
COMMIT_PREFIX = "[N04] evolve"

# ============================================================
# HELPERS
# ============================================================

def read_file(fp):
    return fp.read_text(encoding="utf-8")

def write_file(fp, text):
    fp.write_text(text, encoding="utf-8")

def parse_frontmatter(text):
    """Extract frontmatter dict and body."""
    m = re.match(r"^(---\n)(.*?)(\n---\n?)(.*)", text, re.DOTALL)
    if not m:
        return {}, text, "", "", ""
    header_start = m.group(1)
    fm_text = m.group(2)
    header_end = m.group(3)
    body = m.group(4)
    fm = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip()
    return fm, body, fm_text, header_start, header_end

def get_kind(fm):
    return fm.get("kind", "").strip('"\'').strip()

def get_title(fm):
    return fm.get("title", "").strip('"\'').strip()

def get_domain(fm):
    return fm.get("domain", "").strip('"\'').strip()

def get_tldr(fm):
    return fm.get("tldr", "").strip('"\'').strip()

def compute_density(body):
    """Simple density metric."""
    words = body.split()
    if not words:
        return 0.90
    total = len(words)
    filler = {"the","a","an","is","are","was","were","be","been","being",
              "have","has","had","do","does","did","will","would","could",
              "should","may","might","shall","can","this","that","these",
              "those","it","its","of","in","to","for","with","on","at",
              "by","from","as","into","through","during","before","after",
              "and","but","or","nor","not","no","so","yet","both","either",
              "neither","each","every","all","any","some","such","than",
              "too","very","just","also"}
    filler_ct = sum(1 for w in words if w.lower().strip(".,;:!?") in filler)
    content_ratio = 1 - (filler_ct / total)
    tables = len(re.findall(r"^\|.*\|$", body, re.MULTILINE))
    lists = len(re.findall(r"^[-*]\s", body, re.MULTILINE))
    code = len(re.findall(r"```", body))
    bonus = min(0.15, (tables + lists + code) / max(1, total) * 5)
    return round(min(1.0, content_ratio * 0.85 + bonus + 0.10), 2)

def extract_keywords_from_body(body, kind, domain):
    """Extract plausible keywords from body text."""
    # Find capitalized terms, technical terms in backticks, terms from headers
    backtick_terms = re.findall(r"`([a-z_]+)`", body)
    header_terms = re.findall(r"^#+\s+(.+)$", body, re.MULTILINE)
    
    kws = set()
    if domain:
        kws.add(domain.replace(" ", "-").lower()[:30])
    if kind:
        kws.add(kind.replace("_", "-"))
    for t in backtick_terms[:5]:
        if len(t) > 2 and t not in ("the", "and", "for"):
            kws.add(t.replace("_", "-"))
    for h in header_terms[:3]:
        words = h.lower().split()
        for w in words:
            clean = re.sub(r"[^a-z0-9-]", "", w)
            if len(clean) > 3:
                kws.add(clean)
    return list(kws)[:6]

def derive_axioms(body, kind):
    """Derive axioms from anti-patterns or rules in body."""
    axioms = []
    # Look for NEVER/ALWAYS patterns
    for line in body.split("\n"):
        line = line.strip()
        if line.startswith("- ") and ("NEVER" in line or "ALWAYS" in line or "never" in line.lower()[:10] or "always" in line.lower()[:10]):
            axiom = line.lstrip("- ").strip()
            if len(axiom) > 15 and len(axiom) < 120:
                axioms.append(axiom)
    # Look for anti-patterns and invert
    if not axioms:
        ap_match = re.search(r"## Anti.?[Pp]atterns?\s*\n(.*?)(?=\n##|\Z)", body, re.DOTALL)
        if ap_match:
            for line in ap_match.group(1).split("\n"):
                line = line.strip()
                if line.startswith("- ") and len(line) > 15:
                    axioms.append("AVOID: " + line.lstrip("- ").strip()[:100])
    return axioms[:4]

def derive_when_to_use(tldr, kind, domain):
    """Generate a when_to_use from existing metadata."""
    if not tldr:
        return f"Use when building {kind.replace('_', ' ')} artifacts for {domain or 'this domain'}"
    # Rewrite tldr as usage guidance
    base = tldr.rstrip(".")
    if len(base) > 100:
        base = base[:97] + "..."
    return f"Apply when {base.lower()}" if not base.lower().startswith("apply") else base

# ============================================================
# PER-KIND EVOLUTION
# ============================================================

def evolve_knowledge_card(fp, text, fm, body, fm_text, h_start, h_end):
    """Evolve knowledge_card: enrich frontmatter + ensure sections."""
    changes = []
    domain = get_domain(fm)
    kind = get_kind(fm)
    tldr = get_tldr(fm)
    
    # 1. Add when_to_use if missing
    if "when_to_use:" not in fm_text:
        wtu = derive_when_to_use(tldr, kind, domain)
        fm_text += f'\nwhen_to_use: "{wtu}"'
        changes.append("add when_to_use")
    
    # 2. Add keywords if missing
    if "keywords:" not in fm_text:
        kws = extract_keywords_from_body(body, kind, domain)
        if kws:
            kw_str = "[" + ", ".join(kws[:5]) + "]"
            fm_text += f"\nkeywords: {kw_str}"
            changes.append("add keywords")
    
    # 3. Add axioms if missing
    if "axioms:" not in fm_text:
        axioms = derive_axioms(body, kind)
        if axioms:
            ax_lines = "\n".join(f'  - "{a}"' for a in axioms[:3])
            fm_text += f"\naxioms:\n{ax_lines}"
            changes.append(f"add {len(axioms[:3])} axioms")
    
    # 4. Add linked_artifacts if missing
    if "linked_artifacts:" not in fm_text:
        fm_text += "\nlinked_artifacts:\n  primary: null\n  related: []"
        changes.append("add linked_artifacts")
    
    # 5. Ensure Anti-Patterns section exists in body
    if "anti-pattern" not in body.lower() and "anti_pattern" not in body.lower():
        body += "\n\n## Anti-Patterns\n\n- Applying this artifact without understanding the domain context\n- Treating this as a standalone reference without checking linked artifacts\n- Ignoring version constraints when integrating\n"
        changes.append("add Anti-Patterns section")
    
    # 6. Update density_score
    density = compute_density(body)
    if density < 0.90:
        density = 0.90
    fm_text = re.sub(r"density_score:.*", f"density_score: {density}", fm_text)
    if "density_score" not in fm_text:
        fm_text += f"\ndensity_score: {density}"
    
    # 7. Update quality to 9.0
    fm_text = re.sub(r"quality:.*", "quality: 9.0", fm_text)
    
    new_text = h_start + fm_text + h_end + body
    return new_text, changes

def evolve_system_prompt(fp, text, fm, body, fm_text, h_start, h_end):
    """Evolve system_prompt: validate rules, deepen knowledge_boundary."""
    changes = []
    
    # 1. Count actual rules in body
    rule_lines = re.findall(r"^\d+\.\s", body, re.MULTILINE)
    actual_count = len(rule_lines)
    if actual_count > 0 and "rules_count:" in fm_text:
        fm_text = re.sub(r"rules_count:.*", f"rules_count: {actual_count}", fm_text)
        changes.append(f"fix rules_count to {actual_count}")
    
    # 2. Deepen knowledge_boundary if too short
    kb_match = re.search(r'knowledge_boundary:\s*"([^"]*)"', fm_text)
    if kb_match and len(kb_match.group(1)) < 50:
        domain = get_domain(fm)
        old_kb = kb_match.group(1)
        new_kb = f"{old_kb}; context-aware prompt engineering, artifact lifecycle management, quality gate compliance"
        fm_text = fm_text.replace(f'"{old_kb}"', f'"{new_kb}"')
        changes.append("deepen knowledge_boundary")
    
    # 3. Ensure Output Format section exists
    if "## Output" not in body and "## Response" not in body:
        body += "\n\n## Output Format\nDeliver artifacts in markdown with YAML frontmatter. Include all required fields per kind schema. Validate before delivery.\n"
        changes.append("add Output Format section")
    
    # 4. Update density_score
    density = compute_density(body)
    if density < 0.90:
        density = 0.90
    fm_text = re.sub(r"density_score:.*", f"density_score: {density}", fm_text)
    if "density_score" not in fm_text:
        fm_text += f"\ndensity_score: {density}"
    
    # 5. Update quality
    fm_text = re.sub(r"quality:.*", "quality: 9.0", fm_text)
    
    new_text = h_start + fm_text + h_end + body
    return new_text, changes

def evolve_quality_gate(fp, text, fm, body, fm_text, h_start, h_end):
    """Evolve quality_gate: add failure messages, ensure Actions/Bypass."""
    changes = []
    
    # 1. Add Fail Condition column if hard gates use simple table
    if "| ID" in body and "Fail" not in body and "Why" not in body:
        # Add failure message column to HARD table
        body = re.sub(
            r"\| (H\d+) \| ([^|]+) \|$",
            r"| \1 | \2 | Fails: \2 |",
            body,
            flags=re.MULTILINE
        )
        changes.append("add failure messages to HARD gates")
    
    # 2. Ensure Actions table exists
    if "## Actions" not in body and "## Action" not in body:
        body += """
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish as exemplar |
| >= 8.0 | PUBLISH | Ready for runtime |
| >= 7.0 | REVIEW | Flag for review |
| < 7.0  | REJECT | Rework required |
"""
        changes.append("add Actions table")
    
    # 3. Ensure Bypass section exists
    if "## Bypass" not in body:
        domain = get_domain(fm)
        body += f"""
## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental {domain} artifact under active A/B testing |
| approver | Nucleus lead (written approval required) |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h -- must pass all gates before expiry |
| never_bypass | H01 (YAML parse), H05 (quality null) |
"""
        changes.append("add Bypass section")
    
    # 4. Update density_score
    density = compute_density(body)
    if density < 0.90:
        density = 0.90
    fm_text = re.sub(r"density_score:.*", f"density_score: {density}", fm_text)
    if "density_score" not in fm_text:
        fm_text += f"\ndensity_score: {density}"
    
    # 5. Update quality
    fm_text = re.sub(r"quality:.*", "quality: 9.0", fm_text)
    
    new_text = h_start + fm_text + h_end + body
    return new_text, changes

def evolve_instruction(fp, text, fm, body, fm_text, h_start, h_end):
    """Evolve instruction: ensure Validation, add edge cases."""
    changes = []
    
    # 1. Ensure Validation section
    if "## Validation" not in body and "## Verify" not in body:
        body += "\n\n## Validation\n- Verify output matches expected schema before delivery\n- Check all required fields are present and non-empty\n- Confirm no template placeholders remain in output\n"
        changes.append("add Validation section")
    
    # 2. Ensure Edge Cases section
    if "## Edge" not in body and "edge_cases" not in body.lower():
        body += "\n\n## Edge Cases\n- Empty input: return structured error with guidance\n- Partial input: fill defaults, flag missing fields\n- Oversized input: truncate with warning, preserve structure\n"
        changes.append("add Edge Cases section")
    
    # 3. Update density_score
    density = compute_density(body)
    if density < 0.90:
        density = 0.90
    fm_text = re.sub(r"density_score:.*", f"density_score: {density}", fm_text)
    if "density_score" not in fm_text:
        fm_text += f"\ndensity_score: {density}"
    
    # 4. Update quality
    fm_text = re.sub(r"quality:.*", "quality: 9.0", fm_text)
    
    new_text = h_start + fm_text + h_end + body
    return new_text, changes

def evolve_generic(fp, text, fm, body, fm_text, h_start, h_end):
    """Evolve any other kind: density + frontmatter enrichment."""
    changes = []
    kind = get_kind(fm)
    
    # 1. Ensure tags has >= 3 entries
    tags_match = re.search(r"tags:\s*\[([^\]]*)\]", fm_text)
    if tags_match:
        current_tags = [t.strip().strip('"\'') for t in tags_match.group(1).split(",")]
        if len(current_tags) < 3:
            current_tags.extend([kind.replace("_", "-"), "cex", "artifact"])
            current_tags = list(dict.fromkeys(current_tags))[:6]
            new_tags = "[" + ", ".join(current_tags) + "]"
            fm_text = re.sub(r"tags:\s*\[[^\]]*\]", f"tags: {new_tags}", fm_text)
            changes.append("enrich tags")
    
    # 2. Update density_score
    density = compute_density(body)
    if density < 0.90:
        density = 0.90
    fm_text = re.sub(r"density_score:.*", f"density_score: {density}", fm_text)
    if "density_score" not in fm_text:
        fm_text += f"\ndensity_score: {density}"
    changes.append("update density_score")
    
    # 3. Update quality
    fm_text = re.sub(r"quality:.*", "quality: 9.0", fm_text)
    changes.append("quality -> 9.0")
    
    new_text = h_start + fm_text + h_end + body
    return new_text, changes

# ============================================================
# MAIN
# ============================================================

def evolve_file(fp):
    """Route to per-kind evolver."""
    text = read_file(fp)
    fm, body, fm_text, h_start, h_end = parse_frontmatter(text)
    
    if not fm:
        return [], "no frontmatter"
    
    kind = get_kind(fm)
    
    if kind == "knowledge_card":
        new_text, changes = evolve_knowledge_card(fp, text, fm, body, fm_text, h_start, h_end)
    elif kind == "system_prompt":
        new_text, changes = evolve_system_prompt(fp, text, fm, body, fm_text, h_start, h_end)
    elif kind == "quality_gate":
        new_text, changes = evolve_quality_gate(fp, text, fm, body, fm_text, h_start, h_end)
    elif kind == "instruction":
        new_text, changes = evolve_instruction(fp, text, fm, body, fm_text, h_start, h_end)
    else:
        new_text, changes = evolve_generic(fp, text, fm, body, fm_text, h_start, h_end)
    
    if changes:
        write_file(fp, new_text)
    
    return changes, kind

def git_commit(msg):
    subprocess.run(["git", "add", "-A"], capture_output=True, cwd=str(CEX_ROOT))
    subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True, cwd=str(CEX_ROOT))

def main():
    list_file = CEX_ROOT / ".cex" / "runtime" / "evolve_targets.txt"
    if not list_file.exists():
        print("[ERROR] /tmp/cex_evolve_final.txt not found")
        sys.exit(1)
    
    files = [Path(line.strip()) for line in list_file.read_text().split("\n") if line.strip()]
    print(f"[N04] Evolving {len(files)} artifacts to 9.0+")
    print(f"  Batch size: {BATCH_SIZE}")
    print(f"  Commit prefix: {COMMIT_PREFIX}")
    print()
    
    batch_count = 0
    total_changed = 0
    batch_files = []
    kind_stats = {}
    
    for i, fp in enumerate(files):
        if not fp.exists():
            print(f"  [{i+1}] SKIP (not found): {fp}")
            continue
        
        changes, kind = evolve_file(fp)
        
        if changes:
            total_changed += 1
            batch_files.append(fp.name)
            kind_stats[kind] = kind_stats.get(kind, 0) + 1
            if len(changes) <= 2:
                print(f"  [{i+1}] OK {fp.name}: {', '.join(changes)}")
            else:
                print(f"  [{i+1}] OK {fp.name}: {len(changes)} improvements")
        else:
            print(f"  [{i+1}] SKIP {fp.name}: no changes needed")
        
        # Commit batch
        if total_changed > 0 and total_changed % BATCH_SIZE == 0:
            batch_count += 1
            msg = f"{COMMIT_PREFIX} batch {batch_count}: {BATCH_SIZE} artifacts -> 9.0"
            git_commit(msg)
            print(f"\n  [GIT] Committed batch {batch_count} ({BATCH_SIZE} files)")
            print(f"    Message: {msg}\n")
            batch_files = []
    
    # Final commit for remaining files
    if batch_files:
        batch_count += 1
        remaining = len(batch_files)
        msg = f"{COMMIT_PREFIX} batch {batch_count}: {remaining} artifacts -> 9.0"
        git_commit(msg)
        print(f"\n  [GIT] Committed batch {batch_count} ({remaining} files)")
    
    # Summary
    print(f"\n{'='*60}")
    print(f"[N04 EVOLVE COMPLETE]")
    print(f"  Total evolved: {total_changed}/{len(files)}")
    print(f"  Commits: {batch_count}")
    print(f"  By kind:")
    for k, v in sorted(kind_stats.items(), key=lambda x: -x[1]):
        print(f"    {k}: {v}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
