#!/usr/bin/env python3
"""Score LinkedIn posts against each creator's own baseline and flag outliers.

Usage:
    python score_outliers.py posts.csv [--today YYYY-MM-DD] [--min-age-days 3] [--json]

The CSV needs a header row. Column names are matched loosely (case and spacing
don't matter). Recognised columns:

    creator      (required) the account that posted
    reactions    (required) likes/reactions count, e.g. 1,234 or 1.2K
    comments     (required) comment count
    reposts      (optional) repost count
    age          (optional) how old the post is, e.g. 5h, 3d, 2w, 1mo, 1yr
    date         (optional) post date as YYYY-MM-DD (used if age is missing)
    format       (optional) text / image / carousel / video / poll / other
    first_line   (optional) the hook, or first line of the post
    url          (optional) link to the post

Engagement score = reactions + 2 x comments + 3 x reposts.
Comments and reposts take more effort than a reaction and push a post further,
so they count for more. It's a heuristic, not LinkedIn's formula.

Posts younger than --min-age-days are still collecting engagement, so they
are left out of baselines and listed separately instead of being scored.
Only standard-library Python is used.
"""

import argparse
import csv
import json
import re
import statistics
import sys
from datetime import date, datetime

ALIASES = {
    "creator": ["creator", "author", "account", "name", "profile", "person"],
    "reactions": ["reactions", "likes", "reaction", "like"],
    "comments": ["comments", "comment"],
    "reposts": ["reposts", "repost", "shares", "share", "reshares"],
    "age": ["age", "posted", "time", "posted ago", "ago"],
    "date": ["date", "posted date", "post date", "published"],
    "format": ["format", "type", "post type", "media"],
    "first_line": ["first line", "first_line", "hook", "opening", "text", "post"],
    "url": ["url", "link", "post url"],
}


def norm(s):
    return re.sub(r"[\s_\-]+", " ", (s or "").strip().lower())


def map_columns(header):
    mapping = {}
    normed = {norm(h): h for h in header}
    for key, options in ALIASES.items():
        for opt in options:
            if norm(opt) in normed:
                mapping[key] = normed[norm(opt)]
                break
    return mapping


def parse_count(value):
    """'1,234' -> 1234, '1.2K' -> 1200, '3k' -> 3000, '' -> None."""
    if value is None:
        return None
    s = str(value).strip().lower().replace(",", "")
    if not s or s in {"-", "n/a", "na", "none"}:
        return None
    m = re.match(r"^([\d.]+)\s*([km]?)", s)
    if not m:
        return None
    try:
        num = float(m.group(1))
    except ValueError:
        return None
    if m.group(2) == "k":
        num *= 1000
    elif m.group(2) == "m":
        num *= 1_000_000
    return int(round(num))


AGE_UNITS = {
    "h": 1 / 24, "hr": 1 / 24, "hrs": 1 / 24, "hour": 1 / 24, "hours": 1 / 24,
    "d": 1, "day": 1, "days": 1,
    "w": 7, "wk": 7, "week": 7, "weeks": 7,
    "mo": 30, "mos": 30, "month": 30, "months": 30,
    "y": 365, "yr": 365, "yrs": 365, "year": 365, "years": 365,
}


def parse_age_days(age, date_str, today):
    if age:
        m = re.match(r"^\s*(\d+(?:\.\d+)?)\s*([a-z]+)", str(age).strip().lower())
        if m and m.group(2) in AGE_UNITS:
            return float(m.group(1)) * AGE_UNITS[m.group(2)]
        if m and m.group(2).startswith("min"):
            return 0.0
    if date_str:
        for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d %b %Y", "%b %d, %Y"):
            try:
                d = datetime.strptime(str(date_str).strip(), fmt).date()
                return float((today - d).days)
            except ValueError:
                continue
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv_path")
    ap.add_argument("--today", help="YYYY-MM-DD, defaults to today")
    ap.add_argument("--min-age-days", type=float, default=3.0)
    ap.add_argument("--outlier-x", type=float, default=3.0, help="multiple of median that counts as an outlier")
    ap.add_argument("--strong-x", type=float, default=2.0, help="multiple of median that counts as strong")
    ap.add_argument("--json", action="store_true", help="print JSON instead of markdown")
    args = ap.parse_args()

    today = datetime.strptime(args.today, "%Y-%m-%d").date() if args.today else date.today()

    with open(args.csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        cols = map_columns(reader.fieldnames or [])
        missing = [c for c in ("creator", "reactions", "comments") if c not in cols]
        if missing:
            sys.exit(f"Missing required column(s): {', '.join(missing)}. Found: {reader.fieldnames}")
        rows = list(reader)

    posts, too_new, unscored = [], [], []
    for i, r in enumerate(rows, start=1):
        get = lambda k: r.get(cols[k]) if k in cols else None
        creator = (get("creator") or "").strip()
        reactions = parse_count(get("reactions"))
        comments = parse_count(get("comments"))
        reposts = parse_count(get("reposts")) or 0
        if not creator or reactions is None or comments is None:
            unscored.append({"row": i, "reason": "missing creator, reactions or comments"})
            continue
        age_days = parse_age_days(get("age"), get("date"), today)
        post = {
            "row": i,
            "creator": creator,
            "format": (get("format") or "").strip(),
            "first_line": (get("first_line") or "").strip(),
            "url": (get("url") or "").strip(),
            "reactions": reactions,
            "comments": comments,
            "reposts": reposts,
            "age_days": age_days,
            "score": reactions + 2 * comments + 3 * reposts,
        }
        if age_days is not None and age_days < args.min_age_days:
            too_new.append(post)
        else:
            posts.append(post)

    by_creator = {}
    for p in posts:
        by_creator.setdefault(p["creator"], []).append(p)

    creators, scored = [], []
    for name, items in sorted(by_creator.items()):
        n = len(items)
        med = statistics.median([p["score"] for p in items]) if items else 0
        if n < 5 or med <= 0:
            baseline = "skipped (fewer than 5 settled posts)" if n < 5 else "skipped (median is zero)"
        elif n < 8:
            baseline = "thin (5 to 7 posts)"
        else:
            baseline = "ok"
        creators.append({"creator": name, "posts": n, "median_score": med, "baseline": baseline})
        if baseline.startswith("skipped"):
            continue
        for p in items:
            p["x_median"] = round(p["score"] / med, 2)
            p["baseline"] = baseline
            scored.append(p)

    scored.sort(key=lambda p: p["x_median"], reverse=True)
    outliers = [p for p in scored if p["x_median"] >= args.outlier_x]
    strong = [p for p in scored if args.strong_x <= p["x_median"] < args.outlier_x]

    result = {
        "today": today.isoformat(),
        "settings": {"min_age_days": args.min_age_days, "outlier_x": args.outlier_x, "strong_x": args.strong_x,
                     "score": "reactions + 2*comments + 3*reposts"},
        "creators": creators,
        "outliers": outliers,
        "strong": strong,
        "too_new": too_new,
        "unscored_rows": unscored,
        "creators_with_outliers": sorted({p["creator"] for p in outliers}),
    }

    if args.json:
        print(json.dumps(result, indent=2))
        return

    def short(s, n=90):
        s = (s or "").replace("|", "/").replace("\n", " ")
        return s if len(s) <= n else s[: n - 1] + "…"

    out = [f"# Outlier scoring · {today.isoformat()}", ""]
    out.append(f"Score = reactions + 2 x comments + 3 x reposts. Outlier = {args.outlier_x:g}x the creator's median or more. "
               f"Posts newer than {args.min_age_days:g} days are excluded.")
    out.append("")
    out.append("## Baselines")
    out.append("| Creator | Settled posts | Median score | Baseline |")
    out.append("|---|---|---|---|")
    for c in creators:
        out.append(f"| {c['creator']} | {c['posts']} | {c['median_score']:g} | {c['baseline']} |")
    for label, items in (("Outliers", outliers), ("Strong performers", strong)):
        out.append("")
        out.append(f"## {label} ({len(items)})")
        if not items:
            out.append("None.")
            continue
        out.append("| x median | Creator | Format | First line | Reactions | Comments | Reposts | Age (days) | Link |")
        out.append("|---|---|---|---|---|---|---|---|---|")
        for p in items:
            age = "" if p["age_days"] is None else f"{p['age_days']:.0f}"
            flag = " (thin baseline)" if p["baseline"].startswith("thin") else ""
            out.append(f"| {p['x_median']:g}x{flag} | {p['creator']} | {p['format']} | {short(p['first_line'])} | "
                       f"{p['reactions']} | {p['comments']} | {p['reposts']} | {age} | {p['url']} |")
    if too_new:
        out.append("")
        out.append(f"## Too new to score ({len(too_new)})")
        for p in too_new:
            out.append(f"- {p['creator']}: {short(p['first_line'], 70)} ({p['score']} so far)")
    if unscored:
        out.append("")
        out.append(f"## Rows skipped ({len(unscored)})")
        for u in unscored:
            out.append(f"- row {u['row']}: {u['reason']}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
