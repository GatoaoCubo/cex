#!/usr/bin/env python3
"""cex_cohort_analyzer.py: Cohort retention + churn table for N06 commercial.

Takes signup/churn events CSV and computes monthly cohort retention matrix.
No deps beyond stdlib.

Input CSV format:
    user_id,signup_date,churn_date
    42,2026-01-15,2026-03-20
    43,2026-01-20,

Usage:
    python _tools/cex_cohort_analyzer.py --input events.csv
    python _tools/cex_cohort_analyzer.py --demo  # synthetic data
"""
from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta


def parse_date(s: str):
    s = s.strip()
    if not s:
        return None
    return datetime.strptime(s, "%Y-%m-%d").date()


def month_key(d: date) -> str:
    return f"{d.year}-{d.month:02d}"


def month_diff(a: date, b: date) -> int:
    return (b.year - a.year) * 12 + (b.month - a.month)


def build_cohorts(rows: list[dict], horizon_months: int = 6) -> dict:
    cohorts = defaultdict(lambda: {"size": 0, "active": defaultdict(int)})
    today = date.today()

    for row in rows:
        signup = parse_date(row.get("signup_date", ""))
        churn = parse_date(row.get("churn_date", ""))
        if not signup:
            continue
        cohort = month_key(signup)
        cohorts[cohort]["size"] += 1

        for m in range(horizon_months + 1):
            check_date = signup.replace(day=1)
            for _ in range(m):
                # advance 1 month
                y, mo = check_date.year, check_date.month + 1
                if mo > 12:
                    mo = 1
                    y += 1
                check_date = check_date.replace(year=y, month=mo)
            if check_date > today:
                break
            if churn and churn < check_date:
                continue
            cohorts[cohort]["active"][m] += 1

    return dict(cohorts)


def render_table(cohorts: dict, horizon: int = 6) -> str:
    lines = []
    header = "Cohort     Size  " + "".join(f"M{m:<6}" for m in range(horizon + 1))
    lines.append(header)
    lines.append("-" * len(header))
    for cohort in sorted(cohorts.keys()):
        data = cohorts[cohort]
        size = data["size"]
        row = f"{cohort:<10} {size:<5} "
        for m in range(horizon + 1):
            active = data["active"].get(m, 0)
            pct = (active / size * 100) if size else 0
            row += f"{pct:>5.1f}% "
        lines.append(row)
    return "\n".join(lines)


def generate_demo_data(n: int = 200) -> list[dict]:
    rng = random.Random(42)
    rows = []
    base = date(2026, 1, 1)
    for i in range(n):
        signup = base + timedelta(days=rng.randint(0, 90))
        churn = None
        if rng.random() < 0.35:
            churn = signup + timedelta(days=rng.randint(14, 120))
        rows.append({
            "user_id": str(i),
            "signup_date": signup.isoformat(),
            "churn_date": churn.isoformat() if churn else "",
        })
    return rows


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--input", help="CSV with user_id,signup_date,churn_date")
    p.add_argument("--demo", action="store_true", help="use synthetic data")
    p.add_argument("--horizon", type=int, default=6)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    if args.demo:
        rows = generate_demo_data()
    elif args.input:
        with open(args.input, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    else:
        p.error("provide --input or --demo")

    cohorts = build_cohorts(rows, args.horizon)

    if args.json:
        out = {}
        for c, d in cohorts.items():
            out[c] = {"size": d["size"], "retention": {str(m): v for m, v in d["active"].items()}}
        print(json.dumps(out, indent=2))
    else:
        print(f"Analyzed {len(rows)} users across {len(cohorts)} cohorts\n")
        print(render_table(cohorts, args.horizon))
    return 0


if __name__ == "__main__":
    sys.exit(main())
