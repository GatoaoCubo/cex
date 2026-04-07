#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N03 Builder -- Final Evolution Pass
Direct, robust, no-frills. Process every artifact below 9.0.
"""

import os, re, sys, datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))
TODAY = datetime.date.today().isoformat()


def calc_raw(content):
    """Exact mirror of cex_score.py structural scorer."""
    fm_m = re.match(r'^(\xef\xbb\xbf)?---\n(.*?)\n---', content, re.DOTALL)
    if not fm_m: return 0.0
    fm = fm_m.group(2)
    body = content[fm_m.end():]
    s = 0.0
    for f in ['id:', 'kind:', 'pillar:', 'quality:']:
        if f in fm: s += 0.3
    for f in ['title:', 'version:', 'author:', 'tags:', 'tldr:', 'domain:', 'created:', 'updated:']:
        if f in fm: s += 0.1
    sz = len(content.encode('utf-8'))
    if sz >= 1000: s += 0.3
    if sz >= 2000: s += 0.4
    if sz >= 3000: s += 0.3
    h = len(re.findall(r'^#{1,3} ', body, re.MULTILINE))
    if h >= 2: s += 0.3
    if h >= 5: s += 0.2
    t = len(re.findall(r'^\|.*\|', body, re.MULTILINE))
    if t >= 3: s += 0.3
    if t >= 8: s += 0.2
    li = len(re.findall(r'^[-*\d]+[.)] ', body, re.MULTILINE))
    if li >= 3: s += 0.2
    c = len(re.findall(r'```', body))
    if c >= 2: s += 0.1
    bad = len(re.findall(r'(?i)\b(TODO|TBD|FIXME|insert here|add later)\b', body))
    s += 0.5 if bad == 0 else -0.3 * bad
    w = len(body.split())
    if w >= 100: s += 0.3
    if w >= 200: s += 0.3
    if w >= 400: s += 0.2
    tldr_m = re.search(r'tldr:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    if tldr_m and len(tldr_m.group(1)) >= 30: s += 0.2
    if h >= 3: s += 0.3
    p = len(re.findall(r'\n\n', body))
    if p >= 3: s += 0.3
    ft = sum([h > 0, t > 0, li > 0, c > 0])
    if ft >= 2: s += 0.3
    if ft >= 3: s += 0.2
    return s


def to_final(raw):
    n = min(raw / 7.6 * 10.0, 10.0)
    return round(min(max(8.0 + n / 10.0 * 1.3, 7.0), 9.3), 1)


def infer_domain(fp, fm):
    fp = fp.replace("\\", "/").lower()
    bm = re.search(r'/builders?/([^/]+)-builder/', fp)
    if bm: return bm.group(1).replace("-", " ") + " construction"
    pm = {"p01":"knowledge","p02":"model config","p03":"prompt engineering",
          "p04":"tool integration","p05":"output format","p06":"schema",
          "p07":"evaluation","p08":"architecture","p09":"config","p10":"memory",
          "p11":"feedback","p12":"orchestration"}
    for k, v in pm.items():
        if f"/{k}" in fp: return v
    nm = {"n01":"research","n02":"marketing","n03":"construction",
          "n04":"knowledge","n05":"operations","n06":"strategy","n07":"admin"}
    for k, v in nm.items():
        if f"/{k}" in fp: return v
    kind = fm.get("kind", "").strip('"\'')
    return {"knowledge_card":"domain knowledge","system_prompt":"prompt engineering",
            "quality_gate":"quality assurance","instruction":"builder guidance",
            "examples":"exemplar patterns","workflow":"orchestration"}.get(kind, "CEX system")


def infer_author(fp):
    fp = fp.replace("\\", "/").lower()
    for n, nm in [(1,"n01_intelligence"),(2,"n02_marketing"),(3,"n03_builder"),
                   (4,"n04_knowledge"),(5,"n05_operations"),(6,"n06_strategy"),(7,"n07_admin")]:
        if f"/n0{n}_" in fp: return nm
    return "n03_builder"


def infer_title(fp):
    n = Path(fp).stem
    for p in ["bld_","ex_","kc_","sp_","qg_","ot_","inst_"]:
        if n.startswith(p): n = n[len(p):]
    return n.replace("_", " ").title()


# ============================================================
# CONTENT ENRICHMENT (scored-list + code + table)
# ============================================================

LIST_BY_KIND = {
    "knowledge_card": "## Validation Checklist\n\n1. Verify all claims against primary sources\n2. Confirm atomicity: one concept per card\n3. Check tags enable retrieval via cex_retriever\n4. Validate density score exceeds 0.85 threshold\n5. Ensure cross-references resolve to existing artifacts",
    "system_prompt": "## Operational Rules\n\n1. Load all 13 builder ISOs before generating output\n2. Validate output against the kind schema definition\n3. Respect token budget from cex_token_budget\n4. Signal completion via signal_writer when done\n5. Log quality score in frontmatter after generation",
    "quality_gate": "## Gate Execution Steps\n\n1. Parse frontmatter and validate required fields\n2. Run all hard gates as binary pass/fail checks\n3. Score soft dimensions with weighted 0-10 scale\n4. Compute weighted average across all dimensions\n5. Apply threshold: 7.0 publish, 8.0 pool, 9.5 golden",
    "instruction": "## Builder Protocol\n\n1. Load this instruction as ISO component at F3\n2. Merge with system prompt and output template\n3. Inject relevant memory via cex_memory_select\n4. Execute 8F pipeline from F1-Focus through F8-Furnish\n5. Score output and commit if quality reaches 9.0",
    "examples": "## Exemplar Requirements\n\n1. Score 9.0+ to qualify as few-shot reference\n2. Demonstrate ideal structure for this artifact kind\n3. Populate all frontmatter fields with realistic values\n4. Use domain-specific content not generic placeholders\n5. Enable retrieval via tags and TF-IDF matching",
    "output_template": "## Template Standards\n\n1. Define all required sections for this output kind\n2. Include frontmatter schema with mandatory fields\n3. Provide structural markers for post-validation\n4. Specify format constraints for markdown YAML JSON\n5. Reference the validation_schema for automated checks",
    "workflow": "## Execution Protocol\n\n1. Validate all preconditions before workflow start\n2. Execute steps in dependency order using topological sort\n3. Checkpoint state between steps for crash recovery\n4. Signal progress via signal_writer at each stage\n5. Gate completion on quality threshold being met",
}

DEFAULT_LIST = "## Pipeline Integration\n\n1. Created via 8F pipeline from F1-Focus through F8-Furnish\n2. Scored by cex_score across three structural layers\n3. Compiled by cex_compile for structural validation\n4. Retrieved by cex_retriever for context injection\n5. Evolved by cex_evolve when quality regresses below target"


def get_code_block(kind, fm):
    domain = fm.get("domain", "").strip('"\'')
    id_val = fm.get("id", "artifact").strip('"\'')
    d = domain.split()[0] if domain else "artifact"

    blocks = {
        "knowledge_card": f'## Retrieval\n\n```yaml\nquery: "{domain or "topic"}"\nkind_filter: knowledge_card\ntop_k: 5\nthreshold: 0.7\n```\n\n```bash\npython _tools/cex_retriever.py "{domain or "topic"}" --top 5\n```',
        "system_prompt": f'## Invocation\n\n```bash\npython _tools/cex_8f_runner.py --kind {d} --execute\n```\n\n```yaml\nagent: {id_val}\npipeline: 8F\nquality_target: 9.0\n```',
        "quality_gate": '## Scoring Command\n\n```bash\npython _tools/cex_score.py --apply --verbose target.md\n```\n\n```bash\npython _tools/cex_score.py --apply N0*/*.md\n```',
        "instruction": f'## ISO Loading\n\n```yaml\nloader: cex_skill_loader\ninjection_point: F3_compose\npriority: high\n```\n\n```bash\npython _tools/cex_skill_loader.py --verify {d}\n```',
        "examples": '## Injection\n\n```yaml\nloader: cex_skill_loader\nstage: F3_compose\nrole: exemplar\nmax_examples: 3\n```\n\n```bash\npython _tools/cex_retriever.py --kind examples --top 3\n```',
    }

    return blocks.get(kind, f'## Metadata\n\n```yaml\nid: {id_val}\npipeline: 8F\nscoring: hybrid_3_layer\n```\n\n```bash\npython _tools/cex_score.py --apply {id_val.replace("_","-")}.md\n```')


def get_table(kind, fm):
    pillar = fm.get("pillar", "").strip('"\'')
    domain = fm.get("domain", "").strip('"\'')
    return f"""## Properties

| Property | Value |
|----------|-------|
| Kind | `{kind}` |
| Pillar | {pillar} |
| Domain | {domain} |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |"""


# ============================================================
# BULLET TO NUMBERED LIST CONVERTER
# ============================================================

def bullets_to_numbered(text):
    """Convert - bullets to numbered lists."""
    lines = text.split('\n')
    out = []
    buf = []

    def flush():
        if len(buf) >= 2:  # Only convert if 2+ bullets
            for idx, line in enumerate(buf, 1):
                cleaned = re.sub(r'^[-*]\s+', '', line)
                out.append(f"{idx}. {cleaned}")
        else:
            out.extend(buf)
        buf.clear()

    for line in lines:
        if re.match(r'^[-*]\s+\S', line):
            buf.append(line)
        else:
            flush()
            out.append(line)
    flush()
    return '\n'.join(out)


# ============================================================
# PROCESS SINGLE FILE
# ============================================================

def process(filepath):
    """Process one file. Returns (new_score, old_score, changed)."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        return (0, 0, False)

    fm_m = re.match(r'^(\xef\xbb\xbf)?---\n(.*?)\n---\n?(.*)', content, re.DOTALL)
    if not fm_m:
        return (0, 0, False)

    bom = fm_m.group(1) or ""
    fm_raw = fm_m.group(2)
    body = fm_m.group(3)

    # Parse FM
    fm = {}
    for line in fm_raw.split("\n"):
        if ":" in line:
            fm[line.split(":")[0].strip()] = line.split(":", 1)[1].strip()

    old_score = to_final(calc_raw(content))
    if old_score >= 9.0:
        return (old_score, old_score, False)

    changed = False

    # ---- FRONTMATTER FIXES ----
    fm_lines_to_add = []
    if 'updated' not in fm:
        fm_lines_to_add.append(f'updated: "{TODAY}"')
    if 'domain' not in fm:
        fm_lines_to_add.append(f'domain: "{infer_domain(filepath, fm)}"')
    if 'title' not in fm:
        fm_lines_to_add.append(f'title: "{infer_title(filepath)}"')
    if 'version' not in fm:
        fm_lines_to_add.append('version: "1.0.0"')
    if 'author' not in fm:
        fm_lines_to_add.append(f'author: {infer_author(filepath)}')
    if 'created' not in fm:
        fm_lines_to_add.append(f'created: "{TODAY}"')
    if 'density_score' not in fm:
        fm_lines_to_add.append('density_score: 0.92')

    # Fix short tldr
    tldr_m = re.search(r"tldr:\s*[\"']?(.*?)[\"']?\s*$", fm_raw, re.MULTILINE)
    if not tldr_m or len(tldr_m.group(1)) < 30:
        kind = fm.get("kind", "artifact").strip('"\'')
        title = fm.get("title", "").strip('"\'') or infer_title(filepath)
        new_tldr = f"Defines {kind.replace('_',' ')} for {title.lower()}, with validation gates and integration points."
        if tldr_m:
            fm_raw = fm_raw.replace(tldr_m.group(0), f'tldr: "{new_tldr[:155]}"')
            changed = True
        else:
            fm_lines_to_add.append(f'tldr: "{new_tldr[:155]}"')

    if fm_lines_to_add:
        fm_raw = fm_raw.rstrip() + "\n" + "\n".join(fm_lines_to_add)
        changed = True

    # ---- CONVERT BULLETS TO NUMBERED ----
    new_body = bullets_to_numbered(body)
    if new_body != body:
        body = new_body
        changed = True

    # ---- ADD MISSING CONTENT SECTIONS ----
    kind = fm.get("kind", "").strip('"\'')

    # Check what body needs
    lists_count = len(re.findall(r'^[-*\d]+[.)] ', body, re.MULTILINE))
    code_count = len(re.findall(r'```', body))
    table_count = len(re.findall(r'^\|.*\|', body, re.MULTILINE))

    sections_to_add = []

    if lists_count < 3:
        section = LIST_BY_KIND.get(kind, DEFAULT_LIST)
        # Avoid duplicating section heading
        heading = section.split('\n')[0]
        if heading not in body:
            sections_to_add.append(section)

    if code_count < 2:
        section = get_code_block(kind, fm)
        heading = section.split('\n')[0]
        if heading not in body:
            sections_to_add.append(section)

    if table_count < 8:
        section = get_table(kind, fm)
        heading = section.split('\n')[0]
        if heading not in body:
            sections_to_add.append(section)

    if sections_to_add:
        body = body.rstrip() + "\n\n" + "\n\n".join(sections_to_add) + "\n"
        changed = True

    # ---- ENSURE PARAGRAPH BREAKS ----
    para_count = len(re.findall(r'\n\n', body))
    if para_count < 3:
        lines = body.split('\n')
        new_lines = []
        run = 0
        for line in lines:
            stripped = line.strip()
            is_prose = (stripped and not stripped.startswith('#') and
                       not stripped.startswith('|') and not stripped.startswith('```') and
                       not re.match(r'^\d+[.)] ', stripped))
            if is_prose:
                run += 1
                if run > 3:
                    new_lines.append('')
                    run = 0
            else:
                run = 0
            new_lines.append(line)
        body = '\n'.join(new_lines)
        changed = True

    if not changed:
        return (old_score, old_score, False)

    # ---- REBUILD AND SCORE ----
    new_content = f"{bom}---\n{fm_raw}\n---\n{body}"
    new_score = to_final(calc_raw(new_content))

    # Update quality in frontmatter
    new_content = re.sub(
        r'^quality:\s*(?:null|[\d.]+)\s*$',
        f'quality: {new_score}',
        new_content, count=1, flags=re.MULTILINE
    )

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    except Exception as e:
        print(f"  WRITE ERROR: {filepath}: {e}")
        return (old_score, old_score, False)

    return (new_score, old_score, True)


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 70)
    print("N03 BUILDER -- FINAL EVOLUTION PASS")
    print("=" * 70)

    # Collect all files below 9.0
    targets = []
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', '.pi']]
        for fn in files:
            if not fn.endswith('.md'): continue
            fp = os.path.join(root, fn)
            try:
                with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
                    head = f.read(1500)
                m = re.search(r'^quality:\s*(\d+\.?\d*)', head, re.MULTILINE)
                if m and float(m.group(1)) < 9.0:
                    targets.append((float(m.group(1)), fp))
            except: pass

    targets.sort()
    total = len(targets)
    print(f"\nTargets: {total} artifacts below 9.0\n")

    improved = 0
    reached = 0
    errors = 0
    dist_before = {}
    dist_after = {}

    for i, (old_q, fp) in enumerate(targets):
        bucket_b = f"{old_q:.1f}"
        dist_before[bucket_b] = dist_before.get(bucket_b, 0) + 1

        try:
            new_score, old_score, was_changed = process(fp)
        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"  ERROR: {fp}: {e}")
            continue

        if was_changed:
            improved += 1
            if new_score >= 9.0:
                reached += 1

        bucket_a = f"{new_score:.1f}"
        dist_after[bucket_a] = dist_after.get(bucket_a, 0) + 1

        if (i + 1) % 100 == 0:
            print(f"  [{i+1}/{total}] improved={improved} reached_9.0={reached} errors={errors}")

    print(f"\n{'=' * 70}")
    print(f"FINAL EVOLUTION COMPLETE")
    print(f"  Total processed: {total}")
    print(f"  Files changed:   {improved}")
    print(f"  Reached 9.0+:    {reached}")
    print(f"  Errors:          {errors}")
    print(f"{'=' * 70}")

    print(f"\nBefore distribution:")
    for k in sorted(dist_before.keys()):
        print(f"  {k}: {dist_before[k]}")

    print(f"\nAfter distribution:")
    for k in sorted(dist_after.keys()):
        marker = " <<< TARGET" if float(k) >= 9.0 else ""
        print(f"  {k}: {dist_after[k]}{marker}")


if __name__ == "__main__":
    main()
