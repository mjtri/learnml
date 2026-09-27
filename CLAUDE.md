@AGENTS.md

## Claude Code specifics

- Prefer plan mode for anything that touches more than one lesson.
- Use a subagent for link verification and web research; keep only the summary in the main context.
- Before finishing a week: `python check_lessons.py`, `python build_today.py`, `mkdocs build --strict`, and a 390 px viewport check of every new visual in the built-in browser.
