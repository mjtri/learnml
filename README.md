# LearnML

Just enough ML to use and modify models: 12 weeks, phone-first, one week generated at a time.

- **Read:** <https://mjtri.github.io/learnml/> (Today's lesson is the home page)
- **Plan:** [curriculum.md](curriculum.md)
- **Daily routine and the three commands:** [LOOP.md](LOOP.md)
- **Lesson / visual / notebook contract:** [LESSON_FORMAT.md](LESSON_FORMAT.md)

```
docs/week-NN/day-1..5.md, build.md   lessons (≤ 800 words, one visual, 3 retrieval questions)
docs/visuals/*.html                  self-contained touch-friendly visuals (≤ 60 KB, no network)
notebooks/week-NN.ipynb              Colab build sessions with predict-before-you-run cells
glossary/terms.jsonl                 single source for tap-to-define terms
progress/log.jsonl                   date, lesson, minutes, rating (notes.jsonl stays local)
anki/week-NN.txt                     exported cards
track.py · build_today.py · gen_week.py · build_anki.py · build_glossary.py · check_lessons.py · setup_repo.py
```

Quick start: `python setup_repo.py <github-user> <repo>`, then follow "One-time setup" in [LOOP.md](LOOP.md).
