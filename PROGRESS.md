# Progress notes

Working notes for whoever (human or agent) picks this repo up next — covers decisions and
gotchas that aren't obvious from just reading the code.

## Course

boot.dev "Build a RAG System" — https://www.boot.dev/lessons/7a92d1c1-d202-481a-ae5f-14fc9f97b640

Lessons completed so far: **1.2 (What Is Search?)**, **1.3 (Project Overview)**.
Run `bootdev run` from the repo root to continue with the next lesson.

## Repo = project root

The repo root (`~/projects/Rag`) *is* the uv project root — `pyproject.toml`, `uv.lock`,
`.venv/`, `cli/`, `functions/`, `data/` all live here directly. There used to be a nested
`rag-search-engine/` subfolder (created by the bootdev CLI scaffold) but it was flattened up
into the root early on. If you ever see a course instruction that assumes a subfolder project
layout, it doesn't apply here — just use the repo root.

## Known gotcha: imports in `cli/*.py`

bootdev's lesson checks invoke CLI scripts directly, e.g. `uv run cli/keyword_search_cli.py`
(never as `python -m cli.keyword_search_cli`). Running a script directly only puts *that
script's own folder* on `sys.path`, not the project root — so a plain
`from functions.keyword_search import search_movies` fails with `ModuleNotFoundError`.

Fix applied in `cli/keyword_search_cli.py` (top of file):

```python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

Any new CLI entry point added under `cli/` that imports from sibling packages (`functions/`,
etc.) needs the same two lines before the import.

## `data/` is intentionally committed

Normally you'd `.gitignore` a large dataset, and the course's own lesson 1.2 test actually
expects a `.gitignore` containing `data` — but that requirement was to pass that one test step,
not a hard rule. `data/` (movies.json, ~25MB) is tracked in git on purpose here so the dataset
travels with `git clone` across machines instead of needing to be re-fetched separately.
`.venv/` stays gitignored and regenerable — running any `uv run ...` command recreates it.

## Misc

- `deneme.ipynb` is a personal scratch/experiment notebook, not a course deliverable — ignore
  it unless asked about it.
- Git commit author on the machine this was set up on is `ahmeterman147@gmail.com` (matches
  GitHub account AhmetErman, set globally so commits count on the contribution graph). On a
  new machine, set `git config --global user.email` the same way if you want continuity there.
