"""Quality gate for lessons and visuals. Exit code 1 on any error (warnings do not fail).

Checks: <= 800 words per lesson, required sections, exactly 3 retrieval questions (phone lessons),
one iframe whose target exists, visuals <= 60 KB with no network access, code blocks <= 12 lines,
every front-matter term is in the glossary, and common jargon is not used undefined.
"""
from __future__ import annotations

import re
import sys

import lml_common as c

MAX_WORDS = 800
MAX_VISUAL_BYTES = 60 * 1024
MAX_CODE_LINES = 12
SECTIONS = ["## Idea", "## Mechanism", "## Try it", "## Retrieval", "## Sources", "## Ledger prompt"]
NETWORK_RE = re.compile(r"https?://|(?<![:\w])//[a-z0-9.-]+\.[a-z]{2,}|\bfetch\(|XMLHttpRequest|WebSocket|@import|\.src\s*=", re.I)
# Jargon that must never appear in a lesson without a glossary entry. Extend as weeks are added.
WATCHLIST = ["logits", "epoch", "backprop", "backpropagation", "softmax", "embedding", "batch", "loss",
             "gradient", "tensor", "parameter", "weights", "bias", "activation", "optimizer", "overfitting",
             "learning rate", "autograd", "inference", "hyperparameter", "token", "attention", "fine-tuning",
             "checkpoint", "regularization", "normalization", "cross-entropy", "LoRA", "rank"]


def main() -> int:
    errors, warnings = [], []
    known = set()
    for e in c.load_terms():
        known.update(t.lower() for t in [e["term"], *e.get("aliases", [])])
        if len(e["def"].split()) > 30:
            warnings.append(f"glossary: '{e['term']}' definition is {len(e['def'].split())} words (> 30)")
        if e.get("lesson") and e["lesson"] not in c.lesson_ids():
            errors.append(f"glossary: '{e['term']}' points at missing lesson {e['lesson']}")

    for lesson in c.lesson_ids():
        meta, body = c.read_lesson(lesson)
        is_build = lesson.endswith("/build")

        n = c.word_count(body)
        if n > MAX_WORDS:
            errors.append(f"{lesson}: {n} words (max {MAX_WORDS})")

        if not is_build:
            for s in SECTIONS:
                if s not in body:
                    errors.append(f"{lesson}: missing section '{s}'")
            qs = c.retrieval_questions(body)
            if len(qs) != 3:
                errors.append(f"{lesson}: {len(qs)} retrieval questions (need exactly 3)")
            frames = re.findall(r'<iframe[^>]+src="([^"]+)"', body)
            if len(frames) != 1:
                errors.append(f"{lesson}: {len(frames)} iframes (need exactly 1)")
            for src in frames:
                target = (c.DOCS / lesson).parent / src
                if not target.resolve().exists():
                    errors.append(f"{lesson}: iframe target not found: {src}")
            if not meta.get("card"):
                warnings.append(f"{lesson}: no 'card:' (canvas card id) in front matter")

        for block in re.findall(r"```.*?\n(.*?)```", body, re.S):
            if block.count("\n") > MAX_CODE_LINES:
                errors.append(f"{lesson}: code block of {block.count(chr(10))} lines (max {MAX_CODE_LINES})")

        for term in meta.get("terms", []):
            if term.lower() not in known:
                errors.append(f"{lesson}: term '{term}' is in front matter but not in glossary/terms.jsonl")
        prose = re.sub(r"```.*?```|`[^`]*`", " ", body, flags=re.S).lower()
        for k in sorted(known, key=len, reverse=True):  # a word inside a defined phrase ("low rank") is covered
            prose = prose.replace(k, " ")
        for w in WATCHLIST:
            if re.search(rf"\b{re.escape(w.lower())}\b", prose) and w.lower() not in known:
                warnings.append(f"{lesson}: uses '{w}' but the glossary has no entry for it")

    for v in sorted((c.DOCS / "visuals").glob("*.html")):
        size = v.stat().st_size
        if size > MAX_VISUAL_BYTES:
            errors.append(f"visuals/{v.name}: {size / 1024:.1f} KB (max 60 KB)")
        text = v.read_text(encoding="utf-8")
        text = text.replace("http://www.w3.org/2000/svg", "")  # XML namespace, not a request
        hit = NETWORK_RE.search(text)
        if hit:
            errors.append(f"visuals/{v.name}: possible network access: '{hit.group(0)}'")
        if 'name="viewport"' not in text:
            errors.append(f"visuals/{v.name}: missing viewport meta tag")

    # Prose holders must never be flex/grid: glossary <abbr>s would become separate boxes and text scatters.
    PROSE = r"(summary|p|li|td|th|h[1-6]|blockquote|\.md-typeset|\.admonition-title)"
    css = (c.DOCS / "stylesheets" / "extra.css").read_text(encoding="utf-8")
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    for selector, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        if re.search(r"display\s*:\s*(inline-)?(flex|grid)", body) and re.search(PROSE + r"\s*(,|$|\s*>?\s*$)", selector.strip()):
            errors.append(f"extra.css: '{selector.strip()}' is flex/grid but holds inline prose (see LESSON_FORMAT.md)")

    for w in warnings:
        print("warn :", w)
    for e in errors:
        print("ERROR:", e)
    n_vis = len(list((c.DOCS / "visuals").glob("*.html")))
    print(f"checked {len(c.lesson_ids())} lessons, {n_vis} visuals: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
