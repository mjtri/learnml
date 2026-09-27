"""Generate docs/index.md (Next up per track, active days, progress map), the nav in mkdocs.yml,
docs/curriculum.md and the glossary.

Run locally before `mkdocs serve`, and automatically in the deploy workflow. Self-paced: "Next up" is the
first lesson without a log entry; nothing depends on the calendar.
"""
from __future__ import annotations

import re

import build_glossary
import lml_common as c


def gen_cmd(track: str, week: int) -> str:
    return f"python gen_week.py {week}" if track == "ml" else f"python gen_week.py agentic {week}"


def track_state(track: str, done: set[str]) -> dict:
    t = c.TRACKS[track]
    lessons = c.lesson_ids(track)
    nxt = next((l for l in lessons if l not in done), None)
    if nxt:
        week = c.week_of(nxt)
    elif lessons:
        week = c.week_of(lessons[-1])
    else:
        week = 1
    week_lessons = [f"{c.week_dir(week, track)}/{s}" for s in t["slots"]]
    total = t["weeks"] * len(t["slots"])
    total_done = len(done & set(lessons))
    weeks_present = sorted({c.week_of(l) for l in lessons})
    return {
        "track": track, "label": t["label"], "next": nxt, "week": week, "weeks": t["weeks"],
        "week_lessons": week_lessons, "per_week": len(t["slots"]),
        "week_done": len(done & set(week_lessons)),
        "total": total, "total_done": total_done, "pct": round(100 * total_done / total),
        "generated": lessons, "weeks_present": weeks_present, "long": t["long"],
    }


def compute_state() -> dict:
    log = c.read_jsonl(c.LOG)
    done = {r["lesson"] for r in log}
    return {
        "today": c.today_kst(),
        "done": done,
        "active_days": len({r["date"] for r in log}),
        "minutes": sum(int(r.get("minutes", 0)) for r in log),
        "tracks": {name: track_state(name, done) for name in c.TRACKS},
    }


def bar(label: str, done: int, total: int) -> str:
    return (f'<div class="bar"><span>{label}: {done}/{total}</span>'
            f'<progress value="{done}" max="{total}"></progress></div>')


def next_card(ts: dict) -> list[str]:
    if ts["next"]:
        if ts["next"].endswith("/" + ts["long"]):
            kind = "Build session (laptop + Colab, ~3 h)" if ts["track"] == "ml" else "Apply it (laptop, ~60 min)"
        else:
            kind = "Phone lesson (~20 min)" if ts["track"] == "ml" else "Phone lesson (~15 min)"
        return [
            f'<div class="today-card {ts["track"]}" markdown>',
            f'<span class="today-kicker">{ts["label"]} · next up · {kind}</span>',
            "",
            f"## [{c.lesson_title(ts['next'])}]({ts['next']}.md)",
            "",
            f"<small>Week {ts['week']} · {c.week_title(c.week_dir(ts['week'], ts['track']))}</small>",
            "",
            f"[Start →]({ts['next']}.md){{ .md-button .md-button--primary }}",
            "</div>",
            "",
        ]
    return [
        f'<div class="today-card {ts["track"]}" markdown>',
        f'<span class="today-kicker">{ts["label"]} · complete</span>',
        "",
        "## Every lesson in this track is done",
        "",
        "Revisit anything from the map below, or regenerate a week you want rewritten with "
        f"`{gen_cmd(ts['track'], ts['week'])}`.",
        "</div>",
        "",
    ]


def progress_map(s: dict, ts: dict) -> list[str]:
    out = [f"## {ts['label']} · map", ""]
    for n in range(1, ts["weeks"] + 1):
        wdir = c.week_dir(n, ts["track"])
        lessons = [l for l in ts["generated"] if l.startswith(wdir + "/")]
        if not lessons:
            out.append(f'??? note "Week {n} · {c.week_title(wdir)} · not generated yet"')
            out.append(f"    `{gen_cmd(ts['track'], n)}` prints the prompt that builds it.")
            out.append("")
            continue
        done_n = len([l for l in lessons if l in s["done"]])
        state = "✅" if done_n == len(lessons) else ("▶" if any(l == ts["next"] for l in lessons) else "⬜")
        open_flag = "+" if any(l == ts["next"] for l in lessons) else ""
        out.append(f'???{open_flag} note "{state} Week {n} · {c.week_title(wdir)} · {done_n}/{len(lessons)}"')
        for lesson in lessons:
            mark = "✅" if lesson in s["done"] else "⬜"
            here = " ← next" if lesson == ts["next"] else ""
            out.append(f"    - {mark} [{c.lesson_title(lesson)}]({lesson}.md){here}")
        out.append("")
    return out


def render_index(s: dict) -> str:
    ml, ag = s["tracks"]["ml"], s["tracks"]["agentic"]
    out = ["---", "title: Next up", "hide:", "  - toc", "---", "", "# LearnML", ""]
    out += next_card(ml)
    out += next_card(ag)
    out += [
        '<div class="stats" markdown>',
        f'<div class="stat"><b>{s["active_days"]}</b><span>active days</span></div>',
        f'<div class="stat"><b>{ml["pct"]}%</b><span>ML · 12 wk</span></div>',
        f'<div class="stat"><b>{ag["pct"]}%</b><span>agentic · 8 wk</span></div>',
        "</div>",
        "",
        bar("Track A", ml["total_done"], ml["total"]),
        bar("Track B", ag["total_done"], ag["total"]),
        "",
        f"<small>{s['minutes']} minutes logged. Self-paced: a \"week\" is a unit of content, not a calendar week.</small>",
        "",
    ]
    out += progress_map(s, ml)
    out += progress_map(s, ag)
    out += [
        "## After a lesson",
        "",
        "1. Write the **ledger prompt** answer: ML lessons → next to the named card in your Obsidian canvas; "
        "agentic lessons → your [playbook](agentic/playbook.md).",
        "2. On the laptop: `python track.py done <lesson-id> --rating 1-5 --note \"what surprised me\"`",
        "3. `git push`: the site rebuilds itself. Details: `LOOP.md` in the repo.",
        "",
        "Stuck on a word? Tap any dotted-underlined term, or open the [glossary](glossary.md).",
        "",
        f"<small>Generated {s['today']} (KST) by `build_today.py`. Do not edit by hand.</small>",
        "",
    ]
    return "\n".join(out)


def render_nav() -> str:
    """Nav from disk: one group per week, titles from front matter; agents never edit mkdocs.yml."""
    lines = ["nav:", "  - Next up: index.md"]
    for track in c.TRACKS:
        weeks = sorted({l.split("/")[0] for l in c.lesson_ids(track)})
        for wdir in weeks:
            n = c.week_of(wdir + "/x")
            label = f"Track A · Week {n} · {c.week_title(wdir)}" if track == "ml" else f"Track B · {n} · {c.week_title(wdir)}"
            lines.append(f"  - \"{label}\":")
            for lesson in c.lesson_ids(track):
                if lesson.startswith(wdir + "/"):
                    title = c.lesson_title(lesson).replace('"', "'")
                    lines.append(f"      - \"{title}\": {lesson}.md")
        if track == "agentic":
            lines.append("  - \"Track B · Playbook\": agentic/playbook.md")
            lines.append("  - \"Track B · Changelog\": agentic/changelog.md")
    lines += ["  - Glossary: glossary.md", "  - Curriculum: curriculum.md"]
    return "\n".join(lines) + "\n"


def write_nav() -> None:
    path = c.ROOT / "mkdocs.yml"
    text = path.read_text(encoding="utf-8")
    m = re.search(r"# nav:begin\n.*?# nav:end\n", text, re.S)
    if not m:
        raise SystemExit("mkdocs.yml needs '# nav:begin' and '# nav:end' marker lines around the nav block")
    new = "# nav:begin\n" + render_nav() + "# nav:end\n"
    if new != m.group(0):
        path.write_text(text[:m.start()] + new + text[m.end():], encoding="utf-8", newline="\n")


def main() -> None:
    build_glossary.main()
    write_nav()
    s = compute_state()
    (c.DOCS / "index.md").write_text(render_index(s), encoding="utf-8", newline="\n")

    cur = (c.ROOT / "curriculum.md").read_text(encoding="utf-8")
    header = "<!-- Generated from /curriculum.md by build_today.py. Edit the root file, not this one. -->\n\n"
    (c.DOCS / "curriculum.md").write_text(header + cur, encoding="utf-8", newline="\n")

    parts = []
    for ts in s["tracks"].values():
        nxt = ts["next"] or "(complete)"
        parts.append(f"{ts['track']}: next {nxt}, {ts['total_done']}/{ts['total']} ({ts['pct']}%)")
    print(f"index.md + nav written. active days {s['active_days']} | " + " | ".join(parts))


if __name__ == "__main__":
    main()
