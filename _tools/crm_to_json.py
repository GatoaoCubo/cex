"""Parse CRM markdown tables into JSON for the HTML dashboard.
Handles 3 table formats: T1/T2 (16 cols), T3 (8-9 cols), T4 (8 cols).
"""
import re
import json

CRM_PATH = "N06_commercial/P01_knowledge/kc_influencer_crm_unified.md"
OUT_PATH = "N06_commercial/P05_output/crm_data.json"


def parse_cells(line):
    cells = [c.strip() for c in line.split("|")]
    return [c for c in cells if c != ""]


def is_data_row(cells):
    if len(cells) < 5:
        return False
    if cells[0].startswith("#") or cells[0].startswith("-"):
        return False
    try:
        int(cells[0])
        return True
    except ValueError:
        return False


def detect_section(lines, idx):
    """Walk backwards to find the current section header."""
    for i in range(idx, max(idx - 40, 0), -1):
        line = lines[i].strip()
        if line.startswith("## 3.") or line.startswith("## 4."):
            return "full"  # T1/T2: 16 columns
        if line.startswith("## 5.") or line.startswith("### 5."):
            return "t3"
        if line.startswith("## 6.") or line.startswith("### 6."):
            return "t4"
        if line.startswith("## 7.") or line.startswith("## 8."):
            return "skip"
    return "unknown"


def detect_header_columns(lines, idx):
    """Find the header row above this data row to detect column names."""
    for i in range(idx - 1, max(idx - 5, 0), -1):
        line = lines[i].strip()
        if line.startswith("|") and ("Name" in line or "name" in line):
            return parse_cells(line)
    return []


def infer_tier_from_section(lines, idx):
    for i in range(idx, max(idx - 50, 0), -1):
        line = lines[i].strip()
        if "T1" in line and ("1M+" in line or "Priority" in line):
            return "T1"
        if "T2" in line and ("100K" in line):
            return "T2"
        if "T3" in line and ("10K" in line):
            return "T3"
        if "T4" in line and ("Micro" in line or "<10K" in line):
            return "T4"
        if line.startswith("## 3."):
            return "T1"
        if line.startswith("## 4."):
            return "T2"
        if line.startswith("## 5.") or line.startswith("### 5."):
            return "T3"
        if line.startswith("## 6.") or line.startswith("### 6."):
            return "T4"
    return "--"


def infer_region_from_section(lines, idx):
    for i in range(idx, max(idx - 20, 0), -1):
        line = lines[i].strip().upper()
        if "GLOBAL" in line:
            return "GLOBAL"
        if "BR" in line and ("BRAZIL" in line or "BR " in line or "BR --" in line):
            return "BR"
    return "--"


def parse_full_row(cells):
    """T1/T2 format: 16 columns."""
    return {
        "num": cells[0],
        "name": cells[1],
        "region": cells[2],
        "tier": cells[3],
        "platform": cells[4],
        "handle": cells[5],
        "followers": cells[6],
        "engagement": cells[7] if len(cells) > 7 else "--",
        "content_type": cells[8] if len(cells) > 8 else "--",
        "frequency": cells[9] if len(cells) > 9 else "--",
        "relevance": cells[10] if len(cells) > 10 else "--",
        "contact_method": cells[11] if len(cells) > 11 else "--",
        "priority": int(cells[12]) if len(cells) > 12 and cells[12].isdigit() else 0,
        "notes": cells[13] if len(cells) > 13 else "--",
        "updated": cells[14] if len(cells) > 14 else "--",
        "cross_ref": cells[15] if len(cells) > 15 else "--",
        "outreach_status": "not_started"
    }


def parse_short_row(cells, lines, idx):
    """T3/T4 format: 8-9 columns. Infer missing fields from section context."""
    tier = infer_tier_from_section(lines, idx)
    region = cells[2] if len(cells) > 2 and cells[2] in ("GLOBAL", "BR") else infer_region_from_section(lines, idx)

    # Detect column layout from header
    headers = detect_header_columns(lines, idx)
    header_lower = [h.lower().strip() for h in headers]

    # Build a dict mapping header->value
    row_map = {}
    for j, h in enumerate(header_lower):
        if j < len(cells):
            row_map[h] = cells[j]

    name = row_map.get("name", row_map.get("name/community", cells[1] if len(cells) > 1 else "--"))
    platform = row_map.get("platform", cells[3] if len(cells) > 3 else "--")
    handle = row_map.get("handle", row_map.get("members", cells[4] if len(cells) > 4 else "--"))
    followers = row_map.get("followers", row_map.get("members", row_map.get("subscribers", cells[5] if len(cells) > 5 else "--")))
    relevance = row_map.get("relevance", cells[5] if len(cells) > 5 else "--")
    priority_raw = row_map.get("priority", "0")
    notes = row_map.get("notes", cells[-1] if len(cells) > 6 else "--")

    # Try to get priority from the correct column
    priority = 0
    for key in ("priority",):
        val = row_map.get(key, "0")
        if val.isdigit():
            priority = int(val)
            break

    # Fallback: scan cells for a single-digit number that looks like priority
    if priority == 0:
        for c in reversed(cells[4:]):
            if c.isdigit() and 1 <= int(c) <= 10:
                priority = int(c)
                break

    return {
        "num": cells[0],
        "name": name,
        "region": region,
        "tier": tier,
        "platform": platform,
        "handle": handle if handle != followers else "--",
        "followers": followers,
        "engagement": row_map.get("eng.", "--"),
        "content_type": "--",
        "frequency": "--",
        "relevance": relevance if relevance in ("HIGH", "MEDIUM", "LOW") else "--",
        "contact_method": "--",
        "priority": priority,
        "notes": notes,
        "updated": "2026-04-24",
        "cross_ref": "--",
        "outreach_status": "not_started"
    }


def main():
    with open(CRM_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    contacts = []
    for idx, line in enumerate(lines):
        line_s = line.rstrip()
        if not line_s.startswith("|"):
            continue
        cells = parse_cells(line_s)
        if not is_data_row(cells):
            continue

        section = detect_section(lines, idx)
        if section == "skip":
            continue

        if section == "full" and len(cells) >= 14:
            row = parse_full_row(cells)
        elif section in ("t3", "t4", "unknown"):
            row = parse_short_row(cells, lines, idx)
        else:
            row = parse_short_row(cells, lines, idx)

        if row:
            contacts.append(row)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=None)

    # Stats
    tiers = {}
    for c in contacts:
        t = c.get("tier", "?")
        tiers[t] = tiers.get(t, 0) + 1
    print(f"[OK] Extracted {len(contacts)} contacts to {OUT_PATH}")
    for t in sorted(tiers):
        print(f"  {t}: {tiers[t]}")


if __name__ == "__main__":
    main()
