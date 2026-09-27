"""Quality gate for lessons and visuals. Exit code 1 on any error (warnings do not fail).

    python check_lessons.py                 # everything
    python check_lessons.py --only week-05  # one week's lessons and its w05-* visuals (for generation agents)

Track A (week-NN): <= 800 words, six fixed sections, exactly 3 retrieval questions, exactly one iframe.
Track B (agentic-NN): <= 700 words, its own sections, 3 rules of thumb, 3 retrieval questions, one iframe OR one
worked example, every link to an official product domain carries data-checked="YYYY-MM-DD" (stale after 60 days).
Both: self-paced wording (no Day N titles, no Yesterday/Tomorrow), visuals <= 60 KB with no network access, code
blocks <= 12 lines, front-matter terms exist in the glossary, forward references to later weeks are warned,
no duplicate terms across glossary shards, common jargon is not used undefined, extra.css never makes prose flex/grid.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date

import lml_common as c

MAX_VISUAL_BYTES = 60 * 1024
MAX_CODE_LINES = 12
STALE_DAYS = 60
RULES = {
    "ml": {"max_words": 800, "min_words": 550,
           "sections": ["## Idea", "## Mechanism", "## Try it", "## Retrieval", "## Sources", "## Ledger prompt"]},
    "agentic": {"max_words": 700, "min_words": 450,
                "sections": ["## Idea", "## How it works", "## Try it", "## Rules of thumb", "## Retrieval",
                             "## Sources", "## Ledger prompt"]},
}
# Product claims about these hosts must carry a checked-date stamp (Track B).
OFFICIAL_HOSTS = ("code.claude.com", "docs.claude.com", "docs.anthropic.com", "support.claude.com", "anthropic.com",
                  "claude.com", "claude.ai", "openai.com", "help.openai.com", "platform.openai.com",
                  "developers.openai.com", "learn.chatgpt.com", "chatgpt.com")
NETWORK_RE = re.compile(r"https?://|(?<![:\w])//[a-z0-9.-]+\.[a-z]{2,}|\bfetch\(|XMLHttpRequest|WebSocket|@import|\.src\s*=", re.I)
# Jargon that must never appear in a lesson without a glossary entry. Extend as weeks are added.
WATCHLIST = ["logits", "epoch", "backprop", "backpropagation", "softmax", "embedding", "batch", "loss",
             "gradient", "tensor", "parameter", "weights", "bias", "activation", "optimizer", "overfitting",
             "learning rate", "autograd", "inference", "hyperparameter", "token", "attention", "fine-tuning",
             "checkpoint", "regularization", "normalization", "cross-entropy", "LoRA", "rank",
             "context window", "compaction", "subagent", "MCP", "worktree", "sandbox",
             "usage credits", "prompt cache", "CLAUDE.md", "AGENTS.md", "plan mode", "permission mode",
             "dropout", "residual", "LayerNorm", "BPE", "tokenizer", "positional encoding", "causal mask",
             "query vector", "key vector", "value vector", "temperature", "perplexity", "InfoNCE", "contrastive", "zero-shot",
             "linear probe", "bootstrap", "standard error", "ablation", "baseline", "seed", "VAE", "ELBO"]
DAY_WORDS_RE = re.compile(r"\*\*(Yesterday|Tomorrow)[^*]*\*\*|\bYesterday's\b|\bTomorrow's\b|^# (B\d · )?Day \d", re.M)


def visual_prefix(week_dir: str) -> str:
    n = c.week_of(week_dir + "/x")
    return f"w{n:02d}-" if c.track_of(week_dir + "/x") == "ml" else f"b{n}-"


def check_stamps(lesson: str, body: str, errors: list, warnings: list) -> None:
    """Track B: [text](https://official/...){ .src data-checked="YYYY-MM-DD" }."""
    today = date.fromisoformat(c.today_kst())
    for m in re.finditer(r"\]\((https?://[^)\s]+)\)(\{[^}]*\})?", body):
        url, attrs = m.group(1), m.group(2) or ""
        host = re.sub(r"^https?://(www\.)?", "", url).split("/")[0]
        official = any(host == h or host.endswith("." + h) for h in OFFICIAL_HOSTS)
        stamp = re.search(r'data-checked="(\d{4}-\d{2}-\d{2})"', attrs)
        if official and not stamp:
            errors.append(f"{lesson}: official link without data-checked stamp: {url}")
        if stamp:
            d = date.fromisoformat(stamp.group(1))
            if d > today:
                errors.append(f"{lesson}: stamp {stamp.group(1)} is in the future: {url}")
            elif (today - d).days > STALE_DAYS:
                warnings.append(f"{lesson}: stamp {stamp.group(1)} is {(today - d).days} days old: {url} (run gen_refresh.py)")
    for line in body.splitlines():
        if "(unverified)" in line and any(h in line for h in OFFICIAL_HOSTS):
            errors.append(f"{lesson}: '(unverified)' on a line citing an official source: {line.strip()[:80]}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="week dir, e.g. week-05 or agentic-3 (restricts lessons and visuals)")
    a = ap.parse_args()
    only = a.only.replace("agentic-", "agentic-0") if a.only and re.fullmatch(r"agentic-\d", a.only) else a.only

    errors, warnings = [], []
    all_ids = c.lesson_ids()
    ids = [l for l in all_ids if not only or l.startswith(only + "/")]
    if only and not ids:
        print(f"no lessons found under docs/{only}/")
        return 1

    # Glossary: shards, duplicates, definition length, ownership
    terms = c.load_terms()
    known: dict[str, dict] = {}
    for e in terms:
        for t in [e["term"], *e.get("aliases", [])]:
            k = t.lower()
            if k in known and known[k]["term"] != e["term"]:
                errors.append(f"glossary: '{t}' defined twice ({known[k]['shard']} as '{known[k]['term']}' and {e['shard']} as '{e['term']}')")
            known.setdefault(k, e)
        if len(e["def"].split()) > 30:
            warnings.append(f"glossary: '{e['term']}' definition is {len(e['def'].split())} words (> 30)")
        if e.get("lesson") and e["lesson"] not in all_ids and (not only or e["lesson"].startswith(only + "/")):
            errors.append(f"glossary: '{e['term']}' points at missing lesson {e['lesson']}")
        if e.get("lesson") and e["shard"] != f"terms-{e['lesson'].split('/')[0]}.jsonl":
            errors.append(f"glossary: '{e['term']}' (lesson {e['lesson']}) must live in terms-{e['lesson'].split('/')[0]}.jsonl, not {e['shard']}")

    for lesson in ids:
        track = c.track_of(lesson)
        rules = RULES[track]
        meta, body = c.read_lesson(lesson)
        is_long = lesson.endswith("/" + c.TRACKS[track]["long"])

        n = c.word_count(body)
        if n > rules["max_words"]:
            errors.append(f"{lesson}: {n} words (max {rules['max_words']})")
        elif not is_long and n < rules["min_words"]:
            warnings.append(f"{lesson}: only {n} words (floor {rules['min_words']}); is it thin?")

        m = DAY_WORDS_RE.search(body)
        if m:
            errors.append(f"{lesson}: calendar wording '{m.group(0).strip()[:40]}' (self-paced: use Lesson N / Previously / Next)")
        if not is_long and "**Previously:**" not in body:
            errors.append(f"{lesson}: recall line must start with **Previously:**")
        if is_long and "**This week in one sentence:**" not in body:
            errors.append(f"{lesson}: build/apply page needs a **This week in one sentence:** recall line")

        if not is_long:
            for s in rules["sections"]:
                if s not in body:
                    errors.append(f"{lesson}: missing section '{s}'")
            qs = c.retrieval_questions(body)
            if len(qs) != 3:
                errors.append(f"{lesson}: {len(qs)} retrieval questions (need exactly 3)")
            frames = re.findall(r'<iframe[^>]+src="([^"]+)"', body)
            examples = len(re.findall(r"^### Worked example", body, re.M))
            if track == "ml" and len(frames) < 1:
                errors.append(f"{lesson}: needs at least one iframe visual")
            if track == "ml" and len(frames) > 2:
                errors.append(f"{lesson}: {len(frames)} iframes (max 2)")
            if track == "agentic" and len(frames) + examples != 1:
                errors.append(f"{lesson}: needs exactly one iframe or one '### Worked example' (found {len(frames)} + {examples})")
            for src in frames:
                target = (c.DOCS / lesson).parent / src
                if not target.resolve().exists():
                    errors.append(f"{lesson}: iframe target not found: {src}")
                elif not target.name.startswith(visual_prefix(lesson.split("/")[0])):
                    errors.append(f"{lesson}: visual {target.name} must be prefixed {visual_prefix(lesson.split('/')[0])}")
            if "**Next:**" not in body:
                errors.append(f"{lesson}: missing **Next:** teaser")
            if track == "ml" and not meta.get("card"):
                warnings.append(f"{lesson}: no 'card:' (canvas card id) in front matter")
            if track == "agentic":
                rot = re.search(r"## Rules of thumb\s*\n((?:- .*\n?)+)", body)
                if not rot or len(re.findall(r"^- ", rot.group(1), re.M)) != 3:
                    errors.append(f"{lesson}: '## Rules of thumb' needs exactly 3 bullets")
                if "**Phone:**" not in body or "**Laptop:**" not in body:
                    errors.append(f"{lesson}: 'Try it' needs both a **Phone:** and a **Laptop:** variant")
        if track == "agentic":
            check_stamps(lesson, body, errors, warnings)

        for block in re.findall(r"```.*?\n(.*?)```", body, re.S):
            if block.count("\n") > MAX_CODE_LINES:
                errors.append(f"{lesson}: code block of {block.count(chr(10))} lines (max {MAX_CODE_LINES})")

        for term in meta.get("terms", []):
            e = known.get(term.lower())
            if not e:
                errors.append(f"{lesson}: term '{term}' is in front matter but not in any glossary shard")
            elif e.get("lesson") != lesson:
                errors.append(f"{lesson}: front matter introduces '{term}' but the glossary says lesson {e.get('lesson') or '(core)'}")

        # Term ordering: a lesson may use only terms introduced at or before it (same track); cross-track is a warning.
        prose = re.sub(r"```.*?```|`[^`]*`", " ", body, flags=re.S).lower()
        pos = c.lesson_index(lesson)
        for k in sorted(known, key=len, reverse=True):
            if not re.search(rf"\b{re.escape(k)}\b", prose):
                continue
            e = known[k]
            if e.get("lesson"):
                epos = c.lesson_index(e["lesson"])
                # Same-week forward use is fine (tap-to-define covers it); a later WEEK is a real forward reference.
                if epos[0] == pos[0] and epos[1] > pos[1]:
                    # A tooltip on a term met early helps the reader; flag it so authors keep such mentions light.
                    warnings.append(f"{lesson}: uses '{k}' before it is introduced in {e['lesson']} (forward reference)")
                elif epos[0] != pos[0] and epos[1] > 1 and pos[1] < epos[1]:
                    warnings.append(f"{lesson}: uses '{k}', introduced later in the other track ({e['lesson']})")
            prose = re.sub(rf"\b{re.escape(k)}\b", " ", prose)
        for w in WATCHLIST:
            if re.search(rf"\b{re.escape(w.lower())}\b", prose) and w.lower() not in known:
                warnings.append(f"{lesson}: uses '{w}' but the glossary has no entry for it")

    vis_glob = f"{visual_prefix(only)}*.html" if only else "*.html"
    for v in sorted((c.DOCS / "visuals").glob(vis_glob)):
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
        if "learnmlHeight" not in text:
            errors.append(f"visuals/{v.name}: missing the theme/height boilerplate (learnmlHeight postMessage)")
        if "Words used here" not in text:
            warnings.append(f"visuals/{v.name}: no 'Words used here' block")
        if not re.match(r"[wb]\d+-", v.name):
            errors.append(f"visuals/{v.name}: filename must be prefixed wNN- or bN-")

    if not only:
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
    n_vis = len(list((c.DOCS / "visuals").glob(vis_glob)))
    print(f"checked {len(ids)} lessons, {n_vis} visuals: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
