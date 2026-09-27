"""Monthly freshness pass for Track B. Prints a prompt (generates nothing) that re-verifies every stamped product claim.

    python gen_refresh.py            # claims older than 30 days
    python gen_refresh.py --all      # every stamped claim
    python gen_refresh.py --days 14

Track B lessons cite official pages as  [text](url){ .src data-checked="YYYY-MM-DD" }.
Features, limits, prices and policies change monthly, so the stamps are re-checked, not trusted.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date

import lml_common as c

STAMP_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)\{[^}]*data-checked=\"(\d{4}-\d{2}-\d{2})\"[^}]*\}")


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
    print(f"{len(claims)} stamped claims; {len(due)} selected for re-check" + ("" if a.all else f" (older than {a.days} days)") + ".")
    if not due:
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
    print("=" * 72)
    print(f"Paste everything below this line into Claude Code (run from {c.ROOT}):")
    print("=" * 72)
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
