"""Mark lessons done and see where you are.

    python track.py done week-01/day-2 --rating 4 --note "broadcasting aligns from the right"
    python track.py status

Ratings and minutes go to progress/log.jsonl (committed, public).
The free-text note goes to progress/notes.jsonl (git-ignored, stays on this machine).
"""
from __future__ import annotations

import argparse
import sys

import lml_common as c


def cmd_done(args: argparse.Namespace) -> int:
    lesson = args.lesson.strip().replace("\\", "/").removesuffix(".md")
    known = c.lesson_ids()
    if lesson not in known:
        print(f"Unknown lesson '{lesson}'. Known lessons:\n  " + "\n  ".join(known))
        return 1
    if lesson in c.done_lessons() and not args.again:
        print(f"{lesson} is already logged. Use --again to log a repeat session.")
        return 1

    date = args.date or c.today_kst()
    c.append_jsonl(c.LOG, {"date": date, "lesson": lesson, "minutes": args.minutes, "rating": args.rating})
    if args.note:
        c.append_jsonl(c.NOTES, {"date": date, "lesson": lesson, "note": args.note})

    print(f"Logged {lesson}  ({args.minutes} min, rating {args.rating}/5)")
    if args.note:
        print("Note saved locally (progress/notes.jsonl is git-ignored).")
    print_status()
    print('\nNext (one per line in PowerShell):\n  git add -A\n  git commit -m "done ' + lesson + '"\n  git push')
    return 0


def print_status() -> None:
    import build_today

    s = build_today.compute_state()
    print(f"\nStreak: {s['streak']} day(s)")
    for ts in s["tracks"].values():
        head = f"{ts['label']}: week {ts['week']} {ts['week_done']}/{ts['per_week']}, overall {ts['total_done']}/{ts['total']} ({ts['pct']}%)"
        if ts["next"]:
            print(f"{head}\n   next: {ts['next']} - {c.lesson_title(ts['next'])}")
        else:
            print(f"{head}\n   all generated lessons done. Run: {build_today.gen_cmd(ts['track'], ts['week'] + 1)}")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("done", help="mark a lesson done")
    d.add_argument("lesson", help="e.g. week-01/day-2, week-01/build, agentic-01/day-1, agentic-01/apply")
    d.add_argument("--rating", type=int, choices=range(1, 6), required=True, help="self-rating 1-5")
    d.add_argument("--note", default="", help="surprise note (kept local, never committed)")
    d.add_argument("--minutes", type=int, default=20)
    d.add_argument("--date", help="override date, YYYY-MM-DD (default: today in KST)")
    d.add_argument("--again", action="store_true", help="allow logging a lesson a second time")
    d.set_defaults(fn=cmd_done)

    s = sub.add_parser("status", help="active days, completion, next lesson")
    s.set_defaults(fn=lambda a: (print_status(), 0)[1])

    args = p.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
