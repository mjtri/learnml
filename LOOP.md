# The loop

Phone every day (~20 min). Laptop once a week (~3 h). Three commands keep it running.

## Every day (phone)

1. Open the site from your home screen. The first thing on screen is **Today's lesson**.
2. Read it. Tap any dotted-underlined word for its definition. Do the visual's "predict first" prompts. Answer the three retrieval questions *before* opening them.
3. Write the one-line **ledger prompt** answer next to the named card in the Obsidian canvas (or in a phone note to paste later).

## (a) Mark done: laptop, 30 seconds

Run once per lesson you finished; catch up several days at once with `--date`.

```bash
python track.py done week-01/day-2 --rating 4 --note "broadcasting aligns from the right"
```

- `--rating` 1–5: 1 = lost, 3 = got it with effort, 5 = easy. Low ratings steer next week's content.
- `--note` is your surprise note. It goes to `progress/notes.jsonl`, which is **git-ignored**: it never leaves this machine. Only date, lesson, minutes and rating are committed.
- Optional: `--minutes 25` (default 20), `--date 2026-09-22` (default: today, KST), `--again` to log a repeat.
- `python track.py status` shows streak, completion and the next lesson.

## (b) Generate next week: when the current week is ≥ 80 % done (5 of 6)

```bash
python gen_week.py 2
```

This **prints a prompt**; it generates nothing. Open Claude Code in this folder and paste the prompt. It carries the week's curriculum section, the lesson format contract, your ratings, the glossary so far, and the quality checks. Review what comes back before committing. If the week is under 80 % the script tells you what is still open (`--force` overrides).

## (c) Deploy

```bash
git add -A && git commit -m "progress" && git push
```

The GitHub Actions workflow (`.github/workflows/deploy.yml`) runs `check_lessons.py` and `build_today.py` and publishes to GitHub Pages in about a minute. It also runs by itself at 00:05 KST so the streak stays honest on days you do not push.

Preview locally first if you like:

```bash
python build_today.py && mkdocs serve
```

then open <http://127.0.0.1:8000/> (append your repo name as the path if `site_url` has one).

## Weekly rhythm

| When | What | Where |
|---|---|---|
| Mon–Fri | one phone lesson a day | phone |
| Weekend | build session: Colab notebook, predict before every run | laptop |
| After build | paste the prediction table into the ledger; `track.py done week-NN/build …` | laptop |
| Then | `python gen_week.py N+1` → paste into Claude Code → review → push | laptop |
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
| `curriculum.md`, `docs/week-NN/*.md`, `docs/visuals/*.html`, `notebooks/*.ipynb`, `glossary/terms.jsonl` | `docs/index.md`, `docs/glossary.md`, `docs/curriculum.md`, `includes/glossary.md`, `docs/javascripts/glossary-map.js`, `anki/*.txt` |

Add a glossary term: append one JSON line to `glossary/terms.jsonl`, then `python build_today.py`. Every page picks it up.
