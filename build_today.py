"""Generate docs/index.md (Today's lesson, streak, completion %), docs/curriculum.md and the glossary.

Run locally before `mkdocs serve`, and automatically in the deploy workflow.
"Today's lesson" is the first lesson without a log entry, so a missed day never skips content.
"""
from __future__ import annotations

from datetime import date, timedelta

import build_glossary
import lml_common as c


def compute_streak(dates: set[str], today: str) -> int:
    """Consecutive days with an entry, ending today (or yesterday, so the streak survives until you study)."""
    day = date.fromisoformat(today)
    if day.isoformat() not in dates:
        day -= timedelta(days=1)
    n = 0
    while day.isoformat() in dates:
        n += 1
        day -= timedelta(days=1)
    return n


def compute_state() -> dict:
    log = c.read_jsonl(c.LOG)
    lessons = c.lesson_ids()
    done = {r["lesson"] for r in log}
    nxt = next((l for l in lessons if l not in done), None)

    if nxt:
        week = int(nxt[5:7])
    elif lessons:
        week = int(lessons[-1][5:7])
    else:
        week = 1
    week_lessons = [f"{c.week_dir(week)}/{s}" for s in c.WEEK_SLOTS]
    total = c.TOTAL_WEEKS * c.LESSONS_PER_WEEK
    total_done = len(done & set(lessons))
    return {
        "today": c.today_kst(),
        "next": nxt,
        "week": week,
        "week_lessons": week_lessons,
        "week_done": len(done & set(week_lessons)),
        "done": done,
        "total": total,
        "total_done": total_done,
        "pct": round(100 * total_done / total),
        "streak": compute_streak({r["date"] for r in log}, c.today_kst()),
        "minutes": sum(int(r.get("minutes", 0)) for r in log),
        "generated": lessons,
    }


def bar(label: str, done: int, total: int) -> str:
    return (f'<div class="bar"><span>{label}: {done}/{total}</span>'
            f'<progress value="{done}" max="{total}"></progress></div>')


def render_index(s: dict) -> str:
    out = ["---", "title: Today", "hide:", "  - toc", "---", "", "# LearnML", ""]

    if s["next"]:
        kind = "Build session (laptop + Colab, ~3 h)" if s["next"].endswith("/build") else "Phone lesson (~20 min)"
        out += [
            '<div class="today-card" markdown>',
            f'<span class="today-kicker">Today · {kind}</span>',
            "",
            f"## [{c.lesson_title(s['next'])}]({s['next']}.md)",
            "",
            f"[Start lesson →]({s['next']}.md){{ .md-button .md-button--primary }}",
            "</div>",
            "",
        ]
    else:
        out += [
            '<div class="today-card" markdown>',
            '<span class="today-kicker">Week complete</span>',
            "",
            f"## Generate week {s['week'] + 1}",
            "",
            f"On the laptop: `python gen_week.py {s['week'] + 1}` and paste the printed prompt into Claude Code.",
            "</div>",
            "",
        ]

    wk_pct = round(100 * s["week_done"] / c.LESSONS_PER_WEEK)
    out += [
        '<div class="stats" markdown>',
        f'<div class="stat"><b>{s["streak"]}</b><span>day streak</span></div>',
        f'<div class="stat"><b>{wk_pct}%</b><span>week {s["week"]}</span></div>',
        f'<div class="stat"><b>{s["pct"]}%</b><span>of 12 weeks</span></div>',
        "</div>",
        "",
        bar(f"Week {s['week']}", s["week_done"], c.LESSONS_PER_WEEK),
        bar("All 12 weeks", s["total_done"], s["total"]),
        "",
        f"<small>{s['minutes']} minutes logged so far.</small>",
        "",
        f"## Week {s['week']}",
        "",
    ]
    for lesson in s["week_lessons"]:
        if lesson in s["generated"]:
            mark = "✅" if lesson in s["done"] else "⬜"
            here = " ← today" if lesson == s["next"] else ""
            out.append(f"- {mark} [{c.lesson_title(lesson)}]({lesson}.md){here}")
    if s["week_done"] / c.LESSONS_PER_WEEK >= 0.8 and s["week"] < c.TOTAL_WEEKS:
        out += ["", f"!!! tip \"Week {s['week']} is ≥ 80% done\"",
                f"    Time to generate the next one: `python gen_week.py {s['week'] + 1}`"]
    out += [
        "",
        "## After the lesson",
        "",
        "1. Write the **ledger prompt** answer next to the named card in your Obsidian canvas.",
        "2. On the laptop: `python track.py done <lesson-id> --rating 1-5 --note \"what surprised me\"`",
        "3. `git push`: the site rebuilds itself. Details: `LOOP.md` in the repo.",
        "",
        "Stuck on a word? Tap any dotted-underlined term, or open the [glossary](glossary.md).",
        "",
        f"<small>Generated {s['today']} (KST) by `build_today.py`. Do not edit by hand.</small>",
        "",
    ]
    return "\n".join(out)


def main() -> None:
    build_glossary.main()
    s = compute_state()
    (c.DOCS / "index.md").write_text(render_index(s), encoding="utf-8", newline="\n")

    cur = (c.ROOT / "curriculum.md").read_text(encoding="utf-8")
    header = "<!-- Generated from /curriculum.md by build_today.py. Edit the root file, not this one. -->\n\n"
    (c.DOCS / "curriculum.md").write_text(header + cur, encoding="utf-8", newline="\n")

    nxt = s["next"] or f"(week {s['week']} complete)"
    print(f"index.md written. Today: {nxt} | streak {s['streak']} | week {s['week']}: "
          f"{s['week_done']}/{c.LESSONS_PER_WEEK} | overall {s['pct']}%")


if __name__ == "__main__":
    main()
