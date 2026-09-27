# LearnML

Two parallel phone-first, self-paced tracks:
- **Track A · ML** (12 weeks): just enough ML to use and modify models.
- **Track B · Agentic workflows** (8 weeks): getting full value from Claude Code Max and ChatGPT Business without wasting usage; every product claim carries a checked-date badge and `gen_refresh.py` re-verifies them monthly.

- **Read:** <https://mjtri.github.io/learnml/> (Next up + progress map is the home page)
- **Plan:** [curriculum.md](curriculum.md)
- **Daily routine and the four commands:** [LOOP.md](LOOP.md)
- **Lesson / visual / notebook contract:** [LESSON_FORMAT.md](LESSON_FORMAT.md)

```
docs/week-NN/day-1..5.md, build.md   Track A lessons (≤ 800 words, one visual, 3 retrieval questions)
docs/agentic-NN/day-1..3.md, apply.md Track B lessons (≤ 700 words, visual or worked example, stamped claims)
docs/agentic/playbook.md, changelog.md  your workflow rules; what changed since lessons were written
docs/visuals/*.html                  self-contained touch-friendly visuals (≤ 60 KB, no network)
notebooks/week-NN.ipynb              Colab build sessions with predict-before-you-run cells
glossary/terms-<week>.jsonl          per-week shards for tap-to-define terms (OWNERSHIP.md says who defines what)
progress/log.jsonl                   date, lesson, minutes, rating (notes.jsonl stays local)
anki/week-NN.txt                     exported cards
track.py · build_today.py · gen_week.py · gen_refresh.py · build_anki.py · build_glossary.py · check_lessons.py · setup_repo.py
AGENTS.md (+ CLAUDE.md importing it)  instructions both agents read
```

Quick start: `python setup_repo.py <github-user> <repo>`, then follow "One-time setup" in [LOOP.md](LOOP.md).
