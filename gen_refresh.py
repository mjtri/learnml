"""Monthly freshness pass for Track B. Prints a prompt (generates nothing) that re-verifies every stamped product claim.

    python gen_refresh.py            # claims older than 30 days
    python gen_refresh.py --all      # every stamped claim
    python gen_refresh.py --days 14

Track B lessons cite official pages as  [text](url){ .src data-checked="YYYY-MM-DD" }.
Features, limits, prices and policies change monthly, so the stamps are re-checked, not trusted.
The tool radar (docs/agentic/radar.md) is a table whose last column is the checked date; each row is
re-scored against the GitHub API and the repo's README on the same schedule.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date

import lml_common as c

STAMP_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)\{[^}]*data-checked=\"(\d{4}-\d{2}-\d{2})\"[^}]*\}")
RADAR = c.DOCS / "agentic" / "radar.md"
RADAR_ROW_RE = re.compile(r"^\|\s*(.+?)\s*\|.*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*$")


def radar_rows() -> list[dict]:
    """Every table row of the tool radar: repo cell, section heading, GitHub URL (if any), checked date."""
    out = []
    if not RADAR.exists():
        return out
    section = ""
    for i, line in enumerate(RADAR.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("## "):
            section = line[3:].strip()
        m = RADAR_ROW_RE.match(line)
        if not m:
            continue
        repo_cell = re.sub(r"\s+", " ", m.group(1))
        link = re.search(r"\]\((https?://github\.com/[^)\s]+)\)", repo_cell)
        out.append({"line": i, "section": section, "repo": re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", repo_cell),
                    "url": link.group(1) if link else "", "checked": m.group(2)})
    return out


def stamped_claims() -> list[dict]:
    out = []
    files = sorted(c.DOCS.glob("agentic-*/*.md")) + sorted((c.DOCS / "agentic").glob("*.md"))
    for path in files:
        text = path.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            for text_, url, stamp in STAMP_RE.findall(line):
                context = re.sub(r"\s+", " ", re.sub(r"\{[^}]*\}", "", line)).strip()
                out.append({"file": str(path.relative_to(c.ROOT)).replace("\\", "/"), "line": i,
                            "text": text_, "url": url, "checked": stamp, "context": context[:220]})
    return out


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--days", type=int, default=30)
    p.add_argument("--all", action="store_true")
    a = p.parse_args()

    today = date.fromisoformat(c.today_kst())
    claims = stamped_claims()
    due = [cl for cl in claims if a.all or (today - date.fromisoformat(cl["checked"])).days >= a.days]
    rows = radar_rows()
    rows_due = [r for r in rows if a.all or (today - date.fromisoformat(r["checked"])).days >= a.days]
    print(f"{len(claims)} stamped claims; {len(due)} selected for re-check" + ("" if a.all else f" (older than {a.days} days)") + ".")
    print(f"{len(rows)} tool-radar rows; {len(rows_due)} selected for re-scoring.")
    if not due and not rows_due:
        print("Nothing to refresh. Rerun with --all to re-verify everything.")
        return 0

    by_url: dict[str, list[dict]] = {}
    for cl in due:
        by_url.setdefault(cl["url"], []).append(cl)

    lines = [f"Refresh pass for LearnML Track B, {today.isoformat()}. Re-verify the product claims below against their official sources. "
             "Do not trust memory; fetch each page. Generate nothing else.", "",
             "For each URL: (1) fetch it; (2) for every claim listed under it, decide CONFIRMED / CHANGED / PAGE MOVED; "
             f"(3) if CONFIRMED, update data-checked to {today.isoformat()}; (4) if CHANGED, rewrite the sentence in the lesson to match the source "
             "(keep it under the lesson's word cap), update the stamp, and add a bullet to docs/agentic/changelog.md under a "
             f"'## {today.isoformat()}' heading: what changed, which lesson, the URL; (5) if PAGE MOVED, find the new official page, update the link, "
             "stamp it, and log it. If a fact can no longer be found on any official page, mark the sentence '(verify)' and log it.", "",
             "Then run: python check_lessons.py && python build_today.py && mkdocs build --strict. Do not commit or push.", "",
             "## Claims by source"]
    for url, cls in by_url.items():
        lines.append(f"\n### {url}")
        for cl in cls:
            lines.append(f"- {cl['file']}:{cl['line']} (checked {cl['checked']}) — \"{cl['context']}\"")
    if rows_due:
        lines += ["", "## Tool radar rows (docs/agentic/radar.md)", "",
                  "For each row: fetch the GitHub API record (stars, pushed_at, open issues, licence) and the current README. "
                  "Re-score with the B9 worth-it rubric (six lines, 0-2 each; adopt at >= 8/12 with no zero on trust). "
                  "If the README's install line changed, rewrite the Install cell. If the score drops below 8, move the row to "
                  "'Read, don't bundle-install' or delete it, and log it in the changelog. No push for 90 days goes in the risk note. "
                  f"Set the Checked cell to {today.isoformat()}. Never install anything during the refresh."]
        for r in rows_due:
            lines.append(f"- radar.md:{r['line']} [{r['section']}] {r['repo']} (checked {r['checked']})"
                         + (f" — {r['url']}" if r["url"] else ""))
    print("=" * 72)
    print(f"Paste everything below this line into Claude Code (run from {c.ROOT}):")
    print("=" * 72)
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
