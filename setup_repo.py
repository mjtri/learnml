"""One-time: replace the GH_USER / GH_REPO placeholders everywhere (site URL, repo URL, Colab badges).

    python setup_repo.py <github-user> <repo-name>
"""
from __future__ import annotations

import re
import sys

import lml_common as c

TARGETS = ["mkdocs.yml", "README.md", "docs/**/*.md", "notebooks/*.ipynb"]


def main() -> int:
    if len(sys.argv) != 3 or not all(re.fullmatch(r"[A-Za-z0-9._-]+", a) for a in sys.argv[1:]):
        print(__doc__)
        return 1
    user, repo = sys.argv[1:]
    changed = 0
    for pattern in TARGETS:
        for path in c.ROOT.glob(pattern):
            text = path.read_text(encoding="utf-8")
            new = text.replace("GH_USER", user).replace("GH_REPO", repo)
            if new != text:
                path.write_text(new, encoding="utf-8", newline="\n")
                changed += 1
                print("updated", path.relative_to(c.ROOT))
    print(f"{changed} file(s) updated. Site will be at https://{user}.github.io/{repo}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
