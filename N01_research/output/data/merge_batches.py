#!/usr/bin/env python3
"""
CRM Batch Merger — N07 Orchestrator Tool
Merges batch JSONs into crm_pet_abc.json with dedup + recount.
Usage: python merge_batches.py [--batch X] [--all] [--dry-run]
"""
import json, os, sys, csv
from datetime import datetime

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_FILE = os.path.join(DATA_DIR, "crm_pet_abc.json")
CSV_FILE  = os.path.join(DATA_DIR, "crm_pet_abc.csv")

BATCH_MAP = {
    "a": "crm_batch_a_diretorios.json",
    "b": "crm_batch_b_gmaps.json",
    "c": "crm_batch_c_social.json",
    "d": "crm_batch_d_marketplaces.json",
    "e": "crm_batch_e_reputation.json",
    "f": "crm_batch_f_cnae.json",
}

def normalize(name):
    """Normalize name for dedup comparison."""
    if not name:
        return ""
    return name.lower().strip().replace("  "," ")

def dedup_key(record):
    """Create dedup key from name + city, or CNPJ if available."""
    cnpj = (record.get("cnpj") or "").replace(".", "").replace("/", "").replace("-", "").strip()
    if cnpj and len(cnpj) >= 14:
        return f"cnpj:{cnpj}"
    name = normalize(record.get("nome_fantasia") or record.get("nome") or "")
    city = normalize(record.get("cidade") or "")
    return f"name:{name}@{city}"

def calc_completeness(r):
    """Calculate completeness score (0-5) based on actionable fields."""
    score = 0
    if r.get("nome_fantasia") or r.get("nome"): score += 1
    if r.get("endereco"): score += 1
    if r.get("telefone") or r.get("whatsapp"): score += 1
    if r.get("email") or r.get("website"): score += 1
    if r.get("cnpj"): score += 1
    return score

def load_json(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def export_csv(data, filepath):
    if not data:
        return
    # Collect all keys
    keys = []
    for r in data:
        for k in r.keys():
            if k not in keys:
                keys.append(k)
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(data)

def merge(base, batch_data, batch_label):
    """Merge batch into base, return (new_base, stats)."""
    existing_keys = {dedup_key(r) for r in base}
    added = 0
    dupes = 0
    for r in batch_data:
        dk = dedup_key(r)
        if dk in existing_keys:
            dupes += 1
            continue
        r["completeness_score"] = calc_completeness(r)
        r["batch_source"] = batch_label
        base.append(r)
        existing_keys.add(dk)
        added += 1
    return base, {"added": added, "dupes": dupes, "batch": batch_label}

def recalc_all_completeness(data):
    for r in data:
        r["completeness_score"] = calc_completeness(r)
    return data

def stats(data):
    total = len(data)
    with_phone = sum(1 for x in data if x.get("telefone") or x.get("whatsapp"))
    with_addr = sum(1 for x in data if x.get("endereco"))
    with_web = sum(1 for x in data if x.get("website") or x.get("email") or x.get("instagram"))
    with_cnpj = sum(1 for x in data if x.get("cnpj"))
    cities = {}
    for x in data:
        c = x.get("cidade", "?")
        cities[c] = cities.get(c, 0) + 1
    return {
        "total": total,
        "with_phone": with_phone,
        "with_addr": with_addr,
        "with_web": with_web,
        "with_cnpj": with_cnpj,
        "cities": dict(sorted(cities.items(), key=lambda x: -x[1])[:10]),
    }

def main():
    import argparse
    parser = argparse.ArgumentParser(description="CRM Batch Merger")
    parser.add_argument("--batch", choices=list(BATCH_MAP.keys()), help="Merge specific batch")
    parser.add_argument("--all", action="store_true", help="Merge all available batches")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen")
    parser.add_argument("--recalc", action="store_true", help="Recalculate all completeness scores")
    args = parser.parse_args()

    base = load_json(BASE_FILE)
    if base is None:
        print(f"[ERROR] Base not found: {BASE_FILE}")
        sys.exit(1)

    print(f"[BASE] {len(base)} contatos")

    if args.recalc:
        base = recalc_all_completeness(base)
        save_json(base, BASE_FILE)
        export_csv(base, CSV_FILE)
        s = stats(base)
        print(f"[RECALC] Done. Stats: {s['total']} total | tel:{s['with_phone']} | addr:{s['with_addr']} | web:{s['with_web']} | cnpj:{s['with_cnpj']}")
        return

    batches_to_merge = []
    if args.batch:
        batches_to_merge = [args.batch]
    elif args.all:
        batches_to_merge = list(BATCH_MAP.keys())
    else:
        print("Usage: --batch X or --all")
        sys.exit(1)

    results = []
    for b in batches_to_merge:
        filepath = os.path.join(DATA_DIR, BATCH_MAP[b])
        batch_data = load_json(filepath)
        if batch_data is None:
            print(f"[SKIP] Batch {b.upper()} — file not found: {BATCH_MAP[b]}")
            continue
        if args.dry_run:
            existing_keys = {dedup_key(r) for r in base}
            new = sum(1 for r in batch_data if dedup_key(r) not in existing_keys)
            dup = len(batch_data) - new
            print(f"[DRY-RUN] Batch {b.upper()}: {len(batch_data)} records | {new} new | {dup} dupes")
        else:
            base, st = merge(base, batch_data, f"batch_{b}")
            results.append(st)
            print(f"[MERGE] Batch {b.upper()}: +{st['added']} added | {st['dupes']} dupes")

    if not args.dry_run and results:
        save_json(base, BASE_FILE)
        export_csv(base, CSV_FILE)
        s = stats(base)
        print(f"\n[FINAL] {s['total']} contatos | tel:{s['with_phone']} ({100*s['with_phone']//s['total']}%) | addr:{s['with_addr']} ({100*s['with_addr']//s['total']}%) | web:{s['with_web']} ({100*s['with_web']//s['total']}%) | cnpj:{s['with_cnpj']} ({100*s['with_cnpj']//s['total']}%)")
        print(f"[CITIES] {s['cities']}")
        total_added = sum(r["added"] for r in results)
        print(f"[SUMMARY] +{total_added} novos contatos merged")

if __name__ == "__main__":
    main()
