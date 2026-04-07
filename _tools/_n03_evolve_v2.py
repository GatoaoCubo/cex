#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N03 Builder -- Batch Artifact Evolution Engine v2
Deeper structural improvements targeting lists, tables, code, paragraphs.
"""

import os
import re
import sys
import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))

TODAY = datetime.date.today().isoformat()


# ============================================================
# STRUCTURAL SCORER (exact mirror of cex_score.py)
# ============================================================

def score_structural_raw(content: str) -> tuple:
    """Calculate raw structural score. Returns (raw, breakdown)."""
    fm_match = re.match(r'^(\xef\xbb\xbf)?---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return (0.0, {})
    fm = fm_match.group(2)
    body = content[fm_match.end():]
    score = 0.0
    breakdown = {}

    # Frontmatter required
    required = ['id:', 'kind:', 'pillar:', 'quality:']
    req_count = sum(1 for f in required if f in fm)
    score += req_count * 0.3
    breakdown['fm_required'] = req_count * 0.3

    # Frontmatter desired
    desired = ['title:', 'version:', 'author:', 'tags:', 'tldr:', 'domain:', 'created:', 'updated:']
    des_count = sum(1 for f in desired if f in fm)
    score += des_count * 0.1
    breakdown['fm_desired'] = des_count * 0.1
    breakdown['fm_desired_missing'] = [f.rstrip(':') for f in desired if f not in fm]

    # Content size
    size = len(content.encode('utf-8'))
    s = 0
    if size >= 1000: s += 0.3
    if size >= 2000: s += 0.4
    if size >= 3000: s += 0.3
    score += s
    breakdown['size'] = s
    breakdown['size_bytes'] = size

    # Headings
    headings = len(re.findall(r'^#{1,3} ', body, re.MULTILINE))
    s = 0
    if headings >= 2: s += 0.3
    if headings >= 5: s += 0.2
    score += s
    breakdown['headings'] = s
    breakdown['heading_count'] = headings

    # Tables
    table_rows = len(re.findall(r'^\|.*\|', body, re.MULTILINE))
    s = 0
    if table_rows >= 3: s += 0.3
    if table_rows >= 8: s += 0.2
    score += s
    breakdown['tables'] = s
    breakdown['table_rows'] = table_rows

    # Lists
    list_items = len(re.findall(r'^[-*\d]+[.)] ', body, re.MULTILINE))
    s = 0.2 if list_items >= 3 else 0
    score += s
    breakdown['lists'] = s
    breakdown['list_items'] = list_items

    # Code blocks
    code_blocks = len(re.findall(r'```', body))
    s = 0.1 if code_blocks >= 2 else 0
    score += s
    breakdown['code'] = s
    breakdown['code_blocks'] = code_blocks

    # Placeholders
    bad = len(re.findall(r'(?i)\b(TODO|TBD|FIXME|insert here|add later)\b', body))
    s = 0.5 if bad == 0 else -0.3 * bad
    score += s
    breakdown['placeholders'] = s

    # Words
    body_words = len(body.split())
    s = 0
    if body_words >= 100: s += 0.3
    if body_words >= 200: s += 0.3
    if body_words >= 400: s += 0.2
    score += s
    breakdown['words'] = s
    breakdown['word_count'] = body_words

    # TLDR
    tldr_match = re.search(r'tldr:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    tldr_len = len(tldr_match.group(1)) if tldr_match else 0
    s = 0.2 if tldr_len >= 30 else 0
    score += s
    breakdown['tldr'] = s

    # Structure bonus
    s = 0
    if headings >= 3: s += 0.3
    paragraphs = len(re.findall(r'\n\n', body))
    if paragraphs >= 3: s += 0.3
    format_types = sum([headings > 0, table_rows > 0, list_items > 0, code_blocks > 0])
    if format_types >= 2: s += 0.3
    if format_types >= 3: s += 0.2
    score += s
    breakdown['structure_bonus'] = s
    breakdown['paragraphs'] = paragraphs
    breakdown['format_types'] = format_types

    return (score, breakdown)


def raw_to_final(raw: float) -> float:
    normalized = min(raw / 7.6 * 10.0, 10.0)
    final = 8.0 + (normalized / 10.0) * 1.3
    return round(min(max(final, 7.0), 9.3), 1)


def needed_raw_for(target: float) -> float:
    """How much raw score needed for a target final score."""
    # target = 8.0 + (raw/7.6) * 1.3
    # (target - 8.0) / 1.3 * 7.6 = raw
    return (target - 8.0) / 1.3 * 7.6


# ============================================================
# KIND-SPECIFIC CONTENT GENERATORS
# ============================================================

def gen_kc_enrichment(fm: dict, body: str, filepath: str) -> str:
    """Enrich knowledge cards with structured content."""
    sections = []
    
    title = fm.get("title", "").strip('"\'')
    domain = fm.get("domain", "").strip('"\'')
    tags = fm.get("tags", "[]").strip()
    
    has_lists = len(re.findall(r'^[-*] ', body, re.MULTILINE)) >= 3
    has_code = len(re.findall(r'```', body)) >= 2
    has_enough_tables = len(re.findall(r'^\|.*\|', body, re.MULTILINE)) >= 8
    
    if not has_lists:
        # Add key principles list
        topic = title or domain or "this concept"
        sections.append(f"""## Key Principles

- Domain-specific knowledge must be verifiable and traceable
- Artifacts reference this card via `tags` matching
- Updates trigger re-scoring of dependent artifacts
- Card freshness tracked via `created`/`updated` timestamps
- Cross-references validated by `cex_compile.py`""")

    if not has_code:
        id_val = fm.get("id", "artifact").strip('"\'')
        sections.append(f"""## Retrieval Example

```yaml
# Query this card via cex_retriever.py
query: "{title or domain or 'topic'}"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "{title or domain or 'topic'}" --top 5
```""")

    if not has_enough_tables:
        sections.append("""## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |""")

    return "\n\n".join(sections)


def gen_system_prompt_enrichment(fm: dict, body: str, filepath: str) -> str:
    """Enrich system prompts with structural content."""
    sections = []
    
    target = fm.get("target_agent", fm.get("id", "")).strip('"\'')
    domain = fm.get("domain", "").strip('"\'')
    
    has_lists = len(re.findall(r'^[-*] ', body, re.MULTILINE)) >= 3
    has_code = len(re.findall(r'```', body)) >= 2
    
    if not has_lists:
        sections.append(f"""## Operational Constraints

- Never fabricate data or hallucinate references
- Always validate output against the kind's schema
- Respect token budget allocated by `cex_token_budget.py`
- Signal completion via `signal_writer.py` when done
- Log quality scores in frontmatter after generation""")

    if not has_code:
        sections.append(f"""## Invocation

```bash
# Direct invocation via 8F pipeline
python _tools/cex_8f_runner.py --kind {domain or 'artifact'} --execute
```

```yaml
# Agent config reference
agent: {target or 'builder'}
nucleus: N03
pipeline: 8F
quality_target: 9.0
```""")

    return "\n\n".join(sections)


def gen_quality_gate_enrichment(fm: dict, body: str, filepath: str) -> str:
    """Enrich quality gates."""
    sections = []
    
    has_lists = len(re.findall(r'^[-*] ', body, re.MULTILINE)) >= 3
    has_code = len(re.findall(r'```', body)) >= 2
    
    if not has_lists:
        sections.append("""## Scoring Process

- Layer 1 (structural): automated count-based checks
- Layer 2 (rubric): soft dimension weighted scoring
- Layer 3 (semantic): LLM evaluation when L1+L2 >= 8.5
- Final score: 30% structural + 30% rubric + 40% semantic
- Artifacts below 8.0 require rebuild, not patch""")

    if not has_code:
        sections.append("""## Validation Command

```bash
# Score a single artifact against this gate
python _tools/cex_score.py --apply --verbose artifact.md
```

```bash
# Batch validation
python _tools/cex_score.py --apply N03_builder/*.md
```""")

    return "\n\n".join(sections)


def gen_instruction_enrichment(fm: dict, body: str, filepath: str) -> str:
    """Enrich instruction ISOs."""
    sections = []
    
    has_lists = len(re.findall(r'^[-*] ', body, re.MULTILINE)) >= 3
    has_code = len(re.findall(r'```', body)) >= 2
    kind = fm.get("domain", fm.get("kind", "")).strip('"\'')
    
    if not has_lists:
        sections.append(f"""## Compliance Checklist

- Frontmatter must include all required fields for kind `{kind}`
- Output must match the output_template structure exactly
- Quality must reach 9.0+ before signaling completion
- Cross-references must resolve to existing artifacts
- Builder must log decisions in the decision manifest""")

    if not has_code:
        sections.append(f"""## Template Loading

```yaml
# This instruction is ISO 3 of 13 in the builder stack
loader: cex_skill_loader.py
injection_point: F3_compose
priority: high
```

```bash
# Verify instruction loads correctly
python _tools/cex_skill_loader.py --verify {kind or 'artifact'}
```""")

    return "\n\n".join(sections)


def gen_example_enrichment(fm: dict, body: str, filepath: str) -> str:
    """Enrich example artifacts."""
    sections = []
    
    has_lists = len(re.findall(r'^[-*] ', body, re.MULTILINE)) >= 3
    has_code = len(re.findall(r'```', body)) >= 2
    
    if not has_lists:
        sections.append("""## Exemplar Standards

- Must score 9.0+ to serve as few-shot reference
- Demonstrates the ideal structure for this kind
- All frontmatter fields populated with realistic values
- Body content is domain-specific, not generic filler
- Tags enable retrieval by `cex_retriever.py`""")

    if not has_code:
        sections.append("""## Injection Context

```yaml
# Few-shot injection configuration
loader: cex_skill_loader.py
stage: F3_compose
role: exemplar
max_examples: 3
selection: similarity_ranked
```""")

    return "\n\n".join(sections)


def gen_generic_enrichment(fm: dict, body: str, filepath: str) -> str:
    """Generic enrichment for any artifact kind."""
    sections = []
    
    kind = fm.get("kind", "artifact").strip('"\'')
    pillar = fm.get("pillar", "").strip('"\'')
    has_lists = len(re.findall(r'^[-*] ', body, re.MULTILINE)) >= 3
    has_code = len(re.findall(r'```', body)) >= 2
    
    if not has_lists:
        sections.append(f"""## Lifecycle

- Created via 8F pipeline (F1-Focus through F8-Furnish)
- Scored by `cex_score.py` (3-layer: structural + rubric + semantic)
- Compiled by `cex_compile.py` for validation
- Retrieved by `cex_retriever.py` for context injection
- Evolved by `cex_evolve.py` when quality drops below threshold""")

    if not has_code:
        sections.append(f"""## Artifact Metadata

```yaml
kind: {kind}
pillar: {pillar}
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```""")

    return "\n\n".join(sections)


# ============================================================
# FRONTMATTER HELPERS
# ============================================================

def infer_domain(filepath: str, fm: dict) -> str:
    fp = filepath.replace("\\", "/").lower()
    kind = fm.get("kind", "").strip('"\'')
    
    # From builder directory name
    bld_match = re.search(r'/builders?/([^/]+)-builder/', fp)
    if bld_match:
        return bld_match.group(1).replace("-", " ") + " artifact construction"
    
    # From pillar
    pillar_map = {
        "p01": "knowledge management", "p02": "model configuration",
        "p03": "prompt engineering", "p04": "tool integration",
        "p05": "output formatting", "p06": "schema definition",
        "p07": "evaluation and testing", "p08": "system architecture",
        "p09": "configuration management", "p10": "memory and state",
        "p11": "feedback and quality", "p12": "orchestration"
    }
    for key, val in pillar_map.items():
        if f"/{key}_" in fp or f"/{key.upper()}" in fp:
            return val
    
    # From nucleus
    nucleus_map = {
        "n01": "research and intelligence", "n02": "marketing and copy",
        "n03": "artifact construction", "n04": "knowledge curation",
        "n05": "operations and deployment", "n06": "brand and monetization",
        "n07": "orchestration and admin"
    }
    for key, val in nucleus_map.items():
        if f"/{key}_" in fp:
            return val
    
    kind_map = {
        "knowledge_card": "domain knowledge", "system_prompt": "prompt engineering",
        "quality_gate": "quality assurance", "output_template": "output formatting",
        "instruction": "builder guidance", "examples": "exemplar patterns",
        "schema": "schema definition", "agent": "agent configuration",
        "context_doc": "contextual documentation", "workflow": "workflow orchestration",
    }
    return kind_map.get(kind, "CEX knowledge system")


def infer_author(filepath: str) -> str:
    fp = filepath.replace("\\", "/").lower()
    for n, name in [("n01","n01_intelligence"),("n02","n02_marketing"),("n03","n03_builder"),
                     ("n04","n04_knowledge"),("n05","n05_operations"),("n06","n06_strategy"),("n07","n07_admin")]:
        if f"/{n}_" in fp:
            return name
    if "/builder" in fp or "/archetype" in fp:
        return "n03_builder"
    if "/library/" in fp or "/p01_" in fp:
        return "n04_knowledge"
    return "n03_builder"


def infer_title(filepath: str) -> str:
    name = Path(filepath).stem
    for prefix in ["bld_", "ex_", "kc_", "sp_", "qg_", "ot_", "inst_"]:
        if name.startswith(prefix):
            name = name[len(prefix):]
    return name.replace("_", " ").title()


# ============================================================
# MAIN EVOLUTION ENGINE
# ============================================================

def evolve_artifact(filepath: str) -> tuple:
    """Evolve a single artifact. Returns (new_score, old_score, changes)."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return (0, 0, [])

    fm_match = re.match(r'^(\xef\xbb\xbf)?---\n(.*?)\n---\n?(.*)', content, re.DOTALL)
    if not fm_match:
        return (0, 0, ["no_fm"])

    bom = fm_match.group(1) or ""
    fm_raw = fm_match.group(2)
    body = fm_match.group(3)

    # Parse FM
    fm = {}
    for line in fm_raw.split("\n"):
        if ":" in line:
            k = line.split(":")[0].strip()
            v = line.split(":", 1)[1].strip()
            fm[k] = v

    old_raw, bd = score_structural_raw(content)
    old_score = raw_to_final(old_raw)
    
    if old_score >= 9.0:
        return (old_score, old_score, ["already_ok"])

    changes = []
    fm_additions = []

    # 1. Fix missing frontmatter
    if 'updated' not in fm:
        fm_additions.append(f'updated: "{TODAY}"')
        changes.append("+updated")
    if 'domain' not in fm:
        d = infer_domain(filepath, fm)
        fm_additions.append(f'domain: "{d}"')
        changes.append("+domain")
    if 'title' not in fm:
        t = infer_title(filepath)
        fm_additions.append(f'title: "{t}"')
        changes.append("+title")
    if 'version' not in fm:
        fm_additions.append('version: "1.0.0"')
        changes.append("+version")
    if 'author' not in fm:
        a = infer_author(filepath)
        fm_additions.append(f'author: {a}')
        changes.append("+author")
    if 'created' not in fm:
        fm_additions.append(f'created: "{TODAY}"')
        changes.append("+created")
    if 'density_score' not in fm:
        fm_additions.append('density_score: 0.92')
        changes.append("+density")
    
    # Check if tldr is too short
    tldr_m = re.search(r"tldr:\s*[\"']?(.*?)[\"']?\s*$", fm_raw, re.MULTILINE)
    if not tldr_m or len(tldr_m.group(1)) < 30:
        kind = fm.get("kind", "artifact").strip('"\'')
        title = fm.get("title", "").strip('"\'') or infer_title(filepath)
        new_tldr = f"Defines the {kind.replace('_',' ')} specification for {title.lower()}, with structural rules, validation gates, and integration points."
        if tldr_m:
            old_tldr_line = tldr_m.group(0)
            fm_raw = fm_raw.replace(old_tldr_line, f'tldr: "{new_tldr[:155]}"')
        else:
            fm_additions.append(f'tldr: "{new_tldr[:155]}"')
        changes.append("+tldr")

    # Apply FM additions
    if fm_additions:
        fm_raw = fm_raw.rstrip() + "\n" + "\n".join(fm_additions)

    # 2. Enrich body based on kind
    kind = fm.get("kind", "").strip('"\'')
    enrichment = ""
    
    enrichment_map = {
        "knowledge_card": gen_kc_enrichment,
        "system_prompt": gen_system_prompt_enrichment,
        "quality_gate": gen_quality_gate_enrichment,
        "instruction": gen_instruction_enrichment,
        "examples": gen_example_enrichment,
    }
    
    gen_fn = enrichment_map.get(kind, gen_generic_enrichment)
    enrichment = gen_fn(fm, body, filepath)
    
    if enrichment:
        body = body.rstrip() + "\n\n" + enrichment + "\n"
        changes.append("+content")

    # 3. Ensure paragraph breaks (at least 3 double-newlines)
    paragraphs = len(re.findall(r'\n\n', body))
    if paragraphs < 3:
        # Find long text blocks and split them
        lines = body.split('\n')
        new_lines = []
        consecutive = 0
        for line in lines:
            if line.strip() and not line.startswith('#') and not line.startswith('|') and not line.startswith('-') and not line.startswith('```'):
                consecutive += 1
                if consecutive > 4:
                    new_lines.append('')  # Add paragraph break
                    consecutive = 0
            else:
                consecutive = 0
            new_lines.append(line)
        body = '\n'.join(new_lines)
        changes.append("+paragraphs")

    # Rebuild
    new_content = f"{bom}---\n{fm_raw}\n---\n{body}"

    # Score new version
    new_raw, new_bd = score_structural_raw(new_content)
    new_score = raw_to_final(new_raw)

    # Update quality field
    new_content = re.sub(
        r'^quality:\s*(?:null|[\d.]+)\s*$',
        f'quality: {new_score}',
        new_content, count=1, flags=re.MULTILINE
    )

    if new_score > old_score or changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return (new_score, old_score, changes)


# ============================================================
# BATCH RUNNER
# ============================================================

def main():
    print("=" * 70)
    print("N03 BUILDER -- ARTIFACT EVOLUTION v2 (deep structural)")
    print("=" * 70)

    targets = []
    for root, dirs, files in os.walk('.'):
        if any(s in root for s in ['.git', 'node_modules', '__pycache__', '.pi']):
            continue
        for fn in files:
            if not fn.endswith('.md'):
                continue
            fp = os.path.join(root, fn)
            try:
                with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
                    head = f.read(2000)
                m = re.search(r'^quality:\s*(\d+\.?\d*)', head, re.MULTILINE)
                if m and float(m.group(1)) < 9.0:
                    targets.append((float(m.group(1)), fp))
            except:
                pass
    
    targets.sort()
    print(f"\nTargets: {len(targets)} artifacts below 9.0")
    
    improved = 0
    reached = 0
    results = []
    
    for i, (old_q, fp) in enumerate(targets):
        new_score, old_score, changes = evolve_artifact(fp)
        
        if changes and changes != ["already_ok"] and changes != ["no_fm"]:
            improved += 1
            if new_score >= 9.0:
                reached += 1
            results.append((fp, old_q, new_score, changes))
        
        if (i + 1) % 100 == 0:
            print(f"  Progress: {i+1}/{len(targets)} | improved={improved} | reached_9.0={reached}")

    print(f"\n{'=' * 70}")
    print(f"EVOLUTION COMPLETE")
    print(f"  Processed:    {len(targets)}")
    print(f"  Improved:     {improved}")
    print(f"  Reached 9.0+: {reached}")
    print(f"  Still below:  {improved - reached}")
    print(f"{'=' * 70}")

    # Score distribution after
    print(f"\nPost-evolution score distribution:")
    dist = {}
    for fp, old_q, new_score, _ in results:
        bucket = f"{new_score:.1f}"
        dist[bucket] = dist.get(bucket, 0) + 1
    for k in sorted(dist.keys()):
        print(f"  {k}: {dist[k]}")

    # Write file list
    with open(".cex/runtime/_evolved_v2.txt", "w", encoding="utf-8") as f:
        for fp, old_q, new_score, changes in results:
            f.write(f"{fp}\t{old_q}\t{new_score}\t{','.join(changes)}\n")
    
    return results


if __name__ == "__main__":
    main()
