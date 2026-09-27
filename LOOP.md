# The loop

Self-paced. Phone sessions of ~20 min (ML) or ~15 min (agentic) whenever you have them; a ~3 h laptop build session per content week (Colab notebook + the Track B apply task). Nothing assumes a lesson takes a day. Four commands keep it running.

## Each phone session

1. Open the site from your home screen. The first thing on screen is **Next up** for each track, plus a full map of every week.
2. Read it. Tap any dotted-underlined word for its definition. Do the visual's "predict first" prompts. Answer the three retrieval questions *before* opening them.
3. Write the one-line **ledger prompt** answer: ML lessons go next to the named card in the Obsidian canvas; agentic lessons go into `docs/agentic/playbook.md` (or a phone note to paste later).

## (a) Mark done: laptop, 30 seconds

Run once per lesson you finished; catch up several days at once with `--date`.

```bash
python track.py done week-01/day-2 --rating 4 --note "broadcasting aligns from the right"
```

- `--rating` 1–5: 1 = lost, 3 = got it with effort, 5 = easy. Low ratings steer next week's content.
- `--note` is your surprise note. It goes to `progress/notes.jsonl`, which is **git-ignored**: it never leaves this machine. Only date, lesson, minutes and rating are committed.
- Optional: `--minutes 25` (default 20), `--date 2026-09-22` (default: today, KST), `--again` to log a repeat.
- `python track.py status` shows active days, completion and the next lesson per track.

## (b) Regenerate a week (optional)

```bash
python gen_week.py 2
```

```bash
python gen_week.py agentic 2
```

Every week already exists. If a week landed badly (low ratings, wrong level), this **prints a prompt** to rebuild it; it generates nothing itself. Paste the prompt into Claude Code; it carries the curriculum section, the lesson contract, your ratings, the glossary and the quality checks. Add `--force` because the week's folder exists.

## (c) Deploy

```bash
git add -A
```

```bash
git commit -m "progress"
```

```bash
git push
```

(One command per line: Windows PowerShell 5 does not accept `&&`.)

The GitHub Actions workflow (`.github/workflows/deploy.yml`) runs `check_lessons.py` and `build_today.py` and publishes to GitHub Pages in about a minute. It also runs by itself at 00:05 KST so the streak stays honest on days you do not push.

Preview locally first if you like:

```bash
python build_today.py
```

```bash
mkdocs serve
```

then open <http://127.0.0.1:8000/> (append your repo name as the path if `site_url` has one).

## (d) Monthly: refresh Track B's product claims

```bash
python gen_refresh.py
```

Track B lessons cite features, limits and prices with a `checked YYYY-MM-DD` badge. Once a month (or when the checker warns a stamp is over 60 days old) run this; it prints a prompt that re-fetches every stamped source, corrects what changed, and logs it in `docs/agentic/changelog.md`.

## Weekly rhythm

| When | What | Where |
|---|---|---|
| Phone sessions | one lesson at a time, either track, in any order you like within a week | phone |
| Build session (per content week) | Track B apply task (~60 min), then the Colab notebook | laptop |
| After build | paste the prediction table into the ledger; `track.py done week-NN/build …` | laptop |
| Any time | import `anki/week-NN.txt` into Anki (File → Import) for spaced repetition | phone/laptop |

## One-time setup

1. Create a **public** GitHub repo and note `<user>` and `<repo>`.
2. `python setup_repo.py <user> <repo>` fills the placeholders (site URL, repo URL, Colab badges).
3. `pip install -r requirements.txt`
4. `git remote add origin https://github.com/<user>/<repo>.git`, then commit and `git push -u origin main`.
5. On GitHub: **Settings → Pages → Build and deployment → Source: "Deploy from a branch" → Branch: `gh-pages` / root.** The branch appears after the first workflow run (Actions tab). If the workflow cannot push, set Settings → Actions → General → Workflow permissions to "Read and write".
6. On the phone: open `https://<user>.github.io/<repo>/`, then *Add to Home Screen* (Safari: Share menu; Chrome: ⋮ menu).

## Files you touch vs files that are generated

| You edit | Generated (do not edit) |
|---|---|
| `curriculum.md`, `docs/week-NN/*.md`, `docs/agentic-NN/*.md`, `docs/agentic/playbook.md`, `docs/agentic/changelog.md`, `docs/visuals/*.html`, `notebooks/*.ipynb`, `glossary/terms-*.jsonl`, `AGENTS.md`, `CLAUDE.md` | `docs/index.md`, `docs/glossary.md`, `docs/curriculum.md`, `includes/glossary.md`, `docs/javascripts/glossary-map.js`, `anki/*.txt`, the `nav:` block of `mkdocs.yml` |

Add a glossary term: append one JSON line to the week's `glossary/terms-<week-dir>.jsonl`, then `python build_today.py`. Every page picks it up.
